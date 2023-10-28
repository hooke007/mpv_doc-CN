编码/压制
=========

你可以使用这个工具将文件从一种格式/编码转换到另一种。

``--o=<filename>``
    启用编码模式并指定输出文件名。

``--of=<format>``
    指定输出格式（通过 ``-o`` 指定的文件扩展名覆盖自动检测）。参见 ``--of=help`` 以获取受支持格式的完整列表。

``--ofopts=<options>``
    指定libavformat的输出格式选项。参见 ``--ofopts=help`` 以获取受支持的选项的完整列表。

    这是一个按键/值列表 选项。详见 `列表选项`_

    ``--ofopts-add=<option>``
        将作为参数给定的选项追加到选项列表中（目前仍可传递多个选项，但已过时）

    ``--ofopts=""``
        完全清空选项列表

``--oac=<codec>``
    指定输出的音频编码。参见 ``--oac=help`` 以获取受支持的编码的完整列表。

``--oacopts=<options>``
    指定libavcodec的输出音频编码选项。参见 ``--oacopts=help`` 以获取受支持的选项的完整列表。

    .. admonition:: 示例

        "``--oac=libmp3lame --oacopts=b=128000``"
            选择128kbps的MP3进行编码

    这是一个按键/值列表选项。详见 `列表选项`_

    ``--oacopts-add=<option>``
        将作为参数给定的选项追加到选项列表中（目前仍可传递多个选项，但已过时）

    ``--oacopts=""``
        完全清空选项列表

``--ovc=<codec>``
    指定输出的视频编码。参见 ``--ovc=help`` 以获取受支持的编码的完整列表。

``--ovcopts=<options>``
    指定libavcodec的输出视频编码选项。参见 --ovcopts=help 以获取受支持的选项的完整列表。

    .. admonition:: 示例

        ``"--ovc=mpeg4 --ovcopts=qscale=5"``
            为MPEG-4编码选择恒定的量化器缩放5

        ``"--ovc=libx264 --ovcopts=crf=23"``
            为H.264编码选择VBR质量系数23

    这是一个按键/值列表选项。详见 `列表选项`_

    ``--ovcopts-add=<option>``
        将作为参数给定的选项追加到选项列表中（目前仍可传递多个选项，但已过时）

    ``--ovcopts=""``
        完全清空选项列表

``--orawts``
    将输入pts复制到输出视频中（不受某些输出容器格式的支持，例如AVI）。在这种模式下，不连续点不被固定，所有的点都是被原样传递过去。在这种模式下，千万不要向前跳转或使用多个输入文件！

``--no-ocopy-metadata``
    在进行编码时，关闭从输入文件复制元数据到输出文件的功能（默认： yes）。

``--oset-metadata=<metadata-tag[,metadata-tag,...]>``
    指定要包括在输出文件中的元数据。支持的值在不同的输出格式中有所不同。例如，Matroska（MKV）和FLAC允许几乎任意的符号说明，而MP4和MP3的支持则比较有限。

    这是一个按键/值列表选项。详见 `列表选项`_

    .. admonition:: 示例

        "``--oset-metadata=title="Output title",comment="Another tag"``"
            在输出文件中增加一个标题和一个注释

``--oremove-metadata=<metadata-tag[,metadata-tag,...]>``
    指定从输入文件复制时要从输出文件中排除的元数据。

    这是一个字符串列表选项。详见 `列表选项`_

    .. admonition:: 示例

        "``--oremove-metadata=comment,genre``"
            排除将注释和流派标签复制到输出文件。
