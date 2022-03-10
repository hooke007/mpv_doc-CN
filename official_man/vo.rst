视频输出驱动
============

视频输出驱动是连接不同视频输出设备的接口。其语法是：

``--vo=<driver1,driver2,...[,]>``
    指定一个要使用的视频输出驱动的优先级列表。

如果这个列表末尾有 ``,`` ，mpv将回退到不在列表中的驱动程序。

.. note::

    参见 ``--vo=help`` 获取已编译的视频输出驱动的列表。

    ``--vo=gpu`` 是默认的推荐的输出驱动。其他所有的驱动都是为了兼容性或特定场景。如果默认值无效，它将回退到其他驱动（优先顺序和 ``--vo=help`` 列出的相同）。

可用的视频输出驱动有：

``gpu``
    通用的可定制的、GPU加速的视频输出驱动。它支持扩展缩放方式、抖动、色彩管理、自定义着色器、HDR等。

    参见 `GPU renderer options`_ ，了解该视频输出的特定选项。

    默认情况下，它尝试使用快速和低故障的安全设置。使用配置预设 ``gpu-hq`` 来使初始设置为高质量渲染。这个配置预设可以通过 ``--profile=gpu-hq`` 来应用，其内容可以用 ``--show-profile=gpu-hq`` 来查看。

    这个视频输出虚拟了几个可能的图形API和窗口环境，可以用 ``--gpu-api`` 和 ``--gpu-context`` 选项来影响它们。

    OpenGL-interop的硬件解码在一定程度上受支持。请注意在这种模式下，一些边缘情况可能无法被良好处理，并且色彩空间转换和色度还原通常由硬解码API负责。

    ``gpu`` 默认使用FBOs。有时你可以通过改变选项 ``--fbo-format`` 为 ``rgb16f``, ``rgb32f`` 或 ``rgb`` 来达到更好的质量或性能。已知的问题包括Mesa/Intel不接受 ``rgb16`` ，Mesa有时不支持浮点纹理，以及一些macOS的设置在使用 ``rgb16`` 时非常慢，但使用``rgb32f``时非常快。如果你存在运行问题，也可以尝试启用 ``--gpu-dumb-mode=yes`` 选项。

``gpu-next``
    基于 ``libplacebo`` 的实验性视频渲染器。它几乎支持与 ``--vo=gpu`` 相同的功能集。列表参见 `GPU renderer options`_

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
    使用VDPAU接口来显示，也可以选择对视频进行解码。硬件解码需要和 ``--hwdec=vdpau`` 一起使用。注意，除了兼容性之外，绝对没有理由使用它。我们强烈建议你使用 ``--vo=gpu`` ``--hwdec=nvdec`` 代替它们。

    .. note::

        早期版本的mpv（和MPlayer mplayer2）提供了调整vdpau后处理的子选项，如 ``deint``  ``sharpen`` ``denoise`` ``chroma-deint`` ``pullup`` ``hqscaling`` 。这些子选项已过时，你应该使用视频滤镜 ``vdpaupp`` 来代替。

    支持以下全局选项：

    ``--vo-vdpau-sharpen=<-1-1>``
        （已过时。参见关于 ``vdpaupp`` 的note）

        正值对视频应用锐化算法，负值则为模糊算法（默认： 0）
    ``--vo-vdpau-denoise=<0-1>``
        （已过时。参见关于 ``vdpaupp`` 的note）

        对视频应用降噪算法（默认： 0；不降噪）
    ``--vo-vdpau-chroma-deint``
        （已过时。参见关于 ``vdpaupp`` 的note）

        使时域去交错器同时对亮度和色度扫描（默认）。使用no-chroma-deint只扫描亮度并加速高级去隔行。对慢速显存有用。
    ``--vo-vdpau-pullup``
        （已过时。参见关于 ``vdpaupp`` 的note）

        尝试应用反胶卷过带，需要运动自适应的时域反交错。
    ``--vo-vdpau-hqscaling=<0-9>``
        （已过时。参见关于 ``vdpaupp`` 的note）

        0
            使用默认的VDPAU缩放比例（默认）
        1-9
            应用高质量的VDPAU缩放（需要合格的硬件）
    ``--vo-vdpau-fps=<number>``
        覆盖自动检测的显示器刷新率值（该值对于framedrop来说是需要的，以允许视频播放速率高于显示刷新率，并用于vsync-aware的帧计时调整）。默认0表示使用自动检测的值。正值被解释为刷新率，单位是Hz，并覆盖了自动检测值。负值禁用所有的计时调整和framedrop逻辑。
    ``--vo-vdpau-composite-detect``
        英伟达当前的VDPAU实现在合成窗口管理器下的行为有些不同，不能提供准确的帧计时信息。启用该选项后，播放器将尝试检测合成窗口管理器是否处于活动状态。如果检测到了，播放器将禁用计时调整，就像用户指定了 ``fps=-1`` 一样（因为它们将基于错误的输入）。这意味着计时的准确性比没有合成的情况下要低一些，但由于NVIDIA驱动程序的合成模式行为，即使没有禁用逻辑，也没有硬性的播放速度限制。默认启用，使用 ``--vo-vdpau-composite-detect=no`` 来禁用。
    ``--vo-vdpau-queuetime-windowed=<number>`` ``queuetime-fs=<number>``
        使用VDPAU的presentation queue功能，对未来的视频帧变化最多提前这么多毫秒的队列（默认： 50）。其他信息见下文。
    ``--vo-vdpau-output-surfaces=<2-15>``
        分配这么多输出surface来显示视频帧（默认： 3）。其他信息见下文。
    ``--vo-vdpau-colorkey=<#RRGGBB|#AARRGGBB>``
        设置VDPAU的presentation queue的背景颜色，在实践中，如果VDPAU在overlay模式下运行，它就是使用的colorkey（默认： ``#020507`` ，某种黑色的阴影）。如果这个值的alpha分量为0，就会使用VDPAU的默认colorkey（通常为绿色）。
    ``--vo-vdpau-force-yuv``
        不接受RGBA输入。这意味着mpv将插入一个滤镜，在视频输出之前转换为YUV格式。有时对强制使用某些YUV专用的功能很有用，比如视频均衡器或去隔行扫描。

    使用由queuetime
选项控制的VDPAU的frame queuing功能使mpv的帧翻转时间对系统CPU负载不那么敏感，并允许mpv略提前解码下一帧，这可以减少个别解码缓慢的帧造成的抖动。然而，如果VDPAU正在使用blit queue（主要发生在你启用composite extension的情况下），并且该功能处于激活状态，NVIDIA图形驱动可能会使例如窗口移动不稳定。如果这种情况发生在你的系统上，并且让你感到困扰，那么你可以将queuetime值设置为0来禁用这个功能。在窗口模式和全屏模式下使用的设置是分开的，在全屏模式下应该没有理由禁用这个功能（因为驱动问题不应该影响视频本身）。

    你可以通过增加queuetime值和 ``output_surfaces`` 计数来提前排队等候更多的帧（为了确保有足够的surfaces来提前缓冲视频，你需要至少与视频在该时间内的帧数一样多的surfaces，再加上两个）。这可以帮助在某些情况下使视频更流畅。主要的缺点是增加了surfaces的视频RAM要求，以及对用户命令的显示响应更滞后（显示变化要在排队后的一段时间内才会显现）。图形驱动的实现也可能对最大队列时间的长度或队列的surface数量有限制，或根本无法正常工作。

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

    ``--vo-vaapi-deint-mode=<mode>``
        选择去隔行扫描算法。注意默认情况下，去隔行扫描最初总是关闭的，需要用 ``d`` 键来启用（ ``cycle deinterlace`` 的默认按键绑定）。

        如果libva支持视频后处理（vpp），这个选项就不适用。在这种情况下， ``deint-mode`` 的默认值是 ``no`` ，通过用户交互使用上述方法启用去交错，实际上是插入了 ``vavpp`` 视频滤镜。如果使用的libva后端实际上不支持vpp，你可以使用这个选项强行启用基于视频输出的去隔行扫描。

        no
            不允许去隔行扫描（较新的libva的默认值）
        first-field
            只显示第一个场
        bob
            bob去隔行扫描（较早的libva的默认值）

    ``--vo-vaapi-scaled-osd=<yes|no>``
        如果启用，那么OSD将按视频分辨率渲染，并按显示分辨率进行缩放。默认情况下，这个功能是禁用的，如果驱动程序支持，OSD将以显示分辨率渲染。

``null``
    无视频输出。对于基准测试很有用。

    通常情况下，用 ``--no-video`` 来禁用视频更好。

    支持以下全局选项：

    ``--vo-null-fps=<value>``
        模拟显示FPS。这人为地限制了视频输出每秒接受的帧数。

``caca``
    Color ASCII art video output driver that works on a text console.

    .. note:: This driver is a joke.

``tct``
    彩色Unicode艺术视频输出驱动，在文本控制台中工作。默认情况下，取决于现代终端对真彩色的支持，以完整色范围显示图像，但也支持256色输出（见下文）。在Windows上，它需要一个ansi终端例如mintty。

    从mpv 0.30.0开始，你可能需要使用 ``--profile=sw-fast`` 来获得合格的性能。

    注意：TCT图像输出与mpv的其他终端输出不同步，这可能导致图像破碎。选项 ``--no-terminal`` 或 ``--really-quiet`` 有助于解决这个问题。

    ``--vo-tct-algo=<algo>``
        选择如何将像素写入到终端

        half-blocks
            使用unicode LOWER HALF BLOCK字符来实现更高的垂直分辨率（默认）
        plain
            使用空格。导致垂直分辨率下降两重，但理论上在更多地方起作用

    ``--vo-tct-width=<width>`` ``--vo-tct-height=<height>``
        假设终端有指定的字符宽度和/或高度。如果不能检测终端尺寸，这些默认为80x25

    ``--vo-tct-256=<yes|no>`` （默认： no）
        使用256色 —— 用于不支持真彩色的终端

``sixel``
    使用sixels的终端图形输出。用 ``mlterm`` 和 ``xterm`` 测试。

    注意：Sixel图像输出与mpv的其他终端输出不同步，这可能导致图像破碎。选项 ``--really-quiet`` 有助于解决这个问题，建议使用。

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

    ``--vo-sixel-exit-clear=<yes|no>`` （默认： yes）
        是否在退出时清除终端。当设置为no时 —— 退出后最后一个sixel图像留在屏幕上，光标跟随它。

    Sixel图像质量选项：

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

``rpi`` （树莓派）
    在树莓派上使用MMAL API进行原生视频输出。

    这已过时。使用 ``--vo=gpu`` 代替，这是默认的且提供相同的功能。 ``rpi`` 视频输出将在mpv 0.23.0中被删除。它的功能被折叠到--vo=gpu中，现在通过把它当作硬件overlay来使用RPI硬件解码（不应用GL filtering）。在0.23.0中还将改变：--fs标志在默认情况下将被重置为 "no"（就像在其他平台上）。

    支持以下过时的全局选项：

    ``--rpi-display=<number>``
        选择视频overlay应显示的显示器号码（默认： 0）

    ``--rpi-layer=<number>``
        选择视频overlay应显示的dispmanx层（默认： -10）。注意，mpv也将使用所选层上面的2个层，来处理窗口背景和OSD。实际的视频渲染将发生在所选层上面的那一层。

    ``--rpi-background=<yes|no>``
        是否在视频后面渲染一个黑色背景（默认： no）。通常情况下，最好结束控制台的framebuffer，这样会有更好的性能。

    ``--rpi-osd=<yes|no>``
        默认情况下启用。如果用 ``no`` 禁用，就不会创建OSD层。这也意味着将不会有字幕被渲染。

``drm`` (Direct Rendering Manager)
    使用Kernel Mode Setting / Direct Rendering Manager的视频输出驱动。应该在不想安装完整的图形环境时使用（例如，没有X）。不支持硬件加速（如果你需要，请检查 ``drm`` 后端的 ``gpu`` 视频输出）。

    从mpv 0.30.0开始，你可能需要使 ``--profile=sw-fast`` 来获得合格的性能。

    支持以下全局选项：

    ``--drm-connector=[<gpu_number>.]<name>``
        选择要使用的连接器（通常是显示器）。如果 ``<name>`` 为空或 ``auto`` ，mpv将在第一个可用的连接器上渲染输出。使用 ``--drm-connector=help`` 来获取可用连接器的列表。 ``<gpu_number>`` 参数可用于区分多个显卡，但已过时，改为使用 ``--drm-device`` 。（默认： 空）

    ``--drm-device=<path>``
        选择要使用的DRM设备文件。如果指定了这个文件，它将取代自动选择卡和任何指定的卡号 ``--drm-connector`` 。（默认： 空）

    ``--drm-mode=<preferred|highest|N|WxH[@R]>``
        要使用的模式（分辨率和帧速率）。可能的值：

        :preferred: 使用所选连接器上的屏幕的首选模式（默认）
        :highest:   使用所选连接器上可用的最高分辨率的模式
        :N:         通过索引选择模式
        :WxH[@R]:   通过宽度、高度和可选的刷新率来指定模式。如果有几种模式相匹配，则选择EDID模式列表中排在第一位的模式。

        使用 ``--drm-mode=help`` 来获得所有活动连接器的可用模式列表。

    ``--drm-atomic=<no|auto>``
        切换使用原子模式设置。这在调试时非常有用。

        :no:    使用传统的模式设置
        :auto:  使用原子模式设置，如果不能使用，则退回到传统模式设置（默认）

        注意：只影响到 ``gpu-context=drm`` 。 ``vo=drm`` 只支持传统的模式设置。

    ``--drm-draw-plane=<primary|overlay|N>``
        选择DRM平面，在正常情况下，视频和OSD被绘制到该平面。该平面可以被指定为 ``primary`` ，它将选择第一个适用的主平面； ``overlay`` ，它将选择第一个适用的覆盖平面；或者通过索引。索引是基于零的，与CRTC有关（默认： primary）

        当与drmprime-drm hwdec互操作使用该选项时，只有OSD被渲染到这个平面。

    ``--drm-drmprime-video-plane=<primary|overlay|N>``
        选择DRM平面，用于drmprime-drm hwdec接口的视频（例如RockChip SoC上的rkmpp hwdec，以及其他各种SoC上的v4l2 hwdec）。否则，该平面将不被使用。该选项接受与 ``--drm-draw-plane`` 相同的值。（默认： overlay）

        为了能够在不同的SoC上成功播放4K视频，你可能需要设置 ``--drm-draw-plane=overlay --drm-drmprime-video-plane=primary`` ，并设置 ``--drm-draw-surface-size=1920x1080`` ，以较低的分辨率渲染OSD（由hwdec处理的视频将在drmprime-video平面上以全4K分辨率显示）

    ``--drm-format=<xrgb8888|xrgb2101010>``
        选择要使用的DRM格式（默认： xrgb8888）。这允许你选择DRM模式的比特深度。xrgb8888是你常用的每像素24比特/每通道8比特的填充RGB格式。xrgb2101010是每像素30比特/每通道10比特的填充RGB格式，有2比特的填充。

        在某些情况下，xrgb2101010可以在 ``drm`` 视频输出中工作，但不能在 ``gpu`` 视频输出的 ``drm`` 后端工作。这是因为使用 ``gpu`` 视频输出，除了需要DRM驱动的支持外，还需要EGL驱动对xrgb2101010的支持。

    ``--drm-draw-surface-size=<[WxH]>``
        设置在绘制平面上使用的曲面的大小。然后，该曲面将被放大到当前的屏幕分辨率。这个选项在高分辨率下与drmprim-drm hwdec互操作一起使用时非常有用，因为它允许将绘制平面（在这种情况下只处理OSD）缩小到GPU可以处理的尺寸。

        当不使用drmprime-drm hwdec互操作时，这个选项只会导致视频在不同的分辨率下被渲染，然后被缩放到屏幕尺寸。

        注意：这个选项只有在支持DRM atomic的情况下才可用（默认： display resolution）

``mediacodec_embed`` （安卓）
    将 ``IMGFMT_MEDIACODEC`` 帧直接渲染到 ``android.view.Surface`` 。需要 ``--hwdec=mediacodec`` 的硬件解码，以及 ``--vo=mediacodec_embed`` 和 ``--wid=(intptr_t)(*android.view.Surface)``

    由于这个视频输出使用原生解码和渲染程序，mpv的许多功能（字幕渲染、OSD/OSC、视频滤镜等）在这个驱动中是不可用的。

    要使用硬解码应使用 ``--vo=gpu`` ，并一起使用 ``--hwdec=mediacodec-copy`` 和 ``--gpu-context=android``

``wlshm`` （Wayland独占）
    没有硬件加速的共享内存视频输出驱动，只要有Wayland就能工作。

    从mpv 0.30.0开始，你可能需要使用 ``--profile=sw-fast`` 来获得合格的性能。

    .. note:: 这只是一个后备方案，通常不应使用。
