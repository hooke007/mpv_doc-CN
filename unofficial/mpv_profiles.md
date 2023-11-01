# 配置预设

_ver.20231101_

## 序

阅读本文前默认已基本熟悉 mpv.conf 内各参数的用途及含义。

关联官方手册部分 [Manual_profiles](https://mpv.io/manual/master/#profiles)

"profile" 没找到完美的翻译来避免中文的语义歧义（在mpv-lazy中我习惯性将其称为“配置预设”），为了避免认知偏差，本文使用英文原文。

### 示例配置

首先，从如下的例子开始，逐步解析 profile ——

```ini
### mpv.conf 内容

vo=gpu
hwdec=yes
profile=high-quality
deband=no
keep-open=yes
profile=srt_style


[srt_style]
sub-scale-with-window=no
sub-font-size=58
sub-border-size=4


[playing_ontop]
profile-desc=播放时置顶
profile-cond=not pause
profile-restore=copy
ontop=yes
```

## 1.顺序逻辑

在一个主设置文件中，使用参数 `profile=xxx` 即插入某profile，而profile本身是一个参数集合（不会在启动时应用）  
依照整体逻辑，从上往下读取。对于一般选项，如果存在重名的则后者覆盖前者成为实际被应用的参数。  
其中 `profile=xxx` 是一个特殊选项，当它被读取时，会被解析为它的赋值对象中的实际参数集。

`[xxxxx]` 是一个profile的头部标志，两个profile之间 —— 即 `[srt_style]` 到 `[playing_ontop]` 所有中间行的参数都属于 `[srt_style]` 。  
一旦你在 mpv.conf 自己建立了profile，就不要把常驻参数（即启动时就应用的项）写在profile的后方，因为profile没有明确的结束标志，在上方示例中，任何写在最后的参数都会被mpv认定为属于 `[playing_ontop]`

`high-quality` 是mpv内建（自带）的一个profile（旧版mpv中是 `gpu-hq` ），它具体包含以下参数：
```ini
scale = ewa_lanczossharp
hdr-peak-percentile = 99.995
hdr-contrast-recovery = 0.30
deband=yes
```

P.S. mpv还有其它内建profile，详见 [《profiles_补充内容》](https://github.com/hooke007/MPV_lazy/discussions/42)

因此，上方示例实际被解析为如下常驻参数列表 ——
```ini
### 常驻参数
vo=gpu
hwdec=yes

scale = ewa_lanczossharp
hdr-peak-percentile = 99.995
hdr-contrast-recovery = 0.30
deband=yes

deband=no
keep-open=yes
sub-scale-with-window=no
sub-font-size=58
sub-border-size=4
```

P.S. 在此示例中，把 `deband=no` 放在 `profile=high-qualit` 之后，也是因为目的是要禁用去色带，否则如果顺序相反只会产生相反的结果。

## 2.分类

profile可大致分为 常规/普通profile 和 条件/自动profile  
简单概括特性即 条件profile 会根据内部设定的触发条件，满足情况时自动启用

区分的依据是内部的构成 ——

```ini
### 常规profile的结构
[ass_vsfilter_cmpt]                  # profile的名称，自定义
profile-desc=ass的vsfilter兼容测试   # [非必要参数] profile的描述，自定义
sub-ass-vsfilter-aspect-compat=no    # 此行往后填写要你要应用的参数，自定义
sub-ass-vsfilter-blur-compat=no
sub-ass-vsfilter-color-compat=no
```

```ini
### 条件profile的结构
[idle_border]                     # profile的名称，自定义
profile-desc=非空闲时使用无边框   # [非必要参数] profile的描述，自定义
profile-cond=not p.idle_active    # profile的触发判定条件
profile-restore=copy              # 不满足时的回退方式
border=no                         # 此行往后填写要你要应用的参数，自定义
```

### 2.1.条件profile的深入解释

### 2.1.1.cond

首先是有哪些触发条件即 `profile-cond` 可用，它被解释为Lua条件，即使你完全不了解这门语言，这里亦有示例带你快速入门使用。

判定的核心对象是 “属性” 即手册中的[属性列表](https://mpv.io/manual/master/#property-list)中列出的全部，  
一个安全的引用属性的方式是 `p["xxxx"]` ，这样就不用担心特殊符号导致的判定无效。

- 若只需满足一个属性，对应条件就这样写： `p["xxxx"]`
- 若只需满足一个属性的反面，对应条件就这样写： `not p["xxxx"]`
- 若需满足两个属性，对应条件就这样写： `p["xxxx"] and p["yyyy"]`
- 若需某个属性的等于某个具体值时触发，对应条件就这样写： `p["xxxx"]=="value"`
- 若需某个属性值（数字）大于等于某数值时触发（以音量为例），对应条件就这样写： `p["volume"]>=50`

P.S. 更多示例参见 [主仓库_profiles](https://github.com/hooke007/MPV_lazy/blob/main/portable_config/profiles.conf)

P.S. 常见的引用属性的方式是直接写属性名和 `p.xxxx` 的形式（参见前文的示范），这种方式适合名字简单无符号的属性，不用担心语法上的暗病。

### 2.1.2.restore

其次是profile触发后，不满足条件时的回退方式。

正如开头讲，profile被解析为具体一行行参数，因此准确讲profile并没有开启和关闭的概念。为了解决现实的需求，它以变通的方式解决了这个问题，即备份触发前的涉及的选项及其值，然后在条件不满足是还原备份的参数。

对应“回退方式”的即 `profile-cond` 它的常用可选值为 `default` 或 `copy`  
如果使用 `default` ，则没有“回退”处理。它的实用场景较少，因此常见的几乎都是使用 `copy`

## 3.非典型使用

### 3.1.旧版的自动profile

mpv遗留了一种旧版的 自动profile ，如下所示

```ini
### Legacy auto profiles的结构
[extension.mp4]                    # profile的名称，亦是profile的触发判定条件（回退方式类似 copy）
profile-desc=mp4扩展名文件的处理   # [非必要参数] profile的描述，自定义
hwdec=auto                         # 此行往后填写要你要应用的参数，自定义
```

它的功能有限，通常没有使用的必要而且可以转换为当前的 条件profile ，这在之前的 [《profiles_补充内容》](https://github.com/hooke007/MPV_lazy/discussions/42) 有记录。

### 3.2.profile嵌套

如图所示，注意书写顺序，确保后方的profile所调用的profile已被读取到。

```ini
[deband_base]
deband=yes
deband-iterations=2
deband-threshold=48

[deband_plus]
profile=deband_base
deband-range=10
deband-grain=24

[deband_auto]
profile-cond=fullscreen
profile-restore=copy
profile=deband_plus
```

🔺 注意：不要在 条件profile 里嵌套 条件profile

### 3.3.隔离profile

这也是我当前在 mpv-lazy 中的处理方式，避免开头提到的 常驻参数 误入profile的问题。  
实现方式是通过在mpv.conf中使用参数 `--include=xxxx.conf` 这样mpv就会在主设置文件读取完毕后，再读取该文件作为 mpv.conf 的补充内容，而我只在该文件内写profile，常驻参数只写在 mpv.conf 中。

P.S. 我以同样的方式隔离了脚本选项，参见 [《集中化管理mpv的脚本选项》](https://github.com/hooke007/MPV_lazy/discussions/126)

### 3.4.穿插常驻参数

如果你执意要在两个profile之间穿插 常驻参数 ，官方亦提供了一种解决方案，见下方示例 ——

```ini
### “常驻参数” 区
xxxx=xxxx
xxxx=xxxx
xxxx=xxxx

### “profile参数” 区
[profile_1]
aaaa=aaaa
aaaa=aaaa
aaaa=aaaa

# 使用名为 "default" 的profile即可让这部分的参数被归为 “常驻参数”
[default]
yyyy=yyyy
yyyy=yyyy
yyyy=yyyy

[profile_2]
bbbb=bbbb
bbbb=bbbb
bbbb=bbbb
```

这种方案带来了附属影响，即 `profile=default` 原本是空的，而此时被赋予了 `yyy...` 这部分参数。
