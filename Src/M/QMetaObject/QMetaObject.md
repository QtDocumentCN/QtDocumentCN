# QMetaObject 结构体

QMetaObject 类包含了 Qt 对象的元信息。[更多内容...](#详细描述)。

| 属性   | 内容                      |
| ------ | ------------------------- |
| 头文件 | `#include <QMetaObject> ` |
| qmake  | `QT += core`              |



## 公共成员类型

| 类型  | 名称                            |
| ----- | ------------------------------- |
| class | **[Connection](Connection.md)** |



## 公共成员函数

| 返回类型            | 函数                                                         |
| ------------------- | ------------------------------------------------------------ |
| QMetaClassInfo      | **[classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)**(int *index*) const |
| int                 | **[classInfoCount](#int-qmetaobjectclassinfocount-const)**() const |
| int                 | **[classInfoOffset](#int-qmetaobjectclassinfooffset-const)**() const |
| const char *        | **[className](#const-char-qmetaobjectclassname-const)**() const |
| QMetaMethod         | **[constructor](#qmetamethod-qmetaobjectconstructorint-index-const)**(int *index*) const |
| int                 | **[constructorCount](#int-qmetaobjectconstructorcount-const)**() const |
| QMetaEnum           | **[enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)**(int *index*) const |
| int                 | **[enumeratorCount](#int-qmetaobjectenumeratorcount-const)**() const |
| int                 | **[enumeratorOffset](#int-qmetaobjectenumeratoroffset-const)**() const |
| int                 | **[indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)**(const char \**name*) const |
| int                 | **[indexOfConstructor](#int-qmetaobjectindexofconstructorconst-char-constructor-const)**(const char \**constructor*) const |
| int                 | **[indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)**(const char \**name*) const |
| int                 | **[indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)**(const char \**method*) const |
| int                 | **[indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)**(const char \**name*) const |
| int                 | **[indexOfSignal](#int-qmetaobjectindexofsignalconst-char-signal-const)**(const char \**signal*) const |
| int                 | **[indexOfSlot](#int-qmetaobjectindexofslotconst-char-slot-const)**(const char \**slot*) const |
| bool                | **[inherits](#bool-qmetaobjectinheritsconst-qmetaobject-metaobject-const)**(const QMetaObject \**metaObject*) const |
| QMetaMethod         | **[method](#qmetamethod-qmetaobjectmethodint-index-const)**(int *index*) const |
| int                 | **[methodCount](#int-qmetaobjectmethodcount-const)**() const |
| int                 | **[methodOffset](#int-qmetaobjectmethodoffset-const)**() const |
| QObject *           | **[newInstance](#qobject-qmetaobjectnewinstanceqgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| QMetaProperty       | **[property](#qmetaproperty-qmetaobjectpropertyint-index-const)**(int *index*) const |
| int                 | **[propertyCount](#int-qmetaobjectpropertycount-const)**() const |
| int                 | **[propertyOffset](#int-qmetaobjectpropertyoffset-const)**() const |
| const QMetaObject * | **[superClass](#const-qmetaobject-qmetaobjectsuperclass-const)**() const |
| QMetaProperty       | **[userProperty](#qmetaproperty-qmetaobjectuserproperty-const)**() const |



## 静态公共成员

| 返回类型   | 函数                                                         |
| ---------- | ------------------------------------------------------------ |
| bool       | **[checkConnectArgs](#static-bool-qmetaobjectcheckconnectargsconst-char-signal-const-char-method)**(const char \**signal*, const char \**method*) |
| bool       | **[checkConnectArgs](#static-bool-qmetaobjectcheckconnectargsconst-qmetamethod-&signal-const-qmetamethod-&method)**(const QMetaMethod &*signal*, const QMetaMethod &*method*) |
| void       | **[connectSlotsByName](#static-void-qmetaobjectconnectslotsbynameqobject-object)**(QObject **object*) |
| bool       | **[invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qtconnectiontype-type-qgenericreturnargument-ret-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)**(QObject \**obj*, const char **member*, Qt::ConnectionType *type*, QGenericReturnArgument *ret*, QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | **[invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qgenericreturnargument-ret-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)**(QObject \**obj*, const char **member*, QGenericReturnArgument *ret*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | **[invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qtconnectiontype-type-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)**(QObject \**obj*, const char **member*, Qt::ConnectionType *type*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | **[invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)**(QObject \**obj*, const char **member*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | **[invokeMethod](#static-template-<typename-functor-typename-functorreturntype>-bool-qmetaobjectinvokemethodqobject-context-functor-function-qtconnectiontype-type--qtautoconnection-functorreturntype-ret--nullptr)**(QObject \**context*, Functor *function*, Qt::ConnectionType *type* = Qt::AutoConnection, FunctorReturnType \**ret* = nullptr) |
| bool       | **[invokeMethod](#static-template-<typename-functor-typename-functorreturntype>-bool-qmetaobjectinvokemethodqobject-context-functor-function-functorreturntype-ret)**(QObject \**context*, Functor *function*, FunctorReturnType \**ret*) |
| QByteArray | **[normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)**(const char **method*) |
| QByteArray | **[normalizedType](#static-qbytearray-qmetaobjectnormalizedtypeconst-char-type)**(const char **type*) |



## 宏

| 返回类型               | 宏                                                           |
| ---------------------- | ------------------------------------------------------------ |
| QGenericArgument       | **[Q_ARG](#qgenericargument-qargtype-const-type-&value)**(*Type*, const Type &*value*) |
| QGenericReturnArgument | **[Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)**(*Type*, Type &*value*) |



## 详细描述

Qt 的[元对象系统](../../T/The_Meta-Object_System/The_Meta-Object_System.md)负责信号槽跨对象通信机制、运行时类型信息和 Qt 的属性系统。应用中的每个 [QObject](../../O/QObject/QObject.md) 子类都有一个唯一的 QMetaObject 实例（译者注：与类一一对应，即同一个 QObject 子类的任意对象，都使用同一个 QMetaObject），其中保存了这个 [QObject](../../O/QObject/QObject.md) 子类的所有元信息，可以通过 [QObject::metaObject](../../O/QObject/QObject.md#metaObject)() 获取。

QMetaObject 在应用编写中通常不需要，但在进行元编程时会非常有用，例如脚本引擎或者用户界面生成器。

最常用的成员函数有：

- [className](#const-char-qmetaobjectclassname-const)() 返回类的名称。
- [superClass](#const-qmetaobject-qmetaobjectsuperclass-const)() 返回父类对应的元对象。
- [method](#qmetamethod-qmetaobjectmethodint-index-const)() 和 [methodCount](#int-qmetaobjectmethodcount-const)() 提供关于一个类的元方法（信号、槽和其它[可动态调用](../../O/QObject/QObject.md#QINVOKABLE)的成员方法）。
- [enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)() 和 [enumeratorCount](#int-qmetaobjectenumeratorcount-const)() 提供一个类的枚举类型的信息。
- [propertyCount](#int-qmetaobjectpropertycount-const)() 和 [property](#qmetaproperty-qmetaobjectpropertyint-index-const)() 提供一个类的属性的信息。
- [constructor](#qmetamethod-qmetaobjectconstructorint-index-const)() 和 [constructorCount](#int-qmetaobjectconstructorcount-const)() 提供一个类的元构造函数的信息。

索引函数 [indexOfConstructor](#int-qmetaobjectindexofconstructorconst-char-constructor-const)()、[indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)()、[indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)() 和 [indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)() 将构造函数、成员函数、枚举类型和属性的名称映射为索引。例如，当连接信号槽时，Qt 内部使用 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)() 进行检索。

类可以拥有一系列 名称—数值 格式的附加信息，保存在 [QMetaClassInfo](../../M/QMetaClassInfo/QMetaClassInfo.md) 对象中。信息条目数量可通过 [classInfoCount](#int-qmetaobjectclassinfocount-const)()查询， [classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)()返回单条信息，也可通过 [indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)() 检索信息条目。

注意：元对象系统的操作通常是线程安全的，比如元对象是在编译期生成的静态只读实例。然而，如果元对象在被程序动态修改了（如通过 [QQmlPropertyMap](../../Q/QQmlPropertyMap/QQmlPropertyMap.md)），应用需要显示地同步对相关对象的访问。

**另请参阅：**[QMetaClassInfo](../../M/QMetaClassInfo/QMetaClassInfo.md)、[QMetaEnum](../../M/QMetaEnum/QMetaEnum.md)、[QMetaMethod](../../M/QMetaMethod/QMetaMethod.md)、[QMetaProperty](../../M/QMetaProperty/QMetaProperty.md)、[QMetaType](../../M/QMetaType/QMetaType.md) 和 [Meta-Object System](../../T/The_Meta-Object_System/The_Meta-Object_System.md)。



## 成员函数文档

### *[static]* bool QMetaObject::checkConnectArgs(const char \**signal*, const char \**method*)

如果 `signal` 和 `method` 的参数能够匹配则返回 `true`，否则返回 `false`。

`signal` 和 `method` 都被假设是已经规范化的。

**另请参阅：**[normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)()。

----

### *[static]* bool QMetaObject::checkConnectArgs(const [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) &*signal*, const [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) &*method*)

这是一个重载函数。

如果 `signal` 和 `method` 的参数能够匹配则返回 `true`，否则返回 `false`。

本函数在 Qt 5.0 中被引入。

----

### [QMetaClassInfo](../../M/QMetaClassInfo/QMetaClassInfo.md) QMetaObject::classInfo(int *index*) const

返回对应 `index` 的类型信息的元数据对象。

范例：

```cpp
 class MyClass : public QObject
 {
     Q_OBJECT
     Q_CLASSINFO("author", "Sabrina Schweinsteiger")
     Q_CLASSINFO("url", "http://doc.moosesoft.co.uk/1.0/")

 public:
     ...
 };
```

**另请参阅：**[classInfoCount](#int-qmetaobjectclassinfocount-const)()、[classInfoOffset](#int-qmetaobjectclassinfooffset-const)() 和 [indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)()。

----

### int QMetaObject::classInfoCount() const

返回该类信息条目数量。

**另请参阅：**[classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)()、[classInfoOffset](#int-qmetaobjectclassinfooffset-const)() 和 [indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)()。

----

### int QMetaObject::classInfoOffset() const

返回类信息在该类中的偏移量，即第一条类信息的编号。

若该类没有包含类信息的父类，则偏移量为 `0`，否则偏移量是所有父类的类信息数量的总和。

**另请参阅：**[classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)()、[classInfoCount](#int-qmetaobjectclassinfocount-const)() 和 [indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)()。

----

### const char \*QMetaObject::className() const

返回该类的名称。

**另请参阅：**[superClass](#const-qmetaobject-qmetaobjectsuperclass-const)()。

----

### [static] void QMetaObject::connectSlotsByName([QObject](../../O/QObject/QObject.md) \**object*)

递归检索 `object` 和所有子对象，将它们的信号连接至 `object` 中匹配的槽，匹配格式如下：

```cpp
 void on_<对象名>_<信号名>(<信号参数>);
```

假设有一个[对象名](../../O/QObject/QObject.md#objectName-prop) 为 `button1` 的 `QPushButton` 类型的子对象，则捕获它的 `clicked()` 信号的槽应为：

```
 void on_button1_clicked();
```

若 `object` 对象自身的名字已设置，则它自己的信号也会被连接至对应的槽。

**另请参阅：**[QObject::setObjectName](../../O/QObject/QObject.md#objectName-prop)().

----

### [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) QMetaObject::constructor(int *index*) const

返回指定 `index` 的构造函数的元数据。

该函数在 Qt 4.5 中被引入。

**另请参阅：**[constructorCount](#int-qmetaobjectconstructorcount-const)() 和 [newInstance](#qobject-qmetaobjectnewinstanceqgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)()。

----

### int QMetaObject::constructorCount() const

返回此类的构造函数个数。

该函数在 Qt 4.5 中被引入。

**另请参阅：**[constructor](#qmetamethod-qmetaobjectconstructorint-index-const)() 和 [indexOfConstructor](#int-qmetaobjectindexofconstructorconst-char-constructor-const)()。

----

### [QMetaEnum](qmetaenum.html) QMetaObject::enumerator(int *index*) const

返回指定 `index` 的枚举类型的元数据。

**另请参阅：**[enumeratorCount](#int-qmetaobjectenumeratorcount-const)()、[enumeratorOffset](#int-qmetaobjectenumeratoroffset-const)() 和 [indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)()。

----

### int QMetaObject::enumeratorCount() const

返回该类的枚举类型的个数。

**另请参阅：**[enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)()、[enumeratorOffset](#int-qmetaobjectenumeratoroffset-const)() 和 [indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)()。

----

### int QMetaObject::enumeratorOffset() const

返回该类的枚举类型偏移量，即首个枚举变量的编号。

若该类没有包含枚举类型的父类，则偏移量为 `0`，否则偏移量是所有父类的枚举类型数量的总和。

**另请参阅：**[enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)()、[enumeratorCount](#qmetaenum-qmetaobjectenumeratorint-index-constCount)() 和 [indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)()。

----

### int QMetaObject::indexOfClassInfo(const char \**name*) const

查找名为 `name` 的类型信息条目并返回其编号，未找到则返回`-1`。

**另请参阅：**[classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)()、[classInfoCount](#qmetaclassinfo-qmetaobjectclassinfoint-index-constCount)() 和 [classInfoOffset](#qmetaclassinfo-qmetaobjectclassinfoint-index-constOffset)()。

----

### int QMetaObject::indexOfConstructor(const char \**constructor*) const

查找名为 `constructor` 的构造函数并返回其编号，未找到则返回`-1`。

**注意：**`constructor` 需要为规范化的格式，如 [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)() 的返回值。

该函数在 Qt 4.5 中被引入。

**另请参阅：**[constructor](#qmetamethod-qmetaobjectconstructorint-index-const)()、[constructorCount](#qmetamethod-qmetaobjectconstructorint-index-constCount)() 和 [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)()。

----

### int QMetaObject::indexOfEnumerator(const char \**name*) const

查找名为 `name` 的枚举类型并返回其编号，未找到则返回`-1`。

**另请参阅：**[enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)(), [enumeratorCount](#qmetaenum-qmetaobjectenumeratorint-index-constCount)() 和 [enumeratorOffset](#qmetaenum-qmetaobjectenumeratorint-index-constOffset)().

----

### int QMetaObject::indexOfMethod(const char \**method*) const

查找名为 `method` 的方法并返回其编号，未找到则返回`-1`。

**注意：**`method` 需要为规范化的格式，如 [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)() 的返回值。

**另请参阅：**[method](#qmetamethod-qmetaobjectmethodint-index-const)()、[methodCount](#int-qmetaobjectmethodcount-const)()、[methodOffset](#int-qmetaobjectmethodoffset-const)() 和 [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)()。

----

### int QMetaObject::indexOfProperty(const char \**name*) const

查找名为 `name` 的属性并返回其编号，未找到则返回`-1`。

**另请参阅：**[property](#qmetaproperty-qmetaobjectpropertyint-index-const)()、[propertyCount](#qmetaproperty-qmetaobjectpropertyint-index-constCount)() 和 [propertyOffset](#qmetaproperty-qmetaobjectpropertyint-index-constOffset)()。

----

### int QMetaObject::indexOfSignal(const char \**signal*) const

查找名为 `name` 的信号并返回其编号，未找到则返回`-1`。

此方法与 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)() 相似，区别是若该方法存在但并非信号函数，则会返回 `-1`。

**注意：**`signal` 需要为规范化的格式，如 [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)() 的返回值。

**另请参阅：**[indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)()、[normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)(), [method](#qmetamethod-qmetaobjectmethodint-index-const)()、[methodCount](#int-qmetaobjectmethodcount-const)() 和 [methodOffset](#int-qmetaobjectmethodoffset-const)()。

----

### int QMetaObject::indexOfSlot(const char \**slot*) const

查找名为 `name` 的槽并返回其编号，未找到则返回`-1`。

此方法与 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)() 相似，区别是若该方法存在但并非槽函数，则会返回 `-1`。

**另请参阅：**[indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)()、[method](#qmetamethod-qmetaobjectmethodint-index-const)()、[methodCount](#int-qmetaobjectmethodcount-const)() 和 [methodOffset](#int-qmetaobjectmethodoffset-const)()。

----

### bool QMetaObject::inherits(const [QMetaObject]() \**metaObject*) const

若该 [QMetaObject](../../M/QMetaObject/QMetaObject.md) 继承自 `metaObject` 描述的类型，则返回 `true`，否则返回 `false`。

一个类型被认为是继承自它自己的。

该函数在 Qt 5.7 中被引入。

----

### *[static]* bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**obj*, const char \**member*, [Qt::ConnectionType](../../Q/Qt/Qt.md#ConnectionType-enum) *type*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *ret*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument())

通过 `obj` 对象动态调用它的 `member` 方法（或者信号和槽），若调用成功则返回 `true`，若该对象没有此方法或参数不匹配则返回 `false`。

该调用可以是同步或异步的，由 `type` 决定：

- 若 `type` 是 [Qt::DirectConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，则该方法会被立即执行。

- 若 `type` 是 [Qt::QueuedConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，则会发送一个 [QEvent](../../E/QEvent/QEvent.md) ，该方法会在应用进入该对象所属线程的主事件循环后执行。
- 若 `type` 是 [Qt::BlockingQueuedConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，则该方法会通过与 [Qt::QueuedConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 相同的方式执行，此外当前线程会被阻塞，直到该事件被响应。使用此方法在相同线程的对象间通信会导致死锁。
- 若 `type` 是 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，当 `obj` 与调用者处于相同线程中时，该方法会被同步执行，否则会被异步执行。

`member` 函数的返回值会被存放在 `ret` 中。若调用方式是异步，则返回值无法被获取。最多可以传递十个参数 (`val0`, `val1`, `val2`, `val3`, `val4`, `val5`, `val6`, `val7`, `val8` 和 `val9`) 至 `member` 函数。

[QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) 和 [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) 是内部的辅助类。为了动态调用信号槽，您需要将参数通过 [Q_ARG](#qgenericargument-qargtype-const-type-&value)() 和 [Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)() 宏进行封装。[Q_ARG](#qgenericargument-qargtype-const-type-&value)() 接受一个类型名称和一个该类型的不可变引用；[Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)() 接受一个类型名称和一个该类型的可变引用。

您只需要将信号槽的名称传递至本函数，无需传递完整的签名。例如，异步调用某个 [QThread](../../T/QThread/QThread.md) 对象的 [quit()](../../T/QThread/QThread.md#quit) 槽需要的代码如下：

```cpp
 QMetaObject::invokeMethod(thread, "quit",
                           Qt::QueuedConnection);
```

当异步调用方法时，传递的参数必须被 Qt 的元对象系统所知悉，因为 Qt 需要在后台事件中拷贝并保存它们。如果您使用队列连接时遇到下述错误信息：

```cpp
 QMetaObject::invokeMethod: Unable to handle unregistered datatype 'MyType'
```

则在调用 `invokeMethod`() 之前通过 [qRegisterMetaType](../../M/QMetaType/QMetaType.md#qRegisterMetaType-1)() 来注册该数据类型。

若想通过 `obj` 对象同步调用 `compute(QString, int, double)` 槽，则代码如下：

To synchronously invoke the compute(QString, int, double) slot on some arbitrary object obj retrieve its return value:

```cpp
 QString retVal;
 QMetaObject::invokeMethod(obj, "compute", Qt::DirectConnection,
                           Q_RETURN_ARG(QString, retVal),
                           Q_ARG(QString, "sqrt"),
                           Q_ARG(int, 42),
                           Q_ARG(double, 9.7));
```

若 `compute` 槽通过特定顺序没有完整获取到一个 [QString](../../S/QString/QString.md)、一个 `int` 和一个 `double`，则此调用会失败。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

**另请参阅：**[Q_ARG](#qgenericargument-qargtype-const-type-&value)()、[Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)()、[qRegisterMetaType](qmetatype.html#qRegisterMetaType-1)() 和 [QMetaMethod::invoke](../../M/QMetaMethod/QMetaMethod.md#invoke)()。

----

### *[static]* bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**obj*, const char \**member*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *ret*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument())

此函数是 `invokeMethod`()的重载。

此重载始终通过 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 调用对应方法。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

----

### *[static]* bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**obj*, const char \**member*, [Qt::ConnectionType](../../Q/Qt/Qt.md#ConnectionType-enum) *type*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument())

此函数是 `invokeMethod`()的重载。

此重载用于不关心对返回值的场合。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

----

### *[static]* bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**obj*, const char \**member*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument())

此函数是 `invokeMethod`()的重载。

此重载通过 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 调用对应方法，并忽略返回值。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

----

### *[static]* template <typename Functor, typename FunctorReturnType> bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**context*, Functor *function*, [Qt::ConnectionType](../../Q/Qt/Qt.md#ConnectionType-enum) *type* = Qt::AutoConnection, FunctorReturnType \**ret* = nullptr)

此函数是 `invokeMethod`()的重载。

通过 `type` 方式在 `context` 所属的事件循环中动态调用 `function`。`function` 可以是一个仿函数或成员函数指针。若该函数可被动态调用则返回 `true`，当该函数不存在或参数不匹配时返回 `false`。函数的返回值将被保存至 `ret` 中。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

该函数在 Qt 5.10 中被引入。

----

### *[static]* template <typename Functor, typename FunctorReturnType> bool QMetaObject::invokeMethod([QObject](../../O/QObject/QObject.md) \**context*, Functor *function*, FunctorReturnType \**ret*)

此函数是 `invokeMethod`()的重载。

通过 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 方式动态调用 `function`。`function` 可以是一个仿函数或成员函数指针。若该函数可被动态调用则返回 `true`，当该函数不存在或参数不匹配时返回 `false`。函数的返回值将被保存至 `ret` 中。

**注意：** 此方法是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。

该函数在 Qt 5.10 中被引入。

----

### [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) QMetaObject::method(int *index*) const

返回指定 `index` 的方法的元数据。

**另请参阅：**[methodCount](#int-qmetaobjectmethodcount-const)(), [methodOffset](#int-qmetaobjectmethodoffset-const)() 和 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)().

----

### int QMetaObject::methodCount() const

返回该类中方法的数量，包括所有基类的方法个数。除了常规成员函数外，也包含信号函数和槽函数。

Returns the number of methods in this class, including the number of methods provided by each base class. These include signals and slots as well as normal member functions.

使用下述代码来将所给类的所有方法签名存储至 [QStringList](../../S/QStringList/QStringList.md)：

```cpp
 const QMetaObject* metaObject = obj->metaObject();
 QStringList methods;
 for(int i = metaObject->methodOffset(); i < metaObject->methodCount(); ++i)
     methods << QString::fromLatin1(metaObject->method(i).methodSignature());
```

**另请参阅：**[method](#qmetamethod-qmetaobjectmethodint-index-const)()、[methodOffset](#int-qmetaobjectmethodoffset-const)() 和 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)()。

----

### int QMetaObject::methodOffset() const

返回类方法在该类中的偏移量，即第一个类方法的编号。

该偏移量是所有父类的方法数总和（因此总为正数，因为 [QObject](../../O/QObject/QObject.md) 有 `deleteLater`() 槽和 `destroyed`() 信号）。

**另请参阅：**[method](#qmetamethod-qmetaobjectmethodint-index-const)()、[methodCount](#int-qmetaobjectmethodcount-const)() 和 [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)()。

----

### [QObject](../../O/QObject/QObject.md) \*QMetaObject::newInstance([QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

构造一个此类的新实例。您可以传递最多十个参数 (`val0`, `val1`, `val2`, `val3`, `val4`, `val5`, `val6`, `val7`, `val8` 和 `val9`) 至构造函数。返回构造的新对象，若没有合适的构造函数则返回 `nullptr`。

**注意：**只有通过 [Q_INVOKABLE](../../O/QObject/QObject.md#Q_INVOKABLE) 修饰符声明的构造函数才能在元对象系统中使用。

该函数在 Qt 4.5 中被引入。

**另请参阅：**[Q_ARG](#qgenericargument-qargtype-const-type-&value)() 和 [constructor](#qmetamethod-qmetaobjectconstructorint-index-const)()。

----

### *[static]* [QByteArray](../../B/QByteArray/QByteArray.md) QMetaObject::normalizedSignature(const char \**method*)

将给予的 `method` 进行规范化。

Qt 使用规范化的签名来来判断两个给定的信号和槽是否匹配。规范化操作会将空格减到最少，将 `const` 适当前移，移除值类型的 `const`，并将不可变引用替换为值类型。

**另请参阅：**[checkConnectArgs](#static-bool-qmetaobjectcheckconnectargsconst-char-signal-const-char-method)() 和 [normalizedType](#static-qbytearray-qmetaobjectnormalizedtypeconst-char-type)()。

----

### *[static]* [QByteArray](../../B/QByteArray/QByteArray.md) QMetaObject::normalizedType(const char **type*)

将 `type` 规范化。

请参阅 [QMetaObject::normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)() 中关于 Qt 如何进行规范化的描述。

范例：

```cpp
 QByteArray normType = QMetaObject::normalizedType(" int    const  *");
 // 规范化的类型将为 "const int*"
```

该函数在 Qt 4.2 中被引入。

**另请参阅：**[normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)().

----

### [QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) QMetaObject::property(int *index*) const

返回指定 `index` 的属性的元数据。若该属性不存在，则返回空的 [QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) 对象。

**另请参阅：**[propertyCount](#qmetaproperty-qmetaobjectpropertyint-index-constCount)()、[propertyOffset](#qmetaproperty-qmetaobjectpropertyint-index-constOffset)() 和 [indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)()。

----

### int QMetaObject::propertyCount() const

返回该类中属性的类型，包括所有基类的属性个数。

使用如下代码来将给定类的所有属性名称保存至 [QStringList](../../S/QStringList/QStringList.md)：

```cpp
 const QMetaObject* metaObject = obj->metaObject();
 QStringList properties;
 for(int i = metaObject->propertyOffset(); i < metaObject->propertyCount(); ++i)
     properties << QString::fromLatin1(metaObject->property(i).name());
```

**另请参阅：**[property](#qmetaproperty-qmetaobjectpropertyint-index-const)()、[propertyOffset](#qmetaproperty-qmetaobjectpropertyint-index-constOffset)() 和 [indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)()。

----

### int QMetaObject::propertyOffset() const

返回类属性在该类中的偏移量，即第一条类属性的编号。

该偏移量包含所有父类的类属性数量总和（因此总为正数，因为 [QObject](../../O/QObject/QObject.md) 有 `name`() 属性）。

**另请参阅：**[property](#qmetaproperty-qmetaobjectpropertyint-index-const)()、[propertyCount](#qmetaproperty-qmetaobjectpropertyint-index-constCount)() 和 [indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)()。

----

### const [QMetaObject]() \*QMetaObject::superClass() const

返回父类的元对象，若不存在则返回 `nullptr`。

**另请参阅：**[className](#const-char-qmetaobjectclassname-const)()。

----

### [QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) QMetaObject::userProperty() const

返回 `USER` 标志位为 `true` 的元属性。

该函数在 Qt 4.2 中被引入。

**另请参阅：**[QMetaProperty::isUser](../../M/QMetaProperty/QMetaProperty.md#isUser)()。



## 宏文档

### [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) Q_ARG(*Type*, const Type &*value*)

该宏接受一个 `type` 和一个该类型的 `value` 参数，返回一个用于传递至 [QMetaObject::invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qtconnectiontype-type-qgenericreturnargument-ret-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)() 的 [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) 对象。

**另请参阅：**[Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)()。

----

### [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) Q_RETURN_ARG(*Type*, Type &*value*)

该宏接受一个 `Type` 和一个该类型的可变引用 `value` 参数，返回一个用于传递至 [QMetaObject::invokeMethod](#static-bool-qmetaobjectinvokemethodqobject-obj-const-char-member-qtconnectiontype-type-qgenericreturnargument-ret-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument)() 的包含该类型的 [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) 对象。

**另请参阅：**[Q_ARG](#qgenericargument-qargtype-const-type-&value)().。