# QGenericArgument 类

`QGenericArgument` 类是用于序列化参数的内部辅助类。[更多信息...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)

| 属性   | 内容                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | `#include <QGenericArgument> `                               |
| qmake  | `QT += core`                                                 |
| 被继承 | [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) |



## 公共成员函数

| 返回类型     | 函数                                                         |
| ------------ | ------------------------------------------------------------ |
|              | **[QGenericArgument](#qgenericargumentqgenericargumentconst-char-name--nullptr-const-void-data--nullptr)**(const char \**name* = nullptr, const void \**data* = nullptr) |
| void *       | **[data](#void-qgenericargumentdata-const)**() const         |
| const char * | **[name](#const-char-qgenericargumentname-const)**() const   |



## 详细描述

该类绝不应该被主动使用，请通过 [Q_ARG](#qgenericargument-qargtype-const-type-&value)() 来使用。

**另请参阅：**[Q_ARG](#qgenericargument-qargtype-const-type-&value)()、[QMetaObject::invokeMethod](#static-template-<typename-functor-typename-functorreturntype>-bool-qmetaobjectinvokemethodqobject-context-functor-function-functorreturntype-ret)() 和 [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md)。



## 成员函数描述

### QGenericArgument::QGenericArgument(const char \**name* = nullptr, const void \**data* = nullptr)

通过给定的 `name` 和 `data` 构造 `QGenericArgument` 对象。

----

### void *QGenericArgument::data() const

返回构造函数中设置的数据对象指针。

----

### const char *QGenericArgument::name() const

返回构造函数中设置的名称。
