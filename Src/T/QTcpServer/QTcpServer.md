[TOC]



# QTcpServer Class

QTcpServer 类提供了一个基于 TCP 协议的服务器。

| 属性   | 方法                                              |
| ------ | ------------------------------------------------- |
| 头文件 | \#include \<QTcpServer\>                          |
| qmake  | QT += network                                     |
| 父类   | [QObject](../../O/QObject/QObject.md)             |
| 子类   | [QSctpServer](../../S/QSctpServer/QSctpServer.md) |

​	**注意：** 该类的所有成员函数都是可重入的。



## 公共成员函数

| 类型                         | 函数名                                                       |
| :--------------------------- | ------------------------------------------------------------ |
|                              | **[ QTcpServer](#qtcpserverqtcpserverqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual                      | **[~QTcpServer](#virtual-qtcpserverqtcpserver)**()           |
| void                         | **[close](#void-qtcpserverclose)**()                         |
| QString                      | **[errorString](#qstring-qtcpservererrorstring-const)**() const |
| virtual bool                 | **[hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)**() const |
| bool                         | **[isListening](#bool-qtcpserverislistening-const)**() const |
| bool                         | **[listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)**(const QHostAddress &*address* = QHostAddress::Any, quint16 *port* = 0) |
| int                          | **[maxPendingConnections](#int-qtcpservermaxpendingconnections-const)**() const |
| virtual QTcpSocket *         | **[nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)**() |
| void                         | **[pauseAccepting](#void-qtcpserverpauseaccepting)**()       |
| QNetworkProxy                | **[proxy](#qnetworkproxy-qtcpserverproxy-const)**() const    |
| void                         | **[resumeAccepting](#void-qtcpserverresumeaccepting)**()     |
| QHostAddress                 | **[serverAddress](#qhostaddress-qtcpserverserveraddress-const)**() const |
| QAbstractSocket::SocketError | **[serverError](#qabstractsocketsocketerror-qtcpserverservererror-const)**() const |
| quint16                      | **[serverPort](#quint16-qtcpserverserverport-const)**() const |
| void                         | **[setMaxPendingConnections](#void-qtcpserversetmaxpendingconnectionsint-numconnections)**(int *numConnections*) |
| void                         | **[setProxy](#void-qtcpserversetproxyconst-qnetworkproxy-networkproxy)**(const QNetworkProxy &*networkProxy*) |
| bool                         | **[setSocketDescriptor](#bool-qtcpserversetsocketdescriptorqintptr-socketdescriptor)**(qintptr *socketDescriptor*) |
| qintptr                      | **[socketDescriptor](#qintptr-qtcpserversocketdescriptor-const)**() const |
| bool                         | **[waitForNewConnection](#bool-qtcpserverwaitfornewconnectionint-msec--0-bool-timedout--nullptr)**(int *msec* = 0, bool **timedOut* = nullptr) |



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[acceptError](#signal-void-qtcpserveraccepterrorqabstractsocketsocketerror-socketerror)**(QAbstractSocket::SocketError *socketError*) |
| void | **[newConnection](#signal-void-qtcpservernewconnection)**()  |



## 保护成员函数

| 类型         | 函数名                                                       |
| :----------- | :----------------------------------------------------------- |
| void         | **[addPendingConnection](#protected-void-qtcpserveraddpendingconnectionqtcpsocket-socket)**(QTcpSocket **socket*) |
| virtual void | **[incomingConnection](#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor)**(qintptr *socketDescriptor*) |





## 详细介绍

这个类使“用Qt编写一个接受 TCP 链接的服务器”的构想成为可能。您可以为 QTcpServer 指定一个端口或者让它自动选一个。您也可以令 QTcpServer 仅监听一个指定的地址或者让它监听这台机器上的所有地址。

调用 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 函数来为到达的连接建立服务器监听。每次当有新的客户端连接到这个服务端时，QTcpServer 都会发出 [newConnection](#signal-void-qtcpservernewconnection)() 信号。

调用 [nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 函数接受一个连接到 QTcpServer 的待处理连接。 该函数会返回一个处于*已连接*（ [*QAbstractSocket::ConnectedState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态的 [QTcpSocket](../QTcpSocket/QTcpSocket.md) ，您可以使用这个 QTcpSocket 与客户端进行通信。

如果发生错误，[serverError](#qabstractsocketsocketerror-qtcpserverservererror-const)() 函数会返回该错误的类型。 您可以调用 [errorString](#qstring-qtcpservererrorstring-const)() 函数来获取一个能让人看懂的错误描述。

当服务器正在监听连接时，服务器所监听的地址和端口可以通过 [serverAddress](#qhostaddress-qtcpserverserveraddress-const)() 和 [serverPort](#quint16-qtcpserverserverport-const)() 函数来获取。

调用 [close](#void-qtcpserverclose)() 函数后 QTcpServer 会停止监听到达的连接。

另外您也可以在 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 类文档和Qt官方给出的 Fortune Server Example ，Threaded Fortune Server Example ，Loopback Example 和 Torrent Example 示例文档中找到相关信息。



## 成员函数文档

### QTcpServer::**QTcpServer**([QObject](../../O/QObject) **parent* = nullptr)

构造函数。构造一个 QTcpServer 对象。

*parent* 参数将传递到 [QObject](../../O/QObject) 的构造函数中。

另外您也可以在 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 和 [setSocketDescriptor](#bool-qtcpserversetsocketdescriptorqintptr-socketdescriptor)() 函数介绍中找到相关介绍。

---

### *[SIGNAL]* void QTcpServer::**acceptError**([QAbstractSocket::SocketError](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketerror) *socketError*)

当接受一个新的连接时出错，QTcpServer 会发送此信号。 *socketError* 参数描述了该错误的类型。

该函数最早在Qt5.0版本引入。

另外您也可以在 [pauseAccepting](#void-qtcpserverpauseaccepting)() 和 [resumeAccepting](#void-qtcpserverresumeaccepting)() 函数介绍中找到相关信息。

---

### *[SIGNAL]* void QTcpServer::**newConnection**()

每当有新的连接可用时，QTcpServer 都会发送该消息。

另外您也可以在 [hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)() 和 [nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 函数介绍中找到相关信息。

---

### *[virtual]* QTcpServer::~**QTcpServer**()

析构函数。销毁 QTcpServer 对象。如果服务器正在监听连接，套接字会自动关闭。

在服务端删除之前，所有仍处于连接状态的客户端 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 都必须断开连接或者重新指定父类。

另外您也可以在 [close](#void-qtcpserverclose)() 函数介绍中找到相关信息。

---

### *[protected]* void QTcpServer::**addPendingConnection**([QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) **socket*)

该函数由 [QTcpServer::incomingConnection()](#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor) 函数调用，作用是添加 *socket* 到待处理连接列表中。

**注意：** 如果您不想破坏连接处理机制，请不要忘记从重新实现的 [incomingConnection()](#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor) 中调用此成员。

该函数最初在Qt4.7版本引入。

另外您也可以在 [incomingConnection](#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor)() 函数介绍中找到相关信息。

---

### void QTcpServer::**close**()

关闭服务器。服务器将不再监听到达的连接。

另外您也可以在 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 函数介绍中找到相关信息。

---

### [QString](../../S/QString/QString.md) QTcpServer::**errorString**() const

将最后一个出现的错误的相关信息按照适合人阅读的形式返回。

另外您也可以在 [serverError](#qabstractsocketsocketerror-qtcpserverservererror-const)() 函数介绍中找到相关信息。

---

### *[virtual]* bool QTcpServer::**hasPendingConnections**() const

当服务端有待处理的连接时该函数返回 true ，否则返回 false 。

另外您也可以在 [nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 和 [setMaxPendingConnections](#void-qtcpserversetmaxpendingconnectionsint-numconnections)() 函数中找到相关信息。

---

### *[virtual protected]* void QTcpServer::**incomingConnection**(qintptr*socketDescriptor*)

当有新的连接到达时， QTcpServer 会调用该虚函数。 *socketDescriptor* 参数是为该连接指定的本机套接字描述符。

对该虚函数重写，您需要进行以下操作：

* 构建一个 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 。
* 设置套接字描述符。
* 将 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 储存在内部的待处理连接列表中。
* 发送 [newConnection](#signal-void-qtcpservernewconnection)() 信号。

重写此函数，以在连接可用时更改服务器的行为。

如果该服务器使用了 [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) ，*socketDescriptor* 可能并不能被本地套接字功能使用，应该仅被 [QTcpSocket::setSocketDescriptor()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) 函数使用。

**注意：** 如果在这个方法中创建了另外一个套接字，该套接字需要通过调用 [addPendingConnection](#protected-void-qtcpserveraddpendingconnectionqtcpsocket-socket)() 函数添加到连接处理机制中。

**注意：** 如果您想在另外一个线程中将到达的连接当作一个新的 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 进行处理，您需要将套接字描述符传递到那个线程中并在那个线程中创建一个 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 对象并使用该该对象的 [setSocketDescriptor()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) 方法。

另外您也可以在 [newConnection](#signal-void-qtcpservernewconnection)() ，[nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 和 [addPendingConnection](#protected-void-qtcpserveraddpendingconnectionqtcpsocket-socket)() 函数介绍中找到相关信息。

---

### bool QTcpServer::**isListening**() const

当服务端正在监听连接时返回 true ，否则返回 false 。

另外您也可以在 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 函数介绍中找到相关信息。

---

### bool QTcpServer::**listen**(const [QHostAddress](../../H/QHostAddress/QHostAddress.md) &*address* = QHostAddress::Any, quint16 *port* = 0)

令服务端监听在 *address* 指定的地址和 *port* 指定的端口上到达的连接。如果 *port* 参数为0 ，QTcpServer 会自动选择一个端口。 如果 *address* 参数为 *QHostAddress::Any* ，服务端会监听所有的网络接口。

操作成功该函数返回 true ，否则返回 false 。

另外您也可以在 [isListening](#bool-qtcpserverislistening-const)() 函数介绍中找到相关信息。

---

### int QTcpServer::**maxPendingConnections**() const

返回最大的待处理的已接受连接数。默认为30。

另外您也可以在 [setMaxPendingConnections](#void-qtcpserversetmaxpendingconnectionsint-numconnections)() 和 [hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)() 函数介绍中找到相关信息。

---

### *[virtual]* [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) *QTcpServer::**nextPendingConnection**()

将下一个待处理的连接作为已连接的 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 对象返回。

该套接字将作为该服务端的子对象创建，这就意味着当 QTcpServer 对象销毁后，该套接字对象也会被销毁。最好在完成处理后显式删除该对象，以避免浪费内存。

如果没有待处理的连接，该函数会返回 `nullptr` 。

**注意：** 返回的 QTcpSocket 对象不能在其他线程中使用。如果您想在其他的线程中使用到达的连接，您需要重写 [incomingConnection](#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor)() 函数。

另外您也可以在 [hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)() 函数介绍中找到相关信息。

---

### void QTcpServer::**pauseAccepting**()

暂停接收新连接。队列连接会保留在队列中。

该函数最初在Qt5.0版本引入。

另外您也可以在 [resumeAccepting](#void-qtcpserverresumeaccepting)() 函数介绍中找到相关信息。

---

### [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) QTcpServer::**proxy**() const

返回该套接字的网络代理。默认将使用 QNetworkProxy::DefaultProxy 。

该函数最初在Qt4.1版本引入。

另外您也可以在 [setProxy](#void-qtcpserversetproxyconst-qnetworkproxy-networkproxy)() 函数介绍和 [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) 文档中找到相关信息。

---

### void QTcpServer::**resumeAccepting**()

恢复接收新连接。

该函数最初在Qt5.0版本引入。

另外您也可以在 [pauseAccepting](#void-qtcpserverpauseaccepting)() 函数介绍中找到相关信息。

---

### [QHostAddress](../../QHostAddress/QHostAddress.md) QTcpServer::**serverAddress**() const

如果服务端正在监听，则返回服务端的地址，否则返回 QHostAddress::Null 。

另外您也可以在 [serverPort](#quint16-qtcpserverserverport-const)() 和 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 函数介绍中找到相关信息。

---

### [QAbstractSocket::SocketError](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketerror) QTcpServer::**serverError**() const

返回最后出现的错误的代码。

另外您也可以在 [errorString](#qstring-qtcpservererrorstring-const)() 函数介绍中找到相关信息。

---

### quint16 QTcpServer::**serverPort**() const

如果服务端正在监听，则返回服务端的端口，否则返回 0 。

另外您也可以在 [serverAddress](#qhostaddress-qtcpserverserveraddress-const)() 和 [listen](#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 函数介绍中找到相关信息。

---

### void QTcpServer::**setMaxPendingConnections**(int *numConnections*)

设置待处理的已接受连接的数目最大值为 *numConnections* 。超过该数目后，在调用 [nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 函数之前， QTcpServer 将不会再接收到达的连接。默认情况下，QTcpServer接收连接的最大值为30。

服务器达到其最大待处理连接数后，客户端仍然可以连接（即 [QTcpSocket](../QTcpSocket/QTcpSocket.md) 仍可以发出 connected() 信号）。 QTcpServer 将停止接受新连接，但是操作系统仍可以将它们保持在队列中。

另外您也可以在 [maxPendingConnections](#int-qtcpservermaxpendingconnections-const)() 和 [hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)() 函数介绍中找到相关信息。

---

### void QTcpServer::**setProxy**(const [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) &*networkProxy*)

显式设置该套接字的网络代理为 *networkProxy* 。

您通过设置使用 QNetworkProxy::NoProxy 代理类型来禁止套接字使用代理：

```cpp
 server->setProxy(QNetworkProxy::NoProxy);
```

该函数最初在Qt4.1版本时引入。

另外您也可以在 [proxy](#qnetworkproxy-qtcpserverproxy-const)() 函数介绍和 [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) 文档中找到相关信息。

---

### bool QTcpServer::**setSocketDescriptor**(qintptr *socketDescriptor*)

设置该服务端监听连接时使用的套接字描述符为 *socketDescriptor* 。当操作成功时返回 true ，否则返回 false 。

调用该函数时，服务端应该处于正在监听的状态。

另外您也可以在 [socketDescriptor](#qintptr-qtcpserversocketdescriptor-const)() 和 [isListening](#bool-qtcpserverislistening-const)() 函数介绍中找到相关信息。

---

### qintptr QTcpServer::**socketDescriptor**() const

返回服务端监听连接时使用的套接字描述符，如果该服务器未处于监听状态返回-1。

如果服务器正在使用 [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) ，返回的套接字描述符可能并不能在本地套接字函数中使用。

另外您也可以在 [setSocketDescriptor()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite)() 和 [isListening](#bool-qtcpserverislistening-const)() 函数介绍中找到相关信息。

---

### bool QTcpServer::**waitForNewConnection**(int *msec* = 0, bool **timedOut* = nullptr)

等待 *msec* 毫秒或者直到有新的连接接入。如果有新的连接，该函数返回 true ， 否则返回 false 。如果 *timeOut* 参数不为 `nullptr` 并且操作超时， *\*timeOut* 将被设置为 true 。

这是一个可以引起阻塞的函数。不推荐在一个单线程的 GUI 程序中使用该函数，因为使用该函数后直到该函数返回之前整个应用程序会停止响应。 waitForNewConnection() 函数通常在没有事件循环的情况下使用。

不阻塞应用程序的可选方案是使用 [newConnection](#signal-void-qtcpservernewconnection)() 信号。

如果 *msec* 参数设置为-1，该函数将不会超时。

另外您也可以在 [hasPendingConnections](#virtual-bool-qtcpserverhaspendingconnections-const)() 和 [nextPendingConnection](#virtual-qtcpsocket-qtcpservernextpendingconnection)() 函数介绍中找到相关信息。
