

# **QX11Info**

 **提供有关X11相关的相关配置信息（就是linux下的x11相关的配置信息）**
----------
 
|  属性  | 方法|
|------:|:------|
|头文件:| `#include<QX11Info>`|
| qmake: | QT += x11extras |
| Since: | Qt 5.1 |

----------
 
## **简述**
----------
 
### **Public Functions**
 
|  类型  | 函数名|
|------:|:------|
| int | **[appDpiX](http://doc.qt.io/qt-5.9/qx11info.html#appDpiX)**(int _screen_ = -1) |
| int | **[appDpiY](http://doc.qt.io/qt-5.9/qx11info.html#appDpiY)**(int _screen_ = -1) |
| unsigned long | **[appRootWindow](http://doc.qt.io/qt-5.9/qx11info.html#appRootWindow)**(int _screen_ = -1) |
| int | **[appScreen](http://doc.qt.io/qt-5.9/qx11info.html#appScreen)**() |
| unsigned long | **[appTime](http://doc.qt.io/qt-5.9/qx11info.html#appTime)**() |
| unsigned long | **[appUserTime](http://doc.qt.io/qt-5.9/qx11info.html#appUserTime)**() |
| xcb_connection_t * | **[connection](http://doc.qt.io/qt-5.9/qx11info.html#connection)**() |
| Display * | **[display](http://doc.qt.io/qt-5.9/qx11info.html#display)**() |
| unsigned long | **[getTimestamp](http://doc.qt.io/qt-5.9/qx11info.html#getTimestamp)**() |
| bool | **[isCompositingManagerRunning](http://doc.qt.io/qt-5.9/qx11info.html#isCompositingManagerRunning)**(int _screen_ = -1) |
| bool | **[isPlatformX11](http://doc.qt.io/qt-5.9/qx11info.html#isPlatformX11)**() |
| QByteArray | **[nextStartupId](http://doc.qt.io/qt-5.9/qx11info.html#nextStartupId)**() |
| void | **[setAppTime](http://doc.qt.io/qt-5.9/qx11info.html#setAppTime)**(unsigned long _time_) |
| void | **[setAppUserTime](http://doc.qt.io/qt-5.9/qx11info.html#setAppUserTime)**(unsigned long _time_) |
| void | **[setNextStartupId](http://doc.qt.io/qt-5.9/qx11info.html#setNextStartupId)**(const QByteArray &_id_) |
 

----------
 
## **详细说明**

该类提供了关于 x window相关的显式配置信息

该类提供了两类API：一种是提供特定的widget或者特定的pixmap相关的非静态函数，一种是为应用程序提供默认信息的静态函数。(这个分类简直了！！！)

----------

## **成员函数**

### int QX11Info::appDpiX(int _screen_ = -1) static函数

返回指定屏幕的水平分辨率。

参数screen是指哪个x屏幕（比如两个的话，第一个就是0，第二个就是1）。请注意，如果用户使用的系统是指Xinerama（而不是传统的x11多屏幕），则只有一个x屏幕。请使用[<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QDesktopWidget</font></font>](http://doc.qt.io/qt-5.9/qdesktopwidget.html)来查询有关于Xinerama屏幕的信息。

另参阅apDipY();

-------

### int QX11Info::appDpiY(int _screen_ = -1)  static函数

返回指定屏幕的垂直分辨率。

参数screen是指哪个x屏幕（比如两个的话，第一个就是0，第二个就是1）。请注意，如果用户使用的系统是指Xinerama（而不是传统的x11多屏幕），则只有一个x屏幕。请使用[<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QDesktopWidget</font></font>](http://doc.qt.io/qt-5.9/qdesktopwidget.html)来查询有关于Xinerama屏幕的信息。

另参阅apDipX();

------

### unsigned long QX11Info::appRootWindow(int _screen_ = -1)  static函数
返回指定屏幕应用程序窗口的句柄

参数screen是指哪个x屏幕（比如两个的话，第一个就是0，第二个就是1）。请注意，如果用户使用的系统是指Xinerama（而不是传统的x11多屏幕），则只有一个x屏幕。请使用[<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QDesktopWidget</font></font>](http://doc.qt.io/qt-5.9/qdesktopwidget.html)来查询有关于Xinerama屏幕的信息。

------
### int QX11Info::appScreen() static函数
返回应用程序正在显示的屏幕编号。
此方法是指每个原始的X11屏幕使用不同的DISPLAY环境变量。只有当您的应用程序需要知道它在哪个X屏幕上运行时，这个信息才有用。
在典型的多个物理机连接到一个X11屏幕中时。意味着这个方法对于每台物理机来讲都是相同的编号。在这样的设置中，如果您对X11的RandR拓展程序感兴趣，可以通过[<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QDesktopWidget</font></font>](http://doc.qt.io/qt-5.9/qdesktopwidget.html)和[<font style="vertical-align: inherit;">QScreen</font>](http://doc.qt.io/qt-5.9/qdesktopwidget.html)</font>获得。

-------
### unsigned long QX11Info::appTime() static函数
返回X11的时间

------
### unsigned long QX11Info::appUserTime() static函数
返回X11的用户时间

------
### xcb_connection_t *QX11Info::connection() static函数

返回应用程序默认的XCB信息。

------
### Display *QX11Info::display() static函数

返回应用程序默认的显式屏幕

------
### unsigned long QX11Info::getTimestamp() static函数
从X服务器上获取当前X11的时间戳。
此方法创建一个事件来阻塞住X11服务器，直到它从X服务器接受回来。
这个函数是从Qt5.2中引入的。

------
### bool QX11Info::isCompositingManagerRunning(int _screen_ = -1) static函数
如果屏幕的合成管理器在运行时，则返回 true (ps,合成管理器运行会有一些特殊的效果，比如一些透明色的绘制，可以用这个函数判断下。)，否则则返回 false。
这个函数是从Qt5.7中引入的。

------
### bool QX11Info::isPlatformX11() static函数
如果应用程序运行在X11上则返回true。
这个函数是从Qt5.2开始引入的。

------
### [QByteArray](http://doc.qt.io/qt-5.9/qbytearray.html) QX11Info::nextStartupId()
返回此进程显式的下一个窗口的启动ID。
显式下一个窗口后，下一个启动ID则为空。

（Qt官网很少给这种链接啊）
http://standards.freedesktop.org/startup-notification-spec/startup-notification-latest.txt

这个函数在Qt5.4引入。

------

### void QX11Info::setAppTime(unsigned long _time_) static函数
将X11时间设置成指定的值。

------

### void QX11Info::setAppUserTime(unsigned long _time_) static函数
设置X11用户的时间


------
### void QX11Info::setNextStartupId(const [QByteArray](http://doc.qt.io/qt-5.9/qbytearray.html) &_id_) static函数
设置下一个启动程序的ID。
第一个窗口的启动ID来自环境变量DESKTOP_STARTUP_ID。当请求来自另一个进程(比如通过QDus)时，此方法对于后续窗口很有用。

这个函数是从Qt5.4中引用的。
