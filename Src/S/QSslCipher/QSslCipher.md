[TOC]



# QSslCipher Class

QSslCipher 类提供了 SSL 密钥的支持。

| 属性   | 方法                    |
| ------ | ----------------------- |
| 头文件 | `#include <QSslCipher>` |
| qmake  | QT += network           |
| 引入   | Qt 4.3                  |

该类最早在 Qt 4.3版本引入。

**注意：** 所有的函数都是可重入的。



## 公共成员函数

| 属性              | 方法                                                         |
| ----------------- | ------------------------------------------------------------ |
|                   | **[QSslCipher](#qsslcipherqsslcipherconst-qsslcipher-other)**(const QSslCipher &*other*) |
|                   | **[QSslCipher](#qsslcipherqsslcipherconst-qstring-name-qsslsslprotocol-protocol)**(const QString &*name*, QSsl::SslProtocol *protocol*) |
|                   | **[QSslCipher](#qsslcipherqsslcipherconst-qstring-name)**(const QString &*name*) |
|                   | **[QSslCipher](#qsslcipherqsslcipher)**()                    |
| QSslCipher &      | **[operator=](#qsslcipher-qsslcipheroperatorconst-qsslcipher-other)**(const QSslCipher &*other*) |
|                   | **[~QSslCipher](#qsslcipherqsslcipher-1)**()                 |
| QString           | **[authenticationMethod](#qstring-qsslcipherauthenticationmethod-const)**() const |
| QString           | **[encryptionMethod](#qstring-qsslcipherencryptionmethod-const)**() const |
| bool              | **[isNull](#bool-qsslcipherisnull-const)**() const           |
| QString           | **[keyExchangeMethod](#qstring-qsslcipherkeyexchangemethod-const)**() const |
| QString           | **[name](#qstring-qsslciphername-const)**() const            |
| QSsl::SslProtocol | **[protocol](#qsslsslprotocol-qsslcipherprotocol-const)**() const |
| QString           | **[protocolString](#qstring-qsslcipherprotocolstring-const)**() const |
| int               | **[supportedBits](#int-qsslciphersupportedbits-const)**() const |
| void              | **[swap](#void-qsslcipherswapqsslcipher-other)**(QSslCipher &*other*) |
| int               | **[usedBits](#int-qsslcipherusedbits-const)**() const        |
| bool              | **[operator!=](#bool-qsslcipheroperatorconst-qsslcipher-other-const)**(const QSslCipher &*other*) const |
| bool              | **[operator==](#bool-qsslcipheroperatorconst-qsslcipher-other-const-1)**(const QSslCipher &*other*) const |



## 详细描述

QSslCipher 储存着一个密钥的信息。该类型的对象通常被 [QSslSocket](../QSslSocket/QSslSocket.md) 用来指定某套接字可以使用哪种密钥或者展现某套接字所使用的密钥。

另外您也可以在 [QSslSocket](../QSslSocket/QSslSocket.md) 和 [QSslKey](../QSslKey/QSslKey.md) 类文档中找到相关信息。

## 成员函数文档

### QSslCipher::**QSslCipher**(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

拷贝构造函数。由 *other* 拷贝出一个相同的 QSslCipher 对象。

---

### QSslCipher::**QSslCipher**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*name*, [QSsl::SslProtocol](../QSsl/QSsl.md#enum-qsslsslprotocol) *protocol*)

构造函数。通过鉴定 *name* 和 *protocol* 来构造一个 QSslCipher 对象来储存密钥信息。该构造函数仅接受受支持的密钥（即您指定的 *name* 和 *protocol* 所鉴定出的密钥必须位于 QSslSocket::supportedCiphers() 函数返回的列表中）。

构造后，您可以调用 [isNull](#bool-qsslcipherisnull-const)() 函数检查 *name* 和 *protocol* 是否能正确地鉴定出一个支持的密钥。

---

### QSslCipher::**QSslCipher**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*name*)

构造函数。通过判断 *name* 参数构造一个 QSslCipher 对象储存密钥信息。该构造函数仅接受受支持的密钥（即您指定的 *name* 所鉴定出的密钥必须位于 QSslSocket::supportedCiphers() 函数返回的列表中）。

构造后，可以调用 [isNull](#bool-qsslcipherisnull-const)() 函数检查 *name* 是否正确标识了受支持的密码。

该函数最初在 Qt 5.3 版本中引入。

---

### QSslCipher::**QSslCipher**()

构造函数。构造一个空的 QSslCipher 对象。

---

### [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &QSslCipher::**operator=**(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

将 *other* 的内容拷贝到等式左值，是两个密钥相同。

---

### QSslCipher::~**QSslCipher**()

析构函数。销毁 QSslCipher 对象。

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::**authenticationMethod**() const

以 QString 格式返回密钥的身份验证方式。

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::**encryptionMethod**() const

以 QString 格式返回密钥的加密方式。

---

### bool QSslCipher::**isNull**() const

如果该密钥未空，函数返回 *true* ，否则返回 *false* 。

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::**keyExchangeMethod**() const

以 QString 格式返回该密钥的密钥交换方法。

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::**name**() const

返回该密钥的名称。如果密钥未空，函数将返回一个空的 QString 对象。

另外您也可以在 [isNull](#bool-qsslcipherisnull-const)() 函数介绍中找到相关信息。

---

### [QSsl::SslProtocol](../QSsl/QSsl.md#enum-qsslsslprotocol) QSslCipher::**protocol**() const

返回该协议使用的密钥。如果不能判断 QSslCipher 使用的协议，函数将返回 [QSsl::UnknownProtocol](../QSsl/QSsl.md#enum-qsslsslprotocol) （您可以使用 [protocolString](#qstring-qsslcipherprotocolstring-const)() 函数来获取更多的信息）。

另外您也可以在 [protocolString](#qstring-qsslcipherprotocolstring-const)() 函数介绍中找到相关信息。

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::**protocolString**() const

以 QString 的形式返回该密钥使用的协议。

另外您也可以在 [protocol](#qsslsslprotocol-qsslcipherprotocol-const)() 函数介绍中找到相关信息。

---

### int QSslCipher::**supportedBits**() const

返回该密钥支持的字节数。

另外您也可以在 [usedBits](#int-qsslcipherusedbits-const)() 函数介绍中找到相关信息。

---

### void QSslCipher::**swap**([QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

与 *other* 快速交换密钥信息。该函数操作速度飞快并保证操作成功。

该函数最初在 Qt 5.0 版本引入。

---

### int QSslCipher::**usedBits**() const

返回密钥所用的字节数。

另外您也可以在 [supportedBits](#int-qsslciphersupportedbits-const)() 函数介绍中找到相关信息。

---

### bool QSslCipher::**operator!=**(const QSslCipher &*other*) const

如果当前密钥与 *other* 不同则返回 *true* ，否则返回 *false* 。

---

### bool QSslCipher::**operator==**(const QSslCipher &*other*) const

如果当前密钥与 *other* 相同则返回 *true* ，否则返回 *false* 。