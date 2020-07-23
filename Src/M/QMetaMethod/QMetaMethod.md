# QMetaMethod 类

QMetaMethod 类提供了对应一个成员函数的元数据。[更多内容...](#详细描述)

| 属性   | 内容                     |
| ------ | ------------------------ |
| 头文件 | `#include <QMetaMethod>` |
| qmake  | `QT += core`             |



## 公共类型

| 类型 | 名称                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[Access](#enum-qmetamethodaccess)** { Private, Protected, Public } |
| enum | **[MethodType](#enum-qmetamethodmethodtype)** { Method, Signal, Slot, Constructor } |



## 公共成员函数

| 返回类型                | 函数                                                         |
| ----------------------- | ------------------------------------------------------------ |
| QMetaMethod::Access     | **[access](#qmetamethodaccess-qmetamethodaccess-const)**() const |
| bool                    | **[invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(QObject \**object*, Qt::ConnectionType *connectionType*, QGenericReturnArgument *returnValue*, QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[invoke](#bool-qmetamethodinvokeqobject-object-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(QObject \**object*, QGenericReturnArgument *returnValue*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(QObject \**object*, Qt::ConnectionType *connectionType*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[invoke](#bool-qmetamethodinvokeqobject-object-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(QObject \**object*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[invokeOnGadget](#bool-qmetamethodinvokeongadgetvoid-gadget-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(void \**gadget*, QGenericReturnArgument *returnValue*, QGenericArgument *val0* = QGenericArgument(nullptr), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[invokeOnGadget](#bool-qmetamethodinvokeongadgetvoid-gadget-qgenericargument-val0--qgenericargument0-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)**(void \**gadget*, QGenericArgument *val0* = QGenericArgument(0), QGenericArgument *val1* = QGenericArgument(), QGenericArgument *val2* = QGenericArgument(), QGenericArgument *val3* = QGenericArgument(), QGenericArgument *val4* = QGenericArgument(), QGenericArgument *val5* = QGenericArgument(), QGenericArgument *val6* = QGenericArgument(), QGenericArgument *val7* = QGenericArgument(), QGenericArgument *val8* = QGenericArgument(), QGenericArgument *val9* = QGenericArgument()) const |
| bool                    | **[isValid](#bool-qmetamethodisvalid-const)**() const        |
| int                     | **[methodIndex](#int-qmetamethodmethodindex-const)**() const |
| QByteArray              | **[methodSignature](#qbytearray-qmetamethodmethodsignature-const)**() const |
| QMetaMethod::MethodType | **[methodType](#qmetamethodmethodtype-qmetamethodmethodtype-const)**() const |
| QByteArray              | **[name](#qbytearray-qmetamethodname-const)**() const        |
| int                     | **[parameterCount](#int-qmetamethodparametercount-const)**() const |
| QList\<QByteArray\>     | **[parameterNames](#qlistqbytearray-qmetamethodparameternames-const)**() const |
| int                     | **[parameterType](#int-qmetamethodparametertypeint-index-const)**(int *index*) const |
| QList\<QByteArray\>     | **[parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)**() const |
| int                     | **[returnType](#int-qmetamethodreturntype-const)**() const   |
| int                     | **[revision](#int-qmetamethodrevision-const)**() const       |
| const char *            | **[tag](#const-char-qmetamethodtag-const)**() const          |
| const char *            | **[typeName](#const-char-qmetamethodtypename-const)**() const |



## 静态公共成员

| 返回类型    | 函数                                                         |
| ----------- | ------------------------------------------------------------ |
| QMetaMethod | **[fromSignal](#static-template-typename-pointertomemberfunction-qmetamethod-qmetamethodfromsignalpointertomemberfunction-signal)**(PointerToMemberFunction *signal*) |



## 相关非成员函数

| 返回类型 | 函数                                                         |
| -------- | ------------------------------------------------------------ |
| bool     | **[operator!=](#bool-operatorconst-qmetamethod-m1-const-qmetamethod-m2)**(const QMetaMethod &*m1*, const QMetaMethod &*m2*) |
| bool     | **[operator==](#bool-operatorconst-qmetamethod-m1-const-qmetamethod-m2)**(const QMetaMethod &*m1*, const QMetaMethod &*m2*) |



## 宏

**[Q_METAMETHOD_INVOKE_MAX_ARGS](#qmetamethodinvokemaxargs)**



## 详细描述

QMetaMethod 类具有一个 [methodType](#qmetamethodmethodtype-qmetamethodmethodtype-const)()、一个 [methodSignature](#qbytearray-qmetamethodmethodsignature-const)()、一组 [parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() 和 [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)()、返回值的 [typeName](#const-char-qmetamethodtypename-const)()、一个 [tag](#const-char-qmetamethodtag-const)()、一个 [access](#qmetamethodaccess-qmetamethodaccess-const)() 描述符。可以通过 [invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)() 来执行任意 [QObject](../../O/QObject/QObject.md) 的方法。

**另请参阅：**[QMetaObject](../../M/QMetaObject/QMetaObject.md)、[QMetaEnum](../../M/QMetaEnum/QMetaEnum.md)、[QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) 和 [Qt 属性系统](../../P/The_Property_System/The_Property_System.md)。



## 成员类型文档

### enum QMetaMethod::Access

此枚举描述某方法的访问权限，遵循 C++ 相关公约This enum describes the access level of a method, following the conventions used in C++.

| 常量                     | 数值 |
| ------------------------ | ---- |
| `QMetaMethod::Private`   | `0`  |
| `QMetaMethod::Protected` | `1`  |
| `QMetaMethod::Public`    | `2`  |

----

### enum QMetaMethod::MethodType

| 常量                       | 数值 | 描述                     |
| -------------------------- | ---- | ------------------------ |
| `QMetaMethod::Method`      | `0`  | 该函数是普通的成员函数。 |
| `QMetaMethod::Signal`      | `1`  | 该函数是信号函数。       |
| `QMetaMethod::Slot`        | `2`  | 该函数是槽函数。         |
| `QMetaMethod::Constructor` | `3`  | 该函数是构造函数。       |



## 成员函数文档

### [QMetaMethod::Access](#enum-qmetamethodaccess) QMetaMethod::access() const

返回该方法的访问权限(`private`、`protected` 或 `public)。

**注意：**信号永远是公共的，但应将此认为是实现细节。在类外发射该类的信号通常是个坏主意。

**另请参阅：** [methodType](#qmetamethodmethodtype-qmetamethodmethodtype-const)()。

### `[static] `template <typename PointerToMemberFunction> QMetaMethod QMetaMethod::fromSignal(PointerToMemberFunction *signal*)

Returns the meta-method that corresponds to the given *signal*, or an invalid [QMetaMethod](QMetaMethod.md) if *signal* is not a signal of the class.

Example:

```
QMetaMethod destroyedSignal = QMetaMethod::fromSignal(&QObject::destroyed);
```

This function was introduced in Qt 5.0.

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) **object*, [Qt::ConnectionType](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum) *connectionType*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

Invokes this method on the object *object*. Returns `true` if the member could be invoked. Returns `false` if there is no such member or the parameters did not match.

The invocation can be either synchronous or asynchronous, depending on the *connectionType*:

- If *connectionType* is [Qt::DirectConnection](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum), the member will be invoked immediately.
- If *connectionType* is [Qt::QueuedConnection](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum), a [QEvent](../../E/QEvent/QEvent.md) will be posted and the member is invoked as soon as the application enters the main event loop.
- If *connectionType* is [Qt::AutoConnection](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum), the member is invoked synchronously if *object* lives in the same thread as the caller; otherwise it will invoke the member asynchronously.

The return value of this method call is placed in *returnValue*. If the invocation is asynchronous, the return value cannot be evaluated. You can pass up to ten arguments (*val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8* 和 *val9*) to this method call.

[QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) and [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) are internal helper classes. Because signals and slots can be dynamically invoked, you must enclose the arguments using the [Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)() and [Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)() macros. [Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)() takes a type name and a const reference of that type; [Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)() takes a type name and a non-const reference.

To asynchronously invoke the [animateClick()](../../A/QAbstractButton/QAbstractButton.md#slot-void-qabstractbuttonanimateclickint-msec--100) slot on a [QPushButton](../../P/QPushButton/QPushButton.md):

```
int methodIndex = pushButton->metaObject()->indexOfMethod("animateClick()");
QMetaMethod method = metaObject->method(methodIndex);
method.invoke(pushButton, Qt::QueuedConnection);
```

With asynchronous method invocations, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to  use a queued connection and get the error message

```
QMetaMethod::invoke: Unable to handle unregistered datatype 'MyType'
```

call [qRegisterMetaType](../../M/QMetaType/QMetaType.md#template-typename-t-int-qregistermetatype)() to register the data type before you call QMetaMethod::invoke().

To synchronously invoke the `compute(QString, int, double)` slot on some arbitrary object `obj` retrieve its return value:

```
QString retVal;
QByteArray normalizedSignature = QMetaObject::normalizedSignature("compute(QString, int, double)");
int methodIndex = obj->metaObject()->indexOfMethod(normalizedSignature);
QMetaMethod method = obj->metaObject()->method(methodIndex);
method.invoke(obj,
              Qt::DirectConnection,
              Q_RETURN_ARG(QString, retVal),
              Q_ARG(QString, "sqrt"),
              Q_ARG(int, 42),
              Q_ARG(double, 9.7));
```

[QMetaObject::normalizedSignature](https://doc.qt.io/qt-5/qmetaobject.html#normalizedSignature)() is used here to ensure that the format of the signature is what invoke() expects. E.g. extra whitespace is removed.

If the "compute" slot does not take exactly one [QString](../../S/QString/QString.md), one int and one double in the specified order, the call will fail.

**Warning:** this method will not test the validity of the arguments: *object* must be an instance of the class of the [QMetaObject](../../M/QMetaObject/QMetaObject.md) of which this [QMetaMethod](QMetaMethod.md) has been constructed with. The arguments must have the same type as the ones expected by the method, else, the behaviour is undefined.

**另请参阅：** [Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)(), [Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)(), [qRegisterMetaType](../../M/QMetaType/QMetaType.md#template-typename-t-int-qregistermetatype)() 和 [QMetaObject::invokeMethod](https://doc.qt.io/qt-5/qmetaobject.html#invokeMethod)().

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) **object*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

This function overloads invoke().

This overload always invokes this method using the connection type [Qt::AutoConnection](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum).

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) **object*, [Qt::ConnectionType](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum) *connectionType*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

This function overloads invoke().

This overload can be used if the return value of the member is of no interest.

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) **object*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

This function overloads invoke().

This overload invokes this method using the connection type [Qt::AutoConnection](https://doc.qt.io/qt-5/qt.html#ConnectionType-enum) and ignores return values.

### bool QMetaMethod::invokeOnGadget(void **gadget*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

Invokes this method on a [Q_GADGET](../../O/QObject/QObject.md#qgadget). Returns `true` if the member could be invoked. Returns `false` if there is no such member or the parameters did not match.

The pointer *gadget* must point to an instance of the gadget class.

The invocation is always synchronous.

The return value of this method call is placed in *returnValue*. You can pass up to ten arguments (*val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8* 和 *val9*) to this method call.

**Warning:** this method will not test the validity of the arguments: *gadget* must be an instance of the class of the [QMetaObject](../../M/QMetaObject/QMetaObject.md) of which this [QMetaMethod](QMetaMethod.md) has been constructed with. The arguments must have the same type as the ones expected by the method, else, the behavior is undefined.

This function was introduced in Qt 5.5.

**另请参阅：** [Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)(), [Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)(), [qRegisterMetaType](../../M/QMetaType/QMetaType.md#template-typename-t-int-qregistermetatype)() 和 [QMetaObject::invokeMethod](https://doc.qt.io/qt-5/qmetaobject.html#invokeMethod)().

### bool QMetaMethod::invokeOnGadget(void **gadget*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

This is an overloaded function.

This overload invokes this method for a *gadget* and ignores return values.

This function was introduced in Qt 5.5.

### bool QMetaMethod::isValid() const

Returns `true` if this method is valid (can be introspected and invoked), otherwise returns `false`.

This function was introduced in Qt 5.0.

### int QMetaMethod::methodIndex() const

Returns this method's index.

This function was introduced in Qt 4.6.

### [QByteArray](../../B/QByteArray/QByteArray.md) QMetaMethod::methodSignature() const

Returns the signature of this method (e.g., `setValue(double)`).

This function was introduced in Qt 5.0.

**另请参阅：** [parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() and [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)().

### [QMetaMethod::MethodType](#enum-qmetamethodmethodtype) QMetaMethod::methodType() const

Returns the type of this method (signal, slot, or method).

**另请参阅：** [access](#qmetamethodaccess-qmetamethodaccess-const)().

### [QByteArray](../../B/QByteArray/QByteArray.md) QMetaMethod::name() const

Returns the name of this method.

This function was introduced in Qt 5.0.

**另请参阅：** [methodSignature](#qbytearray-qmetamethodmethodsignature-const)() and [parameterCount](#int-qmetamethodparametercount-const)().

### int QMetaMethod::parameterCount() const

Returns the number of parameters of this method.

This function was introduced in Qt 5.0.

**另请参阅：** [parameterType](#int-qmetamethodparametertypeint-index-const)() and [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)().

### [QList](../../L/QList/QList.md)<[QByteArray](../../B/QByteArray/QByteArray.md)> QMetaMethod::parameterNames() const

Returns a list of parameter names.

**另请参阅：** [parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() and [methodSignature](#qbytearray-qmetamethodmethodsignature-const)().

### int QMetaMethod::parameterType(int *index*) const

Returns the type of the parameter at the given *index*.

The return value is one of the types that are registered with [QMetaType](../../M/QMetaType/QMetaType.md), or [QMetaType::UnknownType](../../M/QMetaType/QMetaType.md#enum-qmetatypetype) if the type is not registered.

This function was introduced in Qt 5.0.

**另请参阅：** [parameterCount](#int-qmetamethodparametercount-const)(), [returnType](#int-qmetamethodreturntype-const)() 和 [QMetaType](../../M/QMetaType/QMetaType.md).

### [QList](../../L/QList/QList.md)<[QByteArray](../../B/QByteArray/QByteArray.md)> QMetaMethod::parameterTypes() const

Returns a list of parameter types.

**另请参阅：** [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)() and [methodSignature](#qbytearray-qmetamethodmethodsignature-const)().

### int QMetaMethod::returnType() const

Returns the return type of this method.

The return value is one of the types that are registered with [QMetaType](../../M/QMetaType/QMetaType.md), or [QMetaType::UnknownType](../../M/QMetaType/QMetaType.md#enum-qmetatypetype) if the type is not registered.

This function was introduced in Qt 5.0.

**另请参阅：** [parameterType](#int-qmetamethodparametertypeint-index-const)(), [QMetaType](../../M/QMetaType/QMetaType.md) 和 [typeName](#const-char-qmetamethodtypename-const)().

### int QMetaMethod::revision() const

Returns the method revision if one was specified by [Q_REVISION](../../O/QObject/QObject.md#qrevision), otherwise returns 0.

This function was introduced in Qt 5.1.

### const char *QMetaMethod::tag() const

Returns the tag associated with this method.

Tags are special macros recognized by `moc` that make it possible to add extra information about a method.

Tag information can be added in the following way in the function declaration:

```
    // In the class MainWindow declaration
    #ifndef Q_MOC_RUN
    // define the tag text as empty, so the compiler doesn't see it
    #  define MY_CUSTOM_TAG
    #endif
    ...
    private slots:
        MY_CUSTOM_TAG void testFunc();
```

and the information can be accessed by using:

```
    MainWindow win;
    win.show();

    int functionIndex = win.metaObject()->indexOfSlot("testFunc()");
    QMetaMethod mm = win.metaObject()->method(functionIndex);
    qDebug() << mm.tag(); // prints MY_CUSTOM_TAG
```

For the moment, `moc` will extract and record all tags,  but it will not handle any of them specially. You can use the tags to  annotate your methods differently 和 treat them according to the  specific needs of your application.

**Note:** Since Qt 5.0, `moc` expands preprocessor macros, so it is necessary to surround the definition with `#ifndef` `Q_MOC_RUN`, as shown in the example above. This was not required in Qt 4. The code as shown above works with Qt 4 too.

### const char *QMetaMethod::typeName() const

Returns the return type name of this method.

**另请参阅：** [returnType](#int-qmetamethodreturntype-const)() and [QMetaType::type](../../M/QMetaType/QMetaType.md#static-int-qmetatypetypeconst-char-typename)().

## Related Non-Members

### bool operator!=(const QMetaMethod &*m1*, const QMetaMethod &*m2*)

This is an overloaded function.

Returns `true` if method *m1* is not equal to method *m2*, otherwise returns `false`.

This function was introduced in Qt 5.0.

### bool operator==(const QMetaMethod &*m1*, const QMetaMethod &*m2*)

This is an overloaded function.

Returns `true` if method *m1* is equal to method *m2*, otherwise returns `false`.

This function was introduced in Qt 5.0.

## Macro Documentation

### Q_METAMETHOD_INVOKE_MAX_ARGS

Equals maximum number of arguments available for execution of the method via [QMetaMethod::invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)()