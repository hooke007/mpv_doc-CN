CHANGES FROM OTHER VERSIONS OF MPLAYER
======================================

**mpv** 基于mplayer2，而mplayer2又是基于最初的MPlayer（也叫mplayer、mplayer-svn、mplayer1）。已经做了许多改变，其中很大一部分是不兼容的，或者完全改变了玩家的行为方式。尽管与它的祖先仍有许多相似之处，但 **mpv** 一般应被视为一个完全不同的程序。

.. admonition:: 警告

    此文档已 **不再更新** ，而且是 **不完整的** 和 **过时的** 。如果你要寻找旧的选项替换，一定要检查当前的mpv手册，因为与此同时，选项可能已经改变。

General Changes from MPlayer to mpv
-----------------------------------

这个列表是关于mplayer2和mpv相对于MPlayer的变化。

Player
~~~~~~

* 二进制文件的新名称（ ``mpv`` ）。配置文件的新位置( ``~/.config/mpv/mpv.conf`` ，或者如果你想的话， ``~/.mpv/config`` )。
* 编码功能（替代MEncoder，见 `ENCODING`_ 部分）。
* 支持Lua脚本（见 `LUA SCRIPTING`_ 部分）。
* 更好的暂停处理（例如，不在命令中取消暂停）。
* 精确搜索的支持。
* 改进了音频/视频同步处理。
* 在同一播放器实例中播放新文件时不会丢失设置。
* 破坏了从属模式的兼容性（见下文）。
* 在播放器暂停时重新启用屏保。
* 允许用 ``Shift+q`` 在稍后的时间点恢复播放，也可以看到 ``quit-watch-later`` 输入命令。
* ``--keep-open`` 选项，阻止播放器在播放结束后关闭窗口并退出。
* 一个客户端API，允许将 **mpv** 嵌入到应用程序中（见源代码中的 ``libmpv/client.h`` ）。

Input
~~~~~

* 改进了默认的键位绑定。MPlayer的绑定也是可用的（见源代码树中的 ``etc/mplayer-input.conf`` ）
* 改进了对用户输入的响应速度。
* 在input.conf中支持修饰键（alt, shift, ctrl）。
* 允许自定义搜索的按键绑定是否显示视频时间、OSD栏或什么都不显示（见 `Input Command Prefixes`_ 部分）。
* 支持将多个命令映射到一个按键上。
* 删除了对经典LIRC的支持。安装遥控器作为输入设备。这样他们将发送X11键事件到mpv窗口，可以用普通的 ``input.conf`` 来绑定。也请看： https://github.com/mpv-player/mpv/wiki/IR-remotes
* Joystick支持被删除。它被认为是无用的，是导致一些问题的原因（例如，笔记本的加速器被识别为操纵杆）。
* 支持按百分比的相对搜索。

Audio
~~~~~

* 支持无间隙音频（见 ``--gapless-audio`` 选项）。
* 支持OSS4音量控制。
* 改进对PulseAudio的支持。
* 使 ``--softvol`` 默认（ **mpv** 不是混音器控制面板）。
* 默认情况下，如果播放速度增加，做音高校正。
* 改进了环绕声的降频和输出。

  - 不使用硬编码的pan滤波器来做混音，而是使用libavresample
  - 通道图用于识别通道布局，因此，例如， ``3.0`` 和 ``2.1`` 音频可以被区分。

Video
~~~~~

* Wayland支持。
* 对VAAPI和VDA的原生支持。改进VDPAU视频输出。
* 改进了GPU加速的视频输出（见 ``gpu-hq`` 预设）。
* 使硬件解码与 ``gpu`` 视频输出一起工作。
* 支持libavfilter（用于视频->视频和音频->音频）。这允许使用FFmpeg的大部分过滤器，这些过滤器在功能、性能和正确性方面比旧的MPlayer过滤器有很大的改进。
* 更正确的色彩再现（色彩矩阵生成），包括支持BT.2020（超高清）、线性XYZ（数字影院）和SMPTE ST2084（HDR）输入。
* 支持显示器色彩管理，通过ICC配置文件。
* 高质量的图像缩放器（见 ``--scale`` 子选项）。
* 支持在（sigmoidized）线性光下的缩放。
* 默认使用libass进行更好的字幕渲染。
* 播放多个文件时的改进（ ``-fixed-vo`` 是默认的，播放新文件时不要默认重置设置）。
* 用 ``--vo=image`` 取代图像视频输出（ ``--vo=jpeg`` 等）。
* 移除 ``--vo=gif89a``, ``--vo=md5sum``, ``--vo=yuv4mpeg`` , 因为编码可以处理这些使用情况。例如，对于yuv4mpeg，使用::

    mpv input.mkv -o output.y4m --no-audio --oautofps --oneverdrop

* 图像字幕（DVD等）以彩色呈现，并使用更正确的定位（图像字幕的颜色可以用 ``--sub-gray`` 禁用）。
* 对X11视频输出的支持被移除，因为它被认为是废弃的。SDL视频输出仍可作为后备方案使用。

OSD and terminal
~~~~~~~~~~~~~~~~

* 清理了终端输出：更漂亮的状态线，更少的无用噪音。
* 改进了使用libass的OSD渲染，完全支持Unicode。
* 新的OSD栏有章节标记。不在视频的中间位置（可以用 ``--osd-bar-align-y`` 选项自定义）。
* 在OSD上显示章节和音频/副标题轨道的列表（见 `Properties`_ 部分）。

Screenshots
~~~~~~~~~~~

* 即时屏幕截图，没有1帧延迟。
* 支持使用硬件解码进行截图。
* 支持将屏幕截图保存为JPEG或PNG格式。
* 支持可配置的文件名。
* 支持带或不带字幕的屏幕截图。

请注意，不再需要 ``screenshot`` 视频过滤器，也不应该放在mpv配置文件中。

Miscellaneous
~~~~~~~~~~~~~

* 更好的MKV支持（例如，有序的章节，3D元数据）。
* 在运行时切换 Matroska edition
* 支持直接播放流行流媒体网站的URL。(例如： ``mpv https://www.youtube.com/watch?v=...`` ）。需要安装最新版本的 ``youtube-dl`` 。可以在mpv配置文件中用 ``ytdl=no`` 来禁用。
* 支持精确滚动，它可以缩放命令的参数。如果输入不支持精确滚动，缩放系数保持为1。
* 允许在运行时改变/调整视频过滤器。(如果不支持去隔行扫描，这也用于使 ``D`` 键插入vf_yadif）。
* 改进了对.cue文件的支持。

Mac OS X
~~~~~~~~

* 原生OpenGL后端。
* Cocoa事件循环独立于MPlayer的事件循环，因此用户的操作，如访问菜单和实时调整大小，不会阻碍播放。
* 支持媒体键。
* 支持VDA，使用libavcodec hwaccel API代替FFmpeg的解码器，CPU使用率降低2-2.5倍。

Windows
~~~~~~~

* 改进了对Unicode文件名的支持。
* 改进了窗口处理。
* 移动窗口时不阻断播放。
* 改进了Direct3D视频输出。
* 增加了WASAPI音频输出。

Internal changes
~~~~~~~~~~~~~~~~

* 切换到GPLv2+（详见 ``Copyright`` 文件）。
* 删除了大量的垃圾：

  - 内部GUI（由OSC取代，见 `ON SCREEN CONTROLLER`_ 部分）。
  - MEncoder (由本地编码取代，见 `ENCODING`_ 部分)。
  - OSD菜单。
  - Linux 2.4的内核视频驱动（包括VIDIX）。
  - 支持Teletext。
  - 对废弃平台的支持。
  - 大多数内置的解复用器已经被libavformat的同类产品所取代。
  - 内置的网络支持已经被 libavformat 的支持所取代（它也支持 https URLs）。
  - 嵌入式库的副本（如FFmpeg）。

* 通用代码清理（包括许多部分的重构或重写）。
* 新的构建系统。
* 许多错误的修正和长期存在的问题的删除。
* 一般来说，比起内部解复用器、解码器和过滤器，更喜欢FFmpeg/Libav。

Detailed Listing of User-visible Changes
----------------------------------------

这个列表是关于改变的命令行开关、从属命令和类似的东西。完全删除的功能没有列出。

Command Line Switches
~~~~~~~~~~~~~~~~~~~~~

* 有一种新的命令行语法，通常比旧的语法更受欢迎。 ``-optname optvalue`` 变成 ``--optname=optvalue``

  旧的语法将不会被删除。然而，新的语法在所有的文档等中都有提及，而且与旧的语法不同，它并不含糊，所以了解这一变化是件好事。
* 一般来说，像 ``-noopt`` 这样的否定开关现在必须写成 ``-no-opt`` 或 ``--no-opt``
* 每个文件的选项不再是默认的了。你可以明确指定文件的本地选项。参见 ``Usage`` 部分。
* 许多选项被重新命名、删除或改变了语义。一些使用MPlayer获得良好播放体验所需的选项现在是多余的，甚至比默认值更差，所以在尝试使用你现有的配置于 **mpv** 之前，请确保阅读手册。
* 重新命名/替换的开关表：

    =========================== ========================================
    Old                         New
    =========================== ========================================
    ``-no<opt>``                ``--no-<opt>`` (add a dash)
    ``-a52drc level``           ``--ad-lavc-ac3drc=level``
    ``-ac spdifac3``            ``--ad=spdif:ac3`` (see ``--ad=help``)
    ``-af volnorm``             (removed; use acompressor ffmpeg filter instead)
    ``-afm hwac3``              ``--ad=spdif:ac3,spdif:dts``
    ``-ao alsa:device=hw=0.3``  ``--ao=alsa:device=[hw:0,3]``
    ``-aspect``                 ``--video-aspect``
    ``-ass-bottom-margin``      ``--vf=sub=bottom:top``
    ``-ass``                    ``--sub-ass``
    ``-audiofile-cache``        (removed; the main cache settings are used)
    ``-audiofile``              ``--audio-file``
    ``-benchmark``              ``--untimed`` (no stats)
    ``-capture``                ``--stream-capture=<filename>``
    ``-channels``               ``--audio-channels`` (changed semantics)
    ``-cursor-autohide-delay``  ``--cursor-autohide``
    ``-delay``                  ``--audio-delay``
    ``-dumpstream``             ``--stream-dump=<filename>``
    ``-dvdangle``               ``--dvd-angle``
    ``-endpos``                 ``--length``
    ``-fixed-vo``               (removed; always the default)
    ``-font``                   ``--osd-font``
    ``-forcedsubsonly``         ``--sub-forced-only``
    ``-forceidx``               ``--index``
    ``-format``                 ``--audio-format``
    ``-fsmode-dontuse``         (removed)
    ``-fstype``                 ``--x11-netwm`` (changed semantics)
    ``-hardframedrop``          ``--framedrop=hard``
    ``-identify``               (removed; use TOOLS/mpv_identify.sh)
    ``-idx``                    ``--index``
    ``-lavdopts ...``           ``--vd-lavc-...``
    ``-lavfdopts``              ``--demuxer-lavf-...``
    ``-loop 0``                 ``--loop=inf``
    ``-mixer-channel``          AO suboptions (``alsa``, ``oss``)
    ``-mixer``                  AO suboptions (``alsa``, ``oss``)
    ``-mouse-movements``        ``--input-cursor``
    ``-msgcolor``               ``--msg-color``
    ``-msglevel``               ``--msg-level`` (changed semantics)
    ``-msgmodule``              ``--msg-module``
    ``-name``                   ``--x11-name``
    ``-noar``                   ``(removed; replaced by MediaPlayer framework)``
    ``-noautosub``              ``--no-sub-auto``
    ``-noconsolecontrols``      ``--no-input-terminal``
    ``-nosound``                ``--no-audio``
    ``-osdlevel``               ``--osd-level``
    ``-panscanrange``           ``--video-zoom``, ``--video-pan-x/y``
    ``-playing-msg``            ``--term-playing-msg``
    ``-pp ...``                 ``'--vf=lavfi=[pp=...]'``
    ``-pphelp``                 (See FFmpeg libavfilter documentation.)
    ``-rawaudio ...``           ``--demuxer-rawaudio-...``
    ``-rawvideo ...``           ``--demuxer-rawvideo-...``
    ``-spugauss``               ``--sub-gauss``
    ``-srate``                  ``--audio-samplerate``
    ``-ss``                     ``--start``
    ``-ssf <sub>``              ``--sws-...``
    ``-stop-xscreensaver``      ``--stop-screensaver``
    ``-sub-fuzziness``          ``--sub-auto``
    ``-sub-text-*``             ``--sub-*``
    ``-sub``                    ``--sub-file``
    ``-subcp``                  ``--sub-codepage``
    ``-subdelay``               ``--sub-delay``
    ``-subfile``                ``--sub-file``
    ``-subfont-*``              ``--sub-*``, ``--osd-*``
    ``-subfont-text-scale``     ``--sub-scale``
    ``-subfont``                ``--sub-font``
    ``-subfps``                 ``--sub-fps``
    ``-subpos``                 ``--sub-pos``
    ``-sws``                    ``--sws-scaler``
    ``-tvscan``                 ``--tv-scan``
    ``-use-filename-title``     ``--title='${filename}'``
    ``-vc ffh264vdpau`` (etc.)  ``--hwdec=vdpau``
    ``-vobsub``                 ``--sub-file`` (pass the .idx file)
    ``-x W``, ``-y H``          ``--geometry=WxH`` + ``--no-keepaspect``
    ``-xineramascreen``         ``--screen`` (different values)
    ``-xy W``                   ``--autofit=W``
    ``-zoom``                   Inverse available as ``--video-unscaled``
    ``dvdnav://``               Removed.
    ``dvd://1``                 ``dvd://0`` (0-based offset)
    =========================== ========================================

.. note::

    ``-opt val`` 变成 ``--opt=val``

.. note::

    很多视频过滤器、视频输出、音频过滤器、音频输出的选项解析都有变化。这些在上面的表格中没有提到。

    另外，一些视频和音频过滤器已经被移除，你必须使用libavfilter（使用 ``--vf=lavfi=[...]`` 或 ``--af=lavfi=[...]`` ）来取回它们。

input.conf and Slave Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 重命名的输入命令表：

    这只列出了那些不总是被内部遗留翻译层优雅地处理的命令。如果一个 input.conf 包含任何遗留命令，在启动播放器时将打印一个警告。这些警告也会显示替换的命令。

    含有 ``_`` 的属性用来分隔单词，使用 ``-`` 代替。

    +--------------------------------+----------------------------------------+
    | Old                            | New                                    |
    +================================+========================================+
    | ``pt_step 1 [0|1]``            | ``playlist-next [weak|force]``         |
    |                                | (translation layer cannot deal with    |
    |                                | whitespace)                            |
    +--------------------------------+----------------------------------------+
    | ``pt_step -1 [0|1]``           | ``playlist-prev [weak|force] (same)``  |
    +--------------------------------+----------------------------------------+
    | ``switch_ratio [<ratio>]``     | ``set video-aspect <ratio>``           |
    |                                |                                        |
    |                                | ``set video-aspect 0`` (reset aspect)  |
    +--------------------------------+----------------------------------------+
    | ``step_property_osd <prop>``   | ``cycle <prop> <step>`` (wraps),       |
    | ``<step> <dir>``               | ``add <prop> <step>`` (clamps).        |
    |                                | ``<dir>`` parameter unsupported. Use   |
    |                                | a negative ``<step>`` instead.         |
    +--------------------------------+----------------------------------------+
    | ``step_property <prop>``       | Prefix ``cycle`` or ``add`` with       |
    | ``<step> <dir>``               | ``no-osd``: ``no-osd cycle <prop>``    |
    |                                | ``<step>``                             |
    +--------------------------------+----------------------------------------+
    | ``osd_show_property_text``     | ``show-text <text>``                   |
    | ``<text>``                     | The property expansion format string   |
    |                                | syntax slightly changed.               |
    +--------------------------------+----------------------------------------+
    | ``osd_show_text``              | Now does the same as                   |
    |                                | ``osd_show_property_text``. Use the    |
    |                                | ``raw`` prefix to disable property     |
    |                                | expansion.                             |
    +--------------------------------+----------------------------------------+
    | ``show_tracks``                | ``show-text ${track-list}``            |
    +--------------------------------+----------------------------------------+
    | ``show_chapters``              | ``show-text ${chapter-list}``          |
    +--------------------------------+----------------------------------------+
    | ``af_switch``, ``af_add``, ... | ``af set|add|...``                     |
    +--------------------------------+----------------------------------------+
    | ``tv_start_scan``              | ``set tv-scan yes``                    |
    +--------------------------------+----------------------------------------+
    | ``tv_set_channel <val>``       | ``set tv-channel <val>``               |
    +--------------------------------+----------------------------------------+
    | ``tv_step_channel``            | ``cycle tv-channel``                   |
    +--------------------------------+----------------------------------------+
    | ``dvb_set_channel <v1> <v2>``  | ``set dvb-channel <v1>-<v2>``          |
    +--------------------------------+----------------------------------------+
    | ``dvb_step_channel``           | ``cycle dvb-channel``                  |
    +--------------------------------+----------------------------------------+
    | ``tv_set_freq <val>``          | ``set tv-freq <val>``                  |
    +--------------------------------+----------------------------------------+
    | ``tv_step_freq``               | ``cycle tv-freq``                      |
    +--------------------------------+----------------------------------------+
    | ``tv_set_norm <norm>``         | ``set tv-norm <norm>``                 |
    +--------------------------------+----------------------------------------+
    | ``tv_step_norm``               | ``cycle tv-norm``                      |
    +--------------------------------+----------------------------------------+

    .. note::

        由于缺乏使用TV/DVB/PVR功能的硬件和用户，并且由于需要清理相关的命令代码，新的命令有可能出现错误或表现得更糟糕。如果有测试人员，这一点可以得到改善。否则，一些电视代码将在某个时候被删除。

Slave mode
~~~~~~~~~~

* 从属模式被删除。一个合适的从属模式的应用需要大量的代码和黑客来完成。主要问题是，从属模式是一个糟糕的、不完整的接口，为了绕过这个问题，应用程序解析了为用户准备的输出信息。很难知道到底哪些信息是由从属模式的应用程序解析的。这使得在不破坏某些东西的情况下，几乎不可能改进为用户准备的终端输出。

  这绝对是疯狂的，由于最初对 **mpv** 的改进很快使从属模式与大多数应用程序不兼容，它被当作无用的杂物而被删除。客户端API（见下文）被取代。

  ``--identify`` 被 ``TOOLS/mpv_identify.sh`` 封装脚本所取代。

* 有一段时间（包括0.4.x版本），mpv支持一个 ``--slave-broken`` 选项。下面的选项是等价的。

  ::

        --input-file=/dev/stdin --input-terminal=no


  假设系统支持 ``/dev/stdin``

  (该选项早在0.5.1版本中加入，并准确设置了这些选项。在0.10.x中又被移除）。

* 还支持一个JSON RPC协议，可以访问客户端的API。参见 `JSON IPC`_ 以了解更多信息。

**mpv** 也提供了一个客户端API，它可以通过加载共享库来嵌入播放器。(参见源代码中的 ``libmpv/client.h`` )。也可以使用Lua脚本实现一个自定义的类似从属模式的协议。

Policy for Removed Features
---------------------------

**mpv** 正在积极开发中。如果有什么东西妨碍了更重要的开发（如修复错误或实现新的功能），我们有时会删除功能。通常这种情况只发生在那些看起来毫无用处，或者不被任何人使用的老功能上。通常这些功能是不明显的，或者是 "继承 "的，或者是被标记为实验性的，但从未得到任何用户的特别赞扬。

有时，功能被新的东西所取代。新的代码要么更简单，要么更强大，但不一定能提供旧功能的一切。

我们不能排除我们不小心删除了那些真正受欢迎的功能。一般来说，我们不知道一个特定的功能被使用了多少。如果你错过了一个功能，并且认为它应该被重新添加，请在mpv的bug追踪器上开一个问题。希望可以找到一个解决方案。通常情况下，重新添加一些东西并不是什么大问题，或者有更好的替代品。

Why this Fork?
--------------

mplayer2实际上已经死了，mpv开始是一个包含新的/实验性开发的分支。(其中一些在分叉公开后就被合并了，似乎是为了承认开发，或者至少是合并，应该更加积极。)

MPlayer专注于不破坏任何东西，但却被困在一个可怕的代码库中，无法清理。(除非你像mpv那样做--无情的、随之而来的对坏的、旧的代码的修剪。) 清理和保留破损的东西是冲突的，所以由于开发政策的冲突，mpv所追求的那种开发不能在MPlayer中完成。

此外，mplayer2已经比MPlayer有了很多变化，这些变化需要回传到MPlayer的代码库中。这不仅困难重重（几年的开发分歧），而且由于上述MPlayer的开发政策，也不可能做到。
