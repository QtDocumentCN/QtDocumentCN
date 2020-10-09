Reserved by froser until 2020-09-15

[TOC]

# QCoreApplication 类

QCoreApplication类为没有UI的Qt程序提供了一个事件循环。

|   属性 | 方法                                                         |
| -----: | :----------------------------------------------------------- |
| 头文件 | `#include<QCoreApplication>`                                 |
|  qmake | `QT+=core`                                                   |
|   自从 | Qt 4.6                                                       |
|   继承 | [QObject](../../O/QObject/QObject.md)                        |
|   派生 | [QGuiApplication](../../G/QGuiApplication/QGuiApplication.md) |



## 属性

| 属性                                        | 类型    | 属性                                     | 类型    |
| :------------------------------------------ | ------- | ---------------------------------------- | ------- |
| [applicationName](#currentloop--const-int)  | QString | [organizationName](#duration--const-int) | QString |
| [applicationVersion](#currenttime--int)     | QString | [quitLockEnabled](#loopcount--int)       | QString |
| [organizationDomain](#direction--direction) | QString |                                          |         |
## 公共成员函数



## 详细说明

此类为那些没有GUI的应用程序提供消息循环。对于使用Qt但无GUI的程序，它们必须有且仅有一个QCoreApplication对象。对于GUI应用程序，请参见[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md)。对于使用了Qt Widgets的模块，请参见[QApplication](../../A/QApplication/QApplication.md)。

QCoreApplication包含主事件循环，这些来自于操作系统（如定时器、网络事件等）及其它来源的事件将由它来处理和派发。它同时也处理应用程序的初始化和析构，以及全系统和全程序的设置。



## 事件循环及事件处理

消息循环从调用exec()开始。长时间运行的一些操作也可以通过调用processEvents()让程序保持响应。

一般地，我们建议您尽可能早地在您的main()函数中创建QCoreApplication、[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md)或[QApplication](../../A/QApplication/QApplication.md)。当消息循环退出时，例如当quit()被调用时，exec()才会返回。

我们也提供了一些便捷的静态函数。QCoreApplication对象能够通过instance()来获取。您可以通过sendEvent()来发送事件，以及通过postEvent()来投送事件。待处理的事件能通过removePostedEvents()来移除，亦可通过sendPostedEvents()来派发。

此类提供了一个槽函数quit()及一个信号aboutToQuit()。



## 程序和库路径

一个应用程序有一个applicationDirPath()和一个applicationFilePath()。库路径(参见[QLibrary](../../L/QLibrary/QLibrary.md))能通过libraryPaths()被获取，且能通过setLibraryPaths()、addLibraryPath()和removeLibraryPath()来对它进行操作。



## 国际化和翻译

翻译文件能分别通过[installTranslator]()()和[removeTranslator]()()被加载和移除。您可以通过[translate]()()来翻译应用中的字符串。[QObject::tr]()()和QObject::trUtf8()这两个函数根据translate()来进行了实现。



## 访问命令行参数

您应该通过arguments()来获取传递给QCoreApplication构造函数的命令行参数。

注意：QCoreApplication将移除**-qmljsdebugger="..."**选项。它会解析**qmljsdebugger**参数，然后删除此选项及其参数。

对于一些更加高级的命令行参数的处理，请创建一个[QCommandLineParser](../QCommandLineParser/QCommandLineParser.md)。



## 区域设置

运行在Unix/Linux的Qt程序，将会默认使用系统的区域设置。这可能会导致在使用POSIX函数时发生冲突，例如，数据类型转换时由转换浮点数转换为字符串，由于不同区域符号的差异可能会导致一些冲突。为了解决这个问题，在初始化[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md)、[QApplication](../../A/QApplication/QApplication.md)或QCoreApplication之后，需要马上调用POSIX函数**setlocale(LC_NUMERIC, "C")**，以重新将数字的格式设置为"C"-locale。

另请参阅[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md), [QAbstractEventDispatcher](../../A/QAbstractEventDispatcher/QAbstractEventDispatcher.md), [QEventLoop](../../E/QEventLoop/QEventLoop.md), [Semaphores Example](../../S/Semaphorse Example/Semaphores Example.md), 以及[Wait Conditions Example](../../W/Wait Conditions Example/Wait Conditions Example.md)。



## 属性文档

### applicationName : [QString](../../S/QString/QString.md)

此属性保存应用程序的名字。

当使用空的构造函数初始化[QSettings](../../S/QSettings/QSettings.md)类的实例时，此属性被使用。这样一来，每次创建[QSettings](../../S/QSettings/QSettings.md)对象时，都不必重复此信息。

如果未设置，则应用程序名称默认为可执行文件名称（自5.0开始）。

**访问函数：**

| QString | **applicationName**()                                |
| ------- | ---------------------------------------------------- |
| void    | **setApplicationName**(const QString &*application*) |

**通知信号：**

| void | **applicationNameChanged**() |
| ---- | ---------------------------- |
| | |

另请参阅 [organizationName](https://doc.qt.io/qt-5/qcoreapplication.html#organizationName-prop), [organizationDomain](https://doc.qt.io/qt-5/qcoreapplication.html#organizationDomain-prop), [applicationVersion](https://doc.qt.io/qt-5/qcoreapplication.html#applicationVersion-prop), 以及 [applicationFilePath](https://doc.qt.io/qt-5/qcoreapplication.html#applicationFilePath)()。



### applicationVersion: [QString](../../S/QString/QString.md)

此属性保存应用程序的版本。

如果没有设置此属性，那么此属性将会被默认设置为平台相关的值，该值由主应用程序的可执行文件或程序包确定（自Qt 5.9起）：



|           平台            |                         源                         |
| :-----------------------: | :------------------------------------------------: |
|    Windows (经典桌面)     |      VERSIONINFO 资源中的 PRODUCTVERSION 参数      |
| Windows通用应用平台(UWP)  |           应用程序包中清单文件的版本属性           |
| macOS, iOS, tvOS, watchOS |        信息属性列表中的CFBundleVersion属性         |
|          Android          | AndroidManifest.xml清单中的android:versionName属性 |

在其他平台上，此属性默认值为空字符串。

此属性自Qt 4.4引入。

**访问函数：**

| QString | **applicationVersion**()                            |
| ------- | --------------------------------------------------- |
| void    | **setApplicationVersion**(const QString &*version*) |

**通知信号：**

| void | **applicationVersionChanged**() |
| ---- | ------------------------------- |
|      |                                 |

另请参阅[applicationName](),  [organizationName](), 以及[organizationDomain]()。



### organizationDomain: [QString](../../S/QString/QString.md)

此属性保存编写此应用程序的组织的Internet域。

当使用空的构造函数初始化[QSettings](../../S/QSettings/QSettings.md)类的实例时，此属性被使用。这样一来，每次创建[QSettings](../../S/QSettings/QSettings.md)对象时，都不必重复此信息。

在Mac上，如果organizationDomain()不是一个空值，那么[QSettings](../../S/QSettings/QSettings.md)将会使用它；否则它将会使用[organizatioName]()()。在其他平台上，[QSettings](../../S/QSettings/QSettings.md)将[organizationName]()()作为组织名来使用。

**访问函数：**

| QString | **organizationDomain**()                              |
| ------- | ----------------------------------------------------- |
| void    | **setOrganizationDomain**(const QString &*orgDomain*) |

**通知信号：**

| void | **organizationDomainChanged**() |
| ---- | ------------------------------- |
|      |                                 |

另请参阅 [organizationName](), [applicationName](), 以及[applicationVersion]()。



### organizationName: [QString](../../S/QString/QString.md)

此属性保存编写此应用程序的组织名。

当使用空的构造函数初始化[QSettings](../../S/QSettings/QSettings.md)类的实例时，此属性被使用。这样一来，每次创建[QSettings](../../S/QSettings/QSettings.md)对象时，都不必重复此信息。

在Mac上，如果organizationDomain()不是一个空值，那么[QSettings](../../S/QSettings/QSettings.md)将会使用它；否则它将会使用[organizatioName]()()。在其他平台上，[QSettings](../../S/QSettings/QSettings.md)将[organizationName]()()作为组织名来使用。

**访问函数：**

| QString | **organizationName**()                            |
| ------- | ------------------------------------------------- |
| void    | **setOrganizationName**(const QString &*orgName*) |

**通知信号：**

| void | **organizationNameChanged**() |
| ---- | ----------------------------- |
|      |                               |

另请参阅 [applicationDomain]()和[applicationName]()。



### quitLockEnabled: bool

此属性保存使用[QEventLoopLocker](../../E/QEventLoopLocker/QEventLoopLocker.md)是否能退出的特性。

默认值是**true**。

**访问函数：**

| bool | **isQuitLockEnabled**()                |
| ---- | -------------------------------------- |
| void | **setQuitLockEnabled**(bool *enabled*) |

另请参阅 [QEventLoopLocker](../../E/QEventLoopLocker/QEventLoopLocker.md)。



## 成员函数文档

------

### QCoreApplication::QCoreApplication(int &*argc*, char ***argv*)

构造一个Qt内核程序。所谓内核程序，就是没有图形用户界面的程序。这样的程序使用控制台，或者是作为服务进程运行着。

*argc*和*argv*参数将会被应用程序处理，将其转换为一种更加便捷的形式，并可以通过[arguments]()()来获取。

**警告**：*argc*和*argv*这两个值所指向的内存，必须在整个QCoreApplication生命周期内有效。另外，*agrc*必须要大于0，且*argv*必须至少包含一个合法的字符串。



-------------

### void QCoreApplication::aboutToQuit() [signal]

当程序即将退出主消息循环时，如当消息循环嵌套层数降为0时，此事件被发射。它可能发生在应用程序中调用[quit]()()之后，亦发生在关闭整个桌面会话时。

**注意**：这是一个私有信号。它能够被连接，但是用户无法发射它。

**另请参阅** [quit](https://doc.qt.io/qt-5/qcoreapplication.html#quit)()。





-----------

### void QCoreApplication::quit() [static slot]

告知程序以返回值0来退出。等效于调用 [QCoreApplication::exit]()(0)。

一般我们将quit()槽连接到[QGuiApplication::lastWindowClosed]()()信号，您同样可以将此槽连接到[QAction](../../A/QAction/QAction.md)、[QMenu](../../M/QMenu/QMenu.md)或[QMenuBar](../../M/QMenuBar/QMenuBar.md)的[QAbstractButton::clicked]()()信号上。

将信号以[QueuedConnection]()参数连接此槽是一个不错的实践。如果连接了此槽的一个信号（未在队列中的）在控制流程进入主消息循环前（如在int main中调用[exec]()()之前）被发射，那么这个槽不会有任何效果，应用程序也不会退出。使用队列连接方式能保证控制路程进入主消息循环后，此槽才会被触发。

例如：

```C++
QPushButton *quitButton = new QPushButton("Quit");
connect(quitButton, &QPushButton::clicked, &app, &QCoreApplication::quit, Qt::QueuedConnection);
```

**另请参阅** [exit](https://doc.qt.io/qt-5/qcoreapplication.html#exit)(), [aboutToQuit](https://doc.qt.io/qt-5/qcoreapplication.html#aboutToQuit)(), and [QGuiApplication::lastWindowClosed](https://doc.qt.io/qt-5/qguiapplication.html#lastWindowClosed)()。



----------
### QCoreApplication::~QCoreApplication() [virtual]


销毁[QCoreApplication](./QCoreApplication.md)对象。



-----

### void QCoreApplication::addLibraryPath(const [QString](../../S/QString/QString.md) &*path*) [static]

将*path*添加到库路径开头，保证它先会被库搜索到。如果*path*为空或者已经存在于路径列表，那么路径列表保持不变。

默认的路径列表只包含一个条目，即插件安装路径。默认的插件安装文件夹是`INSTALL/plugins`，其中`INSTALL`是Qt安装文件夹。

当[QCoreApplication](./QCoreApplication.md)被销毁后，这些库路径将会被重设为默认值。

**另请参阅** [removeLibraryPath](https://doc.qt.io/qt-5/qcoreapplication.html#removeLibraryPath)(), [libraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#libraryPaths)(), and [setLibraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#setLibraryPaths)().



----

### [QString](../../S/QString/QString.md) QCoreApplication::applicationDirPath() [static]

返回包含此可执行文件的文件夹路径。

例如，您已经在`C:\Qt`安装了Qt，然后运行`regexp`示例，那么这个函数会返回"C:/Qt:/examples/tools/regexp"。

在macOS和iOS上，它会指向实际包含可执行文件的目录，该目录可能在一个应用程序包内（如果是以应用程序包形式存在）。

**警告**：在Linux上，这个函数会尝试从`/proc`获取文件路径。如果失败了，那么它假设`argv[0]`包含了可执行文件的绝对路径。此函数同样也假设了应用程序不会改变当前路径。

**另请参阅** [applicationFilePath](https://doc.qt.io/qt-5/qcoreapplication.html#applicationFilePath)()。


----
### [QString](../../S/QString/QString.md) QCoreApplication::applicationFilePath() [static]


返回包含此可执行文件的文件路径。

例如，您已经在`/usr/local/qt`目录安装了Qt，然后运行`regexp`示例，那么这个函数会返回"/usr/local/qt/examples/tools/regexp/regexp"。

**警告**：在Linux上，这个函数会尝试从`/proc`获取文件路径。如果失败了，那么它假设`argv[0]`包含了可执行文件的绝对路径。此函数同样也假设了应用程序不会改变当前路径。

**另请参阅** [applicationDirPath](https://doc.qt.io/qt-5/qcoreapplication.html#applicationDirPath)()。



### [qint64](../../G/QtGlobal/QtGlobal.md) QCoreApplication::applicationPid() [static]

----

返回当前应用程序的进程ID。

此函数自Qt 4.4引入。



---

### [QStringList](../../S/QStringList/QStringList.md) QCoreApplication::arguments() [static]

返回命令行参数列表。

一般情况下，arguments().at(0)表示可执行文件名，arguments().at(1)是第一个参数，arguments().last()是最后一个参数。请见下面关于Windows的注释。

调用这个函数需要花费很多时间——您应该在解析命令行时，将结果缓存起来。

**警告：** 在Unix下，这个参数列表由main()函数中的argc和argv参数生成。argv中的字符串数据将会通过[QString::fromLocal8Bit]()()来解析，因此，在Latin1的区域环境下，是不可能来传递日语的命令行的，其他情况以此类推。大部分现代Unix系统没有此限制，因为它们是基于Unicode的。

在Windows下，这个参数列表，只有在构造函数中传入了修改的argc和argv时，才会从这个argc和argv中解析。这种情况下，就会出现编码问题。

如果不是上述情况，那么arguments()将会从[GetCommandLine()]()中构造。此时arguments().at(0)在Windows下未必是可执行文件名，而是取决于程序是如何被启动的。

此函数自Qt 4.1引入。

**另请参阅** [applicationFilePath]()()和[QCommandLineParser](../../C/QCommandLineParser/QCommandLineParser.md)。



---

### bool QCoreApplication::closingDown() [static]

如果application对象正在被销毁中，则返回true，否则返回false。

**另请参阅** [startingUp]()()。



---

### bool QCoreApplication::event([QEvent](../../E/QEvent/QEvent.md) **e*) [override virtual protected]

重写了：[QObject::event]()(QEvent* e)。



---

### [QAbstractEventDispatcher](../../A/QAbstractEventDispatcher/QAbstractEventDispatcher.md) *QCoreApplication::eventDispatcher() [static]

返回指向主线程事件派发器的指针。如果线程中没有事件派发器，则返回`nullptr`。

**另请参阅** [setEventDispatcher]()()。



---

### int QCoreApplication::exec() [static]

进入主消息循环，直到[exit]()()被调用。其返回值是为[exit]()()传入的那个参数（如果是调用[quit]()()，等效于调用[exit]()(0))。

通过此函数来开始事件循环是很有必要的。主线程事件循环将从窗口系统接收事件，并派发给应用程序下的窗体。

为了能让您的程序在空闲时来处理事件（在没有待处理的事件时，通过调用一个特殊的函数），可以使用一个超时为0的[QTimer](../../T/QTimer/QTimer.md)。可以使用[processEvents]()()来跟进一步处理空闲事件。

我们建议您连接[aboutToQuit]()()信号来做一些清理工作，而不是将它们放在main函数中。因为在某些平台下，exec()可能不会返回。例如，在Windows下，当用户注销时，系统将在Qt关闭所有顶层窗口后才终止进程。因此，不能保证程序有时间退出其消息循环来执行main函数中exec()之后的代码。

**另请参阅** [quit]()()，[exit]()(), [processEvent]()()和[QApplication::exec]()()。



---

### void QCoreApplication::exit(int *returnCode* = 0) [static]

告诉程序需要退出了，并带上一个返回值。

在此函数被调用后，程序将离开主消息循环，并且从[exec]()()中返回。其返回值就是*returnCode*。如果消息循环没有运行，那么此方法什么都不做。

一般我们约定0表示成功，非0表示产生了一个错误。

将信号以[QueuedConnection]()参数连接此槽是一个不错的实践。如果连接了此槽的一个信号（未在队列中的）在控制流程进入主消息循环前（如在int main中调用[exec]()()之前）被发射，那么这个槽不会有任何效果，应用程序也不会退出。使用队列连接方式能保证控制路程进入主消息循环后，此槽才会被触发。

**另请参阅** [quit]()()和[exec]()()。



---

### void QCoreApplication::installNativeEventFilter([QAbstractNativeEventFilter](../../A/QAbstractNativeEventFilter/QAbstractNativeEventFilter.md) **filterObj*)

在主线程为应用程序所能接收到的原生事件安装一个事件过滤器。

事件过滤器*filterObj*通过[nativeEventFilter]()()来接收事件。它可以接收到主线程所有的原生事件。

如果某个原生事件需要被过滤或被屏蔽，那么[QAbstractNativeEventFilter::nativeEventFilter](https://doc.qt.io/qt-5/qabstractnativeeventfilter.html#nativeEventFilter)需要返回true。如果它需要使用Qt默认处理流程，则返回false：那么接下来这个原生事件则会被翻译为一个[QEvent](../../E/QEvent/QEvent.md)，并且由Qt的标准事件过滤器来处理。

如果有多个事件过滤器被安装了，那么最后安装的过滤器将会被最先调用。

**注意：** 此处设置的过滤器功能接收原生事件，即MSG或XCB事件结构。

**注意：** 如果设置了[Qt::AA_PluginApplication]()属性，那么原生事件过滤器将会被屏蔽。

为了最大可能保持可移植性，您应该总是尽可能使用[QEvent](../../E/QEvent/QEvent.md)和[QObject::installEventFilter]()()。

**另请参阅** [QObject::installEventFilter]()()。



---

### bool QCoreApplication::installTranslator([QTranslator](../../T/QTranslator/QTranslator.md) **translationFile*) [static]

将*translationFile*添加到翻译文件列表，它将会被用于翻译。

您可以安装多个翻译文件。这些翻译文件将会按照安装顺序的逆序被搜索到，因此最近添加的翻译文件会首先被搜索到，第一个安装的搜索文件会最后被搜索。一旦翻译文件中匹配了一个字符串，那么搜索就会终止。

安装、移除一个[QTranslator](../../T/QTranslator/QTranslator.md)，或者更改一个已经安装的[QTranslator](../../T/QTranslator/QTranslator.md)将会为[QCoreApplication](./QCoreApplication.md)实例产生一个[LanguageChange]([QEvent](../../E/QEvent/QEvent.md) )事件。一个[QApplication](../../A/QApplication/QApplication.md)会将这个事件派发到所有的顶层窗体，使用[tr]()()来传递用户可见的字符串到对应的属性设置器，通过这种方式来重新实现changeEvent则可以重新翻译用户的界面。通过Qt设计师(Qt Designer)生成的窗体类提供了一个retranslateUi()可以实现上述效果。

函数若执行成功则返回true，失败则返回false。

**另请参阅** [removeTranslator]()()，[translate]()()，[QTranslator::load]()()和[动态翻译]()。



---

### [QCoreApplication](./QCoreApplication.md)* QCoreApplication::instance() [static]

返回程序的[QCoreApplication](./QCoreApplication.md) (或[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md)/[QApplication](../../A/QApplication/QApplication.md))实例的指针。



---

### bool QCoreApplication::isSetuidAllowed() [static]

如果在UNIX平台中，允许应用程序使用setuid，则返回true。

此函数自Qt 5.3引入。

**另请参阅** [QCoreApplication::setSetuidAllowed]()()。



---

### [QStringList](../../S/QStringList/QStringList.md) QCoreApplication::libraryPaths() [static]

返回一个路径列表，其中的路径表示动态加载链接库时的搜索路径。

此函数的返回值也许会在[QCoreApplication](./QCoreApplication.md)创建之后改变，因此不建议在[QCoreApplication](./QCoreApplication.md)创建之前调用。应用程序所在的路径（**非**工作路径），如果是已知的，那么它会被放入列表中。为了能知道这个路径，[QCoreApplication](./QCoreApplication.md)必须要在创建时使用argv[0]来表示此路径。

Qt提供默认的库搜索路径，但是它们同样也可以通过[qt.conf]()文件配置。在此文件中所指定的路径会覆盖默认路径。注意如果qt.conf文件存在于应用程序所在的文件夹目录下，那么直到[QCoreApplication](./QCoreApplication.md)被创建时它才可以被发现。如果它没有被发现，那么调用此函数仍然返回默认搜索路径。

如果插件存在，那么这个列表会包含插件安装目录（默认的插件安装目录是 `INSTALL/plugins`，其中`INSTALL`是Qt所安装的目录。用分号分隔的`QT_PLUGIN_PATH`环境变量中的条目一定会被添加到列表。插件安装目录（以及它存在）在应用程序目录已知时可能会被更改。

如果您想遍历列表，可以使用[foreach]()伪关键字：

```C++
foreach (const QString &path, app.libraryPaths())
    do_something(path);
```

**另请参阅**  [setLibraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#setLibraryPaths)(), [addLibraryPath](https://doc.qt.io/qt-5/qcoreapplication.html#addLibraryPath)(), [removeLibraryPath](https://doc.qt.io/qt-5/qcoreapplication.html#removeLibraryPath)(), [QLibrary](../../L/QLibrary/QLibrary.md) , 以及 [如何创建Qt插件](https://doc.qt.io/qt-5/plugins-howto.html)。



---

### bool QCoreApplication::notify([QObject](../../O/QObject/QObject.md) **receiver*, [QEvent](../../E/QEvent/QEvent.md)* *event*) [virtual]

将事件发送给接收者：*receiver*->event(*event*)。其返回值为接受者的事件处理器的返回值。注意这个函数将会在任意线程中调用，并将事件转发给任意对象。

对于一些特定的事件（如鼠标、键盘事件），如果事件处理器不处理此事件（也就是它返回*false*），那么事件会被逐级派发到对象的父亲，一直派发到顶层对象。

处理事件有5种不同的方式：重写虚函数只是其中一种。所有的五种途径如下所示：

1. 重写[paintEvent]()()，[mousePressEvent]()()等。这个是最通用、最简单但最不强大的一种方法。
2. 重写此函数。这非常强大，提供了完全控制，但是一次只能激活一个子类。
3. 将一个事件过滤器安装到[QCoreApplication](./QCoreApplication.md)。这样的一个事件过滤器可以处理所有窗体的所有事件，就像是重写了notify()函数这样强大。此外，您还可以提供多个应用级别全局的事件过滤器。全局事件过滤器甚至可以接收到那些[不可用窗体]()的鼠标事件。注意程序的事件过滤器仅能响应主线程中的对象。
4. 重写[QObject::event]()()（就像[QWidget](../../W/QWidget/QWidget.md)那样）。如果您是这样做的，您可以接收到Tab按键，及您可以在任何特定窗体的事件过滤器被调用之前接收到事件。
5. 在对象上安装事件过滤器。这样的事件过滤器将可以收到所有事件，包括Tab和Shift+Tab事件——只要它们不更改窗体的焦点。

**未来规划**：在Qt 6中，这个函数不会响应主线程之外的对象。需要该功能的应用程序应同时为其事件检查需求找到其他解决方案。该更改可能会扩展到主线程，因此不建议使用此功能。

**注意**：如果您重写此函数，在您的应用程序开始析构之前，您必须保证所有正在处理事件的线程停止处理事件。这包括了您可能在用的其他库所创建的线程，但是不适用于Qt自己的线程。

**另请参阅**：[QObject::event]()()和[installNativeEventFilter]()()。



---

### void QCoreApplication::postEvent([QObject](../../O/QObject/QObject.md)* *receiver*, [QEvent](../../E/QEvent/QEvent.md)* *event*, int *priority* = Qt::NormalEventPriority) [static]

添加一个*event*事件，其中*receiver*表示事件的接收方。事件被添加到消息队列，并立即返回。

被添加的事件必须被分配在堆上，这样消息队列才能接管此事件，并在它被投送之后删除它。当它被投递之后，再来访问此事件是*不安全*的。

当程序流程返回到了主事件循环时，所有的队列中的事件会通过[notify]()()来发送。

队列中的事件按照*priority*降序排列，这意味着*高优先级*的事件将排列于*低优先级*之前。优先级*priority*可以是任何整数，只要它们在`INT_MAX`和`INT_MIN`之闭区间内。相同优先级的事件会按照投送顺序被处理。

**注意**：此函数是[线程安全]()的。

此函数自Qt 4.3引入。

**另请参阅**：[sendEvent]()()，[notify]()()，[sendPostedEvents]()()，和[Qt::EventPriority]()。



---

### void QCoreApplication::processEvents([QEventLoop::ProcessEventsFlags](https://doc.qt.io/qt-5/qeventloop.html#ProcessEventsFlag-enum) *flags* = QEventLoop::AllEvents) [static]

根据*flags*处理调用线程的所有待处理事件，直到没有事件需要处理。

您可以在您程序进行一项长时间操作的时候偶尔调用此函数（例如拷贝一个文件时）。

如果您在一个本地循环中持续调用这个函数，而不是在消息循环中，那么[DeferredDelete]()事件不会被处理。这会影响到一些窗体的行为，例如[QToolTip](../../T/QToolTip/QToolTip.md)，它依赖[DeferredDelete]()事件。以使其正常运行。一种替代方法是从该本地循环中调用[sendPostedEvents](https://doc.qt.io/qt-5/qcoreapplication.html#sendPostedEvents)()。

此函数只处理调用线程的事件，当所有可处理事件处理完毕之后返回。可用事件是在函数调用之前排队的事件。这意味着在函数运行时投送的事件将会排队到下一轮事件处理为止。

**注意**：此函数是[线程安全]()的。

**另请参阅**：[exec]()()，[QTimer](../../T/QTimer/QTimer.md)，[QEventLoop::processEvents]()()，[flush]()()和[sendPostedEvents]()()。



---

### void QCoreApplication::processEvents([QEventLoop::ProcessEventsFlags](https://doc.qt.io/qt-5/qeventloop.html#ProcessEventsFlag-enum) *flags* = QEventLoop::AllEvents, int *ms*) [static]

此函数重写了processEvents()。

此函数将用*ms*毫秒为调用线程处理待处理的事件，或者直到没有更多事件需要处理。

您可以在您程序进行一项长时间操作的时候偶尔调用此函数（例如拷贝一个文件时）。

此函数只处理调用线程的事件。

**注意**：不像[processEvents]()()的重写，这个函数同样也处理当函数正在运行中时被投送的事件。)，QTimer，QEventLoop::processEvents()。

**另请参阅**：[exec]()()，[QTimer](../../T/QTimer/QTimer.md)，[QEventLoop::processEvents]()()。



---

### void QCoreApplication::removeLibraryPath(const [QString](../../S/QString/QString.md) &*path*) [static]

从库的搜索路径列表中移除*path*。如果*path*是空的，或者不存在于列表，则列表不会改变。

当[QCoreApplication](./QCoreApplication.md)被析构时，此列表会被还原。

**另请参阅**：[exec]()()，[QTimer](../../T/QTimer/QTimer.md)和[QEventLoop::processEvents]()()。



---

### void QCoreApplication::removeNativeEventFilter([QAbstractNativeEventFilter](../../A/QAbstractNativeEventFilter/QAbstractNativeEventFilter.md) **filterObject*)

从此实例中移除*filterObject*事件过滤器。如果这个事件过滤器没有被安装，则什么也不做。

当此实例被销毁时，所有的事件过滤器都会自动被移除。

任何时候——甚至正在事件过滤被激活时（通过nativeEventFilter()函数)——移除一个事件过滤器都是安全的。

此函数自Qt 5.0引入。

**另请参阅**：[installNativeEventFilter]()()。



---

### void QCoreApplication::removePostedEvents([QObject](../../O/QObject/QObject.md) **receiver*, int *eventType* = 0) [static]

移除所指定的 *eventType* 类型且由[postEvent]()()所添加的事件。

这些事件不会被派发，而是直接从队列中移除。您从来都不需要调用此方法。如果您确实调用了它，那么请注意杀掉事件可能会影响 *receiver* 的不变性(invariant)。

如果接收者为`nullptr`，那么所有对象将会移除 *eventType* 所指定的所有事件。如果 *eventType* 为0，那么*receiver*的所有事件将会被移除。自始自终，您都不应将 0 传递给 *eventType* 。

**注意**：此函数是[线程安全]()的。

此函数自Qt 4.3引入。



---

### bool QCoreApplication::removeTranslator([QTranslator]() *translationFile) [static]

从此应用程序使用的翻译文件列表中删除翻译文件 *translationFile* 。 （不会在文件系统中删除此翻译文件。）

该函数成功时返回 true ，失败时返回 false 。

**另请参阅**：[installTranslator()]()，[translate()]()，与 [QObject::tr()]()。



---

### bool QCoreApplication::sendEvent([QObject](../../O/QObject/QObject.md) *receiver, [QEvent]() *event) [static]

通过函数 [notify()]() 将事件 *event* 直接发送至接收对象 *receiver* 。返回从事件处理对象得到的返回值。

事件 *不会* 在发送之后删除掉。通常的方法是在栈上创建事件，例如：

```C++
QMouseEvent event(QEvent::MouseButtonPress, pos, 0, 0, 0);
QApplication::sendEvent(mainWindow, &event);
```

**另请参阅**：[postEvent()]() 与 [notify()]()。



---

### void QCoreApplication::sendPostedEvents([QObject](../../O/QObject/QObject.md) *receiver = nullptr, int event_type = 0) [static]

立刻分派所有先前通过 [QCoreApplication::postEvent()]() 进入队列的事件。这些事件是针对接收对象的，且事件类型为 *event_type* 。

该函数不会对来自窗口系统的事件进行分派，如有需求请参考 [processEvents()]()。

如果接收对象指针为 **nullptr** ，*event_type* 的所有事件将分派到所有对象。如果 *event_type* 为 0 ，所有事件将发送到接收对象 *receiver* 。

**注意：** 该方法必须由其 [QObject](../../O/QObject/QObject.md) 参数 [receiver]() 所在的线程调用。

**另请参阅**：[flush()]() 与 [postEvent()]()。


---

### void QCoreApplication::setAttribute([Qt::ApplicationAttribute]() attribute, bool on = true) [static]

如果 *on* 为 true ，则设置属性 *attribute*；否则清除该属性。

**注意：**在创建 [QCoreApplication]() 实例之前，一些应用程序的属性必须要设置。 有关更多信息，请参考 [Qt::ApplicationAttribute]() 文档。

**另请参阅**：[testAttribute()]()。


---

### void QCoreApplication::setEventDispatcher([QAbstractEventDispatcher]() *eventDispatcher) [static]

将主线程的事件分派器设置为 *eventDispatcher* 。只有在还没有安装事件分派器的情况下，也就是在实例化 [QCoreApplication]() 之前，才可以进行设置。此方法获取对象的所有权。

**另请参阅**：[eventDispatcher()]()。


---

### void QCoreApplication::setLibraryPaths(const [QStringList]() &paths) [static]

将加载库时要搜索的目录列表设置为 *paths*。现有的所有路径将被删除，路径列表将从参数 *paths* 中获取。

当实例 [QCoreApplication]() 被析构时，库路径将设置为默认值。

**另请参阅**：[libraryPaths()]()、[addLibraryPath()]()、[removeLibraryPath()]() 与 [QLibrary]()。



---

### void QCoreApplication::setSetuidAllowed(bool allow) [static]

若 *allow* 为 true，允许程序在 UNIX 平台上运行 setuid 。

若 *allow* 为 false （默认值），且 Qt 检测到程序使用与实际用户id不同的有效用户id运行，那么在创建 QCoreApplication 实例时程序将中止。

Qt 受攻击面较大，因此它并不是一个恰当 setuid 程序解决方案。 不过，出于历史原因，可能某些程序仍需要这种方式运行。 当检测到此标志时，可防止 Qt 中止应用程序。须在创建 QCoreApplication 实例之前将其进行设置。

**注意：**强烈建议不要打开此选项，它会带来安全风险。

此函数自Qt 5.3引入。

**另请参阅**：[isSetuidAllowed()]()。



---

### bool QCoreApplication::startingUp()

如果应用程序对象尚未创建，则返回 **true** ；否则返回 **false** 。

**另请参阅**：[closingDown()]()。



---

### bool QCoreApplication::testAttribute([Qt::ApplicationAttribute]() attribute) [static]

如果设置了属性 *attribute* ，返回 true ；否则返回 false 。

**另请参阅**：[setAttribute()]()。



---

### [QString]() QCoreApplication::translate(const char *context, const char *sourceText, const char *disambiguation = nullptr, int n = -1) [static]

搜索最近到首次安装的翻译文件，查询翻译文件中 sourceText 对应的翻译内容，返回其结果。

[QObject::tr()]() 作用相同且使用更便捷。

*context* 通常为类名（如 "MyDialog"），*sourceText* 则是英文文本或简短的识别文本。

*disambiguation* 为一段识别字符串，用于同一上下文中不同角色使用相同的 *sourceText* 。它的默认值为 **nullptr**。

有关上下文、消除歧义和注释的更多信息，请参阅 [QTranslator]() 和 [QObject::tr()]() 文档。

*n* 与 *%n* 一并使用以便支持复数形式。详见 [QObject::tr()]() 。

如果没有任何翻译文件包含 *context* 中 *sourceText* 的翻译内容，该函数则返回 [QString]() 包裹的 *sourceText* 。

此函数非虚函数。您可以子类化 [QTranslator]() 来使用其他翻译技术。

**注意：**此函数线程安全。

**另请参阅**：[QObject::tr()]()，[installTranslator()]()，[removeTranslator()]()，与 translate()。



## 相关非成员函数

------

### void qAddPostRoutine(QtCleanUpFunction ptr)

添加一个全局例程，它将在  [QCoreApplication]() 析构函数中调用。这个函数通常用来作为在程序范围功能内，添加程序清除例程的函数。

清除例程的调用顺序与添加例程的顺序相反。

参数 *ptr* 指定的函数应既没有参数，也没有返回值，例如：

```C++
static int *global_ptr = nullptr;

static void cleanup_ptr()
{
    delete [] global_ptr;
    global_ptr = nullptr;
}

void init_ptr()
{
    global_ptr = new int[100];      // allocate data
    qAddPostRoutine(cleanup_ptr);   // delete later
}
```

注意，对于应用程序或模块范围的清理，qAddPostRoutine() 通常不太合适。例如，若程序被分割成动态加载的模块，那么相关的模块可能在 [QCoreApplication]() 的析构函数调用之前就卸载了。在这种情况下，如果仍想使用 qAddPostRoutine() ，可以使用 qRemovePostRoutine() 来防止 [QCoreApplication]() 的析构函数调用一个例程。举个例子，在模块卸载前调用 qRemovePostRoutine() 。

对于模块或库，使用引用计数初始化管理器，或者 Qt 对象树删除机制可能会更好。下面是一个私有类使用对象树机制正确调用清除函数的一个例子：

```C++
class MyPrivateInitStuff : public QObject
{
public:
    static MyPrivateInitStuff *initStuff(QObject *parent)
    {
        if (!p)
            p = new MyPrivateInitStuff(parent);
        return p;
    }

    ~MyPrivateInitStuff()
    {
        // cleanup goes here
    }

private:
    MyPrivateInitStuff(QObject *parent)
        : QObject(parent)
    {
        // initialization goes here
    }

    MyPrivateInitStuff *p;
};
```
通过选择正确的父对象，正常情况下可以在正确的时机清理模块的数据。

**注意：** 函数自 Qt 5.10 已线程安全

**注意：** 该函数线程安全

**另请参阅**：[qRemovePostRoutine()]()。



---

### void qRemovePostRoutine(QtCleanUpFunction ptr)

**注意：** 函数自 Qt 5.10 已线程安全

**注意：** 该函数线程安全

此函数自 Qt 5.3 引入。

**另请参阅**：[qAddPostRoutine()]()。




## 宏文档

------

### Q_COREAPP_STARTUP_FUNCTION(QtStartUpFunction ptr)

添加一个全局函数，它将在 [QCoreApplication]() 的构造函数中调用。这个宏通常用于为程序范围内的功能初始化库，无需应用程序调用库进行初始化。

参数 *ptr* 指定的函数应既没有参数，也没有返回值，例如：

```C++
// Called once QCoreApplication exists
static void preRoutineMyDebugTool()
{
    MyDebugTool* tool = new MyDebugTool(QCoreApplication::instance());
    QCoreApplication::instance()->installEventFilter(tool);
}

Q_COREAPP_STARTUP_FUNCTION(preRoutineMyDebugTool)
```
注意，启动函数将在 [QCoreApplication]() 构造后，在任何 GUI 初始化前调用。如果函数中需要GUI代码，请使用计时器(或队列动态调用)，在后面的事件循环中执行初始化。

如果删除了 [QCoreApplication]() 并创建了另一个 [QCoreApplication]() ，将再次调用启动函数。

**注意：**此宏不适用于静态链接到应用程序中的库代码中使用，因为链接器可能会删除该函数，使其根本不会被调用。

**注意：**此函数是[可重入的]()。

此函数自 Qt 5.1 引入。



---

### Q_DECLARE_TR_FUNCTIONS(context)

**Q_DECLARE_TR_FUNCTIONS()** 宏使用以下签名声明并实现了两个转换函数 **tr()** 和 **trUtf8()**：

```C++
static inline QString tr(const char *sourceText,
                         const char *comment = nullptr);
static inline QString trUtf8(const char *sourceText,
                             const char *comment = nullptr);
```

如果您想在不继承 [QObject]() 的类使用 [QObject::tr()]() 或者 QObject::Utf8() ，这个宏就非常适用。

**Q_DECLARE_TR_FUNCTIONS()** 宏必须写在类的第一行（在第一个 public: 或 protected: 之前），例如：

```C++
class MyMfcView : public CView
{
    Q_DECLARE_TR_FUNCTIONS(MyMfcView)

public:
    MyMfcView();
    ...
};
```
通常 *context* 参数为类名，不过也可以是任何文本。

**另请参阅**：[Q_OBJECT]()，[QObject::tr()]()，与 [QObject::trUtf8()]()。

