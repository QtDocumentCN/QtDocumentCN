# QAbstractSocket Class

QAbstractSocket类是Qt中Socket通信的祖宗类，被QTcpSocket和QUdpSocket等类继承。QAbstractSocket类为所有的socket通信类提供了最基本的功能。

|           |                             |
| --------- | --------------------------- |
| 头文件    | \#include <QAbstractSocket> |
| qmake参数 | QT += network               |
| 父类      | QIODevice                   |
| 子类      | QTcpSocket、QUdpSocket      |



## 公共成员类型

|       |                                                              |
| ----- | ------------------------------------------------------------ |
| enum  | BindFlag { ShareAddress, DontShareAddress, ReuseAddressHint, DefaultForPlatform } |
| flags | BindMode                                                     |
| enum  | NetworkLayerProtocol{ IPv4Protocol, IPv6Protocol, AnyIPProtocol, UnknownNetworkLayerProtocol } |
| enum  | PauseMode { PauseNever, PauseOnSslErrors }                   |
| flags | PauseModes                                                   |
| enum  | SocketError { ConnectionRefusedError, RemoteHostClosedError, HostNotFoundError, SocketAccessError, SocketResourceError, …, UnknownSocketError } |
| enum  | SocketOption{ LowDelayOption, KeepAliveOption, MulticastTtlOption, MulticastLoopbackOption, TypeOfServiceOption, …, PathMtuSocketOption } |
| enum  | SocketState { UnconnectedState, HostLookupState, ConnectingState, ConnectedState, BoundState, …, ListeningState } |
| enum  | SocketType { TcpSocket, UdpSocket, SctpSocket, UnknownSocketType } |



## 公共成员函数

|                              |                                                              |
| ---------------------------- | ------------------------------------------------------------ |
|                              | QAbstractSocket(QAbstractSocket::SocketType *socketType*, QObject **parent*) |
| virtual                      | ~QAbstractSocket()                                           |
| void                         | abort()                                                      |
| bool                         | bind(const QHostAddress &*address*, quint16 *port* = 0, QAbstractSocket::BindMode *mode* = DefaultForPlatform) |
| bool                         | bind(quint16 *port* = 0, QAbstractSocket::BindMode *mode* = DefaultForPlatform) |
| virtual void                 | connectToHost(const QString &*hostName*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite, QAbstractSocket::NetworkLayerProtocol *protocol* = AnyIPProtocol) |
| virtual void                 | connectToHost(const QHostAddress &*address*, quint16 *port*, QIODevice::OpenMode *openMode* = ReadWrite) |
| virtual void                 | disconnectFromHost()                                         |
| QAbstractSocket::SocketError | error() const                                                |
| bool                         | flush()                                                      |
| bool                         | isValid() const                                              |
| QHostAddress                 | localAddress() const                                         |
| quint16                      | localPort() const                                            |
| QAbstractSocket::PauseModes  | pauseMode() const                                            |
| QHostAddress                 | peerAddress() const                                          |
| QString                      | peerName() const                                             |
| quint16                      | peerPort() const                                             |
| QString                      | protocolTag() const                                          |
| QNetworkProxy                | proxy() const                                                |
| qint64                       | readBufferSize() const                                       |
| virtual void                 | resume()                                                     |
| void                         | setPauseMode(QAbstractSocket::PauseModes *pauseMode*)        |
| void                         | setProtocolTag(const QString &*tag*)                         |
| void                         | setProxy(const QNetworkProxy &*networkProxy*)                |
| virtual void                 | setReadBufferSize(qint64 *size*)                             |
| virtual bool                 | setSocketDescriptor(qintptr *socketDescriptor*, QAbstractSocket::SocketState *socketState* = ConnectedState, QIODevice::OpenMode *openMode* = ReadWrite) |
| virtual void                 | setSocketOption*(QAbstractSocket::SocketOption *option*, const QVariant &*value*) |
| virtual qintptr              | socketDescriptor() const                                     |
| virtual QVariant             | socketOption(QAbstractSocket::SocketOption *option*)         |
| QAbstractSocket::SocketType  | socketType() const                                           |
| QAbstractSocket::SocketState | state() const                                                |
| virtual bool                 | waitForConnected(int *msecs* = 30000)                        |
| virtual bool                 | waitForDisconnected(int *msecs* = 30000)                     |



## 重载公共成员函数

|                |                                                   |
| -------------- | ------------------------------------------------- |
| virtual bool   | atEnd() const override                            |
| virtual qint64 | bytesAvailable() const override                   |
| virtual qint64 | bytesToWrite() const override                     |
| virtual bool   | canReadLine() const override                      |
| virtual void   | close() override                                  |
| virtual bool   | isSequential() const override                     |
| virtual bool   | waitForBytesWritten(int *msecs* = 30000) override |
| virtual bool   | waitForReadyRead(int *msecs* = 30000) override    |



## 信号

|      |                                                              |
| ---- | ------------------------------------------------------------ |
| void | connected()                                                  |
| void | disconnected()                                               |
| void | errorOccurred(QAbstractSocket::SocketError *socketError*)    |
| void | hostFound()                                                  |
| void | proxyAuthenticationRequired(const QNetworkProxy &*proxy*, QAuthenticator **authenticator*) |
| void | stateChanged(QAbstractSocket::SocketState *socketState*)     |



## 保护成员函数

|      |                                                            |
| ---- | ---------------------------------------------------------- |
| void | setLocalAddress(const QHostAddress &*address*)             |
| void | setLocalPort(quint16 *port*)                               |
| void | setPeerAddress(const QHostAddress &*address*)              |
| void | setPeerName(const QString &*name*)                         |
| void | setPeerPort(quint16 *port*)                                |
| void | setSocketError(QAbstractSocket::SocketError *socketError*) |
| void | setSocketState(QAbstractSocket::SocketState *state*)       |



## 重载保护成员函数

|                |                                                       |
| -------------- | ----------------------------------------------------- |
| virtual qint64 | readData(char **data*, qint64 *maxSize*) override     |
| virtual qint64 | readLineData(char **data*, qint64 *maxlen*) override  |
| virtual qint64 | writeData(const char **data*, qint64 *size*) override |



## 详细介绍

QAbstractSocket类是QTcpSocket类和QUdpSocket类的基类，包含了这两个类所有的常规功能。你可以通过以下两种方法使用一个套接字(Socket)：

* 实例化一个QTcpSocket或者QUdpSocket对象
* 声明一个自定义套接字描述符，实例化QAbstractSocket，然后调用setSocketDescriptor()函数包装该自定义套接字描述符。

​    TCP（传输控制协议）是一种可靠的，面向流，面向连接的传输协议。 UDP（用户数据报协议）是一种不可靠的，面向数据报的无连接协议。 实际上，这意味着TCP更适合于连续数据传输，而当可靠性不重要时，可以使用更轻量的UDP。

​    QAbstractSocket的API统一了这两种协议之间的大部分差异。 例如，尽管UDP是无连接的，但connectToHost()为UDP套接字建立了虚拟连接，使您可以忽略底层协议，以几乎相同的方式使用QAbstractSocket类。 在QAbstractSocket类的内部实现中，QAbstractSocket记录了传递给connectToHost()的地址和端口，并且能在调用read()和write()之类的成员函数时使用这些值。

​    任何情况下，QAbstractSocket类都有一个*状态*（*state*，该值可以由state()成员函数的返回值获得）。 初始状态为*未连接*（*QAbstractSocket :: UnconnectedState*）状态。 调用connectToHost()成员函数连接主机后，套接字会首先进入*寻找主机*（*QAbstractSocket :: HostLookupState*）状态。 如果找到了主机，则QAbstractSocket会进入*连接中*（*QAbstractSocket :: ConnectingState*）状态，并发送hostFound()信号。 建立连接后，它将进入*已连接*（*QAbstractSocket :: ConnectedState*）状态并发送connected()信号。 如果在以上列出任何阶段发生了错误，则会发出errorOccurred()信号。 每当状态发生更改时，QAbstractSocket都会发出stateChanged()信号。 为方便起见，当套接字已准备好进行读取和写入数据操作时，isValid()成员函数的返回值为*true*。但是要特别注意一下，在进行读写操作之前，套接字的状态必须为*已连接*（*QAbstractSocket :: ConnectedState*）状态。

​    您可以通过调用read()或write()来进行数据读写操作，同时为了方便进行特殊的数据读入操作，QAbstractSocket还提供了成员函数readLine()和readAll()。当我们需要以字节为单位进行数据读写操作时，可以使用QAbstractSocket从基类QIODevice中继承来的getChar()，putChar()和ungetChar()成员函数。 待数据写入套接字后，QAbstractSocket会发出bytesWritten()信号。请特别注意一下，Qt并不限制写缓冲区的大小。 您可以通过监听bytesWritten()信号来监视其大小。

​    每当有新的数据块到达时，QAbstractSocket都会发出readyRead()信号。 您可以通过bytesAvailable()成员函数的返回值来获得当前读取缓冲区中可读取的字节数。 通常来讲，您可以将readyRead()信号与一个槽函数相连接，然后在该槽函数中读取所有可用的数据。 如果您不一次性读取所有数据，则其余数据以后仍可以读取，并且任何新的传入数据都将追加到QAbstractSocket的内部读取缓冲区中。您可以通过调用setReadBufferSize()成员函数来限制读取缓冲区的大小。

​    您可以通过调用disconnectFromHost()成员函数关闭套接字。 调用disconnectFromHost()成员函数后，QAbstractSocket会进入*关闭中*（*QAbstractSocket :: ClosingState*）状态。 待所有未处理数据写入套接字后，QAbstractSocket将关闭套接字，进入*未连接*（*QAbstractSocket :: UnconnectedState*）状态，并发送disconnected()信号。 如果要立即中止连接，并丢弃所有未处理数据，请调用abort()成员函数。 如果远程主机关闭了该连接，QAbstractSocket将发出errorOccurred(QAbstractSocket :: RemoteHostClosedError)错误信号，在此期间套接字状态仍为*已连接*（*QAbstractSocket :: ConnectedState*）状态，此后将发送disconnected()信号。

​    您可以通过调用peerPort()和peerAddress()成员函数来获取已连接的对等方的端口和地址。 peerName()成员函数则会返回传递给connectToHost()的对等方的主机名。 另外，localPort()和localAddress()成员函数可返回本地套接字的端口和地址。

​    QAbstractSocket提供了一组函数，这些函数可以挂起调用线程，直到发出某些信号为止。 这些函数可用于实现阻塞套接字：

    * waitForConnected() 阻塞套接字直到一个新的连接建立
    * waitForReadyRead() 阻塞套接字直到有新的数据可以读取
    * waitForBytesWritten() 阻塞套接字直到一个有效的荷载数据写入到了套接字
    * waitForDisconnected() 阻塞套接字直到连接已经关闭

​    Qt官方提供了如下示例：

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

​    如果waitForReadyRead()成员函数返回值为*false*，则说明连接已关闭或发生了错误。

​    使用阻塞套接字进行编程与使用非阻塞套接字进行编程完全不同。 阻塞套接字不需要有一个事件循环，这通常可以简化代码。 但是，在GUI应用程序中，阻塞套接字只能在非GUI线程中使用，以避免冻结用户界面。 有关这两种方法的概述，请参见fortuneclient和blockingfortuneclient示例。

​    **注意：**Qt官方并不推荐将阻塞函数与信号一起使用。

​    QAbstractSocket可以与QTextStream和QDataStream的流运算符（operator<<() 和operator>>()）一起使用。 但是，有一个问题需要注意：在尝试使用operator>>() 读取数据之前，必须确保有足够的数据可用。

​    您也可以在QNetworkAccessManager类和QTcpServer类的文档中找到一部分相关的信息。



## 成员类型文档

### enum **QAbstractSocket**::BindFlag | flags **QAbstractSocket**::BindMode

该枚举描述了一些不同的标志，这些标志可以传递为bind()成员函数的参数，指定了不同的主机绑定模式。

| 常量                                |  值  | 描述                                                         |
| :---------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::ShareAddress       | 0x1  | 允许其他服务绑定到相同的地址和端口。 在多个进程通过侦听相同的地址和端口来分担单个服务的负载的情况下（例如，具有多个预分支侦听器的Web服务器可以大大缩短响应时间），该模式十分有效。 但是，由于该模式下允许任何服务对主机进行重新绑定，因此此选项存在着安全隐患。 请注意，您还可以允许您的服务重新绑定现有的共享地址通过将此选项与*QAbstractSocket::ReuseAddressHint*结合使用。 在Unix上，这等效于SO_REUSEADDR套接字选项。 在Windows上，这是默认行为，因此将忽略此选项。 |
| QAbstractSocket::DontShareAddress   | 0x2  | 绑定主机时独占地址和端口，不允许其他服务重新绑定。 将此选项作为QAbstractSocket :: bind()参数，可以确保在绑定主机成功后，您当前的服务是唯一侦听指定地址和端口的服务。 即使其他服务通过指定*QAbstractSocket::ReuseAddressHint*模式来绑定服务，这个操作也是不允许的。 该模式相比*QAbstractSocket::ShareAddress*提供了更高的安全性，但是在某些操作系统上，它要求您以管理员权限运行该服务。 在Unix和macOS上，独占地址和端口是绑定主机的默认行为，因此该选项将被忽略。 在Windows上，此选项使用SO_EXCLUSIVEADDRUSE套接字选项。 |
| QAbstractSocket::ReuseAddressHint   | 0x4  | 示意QAbstractSocket即使地址和端口已被另一个套接字绑定，它也应尝试重新绑定服务。 在Windows和Unix上，这等效于SO_REUSEADDR套接字选项。 |
| QAbstractSocket::DefaultForPlatform | 0x0  | 使用当前平台的默认模式。 在Unix和macOS上，这等效于（*QAbstractSocket::DontShareAddress* + *QAbstractSocket::ReuseAddressHint*），在Windows上，它等效于*QAbstractSocket::ShareAddress*。 |

​    该枚举最初在Qt5.0版本引入。

​     BindMode类型是typedef QFlags <BindFlag>生成的用户自定义类型。 它存储着BindFlag值的OR组合。



### enum **QAbstractSocket**::NetworkLayerProtocol

该枚举描述了Qt中可以使用的网络层协议。

| 常量                                         |  值  | 描述                   |
| :------------------------------------------- | :--: | :--------------------- |
| QAbstractSocket::IPv4Protocol                |  0   | IPv4                   |
| QAbstractSocket::IPv6Protocol                |  1   | IPv6                   |
| QAbstractSocket::AnyIPProtocol               |  2   | IPv4 或 IPv6           |
| QAbstractSocket::UnknownNetworkLayerProtocol |  -1  | 除IPv4和IPv6之外的协议 |

​    您也可以在QHostAddress::protocol()中找到有关网络层协议的相关知识。



### enum **QAbstractSocket**::PauseMode | flags **QAbstractSocket**::PauseModes

该枚举描述了套接字在什么情况下该停止传输中的数据。 当前Qt支持的唯一通知是QSslSocket :: sslErrors()。

| 常量                              |  值  | 描述                                                         |
| :-------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::PauseNever       | 0x0  | “永远”不暂停套接字上的数据传输。 该模式是默认设置，符合Qt 4的标准。 |
| QAbstractSocket::PauseOnSslErrors | 0x1  | 收到SSL错误（即 QSslSocket :: sslErrors()）的通知后，暂停套接字上的数据传输。 |

​    该枚举最初在Qt5.0版本引入。

​    PauseModes类型是typedef QFlags<PauseMode>生成的用户自定义类型。它储存着PauseMode值的OR组合。



### enum **QAbstractSocket**::SocketError

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
| QAbstractSocket::AddressInUseError                |  8   | QAbstractSocket::bind()指定的主机地址已被另一个套接字使用独占模式绑定。 |
| QAbstractSocket::SocketAddressNotAvailableError   |  9   | QAbstractSocket :: bind()指定的主机地址不属于主机。          |
| QAbstractSocket::UnsupportedSocketOperationError  |  10  | 本地操作系统不支持请求的套接字操作（例如，缺少IPv6支持）。   |
| QAbstractSocket::ProxyAuthenticationRequiredError |  12  | 套接字正在使用代理，并且代理需要身份验证。                   |
| QAbstractSocket::SslHandshakeFailedError          |  13  | SSL / TLS握手失败，因此连接已关闭（仅在QSslSocket中使用）。  |
| QAbstractSocket::UnfinishedSocketOperationError   |  11  | 仅由QAbstractSocketEngine使用，上一次尝试的操作尚未完成（仍在后台进行）。 |
| QAbstractSocket::ProxyConnectionRefusedError      |  14  | 代理服务器拒绝了连接。                                       |
| QAbstractSocket::ProxyConnectionClosedError       |  15  | 与代理服务器的连接意外关闭（在建立与对方的最终连接之前）。   |
| QAbstractSocket::ProxyConnectionTimeoutError      |  16  | 与代理服务器的连接超时或代理服务器在身份验证阶段停止响应。   |
| QAbstractSocket::ProxyNotFoundError               |  17  | 找不到使用setProxy()（或应用程序代理）设置的代理地址。       |
| QAbstractSocket::ProxyProtocolError               |  18  | 与代理服务器通信失败，因为无法理解来自代理服务器的响应，这通常是代理服务协议错误的锅。 |
| QAbstractSocket::OperationError                   |  19  | 套接字所处的状态不允许该操作                                 |
| QAbstractSocket::SslInternalError                 |  20  | 使用的SSL库出现内部错误。 这可能是由于SSl库安装错误或配置错误造成的。 |
| QAbstractSocket::SslInvalidUserDataError          |  21  | 提供了无效的数据（证书，密钥，密码等），其使用导致SSL库出现错误。 |
| QAbstractSocket::TemporaryError                   |  22  | 发生临时错误（例如，操作将阻塞套接字，而套接字未阻塞）。     |
| QAbstractSocket::UnknownSocketError               |  -1  | 神了，出现了一个未知错误。                                   |

​    您也可以在QAbstractSocket::error() 和 QAbstractSocket::errorOccurred() 成员函数的详细介绍中找到一部分套接字错误的介绍。



### enum **QAbstractSocket**::SocketOption

该枚举表示可以在套接字上设置的选项。 如果需要设置这些选项，您可以在套接字接收到connectd（）信号之后，或者在QTcpServer接收到新的套接字之后，对它们进行设置。

| 常量                                           |  值  | 描述                                                         |
| :--------------------------------------------- | :--: | :----------------------------------------------------------- |
| QAbstractSocket::LowDelayOption                |  0   | 尝试优化套接字以降低延迟。 对于QTcpSocket，这将设置TCP_NODELAY选项并禁用Nagle的算法。 将此设置为1启用。 |
| QAbstractSocket::KeepAliveOption               |  1   | 将此设置为1以启用SO_KEEPALIVE套接字选项                      |
| QAbstractSocket::MulticastTtlOption            |  2   | 将此设置为整数值以设置IP_MULTICAST_TTL（多播数据报的TTL）套接字选项。 |
| QAbstractSocket::MulticastLoopbackOption       |  3   | 将此设置为1以启用IP_MULTICAST_LOOP（多播环回）套接字选项。   |
| QAbstractSocket::TypeOfServiceOption           |  4   | Windows不支持此选项。 这映射到IP_TOS套接字选项。 有关其可能的可取值，请参见下表。 |
| QAbstractSocket::SendBufferSizeSocketOption    |  5   | 在操作系统级别设置套接字发送缓冲区的大小（以字节为单位）。 这映射到SO_SNDBUF套接字选项。 该选项不会影响QIODevice或QAbstractSocket缓冲区。 这个枚举值在Qt 5.3中引入。 |
| QAbstractSocket::ReceiveBufferSizeSocketOption |  6   | 在操作系统级别设置套接字接收缓冲区的大小（以字节为单位）。 这映射到SO_RCVBUF套接字选项。 此选项不会影响QIODevice或QAbstractSocket缓冲区（请参见setReadBufferSize()）。 这个枚举值已在Qt 5.3中引入。 |
| QAbstractSocket::PathMtuSocketOption           |  7   | 检索IP堆栈当前已知的路径最大传输单位（PMTU）值（如果该值存在）。 一些IP堆栈还允许设置MTU进行传输。 这个枚举值在Qt 5.11中引入。 |

​    *TypeOfServiceOption* 可能的可取值（优先级）：

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

​    该枚举最初在Qt4.6版本引入。

​    您也可以在QAbstractSocket::setSocketOption() 和 QAbstractSocket::socketOption()函数介绍中找到相关内容。



### enum **QAbstractSocket**::SocketState

该枚举描述了套接字不同的状态。

| 常量                              | Value | Description                                       |
| :-------------------------------- | :---: | :------------------------------------------------ |
| QAbstractSocket::UnconnectedState |   0   | 套接字未连接。                                    |
| QAbstractSocket::HostLookupState  |   1   | The socket is performing a host name lookup.      |
| QAbstractSocket::ConnectingState  |   2   | The socket has started establishing a connection. |
| QAbstractSocket::ConnectedState   |   3   | A connection is established.                      |
| QAbstractSocket::BoundState       |   4   | 套接字已绑定到一个地址和端口。                    |
| QAbstractSocket::ClosingState     |   6   | 套接字即将关闭（数据可能仍在等待写入）。          |
| QAbstractSocket::ListeningState   |   5   | 套接字仅限内部使用。                              |

​    您也可以在QAbstractSocket::state()成员函数介绍中找到相关内容。



### enum **QAbstractSocket**::SocketType

该枚举描述了传输层的协议。

| Constant                           | Value | Description                  |
| :--------------------------------- | :---: | :--------------------------- |
| QAbstractSocket::TcpSocket         |   0   | TCP                          |
| QAbstractSocket::UdpSocket         |   1   | UDP                          |
| QAbstractSocket::SctpSocket        |   2   | SCTP                         |
| QAbstractSocket::UnknownSocketType |  -1   | 除 TCP, UDP 和 SCTP 外的协议 |

​    您也可以在QAbstractSocket::socketType()成员函数介绍中找到相关内容。



## 成员函数文档

### QAbstractSocket::QAbstractSocket(QAbstractSocket::SocketType *socketType*, QObject **parent*)

创建一个新抽象套接字socketType。 函数中父对象的参数传递给QObject的构造函数。

​    这就是它的构造函数嘛，没啥好说的。另外由于QAbstractSocket类继承自QObject类，应注意在QAbstractSocket类构造函数中调用一下父类QObject类的构造函数。

​    另外您也可以在socketType()成员函数文档，以及 QTcpSocket和QUdpSocket类文档找到相关信息。



### *[SIGNAL]* void QAbstractSocket::connected()

connecToHost()调用并成功建立一个连接后，QAbstractSocket类将发送connected()信号。

​    **注意：**在某些操作系统上，connected()信号可能直接从connectToHost()调用发出，以连接到本地主机。

​    另外您也可以在connecToHost() 和 disconnected() 成员函数文档中找到相关信息。



### *[SIGNAL]* void QAbstractSocket::disconnected()