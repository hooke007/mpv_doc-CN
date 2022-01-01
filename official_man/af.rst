AUDIO FILTERS
=============

音频过滤器允许你修改音频流和它的属性。语法是：

``--af=...``
    设置一连串的音频过滤器。完整的语法见 ``--vf`` ( `VIDEO FILTERS`_ )。

.. note::

    要获得可用的音频过滤器的完整列表，见 ``--af=help``

    另外，请记住，大多数实际的过滤器是通过 ``lavfi`` 包装器获得的，它使你可以访问libavfilter的大多数过滤器。这包括所有从MPlayer移植到libavfilter的过滤器。

    ``--vf`` 描述了如何使用libavfilter以及如何解决已deprecated的mpv过滤器。

参见 ``--vf`` 选项组，了解 ``--af-defaults``, ``--af-add``, ``--af-pre``, ``--af-del``, ``--af-clr`` 以及可能的其他工作。

可用的过滤器有：

``lavcac3enc[=options]``
    使用libavcodec在运行时将多声道音频编码为AC-3。支持16-bit native-endian输入格式，最多6个通道。当输出原始AC-3流时，输出是big-endian，当输出到S/PDIF时是native-endian。如果输入的采样率不是48kHz、44.1kHz或32kHz，它将被重新采样为48kHz。

    ``tospdif=<yes|no>``
        如果 ``no`` ，则输出原始AC-3流，如果 ``yes`` （默认），则输出到S/PDIF进行透传。

    ``bitrate=<rate>``
        用于AC-3流的比特率。设置为384以获得384 kbps。

        默认是640。一些接收机可能无法处理这个。

        有效值： 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, 448, 512, 576, 640.

        特殊值 ``auto`` 根据输入的通道号选择一个默认的比特率。

        :1ch: 96
        :2ch: 192
        :3ch: 224
        :4ch: 384
        :5ch: 448
        :6ch: 448

    ``minch=<n>``
        如果输入通道数少于 ``<minch>`` ，滤波器将自行分离（默认： 3）。

    ``encoder=<name>``
        选择使用的libavcodec编码器。目前，这应该是一个AC-3编码器，使用其他编解码器会失败得很厉害。

``format=format:srate:channels:out-srate:out-channels``
    本身不做任何格式转换。相反，如果需要的话，它可以使过滤器系统在这个过滤器之前或之后插入必要的转换过滤器。它主要用于控制进入其他过滤器的音频格式。要指定音频输出的格式，请看``--audio-format`` ``--audio-samplerate`` ``--audio-channels`` 这个过滤器能够强制指定一个特定的格式，而 ``--audio-*`` 可以由ao根据输出的兼容性进行覆盖。

    所有的参数都是可选的。前三个参数限制了过滤器接受的输入内容。因此它们会导致转换过滤器在这个过滤器之前被插入。 ``out-`` 参数告诉在这个滤波器之后的滤波器或音频输出如何解释数据，而不进行实际的转换。设置这些参数可能会破坏事情，除非你真的知道你因为某些原因需要这样做，比如测试或处理破损的媒体。

    ``<format>``
        强制转换为这种格式。使用 ``--af=format=format=help`` 来获得有效格式的列表。

    ``<srate>``
        强制转换到一个特定的采样率。速率是一个整数，例如48000。

    ``<channels>``
        强制混合到一个特定的通道布局。参见 ``--audio-channels`` 选项的可能值。

    ``<out-srate>``

    ``<out-channels>``

    *注意*：这个过滤器曾经被命名为 ``force`` 。旧的 ``format`` 过滤器曾经自己做转换，不像这个过滤器让过滤器系统处理转换。

``scaletempo[=option1:option2:...]``
    在不改变音高的情况下调整音频节奏，可以选择与播放速度同步（默认）。

    它的工作原理是以正常速度播放 'stride' ms 的音频，然后消耗 'stride*scale' ms 的输入音频。它通过将 'overlap'% 的步长与前一个步长之后的音频混合在一起。它可以选择对下一个 "搜索" 毫秒的音频进行简短的统计分析，以确定最佳重叠位置。

    ``scale=<amount>``
        缩放节奏的名义量。除了速度之外，还对这个量进行缩放。(默认： 1.0)
    ``stride=<amount>``
        输出每个步幅的长度，单位是毫秒。太高的值会在高音阶量时引起明显的跳动，在低音阶量时引起回声。非常低的值会改变音高。增加会提高性能。(默认值：60)
    ``overlap=<percent>``
        重叠步长的百分比。减少会提高性能。(默认： 20)
    ``search=<amount>``
        搜索最佳重叠位置的长度（毫秒）。减少会大大改善性能。在慢速系统上，你可能想把它设置得很低。(默认： 14)
    ``speed=<tempo|pitch|both|none>``
        设置对速度变化的响应。

        tempo
             缩放速度与速度同步（默认）。
        pitch
             反转滤波器的效果。缩放音高而不改变速度。在你的 ``input.conf`` 中加入这个，以按音乐半音阶::

                [ multiply speed 0.9438743126816935
                ] multiply speed 1.059463094352953

             .. warning::

                与视频失去同步。
        both
            同时调整速度和音高。
        none
            忽略速度变化。

    .. admonition:: 示例

        ``mpv --af=scaletempo --speed=1.2 media.ogg``
            将以1.2倍的正常速度播放媒体，音频为正常音调。改变播放速度将改变音频节奏以匹配。

        ``mpv --af=scaletempo=scale=1.2:speed=none --speed=1.2 media.ogg``
            将以1.2倍的正常速度播放媒体，音频为正常音调，但改变播放速度对音频节奏没有影响。

        ``mpv --af=scaletempo=stride=30:overlap=.50:search=10 media.ogg``
            会对质量和性能参数进行调整。

        ``mpv --af=scaletempo=scale=1.2:speed=pitch audio.ogg``
            将以1.2倍的正常速度播放媒体，音频为正常音高。改变播放速度将改变音高，使音频节奏保持在1.2倍。
    
``scaletempo2[=option1:option2:...]``
    缩放音频节奏而不改变音高。这个算法是从chromium移植过来的，使用了波形相似度叠加（WSOLA）方法。它似乎比scaletempo和rubberband实现了更高的音频质量。

    默认情况下， ``search-interval`` 和 ``window-size`` 参数的值与chromium相同。

    ``min-speed=<speed>``
        如果播放速度低于 ``<speed>`` ，则将音频静音。(默认： 0.25)

    ``max-speed=<speed>``
        如果播放速度高于 ``<speed>`` 并且 ``<speed> != 0`` ，则将音频静音。(默认： 4.0)

    ``search-interval=<amount>``
        搜索最佳重叠位置的长度（毫秒）。(默认： 30)
    
    ``window-size=<amount>``
        重叠和添加窗口的长度，以毫秒为单位。(默认： 20)

``rubberband``
    用librubberband进行高质量的音高校正。它可以代替 ``scaletempo`` ，当以不同于正常速度播放时，它将用于调整音频音高。它也可以用来调整音频音高而不改变播放速度。

    ``<pitch-scale>``
        设置音高比例系数。频率要乘以这个值。

    这个滤波器有许多额外的子选项。你可以用 ``mpv --af=rubberband=help`` 列出它们。这也会显示每个选项的默认值。这里没有记录这些选项，因为它们只是被传递给librubberband。请看librubberband文档以了解每个选项的作用： https://breakfastquay.com/rubberband/code-doc/classRubberBand_1_1RubberBandStretcher.html （mpv rubberband过滤器的子选项名称和值与librubberband的映射遵循一个简单的模式： ``"Option" + Name + Value`` ）

    这个过滤器支持下列 ``af-command`` 命令：

    ``set-pitch``
        动态设置``<pitch-scale>``参数。这可以用来在运行时改变播放的音高。注意，速度是用标准的``speed``属性控制的，而不是``af-command``。

    ``multiply-pitch <factor>``
        动态地乘以当前的``<pitch-scale>'的值。 例如：0.5可以下降一个八度，1.5可以上升一个五度。如果你想上升或下降半音，用1.059463094352953和0.9438743126816935。

``lavfi=graph``
    使用FFmpeg的libavfilter过滤音频。

    ``<graph>``
        Libavfilter graph。详见 ``lavfi`` 视频过滤器 - 图形语法是一样的。

        .. warning::

            不要忘记引用libavfilter graphs，如lavfi视频过滤器部分所述。

    ``o=<string>``
        AVOptions.

    ``fix-pts=<yes|no>``
        根据样本数确定PTS（默认： no）。如果这个选项被启用，播放器将不依赖于libavfilter准确地传递PTS。相反，它将样本数作为PTS传给libavfilter，并根据它和输入的PTS计算mpv使用的PTS。这有助于处理那些输出重新计算的PTS而不是原始PTS的滤波器（包括要求PTS从0开始的滤波器）。mpv通常希望滤波器不要接触PTS（或者只在改变帧边界的范围内），所以这不是默认的，但在使用破碎的滤波器时需要这样做。在实践中，这些破碎的过滤器会随着时间的推移导致缓慢的A/V解同步（对于某些文件），或者如果你从文件中间寻找或开始播放，会完全中断播放。

``drop``
    这个过滤器减少或重复音频帧以适应播放速度。它总是在完整的音频帧上操作，因为它是为了处理SPDIF（压缩音频穿透）。如果使用 ``--video-sync=display-adrop`` 选项，它会自动使用。不要使用这个过滤器（或给定的选项）；它们的质量极低。
