# 快捷键自定义与控制台

_ver.20221124_

## 序

阅读本文前默认已基本熟悉 mpv.conf 内各参数的用途及含义。  
本文是 [mpv进阶的小节2](https://hooke007.github.io/unofficial/mpv_start.html#id8) 的拓展内容。

关联官方手册部分 [Manual_inputconf](https://mpv.io/manual/master/#input-conf)

## 前文要点

- 设置文件夹内的 **input.conf** 存储用户自行设定的快捷键。通常mpv读取该文件并覆盖内建的初始快捷键方案中的重名项。  
如果没有该文件则默认使用 [内建的原始快捷键预设](https://github.com/mpv-player/mpv/blob/master/etc/input.conf)  
（在 **mpv.conf** 中使用参数 `--input-conf=<filename>` 可指定使用另外的文件取代 **input.conf** ）

- 在 **input.conf** 中使用参数 `input-builtin-bindings=no` 或 `input-default-bindings=no` 可屏蔽全部内建的原始快捷键预设（后者能进一步屏蔽外置脚本内的静态若绑定预设）。

- mpv-lazy版中可供参考的大量[示例](https://github.com/hooke007/MPV_lazy/blob/main/portable_config/input.conf)

## 语法简述

```ini
<键位绑定（按键名）>   <具体命令>   # 支持行后注释
```

`键位绑定` 前添加注释符 `#` 即屏蔽该行内容  
若存在多行相同的 `按键名` ，则后方的行覆盖之前的行，成为mpv读取的实际内容。

### 键位绑定

1. 普通按键和一般功能键可单独作为键位绑定

<kbd>a</kbd> <kbd>1</kbd> <kbd>F1</kbd> <kbd>SPACE</kbd>  
示例：
```ini
SPACE   cycle pause   # 切换暂停
```

🔺 编辑键值名时，输入符号时应注意中文输入法的全半角（即用英文字符）

2. 以下按键作为前缀构成的组合键

<kbd>Shift</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd>  
示例：
```ini
Ctrl+a   set aid no   # 禁用音轨
```

🔺 但是这几个键自身不可以作为键位触发

3. 大写和上档

不支持 `Shift+字母/数字` 这种写法，解决方案是 ——

示例1：
```ini
A   cycle mute   # 切换静音
```
在mpv中对应的操作即 <kbd>Shift</kbd> + <kbd>a</kbd>  
当然你也可以在激活 <kbd>CAPS</kbd>（大写锁定键） 的情况下直接按 <kbd>a</kbd> 触发

示例2：
```ini
!   cycle mute   # 切换静音
```
如果你使用的是美式键盘布局，则实际对应的是 <kbd>Shift</kbd> + <kbd>1</kbd>

🔺 由于 注释符 与 按键 <kbd>#</kbd> 重名，所以如果你要绑定这个键位，用 `SHARP` 作为按键名

4. 连键

连键不是双击，两次按键之间没有限制触发时间间隔。

示例1：
```ini
q-q   quit     # 退出
q     ignore
```
即按两次 <kbd>q</kbd> 退出mpv  
此处屏蔽 `q` 的目的是防止触发上一行时先触发该键的动作

示例2：
```ini
q-a-z   quit     # 退出
q       ignore
q-a     ignore
```
连键不仅支持不同按键，更支持串联多个不同按键  
同上，安全起见，屏蔽中间键的动作

### 具体命令

大体分为两类 ——

1. 属性相关

在mpv运行时可以通过操作属性，来达成动态修改mpv.conf中的选项值的效果。  
mpv中可用的属性列表参见 [此处](https://mpv.io/manual/master/#property-list)  
_部分 属性名 与 mpv.conf 用的 选项名 重名，未全部列出_

设置某个属性为某个值，用 `set <属性名> <值>`  
增减某个属性的数值，用 `add <属性名> <数值>`  
乘以某个属性的数值，用 `multiply <属性名> <数值>`  
使某属性在可变的多个值中切换，用 `cycle <属性名>`  
使某属性在你指定的多个值中切换，用 `cycle-values <属性名> <必要值1> <必要值2> [可选值3] ...`  

以上用途的汇总示例：
```ini
w   set volume 100                        # 设定音量为100
e   add saturation 1                      # 增加饱和度 1
r   add hue -2                            # 减少色相 2
t   multiply speed 1/1.1                  # 减速
y   multiply speed 2                      # 倍速
u   cycle fullscreen                      # 切换 全屏
i   cycle-values hwdec yes no auto-copy   # 切换解码模式
```

🔺 并非所有属性都可以在运行时变更

1.1. 滤镜与着色器列表管理

虽然依然可用通过 `set <属性名> <值>` 的方式设置，但是涉及列表的部分属性提供了更灵活的细致操作 ——

- 滤镜相关的内容详见 （还没重写，先看[旧版](https://hooke007.github.io/mpv-lazy/mpv_lazy_d03)）

- 着色器相关的内容详见 [此处](https://hooke007.github.io/unofficial/mpv_shaders.html#id7)

2. 直接命令

即指不触碰属性，直接执行动作，示例：
```ini
s   stop   # 停止
```

其中 `ignore` 为特殊命令，用来屏蔽键位的操作（ 小节 “键位绑定” 部分已有示例）

更多可用直接命令参见 [此处](https://mpv.io/manual/master/#list-of-input-commands)

2.1. 脚本指令

mpv的脚本可能提供了额外定义的名义可供用户使用，这通常应由开发者进行详细说明。  
涉及的命令为：  
`script-binding [可选脚本名]/<脚本命令名>`  
`script-message <脚本命令名>`  
`script-message-to <对象名> <脚本命令名>`

以内建脚本 **stats.lua** 为例：
```ini
I   script-binding stats/display-stats-toggle   # 开/关 常驻显示统计信息
i   script-binding display-stats-toggle
```

#### 静默与串联

大多数命令执行时会显示OSD信息，可以通过 `no-osd` 作为命令的前缀来禁止其显示。  
示例：
```ini
RIGHT   no-osd seek 5   # 前进 5 秒
```

一个键位可以执行多个命令，可以用 `;` （半角的分号）作为分隔标志  
示例：
```ini
RIGHT   seek 5 ; show-text "向前 5 秒"   # 前进 5 秒并显示OSD文本消息
```

## 辅助

- mpv的内建脚本 **stats.lua** 的第四页可显示已绑定的按键信息  
```{image} _assets/mpv_input-stats_01.webp
:alt: stats_01
:width: 600 px
:align: center
```

- 终端运行 `./mpv --input-keylist` 将列出所有可用的键值名

- 终端运行 `./mpv --input-test --force-window --idle` 将打开一个空mpv窗口便于测试实际键位对应的值  
（mpv-lazy提供了 [输入模式](https://github.com/hooke007/MPV_lazy/blob/main/installer/mpv-输入模式.bat) 便于更快启动）

## 控制台

mpv的内建脚本 **console.lua** 提供了控制台的功能。这是另一种在运行时动态修改“选项值”的解决方案。

默认为 <kbd>`</kbd> 打开控制台（注意观察画面左下角），打开后按 <kbd>ESC</kbd> 即可退出控制台。你可以在 **input.conf** 中重新绑定控制台的启用按键：
```ini
TAB   script-binding console/enable # 进入控制台
```

可在控制台中直接输入命令（它的语法等同 **input.conf** 中的 `<具体命令>` ），按 <kbd>ENTER</kbd> 立即执行。  
示例：
```ini
# 输入以下这行并执行，立即截屏
screenshot
```
