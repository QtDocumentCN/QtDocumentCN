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
|                            | **[ QSslCertificateExtension](#qsslcertificateextensionqsslcertificateextensionconst-qsslcertificateextension-other)**(const QSslCertificateExtension &*other*) |
|                            | **[QSslCertificateExtension](#qsslcertificateextensionqsslcertificateextension)**() |
| QSslCertificateExtension & | **[operator=](#qsslcertificateextension-qsslcertificateextensionoperatorconst-qsslcertificateextension-other)**(const QSslCertificateExtension &*other*) |
|                            | **[~QSslCertificateExtension](#qsslcertificateextensionqsslcertificateextension-1)**() |
| bool                       | **[isCritical](#bool-qsslcertificateextensioniscritical-const)**() const |
| bool                       | **[isSupported](#bool-qsslcertificateextensionissupported-const)**() const |
| QString                    | **[name](#qstring-qsslcertificateextensionname-const)**() const |
| QString                    | **[oid](#qstring-qsslcertificateextensionoid-const)**() const |
| void                       | **[swap](#void-qsslcertificateextensionswapqsslcertificateextension-other)**(QSslCertificateExtension &*other*) |
| QVariant                   | **[value](#qvariant-qsslcertificateextensionvalue-const)**() const |



## 详细描述

QSslCertificateExtension 类为使用 X509证书扩展提供了 API 集成。该类可获取哪些信息取决于该扩展的类型。

所有的 X509证书扩展都拥有以下属性：

| 属性        | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| name        | 该扩展的名称。例如：“basicConstraints”。                     |
| criticality | 布尔值，指定该扩展是否对正确解释该证书至关重要。             |
| oid         | ASN.1对象标识符，指定此扩展身份。                            |
| supported   | 如果该值为 *true* 则该扩展的结构不会在不同的 Qt 版本中发生变化。 |
| value       | 一个储存着该扩展类型相关的结构的 QVariant 对象。             |

尽管此类提供了对任何类型的扩展的使用支持，但是仅保证某些扩展在不同发行版之间有保持不变的格式化返回信息。 您可以使用 [isSupported](#bool-qsslcertificateextensionissupported-const)() 函数来检查是否支持该扩展。

现在支持的扩展及其返回信息结构如下：

| 扩展名                 | OID               | 描述                                                         |
| :--------------------- | :---------------- | :----------------------------------------------------------- |
| basicConstraints       | 2.5.29.19         | 作为 [QVariantMap](../../VQVariant/QVariant.md) 返回。`ca` 关键字包含着一个布尔值。可选的`pathLenConstraint`关键字包含值一个整型变量。 |
| authorityInfoAccess    | 1.3.6.1.5.5.7.1.1 | 作为 [QVariantMap](../../VQVariant/QVariant.md) 返回。每种访问方法都有一个关键字，其值为 URI 。 |
| subjectKeyIdentifier   | 2.5.29.14         | 作为包含一个 [QString](../../S/QString/QString.md) 对象的 [QVariant](../../VQVariant/QVariant.md) 返回。 该字符串是密钥标识符。 |
| authorityKeyIdentifier | 2.5.29.35         | 作为 [QVariantMap](../../VQVariant/QVariant.md) 返回。可选的关键字`keyid` 包含着一个以十六进制形式储存在 [QByteArray](../../B/QByteArray/QByteArray.md) 中的密钥标识符。可选的`serial`关键字包含着 qlonglong 格式的授权密钥序列号。现在已经不支持该扩展的通用名称域。 |

除了上面支持的扩展之外，QSslCertificateExtension 还许多其他常见的扩展，这些扩展的返回信息将以合理的结式返回。 SSL 后端不支持的扩展将作为[QByteArray](../../B/QByteArray/QByteArray.md) 返回。

关于扩展证书更多的信息您可以在 RFC 5280 标准文档中找到。

另外您也可以在 [QSslCertificate::extensions](../QSslCertificate/QSslCertificate.md#qlistqsslcertificateextension-qsslcertificateextensions-const)() 函数介绍中找到相关信息。

## 成员函数文档

### QSslCertificateExtension::**QSslCertificateExtension**(const QSslCertificateExtension &*other*)

拷贝构造函数。由 *other* 拷贝一个新的 QSslCertificateExtension 对象。

---

### QSslCertificateExtension::**QSslCertificateExtension**()

构造函数。构造一个 QSslCertificateExtension 对象。

---

### QSslCertificateExtension &QSslCertificateExtension::**operator=**(const QSslCertificateExtension &*other*)

将 *other* 赋值给该对象，并返回该对象的引用。

---

### QSslCertificateExtension::**~QSslCertificateExtension**()

析构函数。销毁该扩展对象。

---

### bool QSslCertificateExtension::**isCritical**() const

返回该扩展的关键程度。

---

### bool QSslCertificateExtension::**isSupported**() const

如果该扩展受支持则返回`true` 。在这种情况下，受支持仅仅意味着 [value](#qvariant-qsslcertificateextensionvalue-const)() 函数返回的 [QVariant](../../VQVariant/QVariant.md) 值的结构不会因为版本差异而发生变化。即使不受支持也是可以自由使用的，但是不能保证 [value](#qvariant-qsslcertificateextensionvalue-const)() 函数返回的 [QVariant](../../VQVariant/QVariant.md) 值的结构不会因为版本差异而发生变化

---

### [QString](../../S/QString/QString.md) QSslCertificateExtension::**name**() const

返回该扩展名称。若该扩展无已知名称，则返回该扩展的 OID 。

---

### [QString](../../S/QString/QString.md) QSslCertificateExtension::**oid**() const

返回该扩展的 ASN.1 OID。

---

### void QSslCertificateExtension::**swap**(QSslCertificateExtension &*other*)

与 *other* 迅速交换证书扩展。该函数执行速度极快并保证操作成功。

---

### [QVariant](../../VQVariant/QVariant.md) QSslCertificateExtension::**value**() const

返回该证书的值。该返回值的结构取决于扩展的类型。