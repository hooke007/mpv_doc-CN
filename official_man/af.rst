音频滤镜
========

音频滤镜允许你修改音频流和它的属性。其语法是：

``--af=...``
    设置一连串的音频滤镜。完整的语法参见 ``--vf`` （ `视频滤镜`_ ）

.. note::

    要获得可用的音频滤镜的完整列表，参见 ``--af=help``

    另外，请记住，大多数实际的滤镜是通过 ``lavfi`` wrapper获得的，它使你可以使用libavfilter的大多数滤镜。这包括所有从MPlayer移植到libavfilter的滤镜。

    ``--vf`` 的描述阐述了如何使用libavfilter以及如何解决已过时的mpv滤镜。

参见 ``--vf`` 的选项组，了解 ``--af-add`` , ``--af-pre`` , ``--af-clr`` 以及其它可能的工作方式。

可用的滤镜有：

``lavcac3enc[=options]``
    使用libavcodec在运行时将多声道音频编码为AC-3。支持16-bit native-endian输入格式，最多6个声道。当输出原始AC-3流时，输出是big-endian，当输出到S/PDIF时是native-endian。如果输入的采样率不是48kHz、44.1kHz或32kHz，它将被重采样为48kHz。

    ``tospdif=<yes|no>``
        如果 ``no`` ，则输出raw AC-3流，如果 ``yes`` （默认），则输出到S/PDIF进行透传。

    ``bitrate=<rate>``
        用于AC-3流的比特率。设置为384以获得384kbps。

        默认是640。一些接收机可能无法处理。

        有效值： 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, 448, 512, 576, 640.

        特殊值 ``auto`` 根据输入的声道数选择一个默认的比特率。

        :1ch: 96
        :2ch: 192
        :3ch: 224
        :4ch: 384
        :5ch: 448
        :6ch: 448

    ``minch=<n>``
        如果输入声道数少于 ``<minch>`` ，滤镜将自行分离（默认： 3）

    ``encoder=<name>``
        选择要使用的libavcodec编码器。目前，这应该是一个AC-3编码器，使用其它编码器会失败的很惨

``format=format:srate:channels:out-srate:out-channels``
    它本身不做任何格式转换。相反，如果需要的话，它可以使滤镜系统在这个滤镜之前或之后插入必要的转换滤镜。它主要用于控制进入其它滤镜的音频格式。要指定音频输出的格式，参见 ``--audio-format`` ``--audio-samplerate`` ``--audio-channels`` 。这个滤镜能够强制指定一个特定的格式，而 ``--audio-*`` 可以由音频输出驱动根据输出的兼容性进行覆盖。

    所有的参数都是可选的。前三个参数限制了滤镜接受的输入内容。因此它们会导致转换滤镜在这个滤镜之前被插入。 ``out-`` 参数告知在这个滤镜之后的滤镜或音频输出如何解析数据，而不进行实际的转换。设置这些参数可能会损坏什么，除非你真的知道你因为某些原因需要这样做，比如测试或处理损坏的媒体文件。

    ``<format>``
        强制转换为这种格式。使用 ``--af=format=format=help`` 来获得有效格式的列表

    ``<srate>``
        强制转换到一个特定的采样率。采样率是一个整数，例如48000

    ``<channels>``
        强制混合到一个特定的声道布局。参见 ``--audio-channels`` 选项的可能值

    ``<out-srate>``

    ``<out-channels>``

    *注意* ：这个滤镜曾经被命名为 ``force`` 。旧的 ``format`` 滤镜曾经自行转换，不像这个滤镜让滤镜系统处理转换。

``scaletempo[=option1:option2:...]``
    在不改变音调的情况下缩放音频节奏，可选与播放速度同步。

    它的工作原理是以正常速度播放 'stride' 毫秒的音频，然后消耗 'stride*scale' 毫秒的输入音频。它通过将 'overlap'% 的步长与前一个步长之后的音频混合在一起。它可选对下一个 'search' 毫秒的音频进行简短的数据分析，以确定最佳重叠位置。

    ``scale=<amount>``
        名义上的缩放节奏的数量。除了速度之外，还对这个量进行缩放（默认： 1.0）
    ``stride=<amount>``
        输出每个步幅的长度，单位是毫秒。太高的值会在高音阶量时产生明显的跳动，在低音阶量时产生回声。非常低的值会反转音调。增加会改善性能（默认：60）
    ``overlap=<factor>``
        重叠步长的系数。减少会改善性能（默认： 20）
    ``search=<amount>``
        搜索最佳重叠位置的长度，以毫秒为单位。减少会明显改善性能。在慢速系统上，你可能想把它设置得很低（默认： 14）
    ``speed=<tempo|pitch|both|none>``
        设置对速度变化的响应。

        tempo
             缩放速度与播放速度同步（默认）
        pitch
             反转滤镜的效果。缩放音调而不改变速度。在你的 ``input.conf`` 中加入这个，以按音乐的半音阶来调节::

                [ multiply speed 0.9438743126816935
                ] multiply speed 1.059463094352953

             .. warning::

                失去与视频的同步
        both
            同时缩放速度和改变音调
        none
            忽略速度的变化

    .. admonition:: 示例

        ``mpv --af=scaletempo --speed=1.2 media.ogg``
            将以1.2倍于正常的速度播放媒体，音频为正常音调。改变播放速度将改变音频节奏来匹配。

        ``mpv --af=scaletempo=scale=1.2:speed=none --speed=1.2 media.ogg``
            将以1.2倍于正常的速度播放媒体，音频为正常音调，但改变播放速度对音频节奏没有影响。

        ``mpv --af=scaletempo=stride=30:overlap=.50:search=10 media.ogg``
            会对质量和性能参数进行调整。

        ``mpv --af=scaletempo=scale=1.2:speed=pitch audio.ogg``
            将以1.2倍于正常的速度播放媒体，音频为正常音调。改变播放速度将改变音调，使音频节奏保持在1.2倍。

``scaletempo2[=option1:option2:...]``
    缩放音频节奏而不改变音调。这个算法是从chromium移植过来的，使用了波形相似度叠加（WSOLA）方法。与 scaletempo 和 rubberband R2 引擎或 ``engine=faster`` 相比，它似乎能获得更高的音频质量。如果使用了 ``audio-pitch-correction`` 选项（默认开启），则在改变播放速度时会自动插入该滤镜。

    默认情况下， ``search-interval`` 和 ``window-size`` 参数的值与chromium相同。

    ``min-speed=<speed>``
        如果播放速度低于 ``<speed>`` ，则将音频静音（默认： 0.25）

    ``max-speed=<speed>``
        如果播放速度高于 ``<speed>`` 并且 ``<speed> != 0`` ，则将音频静音（默认： 8.0）

    ``search-interval=<amount>``
        搜索最佳重叠位置的长度，以毫秒为单位（默认： 40）

    ``window-size=<amount>``
        overlap-and-add window的长度，以毫秒为单位（默认： 12）

``rubberband``
    用librubberband进行高质量的音调修正。它可以代替 ``scaletempo`` 和 ``scaletempo2`` ，当以不同于正常的速度播放时，它将用于调整音频音调。它也可以用来调整音频音调而不改变播放速度。

    ``<pitch-scale=<amount>``
        设置音调比例系数。频率要乘以这个值。

    ``engine=<faster|finer>``
        选择要使用的核心 Rubberband 引擎。有两种可供选择：

        :Faster: 这是 Rubberband R2 引擎。它的 CPU 占用率明显低于 Finer(R3) 引擎。
        :Finer: 这是 Rubberband R3 引擎。该引擎仅适用于 librubberband 3 或更高版本。其输出质量明显更高，但 CPU 占用率也更高（如果可用的话它是默认值）

    这个滤镜有许多额外的子选项。你可以用 ``mpv --af=rubberband=help`` 列出它们。这也会显示每个选项的默认值。这里没有记录这些选项，因为它们只是被传递给librubberband。参阅librubberband的文档以了解每个选项的作用： https://breakfastquay.com/rubberband/code-doc/classRubberBand_1_1RubberBandStretcher.html 请注意，某些选项只适用于 R2(faster) 和 R3(finer) 引擎中的一个。（mpv rubberband滤镜的子选项名称和值与librubberband的映射遵循一个简单的模式： ``"Option" + Name + Value`` ）

    这个滤镜支持下列 ``af-command`` 命令：

    ``set-pitch``
        动态设置 ``<pitch-scale>`` 参数。这可以用来在运行时改变播放的音调。注意，速度是用标准的 ``speed`` 属性控制的，而不是 ``af-command`` 。

    ``multiply-pitch <factor>``
        动态的乘以当前的 ``<pitch-scale>`` 的值。

``lavfi=graph``
    使用FFmpeg的libavfilter过滤音频。

    ``<graph>``
        Libavfilter graph。详见 ``lavfi`` 视频滤镜 —— graph的语法是一样的

        .. warning::

            不要忘记引用libavfilter graphs，如lavfi视频滤镜部分所述

    ``o=<string>``
        AVOptions

    ``fix-pts=<yes|no>``
        根据采样数确定PTS（默认： no）。如果这个选项被启用，播放器将不依赖于libavfilter准确的传递PTS。相反，它将采样数作为PTS传给libavfilter，并根据它和输入的PTS计算mpv使用的PTS。这有助于处理那些输出重新计算的PTS而不是原始PTS的滤镜（包括要求PTS从0开始的滤镜）。mpv通常希望滤镜不要接触PTS（或者只在改变帧边界的范围内），所以这不是默认的，但在使用损坏的滤镜时需要这样处理。在实际情况中，这些损坏的滤镜会随着时间的推移导致缓慢的A/V不同步（对于某些文件），或者如果你从文件中间跳转或开始播放，会完全中断播放。

``drop``
    这个滤镜丢弃或重复音频帧来适应播放速度。它总是在完整的音频帧上操作，因为它是为了处理SPDIF（压缩音频透传）。如果使用 ``--video-sync=display-adrop`` 选项，它会自动使用。不要使用这个滤镜（或给定的选项）；它们的质量极低。
