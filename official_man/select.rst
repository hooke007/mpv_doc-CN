选择器
======

通过 ``mp.input.select`` API，控制台可显示供浏览和选择的项目列表。 ``select.lua`` 是该 API 的内置client ，提供脚本命令绑定，用于收集和格式化要在控制台中选择的数据，并对所选项目进行操作。可以使用 ``--load-select=no`` 选项禁用它。

按键绑定
--------

当使用 ``mp.input.select`` 时， `控制台`_ 中列出的按键绑定会被扩展为以下内容：

ENTER, Ctrl+j, Ctrl+m
    确认选择当前聚焦的项目。

UP, Ctrl+p
    聚焦上面的项目，或当第一个项目被选择时聚焦最后一个项目。

DOWN, Ctrl+n
    聚焦下面的项目，或当最后一个项目被选择时聚焦第一个项目。

PGUP, Ctrl+b
    向上滚动一页。

PGDN, Ctrl+f
    向下滚动一页。

Ctrl+y
    将聚焦的项目复制到剪贴板。

MBTN_LEFT
    确认选择光标下的项目，或关闭控制台（如果在菜单矩形外点击）。

WHEEL_UP
    向上滚动。

WHEEL_DOWN
    向下滚动。

输入可打印字符会对显示的项目进行模糊搜索。

如果查询以 ``'`` 开头，则只过滤完全匹配的项目。你也可以指定多个以空格分隔的搜索条件，只有符合所有条件的项目才会被过滤。

脚本命令绑定
------------

默认情况下，select.lua 的脚本命令绑定会被绑定到 `键盘控制`_ 中列出的以 ``g`` 开头的按键序列。下面列出的脚本命令绑定名称，可用于将它们绑定到不同的按键上。

.. admonition:: 示例：在 input.conf 中重新绑定播放列表选择

    Ctrl+p script-binding select/select-playlist

可用的脚本命令绑定：

``select-playlist``
    选择一个播放列表条目。 ``--osd-playlist-entry`` 决定播放列表条目的格式。

``select-sid``
    选择一个字幕轨道，或禁用当前的轨道。

``select-secondary-sid``
    选择一个次字幕轨道，或禁用当前的轨道。

``select-aid``
    选择一个音频轨道，或禁用当前的轨道。

``select-vid``
    选择一个视频轨道，或禁用当前的轨道。

``select-track``
    选择一个任意类型轨道，或禁用当前的轨道。

``select-chapter``
    选择一个章节。

``select-edition``
    选择一个 MKV edition 或 DVD/Blu-ray 标题。

``select-subtitle-line``
    选择要查找的字幕行。此功能不适用于图像字幕。

    当前，这需要在 ``PATH`` 或在 Windows 下与 mpv 位于同一文件夹中的 ``ffmpeg`` 。

``select-audio-device``
    选择一个音频设备。

``select-watch-history``
    从稍后观看历史记录中选择文件。需要 ``--save-watch-history``

    如果尚未使用 ``--autocreate-playlist`` ，建议使用此脚本命令绑定启用它，以便用条目目录中的其它文件填充播放列表。

    .. admonition:: 示例：编辑 input.conf 以播放与历史条目相邻文件

        g-h script-binding select/select-watch-history; no-osd set autocreate-playlist filter

``select-watch-later``
    从稍后观看配置文件（参见 `恢复播放`_ ）中选择一个文件继续播放。需要 ``--write-filename-in-watch-later-config`` 。这与 ``--ignore-path-in-watch-later-config`` 无关。

    如果尚未使用 ``--autocreate-playlist`` ，建议使用此脚本命令绑定启用它，以便用条目目录中的其它文件填充播放列表。

    .. admonition:: 示例：编辑 input.conf 以播放与历史条目相邻文件

        g-w script-binding select/select-watch-later; no-osd set autocreate-playlist filter

``select-binding``
    列出已定义的输入绑定。你还可以选择一个来运行相关命令。

``show-properties``
    列出所有属性的名称和值。你还可以选择一个属性，在 OSD 上输出其值，这对被裁切的长值非常有用。

``edit-config-file``
    使用系统文本编辑器打开 ``mpv.conf`` 文件，若不存在则创建。

``edit-input-conf``
    使用系统文本编辑器打开 ``input.conf`` 文件，若不存在则创建。

``open-docs``
    在浏览器中打开mpv的在线文档。

``menu``
    显示一个杂项条目的菜单。

设置
----

该脚本可以通过 mpv 用户目录下的设置文件 ``script-opts/select.conf`` 和命令行选项 ``--script-opts` 进行自定义。设置语法在 `mp.options functions`_ 中描述。

设置选项
~~~~~~~~

``history_date_format``
    默认： %Y-%m-%d %H:%M:%S

    历史条目的日期格式。它将传递给 Lua 的 ``os.date`` ，后者使用与 ``strftime(3)`` 相同的格式。

``hide_history_duplicates``
    默认： yes

    是否只显示路径相同的历史条目中的最后一个。
