统计数据
========

该内置脚本显示当前播放文件的信息和统计数据。如果mpv在编译时支持Lua，它就会默认启用。可以通过 ``--load-stats-overlay=no`` 选项完全禁用它。

使用
----

下面的按键绑定默认是激活的，除非有其他功能已经被绑定：

====   ==============================================
i      只在一个固定的时间段内显示统计数据
I      切换 显示/隐藏统计数据（再次切换前始终显示）
?      切换 显示按键绑定列表
====   ==============================================

当统计数据在屏幕上可见时，以下的按键绑定是激活的，无视之前已有的绑定。它们允许你在 *不同页面* 的统计数据之间切换：

====   ========================
1      显示通用信息
2      显示帧计时（可滚动）
3      输入缓存统计
4      激活的按键绑定（可滚动）
5      选中的轨道信息（可滚动）
0      内部活动（可滚动）
====   ========================

如果统计数据以已打开，这些按键的绑定也是激活的：

====   ==================
ESC    关闭统计数据
====   ==================

在支持滚动的页面上，这些按键的绑定也是激活的：

====   ==================
UP     向上滚动一行
DOWN   向下滚动一行
====   ==================

在第 4 页，这些按键的绑定也是激活的：

====   ==================
/      搜索按键绑定
====   ==================

设置
----

该脚本可以通过放置在mpv用户目录下的设置文件 ``script-opts/stats.conf`` 和 ``--script-opts`` 命令行选项来定制。设置语法在 `mp.options functions`_ 中已描述。

设置选项
~~~~~~~~

``key_page_1``
    默认： 1
``key_page_2``
    默认： 2
``key_page_3``
    默认： 3
``key_page_4``
    默认： 4
``key_page_5``
    默认： 5
``key_page_0``
    默认： 0
``key_exit``
    默认： ESC

    在显示统计数据时进行页面切换的按键绑定

``key_scroll_up``
    默认： UP
``key_scroll_down``
    默认： DOWN
``key_scroll_search``
    默认： /
``scroll_lines``
    默认： 1

    滚动操作的按键绑定和在支持它的页面上单次滚动的行数

``duration``
    默认： 4

    统计数据的持续显示时间，以秒为单位（固定时间段显示时）

``redraw_delay``
    默认： 1

    统计数据的刷新间隔时间，以秒为单位（始终显示时）

``persistent_overlay``
    默认： no

    当 `no` 时，其它脚本输出到屏幕的文本的可以覆盖已显示的统计数据。当 `yes` 时，显示的统计数据会在对应的时间段内持续显示。当多个脚本决定同时输出文本时，这可能导致文本重叠。

``file_tag_max_length``
    默认： 128

    只显示短于此长度（以字节为单位）的文件标签。

``file_tag_max_count``
    默认： 16

    只显示首个指定数量的文件标签。

``term_clip``
    默认： yes

    是否按终端宽度截断行。

``plot_perfdata``
    默认： yes

    显示性能数据的图表（第2页）

``plot_vsync_ratio``
    默认： yes
``plot_vsync_jitter``
    默认： yes

    显示vsync和jitter值的图表（第1页）。只有在始终显示时才显示。

``plot_tonemapping_lut``
    默认： no

    自动启用色调映射LUT可视化。仅在切换时启用。

``flush_graph_data``
    默认： yes

    在始终显示时清除用于绘制图形的数据缓存

``font``
    默认： 与 ``--osd-font`` 一致

    字体名称。应支持尽可能多的字重来获得最佳的视觉体验。

``font_mono``
    默认： monospace

    用于对齐文本所必需的等宽字体名称。目前，monospaced digits已足够。

``font_size``
    默认： 20

    用于渲染文本的字体大小

``font_color``
    默认： 与 ``--osd-color`` 一致

    文本颜色

``border_size``
    默认： 1.65

    围绕字体绘制的边框大小

``border_color``
    默认： 与 ``--osd-border-color`` 一致

    文本边框的颜色

``shadow_x_offset``
    默认： 与 ``--osd-shadow-offset`` 一致

    阴影与文字之间的水平距离。

``shadow_y_offset``
    默认： 与 ``--osd-shadow-offset`` 一致

    阴影与文字之间的垂直距离。

``shadow_color``
    默认： 与 ``--osd-shadow-color`` 一致

    文本阴影3的颜色

``alpha``
    默认： 11

    指定 ``font_color`` 时文本的透明度，指定 ``border_color`` 时文本边框的透明度，指定 ``shadow_color`` 时文本阴影的透明度。

``plot_bg_border_color``
    默认： 0000FF

    用于绘制图形的边框颜色

``plot_bg_border_width``
    默认： 1.25

    用于绘制图形的边框宽度

``plot_bg_color``
    默认： 262626

    用于绘制图形的背景颜色

``plot_color``
    默认： FFFFFF

    用于绘制图形的颜色

``vidscale``
    默认： auto

    根据视频缩放文本和图表。 ``no`` 试图保持大小不变。 ``auto``会根据 ``--osd-scale-by-window`` 选项，将文字和图形与 OSD 一起缩放或保持恒定大小。

注意：颜色为十六进制值，并使用ASS标签的顺序。BBGGRR（蓝绿红）。

不同的按键绑定
~~~~~~~~~~~~~~

可以在 ``input.conf`` 中设置额外的按键来显示统计数据::

    e script-binding stats/display-stats
    E script-binding stats/display-stats-toggle

以及直接显示某个页面::

    i script-binding stats/display-page-1
    h script-binding stats/display-page-4-toggle

激活的按键绑定的页面
~~~~~~~~~~~~~~~~~~~~

列出激活的按键绑定和它们所绑定的命令，不包括统计数据脚本本身的交互键。也参见 ``--input-test`` 以获得每个绑定的更详细信息。

这些按键是通过对命令字符串的简单分析而自动分组的，不应该期望文件级别的分组精度，然而，它仍然应该是相当有用的。

使用 ``--idle --script-opts=stats-bindlist=yes`` 会将列表输出到终端并立即退出。除非使用 ``--script-opt=stats-term_clip=no`` 禁用该行为，否则长行将按终端宽度裁切。在 ``yes`` 前添加 ``-`` 可禁用转义序列，即 ```--script-opt=stats-bindlist=-yes`` 。

和 ``--input-test`` 一样，列表中包括来自 ``input.conf`` 和用户脚本的绑定。使用 ``--no-config`` 只列出内建的绑定。

内部活动的页面
~~~~~~~~~~~~~~

该页显示的大多数条目都有相当模糊的含义。可能这些东西对你无用。不要试图使用它。忘记它的存在。

首次选择这个页面将开始收集一些内部性能数据。这意味着在播放器运行的其余时间里，性能会比正常情况下略低（即使统计数据页面被关闭）。注意，统计数据页面本身会使用大量的CPU甚至GPU资源，可能会对性能产生严重影响。

显示的信息在redraw delay时积累（显示为 ``poll-time`` 字段）

它为每个Lua脚本增加了条目。如果有太多的脚本在运行，列表中的部分内容会简单地排列超出屏幕，但可以滚动浏览。

如果底层平台不支持pthread per thread times，显示的时间将是0或随机的（我怀疑在写本文时，只有Linux通过pthread APIs提供了正确的per thread times）。

大多数条目都是懒散的添加的，而且只在数据收集期间增加，这就是为什么一些条目可能会在一段时间后随机出现。这也是为什么自数据收集开始后，一直不活动的脚本的内存使用条目会消失。

Memory usage是近似情况，并不反映internal fragmentation 。

JS脚本内存报告默认情况下是禁用的，因为在JS端收集数据会增加开销并增加内存使用。可以通过在启动mpv之前设置 ``--js-memory-report`` 选项来启用它。

如果条目有 ``/time`` 和 ``/cpu`` 变量，前者给出真实时间（monotonic clock），而后者给出thread CPU time（只有当相应的pthread API工作并被支持时）。
