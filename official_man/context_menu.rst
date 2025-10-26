上下文菜单脚本
==============

此脚本为未集成原生上下文菜单的平台提供替代方案。在这些平台上，可通过 ``--load-context-menu=no`` 选项完全禁用该功能。而在已实现原生集成的平台上，该功能默认处于禁用状态。

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

    禁用项的颜色。

``seconds_to_open_submenus``
    默认： 0.2

    光标移入关联子菜单项后，该子菜单开启的延长时间（秒）。

``seconds_to_close_submenus``
    默认： 0.2

    光标进入父级菜单后，关闭子菜单所需等待的秒数。
