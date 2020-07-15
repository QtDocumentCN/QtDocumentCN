这里是文档翻译的模板，详情请见[贡献指南](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/CONTRIBUTING.md)。

翻译文档结构为三层目录结构。

```markdown
# 类名
	## 公共成员类型
	## 公有成员函数
	## 成员类型文档
		### 类型1
		### 类型2
	## 成员函数文档
		### 函数1
		### 函数2
```



# **类名**

这里填一些简述。

|  属性  | 方法|
|------:|:------|
|头文件:|`    xxxxx`|
|实例化:|xxxx|
|继承:    |xxxx|
|派生:|xxxxxx|

## **公共成员类型**

|  类型  | 方法|
|------:|:------|
|enum| [BindFlag { ShareAddress, DontShareAddress, ReuseAddressHint, DefaultForPlatform }](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#enum-qabstractsocketbindflag--flags-qabstractsocketbindmode) |
|xxxxx|222222|



## 公共成员函数

|  类型  | 函数名|
|------:|:------|
|    |[QAbstractSocket(QAbstractSocket::SocketType *socketType*, QObject **parent*)](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#qabstractsocketqabstractsocketqabstractsocketsockettype-sockettype-qobject-parent)|
|void | [abort()](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#void-qabstractsocketabort) |
|xxx |yyy|



## **信号**

|  类型  | 函数名|
|------:|:------|
|void| [connected()](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#signal-void-qabstractsocketconnected) |
|xxx| yyy |



## 详细介绍

这里填一些详细介绍。



## 成员类型文档

### enum **QAbstractSocket**::BindFlag | flags **QAbstractSocket**::BindMode

这里填该类型详细信息。

### XXX

这里填该类型详细信息。



## 成员函数文档

### **QAbstractSocket**::QAbstractSocket(**QAbstractSocket**::SocketType *socketType*, QObject **parent*)

创建一个新抽象套接字 socketType 。 函数中父对象的参数传递给 [QObject](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/O/QObject/QObject.md) 的构造函数。

这就是它的构造函数嘛，没啥好说的。另外由于 QAbstractSocket 类继承自 [QObject](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/O/QObject/QObject.md) 类，应注意在 QAbstractSocket 类构造函数中调用一下父类 [QObject](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/O/QObject/QObject.md) 类的构造函数。

另外您也可以在 [socketType()](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/A/QAbstractSocket/QAbstractSocket.md#qabstractsocketsockettype-qabstractsocketsockettype-const) 成员函数文档，以及 [QTcpSocket](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/T/QTcpSocket/QTcpSocket.md) 和 [QUdpSocket](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/U/QUdpSocket/QUdpSocket.md) 类文档找到相关信息。



### *[virtual]* void XXX()

这里填函数详细介绍。

**注意：** 这里填注意事项。

**警告：** 这里填警告事项。

另外您也可以在……中找到相关信息。

