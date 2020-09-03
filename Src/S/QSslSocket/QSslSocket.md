[TOC]

# QSslSocket Class

QSslSocket 类为客户端和服务端提供了一个 SSL 加密的套接字。

| 属性   | 方法                    |
| ------ | ----------------------- |
| 头文件 | `#include <QSslSocket>` |
| qmake  | QT += network           |
| 引入   | Qt4.3                   |
| 继承自 | QTcpSocket              |

该类最初在 Qt4.3 版本引入。

您可以在 [QSslSocket_Obsolete](../QSslSocket_Obsolete/QSslSocket_Obsolete.md) 界面找到过时的成员函数介绍。

**注意：** 该类所有的函数都是可重入的。



## 公共成员类型

| 类型 | 属性                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[PeerVerifyMode](#enum-qsslsocketpeerverifymode)** { VerifyNone, QueryPeer, VerifyPeer, AutoVerifyPeer } |
| enum | **[SslMode](#enum-qsslsocketsslmode)** { UnencryptedMode, SslClientMode, SslServerMode } |



## 公共成员函数

| 类型                       | 函数名                                                       |
| -------------------------- | ------------------------------------------------------------ |
|                            | **[QSslSocket](#qsslsocketqsslsocketqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual                    | **[~QSslSocket](#virtual-qsslsocketqsslsocket)**()           |
| void                       | **[abort](#void-qsslsocketabort)**()                         |
| void                       | **[connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)**(const QString &*hostName*, quint16 *port*, QIODevice::OpenMode *mode* = ReadWrite, QAbstractSocket::NetworkLayerProtocol *protocol* = AnyIPProtocol) |
| void                       | **[connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-const-qstring-sslpeername-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)**(const QString &*hostName*, quint16 *port*, const QString &*sslPeerName*, QIODevice::OpenMode *mode* = ReadWrite, QAbstractSocket::NetworkLayerProtocol *protocol* = AnyIPProtocol) |
| qint64                     | **[encryptedBytesAvailable](#qint64-qsslsocketencryptedbytesavailable-const)**() const |
| qint64                     | **[encryptedBytesToWrite](#qint64-qsslsocketencryptedbytestowrite-const)**() const |
| bool                       | **[flush](#bool-qsslsocketflush)**()                         |
| void                       | **[ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)**(const QList\<QSslError\> &*errors*) |
| bool                       | **[isEncrypted](#bool-qsslsocketisencrypted-const)**() const |
| QSslCertificate            | **[localCertificate](#qsslcertificate-qsslsocketlocalcertificate-const)**() const |
| QList\<QSslCertificate\>   | **[localCertificateChain](#qlistqsslcertificate-qsslsocketlocalcertificatechain-const)**() const |
| QSslSocket::SslMode        | **[mode](#qsslsocketsslmode-qsslsocketmode-const)**() const  |
| QVector\<QOcspResponse\>   | **[ocspResponses](#qvectorqocspresponse-qsslsocketocspresponses-const)**() const |
| QSslCertificate            | **[peerCertificate](#qsslcertificate-qsslsocketpeercertificate-const)**() const |
| QList\<QSslCertificate\>   | **[peerCertificateChain](#qlistqsslcertificate-qsslsocketpeercertificatechain-const)**() const |
| int                        | **[peerVerifyDepth](#int-qsslsocketpeerverifydepth-const)**() const |
| QSslSocket::PeerVerifyMode | **[peerVerifyMode](#qsslsocketpeerverifymode-qsslsocketpeerverifymode-const)**() const |
| QString                    | **[peerVerifyName](#qstring-qsslsocketpeerverifyname-const)**() const |
| QSslKey                    | **[privateKey](#qsslkey-qsslsocketprivatekey-const)**() const |
| QSsl::SslProtocol          | **[protocol](#qsslsslprotocol-qsslsocketprotocol-const)**() const |
| QSslCipher                 | **[sessionCipher](#qsslcipher-qsslsocketsessioncipher-const)**() const |
| QSsl::SslProtocol          | **[sessionProtocol](#qsslsslprotocol-qsslsocketsessionprotocol-const)**() const |
| void                       | **[setLocalCertificate](#void-qsslsocketsetlocalcertificateconst-qsslcertificate-certificate)**(const QSslCertificate &*certificate*) |
| void                       | **[setLocalCertificate](#void-qsslsocketsetlocalcertificateconst-qstring-path-qsslencodingformat-format--qsslpem)**(const QString &*path*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| void                       | **[setLocalCertificateChain](#void-qsslsocketsetlocalcertificatechainconst-qlistqsslcertificate-localchain)**(const QList\<QSslCertificate\> &*localChain*) |
| void                       | **[setPeerVerifyDepth](#void-qsslsocketsetpeerverifydepthint-depth)**(int *depth*) |
| void                       | **[setPeerVerifyMode](#void-qsslsocketsetpeerverifymodeqsslsocketpeerverifymode-mode)**(QSslSocket::PeerVerifyMode *mode*) |
| void                       | **[setPeerVerifyName](#void-qsslsocketsetpeerverifynameconst-qstring-hostname)**(const QString &*hostName*) |
| void                       | **[setPrivateKey](#void-qsslsocketsetprivatekeyconst-qsslkey-key)**(const QSslKey &*key*) |
| void                       | **[setPrivateKey](#void-qsslsocketsetprivatekeyconst-qstring-filename-qsslkeyalgorithm-algorithm--qsslrsa-qsslencodingformat-format--qsslpem-const-qbytearraypassphrase--qbytearray)**(const QString &*fileName*, QSsl::KeyAlgorithm *algorithm* = QSsl::Rsa, QSsl::EncodingFormat *format* = QSsl::Pem, const QByteArray &*passPhrase* = QByteArray()) |
| void                       | **[setProtocol](#void-qsslsocketsetprotocolqsslsslprotocol-protocol)**(QSsl::SslProtocol *protocol*) |
| void                       | **[setSslConfiguration](#void-qsslsocketsetsslconfigurationconst-qsslconfiguration-configuration)**(const QSslConfiguration &*configuration*) |
| QSslConfiguration          | **[sslConfiguration](#qsslconfiguration-qsslsocketsslconfiguration-const)**() const |
| QList\<QSslError\>         | **[sslHandshakeErrors](#qlistqsslerror-qsslsocketsslhandshakeerrors-const)**() const |
| bool                       | **[waitForEncrypted](#bool-qsslsocketwaitforencryptedint-msecs--30000)**(int *msecs* = 30000) |



## 重写公共成员函数

| 类型             | 函数名                                                       |
| ---------------- | ------------------------------------------------------------ |
| virtual bool     | **[atEnd](#override-virtual-bool-qsslsocketatend-const)**() const override |
| virtual qint64   | **[bytesAvailable](#override-virtual-qint64-qsslsocketbytesavailable-const)**() const override |
| virtual qint64   | **[bytesToWrite](#override-virtual-qint64-qsslsocketbytestowrite-const)**() const override |
| virtual bool     | **[canReadLine](#override-virtual-bool-qsslsocketcanreadline-const)**() const override |
| virtual void     | **[close](#override-virtual-void-qsslsocketclose)**() override |
| virtual void     | **[resume](#override-virtual-void-qsslsocketresume)**() override |
| virtual void     | **[setReadBufferSize](#override-virtual-void-qsslsocketsetreadbuffersizeqint64-size)**(qint64 *size*) override |
| virtual bool     | **[setSocketDescriptor](#override-virtual-qvariant-qsslsocketsocketoptionqabstractsocketsocketoption-option)**(qintptr *socketDescriptor*, QAbstractSocket::SocketState *state* = ConnectedState, QIODevice::OpenMode *openMode* = ReadWrite) override |
| virtual void     | **[setSocketOption](#override-virtual-qvariant-qsslsocketsocketoptionqabstractsocketsocketoption-option)**(QAbstractSocket::SocketOption *option*, const QVariant &*value*) override |
| virtual QVariant | **[socketOption](#override-virtual-qvariant-qsslsocketsocketoptionqabstractsocketsocketoption-option)**(QAbstractSocket::SocketOption *option*) override |
| virtual bool     | **[waitForBytesWritten](#override-virtual-bool-qsslsocketwaitforbyteswrittenint-msecs--30000)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForConnected](#override-virtual-bool-qsslsocketwaitforconnectedint-msecs--30000)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForDisconnected](#override-virtual-bool-qsslsocketwaitfordisconnectedint-msecs--30000)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForReadyRead](#override-virtual-bool-qsslsocketwaitforreadyreadint-msecs--30000)**(int *msecs* = 30000) override |



## 公共槽函数

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)**() |
| void | **[startClientEncryption](#slot-void-qsslsocketstartclientencryption)**() |
| void | **[startServerEncryption](#slot-void-qsslsocketstartserverencryption)**() |



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[encrypted](#signal-void-qsslsocketencrypted)**()          |
| void | **[encryptedBytesWritten](#signal-void-qsslsocketencryptedbyteswrittenqint64-written)**(qint64 *written*) |
| void | **[modeChanged](#signal-void-qsslsocketmodechangedqsslsocketsslmode-mode)**(QSslSocket::SslMode *mode*) |
| void | **[newSessionTicketReceived](#signal-void-qsslsocketnewsessionticketreceived)**() |
| void | **[peerVerifyError](#signal-void-qsslsocketpeerverifyerrorconst-qsslerror-error)**(const QSslError &*error*) |
| void | **[preSharedKeyAuthenticationRequired](#signal-void-qsslsocketpresharedkeyauthenticationrequiredqsslpresharedkeyauthenticator-authenticator)**(QSslPreSharedKeyAuthenticator **authenticator*) |
| void | **[sslErrors](#signal-void-qsslsocketsslerrorsconst-qlistqsslerror-errors)**(const QList\<QSslError\> &*errors*) |



### 静态成员函数

| 类型    | 函数名                                                       |
| ------- | ------------------------------------------------------------ |
| long    | **[sslLibraryBuildVersionNumber](#static-long-qsslsocketssllibrarybuildversionnumber)**() |
| QString | **[sslLibraryBuildVersionString](#static-qstring-qsslsocketssllibrarybuildversionstring)**() |
| long    | **[sslLibraryVersionNumber](#static-long-qsslsocketssllibraryversionnumber)**() |
| QString | **[sslLibraryVersionString](#static-long-qsslsocketssllibraryversionnumber)**() |
| bool    | **[supportsSsl](#static-bool-qsslsocketsupportsssl)**()      |



## 重写保护成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual qint64 | **[readData](#override-virtual-protected-qint64-qsslsocketreaddatachar-data-qint64-maxlen)**(char **data*, qint64 *maxlen*) override |
| virtual qint64 | **[writeData](#override-virtual-protected-qint64-qsslsocketwritedataconst-char-data-qint64-len)**(const char **data*, qint64 *len*) override |



## 详细介绍

QSslSocket 能够建立一个安全的、加密的 TCP 连接，您可以使用该连接来传输加密数据。在服务器端和客户端都可以使用它，并且他支持现代的 SSL 协议，包括 SSL 3 和 TLS 1.2。默认情况下，QSslSocket 仅仅使用被认为是安全的（ [QSsl::SecureProtocols](../QSsl/QSsl.md#enum-qsslsslprotocol) ） SSL 协议，但是只要处在握手开始之前，您仍然可以调用 [setProtocol](#void-qsslsocketsetprotocolqsslsslprotocol-protocol)() 函数来更改 SSL 协议。

在套接字进入 *已连接*（[ConnectedState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ）状态后，SSL 将在现有 TCP 流上进行加密。有两种使用 QSslSocket 建立安全连接的简单方法：使用即时 SSL 握手，或在未加密模式下建立连接之后的延迟 SSL 握手。

最常见的 QSslSocket 使用方法是构造一个对象后使用 [connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 函数开启一个安全连接，这种方法会在连接建立后开启一个即时的 SSL 握手。

```cpp
 QSslSocket *socket = new QSslSocket(this);
 connect(socket, SIGNAL(encrypted()), this, SLOT(ready()));

 socket->connectToHostEncrypted("imap.example.com", 993);
```

与普通的 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 相同，若成功建立连接， QSslSocket 会依次进入 [HostLookupState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ，[ConnectingState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) 和 [ConnectedState]((../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate)) 状态。连接成功后，握手会自动开始，若握手连接成功，QSsslSocket 将会发送 [encrypted](#signal-void-qsslsocketencrypted)() 信号，表明该套接字已经进入加密状态并准备好使用。

请注意，在 [connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 函数执行完成返回后（即 [encrypted](#signal-void-qsslsocketencrypted)() 信号发出之前）数据就可以立即写入套接字。此时写入到套接字的数据将会被加入等待队列，直到 [encrypted](#signal-void-qsslsocketencrypted)() 信号被发出。

使用延迟 SSL 握手来保护现有连接的示例是 SSL 服务器保护传入连接。

假设您继承 [QTcpServer](../../T/QTcpServer/QTcpServer.md) 类创建了一个 SSL 服务器类。您需要如下例重写 [QTcpServer::incomingConnection](../../T/QTcpServer/QTcpServer.md#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor)() ：首先构造一个 QSslSocket 对象并调用 [setSocketDescriptor](#override-virtual-qvariant-qsslsocketsocketoptionqabstractsocketsocketoption-option)() 函数将新的套接字描述符设置为传入的已有的套接字描述符。然后调用 [startServerEncryption](#slot-void-qsslsocketstartserverencryption)() 函数初始化 SSL 握手。

```cpp
 void SslServer::incomingConnection(qintptr socketDescriptor)
 {
     QSslSocket *serverSocket = new QSslSocket;
     if (serverSocket->setSocketDescriptor(socketDescriptor)) {
         addPendingConnection(serverSocket);
         connect(serverSocket, &QSslSocket::encrypted, this, &SslServer::ready);
         serverSocket->startServerEncryption();
     } else {
         delete serverSocket;
     }
 }
```

如果出现了错误， QSslSocket 将会发出 [sslErrors](#signal-void-qsslsocketsslerrorsconst-qlistqsslerror-errors)() 信号。在这种情况下，如果没有采取任何操作去忽略出现的错误，该连接将会掉线。若要出现错误后仍然继续维持连接，您可以在错误发生后的槽函数中，或者 QSslSocket 对象构建后、尝试连接之前，调用 [ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数。[ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数将允许 QSslSocket 忽略在建立对等方身份时遇到的错误。 应谨慎使用 [ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数忽略SSL握手期间的错误，因为安全连接的基本特征是应该通过成功的握手来建立它们。

连接加密后，您可以像普通的 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 类一样使用 QSslSocket。当 readyRead() 信号发出后，您可以调用 read()，[canReadLine](#override-virtual-bool-qsslsocketcanreadline-const)() 和 readLine() 或者 getChar() 从 QSslSocket 的内部缓冲区中读取加密数据，然后您可以调用 write() 或者 putChar() 向对等端写回数据。 QSslSocket 将会自动将您写入的数据加密并在数据写入到对等端后发送 [encryptedBytesWritten](#signal-void-qsslsocketencryptedbyteswrittenqint64-written)() 信号。

方便起见，QSslSocket 支持 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 的阻塞函数：[waitForConnected](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketwaitforconnectedint-msecs--30000)()，[waitForReadyRead](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-bool-qabstractsocketwaitforreadyreadint-msecs--30000)()，[waitForBytesWritten](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-bool-qabstractsocketwaitforbyteswrittenint-msecs--30000)() 和 [waitForDisconnected](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketwaitfordisconnectedint-msecs--30000)()。它也提供了 [waitForEncrypted](#bool-qsslsocketwaitforencryptedint-msecs--30000)() 函数来在加密连接建立之前阻塞调用的线程。

```cpp
 QSslSocket socket;
 socket.connectToHostEncrypted("http.example.com", 443);
 if (!socket.waitForEncrypted()) {
     qDebug() << socket.errorString();
     return false;
 }

 socket.write("GET / HTTP/1.0\r\n\r\n");
 while (socket.waitForReadyRead())
     qDebug() << socket.readAll().data();
```

QSslSocket 提供了广泛的、易于使用的 API ，用于处理密码，私钥以及本地，对等端和证书颁发机构（CA）证书。它也为处理握手阶段出现的错误提供了 API 支持。

以下的特性也可以被客制化：

- 套接字的加密密码套件可以在握手阶段之前通过 [QSslConfiguration :: setCiphers](qthelp：//org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() 和 QSslConfiguration :: setDefaultCiphers() 定制。
- 套接字的本地证书和私钥可以在握手阶段之前通过 [setLocalCertificate](#void-qsslsocketsetlocalcertificateconst-qsslcertificate-certificate)() 和 [setPrivateKey](#void-qsslsocketsetprivatekeyconst-qsslkey-key)() 设置。
- CA 证书数据可以通过 [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)() 和 [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)() 扩展和定制。

要扩展在 SSL 握手期间 SSL 套接字使用的*默认* CA 证书列表，您必须像下面的代码片段一样更新默认配置：

```cpp
 QList<QSslCertificate> certificates = getCertificates();
 QSslConfiguration configuration = QSslConfiguration::defaultConfiguration();
 configuration.addCaCertificates(certificates);
 QSslConfiguration::setDefaultConfiguration(configuration);
```

**注意：** 在 Unix 系统（ macOS 除外）下，如果可能的话，QSslSocket 将从标准证书目录中按需加载根证书。如果您不想按需家在根证书，则您需要在应用程序进行首次 SSL 握手之前（例如通过 QSslSocket::systemCaCertificates() 传递证书）调用 [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)()::setCaCertificates() ，或者在您的 QSslSocket 实例进行 SSL 握手前调用 [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)()::setCaCertificates() 。

您也可以在 [QSslCipher](../QSslCipher/QSslCipher.md) 和 [QSslCertificate](../QSslCertificate/QSslCertificate.md) 类文档中找到关于密钥与证书的信息。

该产品包括了由 OpenSSL Project 项目开发的，可在 OpenSSL Toolkit 工具包中使用的软件 (http://www.openssl.org/) 。

**注意：** 要注意 bytesWritten() 信号和 [encryptedBytesWritten](#signal-void-qsslsocketencryptedbyteswrittenqint64-written)() 信号之间的差别。 对于 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 类来说，一旦数据被写入到 TCP 套接字， bytesWritten() 信号就会被发出。 对 QSslSocket 类来说，当数据正在被加密时，bytesWritten() 信号将会被发出；当数据写入到 TCP 套接字后，[encryptedBytesWritten](#signal-void-qsslsocketencryptedbyteswrittenqint64-written)() 信号将会被发出。

另外您也可以在 [QSslCertificate](../QSslCertificate/QSslCertificate.md)，[QSslCipher](../QSslCipher/QSslCipher.md) 和 [QSslError](../QSslError/QSslError.md) 类文档中找到相关信息。

## 成员类型文档

### enum QSslSocket::**PeerVerifyMode**

描述了 QSslSocket 的对等端验证模式。默认模式为 *自动验证对等端* (*AutoVerifyPeer*)，该模式下将会根据 [QSslSocket::SslMode](#enum-qsslsocketsslmode) 选择一个合适的验证模式 。

| 常量                       | 值   | 描述                                                         |
| :------------------------- | :--- | :----------------------------------------------------------- |
| QSslSocket::VerifyNone     | 0    | QSslSocket 将不会请求对等端发送证书。如果您对连接的另一端的身份并不感兴趣，您可以使用该模式。连接依旧会被加密，如果对等端需要您的本地证书，套接字仍然会发送本地套接字到对等端。 |
| QSslSocket::QueryPeer      | 1    | QSslSocket 将会请求对等端发送一个证书，但是并不需要该证书有效。如果您想向用户展示对等端证书的详细信息，但是并不象影响实际的 SSL 握手，可以考虑使用该模式。该模式是服务器的默认模式。注意：在频道(Schannel)中该值与 QSslSocket::VerifyNone 效果相同。 |
| QSslSocket::VerifyPeer     | 2    | This mode is the default for clients.QSslSocket 将在握手阶段请求对等端发送一个有效的证书。如果失败，QSslSocket 将会发送 QSslSocket::[sslErrors](#signal-void-qsslsocketsslerrorsconst-qlistqsslerror-errors)() 信号。 |
| QSslSocket::AutoVerifyPeer | 3    | [QSslSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html) will automatically use QueryPeer for server sockets and VerifyPeer for client sockets.自动模式。服务端 QSslSocket 会自动使用 QueryPeer 模式，客户端 QSslSocket 会自动使用 AutoVerifyPeer 模式。 |

该枚举最初在 Qt 4.4 引入。

另外您也可以在 [QSslSocket::peerVerifyMode](#qsslsocketpeerverifymode-qsslsocketpeerverifymode-const)() 函数介绍中找到相关信息。

---

### enum QSslSocket::**SslMode**

描述了 QSslSocket 可用的连接模式。

| 常量                        | 值   | Description                                                  |
| :-------------------------- | :--- | :----------------------------------------------------------- |
| QSslSocket::UnencryptedMode | 0    | 未加密套接字，该行为与 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 相同。 |
| QSslSocket::SslClientMode   | 1    | 该套接字为客户端 SSL 套接字。它既可以已经被加密，也可以处于握手阶段（详情见 [QSslSocket::isEncrypted](#bool-qsslsocketisencrypted-const)() ）。 |
| QSslSocket::SslServerMode   | 2    | 该套接字为服务端 SSL 套接字。它既可以已经被加密，也可以处于握手阶段（详情见 [QSslSocket::isEncrypted](#bool-qsslsocketisencrypted-const)() ）。 |



## 成员函数文档

### QSslSocket::**QSslSocket**([QObject](../../O/QObject/QObject.md) **parent* = nullptr)

构造一个 QSslSocket 对象。*parent* 参数将传递给 [QObject](../../O/QObject/QObject.md) 构造函数。新套接字的密钥套件设置为静态方法 defaultCiphers() 返回的一个密钥。

---

### *[signal]* void **QSslSocket**::**encrypted**()

当 QSslSocket 进入加密模式时将发出该信号。该信号发送后， [QSslSocket::isEncrypted](#bool-qsslsocketisencrypted-const)() 将会返回 *true*，并且接下来套接字上的传输都将被加密。

另外您也可以在 [QSslSocket::connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 和 [QSslSocket::isEncrypted](#bool-qsslsocketisencrypted-const)() 函数介绍中找到相关信息。

---

### *[signal]* void **QSslSocket**::**encryptedBytesWritten**(qint64 *written*)

当 QSslSocket 将加密数据写入到网路后将会发出该信号。 *written* 参数包含着成功写入的字节书。

该函数最初在 Qt 4.4 版本引入。

另外您也可以在 QIODevice::bytesWritten() 函数介绍中找到相关信息。

---

### *[slot]* void **QSslSocket**::**ignoreSslErrors**()

该函数会让 QSslSocket 忽略握手期间的错误并继续连接。如果您想要让 QSslSocket 在握手期间即使出现错误仍继续链接，您必须在链接到 sslErrors() 信号的槽函数中调用该槽函数或者在握手阶段之前调用该槽函数。如果您不调用该函数，在 sslErrors() 信号发送后，无论是在回应错误期间还是在握手期间之前，连接都会断开。

如果 SSL 握手期间没有发生任何错误（即对等端的身份成功建立），QSslSocket 不会发送 sslErrors() 信号，因而在此时调用该函数是没有任何必要的。

**警告：** 确保始终让用户检查 sslErrors() 信号报告的错误，并且仅在用户确认可以继续进行操作时才调用此方法。如果发生了以外的错误，连接应当被取消。未经检查实际的错误就盲目的调用该函数会给您的应用程序带来极大的安全隐患。请谨慎使用该函数！

另外您也可以在 [sslErrors](#signal-void-qsslsocketsslerrorsconst-qlistqsslerror-errors)() 函数介绍中找到相关信息。

---

### *[signal]* void **QSslSocket**::**modeChanged**([QSslSocket::SslMode](#enum-qsslsocketsslmode) *mode*)

当 QSslSocket 从 [QSslSocket::UnencryptedMode](#enum-qsslsocketsslmode) 模式变为 [QSslSocket::SslClient](#enum-qsslsocketsslmode) 模式或者 [QSslSocket::SslServerMode](#enum-qsslsocketsslmode) 模式后会发出该信号。 参数 *mode* 即新的模式。

另外您也可以在 [mode](#qsslsocketsslmode-qsslsocketmode-const)() 函数介绍中找到相关信息。

### *[signal]* void **QSslSocket**::**newSessionTicketReceived**()

如果在握手期间协商了 TLS 1.3 协议，QSslSocket 会在接收到新的会话票据（ SessionTicket ）后发送该信号。会话和会话票据的生命周期的示意会在套接字的配置中更新。该会话可用于将来的 TLS 连接中的会话恢复（和缩短的握手）。

**注意：** 该功能仅支持 OpenSSL 后端，并要求 OpenSSL 版本 1.1.1及以上。

该函数最初在 Qt 5.15 版本引入。

另外您也可以在 QSslSocket::[sslConfiguration](#qsslconfiguration-qsslsocketsslconfiguration-const)()，QSslConfiguration::[sessionTicket]()() 和 QSslConfirguration::sessionTicketLifeTimeHint() 函数介绍中找到相关信息。

### *[signal]* void **QSslSocket**::**peerVerifyError**(const [QSslError](../QSslError/QSslError.md) &*error*)

QSslSocket 在握手期间、加密连接建立之前，可以多次发出该信号来表明对等端身份建立时出现错误。*error* 参通常表示了 QSslSocket 不能安全地鉴定对等端身份。

当遇到问题时该信号会给你提供早期的指示。通过连接该信号，您可以在连接的槽函数中在握手完成前手动结束该连接。如果该信号发送后未采取任何操作， QSslSocket 会继续发送 QSslSocket::sslErrors() 信号。

该函数最初在 Qt 4.4 版本引入。

另外您也可以在 [sslErrors](#signal-void-qsslsocketsslerrorsconst-qlistqsslerror-errors)() 函数介绍中找到相关信息。

### *[signal]* void **QSslSocket**::**preSharedKeyAuthenticationRequired**([QSslPreSharedKeyAuthenticator](../QSslPreSharedKeyAuthenticator/QSslPreSharedKeyAuthenticator.md) **authenticator*)

QSslSocket 在协商 PSK 密码套件时发出此信号，并且接下来会要求 PSK 身份验证。

当使用 PSK 时，为了使 SSL 握手继续执行，客户端必须向服务端发送一个有效的身份证明和一个有效的预分享密钥。应用程序可以通过一个连接到该信号的槽函数提供这些信息，根据他们的需求来填充传输的 *authenticator* 对象。

**注意：** 忽略该信号或者提供信用材料失败会造成握手失败，该连接也会因而被取消。

**注意：** *authenticator* 对象由该套接字所有并且不能被应用程序删除。

该函数最初在 Qt 5.5 版本引入。

另外您也可以在 [QSslPreSharedKeyAuthenticator](../QSslPreSharedKeyAuthenticator/QSslPreSharedKeyAuthenticator.md) 类文档中找到相关信息。

### *[signal]* void **QSslSocket**::**sslErrors**(const [QList](../../L/QList/QList.md)\<[QSslError](../QSslError/QSslError.md)\> &*errors*)

在握手期间，QSslSocket 会发送该信号表明在建立对等端身份鉴定的时候出现了一个或者多个错误。这些错误通常表明 QSslSocket 不能安全的鉴定对等端的身份。除非采取相关的操作，否则该连接将会在该信号发出后断开。

如果您想要忽略发生的错误并继续连接，您必须在连接到该信号的槽函数中调用 [QsslSocket::ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数。如果您想要在稍后获得错误列表，您可以调用 [sslHandshakeErrors](#qlistqsslerror-qsslsocketsslhandshakeerrors-const)() 函数。

*error* 参数包括着一个或者多个阻止 QSslSocket 验证对等端身份的错误。

**注意：** 连接该信号时，您不能使用 Qt::QueuedConnection 方式，否则调用 [QsslSocket::ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数将不会起任何作用。

**注意：** 信号 *sslErrors* 在该类中被重载。为了通过使用函数指针连接到该信号，Qt 提供了一个便捷的助手来包含函数指针，示例如下：

```cpp
connect(sslSocket, QOverload<const QList<QSslError> &>::of(&QSslSocket::sslErrors),
     [=](const QList<QSslError> &errors){ /* ... */ });
```

另外您也可以在 [peerVerifyError](#signal-void-qsslsocketpeerverifyerrorconst-qsslerror-error)() 函数介绍中找到相关信息。

### *[slot]* void **QSslSocket**::**startClientEncryption**()

为客户端连接开启一个 SSL 延迟握手。您可以在套接字处于**已连接**且仍然处于**未加密模式**时调用该槽函数。如果该套接字处于未连接状态或者该套接字已经进入加密模式，则该函数将不会生效。

重新实现了 STARTTLS 的客户端经常会利用延迟 SSL 握手。其他大部分客户端可以使用 [connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 函数来替代该函数，connectToHostEncrypted() 函数将会自动执行握手。

### *[slot]* void **QSslSocket**::**startServerEncryption**()

为服务端连接开启延迟 SSL 握手。您可以在套接字处于**已连接**且仍然处于**未加密模式**时调用该槽函数。如果该套接字处于未连接状态或者该套接字已经进入加密模式，则该函数将不会生效。

对于服务端套接字来说，调用该函数是初始化 SSL 握手的唯一方式。大多数服务端会在接收到一个连接、或者接收到一个进入 SSL 模式的指定协议指令（例如：服务端接收到 "STARTTLS\r\n"）时，立即调用该函数。

实现一个 SSL 服务器最常用的的方式是创建一个 [QTcpServer](../../T/QTcpServer/QTcpServer.md) 并且重新实现 [QTcpServer::incomingConnection()](../../T/QTcpServer/QTcpServer.md#virtual-protected-void-qtcpserverincomingconnectionqintptrsocketdescriptor) 函数。将返回的套接字描述符传递给 [QSslSOcket::setSocketDescriptor()](#override-virtual-qvariant-qsslsocketsocketoptionqabstractsocketsocketoption-option)。

另外您也可以在 [connectToHostEncrypted](#void-qsslsocketconnecttohostencryptedconst-qstring-hostname-quint16-port-qiodeviceopenmode-mode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 和 [startClientEncryption](#slot-void-qsslsocketstartclientencryption)() 函数介绍中找到相关信息。

### *[virtual]* **QSslSocket**::**~QSslSocket**()

析构函数。销毁 QSslSocket 对象。

### void **QSslSocket**::**abort**()

关闭连接并将套接字重新初始化。不像 [disconnectFromHost](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketdisconnectfromhost)() 函数，该还书会立即关闭套接字，并清空任何在写入缓冲区的数据。

另外您也可以在 [disconnectFromHost](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketdisconnectfromhost)() 和 [close](#override-virtual-void-qsslsocketclose)() 函数介绍中找到相关信息。

### *[override virtual]* bool **QSslSocket**::**atEnd**() const

重新实现：[QAbstractSocket::atEnd](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-bool-qabstractsocketatend-const)() 。

### *[override virtual]* qint64 **QSslSocket**::**bytesAvailable**() const

重新实现：[QAbstractSocket::bytesAvailable](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-qint64-qabstractsocketbytesavailable-const)()。

返回可以立即读取的已解密数据的字节数。

### *[override virtual]* qint64 **QSslSocket**::**bytesToWrite**() const

重新实现：[QAbstractSocket::bytesToWrite](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-qint64-qabstractsocketbytestowrite-const)()。

返回等待被加密和写入到网络的未加密数据的字节数。

### *[override virtual]* bool **QSslSocket**::**canReadLine**() const

重新实现：[QAbstractSocket::canReadLine](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-bool-qabstractsocketcanreadline-const)()。

若能读取一行已解密的数据（以一个 ASCII 字符 '\n' 结束 ）则返回 true，否则返回 false 。

### *[override virtual]* void **QSslSocket**::**close**()

重新实现：[QAbstractSocket::close](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-void-qabstractsocketclose)()。

### void **QSslSocket**::**connectToHostEncrypted**(const [QString](../../S/QString/QString.md) &*hostName*, quint16 *port*, [QIODevice::OpenMode]() *mode* = ReadWrite, [QAbstractSocket::NetworkLayerProtocol](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketnetworklayerprotocol) *protocol* = AnyIPProtocol)

使用 *mode* 指定的 [OpenMode]()，在 *hostName* 指定的主机的 *port* 指定的端口上启动一个加密连接。该函数的作用与调用 [connectToHost](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)() 函数建立连接然后使用 [startClientEncryption](#slot-void-qsslsocketstartclientencryption)() 函数相同。*protocol* 参数可以用来指定网络协议（例如 IPv4 或者 IPv6）。

QSslSocket 首先会进入*查询主机*（[HostLookupState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate)）状态。然后，套接字会进入事件循环或者一个 waitFor...() 函数，进入*连接中*（[ConnectingState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate)）状态，连接成功后，套接字会发出 [connected](../../A/QAbstractSocket/QAbstractSocket.md#signal-void-qabstractsocketconnected)() 信号。紧接着套接字会初始化 SSL 客户端握手。每次状态发生改变后， QSslSocket 都会发出 [stateChanged](../../A/QAbstractSocket/QAbstractSocket.md#signal-void-qabstractsocketstatechangedqabstractsocketsocketstate-socketstate)() 信号。

初始化 SSL 客户端握手后，若对等端身份认证未能成功建立，套接字将会发出 sslErrors() 信号。如果你想忽略出现的错误并继续连接，您必须在连接到 sslErrors() 信号的槽函数中或者在进入加密模式之前调用 [ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数。如果没有调用 [ignoreSslErrors](#void-qsslsocketignoresslerrorsconst-qlistqsslerror-errors)() 函数，该连接将会断开，并发出 [disconnected](../../A/QAbstractSocket/QAbstractSocket.md#signal-void-qabstractsocketdisconnected)() 信号，返回到*未连接*（[UnconnectedState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate)）状态。

若 SSL 握手连接建立成功，套接字将会发出 [encrypted](#signal-void-qsslsocketencrypted)() 信号。

```cpp
QSslSocket socket;
connect(&socket, SIGNAL(encrypted()), receiver, SLOT(socketEncrypted()));

socket.connectToHostEncrypted("imap", 993);
socket->write("1 CAPABILITY\r\n");
```

**注意：** 上面的例子中文本可以在请求加密连接之后、 [encrypted](#signal-void-qsslsocketencrypted)() 信号发出之前立即写入套接字中。在这种情况下，文本将会在对象中队列，并在连接建立且 [encrypted](#signal-void-qsslsocketencrypted)() 信号发出后写入到套接字中。

*mode* 参数的默认值为*读写* （[ReadWrite]()）。

如果您想在服务器端创建一个 QSslSocket，您应该在 [QTcpServer](../../T/QTcpServer/QTcpServer.md) 接收到新接入连接后调用 [startServerEncryption](#slot-void-qsslsocketstartserverencryption)() 函数。

另外您也可以在 [connectToHost](../../A/QAbstractSocket/QAbstractSocket.md#virtual-void-qabstractsocketconnecttohostconst-qstring-hostname-quint16-port-qiodeviceopenmode-openmode--readwrite-qabstractsocketnetworklayerprotocol-protocol--anyipprotocol)()，[startClientEncryption](#slot-void-qsslsocketstartclientencryption)() ，[waitForConnected](../../A/QAbstractSocket/QAbstractSocket.md#virtual-bool-qabstractsocketwaitforconnectedint-msecs--30000)() 和 [waitForEncrypted](#bool-qsslsocketwaitforencryptedint-msecs--30000)() 函数介绍中找到相关介绍。

### void **QSslSocket**::**connectToHostEncrypted**(const [QString](../../S/QString/QString.md) &*hostName*, [quint16](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#quint16-typedef) *port*, const [QString](../../S/QString/QString.md) &*sslPeerName*, [QIODevice::OpenMode]() *mode* = ReadWrite, [QAbstractSocket::NetworkLayerProtocol](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketnetworklayerprotocol) *protocol* = AnyIPProtocol)

重载函数。



### [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::**encryptedBytesAvailable**() const



### [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::**encryptedBytesToWrite**() const



### bool **QSslSocket**::**flush**()



### void **QSslSocket**::**ignoreSslErrors(const** [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> &*errors*)



### bool **QSslSocket**::**isEncrypted**() const



### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) **QSslSocket**::**localCertificate**() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::**localCertificateChain**() const



### [QSslSocket::SslMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#SslMode-enum) **QSslSocket**::**mode**() const



### [QVector](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvector.html)\<[QOcspResponse](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qocspresponse.html)\> **QSslSocket**::**ocspResponses**() const



### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) **QSslSocket**::**peerCertificate**() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::**peerCertificateChain**() const



### int **QSslSocket**::**peerVerifyDepth**() const



### [QSslSocket::PeerVerifyMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#PeerVerifyMode-enum) **QSslSocket**::**peerVerifyMode**() const



### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::**peerVerifyName**() const



### [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) **QSslSocket**::**privateKey**() const



### [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) **QSslSocket**::**protocol**() const



### *[override virtual protected]* [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::**readData**(char **data*, [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *maxlen*)



### *[override virtual]* void **QSslSocket**::**resume**()



### [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) **QSslSocket**::**sessionCipher**() const



### [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) **QSslSocket**::**sessionProtocol**() const



### void **QSslSocket**::**setLocalCertificate**(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)



### void **QSslSocket**::**setLocalCertificate**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*path*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)



### void **QSslSocket**::**setLocalCertificateChain**(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> &*localChain*)



### void **QSslSocket**::**setPeerVerifyDepth**(int *depth*)



### void **QSslSocket**::**setPeerVerifyMode**([QSslSocket::PeerVerifyMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#PeerVerifyMode-enum) *mode*)



### void **QSslSocket**::**setPeerVerifyName**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*hostName*)



### void **QSslSocket**::**setPrivateKey**(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) &*key*)



### void **QSslSocket**::**setPrivateKey**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*fileName*, [QSsl::KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum) *algorithm* = QSsl::Rsa, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem, const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)&*passPhrase* = QByteArray())



### void **QSslSocket**::**setProtocol**([QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) *protocol*)



### *[override virtual]* void **QSslSocket**::**setReadBufferSize**([qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *size*)



### *[override virtual]* void **QSslSocket**::**setSocketOption**([QAbstractSocket::SocketOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) *option*, const [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) &*value*)



### void **QSslSocket**::**setSslConfiguration**(const [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) &*configuration*)



### [override virtual] [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) **QSslSocket**::**socketOption**([QAbstractSocket::SocketOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) *option*)



### [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) **QSslSocket**::**sslConfiguration**() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> **QSslSocket**::**sslHandshakeErrors**() const



### *[static]* long **QSslSocket**::**sslLibraryBuildVersionNumber**()



### *[static]* [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::**sslLibraryBuildVersionString**()



### *[static]* long **QSslSocket**::**sslLibraryVersionNumber**()



### *[static]* [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::**sslLibraryVersionString**()



### *[static]* bool **QSslSocket**::**supportsSsl**()



### *[override virtual]* bool **QSslSocket**::**waitForBytesWritten**(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::**waitForConnected**(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::**waitForDisconnected**(int *msecs* = 30000)



### bool **QSslSocket**::**waitForEncrypted**(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::**waitForReadyRead**(int *msecs* = 30000)



### *[override virtual protected]* [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) QSslSocket::**writeData**(const char **data*, [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *len*)

