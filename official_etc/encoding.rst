General usage
=============

::

  mpv infile -o outfile [-of outfileformat] [-ofopts formatoptions] [-orawts] \
    [(any other mpv options)] \
    -ovc outvideocodec [-ovcopts outvideocodecoptions] \
    -oac outaudiocodec [-oacopts outaudiocodecoptions]

如果将 help 作为参数，则提供这些选项的帮助，如::

  mpv -ovc help

这些选项的子选项通常与ffmpeg的相同（因为选项解析被简单地委托给ffmpeg）。选项 -ocopyts 可以从源文件中原封不动地复制时间戳，而不是修复它们以匹配音频播放时间（注意：这并不适用于所有的输出容器格式）； -orawts 甚至可以关闭不连续修复功能。

注意，如果既没有指定 -ofps 也没有指定 -oautofps ，就会假定VFR编码，时间基准是24000fps。 -oautofps 将 -ofps 设置为输入视频中的一个猜测的fps数字。注意，并不是所有的编解码器和所有的格式都支持VFR编码，一些支持VFR编码的格式在指定目标比特率时有错误——在这些情况下，使用 -ofps 或 -oautofps 来强制进行CFR编码。

当然，这些选项可以存储在一个配置文件中，像这样的 .config/mpv/mpv.conf 部分::

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

也可以把默认的编码选项放在名为 ``[encoding]`` 的部分来定义它们。（在mpv 0.3.x中，默认部分/无部分的配置选项被应用于编码，现在不是这样了。）

然后我们可以用这个配置文件进行编码，命令是::

  mpv infile -o outfile.mp4 -profile myencprofile

在文件 etc/encoding-profiles.conf 中提供了一些配置文件的例子；至于这个，见下文。


Encoding examples
=================

这些是一些编码目标的例子，这段代码已经被使用和测试。

典型的MPEG-4第二部分（"ASP"，"DivX"）编码，AVI容器::

  mpv infile -o outfile.avi \
    --vf=fps=25 \
    -ovc mpeg4 -ovcopts qscale=4 \
    -oac libmp3lame -oacopts ab=128k

注意：AVI不支持可变帧率，所以必须使用fps过滤器。帧率最好与输入相匹配（PAL为25，NTSC为24000/1001或30000/1001）。

典型的MPEG-4 Part 10（"AVC"，"H.264"）编码，Matroska（MKV）容器::

  mpv infile -o outfile.mkv \
    -ovc libx264 -ovcopts preset=medium,crf=23,profile=baseline \
    -oac libvorbis -oacopts qscale=3

典型的MPEG-4 Part 10（"AVC"，"H.264"）编码，MPEG-4（MP4）容器::

  mpv infile -o outfile.mp4 \
    -ovc libx264 -ovcopts preset=medium,crf=23,profile=baseline \
    -oac aac -oacopts ab=128k

典型的VP8编码，WebM（限制Matroska）容器::

  mpv infile -o outfile.mkv \
    -of webm \
    -ovc libvpx -ovcopts qmin=6,b=1000000k \
    -oac libvorbis -oacopts qscale=3


Device targets
==============

由于各种设备的选项可能会变得复杂，因此可以使用配置文件。

源代码树中的 etc/encoding-profiles.conf 提供了一个编码配置文件的例子。这个文件是默认安装和加载的。如果你想修改它，你可以用你自己的副本替换它，方法是::

  mkdir -p ~/.mpv
  cp /etc/mpv/encoding-profiles.conf ~/.mpv/encoding-profiles.conf

请记住，默认的配置文件是用于播放的。如果你想添加只适用于编码模式的选项，把它们放到 ``[encoding]`` 部分。

更多的注释请参考该文件的顶部——简而言之，以下选项是由它添加的::

  -profile enc-to-dvdpal      DVD-Video PAL, use dvdauthor -v pal+4:3 -a ac3+en
  -profile enc-to-dvdntsc     DVD-Video NTSC, use dvdauthor -v ntsc+4:3 -a ac3+en
  -profile enc-to-bb-9000     MP4 for Blackberry Bold 9000
  -profile enc-to-nok-6300    3GP for Nokia 6300
  -profile enc-to-psp         MP4 for PlayStation Portable
  -profile enc-to-iphone      MP4 for iPhone
  -profile enc-to-iphone-4    MP4 for iPhone 4 (double res)
  -profile enc-to-iphone-5    MP4 for iPhone 5 (even larger res)

你可以用这些命令行进行编码，如::

  mpv infile -o outfile.mp4 -profile enc-to-bb-9000

当然，你可以通过在 -profile 选项后指定覆盖这些配置文件设置的选项。


What works
==========

* 以可变帧率编码（默认）。
* 使用 --vf=fps=RATE 以恒定的帧率进行编码
* 2-pass编码（在第一遍的 -ovcopts 中指定 flags=+pass1 ，在第二遍中指定 flags=+pass2 ）
* 使用vobsub、ass或srt字幕渲染的硬编码字幕(只需像往常一样为字幕配置mpv)
* 硬编码任何其他mpv OSD（例如时间码，使用 -osdlevel 3 和 -vf expand=::::1 ）
* 直接从DVD、网络流、网络摄像头或任何其他支持mpv的来源进行编码
* 使用x264预设/调谐/配置（通过在 -ovcopts 中使用 profile=, tune=, preset= ）
* 使用mpv的任何过滤器进行去隔行/反转扫描。
* 音频文件转换： mpv -o outfile.mp3 infile.flac -no-video -oac libmp3lame -oacopts ab=320k

What does not work yet
======================

* 3-pass 编码（确保总体积和比特率限制不变，同时拥有VBR音频；mencoder称之为 "frameno")
* 直接流复制
