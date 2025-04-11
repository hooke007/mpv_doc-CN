屏显式控制器
============

屏显式控制器（简称：OSC）是一个与mpv集成的最小GUI，提供基本的鼠标操控功能。它的目的是使新用户的交互更容易，并且能够精确和直接的进行进度查询。

如果mpv在编译时支持Lua，那么OSC是默认启用的。它可以通过选项 ``--osc=no`` 完全禁用。

使用OSC
-------

默认情况下，只要光标在播放器窗口内移动，OSC就会显示；如果光标在OSC外超过0.5秒没有移动，或者光标离开窗口，OSC就会隐藏。

界面
~~~~

::

    +------+----------+----------+----------------------------------------------------------+
    | 菜单 | 上一文件 | 下一文件 | 标题                                            缓存指示 |
    +------+-+--------+-+--------+-+------+----------------------+------+----+----+----+----+
    |   播   |   上一   |   下一   | 已过 | 进度条               | 剩余 | 音 | 字 | 音 | 全 |
    |   放   |   章节   |   章节   | 时间 |                      | 时间 | 轨 | 幕 | 量 | 屏 |
    +--------+----------+----------+------+----------------------+------+----+----+----+----+


菜单
    =============   ================================================
    左键单击        打开菜单
    =============   ================================================

上一文件
    =============   ================================================
    左键单击        播放列表中的上一个文件
    shift左键单击   显示播放列表
    中键单击        显示播放列表
    右键单击        打开播放列表菜单
    =============   ================================================

下一文件
    =============   ================================================
    左键单击        播放列表中的下一个文件
    shift左键单击   显示播放列表
    中键单击        显示播放列表
    右键单击        打开播放列表菜单
    =============   ================================================

标题
    | 显示当前播放列表位置和媒体标题、文件名或自定义标题，或悬停在进度条上的目标章节名称。

    =============   ================================================
    左键单击        显示文件和轨道信息
    shift左键单击   显示路径
    中键单击        显示路径
    右键单击        打开历史菜单
    =============   ================================================

缓存指示
    | 显示当前的缓冲状态

播放
    =============   ================================================
    左键单击        切换 播放/暂停
    shift左键单击   切换 无限循环播放列表
    中键单击        切换 无限循环播放列表
    右键单击        切换 无限循环当前文件
    =============   ================================================

上一章节
    =============   ================================================
    左键单击        跳转章节开头/上一章节
    shift左键单击   显示章节列表
    中键单击        显示章节列表
    右键单击        打开章节菜单
    =============   ================================================

下一章节
    =============   ================================================
    左键单击        跳转下一章节
    shift左键单击   显示章节列表
    中键单击        显示章节列表
    右键单击        打开章节菜单
    =============   ================================================

已过时间
    | 显示当前播放位置的时间戳

    =============   ================================================
    左键单击        切换 显示带毫秒的时间码
    =============   ================================================

进度条
    | 显示当前的播放位置和章节的位置

    =============   ================================================
    左键单击        跳转至位置
    右键单击        跳转至最近章节
    鼠标滚轮        前进/后退
    =============   ================================================

剩余时间
    | 显示剩余播放时间的时间戳

    =============   ================================================
    左键单击        切换 总时间/剩余时间
    =============   ================================================

音轨 字幕
    | 显示所选轨道的可用数量

    =============   ================================================
    左键单击        循环 音频/字幕轨 前进
    shift左键单击   循环 音频/字幕轨 后退
    中键单击        循环 音频/字幕轨 后退
    右键单击        打开音频/字幕轨菜单
    鼠标滚轮        循环 音频/字幕轨 前进/后退
    =============   ================================================

音量
    =============   ================================================
    左键单击        切换 静音
    右键单击        打开音频设备菜单
    滚轮滚动        音量增大/减小
    =============   ================================================

全屏
    =============   ================================================
    左键单击        切换 全屏
    右键单击        切换 窗口最大化
    =============   ================================================

自 mpv 0.40.0 起，可以在某些界面元素上配置命令与鼠标指令同时运行，而且一些元素的默认行为也有所更改。如果你怀念某些旧行为，请查看 mpv git 仓库中的 ``etc/restore-osc-bindings.conf`` 。

按键绑定
~~~~~~~~

如果没有其他命令已经绑定在这些键上，这些键的绑定默认是激活的。在发生冲突的情况下，需要将该功能绑定到不同的按键上。参见 `脚本命令`_ 部分。

=============   ================================================
del             循环 OSC可见性 始终隐藏/自动显示/始终显示
=============   ================================================

设置
----

可以通过 mpv 用户目录下的设置文件 ``script-opts/osc.conf`` 和命令行选项 ``--script-opts`` 来定制该脚本。设置语法记录在 `mp.options functions`_ 部分。

命令行语法
~~~~~~~~~~

为了避免与其他脚本发生冲突，所有选项都需要以 ``osc-`` 为前缀。

示例::

    --script-opts=osc-optionA=value1,osc-optionB=value2


设置选项
~~~~~~~~

``layout``
    默认： ``bottombar``

    OSC的布局。目前可用的有：box, slimbox, bottombar, topbar, slimbottombar, slimtopbar 。0.21.0之前的默认值是 box

``seekbarstyle``
    默认： bar

    设置播放位置标记的样式和进度条的整体形状： ``bar``, ``diamond`` 或 ``knob`` 

``seekbarhandlesize``
    默认： 0.6

    如果 ``seekbarstyle`` 被设置为 ``diamond`` 或 ``knob`` ，播放位置标记的大小比例。这是相对于进度条的全部高度而言的。

``seekbarkeyframes``
    默认： yes

    控制拖动进度条时使用的搜索模式。如果设置为 ``yes`` ，则使用默认的搜索模式（通常是关键帧，但播放器的默认和启发式方法可以将其改为精确）。如果设置为 ``no`` ，将使用鼠标拖动的精确搜索方式。关键帧是首选，但在找不到关键帧的情况下，精确搜索可能是有用的。请注意，使用精确搜索有可能使鼠标拖动的速度更慢。

``seekrangestyle``
    默认： ``inverted``

    在进度条上显示可搜索的范围。 ``bar`` 显示它们在进度条的全部高度上， ``line`` 是一条粗线， ``inverted`` 是一条细线，在播放位置标记上反色。 ``none`` 将隐藏。此外， ``slider`` 将在进度条内显示永久的线条，里面标有缓存范围。请注意，这些会根据seekbarstyle选项的不同而有所差异。另外， ``slider`` 在 ``seekbarstyle`` 设置为 ``bar`` 时无效。

``seekrangeseparate``
    默认： yes

    控制如果 ``seekbarstyle`` 设置为 ``bar`` ，是否在进度条的顶部显示线型可寻范围，或者单独显示。

``seekrangealpha``
    默认： 200

    可搜寻范围的透明度，0（不透明）到255（完全透明）

``scrollcontrols``
    默认： yes

    默认情况下，如果鼠标悬停在 OSC 元素上，使用鼠标滚轮上下滚动会触发某些操作（例如seek）。设置为 ``no`` 可禁用任何特殊的鼠标滚轮行为。

``deadzonesize``
    默认： 0.5

    死区的大小。死区是一个区域，使鼠标像离开窗口一样。在那里移动不会使OSC显示出来，如果鼠标进入该区域，它将立即隐藏。死区从与OSC相对的窗口边界开始，其大小控制它在窗口中的跨度。值在0.0和1.0之间，其中0意味着OSC将总是随着鼠标在窗口中的移动而弹出，1意味着OSC只在鼠标悬停时显示。0.21.0之前的默认值是0。

``minmousemove``
    默认： 0

    鼠标在刻度之间移动的最小像素量，使OSC显示出来。0.21.0之前的默认值是3。

``showwindowed``
    默认： yes

    在窗口状态下启用OSC

``showfullscreen``
    默认： yes

    全屏时启用OSC

``idlescreen``
    默认： yes

    空闲状态下显示mpv的logo和文字

``scalewindowed``
    默认： 1.0

    窗口化时OSC的比例系数

``scalefullscreen``
    默认： 1.0

    全屏时OSC的比例系数

``vidscale``
    默认： auto

    随视频的比例缩放OSC。 ``no`` 试图在窗口大小允许的范围内保持OSC大小不变。 ``auto`` 缩放OSC和OSD随窗口缩放或保持恒定大小，具体取决于 ``--osd-scale-by-window`` 选项。

``valign``
    默认： 0.8

    垂直对齐（仅box或slimbox布局有效），-1（顶部）到1（底部）

``halign``
    默认： 0.0

    水平对齐（仅box或slimbox布局有效），-1（左侧）到1（右侧）

``barmargin``
    默认： 0

    底部（仅bottomombar或slimbottombar布局有效）或顶部（仅topbar或slimtopbar布局有效）的边距，单位是像素

``boxalpha``
    默认： 80

    背景的透明度，0（不透明）到255（完全透明）

``hidetimeout``
    默认： 500

    在没有鼠标移动的情况下，OSC隐藏的时间，以ms为单位，不能是负数

``fadeduration``
    默认： 200

    淡入淡出的持续时间，以ms为单位，0=不淡出

``fadein``
    默认： no

    启用淡入效果。

``title``
    默认： ${!playlist-count==1:[${playlist-pos-1}/${playlist-count}] }${media-title}

    支持属性扩展的字符串，将被显示为OSC标题。ASS标签被转义，换行被转换为空格。

``tooltipborder``
    默认： 1

    使用bottombar或topbar布局时，搜寻时间码的大小

``timetotal``
    默认： no

    显示总时间而不是剩余时间

``remaining_playtime``
    默认： yes

    时间剩余显示是否考虑播放速度。 ``yes`` - 考虑当前速度下还剩多少播放时间。 ``no`` - 考虑视频时长下还剩多少时间。

``timems``
    默认： no

    显示带毫秒的时间码

``tcspace``
    默认： 100 （允许的范围： 50-200 ）

    调整 ``bottombar`` 和 ``topbar`` 布局中为时间码（当前时间和剩余时间）保留的空间。时间码的宽度取决于字体，对于某些字体，时间码附近的间距变得太小。使用高于100的值来增加间距，或低于100的值来减少间距。

``visibility``
    默认： auto （鼠标移动时自动隐藏/显示）

    也支持 ``never`` 和 ``always``

``visibility_modes``
    默认： never_auto_always

    调用 osc-visibility 循环script message时要循环切换显示的visibility模式列表。模式之间用 ``_`` 分隔。

``boxmaxchars``
    默认： 80

    mpv不能测量屏幕上的文本宽度，所以需要用字符数来限制。默认值是保守的，允许使用等宽字体而不溢出。然而，对于许多常见的字体，可以使用一个更大的数字。请自行斟酌。

``boxvideo``
    默认： no

    是否在视频上覆盖osc（ ``no`` ），或在osc未覆盖的区域内框住视频（ ``yes`` ）。如果设置了这个选项，osc可能会覆盖 ``--video-margin-ratio-*`` 选项，即使用户已经设置了它们（如果所有选项都被设置为默认值，则不会覆盖它们）。此外， ``visibility`` 必须被设置为 ``always`` 。否则，这个选项没有任何效果。

    目前，只支持 ``bottombar``, ``slimbottombar``, ``topbar``, ``slimtopbar`` 的布局。如果设置了这个选项，其他的布局就不会改变。另外，如果存在窗口控件（见下文），无论使用哪种OSC布局，它们都会受到影响。

    边框是静态的，即使OSC被设置为只在鼠标交互时出现，边框也会出现。如果OSC是不可见的，边框就会简单地用背景色（默认为黑色）填充。

    目前这仍然会使OSC与字幕重叠（如果 ``--sub-use-margins`` 选项被设置为 ``yes`` ，默认）。这可能会在以后修复。

    这在个别视频输出驱动中不能正常工作，如 ``--vo=xv`` ，它将OSD渲染进未缩放的视频中。

``windowcontrols``
    默认： auto （如果没有窗口边框就显示窗口控件）

    是否在视频上显示窗口管理控件，如果明确，则放在窗口的一边。当窗口没有装饰时，这可能是可取的，因为它们被明确地禁用（ ``border=no`` ）或者因为当前平台不支持它们（例如：gnome-shell与wayland）。

    窗口控件是固定的，提供 ``minimize``, ``maximize`` 和 ``quit`` 。不是所有的平台都实现了 ``minimize`` 和 ``maximize`` ，但 ``quit`` 总是有效的。

``windowcontrols_alignment``
    默认： right

    如果窗口控件被显示出来，显示它们应该向一边对齐。

    ``left`` 和 ``right`` 支持将把控件放在左侧和右侧。

``windowcontrols_title``
    默认： ${media-title}

    支持属性扩展的字符串，将显示为窗口控件的标题。ASS 标签会被转义，换行符和尾部斜杠会被剥离。

``greenandgrumpy``
    默认： no

    设置为 ``yes`` 以减少节日气氛（例如，在12月禁用圣诞帽）

``livemarkers``
    默认： yes

    在持续时间变化时更新章节标记的位置，例如，直播流。状态更新尚未优化 —— 考虑在非常低端的系统上禁用它。

``chapter_fmt``
    默认： ``Chapter: %s``

    当悬停在进度条上时，显示章节名称的模板。使用 ``no`` 来禁止悬停时的章节显示。否则，它是一个lua ``string.format`` 模板， ``%s`` 被替换成实际的名字。

``unicodeminus``
    默认： no

    在显示剩余播放时间时，使用Unicode减号而不是ASCII连字符。

``background_color``
    默认： #000000

    Sets the background color of the OSC.

``timecode_color``
    默认： #FFFFFF

    Sets the color of the timecode and seekbar, of the OSC.

``title_color``
    默认： #FFFFFF

    Sets the color of the video title. Formatted as #RRGGBB.

``time_pos_color``
    默认： #FFFFFF

    Sets the color of the timecode at hover position in the seekbar.

``time_pos_outline_color``
    默认： #FFFFFF

    Sets the color of the timecode's outline at hover position in the seekbar. Also affects the timecode in the slimbox layout.

``buttons_color``
    默认： #FFFFFF

    Sets the colors of the big buttons.

``top_buttons_color``
    默认： #FFFFFF

    Sets the colors of the top buttons.

``small_buttonsL_color``
    默认： #FFFFFF

    Sets the colors of the small buttons on the left in the box layout.

``small_buttonsR_color``
    默认： #FFFFFF

    Sets the colors of the small buttons on the right in the box layout.

``held_element_color``
    默认： #999999

    Sets the colors of the elements that are being pressed or held down.

``tick_delay``
    默认： 1/60

    设置以秒为单位的 OSC 重绘最小间隔时间。在运行速度较快的系统中，可以缩短这一间隔，使 OSC 渲染更流畅。

    如果 ``tick_delay_follow_display_fps`` 设置为 yes ，且 VO 支持 ``display-fps`` 属性，则忽略该设置。

``tick_delay_follow_display_fps``
    默认： no

    使用显示帧频计算 OSC 重绘的间隔时间。

以下选项可配置点击按钮时运行的命令。 ``shift+mbtn_left`` 也会触发 ``mbtn_mid`` 的命令。

``menu_mbtn_left_command=script-binding select/menu; script-message-to osc osc-hide``

``menu_mbtn_mid_command=``

``menu_mbtn_right_command=``

``playlist_prev_mbtn_left_command=playlist-prev; show-text ${playlist} 3000``

``playlist_prev_mbtn_mid_command=show-text ${playlist} 3000``

``playlist_prev_mbtn_right_command=script-binding select/select-playlist; script-message-to osc osc-hide``

``playlist_next_mbtn_left_command=playlist-next; show-text ${playlist} 3000``

``playlist_next_mbtn_mid_command=show-text ${playlist} 3000``

``playlist_next_mbtn_right_command=script-binding select/select-playlist; script-message-to osc osc-hide``

``title_mbtn_left_command=script-binding stats/display-page-5``

``title_mbtn_mid_command=show-text ${path}``

``title_mbtn_right_command=script-binding select/select-watch-history; script-message-to osc osc-hide``

``play_pause_mbtn_left_command=cycle pause``

``play_pause_mbtn_mid_command=cycle-values loop-playlist inf no``

``play_pause_mbtn_right_command=cycle-values loop-file inf no``

``chapter_prev_mbtn_left_command=osd-msg add chapter -1``

``chapter_prev_mbtn_mid_command=show-text ${chapter-list} 3000``

``chapter_prev_mbtn_right_command=script-binding select/select-chapter; script-message-to osc osc-hide``

``chapter_next_mbtn_left_command=osd-msg add chapter 1``

``chapter_next_mbtn_mid_command=show-text ${chapter-list} 3000``

``chapter_next_mbtn_right_command=script-binding select/select-chapter; script-message-to osc osc-hide``

``audio_track_mbtn_left_command=cycle audio``

``audio_track_mbtn_mid_command=cycle audio down``

``audio_track_mbtn_right_command=script-binding select/select-aid; script-message-to osc osc-hide``

``audio_track_wheel_down_command=cycle audio``

``audio_track_wheel_up_command=cycle audio down``

``sub_track_mbtn_left_command=cycle sub``

``sub_track_mbtn_mid_command=cycle sub down``

``sub_track_mbtn_right_command=script-binding select/select-sid; script-message-to osc osc-hide``

``sub_track_wheel_down_command=cycle sub``

``sub_track_wheel_up_command=cycle sub down``

``volume_mbtn_left_command=no-osd cycle mute``

``volume_mbtn_mid_command=``

``volume_mbtn_right_command=script-binding select/select-audio-device; script-message-to osc osc-hide``

``volume_wheel_down_command=add volume -5``

``volume_wheel_up_command=add volume 5``

``fullscreen_mbtn_left_command="cycle fullscreen"``

``fullscreen_mbtn_mid_command=``

``fullscreen_mbtn_right_command="cycle window-maximized"``

自定义按钮
~~~~~~~~~~

额外脚本选项可用于在 ``bottombar`` 和 ``topbar`` 布局中定义自定义按钮。

.. admonition:: 示例：添加循环播放、播放列表洗牌和速度变更按钮

    ::

        custom_button_1_content=🔁
        custom_button_1_mbtn_left_command=cycle-values loop-file inf no
        custom_button_1_mbtn_right_command=cycle-values loop-playlist inf no

        custom_button_2_content=🔀
        custom_button_2_mbtn_left_command=playlist-shuffle

        custom_button_3_content=⏱
        custom_button_3_mbtn_left_command=add speed 1
        custom_button_3_mbtn_right_command=set speed 1
        custom_button_3_wheel_up_command=add speed 0.25
        custom_button_3_wheel_down_command=add speed -0.25

脚本命令
~~~~~~~~

OSC脚本会监听某些脚本命令。这些命令可以绑定在 ``input.conf`` 中，或者由其他脚本发送。

``osc-visibility``
    控制可见性模式 ``never`` / ``auto`` （在鼠标移动时）/ ``always`` 和 ``cycle`` 在各种模式之间循环。如果传入第二个参数（任意值），则 OSD 上的输出将被静默。

``osc-show``
    触发 OSC 显示，就像用户移动鼠标一样。

``osc-hide``
    当 ``visibility`` 为 ``auto`` 时，隐藏 OSC。

示例

你可以把这个放到 ``input.conf`` 中，用 ``a`` 键隐藏OSC，用 ``b`` 键设置自动模式（默认）::

    a script-message osc-visibility never
    b script-message osc-visibility auto

``osc-idlescreen``
    控制空闲状态时mpv的logo可见性。有效的参数是 ``yes`` ``no`` ，也可用 ``cycle`` 来切换。如果传入第二个参数（任意值），则 OSD 上的输出将被静默。
