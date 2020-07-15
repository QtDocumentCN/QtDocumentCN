[TOC]



# QSctpServer Class

QSctpServer 提供了一个基于 QSCTP 协议的服务器。

| 属性     | 方法                                           |
| -------- | ---------------------------------------------- |
| 头文件   | `include <QSctpServer>`                        |
| qmake    | QT += network                                  |
| 引入版本 | Qt5.8                                          |
| 继承自   | [QTcpServer](../../T/QTcpServer/QTcpServer.md) |

该类最初在 Qt5.8 版本时引入。



## 公共成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
|              | **[QSctpServer](QSctpServer.md)**(QObject **parent* = nullptr) |
| virtual      | **[~QSctpServer](QSctpServer.md)**()                         |
| int          | **[maximumChannelCount](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpserver.html#maximumChannelCount)**() const |
| QSctpSocket* | **[nextPendingDatagramConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpserver.html#nextPendingDatagramConnection)**() |
| void         | **[setMaximumChannelCount](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpserver.html#setMaximumChannelCount)**(int *count*) |



## 重写保护成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | **[incomingConnection](qthelp://org.qt-project.qtnetwork.5150/qtnetwork/qsctpserver.html#incomingConnection)**(qintptr *socketDescriptor*) override |



## 详细介绍





## 成员函数文档

