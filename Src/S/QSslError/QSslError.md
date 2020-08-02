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
| enum | **[SslError](#enum-qsslerrorenum-qsslerrorsslerror)** { NoError, UnableToGetIssuerCertificate, UnableToDecryptCertificateSignature, UnableToDecodeIssuerPublicKey, CertificateSignatureFailed, …, OcspStatusUnknown } |



## 公共成员函数

| 类型                | 函数名                                                       |
| ------------------- | ------------------------------------------------------------ |
|                     | **[QSslError](#qsslerrorqsslerrorconst-qsslerror-other)**(const QSslError &*other*) |
|                     | **[QSslError](#qsslerrorqsslerrorqsslerrorsslerror-error-const-qsslcertificate-certificate)**(QSslError::SslError *error*, const QSslCertificate &*certificate*) |
|                     | **[QSslError](#qsslerrorqsslerrorqsslerrorsslerror-error)**(QSslError::SslError *error*) |
|                     | **[QSslError](#qsslerrorqsslerror)**()                       |
| QSslError &         | **[operator=](#qsslerror-qsslerroroperatorconst-qsslerror-other)**(const QSslError &*other*) |
|                     | **[~QSslError](#qsslerrorqsslerror-1)**()                    |
| QSslCertificate     | **[certificate](#qsslcertificate-qsslerrorcertificate-const)**() const |
| QSslError::SslError | **[error](#qsslerrorsslerror-qsslerrorerror-const)**() const |
| QString             | **[errorString](#qstring-qsslerrorerrorstring-const)**() const |
| void                | **[swap](#void-qsslerrorswapqsslerror-other)**(QSslError &*other*) |
| bool                | **[operator!=](#bool-qsslerroroperatorconst-qsslerror-other-const)**(const QSslError &*other*) const |
| bool                | **[operator==](#bool-qsslerroroperatorconst-qsslerror-other-const-1)**(const QSslError &*other*) const |



## 详细描述



## 成员类型文档

### enum QSslError::**SslError**

该枚举类型描述了所有可以辨认的 SSL 握手时可能出现的错误类型。

| 常量                                           | 值   |
| :--------------------------------------------- | :--- |
| QSslError::NoError                             | 0    |
| QSslError::UnableToGetIssuerCertificate        | 1    |
| QSslError::UnableToDecryptCertificateSignature | 2    |
| QSslError::UnableToDecodeIssuerPublicKey       | 3    |
| QSslError::CertificateSignatureFailed          | 4    |
| QSslError::CertificateNotYetValid              | 5    |
| QSslError::CertificateExpired                  | 6    |
| QSslError::InvalidNotBeforeField               | 7    |
| QSslError::InvalidNotAfterField                | 8    |
| QSslError::SelfSignedCertificate               | 9    |
| QSslError::SelfSignedCertificateInChain        | 10   |
| QSslError::UnableToGetLocalIssuerCertificate   | 11   |
| QSslError::UnableToVerifyFirstCertificate      | 12   |
| QSslError::CertificateRevoked                  | 13   |
| QSslError::InvalidCaCertificate                | 14   |
| QSslError::PathLengthExceeded                  | 15   |
| QSslError::InvalidPurpose                      | 16   |
| QSslError::CertificateUntrusted                | 17   |
| QSslError::CertificateRejected                 | 18   |
| QSslError::SubjectIssuerMismatch               | 19   |
| QSslError::AuthorityIssuerSerialNumberMismatch | 20   |
| QSslError::NoPeerCertificate                   | 21   |
| QSslError::HostNameMismatch                    | 22   |
| QSslError::UnspecifiedError                    | -1   |
| QSslError::NoSslSupport                        | 23   |
| QSslError::CertificateBlacklisted              | 24   |
| QSslError::CertificateStatusUnknown            | 25   |
| QSslError::OcspNoResponseFound                 | 26   |
| QSslError::OcspMalformedRequest                | 27   |
| QSslError::OcspMalformedResponse               | 28   |
| QSslError::OcspInternalError                   | 29   |
| QSslError::OcspTryLater                        | 30   |
| QSslError::OcspSigRequred                      | 31   |
| QSslError::OcspUnauthorized                    | 32   |
| QSslError::OcspResponseCannotBeTrusted         | 33   |
| QSslError::OcspResponseCertIdUnknown           | 34   |
| QSslError::OcspResponseExpired                 | 35   |
| QSslError::OcspStatusUnknown                   | 36   |

另外您也可以在 [QSslError::errorString](#qstring-qsslerrorerrorstring-const)() 函数介绍中找到相关信息。



## 成员函数文档

### QSslError::**QSslError**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

拷贝构造函数。从另外一个 QSslError 对象中构造一个 QSslError 对象。

---

### QSslError::**QSslError**([QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) *error*, const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)

构造函数。两个参数，*error* 指定了出现的错误，*certificate* 指定了该错误相关的证书。

另外您也可以在 [QSslCertificate](../QSslCertificate/QSslCertificate.md) 类文档中找到相关介绍。

---

### QSslError::**QSslError**([QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) *error*)

构造函数。*error* 参数指定了出现的错误。

---

### QSslError::**QSslError**()

构造函数。使用默认证书构造一个 QSslError 对象，该对象无错误发生。

---

### [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &QSslError::**operator=**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

将 *error* 的内容分配到等式左值。

该函数最初在 Qt4.4 版本引入。

---

### QSslError::~QSslError()

析构函数。销毁 QSslError 对象。

---

### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) QSslError::**certificate**() const

返回与该错误相联系的证书。若该错误为与任何证书相关联，函数将返回 null 。

另外您也可以在 error() 和 errorString() 函数介绍中找到相关信息。

另外您也可以在 [error](#qsslerrorsslerror-qsslerrorerror-const)() 和 [errorString](#qstring-qsslerrorerrorstring-const)() 函数介绍中找到相关信息。

---

### [QSslError::SslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#SslError-enum) QSslError::**error**() const

返回出现的错误的类型。

另外您也可以在 [errorString](#qstring-qsslerrorerrorstring-const)() 和 [certificate](#qsslcertificate-qsslerrorcertificate-const)() 函数介绍中找到相关信息。

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslError::**errorString**() const

返回有关于该错误的便于阅读的、简短的描述。

另外您也可以在 [error](#qsslerrorsslerror-qsslerrorerror-const)() 和 [certificate](#qsslcertificate-qsslerrorcertificate-const)() 函数介绍中找到相关信息。

---

### void QSslError::**swap**([QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*)

与 *other* 交换迅速地错误信息。

该函数交换速度极快并保证成功执行。

该函数最初在 Qt 5.0版本引入。

---

### bool QSslError::**operator!=**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*) const

如果当前的错误与 *other* 的错误并不相同则返回 *true* ，否则返回 *false* 。

该函数最初在 Qt 4.4版本引入。

---

### bool QSslError::**operator==**(const [QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html#QSslError) &*other*) const

如果当前的错误与 *other* 的错误相同则返回 *true* ，否则返回 *false* 。

该函数最初在 Qt 4.4版本引入。