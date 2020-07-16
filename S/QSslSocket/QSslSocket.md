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
| QSsl::SslProtocol          | **[protocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#protocol)**() const |
| QSslCipher                 | **[sessionCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sessionCipher)**() const |
| QSsl::SslProtocol          | **[sessionProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sessionProtocol)**() const |
| void                       | **[setLocalCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setLocalCertificate)**(const QSslCertificate &*certificate*) |
| void                       | **[setLocalCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setLocalCertificate-1)**(const QString &*path*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| void                       | **[setLocalCertificateChain](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setLocalCertificateChain)**(const QList\<QSslCertificate\> &*localChain*) |
| void                       | **[setPeerVerifyDepth](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPeerVerifyDepth)**(int *depth*) |
| void                       | **[setPeerVerifyMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPeerVerifyMode)**(QSslSocket::PeerVerifyMode *mode*) |
| void                       | **[setPeerVerifyName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPeerVerifyName)**(const QString &*hostName*) |
| void                       | **[setPrivateKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPrivateKey)**(const QSslKey &*key*) |
| void                       | **[setPrivateKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setPrivateKey-1)**(const QString &*fileName*, QSsl::KeyAlgorithm *algorithm* = QSsl::Rsa, QSsl::EncodingFormat *format* = QSsl::Pem, const QByteArray &*passPhrase* = QByteArray()) |
| void                       | **[setProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setProtocol)**(QSsl::SslProtocol *protocol*) |
| void                       | **[setSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setSslConfiguration)**(const QSslConfiguration &*configuration*) |
| QSslConfiguration          | **[sslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslConfiguration)**() const |
| QList\<QSslError\>         | **[sslHandshakeErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslHandshakeErrors)**() const |
| bool                       | **[waitForEncrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForEncrypted)**(int *msecs* = 30000) |



## 重写公共成员函数

| 类型             | 函数名                                                       |
| ---------------- | ------------------------------------------------------------ |
| virtual bool     | **[atEnd](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#atEnd)**() const override |
| virtual qint64   | **[bytesAvailable](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#bytesAvailable)**() const override |
| virtual qint64   | **[bytesToWrite](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#bytesToWrite)**() const override |
| virtual bool     | **[canReadLine](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#canReadLine)**() const override |
| virtual void     | **[close](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#close)**() override |
| virtual void     | **[resume](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#resume)**() override |
| virtual void     | **[setReadBufferSize](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setReadBufferSize)**(qint64 *size*) override |
| virtual bool     | **[setSocketDescriptor](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setSocketDescriptor)**(qintptr *socketDescriptor*, QAbstractSocket::SocketState *state* = ConnectedState, QIODevice::OpenMode *openMode* = ReadWrite) override |
| virtual void     | **[setSocketOption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#setSocketOption)**(QAbstractSocket::SocketOption *option*, const QVariant &*value*) override |
| virtual QVariant | **[socketOption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#socketOption)**(QAbstractSocket::SocketOption *option*) override |
| virtual bool     | **[waitForBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForBytesWritten)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForConnected](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForConnected)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForDisconnected](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForDisconnected)**(int *msecs* = 30000) override |
| virtual bool     | **[waitForReadyRead](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#waitForReadyRead)**(int *msecs* = 30000) override |



## 公共槽函数

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[ignoreSslErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#ignoreSslErrors)**() |
| void | **[startClientEncryption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#startClientEncryption)**() |
| void | **[startServerEncryption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#startServerEncryption)**() |



## 信号

| 类型 | 函数名                                                       |
| ---- | ------------------------------------------------------------ |
| void | **[encrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encrypted)**() |
| void | **[encryptedBytesWritten](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#encryptedBytesWritten)**(qint64 *written*) |
| void | **[modeChanged](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#modeChanged)**(QSslSocket::SslMode *mode*) |
| void | **[newSessionTicketReceived](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#newSessionTicketReceived)**() |
| void | **[peerVerifyError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#peerVerifyError)**(const QSslError &*error*) |
| void | **[preSharedKeyAuthenticationRequired](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#preSharedKeyAuthenticationRequired)**(QSslPreSharedKeyAuthenticator **authenticator*) |
| void | **[sslErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslErrors-1)**(const QList\<QSslError\> &*errors*) |



### 静态成员函数

| 类型    | 函数名                                                       |
| ------- | ------------------------------------------------------------ |
| long    | **[sslLibraryBuildVersionNumber](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslLibraryBuildVersionNumber)**() |
| QString | **[sslLibraryBuildVersionString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslLibraryBuildVersionString)**() |
| long    | **[sslLibraryVersionNumber](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslLibraryVersionNumber)**() |
| QString | **[sslLibraryVersionString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslLibraryVersionString)**() |
| bool    | **[supportsSsl](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#supportsSsl)**() |



## 重写保护成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual qint64 | **[readData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#readData)**(char **data*, qint64 *maxlen*) override |
| virtual qint64 | **[writeData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#writeData)**(const char **data*, qint64 *len*) override |



## 详细介绍





## 成员类型文档

### enum **QSslSocket**::PeerVerifyMode



### enum **QSslSocket**::SslMode





## 成员函数文档

### **QSslSocket**::QSslSocket**([QObject](../../O/QObject/QObject.md) **parent* = nullptr)



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

