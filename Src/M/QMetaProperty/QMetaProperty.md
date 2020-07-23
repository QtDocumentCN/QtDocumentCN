# QMetaProperty 类

QMetaProperty 类提供了对应一条属性的元数据。[更多内容...](#详细描述)

| 属性   | 内容                       |
| ------ | -------------------------- |
| 头文件 | `#include <QMetaProperty>` |
| qmake: | `QT += core`               |



## 公共成员函数

| 返回类型       | 函数                                                         |
| -------------- | ------------------------------------------------------------ |
| QMetaEnum      | **[enumerator](#qmetaenum-qmetapropertyenumerator-const)**() const |
| bool           | **[hasNotifySignal](#bool-qmetapropertyhasnotifysignal-const)**() const |
| bool           | **[isConstant](#bool-qmetapropertyisconstant-const)**() const |
| bool           | **[isDesignable](#bool-qmetapropertyisdesignableconst-qobject-object--nullptr-const)**(const QObject \**object* = nullptr) const |
| bool           | **[isEnumType](#bool-qmetapropertyisenumtype-const)**() const |
| bool           | **[isFinal](#bool-qmetapropertyisfinal-const)**() const      |
| bool           | **[isFlagType](#bool-qmetapropertyisflagtype-const)**() const |
| bool           | **[isReadable](#bool-qmetapropertyisreadable-const)**() const |
| bool           | **[isRequired](#bool-qmetapropertyisrequired-const)**() const |
| bool           | **[isResettable](#bool-qmetapropertyisresettable-const)**() const |
| bool           | **[isScriptable](#bool-qmetapropertyisscriptableconst-qobject-object--nullptr-const)**(const QObject \**object* = nullptr) const |
| bool           | **[isStored](#bool-qmetapropertyisstoredconst-qobject-object--nullptr-const)**(const QObject \**object* = nullptr) const |
| bool           | **[isUser](#bool-qmetapropertyisuserconst-qobject-object--nullptr-const)**(const QObject \**object* = nullptr) const |
| bool           | **[isValid](#bool-qmetapropertyisvalid-const)**() const      |
| bool           | **[isWritable](#bool-qmetapropertyiswritable-const)**() const |
| const char *   | **[name](#const-char-qmetapropertyname-const)**() const      |
| QMetaMethod    | **[notifySignal](#qmetamethod-qmetapropertynotifysignal-const)**() const |
| int            | **[notifySignalIndex](#int-qmetapropertynotifysignalindex-const)**() const |
| int            | **[propertyIndex](#int-qmetapropertypropertyindex-const)**() const |
| QVariant       | **[read](#qvariant-qmetapropertyreadconst-qobject-object-const)**(const QObject \**object*) const |
| QVariant       | **[readOnGadget](#qvariant-qmetapropertyreadongadgetconst-void-gadget-const)**(const void \**gadget*) const |
| int            | **[relativePropertyIndex](#int-qmetapropertyrelativepropertyindex-const)**() const |
| bool           | **[reset](#bool-qmetapropertyresetqobject-object-const)**(QObject \**object*) const |
| bool           | **[resetOnGadget](#bool-qmetapropertyresetongadgetvoid-gadget-const)**(void \**gadget*) const |
| int            | **[revision](#int-qmetapropertyrevision-const)**() const     |
| QVariant::Type | **[type](#qvarianttype-qmetapropertytype-const)**() const    |
| const char *   | **[typeName](#const-char-qmetapropertytypename-const)**() const |
| int            | **[userType](#int-qmetapropertyusertype-const)**() const     |
| bool           | **[write](#bool-qmetapropertywriteqobject-object-const-qvariant-value-const)**(QObject \**object*, const QVariant &*value*) const |
| bool           | **[writeOnGadget](#bool-qmetapropertywriteongadgetvoid-gadget-const-qvariant-value-const)**(void \**gadget*, const QVariant &*value*) const |



## 详细描述

属性元数据可通过对象的元对象获取。详见 [QMetaObject::property](https://doc.qt.io/qt-5/qmetaobject.html#property)() 和 [QMetaObject::propertyCount](https://doc.qt.io/qt-5/qmetaobject.html#propertyCount)()。



### 属性元数据

属性具有 [name](#const-char-qmetapropertyname-const)() 和 [type](#qvarianttype-qmetapropertytype-const)()，并且有不同的成员来表示其外在表现：[isReadable](#bool-qmetapropertyisreadable-const)()、[isWritable](#bool-qmetapropertyiswritable-const)()、[isDesignable](#bool-qmetapropertyisdesignableconst-qobject-object--nullptr-const)()、[isScriptable](#bool-qmetapropertyisscriptableconst-qobject-object--nullptr-const)()、[revision](#int-qmetapropertyrevision-const)() 和 [isStored](#bool-qmetapropertyisstoredconst-qobject-object--nullptr-const)()。

若该属性是枚举变量，则 [isEnumType](#bool-qmetapropertyisenumtype-const)() 返回 `true`；若该属性是枚举，同时也是标志位（即可通过**或**运算合并多个值），则 [isEnumType](#bool-qmetapropertyisenumtype-const)() 和 [isFlagType](#bool-qmetapropertyisflagtype-const)() 都返回 `true`。这些类型的枚举值可以通过 [enumerator](#qmetaenum-qmetapropertyenumerator-const)() 查询。

属性的值通过 [read](#qvariant-qmetapropertyreadconst-qobject-object-const)()、[write](#bool-qmetapropertywriteqobject-object-const-qvariant-value-const)() 和 [reset](#bool-qmetapropertyresetqobject-object-const)()来获取或设置，也可以通过 [QObject](../../O/QObject/QObject.md) 的 get 和 set 函数来操作，详见 [QObject::setProperty](../../O/QObject/QObject.md#bool-qobjectsetpropertyconst-char-name-const-qvariant-value)() 和 [QObject::property](../../O/QObject/QObject.md#qvariant-qobjectpropertyconst-char-name-const)()。



### 拷贝与赋值

QMetaProperty 对象可以通过传值方式拷贝，与此同时，每份副本内部都会指向相同的属性元数据。

**另请参阅：**[QMetaObject](../../M/QMetaObject/QMetaObject.md)，[QMetaEnum](../../M/QMetaEnum/QMetaEnum.md)，[QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) 和 [Qt 属性系统](../../P/The_Property_System/The_Property_System.md)。



## 成员函数文档

### [QMetaEnum](../../M/QMetaEnum/QMetaEnum.md) QMetaProperty::enumerator() const

若该属性是枚举类型，则返回对应的枚举器，否则返回未定义值。

**另请参阅：**[isEnumType](#bool-qmetapropertyisenumtype-const)() 和 [isFlagType](#bool-qmetapropertyisflagtype-const)()。

----

### bool QMetaProperty::hasNotifySignal() const

若该属性有对应的通知信号则返回 `true`，否则返回 `false`。

**另请参阅：**[notifySignal](#qmetamethod-qmetapropertynotifysignal-const)()。

----

### bool QMetaProperty::isConstant() const

若该属性在 `Q_PROPERTY()`' 中被标记为 `CONSTANT` 则返回 `true`，否则返回 `false`。

本函数在 Qt 4.6 中被引入。

----

### bool QMetaProperty::isDesignable(const [QObject](../../O/QObject/QObject.md) \**object* = nullptr) const

若该属性可被设计师(Qt Designer)编辑则返回 `true`，否则返回 `false`。

若 `object` 未被指定，则当 `Q_PROPERTY()` 的 `DESIGNABLE` 标记被指定为 `false`时，此函数返回 `false` ；其它情况下返回 `true`（若该标记被指定为 `true`，或指定为某个函数，或指定为表达式）。

**另请参阅：**[isScriptable](#bool-qmetapropertyisscriptableconst-qobject-object--nullptr-const)() 和 [isStored](#bool-qmetapropertyisstoredconst-qobject-object--nullptr-const)()。

----

### bool QMetaProperty::isEnumType() const

若该属性是枚举类型则返回 `true`，否则返回 `false`。

**另请参阅：**[enumerator](#qmetaenum-qmetapropertyenumerator-const)() 和 [isFlagType](#bool-qmetapropertyisflagtype-const)()。

----

### bool QMetaProperty::isFinal() const

若该属性在 `Q_PROPERTY()` 中被标记为 `FINAL` 则返回 `true`，否则返回 `false`。

本函数在 Qt 4.6 中被引入。

----

### bool QMetaProperty::isFlagType() const

若该属性是标志位则返回 `true`，否则返回 `false`。

标志位可以通过**或**运算合并多个值。标志位通常也是枚举类型。

**另请参阅：**[isEnumType](#bool-qmetapropertyisenumtype-const)()，[enumerator](#qmetaenum-qmetapropertyenumerator-const)() 和 [QMetaEnum::isFlag](../../M/QMetaEnum/QMetaEnum.md#bool-qmetaenumisflag-const)()。

----

### bool QMetaProperty::isReadable() const

若该属性可被读取则返回 `true`，否则返回 `false`。

**另请参阅：**[isWritable](#bool-qmetapropertyiswritable-const)()，[read](#qvariant-qmetapropertyreadconst-qobject-object-const)() 和 [isValid](#bool-qmetapropertyisvalid-const)()。

----

### bool QMetaProperty::isRequired() const

若该属性在 `Q_PROPERTY()` 中被标记为 `REQUIRED` 则返回 `true`，否则返回 `false`。

本函数在 Qt 5.15 中被引入。

----

### bool QMetaProperty::isResettable() const

若该属性可被重置为默认值则返回 `true`，否则返回 `false`。

**另请参阅：**[reset](#bool-qmetapropertyresetqobject-object-const)()。

----

### bool QMetaProperty::isScriptable(const [QObject](../../O/QObject/QObject.md) \**object* = nullptr) const

若该属性可被脚本化则返回 `true`，否则返回 `false`。

若 `object` 未被指定，则当 `Q_PROPERTY()` 的 `SCRIPTABLE` 标记被指定为 `false`时，此函数返回 `false` ；其它情况下返回 `true`（若该标记被指定为 `true`，或指定为某个函数，或指定为表达式）。

**另请参阅：**[isDesignable](#bool-qmetapropertyisdesignableconst-qobject-object--nullptr-const)() 和 [isStored](#bool-qmetapropertyisstoredconst-qobject-object--nullptr-const)()。

----

### bool QMetaProperty::isStored(const [QObject](../../O/QObject/QObject.md) \**object* = nullptr) const

若该属性可存储则返回 `true`，否则返回 `false`。

若 `object` 未被指定，则当 `Q_PROPERTY()` 的 `STORED` 标记被指定为 `false`时，此函数返回 `false` ；其它情况下返回 `true`（若该标记被指定为 `true`，或指定为某个函数，或指定为表达式）。

**另请参阅：**[isDesignable](#bool-qmetapropertyisdesignableconst-qobject-object--nullptr-const)() 和 [isScriptable](#bool-qmetapropertyisscriptableconst-qobject-object--nullptr-const)().

----

### bool QMetaProperty::isUser(const [QObject](../../O/QObject/QObject.md) \**object* = nullptr) const

若该属性被设计为 `USER` 性质则返回 `true`，即可以在 `object` 中被用户编辑，或在某些方面很重要；其它情况下返回 `false`。例如，[QLineEdit](../../L/QLineEdit/QLineEdit.md) 的 `text` 属性是 `USER` 可编辑的。

若 `object` 是 `nullptr`，则当 `Q_PROPERTY()` 的 `STORED` 标记被指定为 `false`时，此函数返回 `false` ；其它情况下返回 `true`。

**另请参阅：**[QMetaObject::userProperty](https://doc.qt.io/qt-5/qmetaobject.html#userProperty)()，[isDesignable](#bool-qmetapropertyisdesignableconst-qobject-object--nullptr-const)() 和 [isScriptable](#bool-qmetapropertyisscriptableconst-qobject-object--nullptr-const)()。

----

### bool QMetaProperty::isValid() const

若该属性是有效的（可读）则返回 `true`，否则返回 `false`。

**另请参阅：**[isReadable](#bool-qmetapropertyisreadable-const)()。

----

### bool QMetaProperty::isWritable() const

若该属性可被写入则返回 `true`，否则返回 `false`。

**另请参阅：**[isReadable](#bool-qmetapropertyisreadable-const)() 和 [write](#bool-qmetapropertywriteqobject-object-const-qvariant-value-const)()。

----

### const char *QMetaProperty::name() const

返回本属性的名称。

**另请参阅：**[type](#qvarianttype-qmetapropertytype-const)() 和 [typeName](#const-char-qmetapropertytypename-const)()。

----

### [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) QMetaProperty::notifySignal() const

若已为本属性指定数值修改时发送的通知信号，则返回该通知信号对应的 [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) 实例，否则返回无效的 [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) 对象。

本函数在 Qt 4.5 中被引入。

**另请参阅：**[hasNotifySignal](#bool-qmetapropertyhasnotifysignal-const)()、

### int QMetaProperty::notifySignalIndex() const

若已为本属性指定数值修改时发送的通知信号，则返回该通知信号的索引编号，否则返回 `-1`。

本函数在 Qt 4.6 中被引入。

**另请参阅：**[hasNotifySignal](#bool-qmetapropertyhasnotifysignal-const)()。

----

### int QMetaProperty::propertyIndex() const

返回本属性的索引编号。

本函数在 Qt 4.6 中被引入。

----

### [QVariant](../../V/QVariant/QVariant.md) QMetaProperty::read(const [QObject](../../O/QObject/QObject.md) \**object*) const

读取给定的 `object` 中的本属性，若可以读取则返回属性值，否则返回无效的 `QVariant`。

**另请参阅：**[write](#bool-qmetapropertywriteqobject-object-const-qvariant-value-const)()，[reset](#bool-qmetapropertyresetqobject-object-const)() 和 [isReadable](#bool-qmetapropertyisreadable-const)()。

### [QVariant](../../V/QVariant/QVariant.md) QMetaProperty::readOnGadget(const void \**gadget*) const

读取给定的 `gadget` 中的本属性，若可以读取则返回属性值，否则返回无效的 `QVariant`。

当且仅当本属性是 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 中的属性时，才可使用此函数。

本函数在 Qt 5.5 中被引入。

----

### int QMetaProperty::relativePropertyIndex() const

返回本属性在对应的元对象中的相对索引编号。

本函数在 Qt 5.14 中被引入。-

----

### bool QMetaProperty::reset([QObject](../../O/QObject/QObject.md) \**object*) const

通过重置方法重置给定的 `object` 中的本属性。若重置成功则返回 `true`，否则返回 `false`。

重置方法是可选的，只有少量属性支持重置。

**另请参阅：**[read](#qvariant-qmetapropertyreadconst-qobject-object-const)() 和 [write](#bool-qmetapropertywriteqobject-object-const-qvariant-value-const)()。

----

### bool QMetaProperty::resetOnGadget(void \**gadget*) const

通过重置方法重置给定的 `gadget` 中的本属性。若重置成功则返回 `true`，否则返回 `false`。

重置方法是可选的，只有少量属性支持重置。

当且仅当本属性是 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 中的属性时，才可使用此函数。

本函数在 Qt 5.5 中被引入。

----

### int QMetaProperty::revision() const

若该属性被 `REVISION` 标记，则返回对应的版本，否则返回 `0`。

本函数在 Qt 5.1 中被引入。

---

### [QVariant::Type](https://doc.qt.io/qt-5/qvariant-obsolete.html#Type-enum) QMetaProperty::type() const

返回本属性的类型。返回值是 `QVariant::Type` 的枚举值之。

**另请参阅：**[userType](#int-qmetapropertyusertype-const)()，[typeName](#const-char-qmetapropertytypename-const)() 和 [name](#const-char-qmetapropertyname-const)()。

----

### const char *QMetaProperty::typeName() const

返回本属性的类型名称。

**另请参阅：**[type](#qvarianttype-qmetapropertytype-const)() 和 [name](#const-char-qmetapropertyname-const)()。

-----

### int QMetaProperty::userType() const

返回本属性的用户类型。返回值是 [QMetaType](../../M/QMetaType/QMetaType.md) 中注册的类型之一，若该类型未被注册则返回 [QMetaType::UnknownType](../../M/QMetaType/QMetaType.md#enum-qmetatypetype)。

本函数在 Qt 4.2 中被引入。

**另请参阅：**[type](#qvarianttype-qmetapropertytype-const)()，[QMetaType](../../M/QMetaType/QMetaType.md) 和 [typeName](#const-char-qmetapropertytypename-const)()。

----

### bool QMetaProperty::write([QObject](../../O/QObject/QObject.md) \**object*, const [QVariant](../../V/QVariant/QVariant.md) &*value*) const

将 `value` 写入到给定的 `object` 的本属性中，若写入成功则返回 `true`，否则返回 `false`。

若 `value` 与本属性类型不一致，则会尝试进行自动转换。若本属性是可重置的，则传入空的 `QVariant()` 等价于调用 [reset](#bool-qmetapropertyresetqobject-object-const)()，否则等价于设置为默认值。

**另请参阅：**[read](#qvariant-qmetapropertyreadconst-qobject-object-const)()，[reset](#bool-qmetapropertyresetqobject-object-const)() 和 [isWritable](#bool-qmetapropertyiswritable-const)()。

----

### bool QMetaProperty::writeOnGadget(void \**gadget*, const [QVariant](../../V/QVariant/QVariant.md) &*value*) const

将 `value` 写入到给定的 `gadget` 的本属性中，若写入成功则返回 `true`，否则返回 `false`。

当且仅当本属性是 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 中的属性时，才可使用此函数。

本函数在 Qt 5.5 中被引入。