# QMetaClassInfo 类

QMetaClassInfo 类提供了某个类的附加信息。[更多内容...](#详细描述)

| 属性   | 内容                        |
| ------ | --------------------------- |
| 头文件 | `#include <QMetaClassInfo>` |
| qmake: | `QT += core`                |



## Public Functions

| 返回类型     | 函数                                                         |
| ------------ | ------------------------------------------------------------ |
| const char * | **[name](QMetaClassInfo.md#const-char-qmetaclassinfoname-const)**() const |
| const char * | **[value](QMetaClassInfo.md#const-char-qmetaclassinfovalue-const)**() const |



## 详细描述

类型信息对象指的在源代码中通过 [Q_CLASSINFO](../../O/QObject/QObject.md#qclassinfoname-value)() 指定的`名称-值`。这些信息可以通过 [name](QMetaClassInfo.md#const-char-qmetaclassinfoname-const)() 和 [value](QMetaClassInfo.md#const-char-qmetaclassinfovalue-const)() 获取，例如：

```cpp
class MyClass
{
    Q_OBJECT
    Q_CLASSINFO("author", "Sabrina Schweinsteiger")
    Q_CLASSINFO("url", "http://doc.moosesoft.co.uk/1.0/")

public:
    ...
};
```

此机制可以在您的应用中自由使用，Qt 不会在自身的任何类中使用它。

**另请参阅：**[QMetaObject](../../M/QMetaObject/QMetaObject.md)。



## 成员函数文档

### const char *QMetaClassInfo::name() const

返回本信息对象的名称。

**另请参阅：**[value](QMetaClassInfo.md#const-char-qmetaclassinfovalue-const)()。

----

### const char *QMetaClassInfo::value() const

返回本信息对象的值。

**See also** [name](QMetaClassInfo.md#const-char-qmetaclassinfoname-const)()。