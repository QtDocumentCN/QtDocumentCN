[TOC]



# QUdpSocket Class

QUdpSocket 类提供了 UDP 类型的套接字。

| 属性   | 方法                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | \#include <QUdpSocket>                                       |
| qmake  | QT += network                                                |
| 基类   | [QAbstractSocket](../../A/QAbstractSocket/QAbstractSocket.md) |

​    **注意：** 该类提供的所有函数都是可重入的。



## 公共成员函数

| 类型              | 函数名                                                       |
| ----------------- | ------------------------------------------------------------ |
|                   | QUdpSocket(QObject **parent* = nullptr)                      |
| virtual           | ~QUdpSocket()                                                |
| bool              | hasPendingDatagrams() const                                  |
| bool              | joinMulticastGroup(const QHostAddress &*groupAddress*)       |
| bool              | joinMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*) |
| bool              | leaveMulticastGroup(const QHostAddress &*groupAddress*)      |
| bool              | leaveMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*) |
| QNetworkInterface | multicastInterface() const                                   |
| qint64            | pendingDatagramSize() const                                  |
| qint64            | readDatagram(char \**data*, qint64 *maxSize*, QHostAddress \**address* = nullptr, quint16 \**port* = nullptr) |
| QNetworkDatagram  | receiveDatagram(qint64 *maxSize* = -1)                       |
| void              | setMulticastInterface(const QNetworkInterface &*iface*)      |
| qint64            | writeDatagram(const char **data*, qint64 *size*, const QHostAddress &*address*, quint16 *port*) |
| qint64            | writeDatagram(const QNetworkDatagram &*datagram*)            |
| qint64            | writeDatagram(const QByteArray &*datagram*, const QHostAddress &*host*, quint16 *port*) |



## 详细描述





## 成员函数文档

### **QUdpSocket**::QUdpSocket(QObject **parent* = nullptr)



### *[virtual]* **QUdpSocket**::~QUdpSocket()



### bool **QUdpSocket**::hasPendingDatagrams() const



### bool **QUdpSocket**::joinMulticastGroup(const QHostAddress &*groupAddress*)



### bool **QUdpSocket**::joinMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)



### bool **QUdpSocket**::leaveMulticastGroup(const QHostAddress &*groupAddress*)



### bool **QUdpSocket**::leaveMulticastGroup(const QHostAddress &*groupAddress*, const QNetworkInterface &*iface*)



### QNetworkInterface **QUdpSocket**::multicastInterface() const



### qint64 **QUdpSocket**::pendingDatagramSize() const



### qint64 **QUdpSocket**::readDatagram(char \**data*, qint64 *maxSize*, QHostAddress \**address* = nullptr, quint16 \**port* = nullptr)



### QNetworkDatagram **QUdpSocket**::receiveDatagram(qint64 *maxSize* = -1)



### void **QUdpSocket**::setMulticastInterface(const QNetworkInterface &*iface*)



### qint64 **QUdpSocket**::writeDatagram(const char **data*, qint64 *size*, const QHostAddress &*address*, quint16 *port*)



### qint64 **QUdpSocket**::writeDatagram(const QNetworkDatagram &*datagram*)



### qint64 QUdpSocket::writeDatagram(const QByteArray &*datagram*, const QHostAddress &*host*, quint16 *port*)