[TOC]



# QSslError Class

QSslError 类提供了一些关于 SSl 错误的相关信息与操作。

| 属性   | 方法                   |
| ------ | ---------------------- |
| 头文件 | `#include <QSslError>` |
| qmake  | QT += network          |
| 引入   | Qt 4.3                 |

该类最初在 Qt 4.3版本引入。

**注意：** 该类所有的函数都是可重入的。



## 公共成员类型

| 类型 | 属性                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum)** { NoError, UnableToGetIssuerCertificate, UnableToDecryptCertificateSignature, UnableToDecodeIssuerPublicKey, CertificateSignatureFailed, …, OcspStatusUnknown } |



## 公共成员函数

| 类型                | 函数名                                                       |
| ------------------- | ------------------------------------------------------------ |
|                     | **[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError-3)**(const QSslError &*other*) |
|                     | **[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError-2)**(QSslError::SslError *error*, const QSslCertificate &*certificate*) |
|                     | **[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError-1)**(QSslError::SslError *error*) |
|                     | **[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError)**() |
| QSslError &         | **[operator=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#operator-eq-1)**(const QSslError &*other*) |
|                     | **[~QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#dtor.QSslError)**() |
| QSslCertificate     | **[certificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#certificate)**() const |
| QSslError::SslError | **[error](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#error)**() const |
| QString             | **[errorString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#errorString)**() const |
| void                | **[swap](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#swap)**(QSslError &*other*) |
| bool                | **[operator!=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#operator-not-eq)**(const QSslError &*other*) const |
| bool                | **[operator==](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#operator-eq-eq)**(const QSslError &*other*) const |



## 详细描述



## 成员类型文档

### enum QSslError::enum QSslError::SslError



## 成员函数文档

### QSslError::**QSslError**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

Constructs an identical copy of *other*.

---

### QSslError::**QSslError**([QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) *error*, const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)

Constructs a QSslError object. The two arguments specify the *error* that occurred, and which *certificate* the error relates to.

**See also** [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html).

---

### QSslError::**QSslError**([QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) *error*)

Constructs a QSslError object. The argument specifies the *error* that occurred.

---

### QSslError::**QSslError**()

Constructs a QSslError object with no error and default certificate.

---

### [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &QSslError::**operator=**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

Assigns the contents of *other* to this error.

This function was introduced in Qt 4.4.

---

### QSslError::~QSslError()

Destroys the [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html) object.

---

### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) QSslError::**certificate**() const

Returns the certificate associated with this error, or a null certificate if the error does not relate to any certificate.

**See also** [error](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#error)() and [errorString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#errorString)().

---

### [QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) QSslError::**error**() const

Returns the type of the error.

**See also** [errorString](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#errorString)() and [certificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#certificate)().

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslError::**errorString**() const

Returns a short localized human-readable description of the error.

**See also** [error](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#error)() and [certificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#certificate)().

---

### void QSslError::**swap**([QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

Swaps this error instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

---

### bool QSslError::**operator!=**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*) const

Returns `true` if this error is not equal to *other*; otherwise returns false.

This function was introduced in Qt 4.4.

---

### bool QSslError::**operator==**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*) const

Returns `true` if this error is equal to *other*; otherwise returns `false`.

This function was introduced in Qt 4.4.