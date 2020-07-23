# QGenericReturnArgument 类

`QGenericReturnArgument` 类是用于序列化返回值的内部辅助类。[更多信息...](#详细描述)

| 属性   | 内容                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | `#include <QGenericReturnArgument>`                          |
| qmake  | `QT += core`                                                 |
| 继承自 | [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) |



## 公共成员函数

| 返回类型 | 函数                                                         |
| -------- | ------------------------------------------------------------ |
|          | [QGenericReturnArgument](#qgenericreturnargumentqgenericreturnargumentconst-char-name--nullptr-void-data--nullptr)(const char \**name* = nullptr, void \**data* = nullptr) |



## 详细描述

该类绝不应该被主动使用，请通过 [Q_RETURN_ARG](#qgenericargument-qargtype-const-type-&value)() 来使用。. Please use the [Q_RETURN_ARG](qmetaobject.html#Q_RETURN_ARG)() macro instead.

See also [Q_RETURN_ARG](qmetaobject.html#Q_RETURN_ARG)(), [QMetaObject::invokeMethod](qmetaobject.html#invokeMethod)(), and [QGenericArgument](qgenericargument.html).



## 成员函数描述

### QGenericReturnArgument::QGenericReturnArgument(const char \**name* = nullptr, void \**data* = nullptr)

Constructs a QGenericReturnArgument object with the given *name* and *data*. 