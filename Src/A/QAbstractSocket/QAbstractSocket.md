[TOC]



# QAbstractSocket Class

QAbstractSocket 类是Qt中 Socket 通信类的基类，被 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 和 [QUdpSocket](../../U/QUdpSocket/QUdpSocket.md)等类继承。QAbstractSocket 类为所有的socket通信类提供了最基本的功能。

| 属性      | 方法                                                         |
| --------- | ------------------------------------------------------------ |
| 头文件    | \#include \<QAbstractSocket\>                                |
| qmake参数 | QT += network                                                |
| 父类      | [QIODevice](../../I/QIODevice/QIODevice.md)                  |
| 子类      | [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md)、[QUdpSocket](../../U/QUdpSocket/QUdpSocket.md) |



## 公共成员类型

| 类型  | 方法                                                         |
| ----- | ------------------------------------------------------------ |
| enum  | [BindFlag { ShareAddress, DontShareAddress, ReuseAddressHint, DefaultForPlatform }](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) |
| flags | [BindMode](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) |
| enum  | [NetworkLayerProtocol{ IPv4Protocol, IPv6Protocol, AnyIPProtocol, UnknownNetworkLayerProtocol }](#enum-qabstractsocketnetworklayerprotocol) |
| enum  | [PauseMode { PauseNever, PauseOnSslErrors }](#enum-qabstractsocketpausemode--flags-qabstractsocketpausemodes) |
| flags | [PauseModes](#enum-qabstractsocketpausemode--flags-qabstractsocketpausemodes) |
| enum  | [SocketError { ConnectionRefusedError, RemoteHostClosedError, HostNotFoundError, SocketAccessError, SocketResourceError, …, UnknownSocketError }](#enum-qabstractsocketsocketerror) |
| enum  | [SocketOption{ LowDelayOption, KeepAliveOption, MulticastTtlOption, MulticastLoopbackOption, TypeOfServiceOption, …, PathMtuSocketOption }](#enum-qabstractsocketsocketoption) |
| enum  | [SocketState { UnconnectedState, HostLookupState, ConnectingState, ConnectedState, BoundState, …, ListeningState }](#enum-qabstractsocketsocketstate) |
| enum  | [SocketType { TcpSocket, UdpSocket, SctpSocket, UnknownSocketType }](#enum-qabstractsocketsockettype) |



## 公共成员函数

| 类型                         | 函数名                                                       |
| ---------------------------- | ------------------------------------------------------------ |
|                              | [QAbstractSocket(QAbstractSocket::SocketType *socketType*, QObject **parent*)](#qabstractsocketqabstractsocketqabstractsocketsockettype-sockettype-qobject-parent) |
| virtual                      | [~QAbstractSocket()](#virtual-qabstractsocketqabstractsocket) |
| void                         | [abort()](#void-qabstractsocketabort)                        |
| bool                         | [bind(const QHostAddress &*address*, quint16 *port* = 0, QAbstractSocket::BindMode *mode* = DefaultForPlatform)](#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) |
| bool                         | [bind(quint16 *port* = 0, QAbstractSocket::BindMode *mode* = DefaultForPlatform)](#bool-qabstractsocketbindquint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) |
| virtual void                 | [connectToHost(const QString &*hostName*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite, QAbstractSocket::NetworkLayerProtocol *protocol* = AnyIPProtocol)](#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol) |
| virtual void                 | [connectToHost(const QHostAddress &*address*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite)](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) |
| virtual void                 | [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) |
| QAbstractSocket::SocketError | [error() const](#qabstractsocketsocketerror-qabstractsocketerror-const) |
| bool                         | [flush()](#bool-qabstractsocketflush)                        |
| bool                         | [isValid() const](#bool-qabstractsocketisvalid-const)        |
| QHostAddress                 | [localAddress() const](#qhostaddress-qabstractsocketlocaladdress-const) |
| quint16                      | [localPort() const](#quint16-qabstractsocketlocalport-const) |
| QAbstractSocket::PauseModes  | [pauseMode() const](#qabstractsocketpausemodes-qabstractsocketpausemode-const) |
| QHostAddress                 | [peerAddress() const](#qhostaddress-qabstractsocketpeeraddress-const) |
| QString                      | [peerName() const](#qstring-qabstractsocketpeername-const)   |
| quint16                      | [peerPort() const](#quint16-qabstractsocketpeerport-const)   |
| QString                      | [protocolTag() const](#qstring-qabstractsocketprotocoltag-const) |
| QNetworkProxy                | [proxy() const](#qnetworkproxy-qabstractsocketproxy-const)   |
| qint64                       | [readBufferSize() const](#qint64-qabstractsocketreadbuffersize-const) |
| virtual void                 | [resume()](#virtual-void-qabstractsocketresume)              |
| void                         | [setPauseMode(QAbstractSocket::PauseModes *pauseMode*)](#void-qabstractsocketsetpausemodeqabstractsocketpausemodes-pausemode) |
| void                         | [setProtocolTag(const QString &*tag*)](#void-qabstractsocketsetprotocoltagconst-qstring-tag) |
| void                         | [setProxy(const QNetworkProxy &*networkProxy*)](#void-qabstractsocketsetproxyconst-qnetworkproxy-networkproxy-) |
| virtual void                 | [setReadBufferSize(qint64 *size*)](#virtual-void-qabstractsocketsetreadbuffersizeqint64-size) |
| virtual bool                 | [setSocketDescriptor(qintptr *socketDescriptor*, QAbstractSocket::SocketState *socketState* = ConnectedState, QIODevice::OpenMode *openMode* = ReadWrite)](#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) |
| virtual void                 | [setSocketOption(QAbstractSocket::SocketOption *option*, const QVariant &*value*)](#virtual-void-qabstractsocketsetsocketoptionqabstractsocketsocketoption-option-const-qvariant-value) |
| virtual qintptr              | [socketDescriptor() const](#virtual-qintptr-qabstractsocketsocketdescriptor-const) |
| virtual QVariant             | [socketOption(QAbstractSocket::SocketOption *option*)](#virtual-qvariant-qabstractsocketsocketoptionqabstractsocketsocketoption-option) |
| QAbstractSocket::SocketType  | [socketType() const](#qabstractsocketsockettype-qabstractsocketsockettype-const) |
| QAbstractSocket::SocketState | [state() const](#qabstractsocketsocketstate-qabstractsocketstate-const) |
| virtual bool                 | [waitForConnected(int *msecs* = 30000)](#virtual-bool-qabstractsocketwaitforconnectedint-msecs--30000) |
| virtual bool                 | [waitForDisconnected(int *msecs* = 30000)](#virtual-bool-qabstractsocketwaitfordisconnectedint-msecs--30000) |



## 重载公共成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual bool   | [atEnd() const override](#override-virtual-bool-qabstractsocketatend-const) |
| virtual qint64 | [bytesAvailable() const override](#override-virtual-qint64-qabstractsocketbytesavailable-const) |
| virtual qint64 | [bytesToWrite() const override](#override-virtual-qint64-qabstractsocketbytestowrite-const) |
| virtual bool   | [canReadLine() const override](#override-virtual-bool-qabstractsocketcanreadline-const) |
| virtual void   | [close() override](#override-virtual-void-qabstractsocketclose) |
| virtual bool   | [isSequential() const override](#override-virtual-bool-qabstractsocketissequential-const) |
| virtual bool   | [waitForBytesWritten(int *msecs* = 30000) override](#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000) |
| virtual bool   | [waitForReadyRead(int *msecs* = 30000) override](#override-virtual-bool-qabstractsocketwaitforreadyreadint-msecs--30000) |



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | [connected()](#signal-void-qabstractsocketconnected)         |
| void | [disconnected()](#signal-void-qabstractsocketdisconnected)   |
| void | [errorOccurred(QAbstractSocket::SocketError *socketError*)](#signal-void-qabstractsocketerroroccurredqabstractsocketsocketerror-socketerror) |
| void | [hostFound()](#signal-void-qabstractsockethostfound)         |
| void | [proxyAuthenticationRequired(const QNetworkProxy &*proxy*, QAuthenticator **authenticator*)](#signal-void-qabstractsocketproxyauthenticationrequiredconst-qnetworkproxy-proxy-qauthenticator-authenticator) |
| void | [stateChanged(QAbstractSocket::SocketState *socketState*)](#signal-void-qabstractsocketstatechangedqabstractsocketsocketstate-socketstate) |



## 保护成员函数

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | [setLocalAddress(const QHostAddress &*address*)](#protected-void-qabstractsocketsetlocaladdressconst-qhostaddress-address) |
| void | [setLocalPort(quint16 *port*)](#protected-void-qabstractsocketsetlocalportquint16-port) |
| void | [setPeerAddress(const QHostAddress &*address*)](#protected-void-qabstractsocketsetpeeraddressconst-qhostaddress-address) |
| void | [setPeerName(const QString &*name*)](#protected-void-qabstractsocketsetpeernameconst-qstring-name) |
| void | [setPeerPort(quint16 *port*)](#protected-void-qabstractsocketsetpeerportquint16-port) |
| void | [setSocketError(QAbstractSocket::SocketError *socketError*)](#proteched-void-qabstractsocketsetsocketerrorqabstractsocketsocketerror-socketerror) |
| void | [setSocketState(QAbstractSocket::SocketState *state*)](#protected-void-qabstractsocketsetsocketstateqabstractsocketsocketstate-state) |



## 重载保护成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual qint64 | [readData(char **data*, qint64 *maxSize*) override](#override-virtual-protected-qint64-qabstractsocketreaddatachar-data-qint64-maxsize) |
| virtual qint64 | [readLineData(char **data*, qint64 *maxlen*) override](#override-virtual-protected-qint64-qabstractsocketreadlinedatachar-data-qint64-maxlen) |
| virtual qint64 | [writeData(const char **data*, qint64 *size*) override](#overrude-virtual-protected-qint64-qabstractsocketwritedataconst-char-data-qint64-size) |



## 详细介绍

QAbstractSocket 类是 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 类和 QUdpSocket 类的基类，包含了这两个类所有的常规功能。您可以通过以下两种方法使用一个套接字( Socket )：

* 实例化一个 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 或者 QUdpSocket 对象
* 声明一个自定义套接字描述符，实例化 QAbstractSocket ，然后调用 [setSocketDescriptor()](#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) 函数包装该自定义套接字描述符。

TCP（传输控制协议）是一种可靠的，面向流，面向连接的传输协议。 UDP（用户数据报协议）是一种不可靠的，面向数据报的无连接协议。 实际上，这意味着TCP更适合于连续数据传输，而当可靠性不重要时，可以使用更轻量的UDP。

QAbstractSocket 的 API 统一了这两种协议之间的大部分差异。 例如，尽管 UDP 是无连接的，但 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 为 UDP 套接字建立了虚拟连接，使您可以忽略底层协议，以几乎相同的方式使用 QAbstractSocket 类。 在 QAbstractSocket 类的内部实现中，QAbstractSocket 记录了传递给 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 的地址和端口，并且能在调用 read() 和 write() 之类的成员函数时使用这些值。

任何情况下，QAbstractSocket 类都有一个*状态*（ *state* ，该值可以由 [state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 成员函数的返回值获得）。 初始状态为*未连接*（ [*QAbstractSocket :: UnconnectedState*](#enum-qabstractsocketsocketstate) ）状态。 调用 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 成员函数连接主机后，套接字会首先进入*寻找主机*（ [*QAbstractSocket :: HostLookupState*](#enum-qabstractsocketsocketstate) ）状态。 如果找到了主机，则 QAbstractSocket 会进入*连接中*（ [*QAbstractSocket :: ConnectingState*](#enum-qabstractsocketsocketstate) ）状态，并发送 [hostFound()](#signal-void-qabstractsockethostfound) 信号。 建立连接后，它将进入*已连接*（ [*QAbstractSocket :: ConnectedState*](#enum-qabstractsocketsocketstate) ）状态并发送 [connected()](#signal-void-qabstractsocketconnected) 信号。 如果在以上列出任何阶段发生了错误，则会发出 [errorOccurred()](#signal-void-qabstractsocketerroroccurredqabstractsocketsocketerror-socketerror) 信号。 每当状态发生更改时，QAbstractSocket 都会发出 [stateChanged()](#signal-void-qabstractsocketstatechangedqabstractsocketsocketstate-socketstate) 信号。 为方便起见，当套接字已准备好进行读取和写入数据操作时，[isValid()](#bool-qabstractsocketisvalid-const) 成员函数的返回值为 *true* 。但是要注意一下，在进行读写操作之前，套接字的状态必须为*已连接*（ [*QAbstractSocket :: ConnectedState*](#enum-qabstractsocketsocketstate) ）状态。

您可以通过调用 read() 或 write() 来进行数据读写操作，同时为了方便进行特殊的数据读入操作，您还可以使用 QAbstractSocket 的父类 [QIODevice](../../I/QIODevice/QIODevice.md) 提供的成员函数 readLine() 和 readAll() 。当我们需要以字节为单位进行数据读写操作时，可以使用 QAbstractSocket 的父类 [QIODevice](../../I/QIODevice/QIODevice.md) 提供的成员函数 getChar()，putChar() 和 ungetChar() 。 待数据写入套接字后，QAbstractSocket 会发出继承自父类 [QIODevice](../../I/QIODevice/QIODevice.md)  的信号 bytesWritten() 。请特别注意一下，Qt并不限制写缓冲区的大小。 您可以通过监听 bytesWritten() 信号来监视其大小。

每当有新的数据块到达时，QAbstractSocket 都会发出继承自父类 [QIODevice](../../I/QIODevice/QIODevice.md)  的信号 readyRead() 。 您可以通过 [bytesAvailable()](#override-virtual-qint64-qabstractsocketbytesavailable-const) 成员函数的返回值来获得当前读取缓冲区中可读取的字节数。 通常来讲，您可以将 readyRead() 信号与一个槽函数相连接，然后在该槽函数中读取所有可用的数据。 如果您不一次性读取所有数据，则其余数据以后仍可以读取，并且任何新的传入数据都将追加到 QAbstractSocket 的内部读取缓冲区中。您可以通过调用 [setReadBufferSize()](#virtual-void-qabstractsocketsetreadbuffersizeqint64-size) 成员函数来限制读取缓冲区的大小。

您可以通过调用 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 成员函数关闭套接字。 调用 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 成员函数后，QAbstractSocket 会进入*关闭中*（ [*QAbstractSocket :: ClosingState*](#enum-qabstractsocketsocketstate) ）状态。 待所有未处理数据写入套接字后，QAbstractSocket 将关闭套接字，进入*未连接*（ [*QAbstractSocket :: UnconnectedState*](#enum-qabstractsocketsocketstate) ）状态，并发送 [disconnected()](#signal-void-qabstractsocketdisconnected) 信号。 如果要立即中止连接，并丢弃所有未处理数据，请调用 [abort()](#void-qabstractsocketabort) 成员函数。 如果远程主机关闭了该连接，QAbstractSocket 将发出 [errorOccurred(QAbstractSocket :: RemoteHostClosedError)](#signal-void-qabstractsocketerroroccurredqabstractsocketsocketerror-socketerror) 错误信号，在此期间套接字状态仍为*已连接*（ [*QAbstractSocket :: ConnectedState*](#enum-qabstractsocketsocketstate) ）状态，此后将发送 [disconnected()](#signal-void-qabstractsocketdisconnected) 信号。

您可以通过调用 [peerPort()](#quint16-qabstractsocketpeerport-const) 和 [peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const) 成员函数来获取已连接的对等方的端口和地址。 [peerName()](#qstring-qabstractsocketpeername-const) 成员函数则会返回传递给 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 的对等方的主机名。 另外，[localPort()](#quint16-qabstractsocketlocalport-const) 和 [localAddress()](#qhostaddress-qabstractsocketlocaladdress-const) 成员函数可返回本地套接字的端口和地址。

QAbstractSocket 提供了一组函数，这些函数可以挂起调用线程，直到发出某些信号为止。 这些函数可用于实现阻塞套接字：

* [waitForConnected()](#virtual-bool-qabstractsocketwaitforconnectedint-msecs--30000) 阻塞套接字直到一个新的连接建立

* [waitForReadyRead()](#override-virtual-bool-qabstractsocketwaitforreadyreadint-msecs--30000) 阻塞套接字直到有新的数据可以读取
* [waitForBytesWritten()](#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000) 阻塞套接字直到一个有效的荷载数据写入到了套接字
* [waitForDisconnected()](#virtual-bool-qabstractsocketwaitfordisconnectedint-msecs--30000) 阻塞套接字直到连接已经关闭

Qt官方提供了如下示例：

```cpp
int numRead = 0, numReadTotal = 0;
char buffer[50];

forever {
	numRead  = socket.read(buffer, 50);

	// do whatever with array

	numReadTotal += numRead;
	if (numRead == 0 && !socket.waitForReadyRead())
		break;
}
```

[waitForReadyRead()](#override-virtual-bool-qabstractsocketwaitforreadyreadint-msecs--30000) 成员函数返回值为 *false*，则说明连接已关闭或发生了错误。

使用阻塞套接字进行编程与使用非阻塞套接字进行编程完全不同。 阻塞套接字不需要有一个事件循环，这通常可以简化代码。 但是，在GUI应用程序中，阻塞套接字只能在非GUI线程中使用，以避免冻结用户界面。 有关这两种方法的概述，请参见 fortuneclien 和 blockingfortuneclient 示例。

**注意：** Qt官方并不推荐将阻塞函数与信号一起使用。

QAbstractSocket 可以与 [QTextStream](../../T/QTextStream/QTextStream.md) 和 [QDataStream](../../D/QDataStream/QDataStream.md) 的流运算符（operator<<() 和operator>>()）一起使用。 但是，有一个问题需要注意：在尝试使用operator>>() 读取数据之前，必须确保有足够的数据可用。

您也可以在 [QNetworkAccessManager](../../N/QNetworkAccessManager/QNetworkAccessManager.md) 类和 [QTcpServer](../../T/QTcpServer/QTcpServer.md) 类的文档中找到一部分相关的信息。



## 成员类型文档

### enum QAbstractSocket::**BindFlag** | flags QAbstractSocket::**BindMode**

该枚举描述了一些不同的标志，这些标志可以传递为 [bind()](#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 成员函数的参数，指定了不同的主机绑定模式。

| 常量                                |  值  | 描述                                                         |
| :---------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::ShareAddress       | 0x1  | 允许其他服务绑定到相同的地址和端口。 在多个进程通过侦听相同的地址和端口来分担单个服务的负载的情况下（例如，具有多个预分支侦听器的Web服务器可以大大缩短响应时间），该模式十分有效。 但是，由于该模式下允许任何服务对主机进行重新绑定，因此此选项存在着安全隐患。 请注意，您还可以允许您的服务重新绑定现有的共享地址通过将此选项与 *QAbstractSocket::ReuseAddressHint* 结合使用。 在 Unix 上，这等效于 SO_REUSEADDR 套接字选项。 在 Windows 上，这是默认行为，因此将忽略此选项。 |
| QAbstractSocket::DontShareAddress   | 0x2  | 绑定主机时独占地址和端口，不允许其他服务重新绑定。 将此选项作为 [QAbstractSocket :: bind()](#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 参数，可以确保在绑定主机成功后，您当前的服务是唯一侦听指定地址和端口的服务。 即使其他服务通过指定 *QAbstractSocket::ReuseAddressHint* 模式来绑定服务，这个操作也是不允许的。 该模式相比 *QAbstractSocket::ShareAddress* 提供了更高的安全性，但是在某些操作系统上，它要求您以管理员权限运行该服务。 在 Unix 和 macOS 上，独占地址和端口是绑定主机的默认行为，因此该选项将被忽略。 在 Windows 上，此选项使用 SO_EXCLUSIVEADDRUSE 套接字选项。 |
| QAbstractSocket::ReuseAddressHint   | 0x4  | 示意 QAbstractSocket 即使地址和端口已被另一个套接字绑定，它也应尝试重新绑定服务。 在 Windows 和 Unix 上，这等效于 SO_REUSEADDR 套接字选项。 |
| QAbstractSocket::DefaultForPlatform | 0x0  | 使用当前平台的默认模式。 在 Unix 和 macOS 上，这等效于（ *QAbstractSocket::DontShareAddress*  +  *QAbstractSocket::ReuseAddressHint* ），在 Windows 上，它等效于 *QAbstractSocket::ShareAddress* 。 |

该枚举最初在Qt5.0版本引入。

BindMode 类型是 typedef QFlags \<BindFlag\> 生成的用户自定义类型。 它存储着 BindFlag 值的 OR 组合。

---

### enum QAbstractSocket::**NetworkLayerProtocol**

该枚举描述了Qt中可以使用的网络层协议。

| 常量                                         |  值  | 描述                   |
| :------------------------------------------- | :--: | :--------------------- |
| QAbstractSocket::IPv4Protocol                |  0   | IPv4                   |
| QAbstractSocket::IPv6Protocol                |  1   | IPv6                   |
| QAbstractSocket::AnyIPProtocol               |  2   | IPv4 或 IPv6           |
| QAbstractSocket::UnknownNetworkLayerProtocol |  -1  | 除IPv4和IPv6之外的协议 |

您也可以在 QHostAddress::protocol() 中找到有关网络层协议的相关知识。

---

### enum QAbstractSocket::**PauseMode** | flags QAbstractSocket::**PauseModes**

该枚举描述了套接字在什么情况下该停止传输中的数据。 当前Qt支持的唯一通知是 QSslSocket :: sslErrors() 。

| 常量                              |  值  | 描述                                                         |
| :-------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::PauseNever       | 0x0  | “永远”不暂停套接字上的数据传输。 该模式是默认设置，符合Qt 4的标准。 |
| QAbstractSocket::PauseOnSslErrors | 0x1  | 收到 SSL 错误（即 QSslSocket :: sslErrors() ）的通知后，暂停套接字上的数据传输。 |

该枚举最初在Qt5.0版本引入。

PauseModes 类型是 typedef QFlags\<PauseMode\> 生成的用户自定义类型。它储存着 PauseMode 值的 OR 组合。

---

### enum QAbstractSocket::**SocketError**

该枚举描述了常见的套接字错误。

| 常量                                              |  值  | 描述                                                         |
| :------------------------------------------------ | :--: | :----------------------------------------------------------- |
| QAbstractSocket::ConnectionRefusedError           |  0   | 连接被对方拒绝（或连接超时）。                               |
| QAbstractSocket::RemoteHostClosedError            |  1   | 远程主机关闭了连接。 请注意，在发送远程主机连接关闭的通知后，客户端套接字（即此套接字）将被关闭。 |
| QAbstractSocket::HostNotFoundError                |  2   | 未能找到主机地址。                                           |
| QAbstractSocket::SocketAccessError                |  3   | 程序没有权限来进行特定的套接字操作                           |
| QAbstractSocket::SocketResourceError              |  4   | 本地系统资源不足（例如本地系统使用了过多的套接字）。         |
| QAbstractSocket::SocketTimeoutError               |  5   | 套接字操作超时。                                             |
| QAbstractSocket::DatagramTooLargeError            |  6   | 数据报大于操作系统的限制（该限制可以低至8192字节）。         |
| QAbstractSocket::NetworkError                     |  7   | 网络发生错误（例如网线断开）。                               |
| QAbstractSocket::AddressInUseError                |  8   | [QAbstractSocket::bind()](#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 指定的主机地址已被另一个套接字使用独占模式绑定。 |
| QAbstractSocket::SocketAddressNotAvailableError   |  9   | [QAbstractSocket :: bind()](#bool-qabstractsocketbindconst-qhostaddress-address-quint16-port--0-qabstractsocketbindmode-mode--defaultforplatform) 指定的主机地址不属于主机。 |
| QAbstractSocket::UnsupportedSocketOperationError  |  10  | 本地操作系统不支持请求的套接字操作（例如，缺少IPv6支持）。   |
| QAbstractSocket::ProxyAuthenticationRequiredError |  12  | 套接字正在使用代理，并且代理需要身份验证。                   |
| QAbstractSocket::SslHandshakeFailedError          |  13  | SSL / TLS 握手失败，因此连接已关闭（仅在 QSslSocket 中使用）。 |
| QAbstractSocket::UnfinishedSocketOperationError   |  11  | 仅由 QAbstractSocketEngine 使用，上一次尝试的操作尚未完成（仍在后台进行）。 |
| QAbstractSocket::ProxyConnectionRefusedError      |  14  | 代理服务器拒绝了连接。                                       |
| QAbstractSocket::ProxyConnectionClosedError       |  15  | 与代理服务器的连接意外关闭（在建立与对方的最终连接之前）。   |
| QAbstractSocket::ProxyConnectionTimeoutError      |  16  | 与代理服务器的连接超时或代理服务器在身份验证阶段停止响应。   |
| QAbstractSocket::ProxyNotFoundError               |  17  | 找不到使用 [setProxy()](#void-qabstractsocketsetproxyconst-qnetworkproxy-networkproxy-) （或应用程序代理）设置的代理地址。 |
| QAbstractSocket::ProxyProtocolError               |  18  | 与代理服务器通信失败，因为无法理解来自代理服务器的响应，这通常是代理服务协议错误的锅。 |
| QAbstractSocket::OperationError                   |  19  | 套接字所处的状态不允许该操作                                 |
| QAbstractSocket::SslInternalError                 |  20  | 使用的 SSL 库出现内部错误。 这可能是由于 SSL 库安装错误或配置错误造成的。 |
| QAbstractSocket::SslInvalidUserDataError          |  21  | 提供了无效的数据（证书，密钥，密码等），其使用导致 SSL 库出现错误。 |
| QAbstractSocket::TemporaryError                   |  22  | 发生临时错误（例如，操作将阻塞套接字，而套接字未阻塞）。     |
| QAbstractSocket::UnknownSocketError               |  -1  | 神了，出现了一个未知错误。                                   |

您也可以在 [QAbstractSocket::error()](#qabstractsocketsocketerror-qabstractsocketerror-const)  和 [QAbstractSocket::errorOccurred()](#signal-void-qabstractsocketerroroccurredqabstractsocketsocketerror-socketerror) 成员函数的详细介绍中找到一部分套接字错误的介绍。

---

### enum QAbstractSocket::**SocketOption**

该枚举表示可以在套接字上设置的选项。 如果需要设置这些选项，您可以在套接字接收到 [connectd()](#signal-void-qabstractsocketconnected) 信号之后，或者在 [QTcpServer](../../QTcpServer/QTcpServer.md) 接收到新的套接字之后，对它们进行设置。

| 常量                                           |  值  | 描述                                                         |
| :--------------------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::LowDelayOption                |  0   | 尝试优化套接字以降低延迟。 对于 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) ，这将设置 TCP_NODELAY 选项并禁用 Nagle 的算法。 将此设置为1启用。 |
| QAbstractSocket::KeepAliveOption               |  1   | 将此设置为1以启用 SO_KEEPALIVE 套接字选项                    |
| QAbstractSocket::MulticastTtlOption            |  2   | 将此设置为整数值以设置 IP_MULTICAST_TTL （多播数据报的 TTL ）套接字选项。 |
| QAbstractSocket::MulticastLoopbackOption       |  3   | 将此设置为1以启用 IP_MULTICAST_LOOP （多播环回）套接字选项。 |
| QAbstractSocket::TypeOfServiceOption           |  4   | Windows 不支持此选项。 这映射到IP_TOS套接字选项。 有关其可能的可取值，请参见下表。 |
| QAbstractSocket::SendBufferSizeSocketOption    |  5   | 在操作系统级别设置套接字发送缓冲区的大小（以字节为单位）。 这映射到 SO_SNDBUF 套接字选项。 该选项不会影响 QIODevice 或 QAbstractSocket 缓冲区。 这个枚举值在Qt 5.3中引入。 |
| QAbstractSocket::ReceiveBufferSizeSocketOption |  6   | 在操作系统级别设置套接字接收缓冲区的大小（以字节为单位）。 这映射到 SO_RCVBUF 套接字选项。 此选项不会影响 [QIODevice](../../I/QIODevice/QIODevice.md) 或 QAbstractSocket 缓冲区（请参见 [setReadBufferSize()](#virtual-void-qabstractsocketsetreadbuffersizeqint64-size) ）。 这个枚举值已在Qt 5.3中引入。 |
| QAbstractSocket::PathMtuSocketOption           |  7   | 检索IP堆栈当前已知的路径最大传输单位（ PMTU ）值（如果该值存在）。 一些IP堆栈还允许设置 MTU 进行传输。 这个枚举值在Qt 5.11中引入。 |

*TypeOfServiceOption* 可能的可取值（优先级）：

|  值  |                 描述                 |
| :--: | :----------------------------------: |
| 224  |     Network control（网络控制）      |
| 192  | Internetwork control（互联网络控制） |
| 160  |        CRITIC/ECP（至关重要）        |
| 128  |      Flash override（火速覆盖）      |
|  96  |            Flash（火速）             |
|  64  |          Immediate（立即）           |
|  32  |           Priority（主要）           |
|  0   |           Routine（常规）            |

该枚举最初在Qt4.6版本引入。

您也可以在 [QAbstractSocket::setSocketOption()](#virtual-void-qabstractsocketsetsocketoptionqabstractsocketsocketoption-option-const-qvariant-value) 和 [QAbstractSocket::socketOption()](#virtual-qvariant-qabstractsocketsocketoptionqabstractsocketsocketoption-option) 函数介绍中找到相关内容。

---

### enum QAbstractSocket::**SocketState**

该枚举描述了套接字不同的状态。

| 常量                              | Value | Description                              |
| :-------------------------------- | :---: | :--------------------------------------- |
| QAbstractSocket::UnconnectedState |   0   | 套接字未连接。                           |
| QAbstractSocket::HostLookupState  |   1   | 套接字正在查询主机。                     |
| QAbstractSocket::ConnectingState  |   2   | 套接字开始建立连接。                     |
| QAbstractSocket::ConnectedState   |   3   | 新的连接已建立。                         |
| QAbstractSocket::BoundState       |   4   | 套接字已绑定到一个地址和端口。           |
| QAbstractSocket::ClosingState     |   6   | 套接字即将关闭（数据可能仍在等待写入）。 |
| QAbstractSocket::ListeningState   |   5   | 套接字仅限内部使用。                     |

您也可以在 [QAbstractSocket::state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 成员函数介绍中找到相关内容。

---

### enum QAbstractSocket::**SocketType**

该枚举描述了传输层的协议。

| Constant                           | Value | Description                  |
| :--------------------------------- | :---: | :--------------------------- |
| QAbstractSocket::TcpSocket         |   0   | TCP                          |
| QAbstractSocket::UdpSocket         |   1   | UDP                          |
| QAbstractSocket::SctpSocket        |   2   | SCTP                         |
| QAbstractSocket::UnknownSocketType |  -1   | 除 TCP, UDP 和 SCTP 外的协议 |

您也可以在 [QAbstractSocket::socketType()](#qabstractsocketsockettype-qabstractsocketsockettype-const) 成员函数介绍中找到相关内容。

---

## 成员函数文档

### QAbstractSocket::**QAbstractSocket**(**QAbstractSocket**::SocketType *socketType*, QObject **parent*)

创建一个新抽象套接字 socketType 。 函数中父对象的参数传递给 [QObject](../../O/QObject/QObject.md) 的构造函数。

这就是它的构造函数嘛，没啥好说的。另外由于 QAbstractSocket 类继承自 [QObject](../../O/QObject/QObject.md) 类，应注意在 QAbstractSocket 类构造函数中调用一下父类 [QObject](../../O/QObject/QObject.md) 类的构造函数。

另外您也可以在 [socketType()](#qabstractsocketsockettype-qabstractsocketsockettype-const) 成员函数文档，以及 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 和 [QUdpSocket](../../U/QUdpSocket/QUdpSocket.md) 类文档找到相关信息。

---

### *[SIGNAL]* void QAbstractSocket::**connected**()

[connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 调用并成功建立一个连接后，QAbstractSocket 类将发送 connectd() 信号。

**注意：** 在某些操作系统上，connected() 信号可能直接从 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 调用发出，以连接到本地主机。

另外您也可以在 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 和 [disconnected()](#signal-void-qabstractsocketdisconnected) 成员函数文档中找到相关信息。

---

### *[SIGNAL]* void QAbstractSocket::**disconnected**()

套接字断开后会发送该信号。

**警告：** 如果您想在与这个信号相连接的槽函数中删除信号的发送者（ sender() ），请使用 deleteLater() 函数。

另外您也可以在 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) ，[disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 和 [abort()](#void-qabstractsocketabort) 函数介绍中找到相关信息。

---

### *[SIGNAL]* void QAbstractSocket::**errorOccurred**(**QAbstractSocket**::SocketError *socketError*)

当套接字遇到错误时会发送该信号。*socketError* 参数描述了该错误类型。

发出此信号后，套接字可能并未准备好进行重新连接。 在这种情况下，我们应尝试从事件循环中进行重新连接。 例如我们可以调用一个*QTimer::singleShot()*，并将0作为时间间隔。

请注意，[*QAbstractSocket :: SocketError*](#enum-qabstractsocketsocketerror) 并不是Qt预注册好的元类型。因此如果您要在队列连接（ queued connections ）模式的信号与槽的连接中传递该类型的参数，您必须使用 Q_DECLARE_METATYPE() 和 qRegisterMetaType() 注册它为元类型。

该函数在Qt5.15版本引入。

另外您也可以在 [error()](#qabstractsocketsocketerror-qabstractsocketerror-const) 和 errorString() 函数介绍以及 Creating Custom Qt Types 文档中找到相关信息。

---

### *[SIGNAL]* void QAbstractSocket::**hostFound**()

在 QAbstractSocket 调用 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 函数并成功找到主机后，它将发送该消息。

**注意：** 从Qt 4.6.3开始，由于可能已缓存DNS结果，因此 QAbstractSocket 可能直接在调用 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 时发送 hostFound() 信号。

另外您也可以在 [connectd()](#signal-void-qabstractsocketconnected) 函数介绍中找到相关信息。

---

### *[SIGNAL]* void QAbstractSocket::**proxyAuthenticationRequired**(const QNetworkProxy &*proxy*, QAuthenticator **authenticator*)

套接字连接的代理服务期需要身份验证时会发送该消息。您可以用所需的详细信息填充 *authenticator* 对象，以便代理服务期进行身份验证并继续连接。

**注意：** 如果信号返回时未使用新信息填充 *authenticator* ，则连接将失败，因此您不能使用队列连接模式（ QueuedConnection ）连接到该信号。

该函数首次在Qt4.3版本引入。

另外您也可以在 [QAuthenticator](../../A/QAuthenticator/QAuthenticator.md) 和 [QNetworkProxy](../../N/QAuthenticator/QAuthenticator.md) 文档中找到相关信息。

---

### [SIGNAL] void QAbstractSocket::**stateChanged**(**QAbstractSocket**::SocketState *socketState*)

QAbstractSocket 状态发生改变后会发送该信号。*socketState* 参数记录了新的状态。

请注意，[*QAbstractSocket :: SocketState*](#enum-qabstractsocketsocketstate) 并不是Qt预注册好的元类型。因此如果您要在队列连接（ queued connections ）模式的信号与槽的连接中传递该类型的参数，您必须使用 Q_DECLARE_METATYPE() 和 qRegisterMetaType() 注册它为元类型。

另外您也可以在 [state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 成员函数介绍和 Create Custom Qt Types 文档中找到相关信息。

---

### [virtual] QAbstractSocket::~**QAbstractSocket**()

析构函数，销毁套接字。

---

### void QAbstractSocket::**abort**()

中止当前连接并重置套接字。 与 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 不同，此函数会立即关闭套接字，并丢弃写缓冲区中的所有未处理数据。

另外您也可以在 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 和 [close()](#override-virtual-void-qabstractsocketclose) 函数介绍中找到相关信息。

---

### *[override virtual]* bool QAbstractSocket::**atEnd**() const

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::atEnd() const* 。

如果当前没有更多数据可读取，则返回 true ，否则返回 false 。

在循环中从套接字读取数据时，最常使用此功能。 例如：

```cpp
// This slot is connected to QAbstractSocket::readyRead()
void SocketClass::readyReadSlot()
{
	while (!socket.atEnd()) {
		QByteArray data = socket.read(100);
		....
	}
}
```

另外您也可以在 [bytesAvailable()](#override-virtual-qint64-qabstractsocketbytesavailable-const) 和 readyRead() 函数介绍中找到相关信息。

---

### bool QAbstractSocket::**bind**(const QHostAddress &*address*, quint16] *port* = 0, **QAbstractSocket**::BindMode *mode* = DefaultForPlatform)

使用 *mode* 指定的 [*QAbstractSocket::BindMode*](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) 模式绑定到 *address* 和 *port* 指定的地址和端口上。

对于 UDP 套接字来说，在使用 bind() 绑定主机后，只要 UDP 数据报到了达指定的地址和端口，就会发出 *QUdpSocket :: readyRead()* 的信号。 因此，此功能对于编写UDP服务器很有用。

对于 TCP 套接字来说，此功能可用于指定将哪个接口用于传出连接，这在多个网络接口的情况下很有用。

默认情况下， QAbstractSocket 会使用 [*DefaultForPlatform BindMode*](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) 模式绑定套接字。 如果未指定端口 *port* ，则  QAbstractSocket 会选择一个随机端口。

成功后，函数返回 true ，套接字进入 *已绑定* （ [*BoundState*](#enum-qabstractsocketsocketstate) )状态； 否则返回 false 。

该函数最初在Qt5.0版本引入。

---

### bool QAbstractSocket::**bind**(quint16 *port* = 0, **QAbstractSocket**::BindMode *mode* = DefaultForPlatform)

重载 bind() 函数。

该函数会使用 *mode* 指定的 [*QAbstractSocket::BindMode*](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) 模式绑定到主机上的任何地址（ *QHostAddress:Any* ) 和 *port* 指定的端口上。

默认情况下， QAbstractSocket 会使用 [*DefaultForPlatform BindMode*](#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) 模式绑定套接字。 如果未指定端口 *port* ，则  QAbstractSocket 会选择一个随机端口。

该函数最初在Qt5.0版本引入。

---

### *[override virtual]* qint64 QAbstractSocket::**bytesAvailable**() const

该函数重写了父类 QIODevice 的类成员函数 *QIODevice::bytesAvailable() const* 。

返回等待读取的传入字节数。

另外您也可以在 [bytesToWrite()](#override-virtual-qint64-qabstractsocketbytestowrite-const) 和 read() 函数介绍中找到相关信息。

---

### *[override virtual]* qint64 QAbstractSocket::**bytesToWrite**() const

该函数重写了父类 QIODevice 的类成员函数 *QIODevice::bytesToWrite() const* 。

返回等待写入的字节数。 当控制权返回事件循环或调用 [flush()](#bool-qabstractsocketflush) 时，这些字节将会被写入。

另外您也可以在 [bytesAvailable()](#override-virtual-qint64-qabstractsocketbytesavailable-const) 和 [flush()](#bool-qabstractsocketflush) 函数介绍中找到相关信息。

---

### *[override virtual]* bool QAbstractSocket::**canReadLine**() const

该函数重写了父类 QIODevice 的类成员函数 *QIODevice::canReadLine() const* 。

如果能从该套接字中读取一行数据时返回 true，否则返回 false 。

另外您也可以在 readLine() 函数介绍中找到相关信息。

---

### *[override virtual]* void QAbstractSocket::**close**()

该函数重写了父类 QIODevice 的类成员函数 *QIODevice::close()* 。

关闭套接字的 I/O 设备并调用 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 来关闭套接字的连接。

您可以阅读 *QIODevice::close()* 的介绍来查阅关闭 I/O 设备时发生的操作。

另外您也可以在 [abort()](#void-qabstractsocketabort) 函数介绍中找到相关信息。

---

### *[virtual]* void QAbstractSocket::**connectToHost**(const QString &*hostName*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite, **QAbstractSocket**::NetworkLayerProtocol *protocol* = AnyIPProtocol)

尝试连接到远程主机 *hostname* 的给定端口 *port* 。 *protocol* 参数可用于指定要使用的网络协议（例如IPv4或IPv6）。

使用 *openMode* 给定的模式打开套接字并进入 *寻找主机*（ [*HostLookupState*](#enum-qabstractsocketsocketstate) ）状态，然后 QAbstractSocket 开始执行主机名查找操作。 成功查找到主机名后， QAbstractSocket 会发出 [hostFound()](#signal-void-qabstractsockethostfound)  信号，并进入*连接中*（ [*ConnectingState*](#enum-qabstractsocketsocketstate) ）状态。 接着 QAbstractSocket 会尝试连接到上一部查找主机后返回的一个或多个地址。 最终建立连接后，QAbstractSocket 会进入*已连接* （ [*ConnectedState*](#enum-qabstractsocketsocketstate) ）并发送 [connectd()](#signal-void-qabstractsocketconnected) 信号。

在以上的任意一阶段中遇到错误，套接字都会发送 [errorOccurred()](#signal-void-qabstractsocketerroroccurredqabstractsocketsocketerror-socketerror) 信号。

*hostName* 参数可以是一个字符串形式的IP地址（例如"49.195.83.32"），也可以是一个主机名（例如"example.com"）。QAbstractSocket 仅在需要时才会进行查找。  *port* 端口参数按本机字节顺序。

另外您也可以在 [state()](#qabstractsocketsocketstate-qabstractsocketstate-const)，[peerName()](#qstring-qabstractsocketpeername-const)，[peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const)，[peerPort()](#quint16-qabstractsocketpeerport-const) 和 [waitForConnected()](#virtual-bool-qabstractsocketwaitforconnectedint-msecs--30000) 函数介绍中找到相关信息。

---

### *[virtual]* void QAbstractSocket::**connectToHost**(const QHostAddress &*address*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite)

重载 connectToHost() 函数。

尝试连接到远程主机 *hostname* 的给定端口 *port* 。

---

### *[virtual]* void QAbstractSocket::**disconnectFromHost**()

尝试关闭套接字。如果还有未处理的数据等待写入，QAbstractSocket 会进入*正在关闭*（ [*ClosingState*](#enum-qabstractsocketsocketstate) ）状态并等待所有数据被写入后再关闭套接字。最终 QAbstractSocket 会进入*未连接*（ [*UnconnectedState*](#enum-qabstractsocketsocketstate) ）状态并发送 [disconnected()](#signal-void-qabstractsocketdisconnected) 信号。

另外您也可以在 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 函数介绍中找到相关信息。

---

### QAbstractSocket::SocketError QAbstractSocket::**error**() const

返回最后一个错误的类型。

另外您也可以在 [state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 和 errorString() 函数介绍中找到相关信息。

---

### bool QAbstractSocket::**flush**()

该函数尽可能多的在不阻塞套接字的前提下将数据从内部写入缓冲区写入基础网络套接字。 如果写入了任何数据，则此函数返回 true ， 否则返回 false 。

可成功写入的字节数取决于操作系统。请仅在需要 QAbstractSocket 立即开始发送缓冲的数据的情况下调用此函数。  在大多数情况下，您不需要调用此函数，因为一旦控制权返回事件循环，QAbstractSocket 将自动开始发送数据。 在没有事件循环的情况下，请改为调用 [waitForBytesWritten()](#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000) 。

另外您也可以在 write() 和 [waitForBytesWritten()](#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000) 函数介绍中找到相关信息。

---

### *[override virtual]* bool QAbstractSocket::**isSequential**() const

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::isSequential()* 。

---

### bool QAbstractSocket::**isValid**() const

如果套接字有效并且可以使用，则返回 true ，否则返回 false 。

**注意：** 在进行读写操作之前，套接字必须处于*已连接*（ [*ConnectedState*](#enum-qabstractsocketsocketstate) ）状态。

另外您也可以在 [state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 函数介绍中找到相关信息。

---

### QHostAddress QAbstractSocket::**localAddress**() const

如果本地套接字则可用返回主机地址，否则返回 *QHostAddress::Null* 。

返回的主机地址通常是主机的IP地址。但是当套接字连接到本地主机时，返回的主机地址为 *QHostAddress::LocalAddress*。

另外您也可以在 [localPort()](#quint16-qabstractsocketlocalport-const)，[peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const) 和 [setLocalAddress()](#protected-void-qabstractsocketsetlocaladdressconst-qhostaddress-address) 函数介绍中找到相关信息。

---

### quint16 QAbstractSocket::**localPort**() const

如果本地套接字可用则按照本地字节顺序返回主机端口，否则返回0。

另外您也可以在 [localAddress()](#qhostaddress-qabstractsocketlocaladdress-const)，[peerPort()](#quint16-qabstractsocketpeerport-const) 和 [setLocalPort()](#protected-void-qabstractsocketsetlocalportquint16-port) 函数介绍中找到相关信息。

---

### QAbstractSocket::**PauseModes** QAbstractSocket::**pauseMode**() const

返回该套接字的数据传输暂停模式。

该函数最初在Qt5.0版本引入。

另外您也可以在 [setPauseMode()](#void-qabstractsocketsetpausemodeqabstractsocketpausemodes-pausemode) 和 [resume()](#virtual-void-qabstractsocketresume) 函数介绍中找到相关信息。

---

### QHostAddress QAbstractSocket::**peerAddress**() const

如果套接字处于*已连接*（ [*ConnectedState*](#enum-qabstractsocketsocketstate) ）状态则返回对等端的地址，否则返回 *QHostAddress::Null* 。

另外您也可以在 [peerName()](#qstring-qabstractsocketpeername-const)，[peerPort()](#quint16-qabstractsocketpeerport-const)，[localAddress()](#qhostaddress-qabstractsocketlocaladdress-const) 和 [setPeerAddress()](#protected-void-qabstractsocketsetpeeraddressconst-qhostaddress-address) 函数介绍中找到相关信息。

---

### QString QAbstractSocket::**peerName**() const

返回在 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 函数中指定的主机名。如果 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 函数未被调用过则返回一个空的 QString 。

另外您也可以在 [peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const)，[peerPort()](#quint16-qabstractsocketpeerport-const) 和 [setPeerName()](#protected-void-qabstractsocketsetpeernameconst-qstring-name) 函数介绍中找到相关信息。

---

### quint16 QAbstractSocket::**peerPort**() const

如果套接字处于*已连接*（ [*ConnectedState*](#enum-qabstractsocketsocketstate) ）状态则返回对等端的端口，否则返回0。

另外您也可以在 [peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const)，[localPort()](#quint16-qabstractsocketlocalport-const) 和 [setPeerPort()](#protected-void-qabstractsocketsetpeerportquint16-port) 函数介绍中找到相关信息。

---

### QString QAbstractSocket::**protocolTag**() const

返回此套接字的协议标签。 如果设置了协议标签，则在 QAbstractSocket 内部创建协议标签时将其传递给[QNetworkProxyQuery](../../N/QNetworkProxyQuery/QNetworkProxyQuery.md)，以指示要使用的协议标签。

该函数最初在Qt5.13版本引入。

另外您也可以在 [setProtocolTag()](#void-qabstractsocketsetprotocoltagconst-qstring-tag) 函数介绍和 [QNetworkProxyQuery](../../N/QNetworkProxyQuery/QNetworkProxyQuery.md) 文档中找到相关信息。

---

### QNetworkProxy QAbstractSocket::**proxy**() const

返回该套接字的网络代理。默认情况下套接字会使用 *QNetworkProxy::DefaultProxy* ，套接字会查询应用程序的默认网络代理设置。

该函数最早在Qt4.1版本引入。

另外您也可以在 [setProxy()](#void-qabstractsocketsetproxyconst-qnetworkproxy-networkproxy-) 函数介绍以及 [QNetworkProxy](../../N/QNetworkProxy/QNetworkProxy.md) 和 [QNetworkProxyFactory](../../N/QNetworkProxyFactory/QNetworkProxyFactory.md) 文档中找到相关信息。

---

### qint64 QAbstractSocket::**readBufferSize**() const

返回内部读取缓冲区的大小。 这限制了客户端在调用 read() 或 readAll() 之前可以接收的数据量。

读取缓冲区大小为0（默认值）意味着缓冲区没有大小限制，从而确保没有数据丢失。

另外您也可以在 [setReadBufferSize()](#virtual-void-qabstractsocketsetreadbuffersizeqint64-size) 和 read() 函数介绍中找到相关信息。

---

### *[override virtual protected]* qint64 QAbstractSocket::**readData**(char **data*, qint64 *maxSize*)

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::readData()* 。

---

### *[override virtual protected]* qint64 QAbstractSocket::**readLineData**(char **data*, qint64 *maxlen*)

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::readLineData()* 。

---

### *[virtual]* void QAbstractSocket::**resume**()

继续套接字数据传输。 仅当将套接字设置为收到暂停的消息后暂停数据传输，并接收到暂停的消息后暂停了数据传输，才能使用此方法。 当前支持的唯一通知是 *QSslSocket :: sslErrors()* 。 如果套接字未暂停，则调用此方法将导致 *未定义的行为*（ *undefined behavior* ）。

该函数最初在Qt5.0版本引入。

另外您也可以在 [pauseMode()](#qabstractsocketpausemodes-qabstractsocketpausemode-const) 和 [setPauseMode()](#void-qabstractsocketsetpausemodeqabstractsocketpausemodes-pausemode) 函数介绍中找到相关信息。

---

### *[protected]* void QAbstractSocket::**setLocalAddress**(const QHostAddress &*address*)

将套接字连接中本地的地址设置为 *address* 。

套接字连接建立后，您可以在 QAbstractSocket 的子类中调用此函数以更改 [localAddress()](#qhostaddress-qabstractsocketlocaladdress-const) 函数的返回值。 代理连接通常将此功能用于虚拟连接设置。

请注意，此函数在连接之前不会绑定套接字的本地地址（例如 *QAbstractSocket :: bind()* ）。

该函数最初在Qt4.1版本引入。

另外您也可以在 [localAddress()](#qhostaddress-qabstractsocketlocaladdress-const)，[setLocalPort()](#protected-void-qabstractsocketsetlocalportquint16-port) 和 [setPeerAddress()](#protected-void-qabstractsocketsetpeeraddressconst-qhostaddress-address) 函数介绍中找到相关知识。

---

### *[protected]* void QAbstractSocket::**setLocalPort**(quint16 *port*)

将套接字连接中本地的端口设置为 *port* 。

套接字连接建立后，您可以在 QAbstractSocket 的子类中调用此函数以更改 [localPort()](#quint16-qabstractsocketlocalport-const) 函数的返回值。 代理连接通常将此功能用于虚拟连接设置。

请注意，此函数在连接之前不会绑定套接字的本地端口（例如 *QAbstractSocket :: bind()* ）。

该函数最初在Qt4.1版本引入。

另外您也可以在 [localPort()](#quint16-qabstractsocketlocalport-const)， [localAddress()](#qhostaddress-qabstractsocketlocaladdress-const)，[setLocalPort()](#protected-void-qabstractsocketsetlocalportquint16-port)[setPeerAddress()](#protected-void-qabstractsocketsetpeeraddressconst-qhostaddress-address)

---

### void QAbstractSocket::**setPauseMode**(**QAbstractSocket**::PauseModes *pauseMode*)

设置套接字是否在收到通知后暂停数据传输。 *pauseMouse* 参数指定套接字暂停的条件。目前唯一支持的暂停套接字数据传输的信号是 *QSslSocket::sslErrors()* 。如果将套接字暂停模式设置为 [*PauseOnSslErrors*](#enum-qabstractsocketpausemode--flags-qabstractsocketpausemodes) ，在接收到 *QSslSocket::sslErrors()* 信号后套接字上的数据传输将被暂停，并且需要通过调用 [resume()](#virtual-void-qabstractsocketresume) 再次显式启用。默认情况下 QAbstractSocket 暂停模式为 [*PauseNever*](\#enum-qabstractsocketpausemode--flags-qabstractsocketpausemodes) 。 若要修改暂停模式，您必须在连接服务器前调用此函数，否则对此函数的调用将被视为未定义行为。

该函数最初在Qt5.0版本引入。

另外您也可以在 [pauseMode()](#qabstractsocketpausemodes-qabstractsocketpausemode-const) 和 [resume()](#virtual-void-qabstractsocketresume) 函数介绍中找到相关信息。

---

### *[protected]* void QAbstractSocket::**setPeerAddress**(const QHostAddress &*address*)

设将套接字连接中远程的地址设置为 *address* 。

您可以在 QAbstractSocket 的一个子类中去改变 [peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const) 函数的返回值。 代理连接通常将此功能用于虚拟连接设置。

该函数最早在Qt4.1版本引入。

另外您也可以在 [peerAddress()](#qhostaddress-qabstractsocketpeeraddress-const)，[setPeerPort()](#protected-void-qabstractsocketsetpeerportquint16-port) 和 [setLocalAddress()](#protected-void-qabstractsocketsetlocaladdressconst-qhostaddress-address) 函数介绍中找到相关信息。

---

### *[protected]* void QAbstractSocket::**setPeerName**(const QString &*name*)

设将套接字连接中远程的主机名设置为 *name* 。

套接字连接建立后，您可以在 QAbstractSocket 的子类中调用此函数以更改 [peerName()](#qstring-qabstractsocketpeername-const) 函数的返回值。 代理连接通常将此功能用于虚拟连接设置。

该函数最早在Qt4.1版本引入。

另外您也可以在 [peerName()](#qstring-qabstractsocketpeername-const)函数介绍中找到相关信息。

---

### *[protected]* void QAbstractSocket::**setPeerPort**(quint16 *port*)

设将套接字连接中远程的端口设置为 *port* 。

套接字连接建立后，您可以在 QAbstractSocket 的子类中调用此函数以更改 [peerPort()](#quint16-qabstractsocketpeerport-const) 函数的返回值。 代理连接通常将此功能用于虚拟连接设置。

该函数最早在Qt4.1版本引入。

另外您也可以在 [peerPort()](#quint16-qabstractsocketpeerport-const) 函数介绍中找到相关信息。

---

### void QAbstractSocket::**setProtocolTag**(const QString &*tag*)

将此套接字的协议标签设置为 *tag* 。

该函数最早在Qt5.13版本引入。

另外您也可以在 [protocolTag()](#qstring-qabstractsocketprotocoltag-const) 函数介绍中找到相关信息。

---

### void QAbstractSocket::**setProxy**(const QNetworkProxy &*networkProxy* )

将此套接字的显式网络代理设置为 *networkProxy* 。

您可以通过指定 *networkProxy* 为 *QNetworkProxy::NoProxy* 以禁止套接字使用代理网络：

```cpp
socket->setProxy(QNetworkProxy::NoProxy);
```

套接字默认使用的代理为 *QNetworkProxy::DefaultProxy* 即套接字会使用应用程序的代理设置，将代理设置为 *QNetworkProxy::setApplicationProxy* 也可以达到同样的效果。如果您使用 *QNetworkProxyFactory :: setApplicationProxyFactory* 设置了 QNetworkProxy 插件工厂，它将使用 *QNetworkProxyQuery :: TcpSocket* 类型查询该插件工厂。

该函数最早在Qt4.1版本引入。

另外您也可以在 [proxy()](#qnetworkproxy-qabstractsocketproxy-const) 函数介绍以及 [QNetworkProxy](../../N/QNetworkProxy)  和 QNetworkProxyFactory::queryProxy() 文档中找到相关信息。

---

### *[virtual]* void QAbstractSocket::**setReadBufferSize**(qint64 *size*)

设置 QAbstractSocket 内部读入缓冲区的大小（字节为单位）。

如果将该缓冲区的大小设置为一个确定的值，QAbstractSocket 内部读入缓冲区内的值大小超过该值后，便不会再缓冲数据。与此相反，缓冲区大小为0意味着读缓冲区不受限制，所有传入数据都将被缓冲，同时这也是默认值。

该功能在特定的情况下（例如，在实时流应用程序中）读取数据，或者要保护套接字避免接收过多的数据（可能最终导致应用程序用尽内存）很有用。

只有[QTcpSocket](../../T/QTcpSocket/QTcpSocket.md)使用 QAbstractSocket 的内部缓冲区。  [QUdpSocket](../../U/QUdpSocket/QUdpSocket.md) 根本不使用任何缓冲，而是依赖于操作系统提供的隐式缓冲。 因此，在 [QUdpSocket](../../U/QUdpSocket/QUdpSocket.md) 上调用此函数无效。

另外您也可以在 [readBufferSize()](#qint64-qabstractsocketreadbuffersize-const) 和 read() 函数介绍中找到相关信息。

---

### *[virtual]* bool QAbstractSocket::**setSocketDescriptor**(qintptr *socketDescriptor*, **QAbstractSocket**::SocketState *socketState* = ConnectedState, QIODevice::OpenMode *openMode* = ReadWrite)

使用本机套接字描述符 *socketDescriptor* 初始化 QAbstractSocket 。 如果 *socketDescriptor* 为有效的套接字描述符，则返回 true ，否则返回 false 。 套接字以 *openMode* 指定的模式打开，并进入由 *socketState* 指定的套接字状态。 读取和写入缓冲区将会丢弃所有未决数据并清空。

**注意：** 无法使用相同的本机套接字描述符初始化两个抽象套接字。

另外您也可以在 [socketDescriptor()](#virtual-qintptr-qabstractsocketsocketdescriptor-const) 函数介绍中找到相关信息。

---

### *[proteched]* void QAbstractSocket::**setSocketError**(**QAbstractSocket**::SocketError *socketError*)

将套接字最后一个出现的错误的类型设置为 *socketError* 。

另外您也可以在 [setSocketState()](#protected-void-qabstractsocketsetsocketstateqabstractsocketsocketstate-state) 和 setErrorString() 函数中找到相关信息。

---

### *[virtual]* void QAbstractSocket::**setSocketOption**(**QAbstractSocket**::SocketOption *option*, const QVariant &*value*)

将 *option* 指定的套接字选项设置为 *value* 指定的值。

**注意：** 当应用程序在 Windows 下运行时，  *QAbstractSocket::KeepAliveOption* 选项的值必须在套接字连接之前指定。

 该函数最初在Qt4.6版本引入。

另外您也可以在 [socketOption()](#virtual-qvariant-qabstractsocketsocketoptionqabstractsocketsocketoption-option) 函数介绍中找到相关信息。

---

### *[protected]* void QAbstractSocket::**setSocketState**(**QAbstractSocket**::SocketState *state*)

将套接字的状态设置为 *state* 。

另外您也可以在[state()](#qabstractsocketsocketstate-qabstractsocketstate-const) 函数介绍中找到相关信息。

---

### *[virtual]* qintptr QAbstractSocket::**socketDescriptor**() const

当 QAbstractSocket 类对象的本地套接字描述符可用时，则返回该描述符，否则返回-1。

如果套接字使用了网络代理，则返回的描述符可能无法与本机套接字一起使用。

当 QAbstractSocket 类处于*未连接*（[*UnconnectedState*](#enum-qabstractsocketsocketstate)）状态时，该描述符是不可用的。

另外您也可以在 [setSocketDescriptor()](#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) 函数介绍中找到相关信息。

---

### *[virtual]* QVariant QAbstractSocket::**socketOption**(**QAbstractSocket**::SocketOption) *option*)

返回 *option* 指定的套接字选项的值。

该函数最早在Qt4.6版本引入。

另外您也可以在 [setSocketDescriptor()](#virtual-bool-qabstractsocketsetsocketdescriptorqintptr-socketdescriptor-qabstractsocketsocketstate-socketstate--connectedstate-qiodeviceopenmode-openmode--readwrite) 函数介绍中找到相关信息。

---

### QAbstractSocket::**SocketType** QAbstractSocket::**socketType**() const

返回套接字类型（ TCP，UDP，或者其他）。

另外您也可以在 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 和 [QUdpSocket](../../U/QUdpSocket/QUdpSocket.md) 文档中找到相关信息。

---

### QAbstractSocket::**SocketState** QAbstractSocket::**state**() const

返回套接字的当前状态。

另外您也可以在 [error()](#qabstractsocketsocketerror-qabstractsocketerror-const) 函数介绍中找到相关信息。

---

### *[override virtual]* bool QAbstractSocket::**waitForBytesWritten**(int *msecs* = 30000)

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::waitForBytesWritten(int msecs)* 。

该函数将阻塞套接字通信直到至少一个字节被写入到套接字并发送 bytesWritten() 信号为止。 函数将会在 *msecs* 指定的时间后超时，默认的超时时间设置为30000毫秒。

bytesWritten() 信号发出后该函数返回值为 true，偶则返回 false （如果有一个错误发生或者该操作超时）。

**注意：** 在 Windows 上，此功能可能会随机性地失败。 如果您的软件将在 Windows 上运行，请考虑使用事件循环和 bytesWritten() 信号。

另外您也可以在 [waitForReadyRead()](#override-virtual-bool-qabstractsocketwaitforreadyreadint-msecs--30000) 函数介绍中找到相关信息。

---

### *[virtual]* bool QAbstractSocket::**waitForConnected**(int *msecs* = 30000)

在 *msecs* 指定的时间内等待套接字连接到主机。如果连接成功建立，则返回 true ，否则返回 false 。如果该函数返回 false ，您可以调用 [error()](#qabstractsocketsocketerror-qabstractsocketerror-const) 函数来确定连接中出现的错误的类型。

这里Qt官方给了一个1秒内等待套接字建立到主机的连接的示例：

```cpp
socket->connectToHost("imap", 143);
if (socket->waitForConnected(1000))
	qDebug("Connected!");
```

如果将 *msecs* 设置为-1，这个函数将不会超时。

**注意：** 由于套接字完成主机的查询需要一定时间，这个函数超时的时间可能会比 *msecs* 设定的时间要轻微的长一些。

**注意：** 多次调用这个函数并不会累积超时时间。如果函数超时，套接字的连接进程就会被中断。

**注意：** 在 Windows 上，此功能可能会随机性地失败。 如果您的软件将在 Windows 上运行，请考虑使用事件循环和 [connected()](#signal-void-qabstractsocketconnected) 信号。

另外您也可以在 [connectToHost()](#virtual-void-qabstractsocketconnecttohostconst-qhostaddress-address-quint16-port-qiodeviceopenmode-openmode--readwrite) 和 [connected()](#signal-void-qabstractsocketconnected) 函数中找到相关信息。

---

### *[virtual]* bool QAbstractSocket::**waitForDisconnected**(int *msecs* = 30000)

在 *msecs* 指定的时间内等待套接字从主机断开连接。 如果连接成功断开，则返回 true ，否则返回 false （操作超时，出现错误，或者已经断开连接）。 如果该函数返回 false ，您可以调用 [error()](#qabstractsocketsocketerror-qabstractsocketerror-const) 函数来确定断开连接时出现的错误的类型。

这里Qt官方给了一个1秒内等待套接字从主机断开连接的示例：

```cpp
socket->disconnectFromHost();
if (socket->state() == QAbstractSocket::UnconnectedState
	|| socket->waitForDisconnected(1000)) {
		qDebug("Disconnected!");
 }
```

如果 *msecs* 设为-1，该函数将不会超时。

**注意：** 在 Windows 上，此功能可能会随机性地失败。 如果您的软件将在 Windows 上运行，请考虑使用事件循环和 disconnected() 信号。

另外您也可以在 [disconnectFromHost()](#virtual-void-qabstractsocketdisconnectfromhost) 和 close() 函数介绍中找到相关信息。

---

### *[override virtual]* bool QAbstractSocket::**waitForReadyRead**(int *msecs* = 30000)

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 *QIODevice::waitForReadyRead(int msecs)* 。

该函数将阻塞套接字通信直到有新的字节可以读取并发送 readyRead() 信号为止。 函数将会在 *msecs* 指定的时间后超时，默认的超时时间设置为30000毫秒。

readyRead() 信号发出后该函数返回值为 true，偶则返回 false （如果有一个错误发生或者该操作超时）。

**注意：** 在 Windows 上，此功能可能会随机性地失败。 如果您的软件将在 Windows 上运行，请考虑使用事件循环和 readyRead() 信号。

另外您也可以在 [waitForBytesWritten()](#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000)() 函数介绍中找到相关信息。

---

### *[overrude virtual protected]* qint64 QAbstractSocket::**writeData**(const char **data*, qint64 *size*)

该函数重写了父类 [QIODevice](../../I/QIODevice/QIODevice.md) 的类成员函数 QIODevice::writeData(const char *data*, qint64 *size*)。
