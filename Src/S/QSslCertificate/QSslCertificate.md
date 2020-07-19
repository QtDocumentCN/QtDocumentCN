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
| enum | **[SubjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum)** { Organization, CommonName, LocalityName, OrganizationalUnitName, CountryName, …, EmailAddress } |



## 公共成员函数

| 类型                                               | 函数名                                                       |
| -------------------------------------------------- | ------------------------------------------------------------ |
|                                                    | **[ QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate-2)**(const QSslCertificate &*other*) |
|                                                    | **[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate-1)**(const QByteArray &*data* = QByteArray(), QSsl::EncodingFormat *format* = QSsl::Pem) |
|                                                    | **[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)**(QIODevice **device*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QSslCertificate &                                  | **[operator=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#operator-eq-1)**(const QSslCertificate &*other*) |
|                                                    | **[~QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#dtor.QSslCertificate)**() |
| void                                               | **[clear](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#clear)**() |
| QByteArray                                         | **[digest](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#digest)**(QCryptographicHash::Algorithm *algorithm* = QCryptographicHash::Md5) const |
| QDateTime                                          | **[effectiveDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#effectiveDate)**() const |
| QDateTime                                          | **[expiryDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#expiryDate)**() const |
| QList\<QSslCertificateExtension\>                  | **[extensions](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#extensions)**() const |
| Qt::HANDLE                                         | **[handle](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#handle)**() const |
| bool                                               | **[isBlacklisted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isBlacklisted)**() const |
| bool                                               | **[isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)**() const |
| bool                                               | **[isSelfSigned](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isSelfSigned)**() const |
| QString                                            | **[issuerDisplayName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerDisplayName)**() const |
| QStringList                                        | **[issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)**(QSslCertificate::SubjectInfo *subject*) const |
| QStringList                                        | **[issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo-1)**(const QByteArray &*attribute*) const |
| QList\<QByteArray\>                                | **[issuerInfoAttributes](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfoAttributes)**() const |
| QSslKey                                            | **[publicKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#publicKey)**() const |
| QByteArray                                         | **[serialNumber](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#serialNumber)**() const |
| QMultiMap<QSsl::AlternativeNameEntryType, QString> | **[subjectAlternativeNames](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectAlternativeNames)**() const |
| QString                                            | **[subjectDisplayName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectDisplayName)**() const |
| QStringList                                        | **[subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)**(QSslCertificate::SubjectInfo *subject*) const |
| QStringList                                        | **[subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo-1)**(const QByteArray &*attribute*) const |
| QList\<QByteArray\>                                | **[subjectInfoAttributes](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfoAttributes)**() const |
| void                                               | **[swap](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#swap)**(QSslCertificate &*other*) |
| QByteArray                                         | **[toDer](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#toDer)**() const |
| QByteArray                                         | **[toPem](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#toPem)**() const |
| QString                                            | **[toText](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#toText)**() const |
| QByteArray                                         | **[version](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#version)**() const |
| bool                                               | **[operator!=](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#operator-not-eq)**(const QSslCertificate &*other*) const |
| bool                                               | **[operator==](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#operator-eq-eq)**(const QSslCertificate &*other*) const |



## 静态成员

| 类型                     | 函数名                                                       |
| ------------------------ | ------------------------------------------------------------ |
| QList\<QSslCertificate\> | **[fromData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromData)**(const QByteArray &*data*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QList\<QSslCertificate\> | **[fromDevice](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromDevice)**(QIODevice **device*, QSsl::EncodingFormat *format* = QSsl::Pem) |
| QList\<QSslCertificate\> | **[fromPath](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromPath-1)**(const QString &*path*, QSsl::EncodingFormat *format* = QSsl::Pem, QSslCertificate::PatternSyntax *syntax* = PatternSyntax::FixedString) |
| bool                     | **[importPkcs12](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#importPkcs12)**(QIODevice \**device*, QSslKey \**key*, QSslCertificate \**certificate*, QList\<QSslCertificate\> \**caCertificates* = nullptr, const QByteArray &*passPhrase* = QByteArray()) |
| QList\<QSslError\>       | **[verify](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#verify)**(QList\<QSslCertificate\> *certificateChain*, const QString &*hostName* = QString()) |



## 详细描述



## 成员类型文档

### enum QSslCertificate::**SubjectInfo**

Describes keys that you can pass to [QSslCertificate::issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)() or [QSslCertificate::subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() to get information about the certificate issuer or subject.

| Constant                                    | Value | Description                                                  |
| :------------------------------------------ | :---- | :----------------------------------------------------------- |
| QSslCertificate::Organization               | 0     | "O" The name of the organization.                            |
| QSslCertificate::CommonName                 | 1     | "CN" The common name; most often this is used to store the host name. |
| QSslCertificate::LocalityName               | 2     | "L" The locality.                                            |
| QSslCertificate::OrganizationalUnitName     | 3     | "OU" The organizational unit name.                           |
| QSslCertificate::CountryName                | 4     | "C" The country.                                             |
| QSslCertificate::StateOrProvinceName        | 5     | "ST" The state or province.                                  |
| QSslCertificate::DistinguishedNameQualifier | 6     | The distinguished name qualifier                             |
| QSslCertificate::SerialNumber               | 7     | The certificate's serial number                              |
| QSslCertificate::EmailAddress               | 8     | The email address associated with the certificate            |



## 成员函数文档

### QSslCertificate::**QSslCertificate**(const QSslCertificate &*other*)

Constructs an identical copy of *other*.

---

### QSslCertificate::**QSslCertificate**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*data* = QByteArray(), [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)

Constructs a QSslCertificate by parsing the *format* encoded *data* and using the first available certificate found. You can later call [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)() to see if *data* contained a certificate, and if this certificate was loaded successfully.

---

### QSslCertificate::**QSslCertificate**([QIODevice](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html) **device*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)

Constructs a QSslCertificate by reading *format* encoded data from *device* and using the first certificate found. You can later call [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)() to see if *device* contained a certificate, and if this certificate was loaded successfully.

---

### [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) &QSslCertificate::**operator=**(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) &*other*)

Copies the contents of *other* into this certificate, making the two certificates identical.

---

### QSslCertificate::**~QSslCertificate**()

Destroys the [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html).

---

### void QSslCertificate::**clear**()

Clears the contents of this certificate, making it a null certificate.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)().

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslCertificate::**digest**([QCryptographicHash::Algorithm](qthelp://org.qt-project.qtnetwork.5150/qtcore/qcryptographichash.html#Algorithm-enum) *algorithm* = QCryptographicHash::Md5) const

Returns a cryptographic digest of this certificate. By default, an MD5 digest will be generated, but you can also specify a custom *algorithm*.

---

### [QDateTime](qthelp://org.qt-project.qtnetwork.5150/qtcore/qdatetime.html) QSslCertificate::**effectiveDate**() const

Returns the date-time that the certificate becomes valid, or an empty [QDateTime](qthelp://org.qt-project.qtnetwork.5150/qtcore/qdatetime.html) if this is a null certificate.

**See also** [expiryDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#expiryDate)().

---

### [QDateTime](qthelp://org.qt-project.qtnetwork.5150/qtcore/qdatetime.html) QSslCertificate::**expiryDate**() const

Returns the date-time that the certificate expires, or an empty [QDateTime](qthelp://org.qt-project.qtnetwork.5150/qtcore/qdatetime.html) if this is a null certificate.

**See also** [effectiveDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#effectiveDate)().

---

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificateExtension](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificateextension.html)\> QSslCertificate::**extensions**() const

Returns a list containing the X509 extensions of this certificate.

This function was introduced in Qt 5.0.

---

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)\> QSslCertificate::**fromData**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*data*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)

Searches for and parses all certificates in *data* that are encoded in the specified *format* and returns them in a list of certificates.

**See also** [fromDevice](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromDevice)().

---

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)\> QSslCertificate::**fromDevice**([QIODevice](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html) **device*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem)

Searches for and parses all certificates in *device* that are encoded in the specified *format* and returns them in a list of certificates.

**See also** [fromData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromData)().

---

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)\> QSslCertificate::**fromPath**(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*path*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem, QSslCertificate::PatternSyntax *syntax* = PatternSyntax::FixedString)

Searches all files in the *path* for certificates encoded in the specified *format* and returns them in a list. *path* must be a file or a pattern matching one or more files, as specified by *syntax*.

Example:

```
 const auto certs = QSslCertificate::fromPath("C:/ssl/certificate.*.pem",
                                              QSsl::Pem, QSslCertificate::Wildcard);
 for (const QSslCertificate &cert : certs) {
     qDebug() << cert.issuerInfo(QSslCertificate::Organization);
 }
```

This function was introduced in Qt 5.15.

**See also** [fromData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#fromData)().

---

### [Qt::HANDLE](qthelp://org.qt-project.qtnetwork.5150/qtcore/qt.html#HANDLE-typedef) QSslCertificate::**handle**() const

Returns a pointer to the native certificate handle, if there is one, else `nullptr`.

You can use this handle, together with the native API, to access extended information about the certificate.

**Warning:** Use of this function has a high probability of being non-portable, and its return value may vary from platform to platform or change from minor release to minor release.

---

### *[static]* bool QSslCertificate::**importPkcs12**([QIODevice](qthelp://org.qt-project.qtnetwork.5150/qtcore/qiodevice.html) \**device*, [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) \**key*, [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) \**certificate*, [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)\> **caCertificates* = nullptr, const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)&*passPhrase* = QByteArray())

Imports a PKCS#12 (pfx) file from the specified *device*. A PKCS#12 file is a bundle that can contain a number of certificates and keys. This method reads a single *key*, its *certificate* and any associated *caCertificates* from the bundle. If a *passPhrase* is specified then this will be used to decrypt the bundle. Returns `true` if the PKCS#12 file was successfully loaded.

**Note:** The *device* must be open and ready to be read from.

This function was introduced in Qt 5.4.

---

### bool QSslCertificate::**isBlacklisted**() const

Returns `true` if this certificate is blacklisted; otherwise returns `false`.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)().

---

### bool QSslCertificate::**isNull**() const

Returns `true` if this is a null certificate (i.e., a certificate with no contents); otherwise returns `false`.

By default, [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) constructs a null certificate.

**See also** [clear](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#clear)().

---

### bool QSslCertificate::**isSelfSigned**() const

Returns `true` if this certificate is self signed; otherwise returns `false`.

A certificate is considered self-signed its issuer and subject are identical.

This function was introduced in Qt 5.4.

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCertificate::**issuerDisplayName**() const

Returns a name that describes the issuer. It returns the [QSslCertificate::CommonName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) if available, otherwise falls back to the first [QSslCertificate::Organization](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) or the first [QSslCertificate::OrganizationalUnitName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum).

This function was introduced in Qt 5.12.

**See also** [issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)().

---

### [QStringList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstringlist.html) QSslCertificate::**issuerInfo**([QSslCertificate::SubjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) *subject*) const

Returns the issuer information for the *subject* from the certificate, or an empty list if there is no information for *subject* in the certificate. There can be more than one entry of each type.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### [QStringList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstringlist.html) QSslCertificate::**issuerInfo**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*attribute*) const

Returns the issuer information for *attribute* from the certificate, or an empty list if there is no information for *attribute* in the certificate. There can be more than one entry for an attribute.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)\> QSslCertificate::**issuerInfoAttributes**() const

Returns a list of the attributes that have values in the issuer information of this certificate. The information associated with a given attribute can be accessed using the [issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)() method. Note that this list may include the OIDs for any elements that are not known by the SSL backend.

This function was introduced in Qt 5.0.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) QSslCertificate::**publicKey**() const

Returns the certificate subject's public key.

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslCertificate::**serialNumber**() const

Returns the certificate's serial number string in hexadecimal format.

---

### [QMultiMap](qthelp://org.qt-project.qtnetwork.5150/qtcore/qmultimap.html)<[QSsl::AlternativeNameEntryType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#AlternativeNameEntryType-enum), [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html)> QSslCertificate::**subjectAlternativeNames**() const

Returns the list of alternative subject names for this certificate. The alternative names typically contain host names, optionally with wildcards, that are valid for this certificate.

These names are tested against the connected peer's host name, if either the subject information for [CommonName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) doesn't define a valid host name, or the subject info name doesn't match the peer's host name.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCertificate::**subjectDisplayName**() const

Returns a name that describes the subject. It returns the [QSslCertificate::CommonName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) if available, otherwise falls back to the first [QSslCertificate::Organization](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) or the first [QSslCertificate::OrganizationalUnitName](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum).

This function was introduced in Qt 5.12.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### [QStringList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstringlist.html) QSslCertificate::**subjectInfo**([QSslCertificate::SubjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#SubjectInfo-enum) *subject*) const

Returns the information for the *subject*, or an empty list if there is no information for *subject* in the certificate. There can be more than one entry of each type.

**See also** [issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)().

---

### [QStringList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstringlist.html) QSslCertificate::**subjectInfo**(const [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) &*attribute*) const

Returns the subject information for *attribute*, or an empty list if there is no information for *attribute* in the certificate. There can be more than one entry for an attribute.

**See also** [issuerInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#issuerInfo)().

---

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)<[QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html)> QSslCertificate::**subjectInfoAttributes**() const

Returns a list of the attributes that have values in the subject information of this certificate. The information associated with a given attribute can be accessed using the [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)() method. Note that this list may include the OIDs for any elements that are not known by the SSL backend.

This function was introduced in Qt 5.0.

**See also** [subjectInfo](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectInfo)().

---

### void QSslCertificate::**swap**([QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) &*other*)

Swaps this certificate instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslCertificate::**toDer**() const

Returns this certificate converted to a DER (binary) encoded representation.

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslCertificate::**toPem**() const

Returns this certificate converted to a PEM (Base64) encoded representation.

---

### [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) QSslCertificate::**toText**() const

Returns this certificate converted to a human-readable text representation.

This function was introduced in Qt 5.0.

---

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> QSslCertificate::**verify**([QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate)\> *certificateChain*, const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*hostName* = QString())

Verifies a certificate chain. The chain to be verified is passed in the *certificateChain* parameter. The first certificate in the list should be the leaf certificate of the chain to be verified. If *hostName* is specified then the certificate is also checked to see if it is valid for the specified host name.

Note that the root (CA) certificate should not be included in the list to be verified, this will be looked up automatically either using the CA list specified by QSslSocket::defaultCaCertificates() or, if possible, it will be loaded on demand on Unix.

This function was introduced in Qt 5.0.

---

### [QByteArray](qthelp://org.qt-project.qtnetwork.5150/qtcore/qbytearray.html) QSslCertificate::**version**() const

Returns the certificate's version string.

---

### bool QSslCertificate::**operator!=**(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) &*other*) const

Returns `true` if this certificate is not the same as *other*; otherwise returns `false`.

---

### bool QSslCertificate::**operator==**(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#QSslCertificate) &*other*) const

Returns `true` if this certificate is the same as *other*; otherwise returns `false`.