[TOC]



# QSsl Namespace

QSsl 命名空间为所有的 SSL 类声明了通用的枚举类型。

| 属性     | 方法              |
| -------- | ----------------- |
| 头文件   | `#include <QSsl>` |
| qmake    | QT += network     |
| 引入版本 | Qt4.3             |

该命名空间最初在 Qt4.3 版本引入。

您可以在 [QSsl_Obsolete](../QSsl_Obsolete/QSsl_Obsolete.md) 找到过时的枚举类型。



## 类型

| 类型  | 属性                                                         |
| ----- | ------------------------------------------------------------ |
| enum  | **[AlternativeNameEntryType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#AlternativeNameEntryType-enum)** { EmailEntry, DnsEntry, IpAddressEntry } |
| enum  | **[EncodingFormat](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#EncodingFormat-enum)** { Pem, Der } |
| enum  | **[KeyAlgorithm](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyAlgorithm-enum)** { Rsa, Dsa, Ec, Dh, Opaque } |
| enum  | **[KeyType](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#KeyType-enum)** { PrivateKey, PublicKey } |
| enum  | **[SslOption](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslOption-enum)** { SslOptionDisableEmptyFragments, SslOptionDisableSessionTickets, SslOptionDisableCompression, SslOptionDisableServerNameIndication, SslOptionDisableLegacyRenegotiation, …, SslOptionDisableServerCipherPreference } |
| flags | **[SslOptions](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslOption-enum)** |
| enum  | **[SslProtocol](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qssl.html#SslProtocol-enum)** { SslV3, SslV2, TlsV1_0, TlsV1_0OrLater, TlsV1, …, SecureProtocols } |



## 详细介绍

无。



## 类型文档

### enum **QSsl**::AlternativeNameEntryType

Describes the key types for alternative name entries in [QSslCertificate](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html).

| Constant             | Value | Description                                                  |
| :------------------- | :---- | :----------------------------------------------------------- |
| QSsl::EmailEntry     | 0     | An email entry; the entry contains an email address that the certificate is valid for. |
| QSsl::DnsEntry       | 1     | A DNS host name entry; the entry contains a host name entry that the certificate is valid for. The entry may contain wildcards. |
| QSsl::IpAddressEntry | 2     | An IP address entry; the entry contains an IP address entry that the certificate is valid for, introduced in Qt 5.13. |

**Note:** In Qt 4, this enum was called `AlternateNameEntryType`. That name is deprecated in Qt 5.

**See also** [QSslCertificate::subjectAlternativeNames](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectAlternativeNames)().



### enum **QSsl**::EncodingFormat

Describes supported encoding formats for certificates and keys.

| Constant  | Value | Description     |
| :-------- | :---- | :-------------- |
| QSsl::Pem | 0     | The PEM format. |
| QSsl::Der | 1     | The DER format. |



### enum **QSsl**::KeyAlgorithm

Describes the different key algorithms supported by [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html).

| Constant     | Value | Description                                                  |
| :----------- | :---- | :----------------------------------------------------------- |
| QSsl::Rsa    | 1     | The RSA algorithm.                                           |
| QSsl::Dsa    | 2     | The DSA algorithm.                                           |
| QSsl::Ec     | 3     | The Elliptic Curve algorithm.                                |
| QSsl::Dh     | 4     | The Diffie-Hellman algorithm.                                |
| QSsl::Opaque | 0     | A key that should be treated as a 'black box' by [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html). |

The opaque key facility allows applications to add support for facilities such as PKCS#11 that Qt does not currently offer natively.



### enum **QSsl**::KeyType

Describes the two types of keys [QSslKey](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslkey.html) supports.

| Constant         | Value | Description    |
| :--------------- | :---- | :------------- |
| QSsl::PrivateKey | 0     | A private key. |
| QSsl::PublicKey  | 1     | A public key.  |



### enum **QSsl**::SslOption flags **QSsl**::SslOptions

Describes the options that can be used to control the details of SSL behaviour. These options are generally used to turn features off to work around buggy servers.

| Constant                                     | Value | Description                                                  |
| :------------------------------------------- | :---- | :----------------------------------------------------------- |
| QSsl::SslOptionDisableEmptyFragments         | 0x01  | Disables the insertion of empty fragments into the data when using block ciphers. When enabled, this prevents some attacks (such as the BEAST attack), however it is incompatible with some servers. |
| QSsl::SslOptionDisableSessionTickets         | 0x02  | Disables the SSL session ticket extension. This can cause slower connection setup, however some servers are not compatible with the extension. |
| QSsl::SslOptionDisableCompression            | 0x04  | Disables the SSL compression extension. When enabled, this allows the data being passed over SSL to be compressed, however some servers are not compatible with this extension. |
| QSsl::SslOptionDisableServerNameIndication   | 0x08  | Disables the SSL server name indication extension. When enabled, this tells the server the virtual host being accessed allowing it to respond with the correct certificate. |
| QSsl::SslOptionDisableLegacyRenegotiation    | 0x10  | Disables the older insecure mechanism for renegotiating the connection parameters. When enabled, this option can allow connections for legacy servers, but it introduces the possibility that an attacker could inject plaintext into the SSL session. |
| QSsl::SslOptionDisableSessionSharing         | 0x20  | Disables SSL session sharing via the session ID handshake attribute. |
| QSsl::SslOptionDisableSessionPersistence     | 0x40  | Disables storing the SSL session in ASN.1 format as returned by [QSslConfiguration::sessionTicket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#sessionTicket)(). Enabling this feature adds memory overhead of approximately 1K per used session ticket. |
| QSsl::SslOptionDisableServerCipherPreference | 0x80  | Disables selecting the cipher chosen based on the servers preferences rather than the order ciphers were sent by the client. This option is only relevant to server sockets, and is only honored by the OpenSSL backend. |

By default, SslOptionDisableEmptyFragments is turned on since this causes problems with a large number of servers. SslOptionDisableLegacyRenegotiation is also turned on, since it introduces a security risk. SslOptionDisableCompression is turned on to prevent the attack publicised by CRIME. SslOptionDisableSessionPersistence is turned on to optimize memory usage. The other options are turned off.

**Note:** Availability of above options depends on the version of the SSL backend in use.

The SslOptions type is a typedef for [QFlags](qthelp://org.qt-project.qtnetwork.5150/qtcore/qflags.html)<SslOption>. It stores an OR combination of SslOption values.



### enum **QSsl**::SslProtocol

Describes the protocol of the cipher.

| Constant              | Value           | Description                                                  |
| :-------------------- | :-------------- | :----------------------------------------------------------- |
| QSsl::SslV3           | 0               | SSLv3; not supported by [QSslSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html). |
| QSsl::SslV2           | 1               | SSLv2; not supported by [QSslSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html). |
| QSsl::TlsV1_0         | 2               | TLSv1.0                                                      |
| QSsl::TlsV1_0OrLater  | 8               | TLSv1.0 and later versions. This option is not available when using the WinRT backend due to platform limitations. |
| QSsl::TlsV1           | TlsV1_0         | Obsolete, means the same as TlsV1_0                          |
| QSsl::TlsV1_1         | 3               | TLSv1.1. When using the WinRT backend this option will also enable TLSv1.0. |
| QSsl::TlsV1_1OrLater  | 9               | TLSv1.1 and later versions. This option is not available when using the WinRT backend due to platform limitations. |
| QSsl::TlsV1_2         | 4               | TLSv1.2. When using the WinRT backend this option will also enable TLSv1.0 and TLSv1.1. |
| QSsl::TlsV1_2OrLater  | 10              | TLSv1.2 and later versions. This option is not available when using the WinRT backend due to platform limitations. |
| QSsl::DtlsV1_0        | 11              | DTLSv1.0                                                     |
| QSsl::DtlsV1_0OrLater | 12              | DTLSv1.0 and later versions.                                 |
| QSsl::DtlsV1_2        | 13              | DTLSv1.2                                                     |
| QSsl::DtlsV1_2OrLater | 14              | DTLSv1.2 and later versions.                                 |
| QSsl::TlsV1_3         | 15              | TLSv1.3. (Since Qt 5.12)                                     |
| QSsl::TlsV1_3OrLater  | 16              | TLSv1.3 and later versions. (Since Qt 5.12)                  |
| QSsl::UnknownProtocol | -1              | The cipher's protocol cannot be determined.                  |
| QSsl::AnyProtocol     | 5               | Any supported protocol. This value is used by [QSslSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslsocket.html) only. |
| QSsl::TlsV1SslV3      | 6               | Same as TlsV1_0. This enumerator is deprecated, use TlsV1_0 instead. |
| QSsl::SecureProtocols | AnyProtocol + 2 | The default option, using protocols known to be secure.      |