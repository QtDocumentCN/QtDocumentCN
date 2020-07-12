[TOC]



# QTcpSocket Class

QTcpSocket 提供了一个 TCP 类型的套接字。

| 属性   | 方法                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | \#include <QTcpSocket>                                       |
| qmake  | QT += network                                                |
| 父类   | [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) |
| 子类   | QSctpSocket 和 QSslSocket                                    |

**注意：** QTcpSocket类中所有的函数都是可重入函数。



## 公共函数

| 类型    | 函数名                                                       |
| ------- | ------------------------------------------------------------ |
|         | [QTcpSocket(QObject **parent* = nullptr)](#qtcpsocketqtcpsocketqobject-parent--nullptr) |
| virtual | [~QTcpSocket()](#virtual-qtcpsocketqtcpsocket)               |



## 详细描述

TCP（传输控制协议）是一种可靠的，面向流，面向连接的传输协议。 它特别适合连续数据传输。

​    QTcpSocket 是继承自 QAbstractSocket 的一个便利子类，它允许您建立 TCP 连接并传输数据流。您可以阅读 [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) 文档获取详细信息。

​    **注意：** 无法在 *QIODevice::Unbuffered* 模式下打开 TCP 套接字。

​    您也可以在 QTcpServer, QUdpSocket 和 QNetworkAccessManager 类文档以及 Fortune Server Example, Fortune Client Example, Threaded Fortune Server Example, Blocking Fortune Client Example, Loopback Example 和 Torrent Example 示例文档中找到相关信息。



## 成员函数文档

### **QTcpSocket**::QTcpSocket(QObject **parent* = nullptr)

构造函数。创建一个 QTcpSocket 类型的对象。该对象创建后初始状态为*未连接*（ *UnconnectedState* ）状态。

​    函数中父对象参数 *parent* 传递给 QObject 的构造函数。

​    另外您也可以在 [socketType()](../../A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const) 函数介绍中找到相关信息。

### *[virtual]* QTcpSocket::~QTcpSocket()

析构函数。销毁套接字，必要时关闭连接。

​    另外您也可以在 [close()](../../A/QAbstractSocket/QAbstractSocket.md#override-virtual-void-qabstractsocketclose) 函数介绍中找到相关信息。