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

Searches all files in the *path* for certificates encoded in the specified *format* and returns them in a list. *path* must be a file or a pattern matching one or more files, as specified by *syntax*.

Example:

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

To verify a certificate, use [verify](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#verify)(). To check if a certificate is blacklisted, use [isBlacklisted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isBlacklisted)(). To check if a certificate has expired or is not yet valid, compare [expiryDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#expiryDate)() and [effectiveDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#effectiveDate)() with [QDateTime::currentDateTime](qthelp://org.qt-project.qtnetwork.5150/qtcore/qdatetime.html#currentDateTime)()

This function checks that the current date-time is within the date-time range during which the certificate is considered valid, and checks that the certificate is not in a blacklist of fraudulent certificates.

**See also** [isNull](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isNull)(), [verify](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#verify)(), [isBlacklisted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#isBlacklisted)(), [expiryDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#expiryDate)(), and [effectiveDate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#effectiveDate)().