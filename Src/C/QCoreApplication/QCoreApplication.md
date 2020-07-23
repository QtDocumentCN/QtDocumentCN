Reserved by froser until 2020-08-15

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

此属性在Qt 4.4中引入。

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

### QCoreApplication::QCoreApplication(int &*argc*, char ***argv*)

------

构造一个Qt内核程序。所谓内核程序，就是没有图形用户界面的程序。这样的程序使用控制台，或者是作为服务进程运行着。

*argc*和*argv*参数将会被应用程序处理，将其转换为一种更加便捷的形式，并可以通过[arguments]()()来获取。

**警告**：*argc*和*argv*这两个值所指向的内存，必须在整个QCoreApplication生命周期内有效。另外，*agrc*必须要大于0，且*argv*必须至少包含一个合法的字符串。



### void QCoreApplication::aboutToQuit() [signal]

-------------

当程序即将退出主消息循环时，如当消息循环嵌套层数降为0时，此事件被发射。它可能发生在应用程序中调用[quit]()()之后，亦发生在关闭整个桌面会话时。

注意：这是一个私有信号。它能够被连接，但是用户无法发射它。

**另请参阅** [quit](https://doc.qt.io/qt-5/qcoreapplication.html#quit)()。





### void QCoreApplication::quit() [static slot]

-----------

告知程序以返回值0来退出。等效于调用 [QCoreApplication::exit]()(0)。

一般我们将quit()槽连接到[QGuiApplication::lastWindowClosed]()()信号，您同样可以将此槽连接到[QAction](../../A/QAction/QAction.md)、[QMenu](../../M/QMenu/QMenu.md)或[QMenuBar](../../M/QMenuBar/QMenuBar.md)的[QAbstractButton::clicked]()()信号上。

将信号以[QueuedConnection]()参数连接此槽是一个不错的实践。如果连接了此槽的一个信号（未在队列中的）在控制流程进入主消息循环前（如在int main中调用[exec]()()之前）被发射，那么这个槽不会有任何效果，应用程序也不会退出。使用队列连接方式能保证控制路程进入主消息循环后，此槽才会被触发。

例如：

```C++
QPushButton *quitButton = new QPushButton("Quit");
connect(quitButton, &QPushButton::clicked, &app, &QCoreApplication::quit, Qt::QueuedConnection);
```

**另请参阅** [exit](https://doc.qt.io/qt-5/qcoreapplication.html#exit)(), [aboutToQuit](https://doc.qt.io/qt-5/qcoreapplication.html#aboutToQuit)(), and [QGuiApplication::lastWindowClosed](https://doc.qt.io/qt-5/qguiapplication.html#lastWindowClosed)()。



### QCoreApplication::~QCoreApplication() [virtual]

----------

销毁[QCoreApplication](./QCoreApplication.md)对象。



### void QCoreApplication::addLibraryPath(const [QString](../../S/QString/QString.md) &*path*) [static]

-----

将*path*添加到库路径开头，保证它先会被库搜索到。如果*path*为空或者已经存在于路径列表，那么路径列表保持不变。

默认的路径列表只包含一个条目，即插件安装路径。默认的插件安装文件夹是`INSTALL/plugins`，其中`INSTALL`是Qt安装文件夹。

当[QCoreApplication](./QCoreApplication.md)被销毁后，这些库路径将会被重设为默认值。

**另请参阅** [removeLibraryPath](https://doc.qt.io/qt-5/qcoreapplication.html#removeLibraryPath)(), [libraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#libraryPaths)(), and [setLibraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#setLibraryPaths)().



### [QString](../../S/QString/QString.md) QCoreApplication::applicationDirPath() [static]

----

返回包含此可执行文件的文件夹路径。

例如，您已经在`C:\Qt`安装了Qt，然后运行`regexp`示例，那么这个函数会返回"C:/Qt:/examples/tools/regexp"。

在macOS和iOS上，它会指向实际包含可执行文件的目录，该目录可能在一个应用程序包内（如果是以应用程序包形式存在）。

**警告**：在Linux上，这个函数会尝试从`/proc`获取文件路径。如果失败了，那么它假设`argv[0]`包含了可执行文件的绝对路径。此函数同样也假设了应用程序不会改变当前路径。

**另请参阅** [applicationFilePath](https://doc.qt.io/qt-5/qcoreapplication.html#applicationFilePath)()。



### [QString](../../S/QString/QString.md) QCoreApplication::applicationFilePath() [static]

----

返回包含此可执行文件的文件路径。

例如，您已经在`/usr/local/qt`目录安装了Qt，然后运行`regexp`示例，那么这个函数会返回"/usr/local/qt/examples/tools/regexp/regexp"。

**警告**：在Linux上，这个函数会尝试从`/proc`获取文件路径。如果失败了，那么它假设`argv[0]`包含了可执行文件的绝对路径。此函数同样也假设了应用程序不会改变当前路径。

**另请参阅** [applicationDirPath](https://doc.qt.io/qt-5/qcoreapplication.html#applicationDirPath)()。



### [qint64](../../G/QtGlobal/QtGlobal.md) QCoreApplication::applicationPid() [static]

----

返回当前应用程序的进程ID。

此函数在Qt 4.4中引入。

