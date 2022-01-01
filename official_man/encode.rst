ENCODING
========

你可以使用这个工具将文件从一种格式/编码转换到另一种。

``--o=<filename>``
    启用编码模式并指定输出文件名。

``--of=<format>``
    指定输出格式（覆盖由 ``-o`` 指定的文件名扩展名的自动检测）。参见 ``--of=help`` ，以获得支持格式的完整列表。

``--ofopts=<options>``
    指定libavformat的输出格式选项。参见 ``--ofopts=help`` 以获取支持的选项的完整列表。

    这是一个 值/值列表 选项。详见 `List Options`_ 。

    ``--ofopts-add=<option>``
        将作为参数的选项添加到选项列表中。(目前仍可传递多个选项，deprecated)。

    ``--ofopts=""``
        完全清空选项列表。

``--oac=<codec>``
    指定输出的音频编解码器。参见 ``--oac=help`` 以获得支持的编解码器的完整列表。

``--oaoffset=<value>``
    通过在开始时添加/删除样本，将音频数据按给定的时间（以秒为单位）转移。deprecated。

``--oacopts=<options>``
    指定libavcodec的输出音频编解码器选项。参见 ``--oacopts=help`` 以获得支持选项的完整列表。

    .. admonition:: 示例

        "``--oac=libmp3lame --oacopts=b=128000``"
            选择128kbps的MP3编码。

    这是一个 值/值列表 选项。详见 `List Options`_ 。

    ``--oacopts-add=<option>``
        将作为参数的选项添加到选项列表中。（目前仍可传递多个选项，deprecated）。

    ``--oacopts=""``
        完全清空选项列表。

``--oafirst``
    强制音频流成为输出中的第一个流。默认情况下，顺序是未指定的。deprecated。

``--ovc=<codec>``
    指定输出的视频编解码器。参见 ``--ovc=help`` 获取支持的编解码器的完整列表。

``--ovoffset=<value>``
    通过移位pts值将视频数据移位到给定的时间（秒）。deprecated。

``--ovcopts=<options>``
    指定libavcodec的输出视频编解码器选项。参见 --ovcopts=help 获取支持选项的完整列表。

    .. admonition:: 示例

        ``"--ovc=mpeg4 --ovcopts=qscale=5"``
            为MPEG-4编码选择恒定的量化器刻度5。

        ``"--ovc=libx264 --ovcopts=crf=23"``
            为H.264编码选择VBR质量因子23。

    这是一个 值/值列表 选项。详见 `List Options`_ 。

    ``--ovcopts-add=<option>``
        将作为参数的选项添加到选项列表中。（目前仍可传递多个选项，deprecated）。

    ``--ovcopts=""``
        完全清空选项列表。

``--ovfirst``
    强制视频流成为输出中的第一个流。默认情况下，顺序是未指定的。deprecated。

``--orawts``
    将输入pts复制到输出视频中（某些输出容器格式不支持，如AVI）。在这种模式下，不连续点不被固定，所有的点都是原样通过。在这种模式下，千万不要向后寻找或使用多个输入文件！

``--no-ocopy-metadata``
    在编码时，关闭从输入文件复制元数据到输出文件的功能（默认： yes）。

``--oset-metadata=<metadata-tag[,metadata-tag,...]>``
    指定要包括在输出文件中的元数据。支持的值在不同的输出格式中有所不同。例如，Matroska（MKV）和FLAC允许几乎任意的键，而MP4和MP3的支持则比较有限。

    这是一个 值/值列表 选项。详见 `List Options`_ 。

    .. admonition:: 示例

        "``--oset-metadata=title="Output title",comment="Another tag"``"
            在输出文件中增加一个标题和一个注释。

``--oremove-metadata=<metadata-tag[,metadata-tag,...]>``
    指定从输入文件复制时要从输出文件中排除的元数据。

    这是一个字符串列表选项。详见 `List Options`_ 。

    .. admonition:: 示例

        "``--oremove-metadata=comment,genre``"
            排除将注释和流派标签复制到输出文件中。
