视频输出驱动
============

视频输出驱动是连接不同视频输出设备的接口。其语法是：

``--vo=<driver1,driver2,...[,]>``
    指定一个要使用的视频输出驱动的优先级列表。

如果这个列表末尾有 ``,`` ，mpv将回退到不在列表中的驱动程序。

这是一个对象设定列表选项。详见 `列表选项`_

.. note::

    参见 ``--vo=help`` 获取已编译的视频输出驱动的列表。

    ``--vo=gpu`` 是默认的推荐的输出驱动。其他所有的驱动都是为了兼容性或特定场景。如果默认值无效，它将回退到其他驱动（优先顺序和 ``--vo=help`` 列出的相同）。

    请注意，默认视频输出驱动程序可能会发生变化，不得依赖。如果需要使用某个VO（例如 对于 ``libmpv`` rendering API），则必须显式指定该VO。

可用的视频输出驱动有：

``gpu``
    通用的可定制的、GPU加速的视频输出驱动。它支持扩展缩放方式、抖动、色彩管理、自定义着色器、HDR等。

    参见 `GPU渲染选项`_ ，了解该视频输出的特定选项。

    默认情况下，mpv使用平衡质量和性能的设置。此外，还有两个预定义的配置文件可用： ``fast`` 用于最大性能， ``high-quality`` 用于优越的渲染质量。您可以使用 ``--profile=<name>`` 选项应用特定的配置文件，并使用 ``--show-profile=<name>`` 来查看其内容。

    这个视频输出虚拟了几个可能的图形API和窗口环境，可以用 ``--gpu-api`` 和 ``--gpu-context`` 选项来影响它们。

    OpenGL-interop的硬件解码在一定程度上受支持。请注意在这种模式下，一些边缘情况可能无法被良好处理，并且色彩空间转换和色度还原通常由硬解码API负责。

    ``gpu`` 默认使用FBOs。有时你可以通过改变选项 ``--fbo-format`` 为 ``rgb16f``, ``rgb32f`` 或 ``rgb`` 来达到更好的质量或性能。已知的问题包括Mesa/Intel不接受 ``rgb16`` ，Mesa有时不支持浮点纹理，以及一些macOS的设置在使用 ``rgb16`` 时非常慢，但使用``rgb32f``时非常快。如果你存在运行问题，也可以尝试启用 ``--gpu-dumb-mode=yes`` 选项。

``gpu-next``
    基于 ``libplacebo`` 的实验性视频渲染器。它几乎支持与 ``--vo=gpu`` 相同的功能集。列表参见 `GPU渲染选项`_

    通常应该更快，质量更高，但有些功能可能仍然缺失或运行异常。期待（并报告！）错误。有关已知差异和错误的列表，参见此处：

    https://github.com/mpv-player/mpv/wiki/GPU-Next-vs-GPU

``xv`` （X11独占）
    使用XVideo扩展来启用硬件加速显示。这是在X上兼容性最好的视频输出驱动，但可能质量低下，而且在OSD和字幕显示方面存在问题。

    .. note:: 这个驱动程序是为了与旧系统兼容。

    支持以下全局选项：

    ``--xv-adaptor=<number>``
        选择一个指定的XVideo适配器（检查xvinfo结果）
    ``--xv-port=<number>``
        选择一个指定的XVideo端口
    ``--xv-ck=<cur|use|set>``
        选择获取color key的源（默认： cur）

        cur
          默认取当前在Xv中设置的color key
        use
          使用但不设置mpv的color key（使用 ``--colorkey`` 选项来变更）
        set
          与use相同，但也设置提供的color key

    ``--xv-ck-method=<none|man|bg|auto>``
        设置color key的绘制方法（默认： man）

        none
          禁用color-keying
        man
          手动绘制color key（在部分情况下减少闪烁）
        bg
          将color key设置为窗口背景
        auto
          由Xv绘制color key

    ``--xv-colorkey=<number>``
        变更color key为你选择的RGB值。 ``0x000000`` 是纯黑， ``0xffffff`` 是纯白

    ``--xv-buffers=<number>``
        用于内部环形缓冲区的图片缓存的数量（默认： 2）。增大该数会使用更多的内存，但如果视频帧率接近或高于显示器刷新率，可能有助于解决X服务器响应不够快的问题。

``x11`` （X11独占）
    无硬件加速的共享内存视频输出驱动，只要有X11就能工作。

    从mpv 0.30.0开始，你可能需要使用 ``--profile=sw-fast`` 去实现正常的性能。

    .. note:: 这只是一个后备方案，通常不应该使用。

``vdpau`` （X11独占）
    https://mpv.io/manual/master/#video-output-drivers-vdpau

``direct3d`` （Windows独占）
    使用Direct3D接口的视频输出驱动

    .. note:: 这个驱动是为了兼容那些没有提供合适的OpenGL驱动的系统，以及ANGLE表现不好的平台。

    支持以下全局选项：

    ``--vo-direct3d-disable-texture-align``
        通常情况下，纹理尺寸总是对齐到16。启用这个选项后，视频纹理将总是与视频本身的尺寸完全相同。


    调试选项。这些可能是不正确的，可能会在将来被移除，可能会崩溃，可能会导致低速运行，等等。如果你为了性能或正常运行真的需要这些，请联系开发者。

    ``--vo-direct3d-force-power-of-2``
        总是强制纹理为2的幂，即使设备报告支持非2的幂的纹理尺寸

    ``--vo-direct3d-texture-memory=<mode>``
        只影响启用着色器/纹理的操作，以及(E)OSD。可用的值：

        ``default`` （默认）
            使用 ``D3DPOOL_DEFAULT`` 和一个 ``D3DPOOL_SYSTEMMEM`` 纹理进行锁定。如果驱动支持 ``D3DDEVCAPS_TEXTURESYSTEMMEMORY`` ，则直接使用 ``D3DPOOL_SYSTEMMEM``

        ``default-pool``
            使用 ``D3DPOOL_DEFAULT`` （类似  ``default`` ，但绝不使用shadow-texture）

        ``default-pool-shadow``
            使用 ``D3DPOOL_DEFAULT`` 和一个 ``D3DPOOL_SYSTEMMEM`` 纹理进行锁定（类似  ``default`` ，但总是强制使用shadow-texture）

        ``managed``
            使用 ``D3DPOOL_MANAGED``

        ``scratch``
            使用 ``D3DPOOL_SCRATCH`` 和一个 ``D3DPOOL_SYSTEMMEM`` 纹理进行锁定

    ``--vo-direct3d-swap-discard``
        使用 ``D3DSWAPEFFECT_DISCARD`` 可能更快。也可能更慢，因为它必须(?)清除每一帧。

    ``--vo-direct3d-exact-backbuffer``
        始终将后缓存的大小调整到窗口大小。

``sdl``
    SDL 2.0+ 渲染视频输出驱动，取决于是否有硬件加速的系统。应该在SDL 2.0支持的所有平台上工作。关于详细调整，请参考你的副本文件 ``SDL_hints.h``

    .. note:: 此驱动是为了与无法提供正常的图形驱动程序的系统兼容。

    支持以下全局选项：

    ``--sdl-sw``
        即使检测到软件渲染器也继续

    ``--sdl-switch-mode``
        指示SDL在全屏时切换显示器的视频模式

``dmabuf-wayland``
    实验性的Wayland输出驱动，旨在与 drm stateless 或 VA API 硬件解码一起使用。该驱动被设计为避免任何GPU到CPU的拷贝，并使用固定功能的硬件（如果可用的话）而不是GPU着色器来执行缩放和色彩空间转换。这就为其它任务释放了GPU资源。强烈建议使用适当的 ``--hwdec`` 选项（如 ``auto-safe`` ）来配合使用此VO。虽然在某些情况下可以不使用 ``--hwdec`` ，因为mpv的内部转换滤镜，但不建议这样做，因为这是一个不必要的额外步骤。正确的输出取决于您的GPU、驱动程序和合成器的支持。这就要求合成器和 mpv 支持 ``color-management-v1`` ，以准确显示不同于合成器默认（大多数情况下为 bt.601）的色彩空间。

    .. warning::

        mpv 在 Wayland 上运行并不需要该驱动程序。 ``vo=gpu`` 和 ``vo=gpu-next`` 会自动切换到相应的 Wayland 上下文。此驱动是实验性的，质量通常低于 ``gpu``/``gpu-next`` 。

``vaapi``
    Intel VA API视频输出驱动，支持硬件解码。请注意除了兼容性之外，绝对没有理由使用这个。这是低质量的，而且在OSD方面有问题。我们强烈建议你使用 ``--vo=gpu`` ``--hwdec=vaapi`` 代替它。

    支持以下全局选项：

    ``--vo-vaapi-scaling=<algorithm>``
        default
            驱动程序的默认值（默认）
        fast
            速度快但质量低
        hq
            未指定的依赖驱动程序的高质量缩放，但速度慢
        nla
            ``non-linear anamorphic scaling``

    ``--vo-vaapi-scaled-osd=<yes|no>``
        如果启用，那么OSD将按视频分辨率渲染，并按显示分辨率进行缩放。默认情况下，这个功能是禁用的，如果驱动程序支持，OSD将以显示分辨率渲染。

``null``
    无视频输出。对于基准测试很有用。

    通常情况下，用 ``--video=no`` 来禁用视频更好。

    支持以下全局选项：

    ``--vo-null-fps=<value>``
        模拟显示FPS。这人为地限制了视频输出每秒接受的帧数。

``caca``
    Color ASCII art video output driver that works on a text console.

    This driver reserves some keys for runtime configuration. These keys are hardcoded and cannot be bound:

    d and D
        Toggle dithering algorithm.

    a and A
        Toggle antialiasing method.

    h and H
        Toggle charset method.

    c and C
        Toggle color method.

    .. note:: This driver is a joke.

``tct``
    彩色Unicode艺术视频输出驱动，在文本控制台中工作。默认情况下，取决于现代终端对真彩色的支持，以完整色范围显示图像，但也支持256色输出（见下文）。在Windows上，它需要一个ansi终端例如mintty。

    从mpv 0.30.0开始，你可能需要使用 ``--profile=sw-fast`` 来获得合格的性能。

    注意：TCT图像输出与mpv的其他终端输出不同步，这可能导致图像破碎。选项 ``--terminal=no`` 或 ``--really-quiet`` 有助于解决这个问题。

    ``--vo-tct-algo=<algo>``
        选择如何将像素写入到终端

        half-blocks
            使用unicode LOWER HALF BLOCK字符来实现更高的垂直分辨率（默认）
        plain
            使用空格。导致垂直分辨率下降两重，但理论上在更多地方起作用

    ``--vo-tct-buffering=<pixel|line|frame>``
        Specifies the size of data batches buffered before being sent to the terminal.

        TCT image output is not synchronized with other terminal output from mpv, which can lead to broken images. Sending data to the terminal in small batches may improve parallelism between terminal processing and mpv processing but incurs a static overhead of generating tens of thousands of small writes. Also, depending on the terminal used, sending frames in one chunk might help with tearing of the output, especially if not used with ``--really-quiet`` and other logs interrupt the data stream.

        pixel
            Send data to terminal for each pixel.
        line
            Send data to terminal for each line. (Default)
        frame
            Send data to terminal for each frame.

    ``--vo-tct-width=<width>`` ``--vo-tct-height=<height>``
        假设终端有指定的字符宽度和/或高度。如果不能检测终端尺寸，这些默认为80x25

    ``--vo-tct-256=<yes|no>`` （默认： no）
        使用256色 —— 用于不支持真彩色的终端

``kitty``
    使用kitty图形协议的终端图形输出。曾用kitty和Konsole测试。

    你可能需要使用 ``--profile=sw-fast`` 来取得良好的性能。

    Kitty的尺寸和对齐选项：

    ``--vo-kitty-cols=<columns>`` ``--vo-kitty-rows=<rows>`` （默认： 0）
        以字符单元指定终端尺寸，否则 (0) 从终端读取，或回退到 80x25

    ``--vo-kitty-width=<width>`` ``--vo-kitty-height=<height>`` （默认： 0）
        指定可用的像素大小，否则 (0) 从终端读取，或回退到 320x240

    ``--vo-kitty-left=<col>`` ``--vo-kitty-top=<row>`` （默认： 0）
        指定图像开始在字符单元中的位置（1是第一列或第一行）。如果是0（默认值），则尝试根据其它值和图像的长宽比及缩放来自动决定

    ``--vo-kitty-config-clear=<yes|no>`` （默认： yes）
        每当输出被重新配置时，是否清理终端（例如，当视频尺寸发生改变）

    ``--vo-kitty-alt-screen=<yes|no>`` （默认： yes）
        是否使用备用的屏幕缓冲区并在退出时将终端返回到之前的状态。当设置为 no 时，退出后最后的kitty图像会保留在屏幕上，且光标会跟随它

    ``--vo-kitty-use-shm=<yes|no>`` （默认： no）
        使用共享内存对象来传输图像数据到终端。这比以转义代码形式发送数据要快得多，但不被许多终端支持。它也只在本地机器上工作，而无法通过例如SSH的连接

        这个选项在Windows上未实现。

    ``--vo-kitty-auto-multiplexer-passthrough=<yes|no>`` （默认： no）
        自动检测终端multiplexer，直通转义序列。这样，图像协议就能通过直接向终端传递转义序列，在可能不支持 kitty 图像协议的multiplexers中运行。

        当前仅支持 tmux 和 GNU screen

``sixel``
    使用sixels的终端图形输出。用 ``mlterm`` 和 ``xterm`` 测试。

    注意：Sixel图像输出与mpv的其他终端输出不同步，这可能导致图像破碎。选项 ``--really-quiet`` 有助于解决这个问题，建议使用。在某些平台上，使用 ``--vo-sixel-buffered`` 选项可能有效。

    你可能需要使用 ``--profile=sw-fast`` 来获得合格的性能。

    注意：在撰写本文时， ``xterm`` 默认不启用sixel —— 以 ``xterm -ti 340`` 启动是启用它的一个方法。另外， ``xterm`` 默认不显示大于1000x1000像素的图像。

    为了正确地渲染和对齐sixel图像，mpv需要知道终端的尺寸，包括单元格和像素。默认情况下，它试图使用终端报告的值，然而，由于终端之间的差异，这是一个容易出错的过程，不能确定地自动进行 —— 一些终端报告的尺寸是以像素为单位的，包括边距 —— 例如 ``xterm`` ，而其他终端报告的是实际可用的像素数 - 如 ``mlterm`` 。此外，它们在最大化或全屏时的表现可能不同，mpv不能用标准方法检测这种状态。

    Sixel的大小和对齐选项：

    ``--vo-sixel-cols=<columns>`` ``--vo-sixel-rows=<rows>`` （默认： 0）
        以字符单元指定终端尺寸，否则(0)从终端读取，或退回到80x25。注意，mpv不使用最后一行的sixel，因为这似乎会导致滚动。

    ``--vo-sixel-width=<width>`` ``--vo-sixel-height=<height>`` （默认： 0）
        指定可用的像素大小，否则(0)从终端读取，或退回到320x240。除了排除最后一行外，高度也被进一步四舍五入为6的倍数（sixel单位高度），以避免溢出低于指定的尺寸。

    ``--vo-sixel-left=<col>`` ``--vo-sixel-top=<row>`` （默认： 0）
        指定图像开始在字符单元中的位置（1是第一列或第一行）。如果是0（默认），则尝试根据其他值和图像的长宽比和缩放来自动确定它。

    ``--vo-sixel-pad-x=<pad_x>`` ``--vo-sixel-pad-y=<pad_y>`` （默认： -1）
        只在mpv从终端读取尺寸（像素）时使用。指定终端报告的尺寸所包含的填充像素数（单边）。如果-1（默认），那么像素数将被四舍五入为单元格数的倍数（每个轴），以考虑报告中的边距 —— 这只有在每个轴的总体填充量小于单元格数时才能正确工作。

    ``--vo-sixel-config-clear=<yes|no>`` （默认： yes）
        每当输出被重新配置时，是否清理终端（例如，当视频尺寸发生改变）

    ``--vo-sixel-alt-screen=<yes|no>`` （默认： yes）
        是否使用备用的屏幕缓冲区并在退出时将终端返回到之前的状态。当设置为 no 时，退出后最后一个sixel图像会保留在屏幕上，且光标会跟随它

        ``--vo-sixel-exit-clear`` 是该选项的一个过时的别名，将来可能被移除。

    ``--vo-sixel-buffered=<yes|no>`` （默认： no）
        在写入到终端之前，缓冲完整的输出序列。在POSIX平台上，这可以帮助防止中断（包括来自其它应用程序的中断），从而防止图像被破坏，但对于某些终端来说，可能要牺牲性能，而且受限于实现细节

    Sixel图像质量的选项：

    ``--vo-sixel-dither=<algo>``
        选择libsixel应该应用的抖动算法。根据libsixel的文档，可以是以下列表中的一个。

        auto （默认）
            让libsixel选择抖动方法
        none
            不扩散
        atkinson
            用Bill Atkinson的方法进行扩散
        fs
            用Floyd-Steinberg的方法扩散
        jajuni
            用Jarvis, Judice & Ninke的方法进行扩散
        stucki
            用Stucki的方法进行扩散
        burkes
            用Burkes的方法进行扩散
        arithmetic
            位置稳定的算术抖动
        xor
            基于位置稳定的算术xor抖动

    ``--vo-sixel-fixedpalette=<yes|no>`` （默认： yes）
        使用libsixel的内置静态调色板，使用XTERM256配置预设进行抖动。固定调色板使用256色进行抖动。请注意，使用 ``no`` （在撰写本文时）会减慢 ``xterm`` 的速度。

    ``--vo-sixel-reqcolors=<colors>`` （默认： 256）
        对固定调色板没有影响。设置libsixel使用动态调色板所需的颜色数。这个值也取决于终端仿真器。Xterm支持256种颜色。可以把这个值设得低一些，以提高性能。

    ``--vo-sixel-threshold=<threshold>`` （默认： -1）
        对固定调色板没有影响。定义改变调色板的阈值 —— 以颜色数量的百分比表示，例如，当颜色数量改变20%时，20将改变调色板。这是一个减少调色板变化次数的简单措施，因为在某些终端（ ``xterm`` ）中它可能很慢。默认的(-1)将在每一帧上选择一个调色板，并且会有更好的质量。

``image``
    将每一帧输出到当前目录下的一个图像文件。每个文件名是用前导零填充的帧号。

    支持以下全局选项：

    ``--vo-image-format=<format>``
        选择图像文件格式

        jpg
            JPEG文件，扩展名为.jpg（默认）
        jpeg
            JPEG文件，扩展名为.jpeg
        png
            PNG文件
        webp
            WebP文件

    ``--vo-image-png-compression=<0-9>``
        PNG压缩系数（速度与文件大小的权衡）（默认： 7）
    ``--vo-image-png-filter=<0-5>``
        在PNG压缩前应用的过滤器（0 = none; 1 = sub; 2 = up; 3 = average; 4 = Paeth; 5 = mixed）（默认： 5）
    ``--vo-image-jpeg-quality=<0-100>``
        JPEG质量系数（默认： 90）
    ``--vo-image-jpeg-optimize=<0-100>``
        JPEG优化系数（默认： 100）
    ``--vo-image-webp-lossless=<yes|no>``
        启用写入无损质量的WebP文件（默认： no）
    ``--vo-image-webp-quality=<0-100>``
        WebP质量（默认： 75）
    ``--vo-image-webp-compression=<0-6>``
        WebP压缩系数（默认： 4）
    ``--vo-image-outdir=<dirname>``
        指定保存图像文件的目录（默认： ``./`` ）

``libmpv``
    用于libmpv的直接嵌入。作为一个特例，在macOS上，它被当作mpv(cocoa-cb)中的一个普通视频输出使用。否则在其他情况下是无用的（参见 ``<mpv/render.h>`` ）。

    这也支持许多 ``gpu`` 视频输出的选项，取决于后端。

``drm`` (Direct Rendering Manager)
    https://mpv.io/manual/master/#video-output-drivers-drm

``mediacodec_embed`` （安卓）
    将 ``IMGFMT_MEDIACODEC`` 帧直接渲染到 ``android.view.Surface`` 。需要 ``--hwdec=mediacodec`` 的硬件解码，以及 ``--vo=mediacodec_embed`` 和 ``--wid=(intptr_t)(*android.view.Surface)``

    由于这个视频输出使用原生解码和渲染程序，mpv的许多功能（字幕渲染、OSD/OSC、视频滤镜等）在这个驱动中是不可用的。

    要使用硬解码应使用 ``--vo=gpu`` ，并一起使用 ``--hwdec=mediacodec`` 或 ``--hwdec=mediacodec-copy`` 和 ``--gpu-context=android``

``wlshm`` （Wayland独占）
    没有硬件加速的共享内存视频输出驱动，只要有Wayland就能工作。

    从mpv 0.30.0开始，你可能需要使用 ``--profile=sw-fast`` 来获得合格的性能。

    .. note:: 这只是一个后备方案，通常不应使用。
