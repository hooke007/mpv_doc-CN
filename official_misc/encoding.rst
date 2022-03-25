编码/压制的详细指南
###################

一般用法
========

::

  mpv infile --o=outfile [--of=outfileformat] [--ofopts=formatoptions] [--orawts] \
    [(any other mpv options)] \
    --ovc=outvideocodec [--ovcopts=outvideocodecoptions] \
    --oac=outaudiocodec [--oacopts=outaudiocodecoptions]

如果将 ``help`` 作为参数，则提供这些选项的帮助，比如::

  mpv --ovc=help

这些选项的子选项通常与ffmpeg中的相同（因为选项解析被简单地委派给ffmpeg）。选项 ``--ocopyts`` 启用从源文件中原样的复制时间戳，而不是修正它们以匹配音频播放时间（注意：这并不适用于所有的输出容器格式）； ``--orawts`` 甚至可以关闭不连续性修正。

注意，如果既没有指定 ``--ofps`` 也没有指定 ``--oautofps`` ，就会假定进行VFR编码，时间基准是24000fps。 ``--oautofps`` 将 ``--ofps`` 设置为一个从输入视频中的猜测的fps数。注意，并非所有的编码和格式都支持压制VFR，一些支持的格式在指定目标比特率时会存在错误 —— 在这些情况下，使用 ``--ofps`` 或 ``--oautofps`` 来强制进行CFR编码。

当然，这些选项可以存储在一个配置预设中，像这样的 .config/mpv/mpv.conf 中的部分::

  [myencprofile]
  vf-add = scale=480:-2
  ovc = libx264
  ovcopts-add = preset=medium
  ovcopts-add = tune=fastdecode
  ovcopts-add = crf=23
  ovcopts-add = maxrate=1500k
  ovcopts-add = bufsize=1000k
  ovcopts-add = rc_init_occupancy=900k
  ovcopts-add = refs=2
  ovcopts-add = profile=baseline
  oac = aac
  oacopts-add = b=96k

也可以把它们放进名为 ``[encoding]`` 的部分来定义默认的压制选项。（此行为在mpv0.3.x之后改变过。在mpv0.3.x中， ``[default]`` 部分/没有任何部分的设置选项被应用于编码。现在已经不是这样了。）

然后可以使用以下命令使用该配置预设进行编码::

  mpv infile --o=outfile.mp4 --profile=myencprofile

在官方仓库的文件 etc/encoding-profiles.conf 中提供了一些配置预设的示例；至于这一点，参见下文。


压制示例
========

这些是一些编码目标的示例，这段代码已被使用和测试过。

压制典型的MPEG-4 Part 2 ("ASP", "DivX") ，AVI容器::

  mpv infile --o=outfile.avi \
    --vf=fps=25 \
    --ovc=mpeg4 --ovcopts=qscale=4 \
    --oac=libmp3lame --oacopts=ab=128k

注意：AVI不支持可变帧率，所以必须使用fps滤镜。帧率最好与输入相匹配（PAL为25，NTSC为24000/1001或30000/1001）。

压制典型的MPEG-4 Part 10 ("AVC", "H.264") ，Matroska (MKV) 容器::

  mpv infile --o=outfile.mkv \
    --ovc=libx264 --ovcopts=preset=medium,crf=23,profile=baseline \
    --oac=libvorbis --oacopts=qscale=3

压制典型的MPEG-4 Part 10 ("AVC", "H.264") ，MPEG-4 (MP4) 容器::

  mpv infile --o=outfile.mp4 \
    --ovc=libx264 --ovcopts=preset=medium,crf=23,profile=baseline \
    --oac=aac --oacopts=ab=128k

压制典型的VP8，WebM (受限制的Matroska) 容器::

  mpv infile --o=outfile.mkv \
    --of=webm \
    --ovc=libvpx --ovcopts=qmin=6,b=1000000k \
    --oac=libvorbis --oacopts=qscale=3


设备目标
========

由于各种设备的选项可能会变得复杂，因此可以使用配置预设。

源代码树中的 etc/encoding-profiles.conf 提供了一个压制的配置预设的示例。这个文件是默认被安装和加载的。如果你想修改它，你可以用你自己的副本替换它，通过如下操作::

  mkdir -p ~/.mpv
  cp /etc/mpv/encoding-profiles.conf ~/.mpv/encoding-profiles.conf

请记住， ``[default]`` 的配置预设是用于播放的。如果你想添加只应用于编码模式的选项，把它们放入 ``[encoding]`` 的部分。

更多的注释请参考该文件的顶部 —— 简而言之，下列选项是由它添加的::

  --profile=enc-to-dvdpal      DVD-Video PAL, use dvdauthor -v pal+4:3 -a ac3+en
  --profile=enc-to-dvdntsc     DVD-Video NTSC, use dvdauthor -v ntsc+4:3 -a ac3+en
  --profile=enc-to-bb-9000     MP4 for Blackberry Bold 9000
  --profile=enc-to-nok-6300    3GP for Nokia 6300
  --profile=enc-to-psp         MP4 for PlayStation Portable
  --profile=enc-to-iphone      MP4 for iPhone
  --profile=enc-to-iphone-4    MP4 for iPhone 4 (double res)
  --profile=enc-to-iphone-5    MP4 for iPhone 5 (even larger res)

你可以用这些命令行进行压制，比如::

  mpv infile --o=outfile.mp4 --profile=enc-to-bb-9000

当然，你可以通过在 ``--profile`` 后面指定其它选项，来覆盖这些配置预设设置的选项。


可用的功能
==========

* 以可变帧率进行编码（默认）
* 使用 --vf=fps=RATE 以恒定的帧率进行编码
* 2-pass压制（在第一遍的 ``--ovcopts`` 中指定 flags=+pass1 ，在第二遍中指定 flags=+pass2 ）
* 使用vobsub、ass或srt字幕渲染的硬编码字幕（只需像通常一样为设置mpv的字幕相关选项）
* 硬编码任何其他mpv OSD（例如时间码，使用 ``--osdlevel=3`` 和 ``--vf=expand=::::1`` ）
* 直接从DVD、网络流、网络摄像头或任何其它mpv支持的来源进行编码
* 使用x264预设/调节/profiles（通过在 ``--ovcopts`` 中使用 profile=, tune=, preset= ）
* 使用mpv的任何用于去隔行/反交错的滤镜
* 音频文件转换： ``mpv --o=outfile.mp3 infile.flac --no-video --oac=libmp3lame --oacopts=ab=320k``

尚不可用的功能
==============

* 3-pass压制（确保总体积和比特率限制不变，同时拥有VBR音频；mencoder称之为"frameno"）
* 直接复制流
