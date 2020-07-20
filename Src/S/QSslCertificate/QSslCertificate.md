[TOC]



# QSslCertificate Class

QSslCertificate 类为 X509 证书提供了便捷的 API 集成。

| 属性   | 方法                         |
| ------ | ---------------------------- |
| 头文件 | `#include <QSslCertificate>` |
| qmake  | QT += network                |
| 引入   | Qt 4.3                       |

该类最初在 Qt 4.3 版本引入。

您可以[在此](../QSslCertificate_Obsolete/QSslCertificate_Obsolete.md)查看已经过时的类成员。

**注意：** 该类所有的函数都是可重入的。



# 公共成员类型

| 属性 | 方法                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[SubjectInfo](#enum-qsslcertificatesubjectinfo)** { Organization, CommonName, LocalityName, OrganizationalUnitName, CountryName, …, EmailAddress } |



## 公共成员函数

| 类型                                               | 函数名                                                       |
| -------------------------------------------------- | ------------------------------------------------------------ |
|                                                    | **[ QSslCertificate](#qsslcertificateqsslcertificateconst-qsslcertificate-other)**(const QSslCertificate &*other*) |
|                                                    | **[QSslCertificate](#qsslcertificateqsslcertificateconst-qbytearray-data--qbytearray-qsslencodingformat-format--qsslpem)**(const QByteArray &*data* = QByteArray(), QSsl::EncodingFormat *format* = QSsl::Pem) |
|                                                    | **[QSslCertificate](#qsslcertificateqsslcertificateqiodevice-device-qsslencodingformat-format--qsslpem)**(QIODevice **device*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QSslCertificate &                                  | **[operator=](#qsslcertificate-qsslcertificateoperatorconst-qsslcertificate-other)**(const QSslCertificate &*other*) |
|                                                    | **[~QSslCertificate](#qsslcertificateqsslcertificate)**()    |
| void                                               | **[clear](#void-qsslcertificateclear)**()                    |
| QByteArray                                         | **[digest](#qbytearray-qsslcertificatedigestqcryptographichashalgorithm-algorithm--qcryptographichashmd5-const)**(QCryptographicHash::Algorithm *algorithm* = QCryptographicHash::Md5) const |
| QDateTime                                          | **[effectiveDate](#qdatetime-qsslcertificateeffectivedate-const)**() const |
| QDateTime                                          | **[expiryDate](#qdatetime-qsslcertificateexpirydate-const)**() const |
| QList\<QSslCertificateExtension\>                  | **[extensions](#qlistqsslcertificateextension-qsslcertificateextensions-const)**() const |
| Qt::HANDLE                                         | **[handle](#qthandle-qsslcertificatehandle-const)**() const  |
| bool                                               | **[isBlacklisted](#bool-qsslcertificateisblacklisted-const)**() const |
| bool                                               | **[isNull](#bool-qsslcertificateisnull-const)**() const      |
| bool                                               | **[isSelfSigned](#bool-qsslcertificateisselfsigned-const)**() const |
| QString                                            | **[issuerDisplayName](#qstring-qsslcertificateissuerdisplayname-const)**() const |
| QStringList                                        | **[issuerInfo](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const)**(QSslCertificate::SubjectInfo *subject*) const |
| QStringList                                        | **[issuerInfo](#qstringlist-qsslcertificateissuerinfoconst-qbytearray-attribute-const)**(const QByteArray &*attribute*) const |
| QList\<QByteArray\>                                | **[issuerInfoAttributes](#qlistqbytearray-qsslcertificateissuerinfoattributes-const)**() const |
| QSslKey                                            | **[publicKey](#qsslkey-qsslcertificatepublickey-const)**() const |
| QByteArray                                         | **[serialNumber](#qbytearray-qsslcertificateserialnumber-const)**() const |
| QMultiMap<QSsl::AlternativeNameEntryType, QString> | **[subjectAlternativeNames](#qmultimapqsslalternativenameentrytype-qstring-qsslcertificatesubjectalternativenames-const)**() const |
| QString                                            | **[subjectDisplayName](#qstring-qsslcertificatesubjectdisplayname-const)**() const |
| QStringList                                        | **[subjectInfo](#qstringlist-qsslcertificatesubjectinfoqsslcertificatesubjectinfo-subject-const)**(QSslCertificate::SubjectInfo *subject*) const |
| QStringList                                        | **[subjectInfo](#qstringlist-qsslcertificatesubjectinfoconst-qbytearray-attribute-const)**(const QByteArray &*attribute*) const |
| QList\<QByteArray\>                                | **[subjectInfoAttributes](#qlistqbytearray-qsslcertificatesubjectinfoattributes-const)**() const |
| void                                               | **[swap](#void-qsslcertificateswapqsslcertificate-other)**(QSslCertificate &*other*) |
| QByteArray                                         | **[toDer](#qbytearray-qsslcertificatetoder-const)**() const  |
| QByteArray                                         | **[toPem](#qbytearray-qsslcertificatetopem-const)**() const  |
| QString                                            | **[toText](#qstring-qsslcertificatetotext-const)**() const   |
| QByteArray                                         | **[version](#qbytearray-qsslcertificateversion-const)**() const |
| bool                                               | **[operator!=](#bool-qsslcertificateoperatorconst-qsslcertificate-other-const)**(const QSslCertificate &*other*) const |
| bool                                               | **[operator==](#bool-qsslcertificateoperatorconst-qsslcertificate-other-const-1)**(const QSslCertificate &*other*) const |



## 静态成员

| 类型                     | 函数名                                                       |
| ------------------------ | ------------------------------------------------------------ |
| QList\<QSslCertificate\> | **[fromData](#static-qlistqsslcertificate-qsslcertificatefromdataconst-qbytearray-data-qsslencodingformat-format--qsslpem)**(const QByteArray &*data*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QList\<QSslCertificate\> | **[fromDevice](#static-qlistqsslcertificate-qsslcertificatefromdeviceqiodevice-device-qsslencodingformat-format--qsslpem)**(QIODevice **device*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QList\<QSslCertificate\> | **[fromPath](#static-qlistqsslcertificate-qsslcertificatefrompathconst-qstring-path-qsslencodingformat-format--qsslpem-qsslcertificatepatternsyntax-syntax--patternsyntaxfixedstring)**(const QString &*path*, QSsl::EncodingFormat *format* = QSsl::Pem, QSslCertificate::PatternSyntax *syntax* = PatternSyntax::FixedString) |
| bool                     | **[importPkcs12](#static-bool-qsslcertificateimportpkcs12qiodevice-device-qsslkey-key-qsslcertificate-certificate-qlistqsslcertificate-cacertificates--nullptr-const-qbytearraypassphrase--qbytearray)**(QIODevice \**device*, QSslKey \**key*, QSslCertificate \**certificate*, QList\<QSslCertificate\> \**caCertificates* = nullptr, const QByteArray &*passPhrase* = QByteArray()) |
| QList\<QSslError\>       | **[verify](#static-qlistqsslerror-qsslcertificateverifyqlistqsslcertificate-certificatechain-const-qstring-hostname--qstring)**(QList\<QSslCertificate\> *certificateChain*, const QString &*hostName* = QString()) |



## 详细描述



## 成员类型文档

### enum QSslCertificate::**SubjectInfo**

描述了您可以传递到 [QSslCertificate::issuerInfo](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const)() 和 [QSslCertificate::subjectInfo](#qstringlist-qsslcertificatesubjectinfoqsslcertificatesubjectinfo-subject-const)() 函数的键。您可以通过这些键查找出对应的发行人、主题的有关信息。

| 常量                                        | 值   | 描述                               |
| :------------------------------------------ | :--- | :--------------------------------- |
| QSslCertificate::Organization               | 0    | "O"：组织。                        |
| QSslCertificate::CommonName                 | 1    | "CN"：常用名，通常用来储存主机名。 |
| QSslCertificate::LocalityName               | 2    | "L"：地区。                        |
| QSslCertificate::OrganizationalUnitName     | 3    | "OU" ：组织单位。                  |
| QSslCertificate::CountryName                | 4    | "C" ：国家。                       |
| QSslCertificate::StateOrProvinceName        | 5    | "ST" ：州或省。                    |
| QSslCertificate::DistinguishedNameQualifier | 6    | 专有名称修饰符。                   |
| QSslCertificate::SerialNumber               | 7    | 证书系列号。                       |
| QSslCertificate::EmailAddress               | 8    | 邮件地址。                         |



## 成员函数文档

### QSslCertificate::**QSslCertificate**(const QSslCertificate &*other*)

拷贝构造函数。由 *other* 拷贝出新的一份 QSslCertificate 对象。

---

### QSslCertificate::**QSslCertificate**(const [QByteArray](../../B/QByteArray/QByteArray.md) &*data* = QByteArray(), [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format* = QSsl::Pem)

构造函数。使用 *format* 指定的编码格式对 *data* 进行编码作为证书数据，并使用第一个找到的可用证书构造一个 QSslCertificate 对象。

构造后，您可以使用 [isNull](#bool-qsslcertificateisnull-const)() 函数来检查 *data* 是否包含一个证书或者该证书是否已经成功载入。

---

### QSslCertificate::**QSslCertificate**([QIODevice](../../I/QIODevice/QIODevice.md) **device*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format* = QSsl::Pem)

构造函数。从 *device* 指定的 IO 设备中读取以 *format* 格式编码的数据，并使用第一个找到的可用证书构造一个 QSslCertificate 对象。

构造后，您可以使用 [isNull](#bool-qsslcertificateisnull-const)() 函数来检查 *data* 是否包含一个证书或者该证书是否已经成功载入。

---

### QSslCertificate &QSslCertificate::**operator=**(const QSslCertificate &*other*)

将 *other* 的内容拷贝到此证书，使等式左右值相等。

---

### QSslCertificate::**~QSslCertificate**()

析构函数。销毁 QSslCertificate 对象。

---

### void QSslCertificate::**clear**()

清除该证书的内容，使其变为空证书。

另外您也可以在 [isNull](#bool-qsslcertificateisnull-const)() 函数介绍中找到相关内容。

---

### [QByteArray](../../B/QByteArray/QByteArray.md) QSslCertificate::**digest**([QCryptographicHash::Algorithm](qthelp://org.qt-project.qtnetwork.5150/qtcore/qcryptographichash.html#Algorithm-enum) *algorithm* = QCryptographicHash::Md5) const

返回该证书的加密摘要。默认情况下将会使用 MD5 算法生成数字摘要，您也可以指定使用 *algorithm* 摘要算法。

---

### [QDateTime](../../D/QDateTime/QDateTime.md) QSslCertificate::**effectiveDate**() const

返回该证书的生效日期。若该证书为空，则返回一个空的 QDateTime 对象。

另外您也可以在 [expiryDate](#qdatetime-qsslcertificateexpirydate-const)() 函数介绍中找到相关信息。

---

### [QDateTime](../../D/QDateTime/QDateTime.md) QSslCertificate::**expiryDate**() const

返回该证书过期日期。若该证书为空，则返回一个空的 QDateTime 对象。

另外您也可以在 [effectiveDate](#qdatetime-qsslcertificateeffectivedate-const)() 函数介绍中找到相关信息。

---

### [QList](../../L/QList/QList.md)\<[QSslCertificateExtension](../QSslCertificateExtension/QSslCertificateExtension.md)\> QSslCertificate::**extensions**() const

返回此证书所包含的 X509 扩展列表。

该函数最早在 Qt 5.0 版本引入。

---

### *[static]* [QList](../../L/QList/QList.md)\<QSslCertificate\> QSslCertificate::**fromData**(const [QByteArray](../../B/QByteArray/QByteArray.md) &*data*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format* = QSsl::Pem)

搜索 *data* 中所有 *format* 编码格式的证书，并返回这些证书的列表。

另外您也可以在 [fromDevice](#static-qlistqsslcertificate-qsslcertificatefromdeviceqiodevice-device-qsslencodingformat-format--qsslpem)() 函数介绍中找到相关信息。

---

### *[static]* [QList](../../L/QList/QList.md)\<QSslCertificate> QSslCertificate::**fromDevice**([QIODevice](../../I/QIODevice/QIODevice.md) **device*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format* = QSsl::Pem)

搜索设备 *device* 中所有 *format* 编码格式的证书，并返回这些证书的列表。

另外您也可以在 [fromData](#static-qlistqsslcertificate-qsslcertificatefromdataconst-qbytearray-data-qsslencodingformat-format--qsslpem)() 函数介绍中找到相关信息。

---

### *[static]* [QList](../../L/QList/QList.md)\<QSslCertificate> QSslCertificate::**fromPath**(const [QString](../../S/QString/QString.md) &*path*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format* = QSsl::Pem, QSslCertificate::PatternSyntax *syntax* = PatternSyntax::FixedString)

搜索路径 *path* 中所有 *format* 编码格式的证书，并返回这些证书的列表。 *path* 必须是一个文件，*pattern* 指定的模式必须能检测到至少一个文件。

Qt 官方示例如下：

```cpp
 const auto certs = QSslCertificate::fromPath("C:/ssl/certificate.*.pem",
                                              QSsl::Pem, QSslCertificate::Wildcard);
 for (const QSslCertificate &cert : certs) {
     qDebug() << cert.issuerInfo(QSslCertificate::Organization);
 }
```

该函数最初在 Qt 5.15版本引入。

另外您也可以在 [fromData](#static-qlistqsslcertificate-qsslcertificatefromdataconst-qbytearray-data-qsslencodingformat-format--qsslpem)() 函数介绍中找到相关信息。

---

### [Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) QSslCertificate::**handle**() const

返回证书的本地句柄，若该证书没有句柄则返回 *nullptr* 。

您可以结合本地 API 来使用本句柄，这样便可获取该证书的拓展信息。

**警告：** 使用此功能很有可能无法移植，其返回值可能因平台而异，或因次要发行版而异。

---

### *[static]* bool QSslCertificate::**importPkcs12**([QIODevice](../../I/QIODevice/QIODevice.md) \**device*, [QSslKey](../QSslKey/QSslKey.md) \**key*, QSslCertificate \**certificate*, [QList](../../L/QList/QList.md)\<QSslCertificate> **caCertificates* = nullptr, const [QByteArray](../../B/QByteArray/QByteArray.md) &*passPhrase* = QByteArray())

从指定的设备 *device* 中导入 PKCS#12 (pfx) 文件。一个 PKCS#12 是一个包含了众多证书和私钥的包。这个函数会读取一条私钥 *key* ，和与这个私钥的证书 *certificate* 以及这个包中任何相关的证书 *caCertificates* 。 如果指定了 *passPhrase* ，该函数会使用 *passPhrase* 去解码该包。如果 PKCS#12 文件成功导入则返回 *true* 。

**注意：** 设备 *device* 必须已经打开并追被好从中读取数据。

该函数最初在 Qt 5.4版本引入。

This function was introduced in Qt 5.4.

---

### bool QSslCertificate::**isBlacklisted**() const

如果该证书被列入黑名单则返回 *true* ，否则返回 *false* 。

另外您也可以在 [isNull](#bool-qsslcertificateisnull-const)() 函数介绍中找到相关信息。

---

### bool QSslCertificate::**isNull**() const

如果该证书为空则返回 *true* ，否则返回 *false* 。

默认情况下，QSslCertificate 对象会构造一个空的证书。

另外你您也可以在 [clear](#void-qsslcertificateclear)() 函数介绍中找到相关信息。

---

### bool QSslCertificate::**isSelfSigned**() const

如果该证书为自签名证书则返回 *true* ，否则返回 *false* 。

如果该证书的发行人和主题相同，则会被认为是一个自签名证书。

该函数最初在 Qt 5.4版本引入。

---

### [QString](../../S/QString/QString.md) QSslCertificate::**issuerDisplayName**() const

返回发行者的名称。如果可获得 [QSslCertificate::CommonName ](#enum-qsslcertificatesubjectinfo) 则将返回该值，否则将返回首个 [QSslCertificate::Organization](#enum-qsslcertificatesubjectinfo) 或者首个 [QSslCertificate::OrganizationalUnitName](#enum-qsslcertificatesubjectinfo) 。

该函数最初在 Qt 5.12版本引入。

另外您也可以在 [issuerInfo()](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const) 函数介绍中找到相关信息。

---

### [QStringList](../../S/QStringList/QStringList.md) QSslCertificate::**issuerInfo**([QSslCertificate::SubjectInfo](#enum-qsslcertificatesubjectinfo) *subject*) const

返回 *subject* 指定的发行信息，若 *subject* 指定的发行信息为空贼返回一个空的列表。每种类型可能不止有一条记录。

另外您也可以在 [subjectInfo](#qstringlist-qsslcertificatesubjectinfoconst-qbytearray-attribute-const)() 函数介绍中找到相关信息。

---

### [QStringList](../../S/QStringList/QStringList.md) QSslCertificate::**issuerInfo**(const [QByteArray](../../B/QByteArray/QByteArray.md) &*attribute*) const

返回证书中 *attribute* 指定的属性的发行信息。若该属性指定的发行信息为空则返回一个空列表。每种属性可能不止有一条记录。

另外您也可以在 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数介绍中找到相关信息。

---

### [QList](../../L/QList/QList.md)\<[QByteArray](../../B/QByteArray/QByteArray.md)\> QSslCertificate::**issuerInfoAttributes**() const

返回发行信息中有值的属性的列表。与一个给定属性先关联的信息可以使用 [issuerInfo()](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const)() 函数来查看。请注意，此列表可能包含 SSL 后端未知的任何元素的 OID 。

该函数最初在 Qt 5.0版本引入。

另外您也可以在 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数介绍中找到相关信息。

---

### [QSslKey](../QSslKey/QSslKey.md) QSslCertificate::**publicKey**() const

返回证书的公钥。

---

### [QByteArray](../../B/QByteArray/QByteArray.md) QSslCertificate::**serialNumber**() const

返回十六进制形式的该证书的系列号。

---

### [QMultiMap](../../QMultiMap/QMultiMap.md)<[QSsl::AlternativeNameEntryType](../QSsl/QSsl.md#enum-qsslalternativenameentrytype), [QString](../../S/QString/QString.md)> QSslCertificate::**subjectAlternativeNames**() const

返回该证书可选主题的名称列表。可选名称通常来说包含该证书的主机名，有时候会包含通配符。

如果 [CommonName](#enum-qsslcertificatesubjectinfo) 的主题信息未定义一个有效的主机名或者主题信息名称不能匹配对等端的主机名，则将这些名称与连接的对等方的主机名进行测试。 

另外您也可以在 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数介绍中找到相关信息。

---

### [QString](../../S/QString/QString.md) QSslCertificate::**subjectDisplayName**() const

返回主题的名称。如果可获得 [QSslCertificate::CommonName ](#enum-qsslcertificatesubjectinfo) 则将返回该值，否则将返回首个 [QSslCertificate::Organization](#enum-qsslcertificatesubjectinfo) 或者首个 [QSslCertificate::OrganizationalUnitName](#enum-qsslcertificatesubjectinfo) 。

该函数最初在 Qt 5.12版本引入。

另外您也可以在 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数介绍中找到相关信息。

---

### [QStringList](../../S/QStringList/QStringList.md) QSslCertificate::**subjectInfo**([QSslCertificate::SubjectInfo](#enum-qsslcertificatesubjectinfo) *subject*) const

返回证书中 *subject* 指定的主题的信息。若该主题指定的主题信息为空则返回一个空列表。每种主题可能不止有一条记录。

另外您也可以在 [issuerInfo()](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const) 函数介绍中找到相关信息。

---

### [QStringList](../../S/QStringList/QStringList.md) QSslCertificate::**subjectInfo**(const [QByteArray](../../B/QByteArray/QByteArray.md) &*attribute*) const

返回证书中 *attribute* 指定的主题的发行信息。若该属性指定的主题信息为空则返回一个空列表。每种属性可能不止有一条记录。

另外您也可以在 [issuerInfo()](#qstringlist-qsslcertificateissuerinfoqsslcertificatesubjectinfo-subject-const) 函数介绍中找到相关信息。

---

### [QList](../../L/QList/QList.md)\<[QByteArray](../../B/QByteArray/QByteArray.md)\> QSslCertificate::**subjectInfoAttributes**() const

返回该证书中包含主题信息的属性列表。与给定属性相关的信息可以使用 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数来获取。请注意，此列表可能包含 SSL 后端未知的任何元素的 OID 。

该函数最初在 Qt 5.0版本引入。

另外您也可以在 [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() 函数介绍中找到相关信息。

---

### void QSslCertificate::**swap**(QSslCertificate &*other*)

将该证书的内容与 *other* 快速交换。该函数执行速度极快并保证操作成功。

该函数最初在 Qt 5.0版本引入。

---

### [QByteArray](../../B/QByteArray/QByteArray.md) QSslCertificate::**toDer**() const

将证书转化为 DER（binary）格式返回。

---

### [QByteArray](../../B/QByteArray/QByteArray.md) QSslCertificate::**toPem**() const

将证书转化为 PEM（Base64）格式返回。

---

### [QString](../../QString/QString.md) QSslCertificate::**toText**() const

将证书转化为易于阅读的形式返回。

该函数最初在 Qt 5.0版本引入。

---

### *[static]* [QList](../../L/QList/QList.md)\<[QSslError](../QSslError/QSslError.md)\> QSslCertificate::**verify**([QList](../../L/QList/QList.md)\<QSslCertificate> *certificateChain*, const [QString](../../QString/QString.md) &*hostName* = QString())

验证 *certificateChain* 参数指定的证书链。列表中的第一个证书应是要验证的链的节点证书。如果 *hostName* 指定了一个主机地址，该函数也会检查该证书是否对主机名有效。

请注意，根（CA）证书不应包含在要验证的列表中，可以使用 QSslSocket::defaultCaCertificates() 指定的CA列表自动查找。在 Unix 平台上也可以在需要时将其加载。

该函数最初在 Qt 5.0版本引入。

---

### [QByteArray](../../B/QByteArray/QByteArray.md) QSslCertificate::**version**() const

以字符串的形式返回该证书的版本。

---

### bool QSslCertificate::**operator!=**(const QSslCertificate &*other*) const

如果该证书不与 *other*  相同返回 *true* ，否则返回 *false* 。

---

### bool QSslCertificate::**operator==**(const QSslCertificate &*other*) const

如果该证书与 *other*  相同返回 *true* ，否则返回 *false* 。