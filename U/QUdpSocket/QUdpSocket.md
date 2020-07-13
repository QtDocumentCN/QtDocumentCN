[TOC]



# QUdpSocket Class

QUdpSocket 类提供了 UDP 类型的套接字。

| 属性   | 方法                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | \#include <QUdpSocket>                                       |
| qmake  | QT += network                                                |
| 基类   | [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) |

​    **注意：** 该类提供的所有函数都是可重入的。



## 公共成员函数

| 类型              | 函数名                                                       |
| ----------------- | ------------------------------------------------------------ |
|                   | [QUdpSocket(QObject **parent* = nullptr)](#qudpsocketqudpsocketqobject-parent--nullptr) |
| virtual           | [~QUdpSocket()](#virtual-qudpsocketqudpsocket)               |
| bool              | [hasPendingDatagrams() const](#bool-qudpsockethaspendingdatagrams-const) |
| bool              | [joinMulticastGroup(const QHostAddress &*groupAddress*)](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) |
| bool              | [joinMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress-const-qnetworkinterface-iface) |
| bool              | [leaveMulticastGroup(const QHostAddress &*groupAddress*)](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress) |
| bool              | [leaveMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress-const-qnetworkinterface-iface) |
| QNetworkInterface | [multicastInterface() const](#qnetworkinterface-qudpsocketmulticastinterface-const) |
| qint64            | [pendingDatagramSize() const](#qint64-qudpsocketpendingdatagramsize-const) |
| qint64            | [readDatagram(char \**data*, qint64 *maxSize*, QHostAddress \**address* = nullptr, quint16 \**port* = nullptr)](#qint64-qudpsocketreaddatagramchar-data-qint64-maxsize-qhostaddress-address--nullptr-quint16-port--nullptr) |
| QNetworkDatagram  | [receiveDatagram(qint64 *maxSize* = -1)](#qnetworkdatagram-qudpsocketreceivedatagramqint64-maxsize---1) |
| void              | [setMulticastInterface(const QNetworkInterface &*iface*)](#void-qudpsocketsetmulticastinterfaceconst-qnetworkinterface-iface) |
| qint64            | [writeDatagram(const char **data*, qint64 *size*, const QHostAddress &*address*, quint16 *port*)](#qint64-qudpsocketwritedatagramconst-char-data-qint64-size-const-qhostaddress-address-quint16-port) |
| qint64            | [writeDatagram(const QNetworkDatagram &*datagram*)](#qint64-qudpsocketwritedatagramconst-qnetworkdatagram-datagram) |
| qint64            | [writeDatagram(const QByteArray &*datagram*, const QHostAddress &*host*, quint16 *port*)](qint64-qudpsocketwritedatagramconst-qbytearray-datagram-const-qhostaddress-host-quint16-port) |



## 详细描述

UDP（用户数据报协议）是一种轻量级，不可靠，面向数据报的无连接协议。 当在数据传输的可靠性不重要时您可以选择使用它。 QUdpSocket 是 [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) 的子类，可让您发送和接收UDP数据报。

​    使用此类的最常见方法是使用 [bind()](../../A/QAbstractSocket/QAbstractSocket.md#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 绑定到地址和端口，然后调用 [writeDatagram()](#qint64-qudpsocketwritedatagramconst-char-data-qint64-size-const-qhostaddress-address-quint16-port) 和 [readDatagram()](#qint64-qudpsocketreaddatagramchar-data-qint64-maxsize-qhostaddress-address--nullptr-quint16-port--nullptr) 或 [receiveDatagram()](#qnetworkdatagram-qudpsocketreceivedatagramqint64-maxsize---1) 来传输数据。 如果要使用标准 [QIODevice](../../I/QIODevice/QIODevice.md) 函数 read() ，readLine() ，write() 等，则您必须首先通过调用 [connectToHost()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol) 将套接字直接连接到对等方。

​    每次将数据报写入网络后，套接字都会发出 bytesWritten() 信号。 如果只想发送数据报，则不需要调用 [bind()](../../A/QAbstractSocket/QAbstractSocket.md#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 。

​    每次有数据报到达时，套接字都会发出 readyRead() 信号。 在有新数据报到达时，成员函数 [hasPendingDatagrams()](#bool-qudpsockethaspendingdatagrams-const) 的返回值为真。您可以调用 [pendingDatagramSize()](#qint64-qudpsocketpendingdatagramsize-const) 获得第一个待处理的数据报的大小。 

​    **注意：** 当您收到 readyRead() 信号时必须将到达的数据报读入，否则在接下来新的数据报到达后不会将发送 readyRead() 信号。

​    Qt官方示例如下：

```cpp
 void Server::initSocket()
 {
     udpSocket = new QUdpSocket(this);
     udpSocket->bind(QHostAddress::LocalHost, 7755);

     connect(udpSocket, &QUdpSocket::readyRead,
             this, &Server::readPendingDatagrams);
 }

 void Server::readPendingDatagrams()
 {
     while (udpSocket->hasPendingDatagrams()) {
         QNetworkDatagram datagram = udpSocket->receiveDatagram();
         processTheDatagram(datagram);
     }
 }
```

​    QUdpSocket 还支持 UDP 多播功能。您可以使用 [joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 和 [LeaveMulticastGroup()](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress) 函数来控制组成员身份，并使用 [QAbstractSocket :: MulticastTtlOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) 和 [QAbstractSocket :: MulticastLoopbackOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) 来设置 TTL 和回送套接字选项。您也可以使用 [setMulticastInterface()](#void-qudpsocketsetmulticastinterfaceconst-qnetworkinterface-iface) 函数控制多播数据报的传出接口，并使用 [multicastInterface()](#qnetworkinterface-qudpsocketmulticastinterface-const) 函数来查询传出接口。

​    使用 QUdpSocket 时，你可以使用 [connectToHost()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol) 函数建立一个虚拟连接到 UDP 服务器。虚拟连接建立后，您可以用 read() 和 write() 函数来交换数据报而不用指定每个数据报的接收者。

​    Qt官方提供了如下几个在您的应用中使用 QUdpSocket 的示例： Broadcast Sender，Broadcast Receiver， Multicast Sender 和  Multicast Receiver。

​    您也可以在 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 和 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) 文档中找到相关信息。

## 成员函数文档

### **QUdpSocket**::QUdpSocket(QObject **parent* = nullptr)

构造函数。构造一个 QUdpSocket 类型的对象。

​    将 *parent* 参数传递到 [QObject](../../O/QObject/QObject.md) 构造函数。

​    另外您也可以在 [socketType()](../../A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const) 中找到相关信息。



### *[virtual]* **QUdpSocket**::~QUdpSocket()

析构函数。销毁套接字，必要的话关闭连接。

​    另外您也可以在 [close()](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-void-qabstractsocketclose) 中找到相关信息。



### bool **QUdpSocket**::hasPendingDatagrams() const

当至少有一个数据报等待读取时，该函数返回 true ，否则返回 false 。

​    另外您也可以在 [pendingDatagramSize()](#qint64-qudpsocketpendingdatagramsize-const) 和 [readDatagram()](#qint64-qudpsocketreaddatagramchar-data-qint64-maxsize-qhostaddress-address--nullptr-quint16-port--nullptr) 函数介绍中找到相关信息。



### bool **QUdpSocket**::joinMulticastGroup(const QHostAddress &*groupAddress*)

该函数会让套接字在操作系统选择的默认接口上加入由 *groupAddress* 指定的多播组。要加入多播组，套接字必须处于*已绑定* （ [*BoundState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态，否则将会出现错误。

​    请注意如果你想加入一个 IPv4 组，您的套接字不能使用 IPv6 协议绑定到主机（使用 QHostAddress::Any 双重模式也不行）。您必须使用 QHostAddress::AnyIPv4。

​    成功加入多播组后后函数返回 true ，否则返回 false 。

​    **注意：** 不指定接口而直接连接 IPv6 多播组的操作在任何一个操作系统上都是不被允许的。在这种情况下，请您使用该函数另外的一个可以指定接口的重载版本。

​    该函数最初在Qt4.8版本引入。

​    另外您也可以在 [LeaveMulticastGroup()](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress) 函数介绍中找到相关信息。



### bool **QUdpSocket**::joinMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)

重载函数。

​    使用 *iface* 指定的接口连接 *groupAddress* 指定的多播组。

​    该函数最初在Qt4.8版本引入。

​	另外您也可以在 [LeaveMulticastGroup()](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress) 函数介绍中找到相关信息。



### bool **QUdpSocket**::leaveMulticastGroup(const QHostAddress &*groupAddress*)

使用操作系统指定的默认接口离开 *groupAddress* 指定的多播组。要退出多播组，套接字必须处于*已绑定* （ [*BoundState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态，否则将会出现错误。

​    成功退出多播组后该函数返回 true ，否则返回 false 。

​    **注意：** 该函数的参数应该与传递到 [joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 的参数相同。

​    该函数最早在Qt4.8版本引入。

​	另外您也可以在 [joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 函数介绍中找到相关信息。



### bool **QUdpSocket**::leaveMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)

重载函数。

​    使用 *iface* 指定的接口退出 *groupAddress* 指定的多播组。

​    **注意：**[joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 的参数相同。

​    该函数最早在Qt4.8版本引入。

​	另外您也可以在 [joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 函数介绍中找到相关信息。



### QNetworkInterface **QUdpSocket**::multicastInterface() const

返回多播数据报的传出接口的接口信息。这与 IPv4 套接字的 IP_MULTICAST_IF 套接字选项和 IPv6 套接字的 IPV6_MULTICAST_IF 套接字选项相对应。如果此前并没有设置一个接口， 函数将返回一个无效的 [QNetworkInterface](../../N/QNetworkInterface/QNetworkInterface.md) 。要退出多播组，套接字必须处于*已绑定* （ [*BoundState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态，否则将会返回一个无效的 [QNetworkInterface](../../N/QNetworkInterface/QNetworkInterface.md)。

​    该函数最早在Qt4.8版本引入。

​    另外您也可以在 [setMulticastInterface()](#void-qudpsocketsetmulticastinterfaceconst-qnetworkinterface-iface) 函数介绍中找到相关信息。



### qint64 **QUdpSocket**::pendingDatagramSize() const

返回第一个待处理的 UDP 数据报的大小。如果没有可获取的数据报，函数将会返回-1。

[hasPendingDatagrams()](#bool-qudpsockethaspendingdatagrams-const) 和 [readDatagram()](#qint64-qudpsocketreaddatagramchar-data-qint64-maxsize-qhostaddress-address--nullptr-quint16-port--nullptr) 函数介绍中找到相关信息。



### qint64 **QUdpSocket**::readDatagram(char \**data*, qint64 *maxSize*, QHostAddress \**address* = nullptr, quint16 \**port* = nullptr)

接收一个不超过 *maxsize* 字节大小数据报并将其储存在 *data* 中。 发送端的主机地址和端口将分别储存在 \**address* 和 \**port* 中（某值为空指针时除外）。

​    操作成功后返回数据报的大小，否则返回-1。

​    如果 *maxsize* 指定的最大值太小，小于数据报的大小，数据报中剩余的数据将会被丢失。若想要避免丢失数据，您可以在读取该数据报之前调用 [pendingDatagramSize()](#qint64-qudpsocketpendingdatagramsize-const) 来获取该数据报的大小。 如果 *maxsize* 设置为0，该数据报会被丢弃。

​    另外您也可以在 [writeDatagram()](#qint64-qudpsocketwritedatagramconst-char-data-qint64-size-const-qhostaddress-address-quint16-port)，[hasPendingDatagrams()](#bool-qudpsockethaspendingdatagrams-const) 和 [pendingDatagramSize()](#qint64-qudpsocketpendingdatagramsize-const) 函数介绍中找到相关信息。



### QNetworkDatagram **QUdpSocket**::receiveDatagram(qint64 *maxSize* = -1)

接收一个不超过 *maxsize* 字节大小的数字报并将它的内容以及发送者的主机地址和端口一起放在一个 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) 对象中返回。如果可能，该函数还将尝试确定数据报的目标地址，端口以及接收时的跳数计数。

​    如果操作失败，函数会返回一个无效的 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md)  。

​    如果 *maxsize* 指定的最大值太小，小于数据报的大小，数据报中剩余的数据将会被丢失。如果 *maxsize* 设置为0，该数据报会被丢弃。如果 *maxsize* 设置为-1，函数会尝试读取整个数据报。

​    该函数最早在Qt5.8版本引入。

​	另外您也可以在 [writeDatagram()](#qint64-qudpsocketwritedatagramconst-char-data-qint64-size-const-qhostaddress-address-quint16-port)，[hasPendingDatagrams()](#bool-qudpsockethaspendingdatagrams-const) 和 [pendingDatagramSize()](#qint64-qudpsocketpendingdatagramsize-const) 函数介绍中找到相关信息。



### void **QUdpSocket**::setMulticastInterface(const QNetworkInterface &*iface*)

将多播数据报的传出接口设置为接口 *iface* 。 这与 IPv4 套接字的 IP_MULTICAST_IF 套接字选项和 IPv6 套接字的 IPV6_MULTICAST_IF 套接字选项相对应。要设定一个接口，套接字必须处于*已绑定* （ [*BoundState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态，否则函数将不会进行任何操作。

​    该函数最早在Qt4.8版本引入。

​	另外您也可以在 [multicastInterface()](#qnetworkinterface-qudpsocketmulticastinterface-const)，[joinMulticastGroup()](#bool-qudpsocketjoinmulticastgroupconst-qhostaddress-groupaddress) 和 [LeaveMulticastGroup()](#bool-qudpsocketleavemulticastgroupconst-qhostaddress-groupaddress) 函数介绍中找到相关信息。



### qint64 **QUdpSocket**::writeDatagram(const char **data*, qint64 *size*, const QHostAddress &*address*, quint16 *port*)

向 *address* 指定的主机的 *port* 指定的端口上发送 *size* 字节大小的 *data* 中的数据。操作成功则返回发送的字节数，否则返回-1。

​	数据报始终作为一个块写入。 数据报的最大大小与平台高度相关，但可以低至8192字节。 如果数据报太大，则此函数将返回-1，并且 [error()](#qabstractsocketsocketerror-qabstractsocketerror-const) 将返回 [DatagramTooLargeError](#enum-qabstractsocketsocketerror) 。



### qint64 **QUdpSocket**::writeDatagram(const QNetworkDatagram &*datagram*)

重载函数。

​	*datagram* 中除要发送的数据外，还包含主机地址，端口，接口和条数限制。套接字将根据这些信息发送数字报。如果目标地址和端口未被设置，函数将会将数据报发送到传递到 [connectToHost()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol) 函数的地址。

​	如果目标地址是具有非空范围ID的 IPv6 ，但与数据报中的接口索引不同，则操作系统将选择哪一个接口发送数据报并没有相关定义。

​	操作成功则该函数返回发送的字节数，否则返回-1。

​	**警告：** 在一个已连接的 UDP 套接字中调用该函数可能会产生错误并且不能发出任何包。如果你正在使用一个已连接的套接字，请调用 write() 函数发送数据报。

​	该函数在最初在Qt5.8版本引入。

​	另外您也可以在 QNetworkDatagram::setDestination()，QNetworkDatagram::setHopLimit() 和 QNetworkDatagram::setInterfaceIndex() 函数介绍中找到相关信息。



### qint64 QUdpSocket::writeDatagram(const QByteArray &*datagram*, const QHostAddress &*host*, quint16 *port*)

重载函数。

​	发送数据报 *datagram* 到 *host* 指定的主机和 *port* 指定的端口。

​	函数成功发送数据报后会返回发送的字节数，否则返回-1。