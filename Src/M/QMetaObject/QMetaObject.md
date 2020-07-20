# QMetaObject 结构体

QMetaObject 类包含了 Qt 对象的元信息。[更多内容...](#详细描述)。

| 属性   | 内容                      |
| ------ | ------------------------- |
| 头文件 | `#include <QMetaObject> ` |
| qmake  | `QT += core`              |



## 公共成员类型



| 类型  | 名称                        |
| ----- | --------------------------- |
| class | [Connection](Connection.md) |



## 公共成员函数

| 返回类型            | 函数                                                         |
| ------------------- | ------------------------------------------------------------ |
| QMetaClassInfo      | [classInfo](#qmetaclassinfo-qmetaobjectclassinfoint-index-const)(int *index*) const |
| int                 | [classInfoCount](#int-qmetaobjectclassinfocount-const)() const |
| int                 | [classInfoOffset](#int-qmetaobjectclassinfooffset-const)() const |
| const char *        | [className](#const-char-qmetaobjectclassname-const)() const  |
| QMetaMethod         | [constructor](#qmetamethod-qmetaobjectconstructorint-index-const)(int *index*) const |
| int                 | [constructorCount](#int-qmetaobjectconstructorcount-const)() const |
| QMetaEnum           | [enumerator](#qmetaenum-qmetaobjectenumeratorint-index-const)(int *index*) const |
| int                 | [enumeratorCount](#int-qmetaobjectenumeratorcount-const)() const |
| int                 | [enumeratorOffset](#int-qmetaobjectenumeratoroffset-const)() const |
| int                 | [indexOfClassInfo](#int-qmetaobjectindexofclassinfoconst-char-name-const)(const char **name*) const |
| int                 | [indexOfConstructor](#int-qmetaobjectindexofconstructorconst-char-constructor-const)(const char **constructor*) const |
| int                 | [indexOfEnumerator](#int-qmetaobjectindexofenumeratorconst-char-name-const)(const char **name*) const |
| int                 | [indexOfMethod](#int-qmetaobjectindexofmethodconst-char-method-const)(const char **method*) const |
| int                 | [indexOfProperty](#int-qmetaobjectindexofpropertyconst-char-name-const)(const char **name*) const |
| int                 | [indexOfSignal](#int-qmetaobjectindexofsignalconst-char-signal-const)(const char **signal*) const |
| int                 | [indexOfSlot](#int-qmetaobjectindexofslotconst-char-slot-const)(const char **slot*) const |
| bool                | [inherits](#bool-qmetaobjectinheritsconst-qmetaobject-metaobject-const)(const QMetaObject **metaObject*) const |
| QMetaMethod         | [method](#qmetamethod-qmetaobjectmethodint-index-const)(int *index*) const |
| int                 | [methodCount](#int-qmetaobjectmethodcount-const)() const     |
| int                 | [methodOffset](#int-qmetaobjectmethodoffset-const)() const   |
| QObject *           | [newInstance](../../M/QMetaObject/QMetaObject.md#newInstance)(QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| QMetaProperty       | [property](#qmetaproperty-qmetaobjectpropertyint-index-const)(int *index*) const |
| int                 | [propertyCount](#int-qmetaobjectpropertycount-const)() const |
| int                 | [propertyOffset](#int-qmetaobjectpropertyoffset-const)() const |
| const QMetaObject * | [superClass](#const-qmetaobject-qmetaobjectsuperclass-const)() const |
| QMetaProperty       | [userProperty](#qmetaproperty-qmetaobjectuserproperty-const)() const |



## 静态公共成员

| 返回类型   | 函数                                                         |
| ---------- | ------------------------------------------------------------ |
| bool       | [checkConnectArgs](#static-bool-qmetaobjectcheckconnectargsconst-char-signal-const-char-method)(const char \**signal*, const char \**method*) |
| bool       | [checkConnectArgs](#static-bool-qmetaobjectcheckconnectargsconst-qmetamethod-&signal-const-qmetamethod-&method)(const QMetaMethod &*signal*, const QMetaMethod &*method*) |
| void       | [connectSlotsByName](#static-void-qmetaobjectconnectslotsbynameqobject-object)(QObject **object*) |
| bool       | [invokeMethod](#invokeMethod)(QObject \**obj*, const char \**member*, Qt::ConnectionType *type*, QGenericReturnArgument *ret*, QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | [invokeMethod](#invokeMethod-1)(QObject \**obj*, const char \**member*, QGenericReturnArgument *ret*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | [invokeMethod](#invokeMethod-2)(QObject \**obj*, const char \**member*, Qt::ConnectionType *type*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | [invokeMethod](#invokeMethod-3)(QObject \**obj*, const char \**member*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) |
| bool       | [invokeMethod](#static-template-<typename-functor-typename-functorreturntype>-bool-qmetaobjectinvokemethodqobject-context-functor-function-qtconnectiontype-type--qtautoconnection-functorreturntype-ret--nullptr)(QObject \**context*, Functor *function*, Qt::ConnectionType *type* = Qt::AutoConnection, FunctorReturnType \**ret* = nullptr) |
| bool       | [invokeMethod](#static-template-<typename-functor-typename-functorreturntype>-bool-qmetaobjectinvokemethodqobject-context-functor-function-functorreturntype-ret)(QObject \**context*, Functor *function*, FunctorReturnType \**ret*) |
| QByteArray | [normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)(const char **method*) |
| QByteArray | [normalizedType](#static-qbytearray-qmetaobjectnormalizedtypeconst-char-type)(const char **type*) |



## 宏

| QGenericArgument       | [Q_ARG](#qgenericargument-qargtype-const-type-&value)(*Type*, const Type &*value*) |
| ---------------------- | ------------------------------------------------------------ |
| QGenericReturnArgument | [Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)(*Type*, Type &*value*) |



## 详细描述

Qt 的[元对象系统](../../T/The_Meta-Object_System/The_Meta-Object_System.md)负责信号槽跨对象通信机制、运行时类型信息和 Qt 的属性系统。应用中的每个 [QObject](../../O/QObject/QObject.md) 子类都具有一个对立的 QMetaObject 实例，其中保存了这个 [QObject](../../O/QObject/QObject.md) 子类的所有元信息，可以通过 [QObject::metaObject](../../O/QObject/QObject.md#metaObject)() 获取。

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

### [static] bool QMetaObject::checkConnectArgs(const char \**signal*, const char \**method*)

如果 *signal* 和 *method* 的参数能够匹配则返回 `true`，否则返回 `false`。

*signal* 和 *method* 都被假设是已经标准化的。

**另请参阅：**[normalizedSignature](#static-qbytearray-qmetaobjectnormalizedsignatureconst-char-method)()。

----

### [static] bool QMetaObject::checkConnectArgs(const [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) &*signal*, const [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) &*method*)

这是一个重载函数。

如果 *signal* 和 *method* 的参数能够匹配则返回 `true`，否则返回 `false`。

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

Returns the number of items of class information in this class.

**另请参阅：**[classInfo](#classInfo)(), [classInfoOffset](#classInfoOffset)(), and [indexOfClassInfo](#indexOfClassInfo)().

----

### int QMetaObject::classInfoOffset() const

Returns the class information offset for this class; i.e. the index position of this class's first class information item.

If the class has no superclasses with class information, the offset is 0; otherwise the offset is the sum of all the class information items in the class's superclasses.

**另请参阅：**[classInfo](#classInfo)(), [classInfoCount](#classInfoCount)(), and [indexOfClassInfo](#indexOfClassInfo)().

----

### const char *QMetaObject::className() const

Returns the class name.

**另请参阅：**[superClass](#superClass)().

----

### [static] void QMetaObject::connectSlotsByName([QObject](qobject.html) **object*)

Searches recursively for all child objects of the given *object*, and connects matching signals from them to slots of *object* that follow the following form:

```
 void on_<object name>_<signal name>(<signal parameters>);
```

Let's assume our object has a child object of type QPushButton with the [object name](qobject.html#objectName-prop) button1. The slot to catch the button's clicked() signal would be:

```
 void on_button1_clicked();
```

If *object* itself has a properly set object name, its own signals are also connected to its respective slots.

**另请参阅：**[QObject::setObjectName](qobject.html#objectName-prop)().

----

### [Q](../../M/QMetaMethod/QMetaMethod.md)MetaMethod QMetaObject::constructor(int *index*) const

Returns the meta-data for the constructor with the given *index*.

This function was introduced in Qt 4.5.

**另请参阅：**[constructorCount](#constructorCount)() and [newInstance](#newInstance)().

----

### int QMetaObject::constructorCount() const

Returns the number of constructors in this class.

This function was introduced in Qt 4.5.

**另请参阅：**[constructor](#constructor)() and [indexOfConstructor](#indexOfConstructor)().

----

### [Q](qmetaenum.html)MetaEnum QMetaObject::enumerator(int *index*) const

Returns the meta-data for the enumerator with the given *index*.

**另请参阅：**[enumeratorCount](#enumeratorCount)(), [enumeratorOffset](#enumeratorOffset)(), and [indexOfEnumerator](#indexOfEnumerator)().

----

### int QMetaObject::enumeratorCount() const

Returns the number of enumerators in this class.

**另请参阅：**[enumerator](#enumerator)(), [enumeratorOffset](#enumeratorOffset)(), and [indexOfEnumerator](#indexOfEnumerator)().

----

### int QMetaObject::enumeratorOffset() const

Returns the enumerator offset for this class; i.e. the index position of this class's first enumerator.

If the class has no superclasses with enumerators, the offset is 0; otherwise the offset is the sum of all the enumerators in the class's superclasses.

**另请参阅：**[enumerator](#enumerator)(), [enumeratorCount](#enumeratorCount)(), and [indexOfEnumerator](#indexOfEnumerator)().

----

### int QMetaObject::indexOfClassInfo(const char **name*) const

Finds class information item *name* and returns its index; otherwise returns -1.

**另请参阅：**[classInfo](#classInfo)(), [classInfoCount](#classInfoCount)(), and [classInfoOffset](#classInfoOffset)().

----

### int QMetaObject::indexOfConstructor(const char **constructor*) const

Finds *constructor* and returns its index; otherwise returns -1.

Note that the *constructor* has to be in normalized form, as returned by [normalizedSignature](#normalizedSignature)().

This function was introduced in Qt 4.5.

**另请参阅：**[constructor](#constructor)(), [constructorCount](#constructorCount)(), and [normalizedSignature](#normalizedSignature)().

----

### int QMetaObject::indexOfEnumerator(const char **name*) const

Finds enumerator *name* and returns its index; otherwise returns -1.

**另请参阅：**[enumerator](#enumerator)(), [enumeratorCount](#enumeratorCount)(), and [enumeratorOffset](#enumeratorOffset)().

----

### int QMetaObject::indexOfMethod(const char **method*) const

Finds *method* and returns its index; otherwise returns -1.

Note that the *method* has to be in normalized form, as returned by [normalizedSignature](#normalizedSignature)().

**另请参阅：**[method](#method)(), [methodCount](#methodCount)(), [methodOffset](#methodOffset)(), and [normalizedSignature](#normalizedSignature)().

----

### int QMetaObject::indexOfProperty(const char **name*) const

Finds property *name* and returns its index; otherwise returns -1.

**另请参阅：**[property](#property)(), [propertyCount](#propertyCount)(), and [propertyOffset](#propertyOffset)().

----

### int QMetaObject::indexOfSignal(const char **signal*) const

Finds *signal* and returns its index; otherwise returns -1.

This is the same as [indexOfMethod](#indexOfMethod)(), except that it will return -1 if the method exists but isn't a signal.

Note that the *signal* has to be in normalized form, as returned by [normalizedSignature](#normalizedSignature)().

**另请参阅：**[indexOfMethod](#indexOfMethod)(), [normalizedSignature](#normalizedSignature)(), [method](#method)(), [methodCount](#methodCount)(), and [methodOffset](#methodOffset)().

----

### int QMetaObject::indexOfSlot(const char **slot*) const

Finds *slot* and returns its index; otherwise returns -1.

This is the same as [indexOfMethod](#indexOfMethod)(), except that it will return -1 if the method exists but isn't a slot.

**另请参阅：**[indexOfMethod](#indexOfMethod)(), [method](#method)(), [methodCount](#methodCount)(), and [methodOffset](#methodOffset)().

----

### bool QMetaObject::inherits(const [QMetaObject]() **metaObject*) const

Returns true if the class described by this [QMetaObject]() inherits the type described by *metaObject*; otherwise returns false.

A type is considered to inherit itself.

This function was introduced in Qt 5.7.

----

### [static] bool QMetaObject::invokeMethod([QObject](qobject.html) **obj*, const char **member*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *type*, [QGenericReturnArgument](qgenericreturnargument.html) *ret*, [QGenericArgument](qgenericargument.html) *val0* = QGenericArgument(nullptr), [QGenericArgument](qgenericargument.html) *val1* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val2* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val3* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val4* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val5* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val6* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val7* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val8* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val9* = QGenericArgument())

Invokes the *member* (a signal or a slot name) on the object *obj*. Returns true if the member could be invoked. Returns false if there is no such member or the parameters did not match.

The invocation can be either synchronous or asynchronous, depending on *type*:

- If *type* is [Qt::DirectConnection](qt.html#ConnectionType-enum), the member will be invoked immediately.
- If *type* is [Qt::QueuedConnection](qt.html#ConnectionType-enum), a [QEvent](qevent.html) will be sent and the member is invoked as soon as the application enters the main event loop.
- If *type* is [Qt::BlockingQueuedConnection](qt.html#ConnectionType-enum), the method will be invoked in the same way as for [Qt::QueuedConnection](qt.html#ConnectionType-enum), except that the current thread will block until the event is delivered. Using this connection type to communicate between objects in the same thread will lead to deadlocks.
- If *type* is [Qt::AutoConnection](qt.html#ConnectionType-enum), the member is invoked synchronously if *obj* lives in the same thread as the caller; otherwise it will invoke the member asynchronously.

The return value of the *member* function call is placed in *ret*. If the invocation is asynchronous, the return value cannot be evaluated. You can pass up to ten arguments (*val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8*, and *val9*) to the *member* function.

[QGenericArgument](qgenericargument.html) and [QGenericReturnArgument](qgenericreturnargument.html) are internal helper classes. Because signals and slots can be dynamically invoked, you must enclose the arguments using the [Q_ARG](#Q_ARG)() and [Q_RETURN_ARG](#Q_RETURN_ARG)() macros. [Q_ARG](#Q_ARG)() takes a type name and a const reference of that type; [Q_RETURN_ARG](#Q_RETURN_ARG)() takes a type name and a non-const reference.

You only need to pass the name of the signal or slot to this function, not the entire signature. For example, to asynchronously invoke the [quit()](qthread.html#quit) slot on a [QThread](qthread.html), use the following code:

```
 QMetaObject::invokeMethod(thread, "quit",
                           Qt::QueuedConnection);
```

With asynchronous method invocations, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message

```
 QMetaObject::invokeMethod: Unable to handle unregistered datatype 'MyType'
```

call [qRegisterMetaType](qmetatype.html#qRegisterMetaType-1)() to register the data type before you call invokeMethod().

To synchronously invoke the compute(QString, int, double) slot on some arbitrary object obj retrieve its return value:

```
 QString retVal;
 QMetaObject::invokeMethod(obj, "compute", Qt::DirectConnection,
                           Q_RETURN_ARG(QString, retVal),
                           Q_ARG(QString, "sqrt"),
                           Q_ARG(int, 42),
                           Q_ARG(double, 9.7));
```

If the "compute" slot does not take exactly one [QString](qstring.html), one int and one double in the specified order, the call will fail.

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

**另请参阅：**[Q_ARG](#Q_ARG)(), [Q_RETURN_ARG](#Q_RETURN_ARG)(), [qRegisterMetaType](qmetatype.html#qRegisterMetaType-1)(), and [QMetaMethod::invoke](../../M/QMetaMethod/QMetaMethod.md#invoke)().

----

### [static] bool QMetaObject::invokeMethod([QObject](qobject.html) **obj*, const char **member*, [QGenericReturnArgument](qgenericreturnargument.html) *ret*, [QGenericArgument](qgenericargument.html) *val0* = QGenericArgument(0), [QGenericArgument](qgenericargument.html) *val1* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val2* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val3* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val4* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val5* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val6* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val7* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val8* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val9* = QGenericArgument())

This function overloads invokeMethod().

This overload always invokes the member using the connection type [Qt::AutoConnection](qt.html#ConnectionType-enum).

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

----

### [static] bool QMetaObject::invokeMethod([QObject](qobject.html) **obj*, const char **member*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *type*, [QGenericArgument](qgenericargument.html) *val0* = QGenericArgument(0), [QGenericArgument](qgenericargument.html) *val1* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val2* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val3* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val4* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val5* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val6* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val7* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val8* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val9* = QGenericArgument())

This function overloads invokeMethod().

This overload can be used if the return value of the member is of no interest.

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

----

### [static] bool QMetaObject::invokeMethod([QObject](qobject.html) **obj*, const char **member*, [QGenericArgument](qgenericargument.html) *val0* = QGenericArgument(0), [QGenericArgument](qgenericargument.html) *val1* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val2* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val3* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val4* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val5* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val6* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val7* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val8* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val9* = QGenericArgument())

This function overloads invokeMethod().

This overload invokes the member using the connection type [Qt::AutoConnection](qt.html#ConnectionType-enum) and ignores return values.

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

----

### [static] template <typename Functor, typename FunctorReturnType> bool QMetaObject::invokeMethod([QObject](qobject.html) **context*, Functor *function*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *type* = Qt::AutoConnection, FunctorReturnType **ret* = nullptr)

This is an overloaded function.

Invokes the *function* in the event loop of *context*. *function* can be a functor or a pointer to a member function. Returns true if the function could be invoked. Returns false if there is no such function or the parameters did not match. The return value of the function call is placed in *ret*.

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

This function was introduced in Qt 5.10.

----

### [static] template <typename Functor, typename FunctorReturnType> bool QMetaObject::invokeMethod([QObject](qobject.html) **context*, Functor *function*, FunctorReturnType **ret*)

This is an overloaded function.

Invokes the *function* in the event loop of *context* using the connection type [Qt::AutoConnection](qt.html#ConnectionType-enum). *function* can be a functor or a pointer to a member function. Returns true if the function could be invoked. Returns false if there is no such member or the parameters did not match. The return value of the function call is placed in *ret*.

Note: This function is [thread-safe](../qtdoc/threads-reentrancy.html).

This function was introduced in Qt 5.10.

----

### [Q](../../M/QMetaMethod/QMetaMethod.md)MetaMethod QMetaObject::method(int *index*) const

Returns the meta-data for the method with the given *index*.

**另请参阅：**[methodCount](#methodCount)(), [methodOffset](#methodOffset)(), and [indexOfMethod](#indexOfMethod)().

----

### int QMetaObject::methodCount() const

Returns the number of methods in this class, including the number of methods provided by each base class. These include signals and slots as well as normal member functions.

Use code like the following to obtain a [QStringList](qstringlist.html) containing the methods specific to a given class:

```
 const QMetaObject* metaObject = obj->metaObject();
 QStringList methods;
 for(int i = metaObject->methodOffset(); i < metaObject->methodCount(); ++i)
     methods << QString::fromLatin1(metaObject->method(i).methodSignature());
```

**另请参阅：**[method](#method)(), [methodOffset](#methodOffset)(), and [indexOfMethod](#indexOfMethod)().

----

### int QMetaObject::methodOffset() const

Returns the method offset for this class; i.e. the index position of this class's first member function.

The offset is the sum of all the methods in the class's superclasses (which is always positive since [QObject](qobject.html) has the deleteLater() slot and a destroyed() signal).

**另请参阅：**[method](#method)(), [methodCount](#methodCount)(), and [indexOfMethod](#indexOfMethod)().

----

### [Q](qobject.html)Object *QMetaObject::newInstance([QGenericArgument](qgenericargument.html) *val0* = QGenericArgument(nullptr), [QGenericArgument](qgenericargument.html) *val1* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val2* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val3* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val4* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val5* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val6* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val7* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val8* = QGenericArgument(), [QGenericArgument](qgenericargument.html) *val9* = QGenericArgument()) const

Constructs a new instance of this class. You can pass up to ten arguments (*val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8*, and *val9*) to the constructor. Returns the new object, or nullptr if no suitable constructor is available.

Note that only constructors that are declared with the [Q_INVOKABLE](qobject.html#Q_INVOKABLE) modifier are made available through the meta-object system.

This function was introduced in Qt 4.5.

**另请参阅：**[Q_ARG](#Q_ARG)() and [constructor](#constructor)().

----

### [static] [QByteArray](qbytearray.html) QMetaObject::normalizedSignature(const char **method*)

Normalizes the signature of the given *method*.

Qt uses normalized signatures to decide whether two given signals and slots are compatible. Normalization reduces whitespace to a minimum, moves 'const' to the front where appropriate, removes 'const' from value types and replaces const references with values.

**另请参阅：**[checkConnectArgs](#checkConnectArgs)() and [normalizedType](#normalizedType)().

----

### [static] [QByteArray](qbytearray.html) QMetaObject::normalizedType(const char **type*)

Normalizes a *type*.

See [QMetaObject::normalizedSignature](#normalizedSignature)() for a description on how Qt normalizes.

Example:

```
 QByteArray normType = QMetaObject::normalizedType(" int    const  *");
 // normType is now "const int*"
```

This function was introduced in Qt 4.2.

**另请参阅：**[normalizedSignature](#normalizedSignature)().

----

### [Q](qmetaproperty.html)MetaProperty QMetaObject::property(int *index*) const

Returns the meta-data for the property with the given *index*. If no such property exists, a null [QMetaProperty](qmetaproperty.html) is returned.

**另请参阅：**[propertyCount](#propertyCount)(), [propertyOffset](#propertyOffset)(), and [indexOfProperty](#indexOfProperty)().

----

### int QMetaObject::propertyCount() const

Returns the number of properties in this class, including the number of properties provided by each base class.

Use code like the following to obtain a [QStringList](qstringlist.html) containing the properties specific to a given class:

```
 const QMetaObject* metaObject = obj->metaObject();
 QStringList properties;
 for(int i = metaObject->propertyOffset(); i < metaObject->propertyCount(); ++i)
     properties << QString::fromLatin1(metaObject->property(i).name());
```

**另请参阅：**[property](#property)(), [propertyOffset](#propertyOffset)(), and [indexOfProperty](#indexOfProperty)().

----

### int QMetaObject::propertyOffset() const

Returns the property offset for this class; i.e. the index position of this class's first property.

The offset is the sum of all the properties in the class's superclasses (which is always positive since [QObject](qobject.html) has the name() property).

**另请参阅：**[property](#property)(), [propertyCount](#propertyCount)(), and [indexOfProperty](#indexOfProperty)().

----

### const [QMetaObject]() *QMetaObject::superClass() const

Returns the meta-object of the superclass, or nullptr if there is no such object.

**另请参阅：**[className](#className)().

----

### [Q](qmetaproperty.html)MetaProperty QMetaObject::userProperty() const

Returns the property that has the USER flag set to true.

This function was introduced in Qt 4.2.

**另请参阅：**[QMetaProperty::isUser](qmetaproperty.html#isUser)().



## 宏文档

### [Q](qgenericargument.html)GenericArgument Q_ARG(*Type*, const Type &*value*)

This macro takes a *Type* and a *value* of that type and returns a [QGenericArgument](qgenericargument.html) object that can be passed to [QMetaObject::invokeMethod](#invokeMethod)().

**另请参阅：**[Q_RETURN_ARG](#Q_RETURN_ARG)().

----

### [Q](qgenericreturnargument.html)GenericReturnArgument Q_RETURN_ARG(*Type*, Type &*value*)

This macro takes a *Type* and a non-const reference to a *value* of that type and returns a [QGenericReturnArgument](qgenericreturnargument.html) object that can be passed to [QMetaObject::invokeMethod](#invokeMethod)().

**另请参阅：**[Q_ARG](#Q_ARG)(). 

© 2020 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners.
The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](http://www.gnu.org/licenses/fdl.html) as published by the Free Software Foundation.
Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners. 