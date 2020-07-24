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
|                    | **[QSslKey](#qsslkeyqsslkeyconst-qsslkey-other)**(const QSslKey &*other*) |
|                    | **[QSslKey](#qsslkeyqsslkeyqthandle-handle-qsslkeytype-type--qsslprivatekey)**(Qt::HANDLE *handle*, QSsl::KeyType *type* = QSsl::PrivateKey) |
|                    | **[QSslKey](#qsslkeyqsslkeyqiodevice-device-qsslkeyalgorithm-algorithm-qsslencodingformat-encoding--qsslpem-qsslkeytype-type--qsslprivatekey-const-qbytearraypassphrase--qbytearray)**(QIODevice **device*, QSsl::KeyAlgorithm *algorithm*, QSsl::EncodingFormat *encoding* = QSsl::Pem, QSsl::KeyType *type* = QSsl::PrivateKey, const QByteArray &*passPhrase* = QByteArray()) |
|                    | **[QSslKey](#qsslkeyqsslkeyconst-qbytearray-encoded-qsslkeyalgorithm-algorithm-qsslencodingformat-encoding--qsslpem-qsslkeytype-type--qsslprivatekey-const-qbytearray-passphrase--qbytearray)**(const QByteArray &*encoded*, QSsl::KeyAlgorithm *algorithm*, QSsl::EncodingFormat *encoding* = QSsl::Pem, QSsl::KeyType *type* = QSsl::PrivateKey, const QByteArray &*passPhrase* = QByteArray()) |
|                    | **[QSslKey](#qsslkeyqsslkey)**()                             |
| QSslKey &          | **[operator=](#qsslkey-qsslkeyoperatorconst-qsslkey-other)**(const QSslKey &*other*) |
|                    | **[~QSslKey](#qsslkeyqsslkey-1)**()                          |
| QSsl::KeyAlgorithm | **[algorithm](#qsslkeyalgorithm-qsslkeyalgorithm-const)**() const |
| void               | **[clear](#void-qsslkeyclear)**()                            |
| Qt::HANDLE         | **[handle](#qthandle-qsslkeyhandle-const)**() const          |
| bool               | **[isNull](#bool-qsslkeyisnull-const)**() const              |
| int                | **[length](#int-qsslkeylength-const)**() const               |
| void               | **[swap](#void-qsslkeyswapqsslkey-other)**(QSslKey &*other*) |
| QByteArray         | **[toDer](#qbytearray-qsslkeytoderconst-qbytearray-passphrase--qbytearray-const)**(const QByteArray &*passPhrase* = QByteArray()) const |
| QByteArray         | **[toPem](#qbytearray-qsslkeytopemconst-qbytearray-passphrase--qbytearray-const)**(const QByteArray &*passPhrase* = QByteArray()) const |
| QSsl::KeyType      | **[type](#qsslkeytype-qsslkeytype-const)**() const           |
| bool               | **[operator!=](#bool-qsslkeyoperatorconst-qsslkey-other-const)**(const QSslKey &*other*) const |
| bool               | **[operator==](#bool-qsslkeyoperatorconst-qsslkey-other-const-1)**(const QSslKey &*other*) const |



## 详细描述

QSslKey 类为密钥管理提供了简单的 API 支持。

另外您也可以在 [QSslSocket](../QSslSocket/QSslSocket.md) ，[QSslCertificate](../QSslCertificate/QSslCertificate.md) 和 [QSslCipher](../QSslCipher/QSslCipher.md) 类文档中找到相关介绍。

## 成员函数文档

### QSslKey::**QSslKey**(const QSslKey &*other*)

拷贝构造函数。

由 *other* 拷贝一份新的 QSslKey 对象。

---

### QSslKey::**QSslKey**([Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) *handle*, [QSsl::KeyType](../QSsl/QSsl.md#enum-qsslkeytype) *type* = QSsl::PrivateKey)

从一个可以用的本地句柄 *handle* 构造一个 QSslKey 对象。*type* 参数用来指定该密钥是公钥还是私钥。

QSsl 将会接管该密钥，您不得使用本机库来释放该密钥。

该函数最初在 Qt 5.0版本引入。

---

### QSslKey::**QSslKey**([QIODevice](../../I/QIODevice/QIODevice.md) **device*, [QSsl::KeyAlgorithm](../QSsl/QSsl.md#enum-qsslkeyalgorithm) *algorithm*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *encoding* = QSsl::Pem, [QSsl::KeyType](../QSsl/QSsl.md#enum-qsslkeytype) *type* = QSsl::PrivateKey, const [QByteArray](../../B/QByteArray/QByteArray.md)&*passPhrase* = QByteArray())

使用 *algorithm* 指定的算法和 *encoding* 指定的格式从 *device* 指定的设备中读取并解码数据，构造 QSslKey 对象。*type* 参数指定了该密钥是公钥还是私钥。

如果该密钥被加密，则将使用 *passPhrase* 来解密。

构造后该对象后，您可以使用 [isNull](#bool-qsslkeyisnull-const)() 函数来检查 *device* 设备是否提供了一个有效的密钥。

---

### QSslKey::**QSslKey**(const [QByteArray](../../B/QByteArray/QByteArray.md) &*encoded*, [QSsl::KeyAlgorithm](../QSsl/QSsl.md#enum-qsslkeyalgorithm) *algorithm*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *encoding* = QSsl::Pem, [QSsl::KeyType](../QSsl/QSsl.md#enum-qsslkeytype) *type* = QSsl::PrivateKey, const [QByteArray](../../B/QByteArray/QByteArray.md) &*passPhrase* = QByteArray())

使用 *algorithm* 指定的算法和 *encoding* 指定的格式从字符数组 *encoded* 读取并解密字符串，构造 QSslKey 对象。 *type* 将指定该密钥是公钥还是私钥。

如果该密钥被加密，则将使用 *passPhrase* 解密。

构造后该对象后，您可以使用 [isNull](#bool-qsslkeyisnull-const)() 函数来检查 *encoded* 字符数组是否包含了一个有效的密钥。

---

### QSslKey::**QSslKey**()

构造一个空的密钥。

另外您可以在 [isNull](#bool-qsslkeyisnull-const)() 函数介绍中找到更多相关信息。

---

### QSslKey &QSslKey::**operator=**(const QSslKey &*other*)

将 *other* 中的内容拷贝到此密钥中，是等式左右值相等。

返回该对象的引用。

---

### QSslKey::**~QSslKey**()

析构函数。销毁该 QSslKey 对象。

---

### [QSsl::KeyAlgorithm](../QSsl/QSsl.md#enum-qsslkeyalgorithm) QSslKey::**algorithm**() const

返回该密钥加密算法。

---

### void QSslKey::**clear**()

清除该密钥的内容，将密钥变为空密钥。

另外您可以在 [isNull](#bool-qsslkeyisnull-const)() 函数介绍中找到更多相关信息。

---

### [Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) QSslKey::**handle**() const

若本地密钥句柄存在，则返回指向本地密钥句柄的指针，否则返回`nullptr`。

你可以将此句柄与本地 API 结合使用，获得关于该密钥更多的信息。

**警告：** 使用该函数有很大的可能并不能移植，并且该函数的返回值可能会在不同平台之间或者不同 Qt 发行版本之间变化。

---

### bool QSslKey::**isNull**() const

如果该密钥为空则返回`true` ，否则返回`false`。

另外您也可以在 [clear](#void-qsslkeyclear)() 函数介绍中找到相关介绍。

---

### int QSslKey::**length**() const

返回密钥的长度（以位为单位）；如果密钥为空，则返回-1。

---

### void QSslKey::**swap**([QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*)

与 *oher* 交换密钥信息。该函数执行速度很快并且保证操作一定成功。

该函数最初在 Qt 5.0 版本引入。

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslKey::**toDer**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*passPhrase* = QByteArray()) const

以 DER 编码格式返回该密钥。

您应该忽略 *passPhrase* 参数，因为 DER 不能被加密。未来的 Qt 版本中将移除该参数。

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslKey::**toPem**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*passPhrase* = QByteArray()) const

以 PEM 编码格式返回该密钥。如果该密钥为私钥并且 *passPhrase* 不为空，该密钥将利用 *passPhrase* 加密。

---

### [QSsl::KeyType](../QSsl/QSsl.md#enum-qsslkeytype) QSslKey::**type**() const

返回该密钥的类型（即公钥或私钥）。

---

### bool QSslKey::**operator!=**(const QSslKey &*other*) const

若该密钥与 *other* 不相等则返回`true` ，否则返回`false` 。

---

### bool QSslKey::**operator==**(const [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html#QSslKey) &*other*) const

若该密钥与 *other* 相等则返回`true` ，否则返回`false` 。