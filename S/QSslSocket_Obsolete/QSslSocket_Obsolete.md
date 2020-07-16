[TOC]



# Obsolete Members for QSslSocket

这里是 QSslSocket 类中已过时的成员函数。为了保证旧代码仍能运行，Qt 官方保留了这些过时的函数。但是 Qt 官方强烈建议不要在新的代码中使用它们。



## 公共成员函数

| 类型                                  | 函数名                                                       |
| ------------------------------------- | ------------------------------------------------------------ |
| *(obsolete)* void                     | **[addCaCertificate](#void-qsslsocketaddcacertificateconst-qsslcertificate-certificate)**(const QSslCertificate &*certificate*) |
| *(obsolete)* bool                     | **[addCaCertificates](#bool-qsslsocketaddcacertificatesconst-qstring-path-qsslencodingformat-format--qsslpem-qregexppatternsyntax-syntax--qregexpfixedstring)**(const QString &*path*, QSsl::EncodingFormat *format* = QSsl::Pem, QRegExp::PatternSyntax *syntax* = QRegExp::FixedString) |
| *(obsolete)* void                     | **[addCaCertificates](#void-qsslsocketaddcacertificatesconst-qlistqsslcertificate-certificates)**(const QList<\QSslCertificate\> &*certificates*) |
| *(obsolete)* QList\<QSslCertificate\> | **[caCertificates](#qlistqsslcertificate-qsslsocketcacertificates-const)**() const |
| *(obsolete)* QList\<QSslCipher\>      | **[ciphers](#qlistqsslcipher-qsslsocketciphers-const)**() const |
| *(obsolete)* void                     | **[setCaCertificates](#void-qsslsocketsetcacertificatesconst-qlistqsslcertificate-certificates)**(const QList\<QSslCertificate\> &*certificates*) |
| *(obsolete)* void                     | **[setCiphers](#void-qsslsocketsetciphersconst-qlistqsslcipher-ciphers)**(const QList\<QSslCipher\> &*ciphers*) |
| *(obsolete)* void                     | **[setCiphers](#void-qsslsocketsetciphersconst-qstring-ciphers)**(const QString &*ciphers*) |
| *(obsolete)* QList\<QSslError\>       | **[sslErrors](#qlistqsslerror-qsslsocketsslerrors-const)**() const |



## 静态公共成员函数

| 类型                                  | 函数名                                                       |
| ------------------------------------- | ------------------------------------------------------------ |
| *(obsolete)* void                     | **[addDefaultCaCertificate](#static-void-qsslsocketadddefaultcacertificateconst-qsslcertificate-certificate)**(const QSslCertificate &*certificate*) |
| *(obsolete)* bool                     | **[addDefaultCaCertificates](#static-bool-qsslsocketadddefaultcacertificatesconst-qstring-path-qsslencodingformat-encoding--qsslpem-qregexppatternsyntax-syntax--qregexpfixedstring)**(const QString &*path*, QSsl::EncodingFormat *encoding* = QSsl::Pem, QRegExp::PatternSyntax *syntax* = QRegExp::FixedString) |
| *(obsolete)* void                     | **[addDefaultCaCertificates](#static-void-qsslsocketadddefaultcacertificatesconst-qlistqsslcertificate-certificates)**(const QList\<QSslCertificate\> &*certificates*) |
| *(obsolete)* QList\<QSslCertificate\> | **[defaultCaCertificates](#static-qlistqsslcertificate-qsslsocketdefaultcacertificates)**() |
| *(obsolete)* QList\<QSslCipher\>      | **[defaultCiphers](#static-qlistqsslcipher-qsslsocketdefaultciphers)**() |
| *(obsolete)* void                     | **[setDefaultCaCertificates](#static-void-qsslsocketsetdefaultcacertificatesconst-qlistqsslcertificate-certificates)**(const QList\<QSslCertificate\> &*certificates*) |
| *(obsolete)* void                     | **[setDefaultCiphers](#static-void-qsslsocketsetdefaultciphersconst-qlistqsslcipher-ciphers)**(const QList\<QSslCipher\> &*ciphers*) |
| *(obsolete)* QList\<QSslCipher\>      | **[supportedCiphers](#static-qlistqsslcipher-qsslsocketsupportedciphers)**() |
| *(obsolete)* QList\<QSslCertificate\> | **[systemCaCertificates](#static-qlistqsslcertificate-qsslsocketsystemcacertificates)**() |



## 成员函数文档

### void **QSslSocket**::addCaCertificate(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)() instead.

Adds the *certificate* to this socket's CA certificate database. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

To add multiple certificates, use [addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificates)().

**See also** [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)() and [QSslConfiguration::setCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCaCertificates)().

### bool **QSslSocket**::addCaCertificates(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*path*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *format* = QSsl::Pem, [QRegExp::PatternSyntax](qthelp://org.qt-project.qtnetwork.5150/qtcore/qregexp.html#PatternSyntax-enum) *syntax* = QRegExp::FixedString)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)() instead.

Searches all files in the *path* for certificates encoded in the specified *format* and adds them to this socket's CA certificate database. *path* must be a file or a pattern matching one or more files, as specified by *syntax*. Returns `true` if one or more certificates are added to the socket's CA certificate database; otherwise returns `false`.

The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

For more precise control, use [addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificate)().

**See also** [addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificate)() and [QSslCertificate::fromPath](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate-obsolete.html#fromPath)().

### void **QSslSocket**::addCaCertificates(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)> &*certificates*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)() instead.

Adds the *certificates* to this socket's CA certificate database. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

For more precise control, use [addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificate)().

**See also** [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)() and [addDefaultCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addDefaultCaCertificate)().

### *[static]* void **QSslSocket**::addDefaultCaCertificate(const [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html) &*certificate*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Adds *certificate* to the default CA certificate database. Each SSL socket's CA certificate database is initialized to the default CA certificate database.

**See also** [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)().

### *[static]* bool **QSslSocket**::addDefaultCaCertificates(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*path*, [QSsl::EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum) *encoding* = QSsl::Pem, [QRegExp::PatternSyntax](qthelp://org.qt-project.qtnetwork.5150/qtcore/qregexp.html#PatternSyntax-enum) *syntax* = QRegExp::FixedString)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Searches all files in the *path* for certificates with the specified *encoding* and adds them to the default CA certificate database. *path* can be an explicit file, or it can contain wildcards in the format specified by *syntax*. Returns `true` if any CA certificates are added to the default database.

Each SSL socket's CA certificate database is initialized to the default CA certificate database.

**See also** [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)(), [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)(), and [QSslConfiguration::addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificate)().

### *[static]* void **QSslSocket**::addDefaultCaCertificates(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> &*certificates*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Adds *certificates* to the default CA certificate database. Each SSL socket's CA certificate database is initialized to the default CA certificate database.

**See also** [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)() and [QSslConfiguration::addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#addCaCertificates)().

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::caCertificates() const

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)() instead.

Returns this socket's CA certificate database. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate. It can be moodified prior to the handshake with [addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificate)(), [addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificates)(), and [setCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCaCertificates)().

**Note:** On Unix, this method may return an empty list if the root certificates are loaded on demand.

**See also** [addCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificate)(), [addCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addCaCertificates)(), and [setCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCaCertificates)().

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html)\> **QSslSocket**::ciphers() const

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::ciphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#ciphers)() instead.

Returns this socket's current cryptographic cipher suite. This list is used during the socket's handshake phase for choosing a session cipher. The returned list of ciphers is ordered by descending preference. (i.e., the first cipher in the list is the most preferred cipher). The session cipher will be the first one in the list that is also supported by the peer.

By default, the handshake phase can choose any of the ciphers supported by this system's SSL libraries, which may vary from system to system. The list of ciphers supported by this system's SSL libraries is returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)(). You can restrict the list of ciphers used for choosing the session cipher for this socket by calling [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)() with a subset of the supported ciphers. You can revert to using the entire set by calling [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)() with the list returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

You can restrict the list of ciphers used for choosing the session cipher for *all* sockets by calling [setDefaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCiphers)() with a subset of the supported ciphers. You can revert to using the entire set by calling [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)() with the list returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

**See also** [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)(), [defaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCiphers)(), [setDefaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCiphers)(), and [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::defaultCaCertificates()

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#caCertificates)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Returns the current default CA certificate database. This database is originally set to your system's default CA certificate database. If no system default database is found, an empty database will be returned. You can override the default CA certificate database with your own CA certificate database using [setDefaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCaCertificates)().

Each SSL socket's CA certificate database is initialized to the default CA certificate database.

**Note:** On Unix, this method may return an empty list if the root certificates are loaded on demand.

**See also** [setDefaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCaCertificates)() and [caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#caCertificates)().

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html)\> **QSslSocket**::defaultCiphers()

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::ciphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#ciphers)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Returns the default cryptographic cipher suite for all sockets in this application. This list is used during the socket's handshake phase when negotiating with the peer to choose a session cipher. The list is ordered by preference (i.e., the first cipher in the list is the most preferred cipher).

By default, the handshake phase can choose any of the ciphers supported by this system's SSL libraries, which may vary from system to system. The list of ciphers supported by this system's SSL libraries is returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

**See also** [setDefaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCiphers)() and [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

### void **QSslSocket**::setCaCertificates(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> &*certificates*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::setCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCaCertificates)() instead.

Sets this socket's CA certificate database to be *certificates*. The certificate database must be set prior to the SSL handshake. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

The CA certificate database can be reset to the current default CA certificate database by calling this function with the list of CA certificates returned by [defaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCaCertificates)().

**See also** [caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#caCertificates)() and [defaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCaCertificates)().

### void **QSslSocket**::setCiphers(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html)\> &*ciphers*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

USe [QSslConfiguration::setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() instead.

Sets the cryptographic cipher suite for this socket to *ciphers*, which must contain a subset of the ciphers in the list returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

Restricting the cipher suite must be done before the handshake phase, where the session cipher is chosen.

**See also** [ciphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#ciphers)(), [setDefaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCiphers)(), and [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

### void **QSslSocket**::setCiphers(const [QString](qthelp://org.qt-project.qtnetwork.5150/qtcore/qstring.html) &*ciphers*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() instead.

Sets the cryptographic cipher suite for this socket to *ciphers*, which is a colon-separated list of cipher suite names. The ciphers are listed in order of preference, starting with the most preferred cipher. For example:

```
 QSslSocket socket;
 socket.setCiphers("DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:AES256-SHA");
```

Each cipher name in *ciphers* must be the name of a cipher in the list returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)(). Restricting the cipher suite must be done before the handshake phase, where the session cipher is chosen.

**See also** [ciphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#ciphers)(), [setDefaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCiphers)(), and [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

### *[static]* void **QSslSocket**::setDefaultCaCertificates(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> &*certificates*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::setCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCaCertificates)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Sets the default CA certificate database to *certificates*. The default CA certificate database is originally set to your system's default CA certificate database. You can override the default CA certificate database with your own CA certificate database using this function.

Each SSL socket's CA certificate database is initialized to the default CA certificate database.

**See also** [defaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCaCertificates)() and [addDefaultCaCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#addDefaultCaCertificate)().

### *[static]* void **QSslSocket**::setDefaultCiphers(const [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html)\> &*ciphers*)

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#setCiphers)() on the default [QSslConfiguration](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html) instead.

Sets the default cryptographic cipher suite for all sockets in this application to *ciphers*, which must contain a subset of the ciphers in the list returned by [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

Restricting the default cipher suite only affects SSL sockets that perform their handshake phase after the default cipher suite has been changed.

**See also** [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)(), [defaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCiphers)(), and [supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#supportedCiphers)().

### [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslError](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslerror.html)\> **QSslSocket**::sslErrors() const

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [sslHandshakeErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslHandshakeErrors)() instead.

Returns a list of the last SSL errors that occurred. This is the same list as [QSslSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html) passes via the sslErrors() signal. If the connection has been encrypted with no errors, this function will return an empty list.

**See also** [connectToHostEncrypted](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#connectToHostEncrypted)() and [sslHandshakeErrors](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html#sslHandshakeErrors)().

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCipher](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcipher.html)\> **QSslSocket**::supportedCiphers()

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use [QSslConfiguration::supportedCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#supportedCiphers)() instead.

Returns the list of cryptographic ciphers supported by this system. This list is set by the system's SSL libraries and may vary from system to system.

**See also** [defaultCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCiphers)(), [ciphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#ciphers)(), and [setCiphers](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setCiphers)().

### *[static]* [QList](qthelp://org.qt-project.qtnetwork.5150/qtcore/qlist.html)\<[QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html)\> **QSslSocket**::systemCaCertificates()

This function is obsolete. It is provided to keep old source code working. We strongly advise against using it in new code.

Use QSslConfiguration::systemDefaultCaCertificates instead.

This function provides the CA certificate database provided by the operating system. The CA certificate database returned by this function is used to initialize the database returned by [defaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCaCertificates)(). You can replace that database with your own with [setDefaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCaCertificates)().

**Note:** : On OS X, only certificates that are either trusted for all purposes or trusted for the purpose of SSL in the keychain will be returned.

**See also** [caCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#caCertificates)(), [defaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#defaultCaCertificates)(), and [setDefaultCaCertificates](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket-obsolete.html#setDefaultCaCertificates)().