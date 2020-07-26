# Connection 类

[QMetaObject](../../M/QMetaObject/QMetaObject.md)::Connection 类。



## 公共成员函数

| 返回类型     | 函数                                                         |
| ------------ | ------------------------------------------------------------ |
|              | **[Connection](#connectionconnectionconnection-&&o)**(Connection &&*o*) |
|              | **[Connection](#connectionconnectionconst-connection-&other)**(const Connection &*other*) |
|              | **[Connection](#connectionconnection)**()                    |
| Connection & | **[operator=](#connection-&connectionoperatorconnection-&&other)**(Connection &&*other*) |
| Connection & | **[operator=](#connection-&connectionoperatorconst-connection-&other)**(const Connection &*other*) |
|              | **[~Connection](#connection~connection)**()                  |
| bool         | **[operator bool](#bool-connectionoperator-bool-const)**() const |



## 详细描述

代表一组信号槽（或信号-仿函数）连接的句柄。

此类可被用于检查连接是否有效，或通过 [QObject::disconnect](../../O/QObject/QObject.md#static-bool-qobjectdisconnectconst-qobject-sender-const-char-signal-const-qobject-receiver-const-char-method)() 断开连接。对于不具备上下文对象的 信号-仿函数 连接，这是唯一的断开连接的方式。

由于 `Connection` 仅仅是一个句柄，当被销毁或重新赋值时，底层的信号槽连接不会被影响。



## 成员函数文档

### Connection::Connection(Connection &&*o*)

移动构造函数，将其指向 `o` 原先指向的对象。

----

### Connection::Connection(const Connection &*other*)

生成 `other` 连接的句柄的一份拷贝。

----

### Connection::Connection()

创建一个空的连接实例。

----

### Connection &Connection::operator=(Connection &&*other*)

将 `other` 转移赋值至本对象，并返回本对象的引用。

----

### Connection &Connection::operator=(const Connection &*other*)

将 `other` 赋值给本对象，并返回本对象的引用。

----

### Connection::~Connection()

[QMetaObject::Connection](../QMetaObject/QMetaObject_Connection.md) 的析构函数。

----

### bool Connection::operator bool() const

若该对象有效，则返回 `true`。

若 [QObject::connect](../../O/QObject/QObject.md#static-qmetaobjectconnection-qobjectconnectconst-qobject-sender-const-char-signal-const-qobject-receiver-const-char-method-qtconnectiontype-type--qtautoconnection) 成功，则该连接是有效的；若 [QObject::connect](../../O/QObject/QObject.md#static-qmetaobjectconnection-qobjectconnectconst-qobject-sender-const-char-signal-const-qobject-receiver-const-char-method-qtconnectiontype-type--qtautoconnection) 无法找到对应的信号槽或参数不匹配，则该连接无效。 