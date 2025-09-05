# 音视频滤镜

_ver.20231101_

> **该系列文档已经停止更新** 详见： [中止维护非官方系列文档](https://github.com/hooke007/mpv_PlayKit/issues/573)

## 序

本文是 [mpv进阶的小节4](https://hooke007.github.io/unofficial/mpv_start.html#id15) & [《快捷键自定义与控制台》](https://hooke007.github.io/unofficial/mpv_input.html) 的拓展内容。

关联官方手册部分 [Manual_filters](https://mpv.io/manual/master/#video-filters)

本文只以视频滤镜为例进行讲解（音频滤镜的用法完全一致）  
_滤镜 也常被翻译作 过滤器_

默认快捷键 (<kbd>Shift</kbd> + ) <kbd>i</kbd> 的第一页下方显示已挂载的用户滤镜列表 `Filters:` 。无挂载则不显示该条目  
🔺 尽量使用软解或带复制的硬解（即 `--hwdec=no` 或 `--hwdec=auto-copy` ），大多数滤镜无法在原生硬解（即 `--hwdec=yes` ）下工作

本文偏重写法而不是实际用途，推荐熟悉语法后再查看 [《实用向的滤镜》](https://github.com/hooke007/mpv_PlayKit/discussions/120) 中的诸多案例。

## 1.语法简述

通常可以通过 `--vf` 选项使用视频滤镜  
滤镜存在列表管理的性质，因此有不同的后缀可搭配 ——

| 后缀   | 含义 |
| :----- | :----- |
| set    | 设置滤镜链（多个滤镜之间使用半角逗号 <kbd>,</kbd> 作为分隔符） |
| append | 追加单个滤镜（在后方） |
| add    | 追加单个或多个滤镜（在后方） |
| pre    | 追加单个或多个滤镜（在前方） |
| clr    | 移除所有滤镜 |
| remove | 移除指定的滤镜 |
| toggle | 追加指定的滤镜（在后方），但如果已经存在则移除该滤镜 |
| help   | 仅支持在终端使用，用于输出该滤镜的更多信息 |

先不考虑后缀，插入滤镜的语法为：

- 挂载某个滤镜（最简最基础） `vf=滤镜名`
- 挂载某个滤镜时对其中的子参数进行指定 `vf=滤镜名=子参数1:子参数2`
- 挂载多个滤镜的最简方式 `vf=滤镜1,滤镜2`
- 挂载某个滤镜时手动打上 **标签** `vf=@标签名:!滤镜名`

🔺 标签的用途之一是便于管理，例如手动插入一个复杂的滤镜时 `vf=@标签1:滤镜1=子参数1:子参数2:子参数3` ，移除它只需要 `vf-del=@标签1` 即可。

### 1.1.mpv.conf

在主设置文件中使用时通常是为了伴随mpv启动时自动应用某些滤镜，例如：
```ini
vf=vflip,hflip   # 垂直翻转 → 水平翻转
```

如果你的滤镜链比较复杂，推荐拆开写（带append后缀的选项不会相互覆盖）：
```ini
vf=vflip
vf-append=hflip
```

或者：
```ini
vf-append=vflip
vf-append=hflip
```

可能有面对不同的分辨率进行自动处理的需要，可以在profile中操作，此处只简单举例，实际应用时自行举一反三：
```ini
[4k_fast]
profile-cond=height>2000 and width>3000
profile-restore=copy
vf-clr
```

### 1.2.input.conf & 控制台

滤镜在快捷键与控制台中有独特的语法，简单讲就是参考上方的表格中的后缀，但移除连接符 `-` 且 `vf` 提前，示例：
```ini
a   vf set vflip,hflip
s   vf append vflip
d   vf add vflip,hflip
f   vf pre vflip,hflip
g   vf clr ""
h   vf remove vflip
j   vf toggle vflip
```

🔺 根据input语法中的“操作属性”的用法， `vf set vflip,hflip` 亦等效 `set vf vflip,hflip`  
`vf clr ""` 的作用也可通过 `set vf ""` 来达成。

## 2.滤镜分类

mpv所能使用的滤镜大体分为两类 ——

mpv自己实现的滤镜：  
[format](https://mpv.io/manual/master/#video-filters-format) & [sub](https://mpv.io/manual/master/#video-filters-sub) & [vapoursynth](https://mpv.io/manual/master/#video-filters-vapoursynth) & [vavpp](https://mpv.io/manual/master/#video-filters-vavpp) & [vdpaupp](https://mpv.io/manual/master/#video-filters-vdpaupp) & [d3d11vpp](https://mpv.io/manual/master/#video-filters-d3d11vpp) & [fingerprint](https://mpv.io/manual/master/#video-filters-fingerprint) & [gpu](https://mpv.io/manual/master/#video-filters-gpu)

来自ffmpeg的滤镜：  
[lavfi](https://mpv.io/manual/master/#video-filters-lavfi)

根据版本、平台和编译选项的不同，你所能实际使用滤镜类型和个数并不恒定，可通过如下方式查看：  
定位到 **mpv.com** 所在目录，打开 powershell 执行以下命令查看视频滤镜的综合信息 ——
```powershell
./mpv --vf=help
```

```{image} _assets/mpv_filters-terminal_01.jpg
:alt: stats_01
:width: 600 px
:align: center
```

🔺 `Available libavfilter filters:` 此行往下列出的即“来自ffmpeg的滤镜”  
ffmpeg滤镜有自己的 [文档](https://ffmpeg.org/ffmpeg-filters.html) ，它们并不在mpv的官方手册中记录

除开手册外，还可以通过如下指令查看滤镜的子参数
```powershell
./mpv --vf=滤镜名=help
```

### 2.1.原生滤镜

即“mpv自己实现的滤镜”

使用时注意它们的滤镜名（一般情况下）需要写完整（不能跳过中间的项），示例：
```ini
vf=format=fmt=brga   # 转换为brga格式输出
```

其中 `format=fmt` 为完整滤镜名（ `fmt` 不可省略），而 `brga` 为参数值。

### 2.2.非原生滤镜

即“来自ffmpeg的滤镜”

使用时可接受多种语法，因为原始语法较为复杂易于出错，参考如下示例（以下写法皆正确）：
```ini
vf=lavfi=[fps=60]
vf=lavfi="fps=60"
vf=lavfi=graph="fps=60"
vf=fps=60
```

出于简化原因，因此通常使用简化语法 `vf=fps=60` ；  
通过查阅 [文档](https://ffmpeg.org/ffmpeg-filters.html#fps-1) 可知该滤镜有如下子参数 `fps` `start_time` `round` `eof_action`  
由此体现了非原生滤镜的另外的语法特性是可以进一步精简，即 `vf=fps=60` 等效 `vf=fps=fps=60`

_我推荐尽可能把子参数名写上，如果不写子参数名，mpv会尝试自动打上标签。_

🔺 原生与非原生滤镜中可能存在重名的条目，例如通常当使用 `vf=format=...` 时首选mpv滤镜，最简的解决方案是显式指定为ffmpeg滤镜，即 `--vf=lavfi-format=...`

🔺 性能提速小技巧：  
当只使用多个非原生滤镜时，建议合并进一个filtergraph处理，示例 优先用 `vf="lavfi=[vflip,hflip]"` 而不是 `vf=vflip,hflip`

#### 2.2.1.字符串处理

非原生滤镜中的很多滤镜支持引入外部文件参与处理，例如 `lut3d` [文档](https://ffmpeg.org/ffmpeg-filters.html#lut3d-1)

假设已下载 `xxx.cube` 文件到路径 `D:/luts test/`  
🔺 非原生滤镜不支持诸如 `~~/` 之类的相对路径

如果只在 mpv.conf 中使用，十分简单
```ini
vf=lut3d=file="D:/luts test/pinkgirl.cube":interp=trilinear
```

但是若用在 input.conf 中，存在语法上的暗病，需要处理其中的特殊字符
```ini
Ctrl+l   vf toggle "lut3d=file=\"D:/luts test/pinkgirl.cube\":interp=trilinear"
```

或者简单粗暴的使用 [自定义引用](https://mpv.io/manual/master/#flat-command-syntax)
```ini
Ctrl+l vf toggle ``lut3d=file="D:/luts test/pinkgirl.cube":interp=trilinear``
```
