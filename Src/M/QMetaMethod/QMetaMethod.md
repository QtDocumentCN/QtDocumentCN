# QMetaMethod 类

QMetaMethod 类提供了对应一个成员函数的元数据。[更多内容...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)

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



## 宏定义

| 宏定义                                                       |
| ------------------------------------------------------------ |
| **[Q_METAMETHOD_INVOKE_MAX_ARGS](#qmetamethodinvokemaxargs)** |



## 详细描述

QMetaMethod 类具有一个 [methodType](#qmetamethodmethodtype-qmetamethodmethodtype-const)()、一个 [methodSignature](#qbytearray-qmetamethodmethodsignature-const)()、一组 [parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() 和 [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)()、返回值的 [typeName](#const-char-qmetamethodtypename-const)()、一个 [tag](#const-char-qmetamethodtag-const)()、一个 [access](#qmetamethodaccess-qmetamethodaccess-const)() 描述符。可以通过 [invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)() 来执行任意 [QObject](../../O/QObject/QObject.md) 的方法。

**另请参阅：**[QMetaObject](../../M/QMetaObject/QMetaObject.md)、[QMetaEnum](../../M/QMetaEnum/QMetaEnum.md)、[QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) 和 [Qt 属性系统](../../P/The_Property_System/The_Property_System.md)。



## 成员类型文档

### enum QMetaMethod::Access

此枚举描述某方法的访问权限，遵循 C++ 相关公约。

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

**另请参阅：**[methodType](#qmetamethodmethodtype-qmetamethodmethodtype-const)()。

----

### *[static]* template \<typename PointerToMemberFunction\> QMetaMethod QMetaMethod::fromSignal(PointerToMemberFunction *signal*)

返回对应给定 `signal` 的元方法，若 `signal` 并非信号，则返回无效的 [QMetaMethod](QMetaMethod.md) 对象。

范例：

```cpp
QMetaMethod destroyedSignal = QMetaMethod::fromSignal(&QObject::destroyed);
```

本函数在 Qt 5.0 中被引入。

----

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) \**object*, [Qt::ConnectionType](../../Q/Qt_Namespace/Qt_Namespace.md#ConnectionType-enum) *connectionType*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

通过 `object` 对象动态调用本方法。若可被动态调用则返回 `tue`，若该对象无此方法或参数不匹配则返回 `false`。

该动态调用可以是同步或异步的，由 `connectionType` 决定：

- 若 `type` 是 [Qt::DirectConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，则该方法会被立即执行。
- 若 `type` 是 [Qt::QueuedConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，则会发送一个 [QEvent](../../E/QEvent/QEvent.md) ，该方法会在应用进入该对象所属线程的主事件循环后执行。
- 若 `type` 是 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum)，当 `object` 与调用者处于相同线程中时，该方法会被同步执行，否则会被异步执行。

返回值会被存放在 `returnvalue` 中。若调用方式是异步，则返回值无法被获取。最多可以传递十个参数 (`val0`, `val1`, `val2`, `val3`, `val4`, `val5`, `val6`, `val7`, `val8` 和 `val9`) 至本方法。

[QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) 和 [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) 是内部的辅助类。为了动态调用信号槽，您需要将参数通过 [Q_ARG](#qgenericargument-qargtype-const-type-&value)() 和 [Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)() 宏进行封装。[Q_ARG](#qgenericargument-qargtype-const-type-&value)() 接受一个类型名称和一个该类型的不可变引用；[Q_RETURN_ARG](#qgenericreturnargument-qreturnargtype-type-&value)() 接受一个类型名称和一个该类型的可变引用。

通过异步方式动态调用 [QPushButton](../../P/QPushButton/QPushButton.md) 的 [animateClick()](../../A/QAbstractButton/QAbstractButton.md#slot-void-qabstractbuttonanimateclickint-msec--100) 槽:

```cpp
int methodIndex = pushButton->metaObject()->indexOfMethod("animateClick()");
QMetaMethod method = metaObject->method(methodIndex);
method.invoke(pushButton, Qt::QueuedConnection);
```

当异步调用方法时，传递的参数必须被 Qt 的元对象系统所知悉，因为 Qt 需要在后台事件中拷贝并保存它们。如果您使用队列连接时遇到下述错误信息：

```cpp
QMetaMethod::invoke: Unable to handle unregistered datatype 'MyType'
```

则在调用 `invokeMethod`() 之前通过 [qRegisterMetaType](../../M/QMetaType/QMetaType.md#qRegisterMetaType-1)() 来注册该数据类型。

若想通过 `obj` 对象同步调用 `compute(QString, int, double)` 槽，则代码如下：

```cpp
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

此处使用了 [QMetaObject::normalizedSignature](https://doc.qt.io/qt-5/qmetaobject.html#normalizedSignature)() 来确保函数签名符合 `invoke()` 期望的格式，即将多余的空白移除。

若 `compute` 槽通过特定顺序没有完整获取到一个 [QString](../../S/QString/QString.md)、一个 `int` 和一个 `double`，则此调用会失败。

**警告：** 此方法不会验证参数的有效性，`object` 必须是创建 [QMetaMethod](QMetaMethod.md) 的 [QMetaObject](../../M/QMetaObject/QMetaObject.md) 的类型实例，参数列表必须与该方法的保持一直，否则会导致未定义行为。

**另请参阅：**[Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)()、[Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)()、[qRegisterMetaType](../../M/QMetaType/QMetaType.md#template-typename-t-int-qregistermetatype)() 和 [QMetaObject::invokeMethod](https://doc.qt.io/qt-5/qmetaobject.html#invokeMethod)()。

----

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) \**object*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

此函数是 `invoke`() 的重载。

此重载始终通过 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 调用本方法。

----

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) \**object*, [Qt::ConnectionType](../../Q/Qt_Namespace/Qt_Namespace.md#ConnectionType-enum) *connectionType*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

此函数是 `invoke`() 的重载。

此重载用于不关心对返回值的场合。

----

### bool QMetaMethod::invoke([QObject](../../O/QObject/QObject.md) \**object*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

此函数是 `invoke`() 的重载。

此重载通过 [Qt::AutoConnection](../../Q/Qt/Qt.md#ConnectionType-enum) 调用本方法，并忽略返回值。

----

### bool QMetaMethod::invokeOnGadget(void **gadget*, [QGenericReturnArgument](../../G/QGenericReturnArgument/QGenericReturnArgument.md) *returnValue*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(nullptr), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

通过 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 对象动态调用本方法。若可被动态调用则返回 `tue`，若该对象无此方法或参数不匹配则返回 `false`。

`gadget` 指针必须是 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 类的实例。

该调用始终是同步的。

返回值会被存放在 `returnvalue` 中。若调用方式是异步，则返回值无法被获取。最多可以传递十个参数 (`val0`, `val1`, `val2`, `val3`, `val4`, `val5`, `val6`, `val7`, `val8` 和 `val9`) 至本方法。

**警告：** 此方法不会验证参数的有效性，`gadget` 必须是创建 [QMetaMethod](QMetaMethod.md) 的 [QMetaObject](../../M/QMetaObject/QMetaObject.md) 的类型实例，参数列表必须与该方法的保持一直，否则会导致未定义行为。

本函数在 Qt 5.5 中被引入。

**另请参阅：**[Q_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_ARG)()、[Q_RETURN_ARG](https://doc.qt.io/qt-5/qmetaobject.html#Q_RETURN_ARG)()、[qRegisterMetaType](../../M/QMetaType/QMetaType.md#template-typename-t-int-qregistermetatype)() 和 [QMetaObject::invokeMethod](https://doc.qt.io/qt-5/qmetaobject.html#invokeMethod)()。

----

### bool QMetaMethod::invokeOnGadget(void \\**gadget*, [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val0* = QGenericArgument(0), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val1* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val2* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val3* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val4* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val5* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val6* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val7* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val8* = QGenericArgument(), [QGenericArgument](../../G/QGenericArgument/QGenericArgument.md) *val9* = QGenericArgument()) const

这是一个重载函数。

此重载函数通过 `gadget` 对象动态调用本方法，并忽略返回值。

本函数在 Qt 5.5 中被引入。

----

### bool QMetaMethod::isValid() const

若此方法有效则返回 `true`（即可被自省并动态调用），否则返回 `false`。

本函数在 Qt 5.0 中被引入。

----

### int QMetaMethod::methodIndex() const

返回本方法的索引编号。

本函数在 Qt 4.6 中被引入。

----

### [QByteArray](../../B/QByteArray/QByteArray.md) QMetaMethod::methodSignature() const

返回本方法的签名（例如 `setValue(double)`）。

本函数在 Qt 5.0 中被引入。

**另请参阅：**[parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() 和 [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)()。

----

### [QMetaMethod::MethodType](#enum-qmetamethodmethodtype) QMetaMethod::methodType() const

返回本方法的类型(`signal`、`slot`、`method` 或 `constructor`)。

**另请参阅：**[access](#qmetamethodaccess-qmetamethodaccess-const)()。

----

### [QByteArray](../../B/QByteArray/QByteArray.md) QMetaMethod::name() const

返回本方法的名字。

本函数在 Qt 5.0 中被引入。

**另请参阅：**[methodSignature](#qbytearray-qmetamethodmethodsignature-const)() 和 [parameterCount](#int-qmetamethodparametercount-const)()。

----

### int QMetaMethod::parameterCount() const

返回本方法的参数个数。

本函数在 Qt 5.0 中被引入。

**另请参阅：**[parameterType](#int-qmetamethodparametertypeint-index-const)() 和 [parameterNames](#qlistqbytearray-qmetamethodparameternames-const)()。

----

### [QList](../../L/QList/QList.md)<[QByteArray](../../B/QByteArray/QByteArray.md)> QMetaMethod::parameterNames() const

返回参数名称列表。

**另请参阅：**[parameterTypes](#qlistqbytearray-qmetamethodparametertypes-const)() 和 [methodSignature](#qbytearray-qmetamethodmethodsignature-const)()。

----

### int QMetaMethod::parameterType(int *index*) const

返回对应 `index` 的参数类型。

返回值是 [QMetaType](../../M/QMetaType/QMetaType.md) 中注册的类型之一，若该类型未被注册则返回 [QMetaType::UnknownType](../../M/QMetaType/QMetaType.md#enum-qmetatypetype)。

本函数在 Qt 5.0 中被引入。

**另请参阅：**[parameterCount](#int-qmetamethodparametercount-const)()、[returnType](#int-qmetamethodreturntype-const)() 和 [QMetaType](../../M/QMetaType/QMetaType.md)。

### [QList](../../L/QList/QList.md)<[QByteArray](../../B/QByteArray/QByteArray.md)> QMetaMethod::parameterTypes() const

返回参数类型的列表。

**另请参阅：**[parameterNames](#qlistqbytearray-qmetamethodparameternames-const)() 和 [methodSignature](#qbytearray-qmetamethodmethodsignature-const)()。

----

### int QMetaMethod::returnType() const

返回本方法返回值的类型。

返回

返回值是 [QMetaType](../../M/QMetaType/QMetaType.md) 中注册的类型之一，若该类型未被注册则返回 [QMetaType::UnknownType](../../M/QMetaType/QMetaType.md#enum-qmetatypetype)。

本函数在 Qt 5.0 中被引入。

**另请参阅：**[parameterType](#int-qmetamethodparametertypeint-index-const)()、[QMetaType](../../M/QMetaType/QMetaType.md) 和 [typeName](#const-char-qmetamethodtypename-const)()。

----

### int QMetaMethod::revision() const

返回通过 [Q_REVISION](../../O/QObject/QObject.md#qrevision) 注明的版本，若未注明则返回 `0`。

本函数在 Qt 5.1 中被引入。

----

### const char *QMetaMethod::tag() const

返回与本方法关联的标签。

标签在此处指的是可以被 `moc` 识别的特定宏，用于为方法添加附加信息。

标签信息可以用如下方式添加到函数声明中：

```cpp
    // 在 MainWindow 类声明中
    #ifndef Q_MOC_RUN
    // 将标签内容定义为空，以确保对编译器不可见
    #  define MY_CUSTOM_TAG
    #endif
    ...
    private slots:
        MY_CUSTOM_TAG void testFunc();
```

相关信息可通过如下方式获取：

```cpp
    MainWindow win;
    win.show();

    int functionIndex = win.metaObject()->indexOfSlot("testFunc()");
    QMetaMethod mm = win.metaObject()->method(functionIndex);
    qDebug() << mm.tag(); // 将打印 MY_CUSTOM_TAG
```

此时，`moc` 会提取并记录所有标签，但不会对它们做任何特殊处理。您可以用标签来标注不同的方法，并在您的应用中通过特定的用途来使用它们。

**注意：** 自 Qt 5.0 开始，`moc` 会展开预编译宏，所以必须将标签定义包含在 `#ifndef` `Q_MOC_RUN` 中，正如上文范例。这在 Qt 4 中不是必要的，但上述代码在 Qt 4 中同样也能生效。

----

### const char *QMetaMethod::typeName() const

返回本方法的返回类型名称。

**另请参阅：**[returnType](#int-qmetamethodreturntype-const)() 和 [QMetaType::type](../../M/QMetaType/QMetaType.md#static-int-qmetatypetypeconst-char-typename)()。



## 相关非成员函数

### bool operator!=(const QMetaMethod &*m1*, const QMetaMethod &*m2*)

这是一个重载函数。

若 `m1` 与 `m2` 不相等则返回 `true`，否则返回 `false`。

本函数在 Qt 5.0 中被引入。

----

### bool operator==(const QMetaMethod &*m1*, const QMetaMethod &*m2*)

这是一个重载函数。

若 `m1` 与 `m2` 相等则返回 `true`，否则返回 `false`。

本函数在 Qt 5.0 中被引入。



## 宏定义文档

### Q_METAMETHOD_INVOKE_MAX_ARGS

此宏的数值等于通过 [QMetaMethod::invoke](#bool-qmetamethodinvokeqobject-object-qtconnectiontype-connectiontype-qgenericreturnargument-returnvalue-qgenericargument-val0--qgenericargumentnullptr-qgenericargument-val1--qgenericargument-qgenericargument-val2--qgenericargument-qgenericargument-val3--qgenericargument-qgenericargument-val4--qgenericargument-qgenericargument-val5--qgenericargument-qgenericargument-val6--qgenericargument-qgenericargument-val7--qgenericargument-qgenericargument-val8--qgenericargument-qgenericargument-val9--qgenericargument-const)() 执行方法时，可以传递的最大参数个数。
