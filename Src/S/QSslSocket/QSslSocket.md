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

您可以在 [QSslSocket_Obsolete](../QSslSocket_Obsolete/QSslSocket_Obsolete.md) 界面找到废弃的成员函数介绍。

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

QSslSocket 能够建立一个安全的、加密的 TCP 连接，您可以使用该连接来传输加密数据。在服务器端和客户端都可以使用它，并且他支持现代的 SSL 协议，包括 SSL 3 和 TLS 1.2。默认情况下，QSslSocket 仅仅使用被认为是安全的（ [QSsl::SecureProtocols](../QSsl/QSsl.md#enum-qsslsslprotocol) ） SSL 协议，但是只要在握手开始之前，您可以调用 [setProtocol](#void-qsslsocketsetprotocolqsslsslprotocol-protocol)() 函数来更改 SSL 协议。

SSL encryption operates on top of the existing TCP stream after the socket enters the [ConnectedState](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qabstractsocket.html#SocketState-enum). There are two simple ways to establish a secure connection using QSslSocket: With an immediate SSL handshake, or with a delayed SSL handshake occurring after the connection has been established in unencrypted mode.

The most common way to use QSslSocket is to construct an object and start a secure connection by calling [connectToHostEncrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#connectToHostEncrypted)(). This method starts an immediate SSL handshake once the connection has been established.

```
 QSslSocket *socket = new QSslSocket(this);
 connect(socket, SIGNAL(encrypted()), this, SLOT(ready()));

 socket->connectToHostEncrypted("imap.example.com", 993);
```

As with a plain [QTcpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpsocket.html), QSslSocket enters the [HostLookupState](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qabstractsocket.html#SocketState-enum), [ConnectingState](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qabstractsocket.html#SocketState-enum), and finally the [ConnectedState](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qabstractsocket.html#SocketState-enum), if the connection is successful. The handshake then starts automatically, and if it succeeds, the [encrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encrypted)() signal is emitted to indicate the socket has entered the encrypted state and is ready for use.

Note that data can be written to the socket immediately after the return from [connectToHostEncrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#connectToHostEncrypted)() (i.e., before the [encrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encrypted)() signal is emitted). The data is queued in QSslSocket until after the [encrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encrypted)() signal is emitted.

An example of using the delayed SSL handshake to secure an existing connection is the case where an SSL server secures an incoming connection. Suppose you create an SSL server class as a subclass of [QTcpServer](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html). You would override [QTcpServer::incomingConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpserver.html#incomingConnection)() with something like the example below, which first constructs an instance of QSslSocket and then calls [setSocketDescriptor](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setSocketDescriptor)() to set the new socket's descriptor to the existing one passed in. It then initiates the SSL handshake by calling [startServerEncryption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#startServerEncryption)().

```
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

If an error occurs, QSslSocket emits the sslErrors() signal. In this case, if no action is taken to ignore the error(s), the connection is dropped. To continue, despite the occurrence of an error, you can call [ignoreSslErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#ignoreSslErrors)(), either from within this slot after the error occurs, or any time after construction of the QSslSocket and before the connection is attempted. This will allow QSslSocket to ignore the errors it encounters when establishing the identity of the peer. Ignoring errors during an SSL handshake should be used with caution, since a fundamental characteristic of secure connections is that they should be established with a successful handshake.

Once encrypted, you use QSslSocket as a regular [QTcpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpsocket.html). When [readyRead](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#readyRead)() is emitted, you can call [read](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#read)(), [canReadLine](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#canReadLine)() and [readLine](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#readLine)(), or [getChar](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#getChar)() to read decrypted data from QSslSocket's internal buffer, and you can call [write](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#write)() or [putChar](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#putChar)() to write data back to the peer. QSslSocket will automatically encrypt the written data for you, and emit [encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)() once the data has been written to the peer.

As a convenience, QSslSocket supports [QTcpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpsocket.html)'s blocking functions [waitForConnected](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForConnected)(), [waitForReadyRead](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForReadyRead)(), [waitForBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForBytesWritten)(), and [waitForDisconnected](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForDisconnected)(). It also provides [waitForEncrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForEncrypted)(), which will block the calling thread until an encrypted connection has been established.

```
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

QSslSocket provides an extensive, easy-to-use API for handling cryptographic ciphers, private keys, and local, peer, and Certification Authority (CA) certificates. It also provides an API for handling errors that occur during the handshake phase.

The following features can also be customized:

- The socket's cryptographic cipher suite can be customized before the handshake phase with [QSslConfiguration::setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() and QSslConfiguration::setDefaultCiphers().
- The socket's local certificate and private key can be customized before the handshake phase with [setLocalCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setLocalCertificate)() and [setPrivateKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPrivateKey)().
- The CA certificate database can be extended and customized with [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)(), [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)().

To extend the list of *default* CA certificates used by the SSL sockets during the SSL handshake you must update the default configuration, as in the snippet below:

```
 QList<QSslCertificate> certificates = getCertificates();
 QSslConfiguration configuration = QSslConfiguration::defaultConfiguration();
 configuration.addCaCertificates(certificates);
 QSslConfiguration::setDefaultConfiguration(configuration);
```

**Note:** If available, root certificates on Unix (excluding macOS) will be loaded on demand from the standard certificate directories. If you do not want to load root certificates on demand, you need to call either [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)().setCaCertificates() before the first SSL handshake is made in your application (for example, via passing QSslSocket::systemCaCertificates() to it), or call [QSslConfiguration::defaultConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#defaultConfiguration)()::setCaCertificates() on your QSslSocket instance prior to the SSL handshake.

For more information about ciphers and certificates, refer to [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) and [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html).

This product includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit (http://www.openssl.org/).

**Note:** Be aware of the difference between the [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() signal and the [encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)() signal. For a [QTcpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qtcpsocket.html), [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() will get emitted as soon as data has been written to the TCP socket. For a QSslSocket, [bytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html#bytesWritten)() will get emitted when the data is being encrypted and [encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)() will get emitted as soon as data has been written to the TCP socket.

**See also** [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html), [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html), and [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html).



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

