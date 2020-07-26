# QGenericReturnArgument 类

`QGenericReturnArgument` 类是用于序列化返回值的内部辅助类。[更多信息...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)

| 属性   | 内容                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | `#include <QGenericReturnArgument>`                          |
| qmake  | `QT += core`                                                 |
| 继承自 | [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) |



## 公共成员函数

| 返回类型 | 函数                                                         |
| -------- | ------------------------------------------------------------ |
|          | **[QGenericReturnArgument](#qgenericreturnargumentqgenericreturnargumentconst-char-name--nullptr-void-data--nullptr)**(const char \**name* = nullptr, void \**data* = nullptr) |



## 详细描述

该类绝不应该被主动使用，请通过 [Q_RETURN_ARG](#qgenericargument-qargtype-const-type-&value)() 来使用。

**另请参阅：**[Q_RETURN_ARG](qmetaobject.html#Q_RETURN_ARG)()，[QMetaObject::invokeMethod](qmetaobject.html#invokeMethod)() 和 [QGenericArgument](qgenericargument.html)。



## 成员函数描述

### QGenericReturnArgument::QGenericReturnArgument(const char \**name* = nullptr, void \**data* = nullptr)

通过给定的 `name` 和 `data` 构造 `QGenericReturnArgument` 对象。
