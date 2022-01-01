VIDEO FILTERS
=============

视频过滤器允许你修改视频流和它的属性。本节描述的所有信息也适用于音频过滤器（一般使用前缀 ``--af`` 而不是 ``--vf`` ）。

确切的语法是：

``--vf=<filter1[=parameter1:parameter2:...],filter2,...>``
    设置一个视频过滤器链。这包括过滤器的名称，以及 ``=`` 后面的参数选项列表。参数由 ``:`` 分隔（不是 ``,`` ，因为那会开始一个新的过滤器条目）。

    在过滤器名称之前，可以用 ``@name:`` 指定一个标签，其中name是一个任意的用户给定的名称，用来标识该过滤器。只有当你想在运行时切换过滤器的时候才需要这样做。

    过滤器名称前的 ``!`` 表示该过滤器默认是禁用的。它将在过滤器创建时被跳过。这对运行时的过滤器切换也很有用。

    参见 ``vf`` 命令（和 ``toggle`` 子命令）的进一步解释和例子。

    一般的过滤器条目语法是：

        ``["@"<label-name>":"] ["!"] <filter-name> [ "=" <filter-parameter-list> ]``

    或者对于特殊的 "toggle" 语法（见 ``vf`` 命令）。

        ``"@"<label-name>``

    和 ``filter-parameter-list`` ：

        ``<filter-parameter> | <filter-parameter> "," <filter-parameter-list>``

    和 ``filter-parameter`` ：

        ``( <param-name> "=" <param-value> ) | <param-value>``

    ``param-value`` 可以进一步用 ``[`` / ``]`` 来引用，如果该值包含 ``,`` 或 ``=`` 等字符。这一点特别适用于 ``lavfi`` 过滤器，它使用与mpv（MPlayer历史上）非常相似的语法来指定过滤器及其参数。

过滤器可以在运行时被操作。你可以使用上面描述的 ``@`` 标签，结合 ``vf`` 命令（见 `COMMAND INTERFACE`_ ）来获得更多的控制。最初禁用的过滤器与 ``!`` 在这方面也很有用。

你也可以为每个过滤器设置默认值。默认值会在正常的过滤器参数之前应用。这个方法已经过时了，而且在 libavfilter bridge 上从来没有用过。

``--vf-defaults=<filter1[=parameter1:parameter2:...],filter2,...>``
    为每个过滤器设置默认值。(Deprecated。 ``--af-defaults`` 也已deprecated)。

.. note::

    要获得可用的视频过滤器的完整列表，见 ``--vf=help`` 和 https://ffmpeg.org/ffmpeg-filters.html

    另外，请记住，大多数实际的过滤器是通过 ``lavfi`` 包装器获得的，它可以让你访问libavfilter的大多数过滤器。这包括所有从MPlayer移植到libavfilter的过滤器。

    大多数内置过滤器在某些方面已经废弃了，除非它们只在mpv中可用（比如处理mpv特性的过滤器，或者只在mpv中实现）。

    如果一个过滤器不是内置的， ``lavfi-bridge`` 将被自动尝试。这个桥不支持帮助输出，也不在实际使用过滤器之前验证参数。尽管mpv的语法与libavfilter的相当相似，但它并不一样。(这意味着不是所有vf_lavfi的 ``graph`` 选项接受的东西都会被 ``--vf`` 接受)。

    你也可以在过滤器的名字前加上 ``lavfi-`` 来强制使用包装器。如果过滤器的名字与废弃的mpv内置过滤器相冲突，这很有帮助。例如， ``--vf=lavfi-scale=args`` 会使用libavfilter的 ``scale`` 过滤器，而不是mpv的deprecated的内置过滤器。

视频过滤器是在列表中管理的。有几个命令可以管理过滤器列表：

``--vf-append=filter``
    将作为参数的过滤器添加到过滤器列表中。

``--vf-add=filter``
    将作为参数的过滤器添加到过滤器列表中。(目前仍然可以传递多个过滤器，但已deprecated)。

``--vf-pre=filter``
    将作为参数的过滤器添加到过滤器列表中。(目前仍然可以传递多个过滤器，但已deprecated)。

``--vf-remove=filter``
    从列表中删除过滤器。过滤器可以按照添加的方式（过滤器名称和它的完整参数列表），或者通过标签（以 ``@`` 为前缀）给出。过滤器的匹配工作如下：如果任何一个被比较的过滤器有一个标签集，则只比较标签。如果没有一个过滤器有标签，则比较过滤器的名称、参数和参数顺序。(目前仍然可以传递多个过滤器，但已deprecated)。

``-vf-toggle=filter``
    如果给定的过滤器还没有出现，则将其添加到列表中；如果已经出现，则将其从列表中删除。过滤器的匹配工作与 ``--vf-remove`` 中描述的一样。

``--vf-del=filter``
    有点像 ``--vf-remove`` ，但也接受一个索引号。索引号从0开始，负数指向列表的末尾（-1是最后一个）。废弃了。

``--vf-clr``
    完全清空过滤器列表。

对于支持它的过滤器，你可以通过它们的名字访问参数。

``--vf=<filter>=help``
    输出某个特定过滤器的参数名称和参数值范围。

可用的mpv-only过滤器有：

``format=fmt=<value>:colormatrix=<value>:...``
    应用视频参数覆盖，可选择转换。默认情况下，这将覆盖视频的参数而不进行转换（除了 ``fmt`` 参数），但对于支持转换的参数，可以用 ``convert=yes`` 来进行适当的转换。

    ``<fmt>``
        图像格式名称，例如rgb15、bgr24、420p，等等。(默认： 不改变)。

        这个过滤器总是执行对给定格式的转换。

        .. note::

            对于可用的格式列表，使用 ``--vf=format=fmt=help``

    ``<convert=yes|no>``
        强制转换颜色参数（默认： no）。

        如果禁用（默认），可能进行的唯一转换是格式转换，如果 ``<fmt>`` 被设置。所有其他参数（如 ``<colormatrix>`` ）都是强制的，没有转换。这种模式通常在文件被错误地标记时很有用。

        如果启用了这个功能，如果有任何参数不匹配，就会使用 libswscale 或 zimg。如果mpv的zimg包装器支持输入/输出图像格式，并且使用了 ``--sws-allow-zimg=yes`` ，就会使用zimg。这两个库可能不支持所有种类的转换。这通常会导致无声的错误转换。zimg在许多情况下有更好的机会正确执行转换。

        在这两种情况下，颜色参数都是在图像格式转换的输出阶段设置的（如果 ``fmt`` 被设置）。不同的是，在 ``convert=no`` 时，颜色参数不会传递给转换器。

        如果输入和输出的视频参数相同，转换总是被跳过。

        .. admonition:: 示例

            ``mpv test.mkv --vf=format:colormatrix=ycgco``
                结果是不正确的颜色（如果test.mkv被正确标记）。

            ``mpv test.mkv --vf=format:colormatrix=ycgco:convert=yes --sws-allow-zimg``
                结果是真正转换为 ``ycgco`` ，假设渲染器支持它（ ``--vo=gpu``  通常支持）。你可以添加 ``--vo=xv`` 来强制要求一个绝对不支持它的VO，它应该显示不正确的颜色作为确认。

                使用 ``--sws-allow-zimg=no`` （或者在构建时禁用zimg）将使用libswscale，它在编写时不能进行这种转换。

    ``<colormatrix>``
        控制播放视频时YUV到RGB颜色空间的转换。有各种标准。通常情况下，标清视频应使用BT.601，高清视频应使用BT.709。(已默认处理) 使用不正确的颜色空间会导致颜色的饱和度略低或过高，并出现偏移。

        这些选项并不总是被支持。不同的视频输出提供不同程度的支持。 ``gpu`` 和 ``vdpau`` 视频输出驱动通常提供完全支持。 ``xv`` 输出可以设置颜色空间，如果系统视频驱动支持的话，但不支持输入和输出电平。 ``scale`` 视频过滤器可以配置色彩空间和输入电平，但只有在输出格式为RGB的情况下（如果视频输出驱动程序支持RGB输出，你可以用 ``-vf scale,format=rgba`` 强制实现）。

        如果这个选项被设置为 ``auto`` （这是默认的），视频的颜色空间标志将被使用。如果该标志没有设置，颜色空间将被自动选择。这是通过一个简单的启发式方法来完成的，它试图区分标清和高清视频。如果视频大于1279x576像素，将使用BT.709（高清）；否则将选择BT.601（标清）。

        可用的色彩空间有：

        :auto:          自动选择（默认）。
        :bt.601:        ITU-R BT.601 (SD)
        :bt.709:        ITU-R BT.709 (HD)
        :bt.2020-ncl:   ITU-R BT.2020 non-constant luminance system
        :bt.2020-cl:    ITU-R BT.2020 constant luminance system
        :smpte-240m:    SMPTE-240M

    ``<colorlevels>``
        用于YUV到RGB转换的YUV色阶。这个选项只有在播放不遵循标准色阶或被标记为错误的破碎文件时才需要。如果视频没有指定它的颜色范围，则假定它是有限范围。

        与 ``<colormatrix>`` 的限制相同。

        可用的颜色范围是：

        :auto:      自动选择（通常是有限范围）（默认）
        :limited:   有限的范围（16-235的luma，16-240的chroma）
        :full:      全范围(luma和chroma都为0-255)

    ``<primaries>``
        源文件被编码的RGB原色。通常这应该在文件头中设置，但是当播放破损或错误的文件时，可以用它来覆盖这个设置。

        这个选项只影响执行色彩管理的视频输出驱动，例如， ``gpu`` 设置了 ``target-prim`` 或 ``icc-profile`` 子选项。

        如果这个选项被设置为 ``auto`` （这是默认的），视频的底层标志将被使用。如果该标志没有设置，将自动选择颜色空间，使用以下启发式方法。如果 ``<colormatrix>`` 被设置或确定为BT.2020或BT.709，就会使用相应的基色。否则，如果视频高度正好是576（PAL），则使用BT.601-625。如果正好是480或486（NTSC），则使用BT.601-525。如果视频分辨率是其他的，则使用BT.709。

        可用的primaries是：

        :auto:         automatic selection (default)
        :bt.601-525:   ITU-R BT.601 (SD) 525-line systems (NTSC, SMPTE-C)
        :bt.601-625:   ITU-R BT.601 (SD) 625-line systems (PAL, SECAM)
        :bt.709:       ITU-R BT.709 (HD) (same primaries as sRGB)
        :bt.2020:      ITU-R BT.2020 (UHD)
        :apple:        Apple RGB
        :adobe:        Adobe RGB (1998)
        :prophoto:     ProPhoto RGB (ROMM)
        :cie1931:      CIE 1931 RGB
        :dci-p3:       DCI-P3 (Digital Cinema)
        :v-gamut:      Panasonic V-Gamut primaries

    ``<gamma>``
       源文件被编码的伽马函数。通常情况下，这应该在文件头中设置，但当播放破碎或错误的文件时，可以用它来覆盖设置。

       这个选项只影响执行色彩管理的视频输出驱动程序。

       如果这个选项被设置为 ``auto`` （这是默认值），那么对于YCbCr内容，伽玛将被设置为BT.1886，对于RGB内容，将被设置为sRGB，对于XYZ内容，将被设置为Linear。

       可用的伽玛功能：

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
        视频文件的参考峰值照度，相对于信号的参考白电平。这对HDR来说很重要，但也可以用色调映射SDR内容来模拟不同的曝光。通常从MaxCLL或母版元数据等标签中推断出来。

        默认的0.0将默认为源的额定峰值亮度。

    ``<light>``
        场景的光线类型。这主要是根据伽马函数正确推断出来的，但在查看原始摄像机镜头（例如V-Log）时，覆盖这一点可能很有用，因为它通常是场景参考的，而不是显示参考的。

        可用的light类型：

       :auto:         自动选择（默认）
       :display:      Display-referred light (most content)
       :hlg:          Scene-referred using the HLG OOTF (e.g. HLG content)
       :709-1886:     Scene-referred using the BT709+BT1886 interaction
       :gamma1.2:     Scene-referred using a pure power OOTF (gamma=1.2)

    ``<stereo-in>``
        设置视频被假定为编码的立体声模式。使用 ``--vf=format:stereo-in=help`` 来列出所有可用模式。检查 ``stereo3d`` 过滤器文档，看看这些名字的含义。

    ``<stereo-out>``
        设置视频显示的立体声模式。取值与 ``stereo-in`` 选项相同。

    ``<rotate>``
        设置视频的旋转度，假定是以度数进行编码。特殊值 ``-1`` 使用输入格式。

    ``<w>``, ``<h>``
        如果不是0，执行转换到给定的尺寸。如果没有设置 ``convert=yes`` ，则忽略。

    ``<dw>``, ``<dh>``
        设置显示尺寸。请注意，设置显示尺寸，使视频在两个方向上都被缩放，而不仅仅是改变宽高比，这是一个实现细节，以后可能会改变。

    ``<dar>``
        设置视频帧的显示长宽比。这是一个浮点数，但也可以传递诸如 ``[16:9]`` 之类的值（ ``[...]`` 用于引号，以防止选项解析器解释 ``:`` 字符）。

    ``<force-scaler=auto|zimg|sws>``
        如果适用的话，强制一个特定的缩放器后端。这是一个调试选项，随时可能消失。

    ``<alpha=auto|straight|premul>``
        设置视频使用的alpha种类。如果图像格式没有alpha通道，则未定义效果（可能被忽略或导致错误，取决于mpv内部如何发展）。设置这个可能会或不会导致下游的图像处理以不同的方式处理阿尔法，这取决于支持情况。libswscale和其他FFmpeg组件会完全忽略这一点。

``lavfi=graph[:sws-flags[:o=opts]]``
    使用FFmpeg的libavfilter过滤视频。

    ``<graph>``
        libavfilter的图形字符串。该过滤器必须有一个视频输入pad和一个视频输出pad

        语法和可用的过滤器见 `<https://ffmpeg.org/ffmpeg-filters.html>`_ 

        .. warning::

            如果你想用这个选项使用完整的过滤器语法，你必须引用过滤器graph，以防止mpv的语法和过滤器图的语法发生冲突。为了防止引号和转义的混乱，如果你知道你想从输入文件中使用哪个视频轨道，可以考虑使用 ``--lavfi-complex`` 。(反正几乎所有的视频文件都只有一个视频轨道)。

        .. admonition:: 示例

            ``--vf=lavfi=[gradfun=20:30,vflip]``
                ``gradfun`` 过滤器有无意义的参数，接着是 ``vflip`` 过滤器。(这展示了libavfilter如何接受一个graph，而不仅仅是一个过滤器)。过滤graph的字符串是用 ``[`` 和 ``]`` 引用的。这不需要在某些shell（如bash）中使用额外的引号或转义，而其他shell（如zsh）则需要在选项字符串周围加上 ``"`` 引用。

            ``'--vf=lavfi="gradfun=20:30,vflip"'``
                和前面一样，但使用的是所有shell都安全的引号。外侧的 ``'`` 引用确保shell不会删除mpv所需的 ``"`` 引用。

            ``'--vf=lavfi=graph="gradfun=radius=30:strength=20,vflip"'``
                和之前一样，但对所有东西都使用命名参数。

    ``<sws-flags>``
        如果libavfilter插入了像素格式转换的过滤器，这个选项给出了应该传递给libswscale的标志。这个选项是数值型的，并采用 ``SWS_`` 标志的位数组合。

        参见 ``https://git.videolan.org/?p=ffmpeg.git;a=blob;f=libswscale/swscale.h``

    ``<o>``
        设置AVFilterGraph选项。这些应该由FFmpeg来记录。

        .. admonition:: 示例

            ``'--vf=lavfi=yadif:o="threads=2,thread_type=slice"'``
                强制执行一个特定的线程配置。

``sub=[=bottom-margin:top-margin]``
    将字幕渲染移到过滤器链中的一个任意点，或在视频过滤器中强制进行字幕渲染，而不是使用视频输出OSD支持。

    ``<bottom-margin>``
        在帧的底部添加一个黑带。SSA/ASS渲染器可以在那里放置字幕（使用 ``--sub-use-margins`` ）。
    ``<top-margin>``
        顶部的黑色带子用于放置字幕（使用 ``--sub-use-margins`` ）。

    .. admonition:: 示例

        ``--vf=sub,eq``
            将副标题的渲染移到eq过滤器之前。这将使字幕颜色和视频都受到视频均衡器设置的影响。

``vapoursynth=file:buffered-frames:concurrent-frames``
    加载一个VapourSynth过滤脚本。这是为流媒体处理准备的：mpv实际上提供了一个源过滤器，而不是使用本地VapourSynth视频源。mpv源将只在一个小的帧窗口内响应帧请求（这个窗口的大小由 ``buffered-frames`` 参数控制），超出的请求将返回错误。因此，你不能使用VapourSynth的全部功能，但你可以使用某些过滤器。

    .. warning::

        不要使用这个过滤器，除非你有VapourSynth的专家知识，并且知道如何修复mpv VapourSynth包装代码中的错误。

    如果你只是想播放VapourSynth生成的视频（即使用原生的VapourSynth视频源），最好使用 ``vspipe`` 和一个pipe或FIFO来把视频送入mpv。如果过滤脚本需要随机的帧访问（见 ``buffered-frames`` 参数），同样适用。

    ``file``
        脚本来源的文件名。目前，这总是一个Python脚本（VapourSynth惯例中的``.vpy'）。

        变量 ``video_in`` 被设置为mpv的视频源，希望脚本能从它那里读取视频。(否则，mpv将不解码视频，视频包队列将溢出，最终导致只有音频播放，或者更糟）。

        脚本创建的graph过滤也应该使用 ``_DurationNum`` 和 ``_DurationDen`` 帧属性来传递时间戳。

        关于mpv定义的脚本变量的完整列表，见选项列表的末尾。

        .. admonition:: 示例：

            ::

                import vapoursynth as vs
                core = vs.get_core()
                core.std.AddBorders(video_in, 10, 10, 20, 20).set_output()

        .. warning::

            该脚本将在每次寻路时被重新加载。这样做是为了在不连续的情况下正确重置过滤器。

    ``buffered-frames``
        在过滤器之前应该缓冲的最大解码视频帧数（默认： 4）。这指定了脚本在后退方向上可以请求的最大帧数。

        例如，如果 ``buffered-frames=5`` ，脚本刚刚请求了第15帧，它仍然可以请求第10帧，但第9帧已经不可用。如果它请求30帧，mpv将再解码15帧，而只保留25-30帧。

        这个缓冲区存在的唯一原因是为了满足VapourSynth过滤器的随机访问请求。

        VapourSynth API有一个 ``getFrameAsync`` 函数，它需要一个绝对的帧数。源过滤器必须对所有的请求作出回应。例如，一个源过滤器可以请求2432帧，然后是3帧。源过滤器通常通过预先索引整个文件来实现这一点。

        另一方面，mpv是面向流的，不允许过滤器进行搜索。(而且允许这样做是没有意义的，因为这样会破坏性能)。过滤器在播放过程中按顺序获得帧，不能不按顺序请求它们。

        为了弥补这种不匹配，mpv允许过滤器在一个特定的窗口内访问帧。 ``buffered-frames`` 控制这个窗口的大小。大多数VapourSynth过滤器恰好与此配合，因为mpv请求的帧是依次增加的，而大多数过滤器只需要与请求的帧 "接近" 的帧。

        如果过滤器请求的帧数比缓冲的最高帧数高，新的帧将被解码，直到达到请求的帧数。过多的帧将以先进先出的方式被刷掉（这个缓冲区里最多只有 ``buffered-frames`` ）。

        如果过滤器请求的帧数比缓冲区内最低的帧数要低，那么这个请求就不能被满足，并且会向过滤器返回一个错误。这种错误不应该发生在一个 "正确的" VapourSynth环境中。具体会发生什么，取决于所涉及的过滤器。

        增加这个缓冲区不会提高性能。相反，它会浪费内存，并减慢搜索速度（当需要一次性解码足够多的帧来填充缓冲区时）。它只是为了防止上一段所述的错误。

        一个过滤器需要多少帧取决于过滤器的实现细节，mpv没有办法知道。一个缩放滤波器可能只需要1帧，一个插值滤波器可能需要少量的帧，而 ``Reverse`` 滤波器将需要无限多的帧。

        如果你想在VapourSynth的能力范围内可靠地运行，请使用 ``vspipe``

        缓冲帧的实际数量也取决于 ``concurrent-frames`` 选项的值。目前，两个选项的值相乘，得到最终的缓冲区大小。

    ``concurrent-frames``
        应该平行请求的帧的数量。并发的程度取决于过滤器和mpv解码视频的速度，以提供给过滤器。这个值可能应该与你机器上的核心数量成正比。大多数时候，使其高于核心数实际上会使其变慢。

        技术上来说，mpv将循环调用VapourSynth的 ``getFrameAsync`` 函数，直到有 ``concurrent-frames`` 帧还没有被过滤器返回。这也是假设mpv过滤器链的其他部分能够快速读取 ``vapoursynth`` 过滤器的输出。(例如，如果你暂停播放器，过滤将很快停止，因为过滤后的帧在队列中等待）。

        实际的并发性取决于许多其他因素。

        默认情况下，这使用特殊值 ``auto`` ，它将选项设置为检测到的逻辑CPU核的数量。

    以下 ``.vpy`` 脚本变量是由mpv定义的。

    ``video_in``
        作为vapoursynth片段的mpv视频源。注意，这有一个不正确的（非常高的）长度设置，这使许多过滤器感到困惑。这是必要的，因为真正的帧数是未知的。你可以在剪辑上使用 ``Trim`` 过滤器来减少长度。

    ``video_in_dw``, ``video_in_dh``
        视频的显示尺寸。如果视频不使用方形像素，可以与视频尺寸不同(如DVD)。

    ``container_fps``
        由文件头报告的FPS值。这个值可能是错误的或完全坏的（如0或NaN）。即使这个值是正确的，如果另一个过滤器改变了真正的FPS（通过丢弃或插入帧），这个变量的值将没有用。注意 ``--fps`` 命令行选项会覆盖这个值。

        对一些坚持要有FPS的过滤器很有用。

    ``display_fps``
        当前显示器的刷新率。注意，这个值可以是0。

``vavpp``
    VA-API视频后期处理。要求系统支持VA-API，即只支持Linux/BSD。只与 ``--vo=vaapi`` 和 ``--vo=gpu`` 一起工作。目前是去交错。如果要求去交错（使用 ``d`` 键，默认映射到 ``cycle deinterlace`` 命令，或 ``--deinterlace`` 选项），这个过滤器会自动插入。

    ``deint=<method>``
        选择去交错的算法。

        no
            不执行去隔行扫描。
        auto
             选择最佳质量的去隔行算法（默认）。这按照文件中的选项顺序进行， ``motion-compensated`` 被认为是最佳质量。
        first-field
            只显示第一个字段。
        bob
            bob去隔行扫描。
        weave, motion-adaptive, motion-compensated
            高级去隔行扫描算法。这些是否真的有效，取决于GPU硬件、GPU驱动、驱动错误和mpv错误。

    ``<interlaced-only>``
        :no:  对所有帧进行隔行扫描（默认）。
        :yes: 只对标记为交错的帧进行去交错处理。

    ``reversal-bug=<yes|no>``
        :no:  使用旧版Mesa驱动所解释的API。虽然这种解释更明显、更直观，但显然是错误的，而且不被英特尔驱动开发者所认同。
        :yes: 使用英特尔对表面前向和后向引用的解释（默认）。这就是英特尔驱动和新的Mesa驱动所期望的。只对高级去隔行扫描算法重要。

``vdpaupp``
    VDPAU视频后处理。只对 ``--vo=vdpau`` 和 ``--vo=gpu`` 起作用。如果要求去隔行扫描(使用 ``d`` 键，默认映射到 ``cycle deinterlace`` 命令，或 ``--deinterlace`` 选项)，这个过滤器会自动插入。当启用去交错时，如果使用了 ``vdpau`` VO，并且使用了 ``gpu`` 并且至少激活了一次硬件解码（例如加载了vdpau），它总是比软件去交错过滤器更受欢迎。

    ``sharpen=<-1-1>``
        对于正值，对视频应用锐化算法，对于负值应用模糊算法（默认： 0）。
    ``denoise=<0-1>``
        对视频应用降噪算法（默认： 0；不降噪）。
    ``deint=<yes|no>``
        是否启用去隔行扫描（默认： no）。如果启用，它将使用 ``deint-mode`` 选择的模式。
    ``deint-mode=<first-field|bob|temporal|temporal-spatial>``
        选择去隔行扫描模式（默认： temporal）。

        注意，目前有一种机制允许 ``vdpau`` VO改变自动插入的 ``vdpaupp`` 过滤器的 ``deint-mode`` 。为了避免混淆，建议不要使用与过滤有关的 ``--vo=vdpau`` 子选项。

        first-field
            只显示第一个字段。
        bob
            Bob去隔行扫描。
        temporal
            运动适应性的时间性去交错。可能导致慢速视频硬件和/或高分辨率下的A/V解同步。
        temporal-spatial
            运动自适应的时间性去交错，边缘引导的空间插值。需要快速视频硬件。
    ``chroma-deint``
        使时间性去交错器同时运行在luma和chroma上（默认）。使用no-chroma-deint只使用luma并加速高级去隔行。对慢速视频存储器很有用。
    ``pullup``
        尝试应用反胶，需要运动自适应的时间性去交错。
    ``interlaced-only=<yes|no>``
        如果 ``yes`` ，只对标记为隔行的帧进行去交错处理（默认： no）。
    ``hqscaling=<0-9>``
        0
            使用默认的VDPAU缩放比例（默认）。
        1-9
            应用高质量的VDPAU缩放（需要有能力的硬件）。

``d3d11vpp``
    Direct3D 11视频后期处理。目前需要D3D11硬件解码才能使用。

    ``deint=<yes|no>``
        是否启用去隔行扫描(默认： no)。
    ``interlaced-only=<yes|no>``
        如果 ``yes`` ，只对标记为隔行扫描的帧进行隔行扫描（默认： no）。
    ``mode=<blend|bob|adaptive|mocomp|ivctc|none>``
        试图选择一个具有给定处理能力的视频处理器。如果一个视频处理器支持多种能力，不清楚实际选择的是哪种算法。 ``none`` 总是退缩。在大多数（如果不是所有）硬件上，这个选项可能什么都不做，因为视频处理器通常支持所有模式或不支持。

``fingerprint=...``
    计算视频帧指纹并作为元数据提供。事实上，它目前几乎不配被称为 ``fingerprint`` ，因为它不计算 "proper" 指纹，只计算微小的降级图像（但可用于计算图像哈希值或进行相似性匹配）。

    这个过滤器的主要目的是为了支持 ``skip-logo.lua`` 脚本。如果这个脚本被放弃，或者mpv获得了加载用户定义的过滤器的方法（除了VapourSynth），这个过滤器将被删除。由于这个过滤器的 "特殊" 性质，它将被删除而没有任何警告。

    从过滤器中读取的预期方式是使用 ``vf-metadata`` （也见 ``clear-on-query`` 过滤器参数）。该属性将返回一个键/值对的列表，如下所示：

    ::

        fp0.pts = 1.2345
        fp0.hex = 1234abcdef...bcde
        fp1.pts = 1.4567
        fp1.hex = abcdef1234...6789
        ...
        fpN.pts = ...
        fpN.hex = ...
        type = gray-hex-16x16

    每个 ``fp<N>`` 条目是针对一个帧。 ``pts`` 条目指定了帧的时间戳（在过滤器链中；在简单的情况下，这与显示的时间戳相同）。 ``hex`` 字段是十六进制编码的指纹，其大小和含义取决于 ``type`` 过滤器选项。 ``type`` 字段的值与过滤器创建时的选项相同。

    这将返回自上次查询该属性以来被过滤的帧。如果 ``clear-on-query=no`` 被设置，查询不会重置框架的列表。在这两种情况下，最多返回10个框架。如果有更多的框架，最旧的框架会被丢弃。帧是按过滤顺序返回的。

    (因为 ``vf-metadata`` 机制的内部结构很糟糕，所以不会返回每帧细节的结构化列表）。返回的格式在将来可能会改变）。

    这个过滤器为了速度和利益而使用zimg。然而，在一些情况下，它将退回到libswscale：较小的像素格式，不对齐的数据指针或stride，或者如果zimg由于未知的原因不能初始化。在这些情况下，过滤器将使用更多的CPU。另外，它还会输出不同的指纹，因为 libswscale 不能执行我们通常要求 zimg 提供的全范围扩展。因此，过滤器可能会更慢，并且在随机的情况下不能正确工作。

    ``type=...``
        要计算的指纹。可用的类型有：

        :gray-hex-8x8:      grayscale, 8 bit, 8x8 size
        :gray-hex-16x16:    grayscale, 8 bit, 16x16 size (默认)

        这两种类型都是简单地去除所有的颜色，降低图像的比例，将所有的像素值串联成一个字节数组，并将该数组转换为十六进制字符串。

    ``clear-on-query=yes|no``
        如果该过滤器的 ``vf-metadata`` 属性被查询到，则清除框架指纹列表（默认： yes）。这需要用户的一些注意。某些类型的访问可能会多次查询该过滤器，从而导致丢失帧。

    ``print=yes|no``
        打印计算的指纹到终端（默认： no）。这主要是为了测试之类的。脚本应该使用 ``vf-metadata`` 来读取这个过滤器的信息。

``gpu=...``
    使用通常与 ``--vo=gpu`` 一起使用的OpenGL渲染器将视频转换为RGB。这需要EGL实现支持默认显示器上的离屏渲染。(Mesa就是这种情况)。

    子选项：

    ``w=<pixels>``, ``h=<pixels>``
        输出的尺寸，单位是像素（默认： 0）。如果不是正数，这将使用第一个过滤后的输入帧的大小。

    .. warning::

        这是高度实验性的。性能不好，而且它首先不会在任何地方工作。有些功能不被支持。

    .. warning::

        这不是做OSD渲染的。如果你看到OSD，那么它已经被VO后端渲染了。(如果可能的话，字幕是由 ``gpu`` 过滤器渲染的）。

    .. warning::

        如果你在编码模式下使用这个，请记住，编码模式将在软件中使用配置的软件缩放器将RGB过滤器的输出转换为yuv420p。使用 ``zimg`` 可能会改善这一点，但无论如何，这可能会违背你使用这个过滤器的目的。

    .. warning::

        不要和 ``--vo=gpu`` 一起使用。它将应用两次过滤，因为大多数 ``--vo=gpu`` 选项是无条件应用于 ``gpu`` 过滤器的。mpv中没有机制来防止这种情况。

