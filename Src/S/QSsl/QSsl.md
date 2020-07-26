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
| enum  | **[AlternativeNameEntryType](#enum-qsslalternativenameentrytype)** { EmailEntry, DnsEntry, IpAddressEntry } |
| enum  | **[EncodingFormat](#enum-qsslencodingformat)** { Pem, Der }  |
| enum  | **[KeyAlgorithm](#enum-qsslkeyalgorithm)** { Rsa, Dsa, Ec, Dh, Opaque } |
| enum  | **[KeyType](#enum-qsslkeytype)** { PrivateKey, PublicKey }   |
| enum  | **[SslOption](h#enum-qsslssloption-flags-qsslssloptions)** { SslOptionDisableEmptyFragments, SslOptionDisableSessionTickets, SslOptionDisableCompression, SslOptionDisableServerNameIndication, SslOptionDisableLegacyRenegotiation, …, SslOptionDisableServerCipherPreference } |
| flags | **[SslOptions](#enum-qsslssloption-flags-qsslssloptions)**   |
| enum  | **[SslProtocol](#enum-qsslsslprotocol)** { SslV3, SslV2, TlsV1_0, TlsV1_0OrLater, TlsV1, …, SecureProtocols } |



## 详细介绍

无。



## 类型文档

### enum QSsl::**AlternativeNameEntryType**

描述 [QSslCertificate](../QSslCertificate/QSslCertificate.md) 中条目的可替代名称的键类型。

| 常量                 | 值   | 描述                                                         |
| :------------------- | :--- | :----------------------------------------------------------- |
| QSsl::EmailEntry     | 0    | 电子邮件条目。该条目中包含证书有效的电子邮件地址。           |
| QSsl::DnsEntry       | 1    | DNS 主机名条目。 该条目包含证书有效的主机名条目。 该条目也可能包含通配符。 |
| QSsl::IpAddressEntry | 2    | IP 地址条目。 该条目包含 Qt 5.13 中引入的证书有效的IP地址条目。 |

**注意：** 在 Qt 4中，这个枚举被叫做 `AlternateNameEntryType`。 这个名称在 Qt 5 中已不被推荐使用。

另外您也可以在 [QSslCertificate::subjectAlternativeNames](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslcertificate.html#subjectAlternativeNames)() 函数介绍中找到相关信息。

---

### enum QSsl::**EncodingFormat**

描述证书和密钥支持的编码类型。

| 常量      | 值   | 描述     |
| :-------- | :--- | :------- |
| QSsl::Pem | 0    | PEM 格式 |
| QSsl::Der | 1    | DER 格式 |

---

### enum QSsl::**KeyAlgorithm**

描述了 [QSslKey](../QSslKey/QSslKey.md) 支持的不同的密钥加密算法。

| 常量         | 值   | 描述                                                   |
| :----------- | :--- | :----------------------------------------------------- |
| QSsl::Rsa    | 1    | RSA 算法。                                             |
| QSsl::Dsa    | 2    | DSA 算法。                                             |
| QSsl::Ec     | 3    | 椭圆曲线算法。                                         |
| QSsl::Dh     | 4    | Diffie-Hellman算法。                                   |
| QSsl::Opaque | 0    | 密钥将被 [QSslKey](../QSslKey/QSslKey.md) 作为黑匣子。 |

不透明的密钥功能（ QSsl::Opaque ）允许应用程序添加对 Qt 当前不提供的功能（例如 PKCS＃11 ）的支持。

---

### enum QSsl::**KeyType**

描述了 [QSslKey](../QSslKey/QSslKey.md) 支持的两种密钥类型。

| 常量             | 值   | 描述 |
| :--------------- | :--- | :--- |
| QSsl::PrivateKey | 0    | 私钥 |
| QSsl::PublicKey  | 1    | 公钥 |

---

### enum QSsl::**SslOption** flags QSsl::**SslOptions**

描述可用于控制 SSL 详细行为的选项。 这些选项通常用于关闭功能以解决有问题的服务器。

| 常量                                         | 值   | 描述                                                         |
| :------------------------------------------- | :--- | :----------------------------------------------------------- |
| QSsl::SslOptionDisableEmptyFragments         | 0x01 | 使用分组密码时，禁止将空片段插入数据中。 启用该选项后，这可以防止某些攻击（例如 BEAST 攻击），但是与某些服务器不兼容。 |
| QSsl::SslOptionDisableSessionTickets         | 0x02 | 禁用 SSL 会话票证扩展。 这可能会导致连接设置变慢，但是某些服务器不兼容该扩展。 |
| QSsl::SslOptionDisableCompression            | 0x04 | 禁用 SSL 压缩扩展。 启用该功能后，这将允许压缩通过 SSL 传递的数据，但是某些服务器与此扩展不兼容。 |
| QSsl::SslOptionDisableServerNameIndication   | 0x08 | 禁用SSL服务器名称指示扩展名。 启用后，它会告知服务器正在访问的虚拟主机，从而使其可以使用正确的证书进行响应。 |
| QSsl::SslOptionDisableLegacyRenegotiation    | 0x10 | 禁用用于重新协商连接参数的较旧的不安全机制。 启用后，此选项可以允许旧服务器连接，但是它带来了攻击者可能将纯文本注入 SSL 会话的可能性。 |
| QSsl::SslOptionDisableSessionSharing         | 0x20 | 通过会话 ID 握手属性禁用 SSL 会话共享。                      |
| QSsl::SslOptionDisableSessionPersistence     | 0x40 | 禁用以 [QSslConfiguration::sessionTicket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsslconfiguration.html#sessionTicket)() 返回的 ASN.1 格式存储 SSL 会话。 启用此功能会为每个使用的会话票证增加大约1K的内存开销。 |
| QSsl::SslOptionDisableServerCipherPreference | 0x80 | 禁用基于服务器首选项而非客户端发送的顺序密码来选择所选密码的功能。 此选项仅与服务器套接字相关，并且仅由 OpenSSL 后端使用。 |

默认情况下，SslOptionDisableEmptyFragments 选项处于启用状态，因为这会导致大量服务器出现问题。 SslOptionDisableLegacyRenegotiation 选项也处于启用状态，因为它带来了安全风险。 启用 SslOptionDisableCompression 可以防止 CRIME 公开攻击。  SslOptionDisableSessionPersistence 也处于启用状态以优化内存使用。 其他选项处于关闭状态。

**注意：** 以上选项的可用性取决于所使用的 SSL 后端的版本。

SslOptions 类型是由 typedef [QFlags](qthelp://org.qt-project.qtnetwork.5150/qtcore/qflags.html)\<SslOption\>  定义的用户自定义类型。它储存着  SslOption 值的OR组合。

---

### enum QSsl::**SslProtocol**

描述密码的协议。

| 常量                  | 值              | 描述                                                         |
| :-------------------- | :-------------- | :----------------------------------------------------------- |
| QSsl::SslV3           | 0               | SSLv3。不被 [QSslSocket](../QSslSocket/QSslSocket.md) 支持。 |
| QSsl::SslV2           | 1               | SSLv2。不被 [QSslSocket](../QSslSocket/QSslSocket.md) 支持。 |
| QSsl::TlsV1_0         | 2               | TLSv1.0。                                                    |
| QSsl::TlsV1_0OrLater  | 8               | TLSv1.0 和之后的版本。由于平台限制，在使用 WinRT 后端时，此选项不可用。 |
| QSsl::TlsV1           | TlsV1_0         | 已过时，与 TlsV1_0 意义相同。                                |
| QSsl::TlsV1_1         | 3               | TLSv1.1。当使用WinRT 后端时，这个选项也会启用 TLSv1.0 选项。 |
| QSsl::TlsV1_1OrLater  | 9               | TLSv1.1 和之后的版本。由于平台限制，在使用 WinRT 后端时，此选项不可用。 |
| QSsl::TlsV1_2         | 4               | TLSv1.2。当使用WinRT 后端时，这个选项也会启用 TLSv1.0 和 TLSv1.1 选项。 |
| QSsl::TlsV1_2OrLater  | 10              | TLSv1.2 和之后的版本。由于平台限制，在使用 WinRT 后端时，此选项不可用。 |
| QSsl::DtlsV1_0        | 11              | DTLSv1.0。                                                   |
| QSsl::DtlsV1_0OrLater | 12              | DTLSv1.0 和之后的版本。                                      |
| QSsl::DtlsV1_2        | 13              | DTLSv1.2。                                                   |
| QSsl::DtlsV1_2OrLater | 14              | DTLSv1.2 和之后的版本。                                      |
| QSsl::TlsV1_3         | 15              | TLSv1.3。（在 Qt 5.12 版本引入）                             |
| QSsl::TlsV1_3OrLater  | 16              | TLSv1.3 和之后的版本。（在 Qt 5.12 版本引入）                |
| QSsl::UnknownProtocol | -1              | 不能甄别密码的协议。                                         |
| QSsl::AnyProtocol     | 5               | 任何支持的协议。 该选项仅被 [QSslSocket](../QSslSocket/QSslSocket.md)  使用。 |
| QSsl::TlsV1SslV3      | 6               | 与 TlsV1_0 相同。 该枚举成员已不被推荐使用，您应该使用 TlsV1_0 来替代。 |
| QSsl::SecureProtocols | AnyProtocol + 2 | 默认选项，使用已知是安全的协议。                             |
