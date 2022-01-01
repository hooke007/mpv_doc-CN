CONSOLE
=======

控制台是mpv输入命令的REPL。它显示在视频窗口上。它也显示日志信息。它可以通过 ``--load-osd-console=no`` 选项完全禁用。

Keybindings
-----------

\`
    显示控制台。

ESC
    隐藏控制台。

ENTER, Ctrl+J 和 Ctrl+M
    运行输入的命令。

Shift+ENTER
    键入一个字面的换行字符。

LEFT 和 Ctrl+B
    将光标移至前一个字符。

RIGHT 和 Ctrl+F
    将光标移至下一个字符。

Ctrl+LEFT 和 Alt+B
    将光标移到当前单词的开头，如果在单词之间，则移到前一个单词的开头。

Ctrl+RIGHT 和 Alt+F
    将光标移到当前字的末尾，如果在字与字之间，则移到下一个字的末尾。

HOME 和 Ctrl+A
    将光标移到当前行的开头。

END 和 Ctrl+E
    将光标移到当前行的末尾。

BACKSPACE 和 Ctrl+H
    删除前一个字符。

Ctrl+D
    如果当前行是空的，则隐藏控制台，否则删除下一个字符。

Ctrl+BACKSPACE 和 Ctrl+W
    删除从光标到当前字的开头的文本，如果在字与字之间，则删除到前一个字的开头。

Ctrl+DEL 和 Alt+D
    删除从光标到当前单词的结尾的文本，如果在单词之间，则删除到下一个单词的结尾。

Ctrl+U
    删除从光标到当前行的开头的文本。

Ctrl+K
    删除从光标到当前行末的文本。

Ctrl+C
    清除当前行。

UP 和 Ctrl+P
    在命令历史中向后移动。

DOWN 和 Ctrl+N
    在命令历史中向前移动。

PGUP
    转到历史上的第一个命令。

PGDN
    停止浏览命令历史。

INSERT
    切换插入模式。

Ctrl+V
    粘贴文本（在X11和Wayland上使用剪贴板）。

Shift+INSERT
    粘贴文本（在X11和Wayland上使用主选区）。

TAB 和 Ctrl+I
    完成光标处的命令或属性名称。

Ctrl+L
    清除控制台中的所有日志信息。

Commands
--------

``script-message-to console type <text> [<cursor_pos>]``
    显示控制台并预先填入所提供的文本，可选择指定初始光标位置为从1开始的正整数。

    .. admonition::  input.conf示例

        ``% script-message-to console type "seek  absolute-percent" 6``

Known issues
------------

- 在Windows上粘贴文本很慢
- 非ASCII键盘输入有限制
- 光标键在Unicode编码点之间移动，而不是在字素群之间移动

Configuration
-------------

这个脚本可以通过放置在mpv用户目录下的配置文件 ``script-opts/console.conf`` 和 ``--script-opts`` 命令行选项来定制。配置语法在 `ON SCREEN CONTROLLER`_ 中描述。

按键的绑定可以用标准的方式来改变，例如参见 stats.lua 文档。

Configurable Options
~~~~~~~~~~~~~~~~~~~~

``scale``
    默认： 1

    所有的绘图都按这个值缩放，包括文本边框和光标。

    如果使用的VO后端有HiDPI比例报告，则选项值将以报告的HiDPI比例进行缩放。

``font``
    默认： 未设置（根据检测到的平台选择一个硬编码的字体）

    设置用于REPL和控制台的字体。这可能不一定是一种等宽字体。

``font_size``
    默认： 16

    设置用于 REPL 和控制台的字体大小。这将被乘以 "比例"。
