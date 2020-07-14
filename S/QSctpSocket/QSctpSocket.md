[TOC]



# QSctpSocket Class

QSctpSocket 类提供了一个 SCTP 类型的套接字。

| 属性   | 方法                                           |
| ------ | ---------------------------------------------- |
| 头文件 | #include\<QSctpSocket\>                        |
| qmake  | QT += network                                  |
| 引入   | Qt5.8                                          |
| 父类   | [QTcpSocket](../../T/QTcpSocket/QTcpSocket.md) |

该类最初在Qt5.8版本引入。



## 公共成员函数

| 类型             | 函数名                                                       |
| ---------------- | ------------------------------------------------------------ |
|                  | **[ QSctpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#QSctpSocket)**(QObject **parent* = nullptr) |
| virtual          | **[~QSctpSocket](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#dtor.QSctpSocket)**() |
| bool             | **[isInDatagramMode](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#isInDatagramMode)**() const |
| int              | **[maximumChannelCount](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#maximumChannelCount)**() const |
| QNetworkDatagram | **[readDatagram](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#readDatagram)**() |
| void             | **[setMaximumChannelCount](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#setMaximumChannelCount)**(int *count*) |
| bool             | **[writeDatagram](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#writeDatagram)**(const QNetworkDatagram &*datagram*) |



## 重写公共成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | **[close](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#close)**() override |
| virtual void | **[disconnectFromHost](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#disconnectFromHost)**() override |



## 重写保护成员函数

| 类型           | 函数名                                                       |
| -------------- | ------------------------------------------------------------ |
| virtual qint64 | **[readData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#readData)**(char **data*, qint64 *maxSize*) override |
| virtual qint64 | **[readLineData](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpsocket.html#readLineData)**(char **data*, qint64 *maxlen*) override |



## 详细介绍





## 成员函数文档

### **QSctpSocket**::QSctpSocket**([QObject](../../O/QObject) **parent* = nullptr)





### *[virtual]* **QSctpSocket**::~QSctpSocket()





### *[override virtual]* void **QSctpSocket**::close()





### *[override virtual]* void **QSctpSocket**::disconnectFromHost()





### bool **QSctpSocket**::isInDatagramMode() const





### int **QSctpSocket**::maximumChannelCount() const





### *[override virtual protected]* qint64 **QSctpSocket**::readData(char **data*, qint64 *maxSize*)





### [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) **QSctpSocket**::readDatagram()





### *[override virtual protected]* qint64 **QSctpSocket**::readLineData(char **data*, qint64 *maxlen*)





### void **QSctpSocket**::setMaximumChannelCount(int *count*)





### bool **QSctpSocket**::writeDatagram(const [QNetworkDatagram](../../N/QNetworkDatagram/QNetworkDatagram.md) &*datagram*)