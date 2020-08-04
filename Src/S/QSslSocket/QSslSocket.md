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
| bool                       | **[isEncrypted](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/S/QSslSocket/QSslSocket.md#bool-qsslsocketisencrypted-const)**() const |
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

最常见的 QSslSocket 使用方法是构造一个对象后使用 connectToHostEncrypted() 函数开启一个安全连接，这种方法会在连接建立后开启一个即时的 SSL 握手。

```cpp
 QSslSocket *socket = new QSslSocket(this);
 connect(socket, SIGNAL(encrypted()), this, SLOT(ready()));

 socket->connectToHostEncrypted("imap.example.com", 993);
```

与普通的 [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) 相同，若成功建立连接， QSslSocket 会依次进入 [HostLookupState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) ，[ConnectingState](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate) 和 [ConnectedState]((../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketstate)) 状态。连接成功后，握手会自动开始，若握手连接成功，QSsslSocket 将会发送 [encrypted](#signal-void-qsslsocketencrypted)() 信号，表明该套接字已经进入加密状态并准备好使用。

请注意，在 connectToHostEncrypted() 函数执行完成返回后（即 [encrypted](#signal-void-qsslsocketencrypted)() 信号发出之前）数据就可以立即写入套接字。此时写入到套接字的数据将会被加入等待队列，直到 [encrypted](#signal-void-qsslsocketencrypted)() 信号被发出。

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

- The socket's cryptographic cipher suite can be customized before the handshake phase with [QSslConfiguration::setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() and QSslConfiguration::setDefaultCiphers().
- The socket's local certificate and private key can be customized before the handshake phase with [setLocalCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setLocalCertificate)() and [setPrivateKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPrivateKey)().
- The CA certificate database can be extended and customized with [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)(), [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)().

To extend the list of *default* CA certificates used by the SSL sockets during the SSL handshake you must update the default configuration, as in the snippet below:

```cpp
 QList<QSslCertificate> certificates = getCertificates();
 QSslConfiguration configuration = QSslConfiguration::defaultConfiguration();
 configuration.addCaCertificates(certificates);
 QSslConfiguration::setDefaultConfiguration(configuration);
```

**Note:** If available, root certificates on Unix (excluding macOS) will be loaded on demand from the standard certificate directories. If you do not want to load root certificates on demand, you need to call either [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)().setCaCertificates() before the first SSL handshake is made in your application (for example, via passing QSslSocket::systemCaCertificates() to it), or call [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)()::setCaCertificates() on your QSslSocket instance prior to the SSL handshake.

For more information about ciphers and certificates, refer to [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) and [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html).

This product includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit (http://www.openssl.org/).

**Note:** Be aware of the difference between the [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() signal and the [encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)() signal. For a [QTcpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpsocket.html), [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() will get emitted as soon as data has been written to the TCP socket. For a QSslSocket, [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() will get emitted when the data is being encrypted and [encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)() will get emitted as soon as data has been written to the TCP socket.

**注意**：

另外您也可以在 [QSslCertificate](../QSslCertificate/QSslCertificate.md)，[QSslCipher](../QSslCipher/QSslCipher.md) 和 [QSslError](../QSslError/QSslError.md) 类文档中找到相关信息。

## 成员类型文档

### enum QSslSocket::**PeerVerifyMode**



---

### enum QSslSocket::**SslMode**





## 成员函数文档

### QSslSocket::**QSslSocket****([QObject](../../O/QObject/QObject.md) **parent* = nullptr)



### *[signal]* void **QSslSocket**::encrypted()



### *[signal]* void **QSslSocket**::encryptedBytesWritten(qint64 *written*)



### *[slot]* void **QSslSocket**::ignoreSslErrors()



### *[signal]* void **QSslSocket**::modeChanged([QSslSocket::SslMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#SslMode-enum) *mode*)



### *[signal]* void **QSslSocket**::newSessionTicketReceived()



### *[signal]* void **QSslSocket**::peerVerifyError(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html) &*error*)



### *[signal]* void **QSslSocket**::preSharedKeyAuthenticationRequired([QSslPreSharedKeyAuthenticator](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslpresharedkeyauthenticator.html) **authenticator*)



### *[signal]* void **QSslSocket**::sslErrors(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<QSslError\> &*errors*)



### *[slot]* void **QSslSocket**::startClientEncryption()



### *[slot]* void **QSslSocket**::startServerEncryption()



### *[virtual]* **QSslSocket**::~QSslSocket()



### void **QSslSocket**::abort()



### *[override virtual]* bool **QSslSocket**::atEnd() const



### *[override virtual]* qint64 **QSslSocket**::bytesAvailable() const



### *[override virtual]* qint64 **QSslSocket**::bytesToWrite() const



### *[override virtual]* bool **QSslSocket**::canReadLine() const



### *[override virtual]* void **QSslSocket**::close()



### void **QSslSocket**::connectToHostEncrypted(const QString &*hostName*, quint16 *port*, QIODevice::OpenMode *mode* = ReadWrite, [QAbstractSocket::NetworkLayerProtocol](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketnetworklayerprotocol) *protocol* = AnyIPProtocol)



### void **QSslSocket**::connectToHostEncrypted(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*hostName*, [quint16](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#quint16-typedef) *port*, const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*sslPeerName*, [QIODevice::OpenMode](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#OpenModeFlag-enum) *mode* = ReadWrite, [QAbstractSocket::NetworkLayerProtocol](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketnetworklayerprotocol) *protocol* = AnyIPProtocol)



### [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::encryptedBytesAvailable() const



### [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::encryptedBytesToWrite() const



### bool **QSslSocket**::flush()



### void **QSslSocket**::ignoreSslErrors(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> &*errors*)



### bool **QSslSocket**::isEncrypted() const



### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) **QSslSocket**::localCertificate() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::localCertificateChain() const



### [QSslSocket::SslMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#SslMode-enum) **QSslSocket**::mode() const



### [QVector](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvector.html)\<[QOcspResponse](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qocspresponse.html)\> **QSslSocket**::ocspResponses() const



### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) **QSslSocket**::peerCertificate() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::peerCertificateChain() const



### int **QSslSocket**::peerVerifyDepth() const



### [QSslSocket::PeerVerifyMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#PeerVerifyMode-enum) **QSslSocket**::peerVerifyMode() const



### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::peerVerifyName() const



### [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) **QSslSocket**::privateKey() const



### [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) **QSslSocket**::protocol() const



### *[override virtual protected]* [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) **QSslSocket**::readData(char **data*, [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *maxlen*)



### *[override virtual]* void **QSslSocket**::resume()



### [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) **QSslSocket**::sessionCipher() const



### [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) **QSslSocket**::sessionProtocol() const



### void **QSslSocket**::setLocalCertificate(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)



### void **QSslSocket**::setLocalCertificate(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*path*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)



### void **QSslSocket**::setLocalCertificateChain(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> &*localChain*)



### void **QSslSocket**::setPeerVerifyDepth(int *depth*)



### void **QSslSocket**::setPeerVerifyMode([QSslSocket::PeerVerifyMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#PeerVerifyMode-enum) *mode*)



### void **QSslSocket**::setPeerVerifyName(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*hostName*)



### void **QSslSocket**::setPrivateKey(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) &*key*)



### void **QSslSocket**::setPrivateKey(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*fileName*, [QSsl::KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum) *algorithm* = QSsl::Rsa, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem, const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)&*passPhrase* = QByteArray())



### void **QSslSocket**::setProtocol([QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) *protocol*)



### *[override virtual]* void **QSslSocket**::setReadBufferSize([qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *size*)



### *[override virtual]* void **QSslSocket**::setSocketOption([QAbstractSocket::SocketOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) *option*, const [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) &*value*)



### void **QSslSocket**::setSslConfiguration(const [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) &*configuration*)



### [override virtual] [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) **QSslSocket**::socketOption([QAbstractSocket::SocketOption](../../A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketsocketoption) *option*)



### [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) **QSslSocket**::sslConfiguration() const



### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> **QSslSocket**::sslHandshakeErrors() const



### *[static]* long **QSslSocket**::sslLibraryBuildVersionNumber()



### *[static]* [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::sslLibraryBuildVersionString()



### *[static]* long **QSslSocket**::sslLibraryVersionNumber()



### *[static]* [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) **QSslSocket**::sslLibraryVersionString()



### *[static]* bool **QSslSocket**::supportsSsl()



### *[override virtual]* bool **QSslSocket**::waitForBytesWritten(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::waitForConnected(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::waitForDisconnected(int *msecs* = 30000)



### bool **QSslSocket**::waitForEncrypted(int *msecs* = 30000)



### *[override virtual]* bool **QSslSocket**::waitForReadyRead(int *msecs* = 30000)



### *[override virtual protected]* [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) QSslSocket::writeData(const char **data*, [qint64](qthelp://org.qt-project.qtnetwork.5150/qtcore/qtglobal.html#qint64-typedef) *len*)

