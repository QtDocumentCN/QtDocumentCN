# 贡献指南

## 提交说明

各种提交代码之前一定要

```shell
git pull --rebase
```



## 目录/文件管理

为方便快速填充内容，以及便于跨文档引用，文档按首字母排序，从A-Z共12个根文件夹。

每一个类新建一个文件夹，将该类的`.md`文件和其它引用的资源文件（如图片）放入其中。

### 范例

比如我想翻译`QX11Info`类。

我要在 X 文件夹下，新建一个 QX11Info 的文件夹。

然后把对应的`QX11Info.md`文档放进去。

----

### 占位符

为避免编辑冲突，在完成第一版翻译前，请尽量不要多人修改同一个页面。

正在为某页面编写第一版翻译的参与者，可提交一个空文档作为占位符，并且在其中注明编写者和 deadline，如：
> Reserved by ZgblKylin until 2020-07-31.

超过 deadline 后尚未完成第一版提交的页面，或已经完成第一版提交的页面，均被视作**开放状态**，其它参与者可对其进行修改。

----

### Obselete Member

对于 `已废弃/Obselete` 的成员，Qt 会在类开头添加一个链接指向单独的页面。

若已废弃的成员数量并不多（独立页面中没有详细信息章节或函数列表），则为减少阅读时的跳转，建议将该页面作为一个单独的章节，附加到原页面尾部。

即将一级标题 `# Obselete Menber` 降级为二级标题 `## 已废弃成员`，其它标题同样进行降级处理。

----

### 子类型

如 [QMetaObject::Connection](Src/M/QMetaObject/QMetaObject_Connection.md) 等子类型，不应单独开文件夹，而是存在隶属类型的文件夹中。

子类型文件名称应带有隶属类型名称，如 `QMetaObject/QMetaObject_Connection.md`。

----

### 所有成员列表

无需单独添加所有成员列表页面。

该页面是类似 `[TOC]` 的目录索引功能，本项目中应交由发布脚本自动生成目录，而非浪费大量人力编写单独的目录页面——单独的页面在检索时需要在不同页面来回跳转，对于读者也不友好。

**注意：** 需对 `List of all members` 页面进行校对，确保其中所有内容均在主文档中有描述。若存在主文档中没有的内容，需将其挪到主文档中。



## 完成度追踪

每添加一个页面，需在[完成度追踪表](completeness_tracking.md)中增加相应条目。

当页面完成编辑、完成维护等状态改变时，维护者有责任在[完成度追踪表](completeness_tracking.md)中更新对应信息。

需要新增或修改一篇文档时，请先检索追踪表中是否已存在该文档，和该文档的翻译进度。



## 参考资料

技术词汇的翻译可参考 [词汇对照表](Comparison_Table.md)。

关于如何将英文文档信达雅地翻译为中文技术文档，可参考 [语法小贴士](Grammar_Tips.md)。



## Markdown 格式规范

可参考模板文件[Template.md](Template.md) ，抑或参考其它的翻译文档。

翻译名词可参考[对照表](Comparison_Table.md)。

### 类成员或实现方法标题

在对类成员或实现方法进行讲解时，我们决定采用 Qt 官方文档的命名方式。

以成员函数标题为例： `[修饰符] 返回类型 函数名(参数类型 参数名) const/volatile/override`。

其中，`函数名 `加粗，`修饰符`、`参数名` 斜体，`const/volatile/override` 等后缀不添加额外修饰。

示例：

```
### *[static]* int QString::**compare**(const QString &*s1*, const QString &*s2*, Qt::CaseSensitivity *cs* = Qt::CaseSensitive)
### *[virtual protected]* void QObject::**childEvent**(QChildEvent \**event*)
### *[override virtual]* qint64 QAbstractSocket::**bytesAvailable**() const
```

> *[static]* int QString::**compare**(const QString &*s1*, const QString &*s2*, Qt::CaseSensitivity *cs* = Qt::CaseSensitive)
> 
> *[virtual protected]* void QObject::**childEvent**(QChildEvent *\*event*)
> 
> *[override virtual]* qint64 QAbstractSocket::**bytesAvailable**() const

注：对于指针变量`**event*`，请添加转义符 `\`，以避免开头的两个星在多个指针变量中，被渲染为加粗。

----

### 注解

当翻译者需要添加额外的资料或吐槽时，需有明确的标注与官方文档区分开。

若为独立段落，建议使用`>`引用语法，并在开头单独一行标识`译者注:`。

若为段内信息，建议使用段内代码(`译者注：xxx`)的方式标注。

----

### 目录

无需使用`[TOC]`生成目录，因为：
1. `[TOC]`为扩展语法，并非 Markdown 原生语法，GitHub 不支持此扩展。
2. 本项目将使用 GitBook 发布，可自动生成侧边栏目录。

----

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
比如我想翻译 `QX11Info` 类。
```
比如我想翻译 `QX11Info` 类。

----

### 图片

可直接使用 Qt 官方文档图片。

但官方文档图片为 png/jpg 格式，分辨率有限，且对主题样式无法自适应，因此推荐使用 [draw.io](https://app.diagrams.net/) 绘制的矢量图形，并将其保存为`.drawio.svg`格式，以便支持`.md`引用的同时，依然可以作为工程文件供 [draw.io](https://app.diagrams.net/) 编辑。

可使用 VSCode 插件 [hediet.vscode-drawio](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) 直接在 VSCode 中编辑图形。

范例参见 [信号与槽](S/Signals_and_Slots/Signals_and_Slots.md)。

----

### 引用链接

#### 页内跳转

Markdown 页内标题跳转较为简便，语法如下：

```markdown
[页内跳转](本文档名#页内跳转标题)
```

页内跳转：[中英混排](CONTRIBUTING.md#中英混排)

省略本文件名称时，通常也可进行跳转，但有的场景会无法正确生成跳转链接，因此不建议省略。

#### 跨页跳转

编写引用链接时，Markdown 支持直接链接跳转至目标页面的标题，语法如下：

相对路径：

```Markdown
跨页跳转：[真实范例](S/Signals_and_Slots/Signals_and_Slots.md#真实范例)
```
跨页跳转：[真实范例](S/Signals_and_Slots/Signals_and_Slots.md#真实范例)

注：在相对路径中您可以使用`../`进行上层目录访问。

绝对路径：

```Markdown
跨页跳转：[QAbstractSocket::socketDescriptor()](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const)
```
跨页跳转：[QAbstractSocket::socketDescriptor()](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const)

注意：
1. `#`后的标题名称，与文本可能并不一致。若直接使用标题文本无法成功跳转，可尝试：

   1. 将`.md`导出至`.html`，在标题处右键——检查元素，使用该元素的 html tag 中`id`字段值；
   2. （推荐此种方法）提交至 GitHub 后，直接复制标题左方的超链接图标所指向的地址并进行修改。

2. 为方便生成其它不依赖 GitHub 的发布页面，建议使用相对路径跳转而非绝对路径。

2. 不同工具导出的 html 标签字段并不一致，GitHub 生成的中文标题标签会比 Typora 的多`user-content-`前缀。实测无需该前缀也能完成跳转，因此建议不添加此前缀，以减少对特定导出工具的依赖。待本项目发布至 GitBook 后，需要再次检查跳转链接是否能正确运作。

3. 若要跨页跳转的目标页尚未完成，可以先采用规则进行目标地址的推算，待目标页完成后再进行检查。

原标题：
> ```
> ### *[override virtual]* bool **QAbstractSocket**::waitForBytesWritten(int *msecs* = 30000)
> ### bool **QAbstractSocket**::bind(const QHostAddress &*address*, quint16 *port* = 0, QAbstractSocket::BindMode *mode* = DefaultForPlatform)
> ```

跳转路径：
> ```
> #override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000
> #bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform
> ```

从以上示例我们可以推导出跳转规则：
* `* ：() & [] =` 等所有符号直接省略；
* 大写全部改为小写；
* `空格` 改为 `-`。

此外，中文标题请改为 `%` 转义格式，如 `[更多内容...](#详细描述)` 应改为 `[更多内容...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)`。

#### 第三方链接

除 Qt 原文档中的第三方链接，根据翻译需求添加的 `译者注：` 中，**只应**引用其它官方组织的文档，如 [CppReference](https://en.cppreference.com/w/) 或 [MSDN](https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadid)，**不可**添加个人博客等非官方组织的链接。



## Markdown 编辑器

### Typora

为规范格式（空行、缩进等），减少多人合作编辑同一`.md`文件时的无意义的 diff 内容，推荐使用 [Typora](https://typora.io/) 编辑器。

该编辑器为类 Word 的所见即所得编辑方式，会自动按照固定格式对 Markdown 源码进行排版，从而避免手动排版与他人排版风格不匹配的问题。

----

### VSCode

若不想下载独立编辑工具，但想直观阅览 Markdown 渲染效果，则可直接使用 VSCode 编辑`.md`文件。

点击 VSCode 的`.md`文件标签页右上角的“打开侧边预览”(Ctrl+K V)，或在命令面板(F1)中搜索“Markdown”并选择打开预览(Markdown: Open Preview)即可。
