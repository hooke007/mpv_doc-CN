控制台
======

控制台是mpv中可输入命令的交互式解释器。它显示在视频窗口上。它也显示日志信息。它可以通过 ``--load-osd-console=no`` 选项完全禁用。

按键绑定
--------

\`
    显示控制台

ESC
    隐藏控制台

ENTER, Ctrl+J, Ctrl+M
    运行输入的命令

Shift+ENTER
    换行输入

LEFT, Ctrl+B
    移动光标至前一个字符

RIGHT, Ctrl+F
    移动光标至后一个字符

Ctrl+LEFT, Alt+B
    移动光标至当前单词的开头，如果在单词之间，则移到前一个单词的开头

Ctrl+RIGHT, Alt+F
    移动光标至当前单词的末尾，如果在单词之间，则移到后一个单词的结尾

HOME, Ctrl+A
    移动光标至当前行的开头

END, Ctrl+E
    移动光标至当前行的结尾

BACKSPACE, Ctrl+H
    删除前一个字符

Ctrl+D
    如果当前行是空的，隐藏控制台，否则删除后一个字符

Ctrl+BACKSPACE, Ctrl+W
    删除从光标到当前单词的开头的文本，如果在单词之间，则删除到前一个单词的开头

Ctrl+DEL, Alt+D
    删除从光标到当前单词的结尾的文本，如果在单词之间，则删除到下一个单词的结尾

Ctrl+U
    删除从光标到当前行开头的文本

Ctrl+K
    删除从光标到当前行结尾的文本

Ctrl+C
    删除当前行

UP, Ctrl+P
    向前浏览历史命令

DOWN, Ctrl+N
    向后浏览历史命令

PGUP
    转到历史命令的第一个命令

PGDN
    停止浏览历史命令

INSERT
    切换 插入/覆盖模式

Ctrl+V
    粘贴文本（在X11和Wayland上使用剪贴板）

Shift+INSERT
    粘贴文本（在X11和Wayland上使用primary selection）

TAB, Ctrl+I
    补全光标处的命令或属性名称

Ctrl+L
    清除控制台中的所有日志信息

命令
----

``script-message-to console type <text> [<cursor_pos>]``
    显示控制台并预填充所提供的文本，可选择指定初始光标位置为从1开始的正整数。

    .. admonition::  input.conf示例

        ``% script-message-to console type "seek  absolute-percent" 6``

已知问题
--------

- Windows系统粘贴文本的速度慢
- 非ASCII键盘输入有限制
- 光标键在Unicode code-points之间移动，而不是在grapheme cluster之间移动

设置
----

这个脚本可以通过放置在mpv用户目录下的设置文件 ``script-opts/console.conf`` 和 ``--script-opts`` 命令行选项来定制。设置语法在 `屏显式控制器`_ 中已描述。

按键的绑定可以用标准的方式来改变，例如参见 stats.lua 文档。

设置选项
~~~~~~~~

``scale``
    默认： 1

    所有的绘制都按该值缩放，包括文本边框和光标。

    如果使用的视频输出驱动后端有HiDPI比例报告的比例，则选项值将采用HiDPI比例。

``font``
    默认： 未设置（根据检测到的平台选择一个硬编码的字体）

    设置用于交互式解释器和控制台的字体。不一定要是等宽字体。

``font_size``
    默认： 16

    设置用于交互式解释器和控制台的字体大小。这将和scale相乘。

``border_size``
    默认： 1

    设置用于交互式解释器和控制台的字体边框大小。

``history_dedup``
    默认： yes

    删除历史记录中的重复条目，只保留最新的一项。
