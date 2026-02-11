上下文菜单脚本
==============

上下文菜单是可在视频窗口上弹出的菜单。在默认情况下，它与鼠标右键点击绑定。

menu.conf
---------

你可以在 ``~~/menu.conf`` （参见 `文件`_ ）中定义自定义菜单，或通过 ``--script-opt=select-menu_conf_path`` 指定替代路径。建议以 https://github.com/mpv-player/mpv/blob/master/etc/menu.conf 中的默认 ``menu.conf`` 文件作为示例配置开始。

``menu.conf`` 中的每一行代表一个菜单项，各字段以一个或多个制表符分隔。首个字段为菜单都显示文本，次字段通常为选中该项时执行的命令。第三个字段起可通过与 `附带条件的自动配置预设`_ 相同的方式指定 ``checked=`` 、 ``disabled=`` 和 ``hidden=`` 状态。

若未指定命令，该项将展开子菜单。下方首行缩进的字段将添加至该子菜单。可通过增加比父菜单项更多的首行缩进来定义嵌套子菜单项。

空行被视为分隔符。

第二个字段也可使用以下词元使该项成为包含相对项的子菜单： ``$playlist``, ``$tracks``, ``$video-tracks``, ``$audio-tracks``, ``$sub-tracks``, ``$secondary-sub-tracks``, ``$chapters``, ``$editions``, ``$audio-devices``, ``$profiles`` 。这些子菜单在内容为空时会自动禁用。

要使用原生上下文菜单，你需要将菜单定义数据填充 ``menu-data`` 属性，并调用 ``context-menu`` 命令。在内置脚本中，此操作由 ``select.lua`` 实现：该脚本解析 ``menu.conf`` 文件填充 ``menu-data`` ，随后在支持原生上下文菜单集成的平台上调用 ``context-menu`` 命令，而在未集成平台则直接调用 ``context_menu.lua`` 。

在未集成原生上下文菜单的平台上，可通过 ``--load-context-menu=no`` 选项完全禁用 ``context_menu.lua`` 。而在已实现集成的平台上，该脚本默认处于禁用状态，使用 ``--load-context-menu=yes`` 选项可使 ``select.lua`` 调用其功能。

脚本消息
--------

``open``
    显示上下文菜单。

``select``
    当存在聚焦项时，选择该条目。

设置
----

该脚本可通过放置在mpv用户目录下的设置文件 ``script-opts/context_menu.conf`` 以及命令行选项 ``--script-opts`` 进行定制。设置语法详见 `mp.options functions`_

设置选项
~~~~~~~~

``font_size``
    默认： 14

    字体尺寸

``gap``
    默认： 0.2

    菜单项之间的间距，以字体大小的百分比形式指定。

``padding_x``
    默认： 8

    菜单的水平填充距离。

``padding_y``
    默认： 4

    菜单的垂直填充距离。

``menu_outline_size``
    默认： 0

    菜单边框的尺寸。

``menu_outline_color``
    默认： ``#FFFFFF``

    菜单边框的颜色。

``corner_radius``
    默认： 5

    菜单边角的半径。

``scale_with_window``
    默认： auto

    是否根据窗口高度缩放尺寸。可选值为 ``yes`` ``no`` ``auto`` ，其中 ``auto`` 将遵循 ``--osd-scale-by-window`` 的设置值。

    当尺寸未随窗口缩放时，将依据``display-hidpi-scale``进行缩放。

``focused_color``
    默认： ``#222222``

    聚焦项的颜色。

``focused_back_color``
    默认： ``#FFFFFF``

    聚焦项的背景颜色。

``disabled_color``
    默认： ``#555555``

    禁用项和分隔符的颜色。

``seconds_to_open_submenus``
    默认： 0.2

    光标移入关联子菜单项后，该子菜单开启的延长时间（秒）。

``seconds_to_close_submenus``
    默认： 0.2

    光标进入父级菜单后，关闭子菜单所需等待的秒数。
