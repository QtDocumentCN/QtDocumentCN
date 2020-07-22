[TOC]



# QSslCertificateExtension Class

QSslCertificateExtension 类为使用 X509证书扩展提供了 API 支持。

| 属性   | 方法                                  |
| ------ | ------------------------------------- |
| 头文件 | `#include <QSslCertificateExtension>` |
| qmake  | QT += network                         |
| 引入   | Qt 5.0                                |

该类最初在 Qt 5.0版本引入。

**注意：** 该类所有的成员函数都是可重入的。



## 公共成员函数

| 类型                       | 函数名                                                       |
| -------------------------- | ------------------------------------------------------------ |
|                            | **[ QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension-1)**(const QSslCertificateExtension &*other*) |
|                            | **[QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension)**() |
| QSslCertificateExtension & | **[operator=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#operator-eq-1)**(const QSslCertificateExtension &*other*) |
|                            | **[~QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#dtor.QSslCertificateExtension)**() |
| bool                       | **[isCritical](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#isCritical)**() const |
| bool                       | **[isSupported](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#isSupported)**() const |
| QString                    | **[name](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#name)**() const |
| QString                    | **[oid](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#oid)**() const |
| void                       | **[swap](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#swap)**(QSslCertificateExtension &*other*) |
| QVariant                   | **[value](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#value)**() const |



## 详细描述





## 成员函数文档

### QSslCertificateExtension::**QSslCertificateExtension**(const [QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension) &*other*)

Constructs a copy of *other*.

### QSslCertificateExtension::**QSslCertificateExtension**()

Constructs a QSslCertificateExtension.

### [QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension) &QSslCertificateExtension::**operator=**(const [QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension) &*other*)

Assigns *other* to this extension and returns a reference to this extension.

### QSslCertificateExtension::**~QSslCertificateExtension**()

Destroys the extension.

### bool QSslCertificateExtension::**isCritical**() const

Returns the criticality of the extension.

### bool QSslCertificateExtension::**isSupported**() const

Returns the true if this extension is supported. In this case, supported simply means that the structure of the [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) returned by the [value](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#value)() accessor will remain unchanged between versions. Unsupported extensions can be freely used, however there is no guarantee that the returned data will have the same structure between versions.

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCertificateExtension::**name**() const

Returns the name of the extension. If no name is known for the extension then the OID will be returned.

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCertificateExtension::**oid**() const

Returns the ASN.1 OID of this extension.

### void QSslCertificateExtension::**swap**([QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html#QSslCertificateExtension) &*other*)

Swaps this certificate extension instance with *other*. This function is very fast and never fails.

### [QVariant](qthelp://org.qt-project.qtnetwork.5150/qtcore/qvariant.html) QSslCertificateExtension::**value**() const

Returns the value of the extension. The structure of the value returned depends on the extension type.