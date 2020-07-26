[TOC]

#　QWebEngineView Class

QWebEngineView类提供了一个widget, 被使用去查看和编辑web元素。

| 属性      | 方法                       |
| --------- | -------------------------- |
| 头文件    | \#include <QWebEngineView> |
| qmake参数 | QT += webenginewidgets     |
| 继承      | QWidget                    |

## 特性

| 属性名       | 类型          |
| ------------ | ------------- |
| hasSelection | const bool    |
| title        | const QString |
| icon         | const QIcon   |
| zoomFactor   | qreal         |
| selectedText | const QString |

## 公共成员函数

| 类型                 | 函数名                                                       |
| -------------------- | ------------------------------------------------------------ |
|                      | [QWebEngineView]()(QWidget *parent = Q_NULLPTR)]             |
| virtual              | [~QWebEngineView]()()                                        |
| void                 | [findText]()(const QString &*subString*, QWebEnginePage::FindFlags *options* = ..., const QWebEngineCallback<bool> &*resultCallback* = ...)] |
| bool                 | [hasSelection]()() const                                     |
| QWebEngineHostory *  | [history]()() const                                          |
| QIcon                | [icon]()() const                                             |
| QUrl                 | [iconUrl]()() const                                          |
| void                 | [load]()(const QUrl &url)                                    |
| void                 | [load](qwebengineview.html#load-1)(const QWebEngineHttpRequest &*request*) |
| QWebEnginePage *     | [page]()() const                                             |
| QAction *            | [pageAction](qwebengineview.html#pageAction)(QWebEnginePage::WebAction *action*) const |
| QString              | [selectedText](qwebengineview.html#selectedText-prop)() const |
| void                 | [setContent](qwebengineview.html#setContent)(const QByteArray &*data*, const QString &*mimeType* = QString(), const QUrl &*baseUrl* = QUrl()) |
| void                 | [setHtml](qwebengineview.html#setHtml)(const QString &*html*, const QUrl &*baseUrl* = QUrl()) |
| void                 | [setPage](qwebengineview.html#setPage)(QWebEnginePage **page*) |
| void                 | [setUrl](qwebengineview.html#url-prop)(const QUrl &*url*)    |
| void                 | [setZoomFactor](qwebengineview.html#zoomFactor-prop)(qreal *factor*) |
| QWebEngineSettings * | [settings](qwebengineview.html#settings)() const             |
| QString              | [title](qwebengineview.html#title-prop)() const              |
| void                 | [triggerPageAction](qwebengineview.html#triggerPageAction)(QWebEnginePage::WebAction *action*, bool *checked* = false) |
| QUrl                 | [url](qwebengineview.html#url-prop)() const                  |
| qreal                | [zoomFactor](qwebengineview.html#zoomFactor-prop)() const    |

## 重实现公共成员函数

virtual QSize sizeHint() const override

- 216 个公共成员函数继承自 QWidget
- 31 个公共成员函数继承自 QObject
- 14 个公共成员函数继承自 QPaintDevice

## 公有槽函数

| 类型 | 函数名        |
| ---- | ------------- |
| void | [back()]()    |
| void | [forward()]() |
| void | [reload()]()  |
| void | [stop()]()    |

- 19 个公共槽函数继承自 QWidget
- 1  个公共槽函数继承自 QObject



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | [iconChanged]()(const QIcon &icon)                           |
| void | [iconUrlChanged](qwebengineview.html#iconUrlChanged)(const QUrl &*url*) |
| void | [iconUrlChanged](qwebengineview.html#iconUrlChanged)(const QUrl &*url*) |
| void | [loadProgress](qwebengineview.html#loadProgress)(int *progress*) |
| void | [loadStarted](qwebengineview.html#loadStarted)()             |
| void | [renderProcessTerminated](qwebengineview.html#renderProcessTerminated)(QWebEnginePage::RenderProcessTerminationStatus *terminationStatus*, int *exitCode*) |
| void | [selectionChanged](qwebengineview.html#selectionChanged)()   |
| void | [titleChanged](qwebengineview.html#titleChanged)(const QString &*title*) |
| void | [urlChanged](qwebengineview.html#urlChanged)(const QUrl &*url*) |

- 3 signals inherited from QWidget
- 2 signals inherited from QObject

## 静态公有成员函数

- 5  个静态公有成员函数继承自 QWidget
- 9 个静态公有成员函数 QObject

## 保护成员函数

virtual QWebEngineView *
[createWindow]()(QWebEnginePage::WebWindowType type)

## 重实现保护成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| vitrual void | [contextMenuEvent](qwebengineview.html#contextMenuEvent)(QContextMenuEvent **event*) override |
| virtual void | [dragEnterEvent](qwebengineview.html#dragEnterEvent)(QDragEnterEvent **e*) override |
| virtual void | [dragLeaveEvent](qwebengineview.html#dragLeaveEvent)(QDragLeaveEvent **e*) override |
| virtual void | [dragMoveEvent](qwebengineview.html#dragMoveEvent)(QDragMoveEvent **e*) override |
| virtual void | [dropEvent](qwebengineview.html#dropEvent)(QDropEvent **e*) override |
| virtual bool | [event](qwebengineview.html#event)(QEvent **ev*) override    |
| virtual void | [hideEvent](qwebengineview.html#hideEvent)(QHideEvent **event*) override |
| virtual void | [showEvent](qwebengineview.html#showEvent)(QShowEvent **event*) override |

- 35 个保护成员函数继承自 QWidget

- 9  个保护成员函数继承自 QObject
- 1  个保护成员函数继承自 QPaintDevice

## 额外继承成员

- 一个保护槽继承自QWidget

## 详细描述

QWebEngineView类提供了一个小部件, 被用去查看和编辑web文档。

一个web视图是组成Qt WebEngine web 浏览模块的主要widget之一。它可以被用于多种应用去展示来自Internet的web内容。

一个web元素可以通过[load]()()函数加载到web视图。一般总是使用Get方法去加载URLs.

像所有的Qt widgets, 为了展示web的视图， [show]()() 函数 必须被执行。The snippet below illustrates this:

```
QWebEngineView *view = new QWebEngineView(parent);
      view->load(QUrl("http://qt-project.org/"));
      view->show();
```

或者, [setUrl]()() 可以被使用去加载web元素。如果你有可读的 HTML 内容，你可以使用[setHtml]()() 代替。

当视图开始加载的时候，发出[loadStarted]()() 信号，当web视图的一个元素被完整加载的时候，发出[loadProgress]()()信号，例如一个embedded 图像或一个脚本。当视图被完整加载时，发出[loadFinished]()()信号。其参数true或false指示加载是成功还是失败。

[page]()()函数返回一个指向web页对象的指针。一个[QWebEngineView](qwebengineview.html) 包含一个[QWebEnginePage](../../W/QWebEnginePage.md), 允许依次访问[QWebEnginePage](../../W/QWebEngineHistory.md)在页的内容里。HTML文档的标题可以用[title](qwebengineview.html#title-prop)()属性访问。另外，一个web元素可能是一个图标， 可以使用[icon](qwebengineview.html#icon-prop)()访问，使用 [iconUrl](qwebengineview.html#iconUrl-prop)()访问图标的URL。如果标题或是图标改变，将发出[titleChanged](qwebengineview.html#titleChanged)(), [iconChanged](qwebengineview.html#iconChanged)() 和 [iconUrlChanged](qwebengineview.html#iconUrlChanged)()信号来回应。[zoomFactor](qwebengineview.html#zoomFactor-prop)()属性通过缩放因子，能够缩放web页的内容。

该小部件适合于上下文菜单并包含在浏览器中有用的操作。对于自定义上下文菜单，或将动作嵌入菜单或工具栏中，可通过[pageAction]()()获得单个动作。web视图维护返回动作的状态，但允许修改动作属性，例如[text](../qtwidgets/qaction.html#text-prop) or [icon](../qtwidgets/qaction.html#icon-prop). 动作语义也可以通过 [triggerPageAction](qwebengineview.html#triggerPageAction)()直接触发。

对于web元素，如果你想要提供 支持允许用户去打开新的窗口，例如pop-up windows, 你可以子类化[QWebEngineView](qwebengineview.html) 和实现 [createWindow](qwebengineview.html#createWindow)() 函数。

您也可以在 [WebEngine Widgets Simple Browser Example](qtwebengine-webenginewidgets-simplebrowser-example.html), [WebEngine Content Manipulation Example](qtwebengine-webenginewidgets-contentmanipulation-example.html), 和 [WebEngine Markdown Editor Example](qtwebengine-webenginewidgets-markdowneditor-example.html)的文档中找到相关的信息。

## 特性文档编制

| 属性名       | 类型       |
| ------------ | ---------- |
| hasSelection | const bool |

此属性保存此页面是否包含所选内容。
默认情况下，此属性为false。

**访问函数：**

bool **hasSelection() ** const

另请参见 [selectionChanged](qwebengineview.html#selectionChanged)()。



| 属性名 | 类型        |
| ------ | ----------- |
| icon   | const QIcon |

此属性保存当前可视页面关联的图标。

默认，这个属性包含一个空图标。

**访问函数：**

QIcon **icon**() const

**通知信号：**

void [iconChanged](qwebengineview.html#iconChanged)(const QIcon &*icon*)

另请参见[iconChanged](qwebengineview.html#iconChanged)(), [iconUrl](qwebengineview.html#iconUrl-prop)(), 和 [iconUrlChanged](qwebengineview.html#iconUrlChanged)()。



| 属性名  | 类型                              |
| ------- | --------------------------------- |
| iconUrl | const [QUrl](../qtcore/qurl.html) |

此属性保存当前可视页面关联图标的URL。

默认，这个属性包含一个空URL。

该特性在 Qt 5.7 引入。

**访问函数：**

QIcon **iconUrl**() const

**通知信号：**

void [iconUrlChanged](qwebengineview.html#iconUrlChanged)(const QUrl &*url*)

另请参见[iconUrlChanged](qwebengineview.html#iconUrlChanged)(), [icon](qwebengineview.html#icon-prop)(), 和 [iconChanged](qwebengineview.html#iconChanged)()。



| 属性名       | 类型                                    |
| ------------ | --------------------------------------- |
| selectedText | const [QString](../qtcore/qstring.html) |

此属性保存了当前选中的文本。

默认，此属性包含一个空字符串。

**访问函数：**

QString **selectionText**() const

另请参见[findText](qwebengineview.html#findText)() 和 [selectionChanged](qwebengineview.html#selectionChanged)()。

| 属性名 | 类型                                    |
| ------ | --------------------------------------- |
| title  | const [QString](../qtcore/qstring.html) |

此属性保存了定义为HTML<title>元素页面的标题。

**访问函数：**

QString **title**() const

另请参见[titleChanged](qwebengineview.html#titleChanged)().



| 属性名 | 类型                        |
| ------ | --------------------------- |
| url    | [QUrl](../qtcore/qurl.html) |

此属性保存了当前可视web页面的URL。

设置这个属性会清空此view和加载URL。

默认，这个属性包含一个空的，无效的URL。

**访问函数：**

QUrl **url**() const

void **setUrl**(const QUrl &url)

另请参见[load](qwebengineview.html#load)() 和 [urlChanged](qwebengineview.html#urlChanged)().

| 属性名     | 类型  |
| ---------- | ----- |
| zoomFactor | qreal |

此属性保存了该view的缩放因子。

有效数值的范围从 0.25 到 5.0。默认因子是1.0。

**访问函数：**

qreal [zoomFactor]()() const
void [setZoomFactor]()(qreal factor)

## 成员函数文档

### QWebEngineView::**QWebEngineView**([QWidget](../../W/QWidget.md) **parent* = Q_NULLPTR)

与父类parent构造一个空的网页视图。

另请参见[load](qwebengineview.html#load)()。



### [virtual] QWebEngineView::~QWebEngineView()

销毁网页视图。



### [slot] void QWebEngineView::back()

方便的槽函数，加载构建到导航链接的文档列表里的前一个文档。如果没有前一个文档，就不执行任何操作。

它等价于

```
      view->page()->triggerAction(QWebEnginePage::Back);

```

另请参见[forward](qwebengineview.html#forward)() 和 [pageAction](qwebengineview.html#pageAction)()。



###  [override virtual protected] void QWebEngineView::contextMenuEvent([QContextMenuEvent](../../C/QContextMenuEvent.md) **event*)

重实现 [QWidget::contextMenuEvent](../qtwidgets/qwidget.html#contextMenuEvent)()。



###  [virtual protected] [QWebEngineView](qwebengineview.html#QWebEngineView) *QWebEngineView::createWindow([QWebEnginePage::WebWindowType](qwebenginepage.html#WebWindowType-enum) *type*)

每当页面想要创建给定类型的新窗口时，都会从关联的QWebEnginePage的createWindow（）方法中调用此函数。 例如，当发出JavaScript请求以在新窗口中打开文档时。
**注意：** 如果重新实现了关联页面的createWindow（）方法，则不会调用此方法，除非在重新实现中明确地这样做。



### [override virtual protected] void QWebEngineView::dragEnterEvent([QDragEnterEvent](../../D/QDragEnterEvent.md) **e*)

重实现[QWidget::dragEnterEvent](../qtwidgets/qwidget.html#dragEnterEvent)()。



### [override virtual protected] void QWebEngineView::dragLeaveEvent([QDragLeaveEvent](../../D/QDragLeaveEvent.md) **e*)

重实现[QWidget::dragLeaveEvent](../qtwidgets/qwidget.html#dragLeaveEvent)().



### [override virtual protected] void QWebEngineView::dragMoveEvent([QDragMoveEvent](../../D/QDragMoveEvent.md) **e*)

重实现[QWidget::dragMoveEvent](../qtwidgets/qwidget.html#dragMoveEvent)()。



###　[override virtual protected] void QWebEngineView::dropEvent([QDropEvent](../../D/QDropEvent.md) **e*)

重实现[QWidget::dropEvent](../qtwidgets/qwidget.html#dropEvent)()。



###　[override virtual protected] bool QWebEngineView::event([QEvent](../../E/QEvent.md) **ev*)

重实现[QWidget::event](../qtwidgets/qwidget.html#event)().

###  void QWebEngineView::findText(const [QString](../../S/QString.md) &*subString*, [QWebEnginePage::FindFlags](qwebenginepage.html#FindFlag-enum) *options* = ..., const QWebEngineCallback<bool> &*resultCallback* = ...）

在页面里找到特殊的字符串，子字符串，通过使用*options*。

去清空选中部分，只需要传递一个空的字符串。

*resultCallback*必须带boolean参数， 它将返回true或false, 表明是否找到子字符串。

**注意：** 我们保证回调函数总是可以被调用，但可能需要在页面构造完成之后。当[QWebEnginePage](../../W/QWebEnginePage.md) 被删除时，该回调触发带着一个无效的值且作为 [QWebEnginePage](../../W/QWebEnginePage.md) or [QWebEngineView](qwebengineview.html)实例里使用是不安全的。

### [slot] void QWebEngineView::forward()

方便的槽函数，加载构建到导航链接的文档列表里的前一个文档。如果没有前一个文档，就不执行任何操作。

它等价于

```
      view->page()->triggerAction(QWebEnginePage::Forward);

```

另请参见 [back](qwebengineview.html#back)() 和 [pageAction](qwebengineview.html#pageAction)()。

###  [override virtual protected] void QWebEngineView::hideEvent([QHideEvent](../../H/QHideEvent.md) **event*)

重实现[QWidget::hideEvent](../qtwidgets/qwidget.html#hideEvent)().



###  [QWebEngineHistory](../../W/QWebEngineHistory.md) *QWebEngineView::history() const

返回指向web导航页面视图历史的指针。

它等价于:

```
      view->page()->history();
```



### [signal] void QWebEngineView::iconChanged(const [QIcon](../../I/QIcon.md) &*icon*)

当与视图关联的图标（“favicon”）更改时，将发出此信号。 新图标由图标指定。
此功能在Qt 5.7中引入。
注意：属性图标的通知程序信号。
另请参见 [icon](qwebengineview.html#icon-prop)(), [iconUrl](qwebengineview.html#iconUrl-prop)(), 和 [iconUrlChanged](qwebengineview.html#iconUrlChanged)()。

### [signal] void QWebEngineView::iconUrlChanged(const [QUrl](../../U/QUrl.md) &*url*)

当与视图关联的图标（“图标”）的URL更改时，将发出此信号。 新URL由url指定。
注意：属性iconUrl的通知程序信号。
另请参见[icon](qwebengineview.html#icon-prop)(), [iconUrl](qwebengineview.html#iconUrl-prop)(), 和 [iconUrlChanged](qwebengineview.html#iconUrlChanged)()。

### void QWebEngineView::load(const [QUrl](../../U/QUrl.md) &*url*)

加载指定的url和显示它。

**注意：** 该视图保持相同的内容直到足够多的数据去展示新的URL。

另请参见 load(), [setUrl](qwebengineview.html#url-prop)(), [url](qwebengineview.html#url-prop)(), [urlChanged](qwebengineview.html#urlChanged)(), 和 [QUrl::fromUserInput](../qtcore/qurl.html#fromUserInput)().



### void QWebEngineView::load(const [QWebEngineHttpRequest](../../W/QWebEngineHttpRequest.md) &*request*)

发出指定的请求并加载响应。
Qt 5.9中引入了此功能。
另请参见[load](qwebengineview.html#load)(), [setUrl](qwebengineview.html#url-prop)(), [url](qwebengineview.html#url-prop)(), [urlChanged](qwebengineview.html#urlChanged)(), and [QUrl::fromUserInput](../qtcore/qurl.html#fromUserInput)().



### [signal] void QWebEngineView::loadFinished(bool *ok*)

当加载该页面已经完成的时候，发出该信号。*ok* 表明加载是成功还是失败。

### [signal] void QWebEngineView::loadProgress(int *progress*)

每当Web视图中的某个元素完成加载（例如嵌入式图像或脚本）时，都会发出此信号。 因此，它跟踪加载Web视图的总体进度。

当前值由progress提供，范围为0到100，这是[QProgressBar](../qtwidgets/qprogressbar.html)的默认范围。

另请参见 [loadStarted](qwebengineview.html#loadStarted)() 和 [loadFinished](qwebengineview.html#loadFinished)().



### [signal] void QWebEngineView::loadStarted()

当新的页面开始被加载的时候，发出该信号。

### WebEnginePage *QWebEngineView::page() const

返回指向下划线web网页的指针。

### [QAction](../../A/QAction.md)*QWebEngineView::pageAction(QWebEnginePage::WebAction *action*) const

返回一个指向[QAction](../qtwidgets/qaction.html)的指针，封装了特定网页的动作。

### [slot] void QWebEngineView::reload()

重新加载当前的文档。

### [signal] void QWebEngineView::renderProcessTerminated([QWebEnginePage::RenderProcessTerminationStatus](qwebenginepage.html#RenderProcessTerminationStatus-enum) *terminationStatus*, int *exitCode*)

当渲染进程返回非零且中断的时候，发出该信号。

当进程中断时，*terminationStatus*指进程的中断状态，*exitCode*指进程的状态码。

该函数在 Qt 5.6 引入。


### [signal] void QWebEngineView::selectionChanged()

当选择的部分改变的时候，发出该信号。

**注意：** 当鼠标通过左键安和拖拽去选择文本时，对于每一个新的字符被选中都会发出该信号， 和 not upon releasing the left mouse button.

另请参见 [selectedText](qwebengineview.html#selectedText-prop)().



### void QWebEngineView::setContent(const [QByteArray](../qtcore/qbytearray.html) &*data*, const [QString](../qtcore/qstring.html) &*mimeType* = QString(), const [QUrl](../qtcore/qurl.html) &*baseUrl* = QUrl())

设置网页视图内容到数据里。如果*mimeType*是空参数，将假定该内容是text/plain,charset=US-ASCII。外部对象在内容里引用的路径是相对于*baseUrl*。

该数据会被立刻加载。外部对象会被异步加载。

另请参见 [load](qwebengineview.html#load)(), [setHtml](qwebengineview.html#setHtml)(), 和 [QWebEnginePage::toHtml](qwebenginepage.html#toHtml)().



### void QWebEngineView::setHtml(const [QString](../../S/QString.md) &*html*, const [QUrl](../../U/QUrl.md) &*baseUrl* = QUrl())

将Web视图的内容设置为指定的html内容。

外部对象（例如HTML文档中引用的样式表或图像）相对于baseUrl定位。
HTML文档将立即加载，而外部对象则异步加载。

使用此方法时，除非另有说明，否则Qt WebEngine假定外部资源（例如JavaScript程序或样式表）均以UTF-8编码。 例如，可以通过HTML脚本标签的charset属性指定外部脚本的编码。 或者，可以由Web服务器指定编码。
这是一个等效于setContent（html，“ text / html; charset = UTF-8”，baseUrl）的便利函数。

### void QWebEngineView::setPage([QWebEnginePage](../../W/QWebEnginePage.md) **page*)

确保设置page页面到页面视图中。

该父类[QObject](../qtcore/qobject.html)提供页面维护网页视图对象。如果当前页面是该网页视图的子类，它将会被删除。

**警告：**此功能仅适用于HTML。 对于其他MIME类型（例如XHTML或SVG），应改用setContent（）。

**注意：** 无法显示大于2 MB的内容，因为setHtml（）会将提供的HTML转换为百分比编码并将数据：放在其前面以创建要导航到的URL。 从而，提供的代码将成为超出Chromium设置的2 MB限制的URL。 如果内容太大，则使用success = false触发loadFinished（）信号。

另请参见 [load](qwebengineview.html#load)(), [setContent](qwebengineview.html#setContent)(), [QWebEnginePage::toHtml](qwebenginepage.html#toHtml)(), 和 [QWebEnginePage::setContent](qwebenginepage.html#setContent)().



### [QWebEngineSettings](../../W/QWebEngineSettings.md) *QWebEngineView::settings() const

返回一个指向该视图或页面特殊设置对象的指针。

它等价于:

```
      view->page()->settings();
```



另请参见 [QWebEngineSettings::globalSettings](qwebenginesettings-obsolete.html#globalSettings)().



### [override virtual protected] void QWebEngineView::showEvent([QShowEvent](../../S/QShowEvent.md) **event*)

重实现 [QWidget::showEvent](../qtwidgets/qwidget.html#showEvent)().



### [override virtual] [QSize](../../S/QSize.md) QWebEngineView::sizeHint() const

重实现 [QWidget::sizeHint](../qtwidgets/qwidget.html#sizeHint-prop)().



### [slot] void QWebEngineView::stop()

方便的槽函数，停止加载该文档。

它等价于:

```
      view->page()->triggerAction(QWebEnginePage::Stop);
```

另请参见 [reload](qwebengineview.html#reload)(), [pageAction](qwebengineview.html#pageAction)(), 和 [loadFinished](qwebengineview.html#loadFinished)().



### [signal] void QWebEngineView::titleChanged(const [QString](../../S/QString.md) &*title*)

当该视图的标题改变时，发出该信号。

另请参见 [title](qwebengineview.html#title-prop)().



### void QWebEngineView::triggerPageAction([QWebEnginePage::WebAction](qwebenginepage.html#WebAction-enum) *action*, bool *checked* = false)

触发特定的动作。如果它是可以选中的动作，这个特殊的选中状态被设定。

接下来的例子触发了复制动作，因此会拷贝任何选中的文本到剪贴板上。

```
      view->triggerPageAction(QWebEnginePage::Copy);
```

另请参见 [pageAction](qwebengineview.html#pageAction)().



### [signal] void QWebEngineView::urlChanged(const [QUrl](../../U/QUrl.md) &*url*)

当该视图的*url*改变时，发出该信号。

另请参见 [url](qwebengineview.html#url-prop)() 和 [load](qwebengineview.html#load)().
