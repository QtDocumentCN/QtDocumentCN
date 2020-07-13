[TOC]



# QTcpServer Class

QTcpServer 类提供了一个基于 TCP 协议的服务器。

| 属性   | 方法                                              |
| ------ | ------------------------------------------------- |
| 头文件 | \#include <QTcpServer>                            |
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





## 成员函数文档

### **QTcpServer**::QTcpServer([QObject](../../O/QObject) **parent* = nullptr)



### *[SIGNAL]* void **QTcpServer**::acceptError([QAbstractSocket::SocketError](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketerror) *socketError*)



### *[SIGNAL]* void **QTcpServer**::newConnection()



### *[virtual]* **QTcpServer**::~QTcpServer()



### *[protected]* void **QTcpServer**::addPendingConnection([QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) **socket*)



### void **QTcpServer**::close()



### [QString](../../S/QString/QString.md) **QTcpServer**::errorString() const



### *[virtual]* bool **QTcpServer**::hasPendingConnections() const



### *[virtual protected]* void **QTcpServer**::incomingConnection(qintptr*socketDescriptor*)



### bool **QTcpServer**::isListening() const



### bool **QTcpServer**::listen(const [QHostAddress](../../H/QHostAddress/QHostAddress.md) &*address* = QHostAddress::Any, quint16 *port* = 0)



### int **QTcpServer**::maxPendingConnections() const



### *[virtual]* [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) ***QTcpServer**::nextPendingConnection()



### void **QTcpServer**::pauseAccepting()



### [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) **QTcpServer**::proxy() const



### void **QTcpServer**::resumeAccepting()



### [QHostAddress](../../QHostAddress/QHostAddress.md) **QTcpServer**::serverAddress() const



### [QAbstractSocket::SocketError](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketerror) **QTcpServer**::serverError() const



### quint16 **QTcpServer**::serverPort() const



### void **QTcpServer**::setMaxPendingConnections(int *numConnections*)



### void **QTcpServer**::setProxy(const [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) &*networkProxy*)



### bool **QTcpServer**::setSocketDescriptor(qintptr *socketDescriptor*)



### qintptr **QTcpServer**::socketDescriptor() const



### bool **QTcpServer**::waitForNewConnection(int *msec* = 0, bool **timedOut* = nullptr)