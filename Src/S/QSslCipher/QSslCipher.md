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
|                   | **[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher-3)**(const QSslCipher &*other*) |
|                   | **[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher-2)**(const QString &*name*, QSsl::SslProtocol *protocol*) |
|                   | **[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher-1)**(const QString &*name*) |
|                   | **[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher)**() |
| QSslCipher &      | **[operator=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#operator-eq-1)**(const QSslCipher &*other*) |
|                   | **[~QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#dtor.QSslCipher)**() |
| QString           | **[authenticationMethod](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#authenticationMethod)**() const |
| QString           | **[encryptionMethod](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#encryptionMethod)**() const |
| bool              | **[isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#isNull)**() const |
| QString           | **[keyExchangeMethod](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#keyExchangeMethod)**() const |
| QString           | **[name](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#name)**() const |
| QSsl::SslProtocol | **[protocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#protocol)**() const |
| QString           | **[protocolString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#protocolString)**() const |
| int               | **[supportedBits](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#supportedBits)**() const |
| void              | **[swap](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#swap)**(QSslCipher &*other*) |
| int               | **[usedBits](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#usedBits)**() const |
| bool              | **[operator!=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#operator-not-eq)**(const QSslCipher &*other*) const |
| bool              | **[operator==](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#operator-eq-eq)**(const QSslCipher &*other*) const |



## 详细描述





## 成员函数文档

### QSslCipher::QSslCipher(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

Constructs an identical copy of the *other* cipher.

### QSslCipher::QSslCipher(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*name*, [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) *protocol*)

Constructs a QSslCipher object for the cipher determined by *name* and *protocol*. The constructor accepts only supported ciphers (i.e., the *name* and *protocol* must identify a cipher in the list of ciphers returned by QSslSocket::supportedCiphers()).

You can call [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#isNull)() after construction to check if *name* and *protocol* correctly identified a supported cipher.

### QSslCipher::QSslCipher(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*name*)

Constructs a QSslCipher object for the cipher determined by *name*. The constructor accepts only supported ciphers (i.e., the *name* must identify a cipher in the list of ciphers returned by QSslSocket::supportedCiphers()).

You can call [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#isNull)() after construction to check if *name* correctly identified a supported cipher.

This function was introduced in Qt 5.3.

### QSslCipher::QSslCipher()

Constructs an empty QSslCipher object.

### [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &QSslCipher::operator=(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

Copies the contents of *other* into this cipher, making the two ciphers identical.

### QSslCipher::~QSslCipher()

Destroys the [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) object.

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::authenticationMethod() const

Returns the cipher's authentication method as a [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html).

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::encryptionMethod() const

Returns the cipher's encryption method as a [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html).

### bool QSslCipher::isNull() const

Returns `true` if this is a null cipher; otherwise returns `false`.

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::keyExchangeMethod() const

Returns the cipher's key exchange method as a [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html).

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::name() const

Returns the name of the cipher, or an empty [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) if this is a null cipher.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#isNull)().

### [QSsl::SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) QSslCipher::protocol() const

Returns the cipher's protocol type, or [QSsl::UnknownProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum) if [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html) is unable to determine the protocol ([protocolString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#protocolString)() may contain more information).

**See also** [protocolString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#protocolString)().

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCipher::protocolString() const

Returns the cipher's protocol as a [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html).

**See also** [protocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#protocol)().

### int QSslCipher::supportedBits() const

Returns the number of bits supported by the cipher.

**See also** [usedBits](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#usedBits)().

### void QSslCipher::swap([QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*)

Swaps this cipher instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

### int QSslCipher::usedBits() const

Returns the number of bits used by the cipher.

**See also** [supportedBits](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#supportedBits)().

### bool QSslCipher::operator!=(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*) const

Returns `true` if this cipher is not the same as *other*; otherwise, false is returned.

### bool QSslCipher::operator==(const [QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html#QSslCipher) &*other*) const

Returns `true` if this cipher is the same as *other*; otherwise, false is returned.