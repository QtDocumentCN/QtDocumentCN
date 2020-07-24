[TOC]



# QSslKey Class

QSslKey 类为私钥、公钥提供了相应的接口。

| 属性   | 方法                 |
| ------ | -------------------- |
| 头文件 | `#include <QSslKey>` |
| qmake  | QT += network        |
| 引入   | Qt 4.3               |

该类最初在 Qt 4.3 版本引入。

**注意：** 该类所有的函数都是可重入的。



## 公共成员函数

| 类型               | 函数名                                                       |
| ------------------ | ------------------------------------------------------------ |
|                    | **[QSslKey]()**(const QSslKey &*other*)                      |
|                    | **[QSslKey]()**(Qt::HANDLE *handle*, QSsl::KeyType *type* = QSsl::PrivateKey) |
|                    | **[QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey-2)**(QIODevice **device*, QSsl::KeyAlgorithm *algorithm*, QSsl::EncodingFormat *encoding* = QSsl::Pem, QSsl::KeyType *type* = QSsl::PrivateKey, const QByteArray &*passPhrase* = QByteArray()) |
|                    | **[QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey-1)**(const QByteArray &*encoded*, QSsl::KeyAlgorithm *algorithm*, QSsl::EncodingFormat *encoding* = QSsl::Pem, QSsl::KeyType *type* = QSsl::PrivateKey, const QByteArray &*passPhrase* = QByteArray()) |
|                    | **[QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey)**() |
| QSslKey &          | **[operator=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#operator-eq-1)**(const QSslKey &*other*) |
|                    | **[~QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#dtor.QSslKey)**() |
| QSsl::KeyAlgorithm | **[algorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#algorithm)**() const |
| void               | **[clear](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#clear)**() |
| Qt::HANDLE         | **[handle](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#handle)**() const |
| bool               | **[isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#isNull)**() const |
| int                | **[length](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#length)**() const |
| void               | **[swap](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#swap)**(QSslKey &*other*) |
| QByteArray         | **[toDer](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#toDer)**(const QByteArray &*passPhrase* = QByteArray()) const |
| QByteArray         | **[toPem](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#toPem)**(const QByteArray &*passPhrase* = QByteArray()) const |
| QSsl::KeyType      | **[type](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#type)**() const |
| bool               | **[operator!=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#operator-not-eq)**(const QSslKey &*other*) const |
| bool               | **[operator==](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#operator-eq-eq)**(const QSslKey &*other*) const |



## 详细描述



## 成员函数文档

### QSslKey::QSslKey(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*)

Constructs an identical copy of *other*.

### QSslKey::QSslKey([Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) *handle*, [QSsl::KeyType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyType-enum) *type* = QSsl::PrivateKey)

Constructs a QSslKey from a valid native key *handle*. *type* specifies whether the key is public or private.

QSslKey will take ownership for this key and you must not free the key using the native library.

This function was introduced in Qt 5.0.

### QSslKey::QSslKey([QIODevice](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html) **device*, [QSsl::KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum) *algorithm*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *encoding* = QSsl::Pem, [QSsl::KeyType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyType-enum) *type* = QSsl::PrivateKey, const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)&*passPhrase* = QByteArray())

Constructs a QSslKey by reading and decoding data from a *device* using a specified *algorithm* and *encoding* format. *type* specifies whether the key is public or private.

If the key is encrypted then *passPhrase* is used to decrypt it.

After construction, use [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#isNull)() to check if *device* provided a valid key.

### QSslKey::QSslKey(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*encoded*, [QSsl::KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum) *algorithm*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *encoding* = QSsl::Pem, [QSsl::KeyType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyType-enum) *type* = QSsl::PrivateKey, const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*passPhrase* = QByteArray())

Constructs a QSslKey by decoding the string in the byte array *encoded* using a specified *algorithm* and *encoding* format. *type* specifies whether the key is public or private.

If the key is encrypted then *passPhrase* is used to decrypt it.

After construction, use [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#isNull)() to check if *encoded* contained a valid key.

### QSslKey::QSslKey()

Constructs a null key.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#isNull)().

### [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &QSslKey::operator=(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*)

Copies the contents of *other* into this key, making the two keys identical.

Returns a reference to this [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html).

### QSslKey::~QSslKey()

Destroys the [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) object.

### [QSsl::KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum) QSslKey::algorithm() const

Returns the key algorithm.

### void QSslKey::clear()

Clears the contents of this key, making it a null key.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#isNull)().

### [Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) QSslKey::handle() const

Returns a pointer to the native key handle, if there is one, else `nullptr`.

You can use this handle together with the native API to access extended information about the key.

**Warning:** Use of this function has a high probability of being non-portable, and its return value may vary across platforms, and between minor Qt releases.

### bool QSslKey::isNull() const

Returns `true` if this is a null key; otherwise false.

**See also** [clear](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#clear)().

### int QSslKey::length() const

Returns the length of the key in bits, or -1 if the key is null.

### void QSslKey::swap([QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*)

Swaps this ssl key with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslKey::toDer(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*passPhrase* = QByteArray()) const

Returns the key in DER encoding.

The *passPhrase* argument should be omitted as DER cannot be encrypted. It will be removed in a future version of Qt.

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslKey::toPem(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*passPhrase* = QByteArray()) const

Returns the key in PEM encoding. The result is encrypted with *passPhrase* if the key is a private key and *passPhrase* is non-empty.

### [QSsl::KeyType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyType-enum) QSslKey::type() const

Returns the type of the key (i.e., PublicKey or PrivateKey).

### bool QSslKey::operator!=(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*) const

Returns `true` if this key is not equal to key *other*; otherwise returns `false`.

### bool QSslKey::operator==(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*) const

Returns `true` if this key is equal to *other*; otherwise returns `false`.