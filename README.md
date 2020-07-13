# QtDocument_CN

本项目为翻译Qt官方文档，内容基于 Qt 最新发布版本 5.15。

# License
[![CC BY-NC-ND 4.0](https://creativecommons.org/images/deed/svg/cc_blue.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)
[![CC BY-NC-ND 4.0](https://creativecommons.org/images/deed/svg/attribution_icon_blue.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)
[![CC BY-NC-ND 4.0](https://creativecommons.org/images/deed/svg/nc_blue.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)
[![CC BY-NC-ND 4.0](https://creativecommons.org/images/deed/svg/nd_blue.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)

本项目所有的文档遵循协议 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh) 

## 提交

各种提交代码之前一定要

```shell
git pull --rebase
```

## 目录管理

为方便快速填充内容，以及便于跨文档引用，文档按首字母排序，从A-Z共12个根文件夹。

每一个类新建一个文件夹，将该类的`.md`文件和其它引用的资源文件（如图片）放入其中。


比如我想翻译`QX11Info`类。

我要在 X 文件夹下，新建一个 QX11Info 的文件夹。

然后把对应的`QX11Info.md`文档放进去。

## Markdown 格式说明

可参考模板文件[Template.md](Template.md) ，抑或参考其它的的翻译文档。

### 注解

当翻译者需要添加额外的资料或吐槽时，需有明确的标注与官方文档区分开。

若为独立段落，建议使用`>`引用语法，并在开头标识`译者注:`。

若为段内信息，建议使用(译者注：xxx)的方式标注。

### 目录

无需使用`[TOC]`生成目录，因为：
1. `[TOC]`为扩展语法，并非 Markdown 原生语法，GitHub 不支持此扩展。
2. 本项目将使用 GitBook 发布，可自动生成侧边栏目录。

### 中英混排

中英混排时，英文内容前后需增加空格分隔，以避免文字过于紧凑：
> 正确写法：
>
> 我要在 X 文件夹下，新建一个 QX11Info 的文件夹。
>
> 错误写法：
>
> 我要在X文件夹下，新建一个QX11Info的文件夹。

文本字段落中的编程关键字，需用段内代码格式包裹，如：
```text
比如我想翻译`QX11Info`类。
```
比如我想翻译`QX11Info`类。

此时，段内代码自动提供了文字分隔视觉效果，无需再在英文内容前后增加空格。

### 图片

可直接使用Qt官方文档图片。

但官方文档图片为png/jpg格式，分辨率有限，且对主题样式无法自适应，因此推荐使用 [draw.io](https://app.diagrams.net/) 绘制的矢量图形，并将其保存为`.drawio.svg`格式，以便支持`.md`引用的同时，依然可以作为工程文件供 [draw.io](https://app.diagrams.net/) 编辑。

可使用 VSCode 插件 [hediet.vscode-drawio](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) 直接在 VSCode 中编辑图形。

范例参见 [信号与槽](S/Signals_and_Slots/Signals_and_Slots.md)。

## Markdown 编辑器

### Typora

为规范格式（空行、缩进等），减少多人合作编辑同一`.md`文件时的无意义的 diff 内容，推荐使用 [Typora](https://typora.io/) 编辑器。

该编辑器为类 Word 的所见即所得编辑方式，会自动按照固定格式对 Markdown 源码进行排版，从而避免手动排版与他人排版风格不匹配的问题。

### VSCode

若不想下载独立编辑工具，但想直观阅览 Markdown 渲染效果，则可直接使用 VSCode 编辑`.md`文件。

点击 VSCode 的`.md`文件标签页右上角的“打开侧边预览”(Ctrl+K V)，或在命令面板(F1)中搜索“Markdown”并选择打开预览(Markdown: Open Preview)即可。

## 路线图

1. 使用 GitBook 生成 GitHub Pages，作为实际发布页面。
