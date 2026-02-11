OSD命令行
=========

该脚本允许在控制台中交互式运行和完成输入命令，并将 mpv 的日志添加到控制台的日志中。

按键绑定
--------

\`
    打开控制台输入命令。

命令
----

``script-binding commands/open``

    打开控制台输入命令。

``script-message-to commands type <text> [<cursor_pos>]``
    显示控制台并用提供的文本预先填充，可选择指定初始光标位置为从 1. 开始的正整数。运行命令后控制台自动关闭。

    .. admonition:: input.conf 示例

        ``% script-message-to commands type "seek  absolute-percent" 6``
            输入要跳转到的百分比位置。

        ``Ctrl+o script-message-to commands type "loadfile ''" 11``
            输入要播放的文件或 URL，并自动补全文件系统中的路径。

设置
----

该脚本可以通过 mpv 用户目录下的设置文件  ``script-opts/commands.conf`` 和命令行选项 ``--script-opts`` 进行自定义。设置语法在 `mp.options functions`_ 中描述。

设置选项
~~~~~~~~

``persist_history``
    默认： no

    是否将命令历史保存到文件并在下次加载。

``history_path``
    默认： ``~~state/command_history.txt``

    ``persist_history`` 的文件路径（参见 `文件`_ ）

``remember_input``
    默认： yes

    是否在关闭控制台时记住输入的行和光标位置，并在下次打开时预填充。
