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
|                              | **[ QTcpServer](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#QTcpServer)**(QObject **parent* = nullptr) |
| virtual                      | **[~QTcpServer](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#dtor.QTcpServer)**() |
| void                         | **[close](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#close)**() |
| QString                      | **[errorString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#errorString)**() const |
| virtual bool                 | **[hasPendingConnections](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#hasPendingConnections)**() const |
| bool                         | **[isListening](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#isListening)**() const |
| bool                         | **[listen](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#listen)**(const QHostAddress &*address* = QHostAddress::Any, quint16 *port* = 0) |
| int                          | **[maxPendingConnections](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#maxPendingConnections)**() const |
| virtual QTcpSocket *         | **[nextPendingConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#nextPendingConnection)**() |
| void                         | **[pauseAccepting](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#pauseAccepting)**() |
| QNetworkProxy                | **[proxy](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#proxy)**() const |
| void                         | **[resumeAccepting](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#resumeAccepting)**() |
| QHostAddress                 | **[serverAddress](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#serverAddress)**() const |
| QAbstractSocket::SocketError | **[serverError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#serverError)**() const |
| quint16                      | **[serverPort](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#serverPort)**() const |
| void                         | **[setMaxPendingConnections](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#setMaxPendingConnections)**(int *numConnections*) |
| void                         | **[setProxy](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#setProxy)**(const QNetworkProxy &*networkProxy*) |
| bool                         | **[setSocketDescriptor](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#setSocketDescriptor)**(qintptr *socketDescriptor*) |
| qintptr                      | **[socketDescriptor](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#socketDescriptor)**() const |
| bool                         | **[waitForNewConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#waitForNewConnection)**(int *msec* = 0, bool **timedOut* = nullptr) |



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[acceptError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#acceptError)**(QAbstractSocket::SocketError *socketError*) |
| void | **[newConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#newConnection)**() |



## 保护成员函数

| 类型         | 函数名                                                       |
| :----------- | :----------------------------------------------------------- |
| void         | **[addPendingConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#addPendingConnection)**(QTcpSocket **socket*) |
| virtual void | **[incomingConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#incomingConnection)**(qintptr *socketDescriptor*) |





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