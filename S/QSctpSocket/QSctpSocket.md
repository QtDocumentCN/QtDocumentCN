[TOC]



# QSctpSocket Class

QSctpSocket 类提供了一个 SCTP 类型的套接字。

| 属性   | 方法                                           |
| ------ | ---------------------------------------------- |
| 头文件 | #include\<QSctpSocket\>                        |
| qmake  | QT += network                                  |
| 引入   | Qt5.8                                          |
| 父类   | [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) |

该类最初在Qt5.8版本引入。



## 公共成员函数

| 类型             | 函数名                                                       |
| ---------------- | ------------------------------------------------------------ |
|                  | **[ QSctpSocket](#qsctpsocketqsctpsocketqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual          | **[~QSctpSocket](#virtual-qsctpsocketqsctpsocket)**()        |
| bool             | **[isInDatagramMode](#bool-qsctpsocketisindatagrammode-const)**() const |
| int              | **[maximumChannelCount](#int-qsctpsocketmaximumchannelcount-const)**() const |
| QNetworkDatagram | **[readDatagram](#qnetworkdatagram-qsctpsocketreaddatagram)**() |
| void             | **[setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)**(int *count*) |
| bool             | **[writeDatagram](#bool-qsctpsocketwritedatagramconst-qnetworkdatagram-datagram)**(const QNetworkDatagram &*datagram*) |



## 重写公共成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | **[close](#override-virtual-void-qsctpsocketclose)**() override |
| virtual void | **[disconnectFromHost](#override-virtual-void-qsctpsocketdisconnectfromhost)**() override |



## 重写保护成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual qint64 | **[readData](#qnetworkdatagram-qsctpsocketreaddatagram)**(char **data*, qint64 *maxSize*) override |
| virtual qint64 | **[readLineData](#override-virtual-protected-qint64-qsctpsocketreadlinedatachar-data-qint64-maxlen)**(char **data*, qint64 *maxlen*) override |



## 详细介绍

SCTP（流控制传输协议）是一种传输层协议，其作用与流行的协议 TCP 和 UDP 类似。 像 UDP 一样，SCTP 也是面向消息的，但是它可以通过类似 TCP 的拥塞控制来确保消息的可靠性，使消息按顺序传输。

SCTP 是面向连接的协议，它提供端点之间多个数据流的完全同时传输。 这种多数据流允许通过独立的通道传输数据，因此，如果一个数据流中有数据丢失，则其他数据流的传输将不会受到影响。

作为一个面向消息的传输协议，SCTP 以序列方式传输消息，而不是像 TCP 一样传输连续的字节流。 像在 UDP 中一样，在 SCTP 中，发送方在一个操作中发送一条消息，而确切的消息则在一个操作中传递给接收应用程序进程。 但是与 UDP 不同，消息的传递是有可靠性保证的。

SCTP 还支持多宿主，这意味着连接的端点可以具有一些与其关联的备用 IP 地址，以便绕过网络故障或变化的条件进行数据传输。

QSctpSocket 是 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 的便利子类，它使您可以通过 SCTP 模拟 TCP 数据流或建立 SCTP 连接以实现可靠的数据报服务。

QSctpSocket 可以在以下两种模式之一中运行：

* 连续字节流（TCP 模拟）。
* 多流数据报模式。

要设置连续字节流模式，您可以首先实例化一个 QSctpSocket 对象并使用一个负值作为参数调用 [setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)() ，这样就可以将 QSctpSocket 用作常规的缓冲 QTcpSocket 类型套接字使用。 您可以调用 [connectToHost](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 来发起与端点的连接，可以调用 write() 和 read() 来与对等方进行消息发送与接收，但是在这种模式下您无法区分消息的边界。

默认情况下，QSctpSocket 使用数据报模式下进行操作。 在您建立连接之前，请先调用 [setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)() 设置应用程序准备支持的最大通道数。 此数字是与远程端点协商的参数，其值受操作系统的限制。 默认值0表示使用对等端的值。 如果两个端点都使用默认值，则连接通道的数量取决于系统。 建立连接后，可以通过调用 readChannelCount() 和 writeChannelCount() 获取实际的通道数。

```cpp
 QSctpSocket *socket = new QSctpSocket(this);

 socket->setMaxChannelCount(16);
 socket->connectToHost(QHostAddress::LocalHost, 1973);

 if (socket->waitForConnected(1000)) {
     int inputChannels = socket->readChannelCount();
     int outputChannels = socket->writeChannelCount();

     ....
 }
```

在数据报模式，QSctpSocket 为每一个通道单独执行数据报的缓冲操作。您可以通过调用 [writeDatagram](#bool-qsctpsocketwritedatagramconst-qnetworkdatagram-datagram)() 函数将当前通道的一个数据报加入缓冲队列，调用 [readDatagram](#qnetworkdatagram-qsctpsocketreaddatagram)() 函数从当前通道读取一个待处理的数据报。

在数据报模式下，允许使用标准的 [QIODevice](../../I/QIODevice/QIODevice.md) 成员函数 read()，readLine()，write() 等，其限制与连续字节流模式相同。

**注意：** 多通道数据报模式并不被 Windows 操作系统支持。

另外您也可以在 [QSctpServer](../../S/QSctpSocket/QSctpSocket.md) ，[QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) ，[QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) 等类文档中找到相关信息。



## 成员函数文档

### **QSctpSocket**::QSctpSocket**([QObject](../../O/QObject) **parent* = nullptr)

构造函数。创建一个处于 *未连接*（ *UnconnectedState* ）状态的 QSctpSocket 类型的对象并设置为数据报操作模式。

另外您也可以在 [socketType](../../A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const)() 和 [setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)() 函数介绍中找到相关信息。



### *[virtual]* **QSctpSocket**::~QSctpSocket()

析构函数。销毁套接字，必要时关闭连接。

另外您也可以在 [close](#override-virtual-void-qsctpsocketclose)() 函数介绍中找到相关信息。



### *[override virtual]* void **QSctpSocket**::close()

重写 [QAbstractSocket::close()](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-void-qabstractsocketclose) 。



### *[override virtual]* void **QSctpSocket**::disconnectFromHost()

重写 [QAbstractSocket::disconnectFromHost()](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketdisconnectfromhost) 。



### bool **QSctpSocket**::isInDatagramMode() const

如果该套接字运行在数据报模式则返回 true 。

另外您也可以在 [setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)() 函数介绍中找到相关信息。



### int **QSctpSocket**::maximumChannelCount() const

返回 QSctpSocket 能支持的最大通道数。

如果返回值为0（默认值）意味着连接的通道数由远程端点设置。

如果 QSctpSocket 运行在连续字节流模式则返回-1。

另外您也可以在 [setMaximumChannelCount](#void-qsctpsocketsetmaximumchannelcountint-count)() ，readChannelCount() 和 writeChannelCount() 函数介绍中找到相关信息。



### *[override virtual protected]* qint64 **QSctpSocket**::readData(char **data*, qint64 *maxSize*)

重写：  [QAbstractSocket::readData](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-protected-qint64-qabstractsocketreaddatachar-data-qint64-maxsize)(char *data, qint64 maxSize).



### [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) **QSctpSocket**::readDatagram()

从当前的读取通道的缓冲区读取一个数据报并将该数据报内容及其发送者的主机地址和端口写入一个 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) 对象中返回。如果可能，此功能还将尝试确定数据报的目标地址，端口以及接收时的跳数计数，并将这些信息写入到返回的 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) 对象中。

如果操作失败，将会返回一个无效的 [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) 对象。

另外您也可以在 [writeDatagram](#bool-qsctpsocketwritedatagramconst-qnetworkdatagram-datagram)() ，[isInDatagramMode](#bool-qsctpsocketisindatagrammode-const)() 和 currentReadChannel() 函数中找到相关信息。



### *[override virtual protected]* qint64 **QSctpSocket**::readLineData(char **data*, qint64 *maxlen*)

重写：  [QAbstractSocket::readLineData](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-protected-qint64-qabstractsocketreadlinedatachar-data-qint64-maxlen)(char *data, qint64 maxlen).



### void **QSctpSocket**::setMaximumChannelCount(int *count*)

设置该应用程序在数据报模式下将支持的最大通道数为 *count* 。 如果 *count* 为0，程序将使用远程端点设置的最大通道支持数。将 *count* 设置为一个负数时，程序将使用连续字节流模式。

您应该仅在 QSctpSocket 处在*未连接*（ [*UnconnectedState*](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态时调用该函数。

另外您也可以在 [maximumChannelCount](#int-qsctpsocketmaximumchannelcount-const)() ，readChannelCount() 和 writeChannelCount() 函数介绍中找到相关信息。



### bool **QSctpSocket**::writeDatagram(const [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) &*datagram*)

将一个数据报写入到当前写出通道的缓冲区。操作成功该函数返回 true ，否则返回 false 。

另外您也可以在 [readDatagram](#qnetworkdatagram-qsctpsocketreaddatagram)() ，[isInDatagramMode](#bool-qsctpsocketisindatagrammode-const)() 和 currentWriteChannel() 函数介绍中找到相关信息。