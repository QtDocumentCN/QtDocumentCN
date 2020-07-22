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

翻译文件能分别通过installTranslator()和removeTranslator()被加载和移除。您可以通过translate()来翻译应用中的字符串。QObject::tr()和QObject::trUtf8()这两个函数根据translate()来进行了实现。



## 访问命令行参数

您应该通过arguments()来获取传递给QCoreApplication构造函数的命令行参数。

注：QCoreApplication将移除**-qmljsdebugger="..."**选项。它会解析**qmljsdebugger**参数，然后删除此选项及其参数。

对于一些更加高级的命令行参数的处理，请创建一个[QCommandLineParser](../QCommandLineParser/QCommandLineParser.md)。



## 区域设置

运行在Unix/Linux的Qt程序，将会默认使用系统的区域设置。这可能会导致在使用POSIX函数时发生冲突，例如，数据类型转换时由转换浮点数转换为字符串，由于不同区域符号的差异可能会导致一些冲突。为了解决这个问题，在初始化[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md)、[QApplication](../../A/QApplication/QApplication.md)或QCoreApplication之后，需要马上调用POSIX函数**setlocale(LC_NUMERIC, "C")**，以重新将数字的格式设置为"C"-locale。

另请参阅[QGuiApplication](../../G/QGuiApplication/QGuiApplication.md), [QAbstractEventDispatcher](../../A/QAbstractEventDispatcher/QAbstractEventDispatcher.md), [QEventLoop](../../E/QEventLoop/QEventLoop.md), [Semaphores Example](../../S/Semaphorse Example/Semaphores Example.md), 以及[Wait Conditions Example](../../W/Wait Conditions Example/Wait Conditions Example.md)。



## 属性文档

### applicationName : [QString](../../S/QString/QString.md)

此属性持有应用程序的名字。

当使用空的构造函数初始化QSettings类的实例时，此字段被使用。这样一来，每次创建[QSettings](../../S/QSettings/QSettings.md)对象时，都不必重复此信息。

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