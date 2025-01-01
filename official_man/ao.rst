音频输出驱动
============

音频输出驱动是连接不同音频输出设施的接口。其语法是

``--ao=<driver1,driver2,...[,]>``
    指定一个要使用的音频输出驱动的优先级列表。

如果这个列表末尾有 ``,`` ，mpv将回退到不在列表中的驱动程序。

.. note::

    参见 ``--ao=help`` 获取已编译的音频输出驱动的列表，按自动探测顺序排列。

    请注意，默认音频输出驱动程序可能会发生变化，不得依赖。如果需要使用某个AO，则必须明确指定。

可用的音频输出驱动有：

``alsa``
    ALSA音频输出驱动

    该AO支持以下全局选项：

    ``--alsa-resample=yes``
        启用ALSA重采样插件。（默认禁用，因为一些驱动程序在某些情况下报告了不正确的音频延迟）。

    ``--alsa-mixer-device=<device>``
        设置与 ``ao-volume`` 一起使用的混音器设备（默认： ``default`` ）。

    ``--alsa-mixer-name=<name>``
        设置混音器元素的名称（默认： ``Master`` ）。例如，这是 ``PCM`` 或 ``Master``

    ``--alsa-mixer-index=<number>``
        设置混音器通道的索引（默认： 0）。考虑到 "``amixer scontrols``" 的输出，那么索引就是元素名称后面的数字。

    ``--alsa-non-interleaved``
        允许输出非交错格式（如果音频解码器使用这种格式）。目前默认禁用，因为一些流行的ALSA插件在使用非交错格式时完全失效。

    ``--alsa-ignore-chmap``
        不读取或设置ALSA设备的声道图 —— 只请求所需的声道数，然后将音频原封不动的传递给它。此选项很可能不应被使用。它在调试中可能很有用，或者对于有特殊设计的ALSA配置的静态设置（在这种情况下，你应该始终用 ``--audio-channels`` 强制使用相同的布局，否则它只对使用ALSA设备暗含布局的文件有效）。

    ``--alsa-buffer-time=<microseconds>``
        设置请求的缓冲时间，以微秒为单位。数值 0 可以跳过ALSA API的任何请求。该选项和 ``--alsa-periods`` 选项使用ALSA的 ``near`` 函数来设置请求的参数。如果这样做的结果是一个空的配置集，那么就跳过设置这些参数。

    这两个选项都控制缓冲区的大小。过小的缓冲区会导致较高的CPU使用率和音频丢失，而过大的缓冲区则会导致音量变化和其它滤镜的延迟。

    ``--alsa-periods=<number>``
        从ALSA API请求的周期数。详见 ``--alsa-buffer-time`` 以了解更多。

    .. warning::

        要获得多声道/环绕声音频，使用 ``--audio-channels=auto`` 。 这个选项的默认值是 ``auto-safe``，它将明确地拒绝多声道输出，因为无法检测某个声道布局是否被实际支持。

        你也可以尝试 `使用上混插件 <https://github.com/mpv-player/mpv/wiki/ALSA-Surround-Sound-and-Upmixing>`_ 。这使 ``default`` 设备启用多声道音频，并在共享访问的情况下自动上混，因此同时播放立体声和多声道音频将按预期工作。

``oss``
    OSS音频输出驱动

``jack``
    JACK（Jack Audio Connection Kit）音频输出驱动

    支持以下全局选项：

    ``--jack-port=<name>``
        连接到指定名称的端口（默认： physical ports）
    ``--jack-name=<client>``
        传递给JACK的客户端名称（默认： ``mpv`` ）。如果你想让某些连接自动建立，这很有用。
    ``--jack-autostart=<yes|no>``
        必要时自动启动jack（默认： no）。注意这往往是不可靠的，并且会使stdout中充斥着服务器信息。
    ``--jack-connect=<yes|no>``
        自动建立与输出端口的连接（默认： yes）。当启用时，输出声道的最大数量将被限制到可用输出端口的数量。
    ``--jack-std-channel-layout=<waveext|any>``
        选择标准的声道布局（默认： waveext）。JACK本身没有声道布局的概念（例如指定一个声道应该映射到对应的扬声器） —— 它只是接收应用程序输出的任何东西，并将其重新连接到用户定义的任何地方。这意味着用户和应用程序负责处理声道的布局。 ``waveext`` 使用 WAVE_FORMAT_EXTENSIBLE 顺序，尽管它是由微软定义的，但它是许多系统的标准。值 ``any`` 使JACK接受来自音频滤镜链的任何东西，无视声道布局，也无需重新排序。这种模式可能不是很有用，除了用于调试或固定的设置。

``coreaudio`` （macOS独占）
    使用AudioUnits和CoreAudio声音服务的原生macOS音频输出驱动。

    当播放有损格式时，自动重定向到 ``coreaudio_exclusive``

    支持以下全局选项：

    ``--coreaudio-change-physical-format=<yes|no>``
        更改物理格式为与请求的音频格式相似（默认： no）。这样有利于多声道音频输出将实际起效。缺点是它会改变系统全局的音频设置。这相当于在 ``Audio MIDI Setup`` 工具中的 ``Audio Devices`` 对话框中改变 ``Format`` 设置。注意这不会影响所选的扬声器设置。

    ``--coreaudio-spdif-hack=<yes|no>``
        尝试将AC3/DTS数据作为PCM透传。这对不支持AC3的驱动很有用。它将 AC3 数据转换为浮点，并假定驱动程序将做逆向转换，这意味着传统的A/V接收机将把它作为压缩的IEC框架的AC3流来接收，而忽略它被标记为PCM 。这禁用了正常的AC3直通功能（即使设备报告支持它）。使用时要特别小心。

``coreaudio_exclusive`` （macOS独占）
    原生macOS音频输出驱动，使用直接设备访问和独占模式（绕过声音服务）

``avfoundation`` （macOS独占）
    使用 AVFoundation 中 ``AVSampleBufferAudioRenderer`` 的原生 macOS 音频输出驱动程序，支持 `空间音频 <https://support.apple.com/102469>`_.

    .. warning::

        如果不是以bundle的形式启动 mpv，启用空间音频可能会挂起播放，不过关闭空间音频后播放总是正常的。

``audiounit`` （ios独占）
    使用 ``AudioUnits`` 和 AudioToolbox 的原生 iOS 音频输出驱动程序。

``openal``
    OpenAL音频输出驱动

    ``--openal-num-buffers=<2-128>``
        指定音频缓冲区的使用数量。值越低CPU的使用率越低。默认： 4

    ``--openal-num-samples=<256-32768>``
        指定用于每个缓冲区的完整采样的数量。更高的值利于降低CPU占用率。默认： 8192

    ``--openal-direct-channels=<yes|no>``
        启用OpenAL Soft的直接声道扩展，以避免ambisonics或HRTF的音染。默认： yes

``pulse``
    PulseAudio音频输出驱动

    支持以下全局选项：

    ``--pulse-host=<host>``
        指定要使用的主机。空的 <host> 字符串使用本地连接， "localhost" 则使用网络传输（很可能不是你期望的）

    ``--pulse-buffer=<1-2000|native>``
        以毫秒为单位设置音频缓冲区的大小。较高的值可以缓冲更多的数据，并且有较低的缓冲区不足的概率。较小的值使音频流反应更快，例如对播放速度变化的响应。 "native" 让声音服务自行设定缓冲

    ``--pulse-latency-hacks=<yes|no>``
        启用hack来解决PulseAudio的时间错误（默认： yes）。如果启用，mpv将自己进行详细的延迟计算。如果禁用，它将使用PulseAudio自动更新的时间信息。禁用这个功能可能对网络音频或一些插件有帮助，而启用它可能对一些未知的情况有帮助（由于 PulseAudio 16.0 的已知错误，目前已启用）

    ``--pulse-allow-suspended=<yes|no>``
        即使sink挂起也允许mpv使用PulseAudio（默认： no）。如果PulseAudio以桥接到jack的方式运行，而mpv的sink-input被设置为jack使用的输入，则会很有用。

``pipewire``
    PipeWire音频输出驱动

    该音频输出支持以下全局选项：

    ``--pipewire-buffer=<1-2000|native>``
        设置音频缓冲区，以毫秒为单位。越高的值缓存更多的数据，且具有较低的缓冲区不足概率。值越小，音频流的反应越快，例如对播放速度变化的反应。 "native" 让声音服务自行设定缓冲

    ``--pipewire-remote=<remote>``
        指定通过本地UNIX套接字连接的PipeWire远程守护进程名称。一个空的 <remote> 字符串使用默认的名为``pipewire-0`` 的远程。

    ``--pipewire-volume-mode=<channel|global>``
        指定 ``ao-volume`` 属性是否应该应用于声道音量或全局音量。默认为全局音量。

``sdl``
    SDL 2.0+音频输出驱动。应该在任何受SDL 2.0支持的平台上工作，但可能需要为你的系统正确的设置 ``SDL_AUDIODRIVER`` 环境变量。

    .. note:: 该驱动是为了与极其陌生的环境兼容，例如其他驱动程序都无法使用的系统。

    支持以下全局选项：

    ``--sdl-buflen=<length>``
        以秒为单位设置音频缓冲区的长度。只作为声音系统的提示使用。用 ``-v`` 播放文件将显示请求的和获得的确切缓冲区大小。如果数值为0，则选择声音系统的默认值。

``null``
    无音频输出，但保持视频播放速度。你可以使用 ``--ao=null --ao-null-untimed`` 做基准测试。

    支持以下全局选项：

    ``--ao-null-untimed``
        不模拟一个完美音频设备的计时。这意味着音频解码将尽快的进行，而不是按照系统时钟计时。

    ``--ao-null-buffer``
        以秒为单位模拟的缓冲区长度

    ``--ao-null-outburst``
        以采样为单位模拟的块状大小

    ``--ao-null-speed``
        以倍率为单位模拟的音频播放速度。通常，真实的音频设备不会和系统时钟的速度完全一样。它会有一点偏差，这个选项有助于模拟这种情况。

    ``--ao-null-latency``
        模拟的设备延时。这是对EOF的补充。

    ``--ao-null-broken-eof``
        模拟损坏的音频驱动，它总是将固定的设备延迟添加到报告的音频播放位置。

    ``--ao-null-broken-delay``
        模拟损坏的不能正确报告延迟的音频驱动

    ``--ao-null-channel-layouts``
        如果不是空值，这是一个声音输出驱动允许的以 ``,`` 分隔的声道布局列表。这可以用来测试声道布局的选择。

    ``--ao-null-format``
        强制声音输出驱动接受的音频输出格式。如果没有设置则接受任何格式。

``pcm``
    原始PCM/WAVE文件编码的音频输出

    支持以下全局选项：

    ``--ao-pcm-waveheader=<yes|no>``
        包括或不包括WAVE header（默认： yes）。如果不包括，将生成raw PCM
    ``--ao-pcm-file=<filename>``
        把声音写入到 ``<filename>`` 而不是默认的 ``audiodump.wav`` 。如果指定了 ``no-waveheader`` ，则默认为 ``audiodump.pcm``
    ``--ao-pcm-append=<yes|no>``
        追加到文件中，而不是覆盖写入它。一定要和 ``no-waveheader`` 选项一起使用 —— 和 ``waveheader`` 一起使用会损坏，因为每次打开文件时都会写入一个WAVE header

``sndio``
    音频输出到OpenBSD sndio声音系统

    （注意：仅支持单声道，立体声，4.0/5.1和7.1声道布局）

``wasapi``
    音频输出到Windows音频会话API

    该AO支持以下全局选项：

    ``--wasapi-exclusive-buffer=<default|min|1-2000000>``
        设置独占模式下的缓冲区持续时间（即使用 ``--audio-exclusive=yes`` 时）。 ``default`` 和 ``min`` 分别使用 WASAPI 报告的默认和最小设备周期。你也可以直接以微秒为单位指定缓冲持续时间，在这种情况下，短于最小设备周期的持续时间将四舍五入为最小周期。

        默认的缓冲持续时间在大多数情况下都能提供稳定的播放，但据报告，在某些设备上，默认设置下的流重置会出现故障。在这种情况下，指定更短的持续时间可能会有帮助。
