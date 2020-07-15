# 贡献指南

## 提交说明

各种提交代码之前一定要

```shell
git pull --rebase
```

## 目录管理

为方便快速填充内容，以及便于跨文档引用，文档按首字母排序，从A-Z共12个根文件夹。

每一个类新建一个文件夹，将该类的`.md`文件和其它引用的资源文件（如图片）放入其中。

### 范例

比如我想翻译`QX11Info`类。

我要在 X 文件夹下，新建一个 QX11Info 的文件夹。

然后把对应的`QX11Info.md`文档放进去。

### 占位符

为避免编辑冲突，在完成第一版翻译前，请尽量不要多人修改同一个页面。

正在为某页面编写第一版翻译的参与者，可提交一个空文档作为占位符，并且在其中注明编写者和 deadline，如：
> Reserved by ZgblKylin until 2020-07-31.

超过 deadline 后尚未完成第一版提交的页面，或已经完成第一版提交的页面，均被视作**开放状态**，其它参与者可对其进行修改。

## 完成度追踪

每当添加一个占位页面，或已完成的页面有需要继续完善的内容，维护者有责任在[完成度追踪表](completeness_tracking.md)中更新对应信息。

已完成编写，无需进一步维护的页面，需从该表格中删除。

## Markdown 格式规范

可参考模板文件[Template.md](Template.md) ，抑或参考其它的翻译文档。

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

此时，段内代码自动提供了文字分隔视觉效果和前后间隔，无需再在英文内容前后增加空格。

### 图片

可直接使用Qt官方文档图片。

但官方文档图片为png/jpg格式，分辨率有限，且对主题样式无法自适应，因此推荐使用 [draw.io](https://app.diagrams.net/) 绘制的矢量图形，并将其保存为`.drawio.svg`格式，以便支持`.md`引用的同时，依然可以作为工程文件供 [draw.io](https://app.diagrams.net/) 编辑。

可使用 VSCode 插件 [hediet.vscode-drawio](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) 直接在 VSCode 中编辑图形。

范例参见 [信号与槽](S/Signals_and_Slots/Signals_and_Slots.md)。

### 引用链接

编写引用链接时，Markdown 支持直接链接跳转至目标页面的标题，语法如下：
```Markdown
跨页跳转：[真实范例](S/Signals_and_Slots/Signals_and_Slots.md#真实范例)
```
跨页跳转：[真实范例](S/Signals_and_Slots/Signals_and_Slots.md#真实范例)
```Markdown
页内跳转：[中英混排](CONTRIBUTING.md#中英混排)
```
页内跳转：[中英混排](CONTRIBUTING.md#中英混排)

注意：
1. `#`后的标题名称，与文本可能并不一致。若直接使用标题文本无法成功跳转，可尝试将`.md`导出至`.html`或提交至 GitHub 后，在标题处右键——检查元素，使用该元素的 html tag 中`id`字段值。
2. 不同工具导出的 html 标签字段并不一致，GitHub 生成的标签会比 Typora 的多`user-content-`前缀。实测无需该前缀也能完成跳转，因此建议不添加此前缀。待本项目发布至 GitBook 后，需要再次检查跳转链接是否能正确运作。


## Markdown 编辑器

### Typora

为规范格式（空行、缩进等），减少多人合作编辑同一`.md`文件时的无意义的 diff 内容，推荐使用 [Typora](https://typora.io/) 编辑器。

该编辑器为类 Word 的所见即所得编辑方式，会自动按照固定格式对 Markdown 源码进行排版，从而避免手动排版与他人排版风格不匹配的问题。

### VSCode

若不想下载独立编辑工具，但想直观阅览 Markdown 渲染效果，则可直接使用 VSCode 编辑`.md`文件。

点击 VSCode 的`.md`文件标签页右上角的“打开侧边预览”(Ctrl+K V)，或在命令面板(F1)中搜索“Markdown”并选择打开预览(Markdown: Open Preview)即可。
