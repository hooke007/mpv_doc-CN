位移器
======

该脚本提供了平移视频和图像的脚本按键绑定。可以使用 ``--load-positioning=no`` 选项禁用它。

脚本命令绑定
------------

``pan-x <amount>``
    调节 ``--video-align-x`` 相对于 OSD 宽度，而不是像选项那样相对于视频宽度。这对于连续平移大型图像非常有用。

    ``amount`` 是一个数字，当数值为 1 时，滚动的幅度与 OSD 的宽度相同。

``pan-y <amount>``
    调节 ``--video-align-x`` 相对于 OSD 高度，而不是像选项那样相对于视频高度。这对于连续平移大型图像非常有用。

    ``amount`` 是一个数字，当数值为 1 时，滚动的幅度与 OSD 的高度相同。

``drag-to-pan``
    在按住鼠标键的同时平移视频，将视频的点击部分保持在光标下方。

``align-to-cursor``
    在按住鼠标键的同时平移整个视频，如果 ``toggle_align_too_cursor`` 为 ``yes`` ，则在点击一次后平移。

``cursor-centric-zoom <amount>``
    通过 ``amount`` 增加 ``-video-zoom`` ，同时保持光标悬停的视频部分在其下方，或已知触摸点的平均位置。

设置
----

该脚本可以通过 mpv 用户目录下的设置文件 ``script-opts/positioning.conf`` 和命令行选项 ``--script-opts` 进行自定义。设置语法在 `mp.options functions`_ 中描述。

设置选项
~~~~~~~~

``toggle_align_to_cursor``
    默认： no

    是否 ``align-to-cursor`` 需要按住鼠标键才能平移。如果 ``no`` ，则拖动平移。如果 ``yes`` ，第一次点击会使平移跟随光标，第二次点击则会禁用。

``suppress_osd``
    默认： no

    使用 ``cursor-centric-zoom`` 时是否不输出 ``--video-zoom`` 的新值。
