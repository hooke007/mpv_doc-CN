AUDIO OUTPUT DRIVERS
====================

音频输出驱动是连接不同音频输出设施的接口。其语法是

``--ao=<driver1,driver2,...[,]>``
    指定一个要使用的音频输出驱动的优先级列表。

如果这个列表有一个尾巴','，mpv将回到列表中不包含的驱动程序。

.. note::

    参见 ``--ao=help`` 获取已编译的音频输出驱动的列表。驱动程序 ``--ao=alsa`` 是首选。 ``--ao=pulse`` 在使用PulseAudio的系统上是首选。在BSD系统上， ``--ao=oss`` 是首选。

可用的音频输出驱动有:

``alsa`` (Linux only)
    ALSA音频输出驱动

    参见 `ALSA audio output options`_ 以了解该AO的特定选项。

    .. warning::

        要获得多声道/环绕声，请使用 ``--audio-channels=auto``。 这个选项的默认值是 ``auto-safe``，它使这个音频输出明确地拒绝多声道输出，因为没有办法检测某个声道布局是否真的被支持。

        你也可以尝试 `using the upmix plugin <http://git.io/vfuAy>`_。这种设置使 ``default`` 设备上的多声道音频与共享访问的自动向上混合，因此在同一时间播放立体声和多声道音频将按预期工作。

``oss``
    OSS音频输出驱动

``jack``
    JACK（Jack Audio Connection Kit）音频输出驱动。

    这个音频输出支持以下全局选项。

    ``--jack-port=<name>``
        连接到指定名称的端口（默认： physical ports）。
    ``--jack-name=<client>``
        传递给JACK的客户端名称（默认： ``mpv``）。如果你想让某些连接自动建立，这很有用。
    ``--jack-autostart=<yes|no>``
        必要时自动启动jackd（默认： no）。注意，这往往是不可靠的，并且会使stdout中充斥着服务器信息。
    ``--jack-connect=<yes|no>``
        自动建立与输出端口的连接（默认： yes）。当启用时，输出通道的最大数量将被限制在可用输出端口的数量上。
    ``--jack-std-channel-layout=<waveext|any>``
        选择标准的通道布局（默认： waveext）。JACK本身没有通道布局的概念（即指定一个给定的通道应该映射到哪个扬声器）——它只是接收应用程序输出的任何东西，并将其重新路由到用户定义的任何地方。这意味着用户和应用程序负责处理通道的布局。 ``waveext`` 使用 WAVE_FORMAT_EXTENSIBLE 顺序，尽管它是由微软定义的，但它是许多系统的标准。值 ``any`` 使JACK接受来自音频过滤器链的任何东西，不管通道布局如何，也不需要重新排序。这种模式可能不是很有用，除了用于调试或用于固定设置。

``coreaudio`` (macOS only)
    使用 AudioUnits 和 CoreAudio 声音服务器的原生macOS音频输出驱动。

    当播放压缩格式时，自动重定向到 ``coreaudio_exclusive`` 。

    这个音频输出支持以下全局选项：

    ``--coreaudio-change-physical-format=<yes|no>``
        将物理格式改为与要求的音频格式相似的格式（默认： no）。这样做的好处是，多声道音频输出将实际工作。缺点是它会改变整个系统的音频设置。这相当于在 ``Audio MIDI Setup`` 工具中的 ``Audio Devices`` 对话框中改变 ``Format`` 设置。注意，这不会影响所选的扬声器设置。

    ``--coreaudio-spdif-hack=<yes|no>``
        尝试将 AC3/DTS 数据作为 PCM 传输。这对不支持 AC3 的驱动程序很有用。它将 AC3 数据转换为浮点数据，并假定驱动程序将做反向转换，这意味着典型的A/V接收器将把它作为压缩的 IEC 框架 AC3 流来接收，而忽略它被标记为 PCM 。这使正常的 AC3 直通功能失效（即使设备报告支持它）。使用时要特别小心。


``coreaudio_exclusive`` (macOS only)
    原生macOS音频输出驱动，使用直接设备访问和独占模式（绕过声音服务器）。

``openal``
    OpenAL音频输出驱动。

    ``--openal-num-buffers=<2-128>``
        指定要使用的音频缓冲区的数量。数值越低越好，以降低CPU的使用率。默认： 4。

    ``--openal-num-samples=<256-32768>``
        指定每个缓冲区要使用的完整样本的数量。更高的值对降低CPU占用率有好处。默认： 8192。

    ``--openal-direct-channels=<yes|no>``
        启用OpenAL Soft的直接通道扩展，以避免用 ambisonics 或 HRTF 对声音进行染色。默认： yes。

``pulse``
    PulseAudio音频输出驱动

    这个音频输出支持以下全局选项：

    ``--pulse-host=<host>``
        指定要使用的主机。一个空的 <host> 字符串使用本地连接，"localhost" 使用网络传输（很可能不是你想要的）。

    ``--pulse-buffer=<1-2000|native>``
        以毫秒为单位设置音频缓冲区的大小。一个较高的值可以缓冲更多的数据，并且有较低的缓冲区不足的概率。一个较小的值使音频流反应更快，例如对播放速度的变化。

    ``--pulse-latency-hacks=<yes|no>``
        启用黑客技术来解决 PulseAudio 的时间错误（默认： no）。如果启用，mpv将自己进行详细的延迟计算。如果禁用，它将使用 PulseAudio 自动更新的时间信息。禁用这个功能可能对网络音频或一些插件有帮助，而启用它可能对一些未知的情况有帮助（在旧的 PulseAudio 版本中，它曾经是获得良好行为的必要条件）。

        如果你在使用pulse时有视频卡顿的情况，请尝试启用这个选项。（或者尝试更新 PulseAudio）。

    ``--pulse-allow-suspended=<yes|no>``
        允许mpv使用 PulseAudio ，即使汇流排被暂停（默认： no）。如果 PulseAudio 以桥接方式运行，而mpv的sink-input被设置为jack使用的输入，则会很有用。

``sdl``
    SDL 1.2+音频输出驱动。应该在SDL 1.2支持的任何平台上工作，但可能需要为你的系统适当设置 ``SDL_AUDIODRIVER`` 环境变量。

    .. 注意:: 这个驱动程序是为了与极其陌生的环境兼容，例如其他驱动程序都无法使用的系统。

    这个音频输出支持以下全局选项：

    ``--sdl-buflen=<length>``
        设置音频缓冲区的长度，单位是秒。只作为声音系统的提示使用。用 ``-v`` 播放文件将显示要求的和获得的确切缓冲区大小。如果数值为0，则选择声音系统的默认值。

``null``
    不产生音频输出，但保持视频播放速度。你可以使用 ``--ao=null --ao-null-untimed`` 来做基准测试。

    这个音频输出支持以下全局选项：

    ``--ao-null-untimed``
        不模拟完美音频设备的时间。这意味着音频解码将尽可能快地进行，而不是按照系统时钟计时。

    ``--ao-null-buffer``
        模拟的缓冲区长度，以秒为单位。

    ``--ao-null-outburst``
        模拟的块状大小，以采样为单位。

    ``--ao-null-speed``
        模拟的音频播放速度是一个倍数。通常情况下，真实的音频设备不会和系统时钟的速度完全一样。它只会有一点偏差，这个选项有助于模拟这种情况。

    ``--ao-null-latency``
        模拟设备延时。这是对EOF的补充。

    ``--ao-null-broken-eof``
        模拟损坏的音频驱动，它总是将固定的设备延迟添加到报告的音频播放位置。

    ``--ao-null-broken-delay``
        模拟损坏的音频驱动，不能正确报告延迟。

    ``--ao-null-channel-layouts``
        如果不是空的，这是一个AO允许的通道布局的 ``,`` 分隔列表。这可以用来测试通道布局的选择。

    ``--ao-null-format``
        强制AO接受的音频输出格式。如果没有设置，则接受任何格式。

``pcm``
    原始 PCM/WAVE 文件编码的音频输出

    这个音频输出支持以下全局选项：

    ``--ao-pcm-waveheader=<yes|no>``
        包括或不包括 WAVE header （默认： yes）。如果不包括，将生成 raw PCM。
    ``--ao-pcm-file=<filename>``
        把声音写到 ``<filename>`` 而不是默认的 ``audiodump.wav``。如果指定了 ``no-waveheader``，则默认为 ``audiodump.pcm``。
    ``--ao-pcm-append=<yes|no>``
        追加到文件中，而不是覆盖它。一定要和 ``no-waveheader`` 选项一起使用——使用`waveheader'会被破坏，因为每次打开文件时都会写一个WAVE头。

``wasapi``
    音频输出到Windows音频会话的API。
