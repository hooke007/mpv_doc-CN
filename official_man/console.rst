控制台
======

控制台是mpv中可输入命令的交互式解释器。它显示在视频窗口上。它也显示日志信息。它可以通过 ``--load-osd-console=no`` 选项完全禁用。

按键绑定
--------

\`
    显示控制台

ESC, Ctrl+[
    隐藏控制台

ENTER, Ctrl+J, Ctrl+M
    运行输入的命令

Shift+ENTER
    换行输入

LEFT, Ctrl+b
    移动光标至前一个字符

RIGHT, Ctrl+f
    移动光标至后一个字符

Ctrl+LEFT, Alt+b
    移动光标至当前单词的开头，如果在单词之间，则移到前一个单词的开头

Ctrl+RIGHT, Alt+f
    移动光标至当前单词的末尾，如果在单词之间，则移到后一个单词的结尾

HOME, Ctrl+a
    移动光标至当前行的开头

END, Ctrl+e
    移动光标至当前行的结尾

BACKSPACE, Ctrl+h
    删除前一个字符

Ctrl+d
    如果当前行是空的，隐藏控制台，否则删除后一个字符

Ctrl+BACKSPACE, Ctrl+w
    删除从光标到当前单词的开头的文本，如果在单词之间，则删除到前一个单词的开头

Ctrl+DEL, Alt+d
    删除从光标到当前单词的结尾的文本，如果在单词之间，则删除到下一个单词的结尾

Ctrl+u
    删除从光标到当前行开头的文本

Ctrl+k
    删除从光标到当前行结尾的文本

Ctrl+c
    删除当前行

UP, Ctrl+p
    向前浏览历史命令

DOWN, Ctrl+n
    向后浏览历史命令

PGUP
    转到历史命令的第一个命令

PGDN
    停止浏览历史命令

INSERT
    切换 插入/覆盖模式

Ctrl+v
    粘贴文本（在X11和Wayland上使用剪贴板）

Shift+INSERT
    粘贴文本（在X11和Wayland上使用primary selection）

TAB, Ctrl+i
    补全光标处的命令或属性名称。第一次按下时会插入补全内容的最长公共前缀，随后按下时会在它们之间循环。

Shift+TAB
    向后循环浏览补全信息

Ctrl+l
    清除控制台中的所有日志信息

命令
----

``script-message-to console type <text> [<cursor_pos>]``
    显示控制台并预填充所提供的文本，可选择指定初始光标位置为从1开始的正整数。

    .. admonition::  input.conf示例

        ``% script-message-to console type "seek  absolute-percent" 6``; keypress ESC" 6``
            （打开控制台）输入一个百分比位置，跳转并关闭控制台。

        ``Ctrl+o script-message-to console type "loadfile ''; keypress ESC" 11``
            输入要播放的文件或 URL。Tab 补全文件系统中的路径。

已知问题
--------

- Windows系统粘贴文本的速度慢
- 非ASCII键盘输入有限制
- 光标键在Unicode code-points之间移动，而不是在grapheme cluster之间移动

设置
----

这个脚本可以通过放置在mpv用户目录下的设置文件 ``script-opts/console.conf`` 和 ``--script-opts`` 命令行选项来定制。设置语法在 `mp.options functions`_ 中描述。

按键的绑定可以用标准的方式来改变，例如参见 stats.lua 文档。

设置选项
~~~~~~~~

``scale``
    默认： 1

    所有的绘制都按该值缩放，包括文本边框和光标。

    如果使用的视频输出驱动后端有HiDPI比例报告的比例，则选项值将采用HiDPI比例。

``font``
    默认： 未设置（根据检测到的平台选择一个硬编码的字体）

    设置用于交互式解释器和控制台的字体。必需是等宽字体才能正确对齐代码补全辅助。 

``font_size``
    默认： 16

    设置用于交互式解释器和控制台的字体大小。这将和scale相乘。

``border_size``
    默认： 1

    设置用于交互式解释器和控制台的字体边框大小。

``case_sensitive``
    默认： （windows为 yes ，其它平台为 no ）

    Tab 补全是否区分大小写，仅适用于 ASCII 字符。

``history_dedup``
    默认： yes

    删除历史记录中的重复条目，只保留最新的一项。

``font_hw_ratio``
    默认： auto

    字体高度与字体宽度的比例。调节代码补全辅助的表格宽度。对于一般的等宽字体，1.8-2.5 范围内的值是合理的。
