视频滤镜
========

视频滤镜允许你修改视频流和它的属性。本节描述的所有信息也适用于音频滤镜（一般使用前缀 ``--af`` 而不是 ``--vf`` ）。

确切的语法是：

``--vf=<filter1[=parameter1:parameter2:...],filter2,...>``
    设置一个视频滤镜链。这包括滤镜的名称，以及 ``=`` 后面的参数选项列表。参数由 ``:`` 分隔（不是 ``,`` ，因为那会开始一个新的滤镜条目）。

    在滤镜名称之前，可以用 ``@name:`` 指定一个标签，其中name是一个用户给定的任意的名称，用来标识该滤镜。只有当你想在运行时切换滤镜的时候才需要这样做。

    滤镜名称前的 ``!`` 表示该滤镜默认是禁用的。它将在滤镜创建时被跳过。这对运行时的滤镜切换也很有用。

    参见 ``vf`` 命令（和 ``toggle`` 子命令）的进一步解释和示例。

    这是一个对象设定列表选项。详见 `列表选项`_

    一般的滤镜条目语法是：

        ``["@"<label-name>":"] ["!"] <filter-name> [ "=" <filter-parameter-list> ]``

    或者对于特殊的 "toggle" 语法（参见 ``vf`` 命令）：

        ``"@"<label-name>``

    和 ``filter-parameter-list`` ：

        ``<filter-parameter> | <filter-parameter> "," <filter-parameter-list>``

    和 ``filter-parameter`` ：

        ``( <param-name> "=" <param-value> ) | <param-value>``

    ``param-value`` 可以进一步用 ``[`` / ``]`` 来引用，如果该值包含 ``,`` 或 ``=`` 等字符。这一点特别适用于 ``lavfi`` 滤镜，它使用与mpv（MPlayer历史上的）非常相似的语法来指定滤镜及其参数。

.. note::

    ``--vf`` 只能以单个轨道作为输入，即使过滤器支持动态输入。无法使用需要多个输入的滤镜。对于这种情况，请使用 ``--lavfi-complex`` 。这也适用于 ``--af`` 。

滤镜可以在运行时被操控。你可以使用上面描述的 ``@`` 标签，结合 ``vf`` 命令（参见 `命令接口`_ ）来获得更多的控制。初始禁用的滤镜与 ``!`` 在这方面也很有用。

.. note::

    要获得可用的视频滤镜的完整列表，参见 ``--vf=help`` 和 https://ffmpeg.org/ffmpeg-filters.html

    另外，请记住，大多数实际的滤镜是通过 ``lavfi`` wrapper获得的，它可以让你使用libavfilter的大多数滤镜。这包括所有从MPlayer移植到libavfilter的滤镜。

    大多数内置滤镜在某些方面已经过时了，除非它们只在mpv中可用（比如处理mpv特性的滤镜，或者只在mpv中实现的）。

    如果一个滤镜不是内置的， ``lavfi-bridge`` 将被自动尝试。这个bridge不支持支援输出，也不在实际使用滤镜之前验证参数。尽管mpv的语法与libavfilter的相当相似，但它并不一样（这表示不是所有vf_lavfi的 ``graph`` 选项接受的东西都会被 ``--vf`` 接受）。

    你也可以在滤镜的名字前缀加上 ``lavfi-`` 来强制使用wrapper。如果滤镜的名字与mpv内置的过时的滤镜相冲突时，这很有帮助。例如， ``--vf=lavfi-scale=args`` 会使用libavfilter的 ``scale`` 滤镜，而不是mpv的过时的内置滤镜。

视频滤镜是在列表中管理的。有许多命令可以管理滤镜列表：

``--vf-append=filter``
    将给定参数的滤镜追加到滤镜列表的后方。

``--vf-add=filter``
    将给定参数的滤镜追加到滤镜列表的后方（目前仍然可以传递多个滤镜，但已过时）。

``--vf-pre=filter``
    将给定参数的滤镜添加到滤镜列表的前方（目前仍然可以传递多个滤镜，但已过时）。

``--vf-remove=filter``
    从列表中删除滤镜。滤镜可以按照添加的方式（滤镜名称和它的完整参数列表），或者通过标签（以 ``@`` 为前缀）给出。滤镜的匹配工作如下：如果任何一个被比较的滤镜有一个标签集，则只比较标签。如果没有一个滤镜有标签，则比较滤镜的名称、参数和参数顺序（目前仍然可以传递多个滤镜，但已过时）。

``--vf-toggle=filter``
    如果给定的滤镜还没有出现，则将其追加到列表的后方；如果已经出现，则将其从列表中移除。滤镜的匹配工作如 ``--vf-remove`` 中所描述。

``--vf-clr``
    完全清空滤镜列表。

对于支持它的滤镜，你可以通过它们的名字访问参数。

``--vf=<filter>=help``
    输出某个特定滤镜的参数名称和参数值范围。

可用的mpv独占滤镜有：

``format=fmt=<value>:colormatrix=<value>:...``
    应用视频参数覆盖，可选择转换。默认情况下，这将覆盖视频的参数而不进行转换（除了 ``fmt`` 参数），但对于支持转换的参数，可以用 ``convert=yes`` 来进行适当的转换。

    ``<fmt>``
        图像格式名称，例如rgb15、bgr24、420p，等等。（默认：不改变。）

        这个滤镜总是执行转换到给定的格式。

        .. note::

            为获取可用的格式列表，使用 ``--vf=format=fmt=help``

        .. note::

            在某些情况下支持硬件格式之间的转换。例如： 从 ``cuda`` 到 ``vulkan`` ，或 ``vaapi`` 到 ``vulkan``.

    ``<convert=yes|no>``
        强制颜色参数的转换（默认： no）。

        如果禁用（默认），可能进行的唯一转换是格式转换，如果 ``<fmt>`` 被设置。所有其它参数（如 ``<colormatrix>`` ）都是强制的，而没有转换。这种模式通常在文件被错误地标记时很有用。

        如果启用了这个功能，如果有任何参数不匹配，就会使用libswscale或zimg。如果mpv的zimg wrapper支持输入/输出图像格式，并且使用了 ``--sws-allow-zimg=yes`` ，就会使用zimg。这两种库可能不支持所有种类的转换。这通常会导致无声的错误转换。zimg在许多情况下有更好的机会正确执行转换。

        在这两种情况下，颜色参数都是在图像格式转换的输出阶段设置的（如果 ``fmt`` 被设置）。不同的是，在 ``convert=no`` 时，颜色参数不会传递给转换器。

        如果输入和输出的视频参数相同，转换总是会被跳过。

        在硬件格式之间转换时，该参数没有影响，唯一进行转换的是格式转换。

        .. admonition:: 示例

            ``mpv test.mkv --vf=format:colormatrix=ycgco``
                结果是不正确的颜色（如果test.mkv被正确标记）。

            ``mpv test.mkv --vf=format:colormatrix=ycgco:convert=yes --sws-allow-zimg``
                结果是真正转换为 ``ycgco`` ，假设渲染器支持它（ ``--vo=gpu``  通常支持）。你可以添加 ``--vo=xv`` 来强制要求一个绝对不支持它的视频输出驱动，它应该显示不正确的颜色作为确认。

                使用 ``--sws-allow-zimg=no`` （或者在构建时禁用zimg）将使用libswscale，它在写入时不能执行这种转换。

    ``<colormatrix>``
        控制播放视频时YUV到RGB色彩空间的转换。有各种标准。通常情况下，标清视频应使用BT.601，高清视频应使用BT.709（这已默认处理）。使用不正确的色彩空间会导致颜色的饱和度略低或过高，并出现偏移。

        这些选项并不总是受支持。不同的视频输出提供不同支持程度的程度。 ``gpu`` 和 ``vdpau`` 视频输出驱动通常提供完全支持。如果系统视频驱动支持的话， ``xv`` 输出可以设置色彩空间，但不支持输入和输出电平。 ``scale`` 视频滤镜可以设置色彩空间和输入电平，但只有在输出格式为RGB的情况下（如果视频输出驱动程序支持RGB输出，你可以用 ``--vf=scale,format=rgba`` 强制实现它）。

        如果这个选项被设置为 ``auto`` （这是默认的），视频的色彩空间标志将被使用。如果该标志没有设置，色彩空间将被自动选择。这是通过一个简单的启发式方法来完成的，它尝试区分标清和高清视频。如果视频大于1279x576像素，将使用BT.709（高清）；否则将选择BT.601（标清）。

        可用的色彩空间有：

        :auto:          自动选择（默认）
        :bt.601:        ITU-R Rec. BT.601 (SD)
        :bt.709:        ITU-R Rec. BT.709 (HD)
        :bt.2020-ncl:   ITU-R Rec. BT.2020 （非恒定亮度）
        :bt.2020-cl:    ITU-R Rec. BT.2020 （恒定亮度）
        :bt.2100-pq:    ITU-R Rec. BT.2100 ICtCp PQ 变体
        :bt.2100-hlg:   ITU-R Rec. BT.2100 ICtCp HLG 变体
        :dolbyvision:   Dolby Vision 杜比视界
        :smpte-240m:    SMPTE-240M

    ``<colorlevels>``
        用于YUV到RGB转换的YUV动态范围。这个选项只有在播放不遵循标准动态范围或被错误标记的损坏文件时才需要。如果视频没有指定它的动态范围，则假定它是有限范围。

        与应用 ``<colormatrix>`` 的限制相同。

        可用的动态范围有：

        :auto:      自动选择（通常是有限范围）（默认）
        :limited:   有限范围（亮度为16-235，色度为16-240）
        :full:      全范围（亮度和色度都为0-255）

    ``<primaries>``
        源文件被编码的RGB原色。通常这应该设置在文件头中，但是当播放损坏或错误标记的文件时，可以用它来覆盖这个设置。

        这个选项只影响执行色彩管理的视频输出驱动，例如， ``gpu`` 设置了 ``target-prim`` 或 ``icc-profile`` 子选项。

        如果这个选项被设置为 ``auto`` （这是默认的），视频的色彩原色标志将被使用。如果该标志没有设置，将自动选择颜色空间，使用以下启发式方法。如果 ``<colormatrix>`` 被设置或确定为BT.2020或BT.709，就会使用相应的原色。否则，如果视频高度正好是576（PAL），则使用BT.601-625。如果正好是480或486（NTSC），则使用BT.601-525。如果视频分辨率是其他的，则使用BT.709。

        可用的色彩原色有：

        :auto:         自动选择（默认）
        :bt.601-525:   ITU-R BT.601 (SD) 525-line systems (NTSC, SMPTE-C)
        :bt.601-625:   ITU-R BT.601 (SD) 625-line systems (PAL, SECAM)
        :bt.709:       ITU-R BT.709 (HD)（等同sRGB原色）
        :bt.2020:      ITU-R BT.2020 (UHD)
        :apple:        Apple RGB
        :adobe:        Adobe RGB (1998)
        :prophoto:     ProPhoto RGB (ROMM)
        :cie1931:      CIE 1931 RGB
        :dci-p3:       DCI-P3 (Digital Cinema)
        :v-gamut:      Panasonic V-Gamut primaries

    ``<gamma>``
       源文件被编码的伽马函数。通常情况下，这应该设置在文件头中，但当播放损坏或错误标记的文件时，可以用它来覆盖设置。

       这个选项只影响执行色彩管理的视频输出驱动程序。

       如果这个选项被设置为 ``auto`` （这是默认值），那么对于YCbCr内容，伽玛将被设置为BT.1886，对于RGB内容，将被设置为sRGB，对于XYZ内容，将被设置为Linear。

       可用的伽玛函数有：

       :auto:         自动选择（默认）
       :bt.1886:      ITU-R BT.1886 (EOTF corresponding to BT.601/BT.709/BT.2020)
       :srgb:         IEC 61966-2-4 (sRGB)
       :linear:       Linear light
       :gamma1.8:     Pure power curve (gamma 1.8)
       :gamma2.0:     Pure power curve (gamma 2.0)
       :gamma2.2:     Pure power curve (gamma 2.2)
       :gamma2.4:     Pure power curve (gamma 2.4)
       :gamma2.6:     Pure power curve (gamma 2.6)
       :gamma2.8:     Pure power curve (gamma 2.8)
       :prophoto:     ProPhoto RGB (ROMM) curve
       :pq:           ITU-R BT.2100 PQ (Perceptual quantizer) curve
       :hlg:          ITU-R BT.2100 HLG (Hybrid Log-gamma) curve
       :v-log:        Panasonic V-Log transfer curve
       :s-log1:       Sony S-Log1 transfer curve
       :s-log2:       Sony S-Log2 transfer curve

    ``<sig-peak>``
        视频文件的参考峰值照度，相对于信号的参考白电平。这对HDR来说很重要，但也可以用色调映射SDR内容来模拟不同的曝光。通常从最大内容亮度或母版元数据等标签中推断出来。

        默认的0.0将默认为源的标称峰值亮度。

    ``<light>``
        场景的亮度类型。这主要是根据伽马函数正确推断出来的，但在查看raw camera footage（例如V-Log）时，覆盖这一点可能很有用，因为它通常是基于场景参考的，而不是基于显示参考的。

        可用的亮度类型有：

       :auto:         自动选择（默认）
       :display:      Display-referred light（大多数内容）
       :hlg:          Scene-referred using the HLG OOTF (e.g. HLG content)
       :709-1886:     Scene-referred using the BT709+BT1886 interaction
       :gamma1.2:     Scene-referred using a pure power OOTF (gamma=1.2)

    ``<dolbyvision=yes|no>``
        是否包含杜比视界元数据（默认： yes）。如果禁用，将从帧中剥离任何杜比视界元数据。

    ``<hdr10plus=yes|no>``
        是否包含HDR10+元数据（默认： yes）。如果禁用，将从帧中剥离任何HDR10+元数据。

    ``<film-grain=yes|no>``
        是否包括胶片颗粒元数据（默认： yes）。如果禁用，任何胶片颗粒元数据都将从帧中剥离。

    ``<chroma-location>``
        设置视频的色度位置。使用 ``--vf=format:chroma-location=help`` 来列出所有可用模式。

    ``<stereo-in>``
        设置视频被假定为编码的立体模式。使用 ``--vf=format:stereo-in=help`` 来列出所有可用模式。检查 ``stereo3d`` 的滤镜文档，看看这些名称的含义。

    ``<rotate>``
        设置视频的旋转度，假定是以度数进行编码。特殊值 ``-1`` 使用输入的格式。

    ``<w>``, ``<h>``
        如果不是0，执行转换到给定的尺寸。如果没有设置 ``convert=yes`` ，则忽略。

    ``<dw>``, ``<dh>``
        设置显示尺寸。请注意，设置显示尺寸，使视频在两个方向上都被缩放，而不仅仅是改变宽高比，这是一个实现细节，以后可能会改变。

    ``<dar>``
        设置视频帧的显示长宽比。这是一个浮点数，但也可以传递诸如 ``[16:9]`` 之类的值（用 ``[...]`` 来引用，以防止选项解析器解释 ``:`` 字符）。

    ``<force-scaler=auto|zimg|sws>``
        如果适用的话，强制一个特定的缩放器后端。这是一个调试选项，随时可能消失。

    ``<alpha=auto|straight|premul|none>``
        设置视频使用的透明种类。如果图像格式没有透明通道，则未定义效果（可能被忽略或导致错误，取决于mpv内部如何发展）。设置这个可能会或不会导致下游的图像处理以不同的方式处理透明度，这取决于支持的情况。使用了 ``convert`` 或zimg，这将转换透明。libswscale和其他FFmpeg组件会完全忽略这一点。 ``none`` 仅在 libplacebo vN.344.0 开始可用。

``lavfi=graph[:sws-flags[:o=opts]]``
    使用FFmpeg的libavfilter过滤视频。

    ``<graph>``
        libavfilter graph的字符串。该滤镜必须有一个视频输入pad和一个视频输出pad

        语法和可用的滤镜参见 `<https://ffmpeg.org/ffmpeg-filters.html>`_ 

        .. warning::

            如果你想用这个选项使用完整的滤镜语法，你必须引用滤镜graph，以防止mpv的语法和滤镜graph的语法发生冲突。为了防止引用和转义的混乱，如果你知道你想从输入文件中使用哪个视频轨道，可以考虑使用 ``--lavfi-complex`` （反正几乎所有的视频文件都只有一个视频轨道）。

        .. admonition:: 示例

            ``--vf=lavfi=[gradfun=20:30,vflip]``
                ``gradfun`` 滤镜带无意义的参数，接着是 ``vflip`` 滤镜（这展示了libavfilter如何接受一个graph，而不仅仅是一个滤镜）。滤镜graph的字符串是用 ``[`` 和 ``]`` 引用的。这不需要在某些shell（如bash）中使用额外的引用或转义，而其他shell（如zsh）则需要在选项字符串周围加上额外的 ``"`` 来引用。

            ``'--vf=lavfi="gradfun=20:30,vflip"'``
                和前面一样，但使用的是所有shell都安全的引用。外侧的 ``'`` 引用确保shell不会删除mpv所需的 ``"`` 引用。

            ``'--vf=lavfi=graph="gradfun=radius=30:strength=20,vflip"'``
                和之前一样，但对所有东西都使用命名的参数。

    ``<sws-flags>``
        如果libavfilter插入了像素格式转换的滤镜，这个选项给出了应该传递给libswscale的标志。这个选项是数值型的，并采用 ``SWS_`` 标志的位数组合。

        参见 ``https://git.videolan.org/?p=ffmpeg.git;a=blob;f=libswscale/swscale.h``

    ``<o>``
        设置AVFilterGraph选项。这些应该在FFmpeg中有所记录。

        .. admonition:: 示例

            ``'--vf=lavfi=yadif:o="threads=2,thread_type=slice"'``
                强制一个特定的线程设置。

``sub=[=bottom-margin:top-margin]``
    将字幕渲染移到滤镜链中的一个任意点，或在视频滤镜中强制进行字幕渲染，而不是使用视频输出OSD支持。

    ``<bottom-margin>``
        在帧的底部添加一个黑带。SSA/ASS渲染器可以在那里放置字幕（使用 ``--sub-use-margins`` ）。
    ``<top-margin>``
        顶部的黑带用于放置顶部字幕（使用 ``--sub-use-margins`` ）。

    .. admonition:: 示例

        ``--vf=sub,eq``
            将字幕的渲染移到eq滤镜之前。这将使字幕颜色和视频都受到视频均衡器设置的影响。

``vapoursynth=file:buffered-frames:concurrent-frames:user-data``
    加载一个VapourSynth滤镜脚本。这是为流处理准备的：mpv实际上提供了一个源滤镜，而不是使用原生的VapourSynth视频源。mpv源将只在一个小的帧窗口内响应帧请求（这个窗口的大小由 ``buffered-frames`` 参数控制），超出的请求将返回错误。因此，你不能使用VapourSynth的全部功能，但你可以使用某些滤镜。

    .. warning::

        不要使用这个滤镜，除非你有VapourSynth的专业知识，并且知道如何修复mpv VapourSynth wrapper代码中的错误。

    如果你只是想播放VapourSynth生成的视频（例如使用原生的VapourSynth视频源），最好使用 ``vspipe`` 和一个pipe或FIFO来把视频送入mpv。如果滤镜脚本需要随机的帧访问（参见 ``buffered-frames`` 参数），同样适用。

    ``file``
        脚本源的文件名。目前，这总是一个Python脚本（VapourSynth惯例下的 ``.vpy`` ）。

        变量 ``video_in`` 被设置为mpv的视频源，希望脚本能从它那里读取视频（否则，mpv将不解码视频，视频packet队列将溢出，最终导致只有音频播放，或者更糟）。

        脚本创建的graph滤镜也应该使用 ``_DurationNum`` 和 ``_DurationDen`` 帧属性来透传时间戳。

        关于mpv定义的脚本变量的完整列表，参见选项列表的末尾。

        .. admonition:: 示例：

            ::

                import vapoursynth as vs
                from vapoursynth import core
                core.std.AddBorders(video_in, 10, 10, 20, 20).set_output()

        .. warning::

            该脚本将在每次跳转时被重新加载。这样做是为了在不连续的情况下正确重置滤镜。

    ``buffered-frames``
        在滤镜之前应该缓冲的最大解码视频帧数（默认： 4）。这指定了脚本在向后方向上可以请求的最大帧数。

        例如，如果 ``buffered-frames=5`` ，脚本刚刚请求了第15帧，它仍然可以请求第10帧，但第9帧已经不可用。如果它请求第30帧，mpv将再解码15帧，而只保留第25-30帧。

        这个缓冲区存在的唯一原因是为了满足VapourSynth滤镜的随机访问请求。

        VapourSynth API有一个 ``getFrameAsync`` 函数，它需要一个绝对的帧数。源滤镜必须对所有的请求作出回应。例如，一个源滤镜可以请求第2432帧，然后是第3帧。源滤镜通常通过预先索引整个文件来实现这一点。

        另一方面，mpv是面向流的，不允许滤镜进行跳转（而且允许这样做是无意义的，因为这样会有损性能）。滤镜在播放过程中按顺序获得帧，不能不按顺序请求它们。

        为了弥补这种不匹配，mpv允许滤镜在一个特定的窗口内访问帧。 ``buffered-frames`` 控制这个窗口的大小。大多数VapourSynth滤镜恰好与此配合，因为mpv请求的帧是依次增加的，而大多数滤镜只需要请求“临近”的帧。

        如果滤镜请求的帧序号比缓冲的最高帧还高，新的帧将被解码，直到达到请求的帧序数。超过数量的帧将以先进先出的方式被刷掉（这个缓冲区里的最大数量只有 ``buffered-frames`` ）。

        如果滤镜请求的帧序号比缓冲区内最低帧还低，那么这个请求就不能被满足，并且会向滤镜返回一个错误。这种错误不应该发生在一个“正确的”VapourSynth环境中。具体会发生什么，取决于所涉及的滤镜。

        增加这个缓冲区不会改善性能。相反，它会浪费内存，并减慢跳转速度（当需要一次性解码足够多的帧来填充缓冲区时）。它只是为了防止上一段所述的错误。

        一个滤镜需要多少帧取决于滤镜的实现细节，mpv无法知道。一个缩放滤镜可能只需要1帧，一个插值滤镜可能需要少量帧，而 ``Reverse`` 滤镜将需要无限帧。

        如果你想在VapourSynth的能力范围内可靠地运行，请使用 ``vspipe``

        缓冲帧的实际数量也取决于 ``concurrent-frames`` 选项的值。目前，两个选项的值相乘，得到最终的缓冲区大小。

    ``concurrent-frames``
        应该并行请求的帧的数量。并行的程度取决于滤镜和mpv解码视频以提供给滤镜的速度。这个值可能应该与你机器上的核心数量成正比。大多数时候，使其高于核心数实际上会使其变慢。

        技术上来说，mpv将循环调用VapourSynth的 ``getFrameAsync`` 函数，直到有 ``concurrent-frames`` 帧还没有被滤镜返回。这也是假设mpv滤镜链的其他部分能够快速读取 ``vapoursynth`` 滤镜的输出（例如，如果你暂停播放器，过滤将很快停止，因为过滤后的帧在队列中等待）。

        实际的并行性取决于许多其他因素。

        默认情况下，这使用特殊值 ``auto`` ，它将选项设置为检测到的逻辑CPU核心的数量。

    ``user-data``
        传递给脚本的可选任意字符串。如果未设置，默认为空字符串。

    以下 ``.vpy`` 脚本的变量是由mpv定义的：

    ``video_in``
        作为vapoursynth clip的mpv视频源。注意，这有一个不正确的（非常高的）长度设置，这使许多滤镜感到困惑。这是必要的，因为真正的帧数是未知的。你可以在clip上使用 ``Trim`` 滤镜来减少长度。

    ``video_in_dw``, ``video_in_dh``
        视频的显示尺寸。如果视频不使用方形像素（如DVD），可以与视频尺寸不同。

    ``container_fps``
        由文件头报告的FPS值。这个值可能是错误的或完全损坏的（例如0或NaN）。即使这个值是正确的，如果另一个滤镜改变了真实的FPS（通过丢帧或插入帧），这个变量的值将没有用。注意 ``--container-fps-override`` 命令行选项会覆盖这个值。

        对一些坚持要有FPS的滤镜很有用。

    ``display_fps``
        当前显示器的刷新率。注意，这个值可以是0。

    ``display_res``
        当前显示器的分辨率。这是一个整数数组，第一个条目对应宽度，第二个条目对应高度。这些值可以为0。请注意，这不会响应显示器更改，而且可能在所有平台上都无法正常工作。
    ``user_data``
        从滤镜传递的用户数据。该变量始终存在，默认为空字符串。

``vavpp``
    VA-API视频后处理。要求系统支持VA-API，即Linux/BSD独占。只与 ``--vo=vaapi`` 和 ``--vo=gpu`` 一起工作。目前是去交错。如果要求去交错（使用 ``d`` 键，默认映射到 ``cycle deinterlace`` 命令，或 ``--deinterlace`` 选项），这个滤镜会自动插入。

    ``deint=<method>``
        选择反交错的算法。

        no
            不执行去隔行扫描
        auto
             选择最佳质量的去隔行算法（默认）。这按照文档中的选项顺序进行， ``motion-compensated`` 被认为是最佳质量
        first-field
            只显示第一个场
        bob
            bob去隔行扫描
        weave, motion-adaptive, motion-compensated
            高级去隔行扫描算法。这些是否真的有效，取决于GPU硬件、GPU驱动、驱动错误和mpv错误

    ``<interlaced-only>``
        :no:  对所有帧进行隔行扫描（默认）
        :yes: 只对标记为交错的帧进行反交错处理

    ``reversal-bug=<yes|no>``
        :no:  使用旧版Mesa驱动所解析的API。虽然这种解释更明显、更直观，但显然是错误的，而且不被英特尔驱动开发者所认同
        :yes: 使用英特尔对表面前向和后向参考的解释（默认）。这就是英特尔驱动和新的Mesa驱动所期望的。只对高级去隔行扫描算法重要

``vdpaupp``
    VDPAU视频后处理。只对 ``--vo=vdpau`` 和 ``--vo=gpu`` 起作用。如果要求去隔行扫描（使用 ``d`` 键，默认映射到 ``cycle deinterlace`` 命令，或 ``--deinterlace`` 选项），这个滤镜会自动插入。当启用去交错时，如果使用了 ``vdpau`` 视频输出，或如果使用了 ``gpu`` ，并且至少激活了一次硬件解码（例如加载了vdpau），它总是比软件去交错滤镜更具优先级。

    ``sharpen=<-1-1>``
        对于正值，对视频应用锐化算法，对于负值应用模糊算法（默认： 0）
    ``denoise=<0-1>``
        对视频应用降噪算法（默认： 0；不降噪）
    ``deint=<yes|no>``
        是否启用去隔行扫描（默认： no）。如果启用，它将使用 ``deint-mode`` 选择的模式
    ``deint-mode=<first-field|bob|temporal|temporal-spatial>``
        选择去隔行扫描模式（默认： temporal）

        注意，目前有一种机制允许 ``vdpau`` 视频输出改变自动插入的 ``vdpaupp`` 滤镜的 ``deint-mode`` 。为了避免混淆，建议不要使用与过滤有关的 ``--vo=vdpau`` 子选项。

        first-field
            只显示第一个场
        bob
            Bob去隔行扫描
        temporal
            基于运动适应性的时域反交错。可能导致慢速视频硬件和/或高分辨率下的A/V不同步
        temporal-spatial
            基于运动自适应的时域反交错，边缘引导的空间插值。需要快速的视频硬件
    ``chroma-deint``
        使时域反交错器同时运行在亮度和色度上（默认）。使用no-chroma-deint来只使用亮度并加速高级去隔行。对慢速的视频内存很有用
    ``pullup``
        尝试应用反转交错，需要基于运动自适应的时域反交错
    ``interlaced-only=<yes|no>``
        如果 ``yes`` ，只对标记为隔行的帧进行去交错处理（默认： no）
    ``hqscaling=<0-9>``
        0
            使用默认的VDPAU缩放比例（默认）
        1-9
            应用高质量的VDPAU缩放（需要适格的硬件）

``d3d11vpp``
    Direct3D 11视频后处理。需要 D3D11 上下文，与硬件解码配合使用效果最佳。软件帧会自动上传到硬件进行处理。

    ``format``
        转换为选定的图像格式，如 nv12、p010 等（默认：不变更）。可使用 ``--vf=d3d11vpp=format=help`` 查询格式名称。请注意，仅支持有限的子集，实际支持情况取决于您的硬件。通常情况下，除非某些处理只能使用特定格式，否则不应更改，在这种情况下，可以在此处选择特定格式。
    ``deint=<yes|no>``
        是否启用去隔行扫描（默认： no）
    ``scale``
        视频帧的缩放系数（默认： 1.0）
    ``scaling-mode=<standard,intel,nvidia>``
        选择要使用的缩放模式。请注意，这只会启用相应的处理扩展；实际是否有效取决于您的硬件和 GPU 驱动程序控制面板中的设置（默认： standard）

        standard
            由 d3d11vpp 实现决定的默认缩放模式。
        intel
            Intel Video Super Resolution
        nvidia
            NVIDIA RTX Super Resolution
    ``interlaced-only=<yes|no>``
        如果 ``yes`` ，只对标记为隔行的帧进行去隔行（默认： no）
    ``mode=<blend|bob|adaptive|mocomp|ivctc|none>``
        尝试选择一个具有给定处理能力的视频处理器。如果一个视频处理器支持多种能力，不清楚实际选择的是哪种算法。 ``none`` 始终回退。在大多数（但不是所有）硬件上，这个选项可能什么都不做，因为视频处理器通常支持所有模式或不支持任何模式。
    ``nvidia-true-hdr``
        启用 NVIDIA RTX Video HDR 后处理

``fingerprint=...``
    计算视频帧fingerprints并作为元数据提供。事实上，它目前几乎不配被称为 ``fingerprint`` ，因为它不计算“正确的”fingerprints，只计算微小的降级图像（但可用于计算图像哈希值或进行相似性匹配）。

    这个滤镜的主要目的是为了支持 ``skip-logo.lua`` 脚本。如果这个脚本被抛弃，或者mpv获得了加载用户定义的滤镜的方法（除了VapourSynth），这个滤镜将被移除。由于这个滤镜的“特殊”性质，它将被移除而没有任何警告。

    从滤镜中读取的预期方式是使用 ``vf-metadata`` （另参见 ``clear-on-query`` 滤镜参数）。该属性将返回一个按键/值成对的列表，如下所示：

    ::

        fp0.pts = 1.2345
        fp0.hex = 1234abcdef...bcde
        fp1.pts = 1.4567
        fp1.hex = abcdef1234...6789
        ...
        fpN.pts = ...
        fpN.hex = ...
        type = gray-hex-16x16

    每个 ``fp<N>`` 条目是针对一个帧。 ``pts`` 条目指定了帧的时间戳（在滤镜链中；在简单的情况下，这与显示的时间戳相同）。 ``hex`` 字段是十六进制编码的fingerprint，其大小和含义取决于 ``type`` 滤镜选项。 ``type`` 字段的值与滤镜创建时的选项相同。

    这将返回自上次查询该属性以来被过滤的帧。如果 ``clear-on-query=no`` 被设置，查询不会重置帧的列表。在这两种情况下，最多返回10个帧。如果有更多的帧，最旧的帧会被丢弃。帧是按过滤顺序返回的。

    （因为 ``vf-metadata`` 机制的内部结构很糟糕，所以不会返回每帧细节的结构化列表。返回的格式可能会在将来改变）

    这个滤镜为了速度和利益而使用zimg。然而，在一些情况下，它将回退到libswscale：较小的像素格式，不对齐的数据指针或stride，或者如果zimg由于未知的原因不能初始化。在这些情况下，滤镜将使用更多的CPU。另外，它还会输出不同的fingerprints，因为libswscale不能执行我们通常要求zimg提供的全范围扩展。因此，滤镜可能会更慢，并且在随机的情况下可能不能正确工作。

    ``type=...``
        要计算的fingerprint。可用的类型有：

        :gray-hex-8x8:      grayscale, 8 bit, 8x8 size
        :gray-hex-16x16:    grayscale, 8 bit, 16x16 size（默认）

        这两种类型都是简单地移除所有的颜色，降级图像的缩放，将所有的像素值串联成一个字节数组，并将该数组转换为十六进制字符串。

    ``clear-on-query=yes|no``
        如果该滤镜的 ``vf-metadata`` 属性被查询到，则清除帧fingerprints列表（默认： yes）。这需要用户的一些注意。某些类型的访问可能会多次查询该滤镜，从而导致帧丢失。

    ``print=yes|no``
        输出计算的fingerprints到终端（默认： no）。这主要是为了测试之类的。脚本应该使用 ``vf-metadata`` 来读取这个滤镜的信息。

``gpu=...``
    使用通常与 ``--vo=gpu`` 一起使用的Vulkan或OpenGL渲染器，将视频转换为RGB。对于OpenGL来说，这需要EGL实现的支持默认显示器上的离屏渲染（Mesa就是这种情况）。

    子选项：

    ``api=<type>``
        更改值 ``type`` 来选择渲染 API。 您还可以通过传递 ``help`` 获取已编译后端的完整列表。

        egl
            EGL （如果可用即默认）
        vulkan
            Vulkan

    ``w=<pixels>``, ``h=<pixels>``
        输出的尺寸，单位是像素（默认： 0）。如果不是正数，这将使用第一个过滤后的输入帧的大小

    .. warning::

        这是高度实验性的。性能糟糕，而且它首先不会在任何地方工作。有些功能不被支持。

    .. warning::

        这不做OSD渲染。如果你看到OSD，那么它已经被视频输出驱动的后端渲染了（如果可能的话，字幕是由 ``gpu`` 滤镜渲染的）。

    .. warning::

        如果你在编码模式下使用这个，请记住，编码模式将在软件中使用设置的软件缩放器将RGB滤镜的输出转换为yuv420p。使用 ``zimg`` 可能会改善这一点，但无论如何，这可能会违背你使用这个滤镜的目的。

    .. warning::

        不要和 ``--vo=gpu`` 一起使用。它将应用两次过滤，因为大多数 ``--vo=gpu`` 选项是无条件应用于 ``gpu`` 滤镜的。mpv中没有机制来阻止这种情况。
