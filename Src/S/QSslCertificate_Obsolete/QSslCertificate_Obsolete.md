[TOC]



# QSslCertificate Obsolete Members

以下的 [QSslCertificate](../QSslCertificate/QSslCertificate.md) 类成员都已过时。为了保证旧代码仍能运行，Qt 官方保留了这些过时的函数。但是 Qt 官方强烈建议不要在新的代码中使用它们。

## 公共成员函数

| 类型                                                        | 函数名                                                       |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| (obsolete) QMultiMap<QSsl::AlternateNameEntryType, QString> | **[alternateSubjectNames](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate-obsolete.html#alternateSubjectNames)**() const |
| (obsolete) bool                                             | **[isValid](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate-obsolete.html#isValid)**() const |



## 静态公共成员函数

| 类型                               | 函数名                                                       |
| ---------------------------------- | ------------------------------------------------------------ |
| (obsolete)QList\<QSslCertificate\> | **[fromPath](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate-obsolete.html#fromPath)**(const QString &*path*, QSsl::EncodingFormat *format*, QRegExp::PatternSyntax *syntax*) |



## 成员函数文档

### [QMultiMap](../../QMultiMap/QMultiMap.md)<[QSsl::AlternativeNameEntryType](../QSsl/QSsl.md#enum-qsslalternativenameentrytype), [QString](../../S/QString/QString.md)> QSslCertificate::**alternateSubjectNames**() const

该函数已经过时。为了保证旧代码仍能运行，Qt 官方保留了这个过时的函数。但是 Qt 官方强烈建议不要在新的代码中使用它。

请使用 [QSslCertificate::subjectAlternativeNames](#qmultimapqsslalternativenameentrytype-qstring-qsslcertificatesubjectalternativenames-const)() 函数。

### *[static]* [QList](../L/QList/QList.md)\<[QSslCertificate](../QSslCertificate/QSslCertificate.md)\> QSslCertificate::**fromPath**(const [QString](../../S/QString/QString.md) &*path*, [QSsl::EncodingFormat](../QSsl/QSsl.md#enum-qsslencodingformat) *format*, [QRegExp::PatternSyntax](qthelp://org.qt-project.qtnetwork.5150/qtcore/qregexp.html#PatternSyntax-enum) *syntax*)

该函数已经过时。为了保证旧代码仍能运行，Qt 官方保留了这个过时的函数。但是 Qt 官方强烈建议不要在新的代码中使用它。

搜索路径 *path* 中所有 *format* 编码格式的证书，并返回这些证书的列表。*path* 必须是一个文件，*syntax* 指定的正则表达式必须能检测到至少一个文件。

Qt 官方示例如下：

```cpp
 const auto certs = QSslCertificate::fromPath("C:/ssl/certificate.*.pem",
                                              QSsl::Pem, QRegExp::Wildcard);
 for (const QSslCertificate &cert : certs) {
     qDebug() << cert.issuerInfo(QSslCertificate::Organization);
 }
```

另外您也可以在 [fromData](#static-qlistqsslcertificate-qsslcertificatefromdataconst-qbytearray-data-qsslencodingformat-format--qsslpem)() 函数介绍中找到相关信息。

### bool QSslCertificate::**isValid**() const

该函数已经过时。为了保证旧代码仍能运行，Qt 官方保留了这个过时的函数。但是 Qt 官方强烈建议不要在新的代码中使用它。

验证证书的有效性请使用 [verify](../QSslCertificate/QSslCertificate.md#static-qlistqsslerror-qsslcertificateverifyqlistqsslcertificate-certificatechain-const-qstring-hostname--qstring)() 函数。查看证书是否被列入黑名单，请使用 [isBlacklisted](../QSslCertificate/QSslCertificate.md#bool-qsslcertificateisblacklisted-const)() 函数。检查证书是否已经过期或者是否尚未生效，请结合 [expiryDate](../QSslCertificate/QSslCertificate.md#qdatetime-qsslcertificateexpirydate-const)() 、[effectiveDate](../QSslCertificate/QSslCertificate.md#qdatetime-qsslcertificateeffectivedate-const)() 和 QDateTime::currentDateTime() 使用。

该函数检查当前日期是否处于证书的有效日期内以及是否被列入黑名单。

另外您也可以在 [isNull](../QSslCertificate/QSslCertificate.md#bool-qsslcertificateisnull-const)() ，[verify](../QSslCertificate/QSslCertificate.md#static-qlistqsslerror-qsslcertificateverifyqlistqsslcertificate-certificatechain-const-qstring-hostname--qstring)() ，[isBlacklisted](../QSslCertificate/QSslCertificate.md#bool-qsslcertificateisblacklisted-const)() ， [expiryDate](../QSslCertificate/QSslCertificate.md#qdatetime-qsslcertificateexpirydate-const)() 和 [effectiveDate](../QSslCertificate/QSslCertificate.md#qdatetime-qsslcertificateeffectivedate-const)() 函数介绍中找到相关信息。