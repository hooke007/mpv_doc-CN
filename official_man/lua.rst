LUA SCRIPTING
=============

已精简全部偏开发类的内容（仅保留部分的面向一般用户类的内容），完整内容见 https://mpv.io/manual/master/#lua-scripting

mp.options functions
--------------------

（x省x略x内x容x）

设置文件将保存在 mpv 用户文件夹下的 ``script-opts/identifier.conf`` 中。注释行可以 # 开头，杂散的空格不会被删除。布尔值将用 yes/no 表示。

设置文件示例::

    # 注释
    optionA=Hello World
    optionB=9999
    optionC=no


命令行选项从 ``--script-opts`` 参数中读取。为避免冲突，所有关键值都必须以 ``identifier-`` 为前缀。

命令行示例::

     --script-opts=myscript-optionA=TEST,myscript-optionB=0,myscript-optionC=yes
