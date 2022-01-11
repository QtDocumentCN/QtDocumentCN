[TOC]



# QSctpServer Class

QSctpServer 提供了一个基于 QSCTP 协议的服务器。

| 属性     | 方法                                           |
| -------- | ---------------------------------------------- |
| 头文件   | `#include <QSctpServer>`                        |
| qmake    | QT += network                                  |
| 引入版本 | Qt5.8                                          |
| 继承自   | [QTcpServer](../../T/QTcpServer/QTcpServer.md) |

该类最初在 Qt5.8 版本时引入。



## 公共成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
|              | **[QSctpServer](#qsctpserverqsctpserverqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual      | **[~QSctpServer](#virtual-qsctpserverqsctpserver)**()        |
| int          | **[maximumChannelCount](#int-qsctpservermaximumchannelcount-const)**() const |
| QSctpSocket* | **[nextPendingDatagramConnection](#qsctpsocket-qsctpservernextpendingdatagramconnection)**() |
| void         | **[setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)**(int *count*) |



## 重写保护成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | **[incomingConnection](#override-virtual-protected-void-qsctpserverincomingconnectionqintptr-socketdescriptor)**(qintptr *socketDescriptor*) override |



## 详细介绍

SCTP（流控制传输协议）是一种传输层协议，其作用与流行的协议 TCP 和 UDP 类似。像 UDP 一样，SCTP 也是面向消息的，但是它可以通过与 TCP 类似的拥塞控制来确保消息的可靠性，让消息按顺序传输。您可以在 [QSctpSocket](../QSctpSocket/QSctpSocket.md) 类文档中找到关于 SCTP 协议的更多的信息。

QSctpServer 是 QTcpServer 的便利子类，它允许您以 TCP 模拟或数据报模式接受传入的 SCTP 套接字连接。

QSctpServer 最常见的用法是构造一个 QSctpServer 类的对象并调用 [setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)() 函数设置该服务器准备支持的最大通道数。您可以在调用 [setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)() 函数时传入一个负值，这样便可以让服务端在 TCP 模拟模式下运行。另外，如果在 [setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)() 函数调用时传入0（0也是默认值），这会指定服务端使用对等端设置的最大通道数目。新的传入连接从服务器套接字描述符继承此数字，并根据远程端点设置对其进行调整。

在 TCP 模拟模式下，服务端允许客户端使用一条连续的字节流来进行数据传输。此时 QSctpSocket 的操作模式与普通的 [QTcpServer](../../T/QTcpServer/QTcpServer.md) 类似。您可以调用 [nextPendingConnection()](../../T/QTcpServer/QTcpServer.md#virtual-qtcpsocket-qtcpservernextpendingconnection) 函数将一个待处理的连接作为一个已连接的 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 套字节来接受。您可以使用该 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 套接字与客户端进行通信。此模式仅能使用基本的 SCTP 协议功能。套接字在系统层面通过 IP 传输 SCTP 数据包，并通过 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 接口与应用程序进行交互。

与 TCP 模拟模式相反，数据报模式是面向消息的，并且在端点之间提供了多个数据流的完全同时传输。您可以调用 [nextPendingDatagramConnection()](#qsctpsocket-qsctpservernextpendingdatagramconnection) 函数将待处理的数据报模式的连接作为一个已连接的 [QSctpSocket](../QSctpSocket/QSctpSocket.md) 套接字接受。

**注意：** WIndows系统不支持该特性。

另外您也可以在 [QTcpServer](../../T/QTcpServer/QTcpServer.md) ，[QSctpSocket](../QSctpSocket/QSctpSocket.md) 和 [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) 类文档中找到相关信息。



## 成员函数文档

### QSctpServer::**QSctpServer**([QObject](../../O/QObject/QObject.md) **parent* = nullptr)

构造函数。构造一个 QSctpServer 类型的对象并将其设置为数据报模式。

*parent* 参数将传递到 [QObject](../../O/QObject/QObject.md) 构造函数中。

另外您也可以在 [setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)() ，[listen](../../T/QTcpServer/QTcpServer.md#bool-qtcpserverlistenconst-qhostaddress-address--qhostaddressany-quint16-port--0)() 和 [setSocketDescriptor](../../T/QTcpServer/QTcpServer.md#bool-qtcpserversetsocketdescriptorqintptr-socketdescriptor)() 函数介绍中找到相关信息。

---

### *[virtual]* QSctpServer::~**QSctpServer**()

析构函数。销毁 QSctpServer 类型的对象。如果服务端仍然在监听客户端连接，该套接字会自动关闭。

另外您也可以在 [close](../../T/QTcpServer/QTcpServer.md#void-qtcpserverclose)() 函数介绍中找到相关信息。

---

### *[override virtual protected]* void QSctpServer::**incomingConnection**(qintptr *socketDescriptor*)

重写 [QTcpServer::incomingConnection(qintptr socketDescriptor)](../../T/QTcpServer/QTcpServer.md#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor) 函数。

---

### int QSctpServer::**maximumChannelCount**() const

返回套接字能够支持的最大通道数。

如果返回值为0（默认值）意味着支持的最大通道数将由远程端点设置。

如果 QSctpServer 运行在 TCP 模拟模式，该函数返回-1。

另外您也可以在 [setMaximumChannelCount](#void-qsctpserversetmaximumchannelcountint-count)() 函数介绍中找到相关信息。

---

### [QSctpSocket](../QSctpSocket/QSctpSocket.md) *QSctpServer::**nextPendingDatagramConnection**()

将下一个待处理的数据报模式的连接作为一个已连接的 [QSctpSocket](../QSctpSocket/QSctpSocket.md) 对象返回。

数据报模式的连接提供了一个面向消息的、多数据流的通信。

该返回的套接字将作为服务端的子类创建，这意味着当 QSctpServer 对象销毁时，该套接字也将销毁。当您使用完一个对象后显式地删除该对象是一个好的做法，这能避免浪费内存。

如果没有待处理的数据报模式的连接，该函数将返回空。

**注意：** 返回的 QSctpSocket 对象不能被其他线程使用。如果想在其他线程中使用到达的连接，您需要重写 [incomingConnection](#override-virtual-protected-void-qsctpserverincomingconnectionqintptr-socketdescriptor)() 函数。

另外您也可以在 [hasPendingConnections](../../T/QTcpServer/QTcpServer.md#virtual-bool-qtcpserverhaspendingconnections-const)() ，[nextPendingConnection](../T/QTcpServer/QTcpServer.md#virtual-qtcpsocket-qtcpservernextpendingconnection)() 函数介绍和 [QSctpSocket](../QSctpSocket/QSctpSocket.md) 类文档中找到相关信息。

---

### void QSctpServer::**setMaximumChannelCount**(int *count*)

设置在数据报模式下服务端准备支持的最大通道数为 *count* 。

如果 *count* 为0，服务端将使用其他端点的最大通道数。

如果 *count* 为一个负值，则 QSctpServer 将会在 TCP 模拟模式下运行。

另外您也可以在 [maximumChannelCount](#int-qsctpservermaximumchannelcount-const)() 函数介绍和 [QSctpSocket](../QSctpSocket/QSctpSocket.md) 类文档中找到相关信息。

