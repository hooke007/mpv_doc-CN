mpv
###

##############
a media player
##############

:Copyright: GPLv2+
:Manual section: 1
:Manual group: multimedia

.. contents:: 目录

SYNOPSIS
========

| **mpv** [options] [file|URL|PLAYLIST|-]
| **mpv** [options] files

DESCRIPTION
===========

**mpv** 是一个基于MPlayer和mplayer2的媒体播放器。它支持各种各样的视频文件格式、音频和视频编解码器以及字幕类型。特殊的输入URL类型可用于读取磁盘文件以外的各种来源的输入。根据平台的不同，支持各种不同的视频和音频输出方法。

让你快速入门的使用例子可以在本手册的末尾找到。


INTERACTIVE CONTROL
===================

mpv有一个完全可配置的、命令驱动的控制层，允许你使用键盘、鼠标或遥控器来控制mpv（没有LIRC支持--将遥控器配置为输入设备）。

请看 ``--input-`` 选项，以了解定制的方法。

下面的列表不一定完整。参见 ``etc/input.conf`` ，了解默认绑定的列表。用户的 ``input.conf`` 文件和Lua脚本可以定义额外的键绑定。

参见 ``--input-test`` ，了解各键的交互式绑定细节，以及 `stats`_ 内置脚本，了解键绑定列表（包括输出到终端）。

Keyboard Control
----------------

左和右
    向后/向前搜索5秒。Shift+箭头 进行1秒的精确搜索（见 ``--hr-seek`` ）。

上和下
    向前/向后搜索1分钟。Shift+箭头 做5秒的精确搜索（见 ``--hr-seek`` ）。

Ctrl+左和右
    寻找前一个/下一个字幕。受一些限制，可能不一定有效；见 ``sub-seek`` 命令。

Ctrl+Shift+左和右
    调整字幕延迟，以便现在显示下一个或上一个字幕。这对同步字幕和音频特别有用。

[ 和 ]
    减少/增加当前播放速度10%。

{ 和 }
    将当前的播放速度减半/加倍。

退格键
    重置播放速度为正常。

Shift+退格
    撤销上一次的搜索。这只在播放列表条目没有被改变的情况下起作用。第二次点击它将回到原来的位置。详见 ``revert-seek`` 命令。

Shift+Ctrl+退格
    标记当前位置。这将被 ``Shift+BACKSPACE`` 作为返回的位置（一旦你返回寻找，标记将被重置）。你可以用它来在文件中寻找，然后返回到你离开的确切位置。

< 和 >
    在播放列表中往前/往后。

回车键
    在播放列表往后

p 或 空格键
    暂停（再按一次会取消暂停）。

\.
    前进。按一次将暂停，每连续按一次将播放一帧，然后再次进入暂停模式。

,
    后退。按一次将暂停，每连续按一次将反向播放一帧，然后再次进入暂停模式。

q
    停止播放并退出。

Q
    和 ``q`` 一样，但存储当前的播放位置。如果可能的话，以后播放同一文件将在旧的播放位置恢复。

/ 和 *
    减少/增加音量。

9 和 0
    减少/增加音量。

m
    静音。

\_
    循环浏览可用的视频轨道。

\#
    循环播放可用的音轨。

f
    切换全屏（另见 ``--fs`` ）。

ESC
    退出全屏模式。

T
    切换停留在顶部（另见 ``--ontop`` ）。

w 和 W
    减少/增加平移和扫描范围。e ``e`` 键目前与 ``W`` 键的作用相同，但不鼓励使用。

o （还有 P）
    在OSD上显示进度条、经过的时间和总时间。

O
    在正常和播放时间/持续时间之间切换OSD状态。

v
    切换字幕的可见性。

j 和 J
    循环可用的字幕。

z 和 Z
    调整字幕延迟+/-0.1秒。 ``x`` 键目前与 ``Z`` 键的作用相同，但不鼓励使用。

l
    设置/清除A-B循环点。详见 ``ab-loop`` 命令。

L
    切换无限循环。

Ctrl + 和 Ctrl -
    调整音频延迟（A/V同步）+/-0.1秒。

Shift+g 和 Shift+f
    调整字幕字体大小，幅度为+/-10%。

u
    在不对SSA/ASS字幕进行样式覆盖和几乎完全用普通字幕样式覆盖之间进行切换。更多信息请参见 ``--sub-ass-override``

V
    切换字幕VSFilter长宽兼容模式。参见 ``--sub-ass-vsfilter-aspect-compat`` 以获得更多信息。

r 和 R
    上/下移动字幕。 ``t`` 键的作用与 ``R`` 目前相同，但不鼓励使用。

s
    截屏

S
    截图，无字幕。(这是否有效取决于VO驱动的支持。)

Ctrl s
    按窗口显示的方式进行截图（有字幕、OSD和缩放的视频）。

PGUP 和 PGDWN
    寻找上一章/下一章的开头。在大多数情况下，"上一章"实际上是指当前章节的开头；见 ``--chapter-seek-threshold``

Shift+PGUP和PGDWN
    向后或向前搜索10分钟。(这曾经被映射到PGUP/PGDWN而不需要Shift)。

d
    激活/停用去隔行扫描。

A
    循环长宽比覆盖。

Ctrl h
    切换硬件视频解码开/关。

Alt+上下左右
    移动视频矩形（平移）。

Alt +和-
    将 ``Alt`` 与 ``+`` 或 ``-`` 键结合，可改变视频缩放。

Alt+退格
    重置平移/缩放设置。

F8
    显示播放列表和其中的当前位置（只在使用UI窗口时有用，在终端上被破坏）。

F9
    显示音频和字幕流的列表（仅在使用UI窗口时有用，在终端上被破坏）。

i和I
    显示/切换显示当前播放文件的统计数据的覆盖层，如编解码器、帧率、丢帧数等。参见 `STATS`_ 以获得更多信息。

del
    在从不/自动（鼠标移动）/总是之间循环OSC可见性。

\`
    显示控制台。(ESC会再次关闭它，见 `CONSOLE`_ )。

(以下按键只有在使用支持相应调整的视频输出时才有效。)

1 和 2
    调整对比度。

3 和 4
    调整亮度。

5 和 6
    调整伽玛。

7 和 8
    调整饱和度。

Alt+0（和macOS上的command+0）
    将视频窗口的大小调整为原来的一半。

Alt+1 (和macOS上的command+1)
    调整视频窗口的大小到原来的大小。

Alt+2 (和macOS上的command+2)
    将视频窗口的大小调整为原来的两倍。

command + f (仅macOS)
    切换全屏（另见 ``--fs`` ）。

(如果你的键盘上有多媒体键，以下按键是有效的。)

PAUSE
    暂停。

STOP
    停止播放并退出。

PREVIOUS 和 NEXT
    向后/向前寻找1分钟。


如果你错过了一些旧的按键绑定，请查看mpv git仓库中的 ``etc/restore-old-bindings.conf``

Mouse Control
-------------

左键双击
    切换全屏的开/关。

右键
    切换暂停的开/关。

前进/后退
    跳到播放列表中的下一个/上一个条目。

上/下轮
    向前/向后寻找10秒。

左/右轮
    减少/增加音量。


USAGE
=====

以 ``-`` 开头的命令行参数被解释为选项，其他都是文件名或URL。除了 *flag* 选项（或包括 ``yes`` 的选项），所有选项都需要一个参数，其形式为 ``--option=value``

一个例外是唯一的 ``-`` （没有其他东西），这意味着媒体数据将从stdin读取。另外， ``--`` （没有其他东西）将使播放器把所有下面的参数解释为文件名，即使它们以 ``-`` 开头。(要播放一个名为 ``-`` 的文件，你需要使用 ``./-`` )。

每个 *flag* 选项都有一个 *no-flag* 对应的选项，例如， ``--fs`` 选项的反面是 ``--no-fs`` 。 ``--fs=yes`` 与 ``--fs`` 相同， ``--fs=no`` 与 ``--no-fs`` 相同。

如果一个选项被标记为 *(XXX only)* ，它只能与 *XXX* 选项结合使用，或者在 *XXX* 被编译进去的情况下使用。

Legacy option syntax
--------------------

``--option=value`` 的语法没有被严格执行，被替代的传统语法 ``-option value`` 和 ``-option=value`` 也可以工作。这主要是为了与MPlayer兼容。应该避免使用这些。它们的语义可能在未来的任何时候发生变化。

例如，另一种语法将认为选项后面的参数是一个文件名。 ``mpv -fs no`` 将尝试播放一个名为 ``no`` 的文件，因为 ``--fs`` 是一个标志选项，不需要参数。如果一个选项改变了，它的参数成为可选项，那么使用替代语法的命令行就会中断。

在mpv 0.31.0之前，一个选项是以 ``--`` 开头还是以单个 ``-`` 开头没有区别。新的mpv版本严格要求你在 ``=`` 之后传递选项值。例如，以前  ``mpv --log-file f.txt`` 会向 ``f.txt`` 写日志，但现在这个命令行失败了，因为 ``--log-file`` 期待一个选项值，而 ``f.txt`` 只是被认为是一个正常的文件被播放（如 ``mpv f.txt`` ）。

未来的计划是， ``-option value`` 将不再起作用，带有单个 ``-`` 的选项与 ``--`` 选项的行为相同。

Escaping spaces and other special characters
--------------------------------------------

请记住，shell会对你传递给mpv的参数进行部分分析和处理。例如，你可能需要引用或转义选项和文件名：

    ``mpv "filename with spaces.mkv" --title="window title"``

如果涉及到子选项解析器，情况会变得更加复杂。子选项解析器将几个选项放入一个字符串中，并一次将它们传递给一个组件，而不是在命令行的层面上使用多个选项。

子选项分析器可以用 ``"`` 和 ``[...]`` 来引用字符串。此外，还有一种特殊形式的用 ``%n%`` 引用，如下所述。

例如，假设假设的 ``foo`` 过滤器可以接受多个选项：

    ``mpv test.mkv --vf=foo:option1=value1:option2:option3=value3,bar``

这将把 ``option1`` 和 ``option3`` 传给 ``foo`` 过滤器， ``option2`` 作为标志（隐含 ``option2=yes`` ），并在其后添加一个 ``bar`` 过滤器。如果一个选项包含空格或像 ``,`` 或 ``:`` 这样的字符，你需要引用它们。

    ``mpv '--vf=foo:option1="option value with spaces",bar'``

Shell实际上可能从传递到命令行的字符串中剥离一些引号，所以这个例子对字符串进行了两次引号，确保mpv收到 ``"`` 引号。

 ``[...]`` 形式的引号包裹了 ``[`` 和 ``]`` 之间的一切。它对那些不解释参数中间的这些字符的shells很有用（比如bash）。这些引号是平衡的（从mpv 0.9.0开始）： ``[`` 和 ``]`` 嵌套，引号终止于字符串中没有匹配 ``[`` 的最后一个 ``]`` 。(例如， ``[a[b]c]`` 的结果是 ``a[b]c`` ）。

固定长度的引用语法是为外部脚本和程序使用的。

它以 ``%`` 开头，格式如下::

    %n%string_of_length_n

.. admonition:: 示例

    ``mpv '--vf=foo:option1=%11%quoted text' test.avi``

    或者在一个脚本中：

    ``mpv --vf=foo:option1=%`expr length "$NAME"`%"$NAME" test.avi``

注意：在适用于JSON-IPC的地方， ``%n%`` 是UTF-8字节的长度，在解码JSON数据后。

传递给客户端API的子选项也要进行转义处理。使用 ``mpv_set_option_string()`` 就像在命令行中传递 ``--name=data`` 一样（但是没有对字符串进行shell处理）。一些选项支持以更结构化的方式传递数值，而不是平面字符串，可以避免子选项解析的混乱。例如， ``--vf`` 支持 ``MPV_FORMAT_NODE`` ，它允许你以地图和数组的嵌套数据结构传递子选项。

Paths
-----

在向mpv传递任意的路径和文件名时必须注意一些问题。例如，以 ``-`` 开头的路径将被解释为选项。同样，如果一个路径包含序列 ``://`` ，前面的字符串可能被解释为协议前缀，尽管 ``://`` 可以是合法UNIX路径的一部分。为了避免任意路径的问题，你应该确保传递给mpv的绝对路径以 ``/`` 开始，而相对路径以 ``./`` 为前缀。

不鼓励使用 ``file://`` 伪协议，因为它涉及到奇怪的URL解压规则。

名称 ``-`` 本身被解释为 stdin ，并将导致mpv禁用控制台控制。(这使得它适合于播放发送到stdin的数据)。

特殊参数 ``--`` 可以用来阻止mpv将后面的参数解释为选项。

当使用客户端API时，你应该严格避免使用 ``mpv_command_string`` 来调用 ``loadfile`` 命令，而应该选择例如 ``mpv_command`` 来避免文件名转义的需要。

对于传递给子选项的路径，由于需要转义特殊字符，情况会更加复杂。为了解决这个问题，可以用固定长度的语法来包装路径，例如 ``%n%string_of_length_n`` （见上文）。

一些mpv选项解释以 ``~`` 开头的路径。目前，前缀 ``~~home/`` 扩展到mpv配置目录（通常是 ``~/.config/mpv/`` ）。 ``~/`` 扩展到用户的主目录。(后面的 ``/`` 总是需要的。)目前可以识别以下路径：

================ ===============================================================
名称             意义
================ ===============================================================
``~~/``          如果子路径存在于mpv的任何配置目录中，则返回现有文件/目录的路径。否则这相当于 ``~~home/`` 。注意，如果使用了 --no-config ， ``~~/foobar`` 将解析为 ``foobar`` ，这可能是意想不到的。
``~/``           用户主目录根（类似于shell， ``$HOME`` ）
``~~home/``      mpv配置目录（例如 ``~/.config/mpv/`` ）
``~~global/``    全局配置路径，如果有的话(not on win32)
``~~osxbundle/`` macOS bundle资源路径(macOS only)
``~~desktop/``   桌面的路径 (win32, macOS)
``~~exe_dir/``   仅限win32：包含exe的目录路径（用于配置文件； ``$MPV_HOME`` 会覆盖它）
``~~old_home/``  不要使用
================ ===============================================================


Per-File Options
----------------

当播放多个文件时，在命令行中给出的任何选项通常会影响所有文件。例如::

    mpv --a file1.mkv --b file2.mkv --c

=============== ===========================
文件            激活的选项
=============== ===========================
file1.mkv       ``--a --b --c``
file2.mkv       ``--a --b --c``
=============== ===========================

(这与MPlayer和mplayer2不同）。

另外，如果任何选项在运行时被改变（通过输入命令），它们在播放新文件时不会被重置。

有时，按文件改变选项是很有用的。这可以通过添加特殊的每文件标记 ``--{`` 和 ``--}`` 来实现。(注意，在某些shells上必须转义这些标记。) 例如::

    mpv --a file1.mkv --b --\{ --c file2.mkv --d file3.mkv --e --\} file4.mkv --f

=============== ===========================
文件            激活的选项
=============== ===========================
file1.mkv       ``--a --b --f``
file2.mkv       ``--a --b --f --c --d --e``
file3.mkv       ``--a --b --f --c --d --e``
file4.mkv       ``--a --b --f``
=============== ===========================

此外，任何在运行时改变的文件本地选项都会在当前文件停止播放时被重置。如果在播放 ``file2.mkv`` 时改变了 ``--c`` 选项，那么在推进到 ``file3.mkv`` 时就会被重置。这只影响到文件本地的选项。选项 ``--a`` 在这里永远不会被重置。


List Options
------------

一些存储选项值列表的选项可以有动作后缀。例如， ``--display-tags`` 选项接收一个 ``,`` 分开的标签列表，但该选项也允许你用 ``--display-tags-append`` 附加一个标签，例如，标签名称可以包含一个字面的 ``,`` 而不需要转义。

String list and path list options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

字符串列表是由 ``,`` 分隔的。字符串不被选项系统本身所解析或解释。然而，大多数路径或文件列表选项使用 ``:`` （Unix）或 ``;`` （Windows）作为分隔符，而不是 ``,``

它们支持以下操作：

============= ===============================================
后缀          含义
============= ===============================================
-set          设置一个项目列表（使用列表分隔符，用反斜杠转义）
-append       添加单个项目（不解释转义）
-add          添加1个或多个项目（与 -set 的语法相同）
-pre          前置1个或多个项目（与 -set 的语法相同）
-clr          清除选项（删除所有项目）
-remove       如果存在，则删除项目（不解释转义）
-del          按整数索引删除1个或多个项目 (deprecated)
-toggle       添加一个项目，如果它已经存在，则删除（不解释转义）
============= ===============================================

``-append`` 是作为一个简单的方法来追加一个项目，而不需要转义参数（你可能仍然需要在shell级别转义）。

Key/value list options
~~~~~~~~~~~~~~~~~~~~~~

一个键/值列表是一个键/值字符串对的列表。在编程语言中，这种类型的数据结构通常被称为地图或字典。顺序通常并不重要，尽管在某些情况下，顺序可能很重要。

它们支持以下操作：

============= ===============================================
后缀          含义
============= ===============================================
-set          设置一个项目列表（使用 ``,`` 作为分隔符）
-append       添加一个项目(键用转义词，值不用转义词)
-add          添加1个或多个项目(与 -set 的语法相同)
-remove       如果存在，按键删除项目（不解释转义）
============= ===============================================

键在列表中是唯一的。如果设置了一个已经存在的键，在附加新值之前，现有的键会被删除。

如果你想在不解释转义或 ``,`` 的情况下传递一个值，建议使用 ``-add`` 的变体。当使用libmpv时，最好使用 ``MPV_FORMAT_NODE_MAP`` ；当使用脚本后端或JSON IPC时，使用适当的结构化数据类型。

在mpv 0.33之前， ``:`` 也被 ``-set`` 识别为分隔符。

Filter options
~~~~~~~~~~~~~~

这是一个非常复杂的选项类型，只用于 ``--af`` 和 ``--vf`` 选项。它们通常需要复杂的转义。详见 `VIDEO FILTERS`_ 。它们支持以下操作：

============= ===============================================
后缀          含义
============= ===============================================
-set          设置一个过滤器列表(使用 ``,`` 作为分隔符)
-append       添加单个过滤器
-add          添加1个或多个过滤器(与 -set 语法相同)
-pre          预置1个或多个过滤器(与 -set 语法相同)
-clr          清除选项（删除所有过滤器）
-remove       删除过滤器（如果存在的话
-del          通过整数索引或过滤器标签删除1个或多个过滤器 (deprecated)
-toggle       添加一个过滤器，如果它已经存在，则删除
-help         伪操作，在终端打印出帮助文本
============= ===============================================

General
~~~~~~~

如果没有后缀，所使用的操作通常是 ``-set``

尽管有些操作允许指定多个项目，但除了 ``-set`` 之外，强烈不鼓励使用这种操作，并且已经deprecated。有可能像 ``-add`` 和 ``-pre`` 这样的操作会像 ``-append`` 一样工作，只接受一个未转义的项目（所以 ``,`` 分隔符不会被解释，而是作为值的一部分被传递）。

一些选项（如 ``--sub-file``, ``--audio-file``, ``--glsl-shader`` ）是具有 ``-append`` 动作的适当选项的别名。例如， ``--sub-file`` 是 ``--sub-files-append`` 的别名。

这种类型的选项可以在运行时使用 ``change-list`` 命令进行修改，该命令将后缀（不含 ``-`` ）作为单独的操作参数。

CONFIGURATION FILES
===================

Location and Syntax
-------------------

你可以把所有的选项放在配置文件中，每次运行mpv的时候都会读取。全系统的配置文件 'mpv.conf' 在你的配置目录中（例如 ``/etc/mpv`` 或 ``/usr/local/etc/mpv`` ），用户专用的是 ``~/.config/mpv/mpv.conf`` 。有关细节和平台的具体情况（特别是Windows的路径），请参见 `FILES`_ 部分。

用户特定的选项覆盖系统范围的选项，命令行给出的选项也覆盖这两种选项。配置文件的语法是 ``option=value`` 。在 *#* 之后的所有内容都被认为是注释。没有值的选项可以通过设置为 *yes* 来启用，而通过设置为 *no* 来禁用。甚至子选项也可以用这种方式指定。

.. admonition:: 配置文件示例

    ::

        # 默认使用GPU加速的视频输出
        vo=gpu
        # 对可能包含空格的文本使用引号：
        term-status-msg="Time: ${time-pos}"

Escaping spaces and special characters
--------------------------------------

这和命令行选项的做法一样。这里不涉及shell，但是如果选项值包含某些字符，比如空格，仍然需要整体加引号。一个配置项可以用 ``"`` 引用，也可以用前面提到的固定长度的语法（ ``%n%`` ）。这就像把引号字符串的确切内容作为命令行选项来传递。C-style的转义目前 _不_ 在这一层次上解释，尽管有些选项手动做了这个。（这是个乱七八糟的问题，也许应该在某个时候进行修改）。

Putting Command Line Options into the Configuration File
--------------------------------------------------------

几乎所有的命令行选项都可以放到配置文件中。这里有一个小指南。

======================= ========================
选项                    配置文件条目
======================= ========================
``--flag``              ``flag``
``-opt val``            ``opt=val``
``--opt=val``           ``opt=val``
``-opt "has spaces"``   ``opt="has spaces"``
======================= ========================

File-specific Configuration Files
---------------------------------

你也可以编写针对文件的配置文件。如果你想为一个叫 "video.avi" 的文件写一个配置文件，创建一个名为 "video.avi.conf" 的文件，并在其中加入特定文件的选项，然后把它放在 ``~/.config/mpv/`` 。你也可以把配置文件和要播放的文件放在同一目录下。这两种方法都需要你设置 ``--use-filedir-conf`` 选项（在命令行或你的全局配置文件中）。如果在同一目录下发现了特定文件的配置文件，就不会从 ``~/.config/mpv`` 中加载特定文件的配置。此外， ``--use-filedir-conf`` 选项可以启用特定目录的配置文件。对于这一点，mpv首先尝试从播放的文件的同一目录加载mpv.conf，然后尝试加载任何文件特定的配置。


Profiles
--------

为了便于处理不同的配置，可以在配置文件中定义profile。profile以方括号中的名称开头，例如： ``[my-profile]`` 。所有后面的选项将是profile的一部分。描述（由 ``profile-desc`` 显示）可以用 ``profile-desc`` 选项来定义。要结束profile，可以启动另一个，或者使用profile名称 ``default`` 继续使用正常选项。

你可以用 ``--profile=help`` 列出profile，用 ``--show-profile=<name>`` （用profile名称替换 ``<name>`` ）显示profile的内容。你可以使用 ``--profile=<name>`` 选项在启动时应用profile，或者在运行时使用 ``apply-profile <name>`` 命令。

.. admonition:: 带有profile的mpv配置文件示例

    ::

        # 普通的顶层选项
        fullscreen=yes

        # 一个可以用 --profile=big-cache 启用的profile
        [big-cache]
        cache=yes
        demuxer-max-bytes=123400KiB
        demuxer-readahead-secs=20

        [slow]
        profile-desc="some profile name"
        # 引用一个内置的profile
        profile=gpu-hq

        [fast]
        vo=vdpau

        # 再次使用一个profile来扩展它
        [slow]
        framedrop=no
        # 你也可以包括其他profile
        profile=big-cache

Runtime profiles
----------------

profile可以在运行时用 ``apply-profile`` 命令来设置。由于这个操作是 "破坏性的"（profile中的每一项都被简单地设置为选项，覆盖了之前的值），你不能再启用和禁用profile。

作为部分补救措施，有一种方法可以使profile在用profile的值覆盖之前保存旧的选项值，然后在以后使用 ``apply-profile <profile-name> restore`` 恢复旧值。

这可以通过 ``profile-restore`` 选项启用，该选项需要以下一个选项：

    ``default``
        什么都不做，什么都不能恢复（默认）。

    ``copy``
        当应用一个profile时，将所有profile选项的旧值复制到一个备份中，然后再从profile中设置它们。当恢复时，这些选项被重置为使用备份的旧值。

        每个profile都有自己的备份值列表。如果备份已经存在（例如，如果 ``apply-profile name`` 被连续调用了一次以上），现有的备份就不会被改变。还原操作将删除该备份。

        重要的是要知道，恢复并不是 "撤销 "选项的设置，而只是复制旧的选项值。例如考虑 ``vf-add`` ，向 ``vf`` 追加一个条目。这个机制将简单地复制整个 ``vf`` 列表，并且在恢复时不执行 ``vf-add`` 的逆操作（即 ``vf-remove`` ）。

        注意，如果一个profile包含递归profile（通过 ``profile`` 选项），这些递归profile中的选项会被视为该profile的一部分。在创建或使用备份时，被引用的profile的备份列表不会被使用。恢复一个profile不恢复被引用的profile，只恢复被引用的profile的选项（就像它们是主profile的一部分）。

    ``copy-equal``
        类似于 ``copy`` ，但只有当选项的值与profile有效设置的值相同时才会恢复。这试图处理用户在交互式改变选项后不希望其被重置的情况。

.. admonition:: 示例

    ::

        [something]
        profile-restore=copy-equal
        vf-add=rotate=90

    然后运行这些命令将导致如注释的行为：

    ::

        set vf vflip
        apply-profile something
        vf-add=hflip
        apply-profile something
        # vf == vflip,rotate=90,hflip,rotate=90
        apply-profile something restore
        # vf == vflip

Conditional auto profiles
-------------------------

设置了 ``profile-cond`` 选项的profile在相关条件符合的情况下会自动应用（除非自动profile被禁用）。该选项需要一个字符串，它被解释为Lua条件。如果评估表达式返回真，则应用profile，如果返回假，则被忽略。这个Lua代码的执行没有被沙盒化。

条件表达式中的任何变量都可以引用属性。如果一个标识符还没有被Lua或mpv定义，它将被解释为属性。例如， ``pause`` 将返回当前的暂停状态。你不能用 ``-`` 来引用属性，因为那表示减法，但是如果变量名包含任何 ``_`` 字符，它们就会变成 ``-`` 。例如， ``playback_time`` 将返回属性 ``playback-time``

一个更强大的访问属性的方法是使用 ``p.property_name`` 或 ``get("property-name", default_value)`` 。如果引入一个同名的新标识符，自动变量到属性的魔法就会失效（例如，如果添加一个名为 ``pause()`` 的函数， ``pause`` 将返回一个函数值，而不是 ``pause`` 属性的值）。

注意，如果一个属性不可用，它将返回 ``nil`` ，如果在表达式中使用，可能会导致错误。这些错误会被记录在verbose模式中，并且表达式被认为是错误的。

每当一个profile条件所引用的属性发生变化时，条件会被重新评估。如果条件的返回值从false或error变成了true，就会应用profile。

一旦条件从true变为false，这个机制就会尝试"unapply" profile。如果你想使用这个，你需要为profile设置 ``profile-restore`` 。另一种可能性是创建另一个具有反转条件的profile来撤销另一个profile。

递归profile可以被使用。但是我们不鼓励在一个有条件的profile中引用其他有条件的profile，因为这可能导致棘手和不直观的行为。

.. admonition:: 示例

    只是让高清视频看起来很有趣：

    ::

        [something]
        profile-desc=HD video sucks
        profile-cond=width >= 1280
        hue=-50

    如果你想在条件再次变为false时恢复profile，你可以设置 ``profile-restore`` ：

    ::

        [something]
        profile-desc=Mess up video when entering fullscreen
        profile-cond=fullscreen
        profile-restore=copy
        vf-add=rotate=90

    这是在进入全屏时将 ``rotate`` 过滤器追加到视频过滤器链中。当离开全屏时， ``vf`` 选项被设置为进入全屏前的值。请注意，这也会删除用户在全屏模式下添加的任何其他过滤器。避免这种情况比较棘手，例如可以通过添加第二个具有相反条件和操作的profile来解决。

    ::

        [something]
        profile-cond=fullscreen
        vf-add=@rot:rotate=90

        [something-inv]
        profile-cond=not fullscreen
        vf-remove=@rot

.. warning::

    每当涉及到的属性发生变化时，条件就会被再次评估。例如，如果你的条件使用 ``p.playback_time`` ，条件大约在每一帧视频中都要重新评估。这可能很慢。

这个功能由一个内部的Lua脚本管理。条件在这个脚本中作为Lua代码执行。它的环境至少包含以下内容：

``(function environment table)``
    每个Lua函数都有一个环境表。这用于标识符的访问。它没有命名的Lua符号；它是隐含的。

    环境对mpv属性进行 "magic" 访问。如果一个标识符还没有在 ``_G`` 中定义，它将检索同名的mpv属性。在读取属性之前，名称中任何出现的 ``_`` 都会被替换成 ``-`` 。返回的值是由 ``mp.get_property_native(name)`` 检索的。在内部，使用了一个属性值的缓存，通过观察属性来更新，所以不能观察的属性将永远停留在初始值。

    如果你想访问名称中实际包含 ``_`` 的属性，请使用 ``get()`` （它不执行transliteration）。

    在内部，环境表有一个 ``__index`` 元方法设置，它执行访问逻辑。

``p``
    一个类似于环境表的 "magic" 表。与后者不同，它不喜欢访问定义在 ``_G`` 中的变量 - 它总是访问属性。

``get(name [, def])``
    读取一个属性并返回其值。如果属性值为 ``nil`` （例如，如果属性不存在），将返回 ``def`` 

    这在表面上与 ``mp.get_property_native(name)`` 类似。一个重要的区别是，它访问了属性缓存，并启用了变化检测逻辑（这对自动profile的动态运行时行为至关重要）。另外，它不会返回一个错误值作为第二个返回值。

    上面提到的 "magic" 表使用这个函数作为后端。它不执行 ``_`` 的transliteration

此外，与空白mpv Lua脚本中的环境相同。例如， ``math`` 被定义了，可以访问Lua标准数学库。

.. warning::

    这个功能可能会被无限期地改变。你可能被迫在mpv更新时调整你的profile

Legacy auto profiles
--------------------

有些profile是使用传统的机制自动加载的。下面的例子证明了这一点：

.. admonition:: 自动加载profile

    ::

        [extension.mkv]
        profile-desc="profile for .mkv files"
        vf=vflip

profile的名称遵循 ``type.name`` 的模式，其中type可以是 ``protocol`` 表示正在使用的输入/输出协议（见 ``--list-protocols`` ）， ``extension`` 表示当前播放文件的路径扩展名（ *不是* 文件的格式）。

这个功能非常有限，被认为是soft-deprecated 。使用conditional auto profiles。

Using mpv from other programs or scripts
========================================

从其他程序或脚本中使用mpv，有三种选择：

    1. 把它作为UNIX进程调用。如果你这样做， *不要解析终端输出* 。终端输出是为人类准备的，并且可能随时改变。此外，终端行为本身也可能随时改变。不能保证兼容性。

       即使你传递了 ``--no-terminal`` ，你的代码也应该工作。不要试图通过向mpv的stdin发送终端控制代码来模拟用户输入。如果你需要交互式控制，建议使用  ``--input-ipc-server`` 。这可以让你通过unix域套接字（或Windows的命名管道）访问 `JSON IPC`_ 

       根据你的工作，传递 ``--no-config`` 或 ``--config-dir`` 可能是一个好主意，以避免与用于CLI播放的正常mpv用户配置冲突。

       使用 ``--input-ipc-server`` 也适用于远程控制等目的（然而，IPC协议本身并不 "安全"，也不打算如此）。

    2. 使用libmpv。当mpv被用作一个完全不同的应用程序的播放后端时，一般建议使用这种方法。提供的C语言API与CLI机制和脚本API非常接近。

       注意，即使libmpv有不同的默认值，它也可以被配置成与CLI播放器完全一样的工作（除了命令行解析不可用）。

       参见 `EMBEDDING INTO OTHER PROGRAMS (LIBMPV)`_

    3. 作为一个用户脚本（ `LUA SCRIPTING`_, `JAVASCRIPT`_, `C PLUGINS`_ ）。当目标是 "增强" CLI播放器时，建议使用这种方式。脚本可以访问mpv的整个客户端API。

       这是为播放器创建第三方扩展的标准方式。

所有这些都可以访问客户端API，它是由播放器核心提供的各种机制的总和，正如这里所记录的：  `OPTIONS`_, `List of Input Commands`_, `Properties`_, `List of events`_ (也见 C API), `Hooks`_.

TAKING SCREENSHOTS
==================

当前播放的文件的截图可以使用'screenshot'输入模式命令来拍摄，它默认与 ``s`` 键绑定。命名为 ``mpv-shotNNNN.jpg`` 的文件将被保存在工作目录中，使用第一个可用的编号--没有文件会被覆盖。在伪GUI模式下，屏幕截图将被保存在其他地方。参见 `PSEUDO GUI MODE`_

屏幕截图通常会包含视频过滤链末端的未缩放的视频内容和字幕。默认情况下， ``S`` 拍摄的屏幕截图没有字幕，而 ``s`` 包括字幕。

与MPlayer不同， ``screenshot`` 视频过滤器是不需要的。这个过滤器在mpv中从来不需要，已经被删除。

TERMINAL STATUS LINE
====================

在播放过程中，mpv在终端显示播放状态。它看起来像这样的东西：

    ``AV: 00:03:12 / 00:24:25 (13%) A-V: -0.000``

状态行可以用 ``--term-status-msg`` 选项来覆盖。

以下是可以在状态行显示的东西的列表。还列出了输入属性，可以用来手动获得相同的信息。

- ``AV:`` or ``V:`` (video only) or ``A:`` (audio only)
- 当前的时间位置，以 ``HH:MM:SS`` 格式（ ``playback-time`` 属性）
- 总的文件持续时间（如果未知，则不存在）（ ``duration`` 属性）
- 播放速度，例如： ``x2.0`` 。只有在速度不正常时才可见。这是用户要求的速度，而不是实际速度（通常它们应该是一样的，除非播放太慢）。( ``speed`` 属性。)
- 播放百分比，例如： ``(13%)`` 。文件已经播放了多少。通常从播放位置和持续时间计算出来，但如果这些方法不可用，可以退回到其他方法（如字节位置）。( ``percent-pos`` 属性。)
- 音频/视频同步为 ``A-V:  0.000`` 。这是音频和视频时间的区别。通常它应该是0或接近0。如果它在增长，可能表明有播放问题。( ``avsync`` 属性。)
- 总的A/V同步变化，例如： ``ct: -0.417`` 。通常是不可见的。如果有音频 "丢失"，或者没有足够的帧可以丢弃，就会显示出来。通常这将表明有问题。( ``total-avsync-change`` 属性。)
- 编码状态在 ``{...}`` ，只在编码模式下显示。
- 显示同步状态。如果显示同步是激活的（ ``display-sync-active`` 属性），会显示 ``DS: 2.500/13`` ，其中第一个数字是每个视频帧的平均vsyncs数（例如，在60Hz屏幕上播放24Hz视频时为2.5），如果比率没有取整，或者有错误的帧（ ``vsync-ratio`` ），可能会出现抖动，第二个数字是估计的vsyncs数，花了太长时间（ ``vo-delayed-frame-count`` 属性）。后者是启发式的，因为一般来说不可能肯定地确定。
- 丢弃的帧，例如： ``Dropped: 4`` 。只有当计数不为0时才会显示。如果视频帧率高于显示器的帧率，或者视频渲染太慢，就会增加。也可能在 "hiccups" 和视频帧不能及时显示时被增加。( ``frame-drop-count`` 属性。)如果解码器掉帧，解码器掉帧的数量也会附加到显示上，例如。 ``Dropped: 4/34`` 。只有当解码器丢帧的功能被启用时，才会发生这种情况， ``--framedrop`` 选项。( ``decoder-frame-drop-count`` 属性。)
- 缓存状态，例如： ``Cache:  2s/134KB`` 。如果流媒体缓存被启用，则可见。第一个值显示在demuxer中缓冲的视频量（秒），第二个值显示缓冲量的估计大小（千字节）。( ``demuxer-cache-duration`` 和 ``demuxer-cache-state`` 属性)


LOW LATENCY PLAYBACK
====================

mpv为正常的视频播放进行了优化，这意味着它实际上试图缓冲尽可能多的数据，这似乎是合理的。这将增加延时。只有通过特别禁用增加延迟的功能，才有可能减少延迟。

内置的 ``low-latency`` profile试图应用一些可以减少延迟的选项。你可以使用  ``--profile=low-latency`` 来应用所有的选项。你可以用 ``--show-profile=low-latency`` 来列出内容（有些选项很不明显，可能每个mpv版本都有变化）。

请注意，有些选项会降低播放质量。

大多数延迟实际上是由不方便的计时行为引起的。你可以用 ``--untimed`` 来禁用它，但它很可能会中断，除非流中没有音频，而且输入以恒定的速率向播放器提供数据。

另一个常见的问题是MJPEG流。这些流没有正确的帧率信号。使用 ``--untimed`` 或 ``--no-correct-pts --fps=60`` 可能有帮助。

对于现场直播，由于暂停数据流，由于稍低的播放速率，或 "缓冲"暂停，数据可能会积累起来。如果demuxer cache被启用，这些可以被手动跳过。实验性的 ``drop-buffers`` 命令可以用来丢弃任何缓冲的数据，尽管它非常具有破坏性。

在某些情况下，手动调整TCP缓冲区的大小等可以帮助减少延迟。

可以尝试其他选项：

- ``--opengl-glfinish=yes`` 可以减少图形驱动中的缓冲区
- ``--opengl-swapinterval=0`` 同上
- ``--vo=xv`` 相同
- 没有音频 ``--framedrop=no --speed=1.01`` 可能对现场信号源有帮助（结果可能是混合的）。


PROTOCOLS
=========

``http://...``, ``https://``, ...

    支持许多网络协议，但必须始终指定协议前缀。mpv不会试图猜测一个文件名是否实际上是一个网络地址。协议前缀始终是必需的。

    注意，并不是所有的前缀在这里都有记录。未记录的前缀要么是记录的协议的别名，要么只是重定向到FFmpeg中实现和记录的协议。

    ``data:`` 在FFmpeg中支持（在Libav中不支持），但需要采用 ``data://`` 的格式。这样做是为了避免与文件名产生歧义。你也可以用 ``lavf://`` 或 ``ffmpeg://`` 作为前缀。

``ytdl://...``

    默认情况下，youtube-dl hook脚本只看http(s)的URLs。用 ``ytdl://`` 作为URL的前缀，可以让脚本始终处理该URL。这也可以用来调用youtube-dl的特殊功能，如按ID播放视频或调用搜索功能。

    请记住，你不能用它来传递youtube-dl的命令行选项，你必须使用 ``--ytdl-raw-options`` 来代替。

``-``

    从stdin播放数据。

``smb://PATH``

    播放来自Samba共享的路径。(需要FFmpeg支持)。

``bd://[title][/device]`` ``--bluray-device=PATH``

    播放蓝光光盘。从libbluray 1.0.1开始，你可以通过将ISO文件传递给 ``--bluray-device`` 来读取。

    ``title`` 可以是 ``longest`` 或 ``first`` （选择默认的播放列表）； ``mpls/<number>`` （选择 <number>.mpls 播放列表）； ``<number>`` （选择具有相同索引的播放列表）。mpv在加载时将列出可用的播放列表。

    ``bluray://`` 是一个别名

``dvd://[title][/device]`` ``--dvd-device=PATH``

    播放一个DVD。不支持DVD菜单。如果没有给出标题，将自动选择最长的标题。如果没有 ``--dvd-device`` ，它可能会尝试打开一个实际的光驱，如果有的话，并为操作系统实现。

    ``dvdnav://`` 是 ``dvd://`` 的旧别名，其作用完全相同。

``dvb://[cardnumber@]channel`` ``--dvbin-...``

    通过DVB的数字电视。 (Linux only.)

``mf://[filemask|@listfile]`` ``--mf-...``

    将一系列图像作为视频播放。

``cdda://[device]`` ``--cdrom-device=PATH`` ``--cdda-...``

    播放CD。

``lavf://...``

    访问任何FFmpeg/Libav的libavformat协议。基本上，这把 ``//`` 后面的字符串直接传给了libavformat。

``av://type:options``

    这是为使用libavdevice输入而准备的。 ``type`` 是libavdevice demuxer的名称， ``options`` 是传递给demuxer的（伪）文件名。

    .. admonition:: 示例

        ::

            mpv av://v4l2:/dev/video0 --profile=low-latency --untimed

        这将以几乎最低的延迟播放来自第一个v4l输入的视频。这是一个很好的替代被删除的 ``tv://`` 输入的方法。使用 ``--untimed`` 是一个黑客，可以立即输出捕获的帧，而不是尊重输入的帧速率。(将来可能有更好的方法来处理这个问题)。

    ``avdevice://`` 是一个别名

``file://PATH``

    一个作为URL的本地路径。在一些特殊的使用情况下可能会有用。注意， ``PATH`` 本身应该以第三个 ``/`` 开头，以使路径成为绝对路径。

``appending://PATH``

    播放一个本地文件，但假设它被附加到了。例如，这对目前正在下载到磁盘的文件很有用。这将阻止播放，只有在超时约2秒后没有新数据被追加时才停止播放。

    使用这个方法还是有点不好，因为没有办法检测一个文件是否真的被追加了，或者是否还在写。如果你想播放一些程序的输出，可以考虑使用pipe（ ``something | mpv -`` ）。如果真的必须是磁盘上的文件，用tail来让它永远等待，例如： ``tail -f -c +0 file.mkv | mpv -``

``fd://123``

    从给定的文件描述符（例如123）读取数据。这类似于通过 ``-`` 将数据输送到stdin，但可以使用任意的文件描述符。当stream layer "打开" 文件描述符时，mpv可能会修改一些文件描述符的属性。

``fdclose://123``

    类似 ``fd://`` ，但文件描述符在使用后会被关闭。当使用这个时，你需要确保同一个fd URL只被使用一次。

``edl://[edl specification as in edl-mpv.rst]``

    将多个文件的部分内容拼接在一起并播放。

``slice://start[-end]@URL``

    读取一个流的切片。

    ``start`` 和 ``end`` 代表一个字节范围，接受后缀，如 ``KiB`` 和 ``MiB`` 。 ``end`` 是可选的。

    如果  ``end`` 以 ``+`` 开头，则被视为从 ``start`` 开始的偏移。

    只适用于可搜索的流。

    示例::

      mpv slice://1g-2g@cap.ts

      在寻找1GiB后开始读取cap.ts，然后读取直到达到2GiB或文件结束。

      mpv slice://1g-+2g@cap.ts

      这个在寻求1 GiB后开始从cap.ts读取，然后读取到3 GiB或文件结束。

      mpv slice://100m@appending://cap.ts

      这个在寻找100MB后开始从cap.ts读取，然后读取直到文件结束。

``null://``

    模拟一个空文件。如果打开写入，它将丢弃所有数据。如果使用这个协议， ``null`` demuxer将特别通过autoprobing（而对于空文件不会自动调用）。

``memory://data``

    使用 ``data`` 部分作为源数据。

``hex://data``

    类似 ``memory://``，但字符串被解释为hexdump。

PSEUDO GUI MODE
===============

mpv没有正式的GUI，除了OSC（ `ON SCREEN CONTROLLER`_ ），它不是一个完整的GUI，也不打算成为GUI。然而，为了弥补缺乏预期的GUI行为，mpv在某些情况下会在启动时改变一些设置，使其行为略微更像GUI模式。

目前这只发生在以下情况：

- 如果在Linux上使用 ``mpv.desktop`` 文件启动（例如，从菜单或桌面环境提供的文件关联启动）
- 如果在Windows上从explorer.exe启动（技术上来说，如果它是在Windows上启动的，并且所有的stdout/stderr/stdin句柄都没有设置）。
- 在macOS上从bundle中启动
- 如果你手动在命令行中使用 ``--player-operation-mode=pseudo-gui``

该模式应用内置profile ``builtin-pseudo-gui`` 中的选项，但仅当这些选项没有在用户的配置文件或命令行中设置，这是与使用 ``--profile=builtin-pseudo-gui`` 的主要区别。

目前profile的定义如下：

::

    [builtin-pseudo-gui]
    terminal=no
    force-window=yes
    idle=once
    screenshot-directory=~~desktop/

``pseudo-gui`` profile的存在是为了兼容。 ``pseudo-gui`` profile中的选项是无条件应用的。此外，该profile确保启用伪GUI模式，因此 ``--profile=pseudo-gui`` 可以像在旧版mpv中一样工作。

::

    [pseudo-gui]
    player-operation-mode=pseudo-gui

.. warning::

    目前，你可以在配置文件中以正常的方式扩展 ``pseudo-gui`` profile。这已经deprecated。在未来的mpv版本中，行为可能会改变，不应用你的额外设置，和/或使用一个不同的profile名称。

Linux desktop issues
====================

本小节描述了Linux桌面上的常见问题。这些问题在Windows或macOS等系统上都不存在。

Disabling Screensaver
---------------------

默认情况下，mpv试图在播放过程中禁用操作系统的屏幕保护程序（只有当使用操作系统GUI API的VO处于激活状态时）。 ``--stop-screensaver=no`` 禁止这个功能。

一个常见的问题是，Linux桌面环境忽略了mpv所依赖的标准屏保API。特别是，mpv在X11上使用屏幕保护程序扩展（XSS），在Wayland上使用idle-inhibit。

GNOME是最严重的违法者之一，它甚至忽略了现在广泛支持的idle-inhibit协议。(这可能是由于恶意和无能的结合，但由于实现这个协议只需要几行代码，所以最可能是前者。你也会注意到，每当他们的破坏行为被指出来时，GNOME的拥护者是如何做出冒犯的反应的，这表明他们要么是虚伪，要么是更无知）。

这种不兼容的桌面环境（即无视标准）通常需要使用DBus API。这在几个方面都是荒谬的。直接的实际问题是，它需要为DBus库添加一个相当不方便的依赖关系，以某种方式将其主循环整合到mpv中，以及其他普遍不能接受的事情。

然而，由于mpv并不正式支持GNOME，这并不是什么大问题。如果你是那些想在 GNOME 上使用 mpv 的悲惨用户之一，请在 GNOME 问题跟踪器上报告一个错误： https://gitlab.gnome.org/groups/GNOME/-/issues

另外，你也可以写一个Lua脚本，调用 ``xdg-screensaver`` 命令行程序。(顺便说一下，这个命令行程序是一个完全可怕的笨拙程序，它试图识别你的DE，然后试图通过DBus CLI工具发送正确的DBus命令）。如果你觉得为了不让屏保启动而不得不写一个脚本的想法很可笑，那就不要使用 GNOME，或者使用 GNOME 视频软件而不是 mpv（祝你好运）。

在mpv 0.33.0之前，X11后端在未暂停时以10秒的间隔运行 ``xdg-screensaver reset`` 。在0.33.0中，这个黑客被移除。

.. include:: options.rst

.. include:: ao.rst

.. include:: vo.rst

.. include:: af.rst

.. include:: vf.rst

.. include:: encode.rst

.. include:: input.rst

.. include:: osc.rst

.. include:: stats.rst

.. include:: console.rst

.. include:: lua.rst

.. include:: javascript.rst

.. include:: ipc.rst

.. include:: changes.rst

.. include:: libmpv.rst

ENVIRONMENT VARIABLES
=====================

有一些环境变量可以用来控制mpv的行为。

``HOME``, ``XDG_CONFIG_HOME``
    用来决定mpv的配置目录。如果 ``XDG_CONFIG_HOME`` 没有设置， ``$HOME/.config/mpv`` 被使用。

    ``$HOME/.mpv`` 总是被添加到优先级较低的配置搜索路径列表中。

``MPV_HOME``
    mpv寻找用户设置的目录。覆盖 ``HOME`` ，mpv将尝试加载配置文件为 ``$MPV_HOME/mpv.conf``

``MPV_VERBOSE`` (see also ``-v`` and ``--msg-level``)
    设置所有消息模块的初始粗略程度（默认： 0）。这是一个整数，产生的粗略程度与传递到命令行的 ``--v`` 选项的数量相对应。

``MPV_LEAK_REPORT``
    如果设置为 ``1`` ，启用内部talloc泄漏报告。如果设置为其他值，禁用泄漏报告。如果没有设置，使用默认值，通常是 ``0`` 。如果mpv是用 ``--enable-ta-leak-report`` 构建的，默认是 ``1`` 。如果泄漏报告在编译时被禁用（在自定义的 ``CFLAGS`` 中的 ``NDEBUG`` ），这个环境变量被忽略。

``LADSPA_PATH``
    指定LADSPA插件的搜索路径。如果它没有被设置，必须使用完全合格的路径名称。

``DISPLAY``
    要使用的标准X11显示名称。

FFmpeg/Libav:
    这个库会访问各种环境变量。然而，它们没有被集中记录下来，记录它们也不是我们的工作。因此，这个列表是不完整的。

    值得注意的环境变量：

    ``http_proxy``
        用于代理 ``http://`` 和 ``https://`` 网址的URL。

    ``no_proxy``
        不应该使用代理的域名模式列表。列表条目由 ``,`` 分隔。模式可以包括 ``*``

libdvdcss:
    ``DVDCSS_CACHE``
        指定一个目录，用于存储标题键值。这将加快对缓存中的DVD的解扰速度。如果 ``DVDCSS_CACHE`` 目录不存在，将被创建，并创建一个以DVD的标题或生产日期命名的子目录。如果 ``DVDCSS_CACHE`` 没有设置或为空，libdvdcss将使用默认值，在Unix下为 ``${HOME}/.dvdcss/`` ，在Windows下为漫游应用数据目录（ ``%APPDATA%`` ）。特殊值 "off" 可禁用缓存。

    ``DVDCSS_METHOD``
        设置libdvdcss用于读取加扰盘的认证和解密方法。可以是 ``title``, ``key`` 或 ``disc`` 之一。

        key
           是默认方法。libdvdcss将使用一组计算好的播放器密钥来尝试获取光盘密钥。如果驱动器不能识别任何播放器的密钥，这可能会失败。

        disc
           是密钥失败时的一个后备方法。libdvdcss不使用播放器密钥，而是使用蛮力算法破解光盘密钥。这个过程是CPU密集型的，需要64MB的内存来存储临时数据。

        title
           是当所有其他方法都失败时的退路。它不依赖与DVD驱动器的密钥交换，而是使用密码攻击来猜测标题密钥。在极少数情况下，这可能会失败，因为光盘上没有足够的加密数据来进行统计攻击，但另一方面，这是解密存储在硬盘上的DVD，或RPC2驱动器上有错误区域的DVD的唯一方法。

    ``DVDCSS_RAW_DEVICE``
        指定要使用的原始设备。确切的用法取决于你的操作系统，例如，Linux设置原始设备的工具是raw(8)。请注意，在大多数操作系统中，使用一个原始设备需要高度对齐的缓冲区。Linux要求2048字节对齐（这是一个DVD扇区的大小）。

    ``DVDCSS_VERBOSE``
        设置libdvdcss的粗略程度。

        :0: 完全不输出任何信息。
        :1: 将错误信息输出到stderr。
        :2: 将错误信息和调试信息输出到stderr。

    ``DVDREAD_NOKEYS``
        在启动时跳过检索所有按键。目前禁用。

    ``HOME``
        FIXME: 记录这个问题。


EXIT CODES
==========

通常情况下， **mpv** 在成功完成播放后返回0作为退出代码。如果发生错误，可以返回以下退出代码。

    :1: 初始化mpv时出错。如果未知的选项被传递给mpv，也会返回这个代码。
    :2: 传递给mpv的文件不能被播放。这有点模糊：目前，如果初始化基本成功，文件的播放就被认为是成功的，即使初始化后立即播放失败。
    :3: 有一些文件可以被播放，也有一些文件不能被播放（使用上面的成功定义）。
    :4: 由于信号、VO窗口中的Ctrl+c（默认），或来自编码模式下的默认退出键绑定而退出。

注意，手动退出播放器将总是导致退出代码0，覆盖正常返回的退出代码。另外， ``quit`` 输入命令可以接受一个退出代码：在这种情况下，该退出代码会被返回。

FILES
=====

有关Windows的具体内容，请参见 `FILES ON WINDOWS`_ 部分。

``/usr/local/etc/mpv/mpv.conf``
    mpv系统范围内的设置（取决于传递给configure的 ``--prefix`` --mpv在默认配置中使用 ``/usr/local/etc/mpv/`` 作为配置目录，而大多数Linux发行版将其设置为 ``/etc/mpv/`` ）。

``~/.config/mpv``
    标准配置目录。这可以被环境变量覆盖，按升序排列。

    :1: 如果 ``$XDG_CONFIG_HOME`` 被设置，那么衍生的配置目录将是 ``$XDG_CONFIG_HOME/mpv``
    :2: 如果 ``$MPV_HOME``被设置，那么衍生的配置目录将是 ``$MPV_HOME``

    如果这个目录和原始配置目录（见下文）都不存在，mpv将尝试自动创建这个目录。

``~/.mpv/``
    原始（0.5.0之前）配置目录。如果存在，它将继续被读取。

    如果这个目录和标准配置目录都存在，配置将从两者中读取，标准配置目录的内容优先。然而，你应该完全迁移到标准目录，在这种情况下，将显示一个警告。

``~/.config/mpv/mpv.conf``
    mpv用户设置（见 `CONFIGURATION FILES`_ 部分）

``~/.config/mpv/input.conf``
    按键绑定 (见 `INPUT.CONF`_ 部分)

``~/.config/mpv/fonts.conf``
    为mpv定制的字体配置fonts.conf。你应该在这个文件中包括系统的fonts.conf，否则mpv将不知道你在系统中已经有的字体。

    只有在libass与fontconfig一起构建时才可用。

``~/.config/mpv/subfont.ttf``
    后备字幕字体

``~/.config/mpv/fonts/``
    这个目录中的字体文件被mpv/libass用来渲染字幕。如果你不想在你的系统中安装字体，这个目录很有用。注意，这个目录中的文件在被mpv使用之前会被加载到内存中。如果你有很多字体，可以考虑使用fonts.conf（见上文）来包括额外的字体，这样更节省内存。

``~/.config/mpv/scripts/``
    这个目录中的所有文件被加载，就像它们被传递给 ``--script`` 选项一样。它们是按字母顺序加载的。

    ``--load-scripts=no`` 选项禁止加载这些文件。

    详见 `Script location`_

``~/.config/mpv/watch_later/``
    包含临时的配置文件，用于恢复使用watch later功能的文件播放。例如参见 ``Q`` 键绑定，或 ``quit-watch-later`` 输入命令。

    每个文件都是一个小的配置文件，如果相应的媒体文件被加载，就会被加载。它包含播放位置和一些（不一定是全部）在播放过程中改变的设置。文件名是由媒体文件的完整路径散列出来的。一般来说，不可能从这个哈希值中提取媒体文件名。然而，你可以设置 ``--write-filename-in-watch-later-config`` 选项，播放器将把媒体文件名添加到恢复配置文件的内容中。

``~/.config/mpv/script-opts/osc.conf``
    这是由OSC脚本加载的。详见 `ON SCREEN CONTROLLER`_

    这个目录中的其他文件也是特定于相应的脚本的，mpv核心不会碰它们。

FILES ON WINDOWS
================

在win32上（如果用MinGW编译，但不是Cygwin），默认的配置文件位置是不同的。它们通常位于 ``%APPDATA%/mpv/`` 下。例如，mpv.conf的路径是 ``%APPDATA%/mpv/mpv.conf`` ，它映射到一个系统和用户的特定路径，例如

    ``C:\users\USERNAME\AppData\Roaming\mpv\mpv.conf``

你可以通过在cmd.exe中运行 ``echo %APPDATA%\mpv\mpv.conf`` 来找到确切路径。

其他配置文件（如 ``input.conf`` ）也在同一目录下。见上面的 `FILES`_ 部分。

环境变量 ``$MPV_HOME`` 完全覆盖了这些，就像在UNIX上一样。

如果mpv.exe旁边有一个名为 ``portable_config`` 的目录存在，所有的配置将只从这个目录加载。注意以后的配置文件也会写到这个目录。(这只存在于Windows，与 ``$MPV_HOME`` 是多余的。然而，由于Windows对脚本非常不友好，仅仅设置 ``$MPV_HOME`` 的包装脚本，就像你在其他系统上做的那样，是行不通的。 ``portable_config`` 是为了方便而提供的，以绕过这一限制。）

与 ``mpv.exe`` 在同一目录下的配置文件的加载优先级较低。一些配置文件只被加载一次，这意味着例如两个 ``input.conf`` 文件位于两个配置目录中，只有优先级较高的目录中的文件会被加载。

第三个优先级最低的配置目录是与 ``mpv.exe`` 在同一目录下的名为 ``mpv`` 的目录。这曾经是具有最高优先级的目录，但现在不鼓励使用，将来可能会被删除。

注意，mpv喜欢混合使用 ``/`` 和 ``\`` 路径分隔符，以达到简便的目的。kernel32.dll接受这个，但cmd.exe不接受。
