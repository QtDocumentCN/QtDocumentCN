# QMetaType 类

QMetaType 类管理元对象系统中的注名类型。[更多内容...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)。

| 属性   | 内容                   |
| ------ | ---------------------- |
| 头文件 | `#include <QMetaType>` |
| qmake  | `QT += core`           |

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。



## 公共成员类型

| 类型  | 名称                                                         |
| ----- | ------------------------------------------------------------ |
| enum  | **[Type](#enum-qmetatypetype)** { Void, Bool, Int, UInt, Double, ..., UnknownType } |
| enum  | **[TypeFlag](#enum-qmetatypetypeflag)** { NeedsConstruction, NeedsDestruction, MovableType, IsEnumeration, PointerToQObject } |
| flags | **[TypeFlags](#enum-qmetatypetypeflag)**                     |



## 公共成员函数

| 返回类型             | 函数                                                         |
| -------------------- | ------------------------------------------------------------ |
|                      | **[QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype)**(const int *typeId* = QMetaType::UnknownType) |
|                      | **[~QMetaType](#qmetatypeqmetatype)**()                      |
| void *               | **[construct](#void-qmetatypeconstructvoid-where-const-void-copy--0-const)**(void \**where*, const void \**copy* = 0) const |
| void *               | **[create](#void-qmetatypecreateconst-void-copy--0-const)**(const void \**copy* = 0) const |
| void                 | **[destroy](#void-qmetatypedestroyvoid-data-const)**(void \**data*) const |
| void                 | **[destruct](#void-qmetatypedestructvoid-data-const)**(void \**data*) const |
| QMetaType::TypeFlags | **[flags](#qmetatypetypeflags-qmetatypeflags-const)**() const |
| int                  | **[id](#int-qmetatypeid-const)**() const                     |
| bool                 | **[isRegistered](#bool-qmetatypeisregistered-const)**() const |
| bool                 | **[isValid](#bool-qmetatypeisvalid-const)**() const          |
| const QMetaObject *  | **[metaObject](#const-qmetaobject-qmetatypemetaobject-const)**() const |
| ::QByteArray         | **[name](#qbytearray-qmetatypename-const)**() const          |
| int                  | **[sizeOf](#int-qmetatypesizeof-const)**() const             |



## 静态公共成员

| 返回类型             | 函数                                                         |
| -------------------- | ------------------------------------------------------------ |
| bool                 | **[compare](#static-bool-qmetatypecompareconst-void-lhs-const-void-rhs-int-typeid-int-result)**(const void \**lhs*, const void \**rhs*, int *typeId*, int \**result*) |
| void *               | **[construct](#static-void-qmetatypeconstructint-type-void-where-const-void-copy)**(int *type*, void \**where*, const void \**copy*) |
| bool                 | **[convert](#static-bool-qmetatypeconvertconst-void-from-int-fromtypeid-void-to-int-totypeid)**(const void \**from*, int *fromTypeId*, void \**to*, int *toTypeId*) |
| void *               | **[create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)**(int *type*, const void \**copy* = nullptr) |
| bool                 | **[debugStream](#static-bool-qmetatypedebugstreamqdebug-dbg-const-void-rhs-int-typeid)**(QDebug &*dbg*, const void \**rhs*, int *typeId*) |
| void                 | **[destroy](#static-void-qmetatypedestroyint-type-void-data)**(int *type*, void \**data*) |
| void                 | **[destruct](#static-void-qmetatypedestructint-type-void-where)**(int *type*, void \**where*) |
| bool                 | **[equals](#static-bool-qmetatypeequalsconst-void-lhs-const-void-rhs-int-typeid-int-result)**(const void \**lhs*, const void \**rhs*, int *typeId*, int \**result*) |
| QMetaType            | **[fromType](#static-template-typename-t-qmetatype-qmetatypefromtype)**() |
| bool                 | **[hasRegisteredComparators](#static-template-typename-t-bool-qmetatypehasregisteredcomparators)**() |
| bool                 | **[hasRegisteredComparators](#static-bool-qmetatypehasregisteredcomparatorsint-typeid)**(int *typeId*) |
| bool                 | **[hasRegisteredConverterFunction](#static-bool-qmetatypehasregisteredconverterfunctionint-fromtypeid-int-totypeid)**(int *fromTypeId*, int *toTypeId*) |
| bool                 | **[hasRegisteredConverterFunction](#static-template-typename-from-typename-to-bool-qmetatypehasregisteredconverterfunction)**() |
| bool                 | **[hasRegisteredDebugStreamOperator](#static-template-typename-t-bool-qmetatypehasregistereddebugstreamoperator)**() |
| bool                 | **[hasRegisteredDebugStreamOperator](#static-bool-qmetatypehasregistereddebugstreamoperatorint-typeid)**(int *typeId*) |
| bool                 | **[isRegistered](#static-bool-qmetatypeisregisteredint-type)**(int *type*) |
| bool                 | **[load](#static-bool-qmetatypeloadqdatastream-stream-int-type-void-data)**(QDataStream &*stream*, int *type*, void \**data*) |
| const QMetaObject *  | **[metaObjectForType](#static-const-qmetaobject-qmetatypemetaobjectfortypeint-type)**(int *type*) |
| bool                 | **[registerComparators](#static-template-typename-t-bool-qmetatyperegistercomparators)**() |
| bool                 | **[registerConverter](#static-template-typename-from-typename-to-bool-qmetatyperegisterconverter)**() |
| bool                 | **[registerConverter](#static-template-typename-memberfunction-int-bool-qmetatyperegisterconvertermemberfunction-function)**(MemberFunction *function*) |
| bool                 | **[registerConverter](#static-template-typename-memberfunctionok-char-bool-qmetatyperegisterconvertermemberfunctionok-function)**(MemberFunctionOk *function*) |
| bool                 | **[registerConverter](#static-template-typename-unaryfunction-bool-qmetatyperegisterconverterunaryfunction-function)**(UnaryFunction *function*) |
| bool                 | **[registerDebugStreamOperator](#static-template-typename-t-bool-qmetatyperegisterdebugstreamoperator)**() |
| bool                 | **[registerEqualsComparator](#static-template-typename-t-bool-qmetatyperegisterequalscomparator)**() |
| bool                 | **[save](#static-bool-qmetatypesaveqdatastream-stream-int-type-const-void-data)**(QDataStream &*stream*, int *type*, const void \**data*) |
| int                  | **[sizeOf](#static-int-qmetatypesizeofint-type)**(int *type*) |
| int                  | **[type](#static-int-qmetatypetypeconst-char-typename)**(const char \**typeName*) |
| int                  | **[type](#static-int-qmetatypetypeconst-qbytearray-typename)**(const ::QByteArray &*typeName*) |
| QMetaType::TypeFlags | **[typeFlags](#static-qmetatypetypeflags-qmetatypetypeflagsint-type)**(int *type*) |
| const char *         | **[typeName](#static-const-char-qmetatypetypenameint-typeid)**(int *typeId*) |



## 相关非成员函数

| 返回类型 | 函数                                                         |
| -------- | ------------------------------------------------------------ |
| int      | **[qMetaTypeId](#template-typename-t-int-qmetatypeid)**()    |
| int      | **[qRegisterMetaType](#template-typename-t-int-qregistermetatypeconst-char-typename)**(const char \**typeName*) |
| int      | **[qRegisterMetaType](#template-typename-t-int-qregistermetatype)**() |
| void     | **[qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)**(const char \**typeName*) |
| bool     | **[operator!=](#bool-operatorconst-qmetatype-a-const-qmetatype-b)**(const QMetaType &*a*, const QMetaType &*b*) |
| bool     | **[operator==](#bool-operatorconst-qmetatype-a-const-qmetatype-b)**(const QMetaType &*a*, const QMetaType &*b*) |



## 宏定义

| 宏定义                                                       |
| ------------------------------------------------------------ |
| **[Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE](#qdeclareassociativecontainermetatypecontainer)**(*Container*) |
| **[Q_DECLARE_METATYPE](#qdeclaremetatypetype)**(*Type*)      |
| **[Q_DECLARE_OPAQUE_POINTER](#qdeclareopaquepointerpointertype)**(*PointerType*) |
| **[Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE](#qdeclaresequentialcontainermetatypecontainer)**(*Container*) |
| **[Q_DECLARE_SMART_POINTER_METATYPE](#qdeclaresmartpointermetatypesmartpointer)**(*SmartPointer*) |



## 详细描述

此类是一个辅助类，被用作序列化 [QVariant](#enum-qmetatypetype) 以及队列连接信号槽中的类型。它将类型名称关联到对应类型，以支持运行时动态创建和销毁此类型。通过 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 声明新类型，让它可以被 [QVariant](#enum-qmetatypetype) 和其它模板函数（[qMetaTypeId](#template-typename-t-int-qmetatypeid)() 等）使用。调用 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)() 来让其可以被非模板型函数使用，如信号槽的队列连接。

任何包含一个公共默认构造函数、一个公共拷贝构造函数、一个默认析构函数的类或结构体都可以被注册为元类型。

下述代码展示了如何分配和销毁一个 `MyClass` 的实例：

```cpp
int id = QMetaType::type("MyClass");
if (id != QMetaType::UnknownType) {
    void *myClassPtr = QMetaType::create(id);
    ...
    QMetaType::destroy(id, myClassPtr);
    myClassPtr = 0;
}
```

若我们想让流运算符 `operator<<()` 和 `operator>>()` 可被用于存储了自定义类型的 [QVariant](#enum-qmetatypetype) 对象，则这个自定义类型必须提供 `operator<<()` 和 `operator>>()` 运算符重载。

**另请参阅：**[Q_DECLARE_METATYPE](#qdeclaremetatypetype)()，[QVariant::setValue](../../V/QVariant/QVariant.md#template-typename-t-void-qvariantsetvalueconst-t-value)()，[QVariant::value](../../V/QVariant/QVariant.md#template-typename-t-t-qvariantvalue-const)() 和 [QVariant::fromValue](../../V/QVariant/QVariant.md#static-template-typename-t-qvariant-qvariantfromvalueconst-t-value)().



## 成员类型文档

### enum QMetaType::Type

下表是 [QMetaType](../../M/QMetaType/QMetaType.md) 内置支持的类型：

| 常量                               | 数值   | 描述                                                         |
| ---------------------------------- | ------ | ------------------------------------------------------------ |
| `QMetaType::Void`                  | `43`   | `void`                                                       |
| `QMetaType::Bool`                  | `1`    | `bool`                                                       |
| `QMetaType::Int`                   | `2`    | `int`                                                        |
| `QMetaType::UInt`                  | `3`    | `unsigned int`                                               |
| `QMetaType::Double`                | `6`    | `double`                                                     |
| `QMetaType::QChar`                 | `7`    | `QChar`                                                      |
| `QMetaType::QString`               | `10`   | [QString](../../S/QString/QString.md)                        |
| `QMetaType::QByteArray`            | `12`   | [QByteArray](../../B/QByteArray/QByteArray.md)               |
| `QMetaType::Nullptr`               | `51`   | `std::nullptr_t`                                             |
| `QMetaType::VoidStar`              | `31`   | `void *`                                                     |
| `QMetaType::Long`                  | `32`   | `long`                                                       |
| `QMetaType::LongLong`              | `4`    | `long long`                                                  |
| `QMetaType::Short`                 | `33`   | `short`                                                      |
| `QMetaType::Char`                  | `34`   | `char`                                                       |
| `QMetaType::ULong`                 | `35`   | `unsigned long`                                              |
| `QMetaType::ULongLong`             | `5`    | `unsigned long long`                                         |
| `QMetaType::UShort`                | `36`   | `unsigned short`                                             |
| `QMetaType::SChar`                 | `40`   | `signed char`                                                |
| `QMetaType::UChar`                 | `37`   | `unsigned char`                                              |
| `QMetaType::Float`                 | `38`   | `float`                                                      |
| `QMetaType::QObjectStar`           | `39`   | [QObject](../../O/QObject/QObject.md) *                      |
| `QMetaType::QVariant`              | `41`   | [QVariant](../../V/QVariant/QVariant.md)                     |
| `QMetaType::QCursor`               | `74`   | [QCursor](../../C/QCursor/QCursor.md)                        |
| `QMetaType::QDate`                 | `14`   | [QDate](../../D/QDate/QDate.md)                              |
| `QMetaType::QSize`                 | `21`   | [QSize](../../S/QSize/QSize.md)                              |
| `QMetaType::QTime`                 | `15`   | [QTime](../../T/QTime/QTime.md)                              |
| `QMetaType::QVariantList`          | `9`    | [QVariantList](../../V/QVariant/QVariant.md#typedef-qvariantlist) |
| `QMetaType::QPolygon`              | `71`   | [QPolygon](../../P/QPolygon/QPolygon.md)                     |
| `QMetaType::QPolygonF`             | `86`   | [QPolygonF](../../P/QPolygonF/QPolygonF.md)                  |
| `QMetaType::QColor`                | `67`   | [QColor](../../C/QColor/QColor.md)                           |
| `QMetaType::QColorSpace`           | `87`   | [QColorSpace](../../C/QColorSpace/QColorSpace.md)（在 Qt 5.15 中被引入） |
| `QMetaType::QSizeF`                | `22`   | [QSizeF](../../S/QSizeF/QSizeF.md)                           |
| `QMetaType::QRectF`                | `20`   | [QRectF](../../R/QRectF/QRectF.md)                           |
| `QMetaType::QLine`                 | `23`   | [QLine](../../L/QLine/QLine.md)                              |
| `QMetaType::QTextLength`           | `77`   | [QTextLength](../../T/QTextLength/QTextLength.md)            |
| `QMetaType::QStringList`           | `11`   | [QStringList](../../S/QStringList/QStringList.md)            |
| `QMetaType::QVariantMap`           | `8`    | [QVariantMap](../../V/QVariant/QVariant.md#typedef-qvariantmap) |
| `QMetaType::QVariantHash`          | `28`   | [QVariantHash](../../V/QVariant/QVariant.md#typedef-qvarianthash) |
| `QMetaType::QIcon`                 | `69`   | [QIcon](../../I/QIcon/QIcon.md)                              |
| `QMetaType::QPen`                  | `76`   | [QPen](../../P/QPen/QPen.md)                                 |
| `QMetaType::QLineF`                | `24`   | [QLineF](../../L/QLineF/QLineF.md)                           |
| `QMetaType::QTextFormat`           | `78`   | [QTextFormat](../../T/QTextFormat/QTextFormat.md)            |
| `QMetaType::QRect`                 | `19`   | [QRect](../../R/QRect/QRect.md)                              |
| `QMetaType::QPoint`                | `25`   | [QPoint](../../P/QPoint/QPoint.md)                           |
| `QMetaType::QUrl`                  | `17`   | [QUrl](../../U/QUrl/QUrl.md)                                 |
| `QMetaType::QRegExp`               | `27`   | [QRegExp](../../R/QRegExp/QRegExp.md)                        |
| `QMetaType::QRegularExpression`    | `44`   | [QRegularExpression](../../R/QRegularExpression/QRegularExpression.md) |
| `QMetaType::QDateTime`             | `16`   | [QDateTime](../../D/QDateTime/QDateTime.md)                  |
| `QMetaType::QPointF`               | `26`   | [QPointF](../../P/QPointF/QPointF.md)                        |
| `QMetaType::QPalette`              | `68`   | [QPalette](../../P/QPalette/QPalette.md)                     |
| `QMetaType::QFont`                 | `64`   | [QFont](../../F/QFont/QFont.md)                              |
| `QMetaType::QBrush`                | `66`   | [QBrush](../../B/QBrush/QBrush.md)                           |
| `QMetaType::QRegion`               | `72`   | [QRegion](../../R/QRegion/QRegion.md)                        |
| `QMetaType::QBitArray`             | `13`   | [QBitArray](../../B/QBitArray/QBitArray.md)                  |
| `QMetaType::QImage`                | `70`   | [QImage](../../I/QImage/QImage.md)                           |
| `QMetaType::QKeySequence`          | `75`   | [QKeySequence](../../K/QKeySequence/QKeySequence.md)         |
| `QMetaType::QSizePolicy`           | `121`  | [QSizePolicy](../../S/QSizePolicy/QSizePolicy.md)            |
| `QMetaType::QPixmap`               | `65`   | [QPixmap](../../P/QPixmap/QPixmap.md)                        |
| `QMetaType::QLocale`               | `18`   | [QLocale](../../L/QLocale/QLocale.md)                        |
| `QMetaType::QBitmap`               | `73`   | [QBitmap](../../B/QBitmap/QBitmap.md)                        |
| `QMetaType::QMatrix`               | `79`   | [QMatrix](../../M/QMatrix/QMatrix.md)                        |
| `QMetaType::QTransform`            | `80`   | [QTransform](../../T/QTransform/QTransform.md)               |
| `QMetaType::QMatrix4x4`            | `81`   | [QMatrix4x4](../../M/QMatrix4x4/QMatrix4x4.md)               |
| `QMetaType::QVector2D`             | `82`   | [QVector2D](../../V/QVector2D/QVector2D.md)                  |
| `QMetaType::QVector3D`             | `83`   | [QVector3D](../../V/QVector3D/QVector3D.md)                  |
| `QMetaType::QVector4D`             | `84`   | [QVector4D](../../V/QVector4D/QVector4D.md)                  |
| `QMetaType::QQuaternion`           | `85`   | [QQuaternion](../../Q/QQuaternion/QQuaternion.md)            |
| `QMetaType::QEasingCurve`          | `29`   | [QEasingCurve](../../E/QEasingCurve/QEasingCurve.md)         |
| `QMetaType::QJsonValue`            | `45`   | [QJsonValue](../../J/QJsonValue/QJsonValue.md)               |
| `QMetaType::QJsonObject`           | `46`   | [QJsonObject](../../J/QJsonObject/QJsonObject.md)            |
| `QMetaType::QJsonArray`            | `47`   | [QJsonArray](../../J/QJsonArray/QJsonArray.md)               |
| `QMetaType::QJsonDocument`         | `48`   | [QJsonDocument](../../J/QJsonDocument/QJsonDocument.md)      |
| `QMetaType::QCborValue`            | `53`   | [QCborValue](../../C/QCborValue/QCborValue.md)               |
| `QMetaType::QCborArray`            | `54`   | [QCborArray](../../C/QCborArray/QCborArray.md)               |
| `QMetaType::QCborMap`              | `55`   | [QCborMap](../../C/QCborMap/QCborMap.md)                     |
| `QMetaType::QCborSimpleType`       | `52`   | [QCborSimpleType](../../C/QCborCommon/QCborCommon.md#enum-class-qcborsimpletype) |
| `QMetaType::QModelIndex`           | `42`   | [QModelIndex](../../M/QModelIndex/QModelIndex.md)            |
| `QMetaType::QPersistentModelIndex` | `50`   | [QPersistentModelIndex](../../P/QPersistentModelIndex/QPersistentModelIndex.md)（在 Qt 5.5 中被引入） |
| `QMetaType::QUuid`                 | `30`   | [QUuid](../../U/QUuid/QUuid.md)                              |
| `QMetaType::QByteArrayList`        | `49`   | [QByteArrayList](../../B/QByteArrayList/QByteArrayList.md)   |
| `QMetaType::User`                  | `1024` | 用户类型的基础值（`译者注：即起始值`）                           |`
| `QMetaType::UnknownType`           | `0`    | 这是无效的类型编号，[QMetaType](../../M/QMetaType/QMetaType.md) 会在类型未注册时返回此值。 |

可以使用 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 注册额外的类型。

**另请参阅：**[type](#static-int-qmetatypetypeconst-char-typename)() 和 [typeName](#static-const-char-qmetatypetypenameint-typeid)()。

----

### enum QMetaType::TypeFlag

### flags QMetaType::TypeFlags

此枚举类型描述了被 [QMetaType](../../M/QMetaType/QMetaType.md) 支持的类型的属性。

| 常量                           | 数值   | 描述                                                         |
| ------------------------------ | ------ | ------------------------------------------------------------ |
| `QMetaType::NeedsConstruction` | `0x1`  | 此类型具有[非平凡的构造函数](https://en.cppreference.com/w/cpp/language/default_constructor#Trivial_default_constructor)。若某类型不具备此标志，则可通过 `memset`() 安全地清零。 |
| `QMetaType::NeedsDestruction`  | `0x2`  | 此类型[非平凡的析构函数](https://en.cppreference.com/w/cpp/language/destructor#Trivial_destructor)。若某类型不具备此标志，则丢弃对象前不需要调用析构函数（`译者注：即可以用 free() 释放对象`） |
| `QMetaType::MovableType`       | `0x4`  | 具有此标志的类型实例可以通过 `memcpy`() 安全地移动。         |
| `QMetaType::IsEnumeration`     | `0x10` | 此类型是枚举值。                                             |
| `QMetaType::PointerToQObject`  | `0x8`  | 此类型是指向继承自 [QObject](../../O/QObject/QObject.md) 的类型的指针。 |

`TypeFlags` 类型是 [QFlags](../../F/QFlags/QFlags.md)\<TypeFlag\> 的别名，支持通过**或**操作合并不同的 `TypeFlag` 值。



## 成员函数文档

### QMetaType::QMetaType(const int *typeId* = QMetaType::UnknownType)

构造一个包含 `typeId` 对应的类型信息的 `QMetaType` 对象。

**注意：** 默认参数在 Qt 5.15 中被引入。

此函数在 Qt 5.0 中被引入。

----

### QMetaType::~QMetaType()

析构此对象。

----

### *[static]* bool QMetaType::compare(const void \**lhs*, const void \**rhs*, int *typeId*, int \**result*)

比较 `lhs` 和 `rhs` 对象，双方都需要是 `typeid` 中的类型。*result* 会被设为小于、等于或大于零，表示 `lhs` 小于、等于或大于 `rhs`。若比较成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* void \*QMetaType::construct(int *type*, void \**where*, const void \**copy*)

在给定的内存地址 `where` 上构造对应 `type` 类型的对象，该对象是 `copy` 的副本，并返回 `where`。若 `copy` 是空指针，则执行默认构造。

这是用于显示管理存储 `type` 类型对象的内存的底层函数。若不需要此类底层控制，则考虑使用 [create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)() 函数（也就是指，使用 `new` 而非 `placement new`）。

您必须确保 `where` 指向的内存区域大小足够存储 `type` 对应的数据，并且 `where` 地址需要对齐，对应类型的大小可通过 [sizeOf](#int-qmetatypesizeof-const)() 获取。

内存对齐的规则是对齐至类型的自然边界，也就是大于等于类型大小的2的n次方值，直至平台有效对齐宽度上限为止。对于特定用途来说，超过 `2 * sizeof(void*)` 的对齐宽度只是某些特定硬件指令所必需的（例如，x86 平台中对齐后的 SSE 读取和存储）。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[destruct](#static-void-qmetatypedestructint-type-void-where)() 和 [sizeOf](#int-qmetatypesizeof-const)()。

----

### void \*QMetaType::construct(void \**where*, const void \**copy* = 0) const

在给定的内存地址 `where` 上构造此 [QMetaType](../../M/QMetaType/QMetaType.md) 类型的对象，该对象是 `copy` 的副本，并返回 `where`。若 `copy` 是空指针，则执行默认构造。

这是用于显示管理存储 `type` 类型对象的内存的底层函数。若不需要此类底层控制，则考虑使用 [create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)() 函数（也就是指，使用 `new` 而非 `placement new`）。

您必须确保 `where` 指向的内存区域大小足够存储 `type` 对应的数据，并且 `where` 地址需要对齐，对应类型的大小可通过 [sizeOf](#int-qmetatypesizeof-const)() 获取。

内存对齐的规则是对齐至类型的自然边界，也就是大于等于类型大小的2的n次方值，直至平台有效对齐宽度上限为止。对于特定用途来说，超过 `2 * sizeof(void*)` 的对齐宽度只是某些特定硬件指令所必需的（例如，x86 平台中对齐后的 SSE 读取和存储）。

此函数在 Qt 5.0 中被引入。

----

### *[static]* bool QMetaType::convert(const void \**from*, int *fromTypeId*, void \**to*, int *toTypeId*)

将 `from` 对象从 `fromTypeId` 转换至 `toTypeId` 并存储到预分配空间 `to` 中。若转换成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* void \*QMetaType::create(int *type*, const void \**copy* = nullptr)

假设 `copy` 的类型是 `type`，返回它的的拷贝。若 `copy` 是空指针，则返回默认构造的实例。

**另请参阅：**[destroy](#static-void-qmetatypedestroyint-type-void-data)()，[isRegistered](#bool-qmetatypeisregistered-const)() 和 [Type](#enum-qmetatypetype)。

----

### void *QMetaType::create(const void \**copy* = 0) const

假设 `copy` 的类型是此 [QMetaType](../../M/QMetaType/QMetaType.md) ，返回它的的拷贝。若 `copy` 是空指针，则返回默认构造的实例。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::destroy](#static-void-qmetatypedestroyint-type-void-data)()。

----

### *[static]* bool QMetaType::debugStream([QDebug](../../D/QDebug/QDebug.md) &*dbg*, const void \**rhs*, int *typeId*)

将 `typeId` 类型的 `rhs` 对象输出至调试流 `debug`，输出成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* void QMetaType::destroy(int *type*, void \**data*)

假设 `data` 的类型是 `type`，销毁该对象。

**另请参阅：**[create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)()，[isRegistered](#bool-qmetatypeisregistered-const)() 和 [Type](#enum-qmetatypetype)。

----

### void QMetaType::destroy(void **data*) const

假设 `data` 的类型是此 [QMetaType](../../M/QMetaType/QMetaType.md) ，销毁该对象。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)()。

----

### *[static]* void QMetaType::destruct(int *type*, void \**where*)

假设 `where` 地址中存储的对象类型是 `type`，销毁该对象。

与 [destroy](#static-void-qmetatypedestroyint-type-void-data)() 不同，此函数只会执行该类型的析构函数，但不会执行 `delete` 运算符（`译者注：即不会释放内存，与 placement new 相同机制`）。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)()。

----

### void QMetaType::destruct(void \**data*) const

假设 `data` 地址中存储的对象类型是此 [QMetaType](../../M/QMetaType/QMetaType.md) ，销毁该对象。

与 [destroy](#static-void-qmetatypedestroyint-type-void-data)() 不同，此函数只会执行该类型的析构函数，但不会执行 `delete` 运算符（`译者注：即不会释放内存，与 placement new 相同机制`）。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)()。

----

### *[static]* bool QMetaType::equals(const void \**lhs*, const void \**rhs*, int *typeId*, int \**result*)

比较 `lhs` 和 `rhs` 对象，双方都需要是 `typeid` 中的类型。若 `lhs` 等于 `rhs`，则 *result* 会被设为零。若比较成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.5 中被引入。

----

### [QMetaType::TypeFlags](#enum-qmetatypetypeflag) QMetaType::flags() const

返回此 [QMetaType](../../M/QMetaType/QMetaType.md) 实例的类型标志。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::TypeFlags](#enum-qmetatypetypeflag) 和 [QMetaType::typeFlags](#static-qmetatypetypeflags-qmetatypetypeflagsint-type)()。

----

### *[static]* template \<typename T\> [QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype) QMetaType::fromType()

返回模板类型 `T` 对应的 [QMetaType](../../M/QMetaType/QMetaType.md) 实例。

此函数在 Qt 5.15 中被引入。

----

### *[static]* template \<typename T\> bool QMetaType::hasRegisteredComparators()

若模板类型 `T` 已被注册至元对象系统则返回 `true`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* bool QMetaType::hasRegisteredComparators(int *typeId*)

若 `typeId` 的类型已被注册至元对象系统则返回 `true`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* bool QMetaType::hasRegisteredConverterFunction(int *fromTypeId*, int *toTypeId*)

若自 `fromTypeId` 到 `toTypeId` 的类型转换已被注册至元对象系统则返回 `true`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* template <typename From, typename To> bool QMetaType::hasRegisteredConverterFunction()

若自模板类型 `From` 到 `To` 的类型转换已被注册至元对象系统则返回 `true`。

这是一个重载函数。

此函数在 Qt 5.2 中被引入。

----

### *[static]* template \<typename T\> bool QMetaType::hasRegisteredDebugStreamOperator()

若自模板类型 `T` 的 [QDebug](../../D/QDebug/QDebug.md) 流运算符已被注册至元对象系统则返回 `true`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* bool QMetaType::hasRegisteredDebugStreamOperator(int *typeId*)

若自 `typeId` 对应类型的 [QDebug](../../D/QDebug/QDebug.md) 流运算符已被注册至元对象系统则返回 `true`。

此函数在 Qt 5.2 中被引入。

----

### int QMetaType::id() const

返回此 QMetatype 实例的类型编号。

此函数在 Qt 5.13 中被引入。

----

### *[static]* bool QMetaType::isRegistered(int *type*)

若 `typeId` 对应已被注册至元对象系统则返回 `true`，否则返回 `false`。

**另请参阅：**[type](#static-int-qmetatypetypeconst-char-typename)()，[typeName](#static-const-char-qmetatypetypenameint-typeid)() 和 [Type](#enum-qmetatypetype)。

----

### bool QMetaType::isRegistered() const

若此 [QMetaType](../../M/QMetaType/QMetaType.md) 包含某类型的有效信息则返回 `true`，否则返回 `false`。

此函数在 Qt 5.0 中被引入。

----

### bool QMetaType::isValid() const

若此 [QMetaType](../../M/QMetaType/QMetaType.md) 包含某类型的有效信息则返回 `true`，否则返回 `false`。

此函数在 Qt 5.0 中被引入。

----

### *[static]* bool QMetaType::load([QDataStream](../../D/QDataStream/QDataStream.md) &*stream*, int *type*, void \**data*)

从数据流 `stream` 中读取对应 `type` 类型的对象至 `data` 中，若读取成功则返回 `true`，否则返回 `false`。

此类型必须在这之前通过 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)() 完成注册。

通常来说，您不需要显示调用此函数，而是应使用 [QVariant](#enum-qmetatypetype) 的 `operator>>()`，该运算符依赖 `load`() 来传递自定义类型。

**另请参阅：**[save](#static-bool-qmetatypesaveqdatastream-stream-int-type-const-void-data)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)()。

----

### const [QMetaObject](../../M/QMetaObject/QMetaObject.md) \*QMetaType::metaObject() const

返回此类型对应的 [QMetaObject](../../M/QMetaObject/QMetaObject.md)。

若此类型是 [QObject](../../O/QObject/QObject.md) 子类的指针，即 [flags](#qmetatypetypeflags-qmetatypeflags-const)() 包含 [QMetaType::PointerToQObject](#enum-qmetatypetypeflag)，则此函数会返回对应类型的 [QMetaObject](../../M/QMetaObject/QMetaObject.md)。这可被用于结合 `QMetaObject::construct`（`译者注：无此函数，请使用` [QMetaObject::constructor](../../M/QMetaObject/QMetaObject.md#qmetamethod-qmetaobjectconstructorint-index-const) `或` [QMetaType::construct](#void-qmetatypeconstructvoid-where-const-void-copy--0-const)）来创建此类型的 [QObject](../../O/QObject/QObject.md) 实例。

若此类型是 [Q_GADGET](../../O/QObject/QObject.md#qgadget)，即 [flags](#qmetatypetypeflags-qmetatypeflags-const)() 包含 [QMetaType::IsGadget](#enum-qmetatypetypeflag)（`译者注：文档中未给出，但` [QMetaType::TypeFlag](#enum-qmetatypetypeflag) `中的确包含此枚举值`），则此函数会返回对应类型的 [QMetaObject](../../M/QMetaObject/QMetaObject.md)。这可以被用于获取 [QMetaMethod](../../M/QMetaMethod/QMetaMethod.md) 和 [QMetaProperty](../../M/QMetaProperty/QMetaProperty.md)，并将其用于此类型的对象指针上（例如通过 QVariant::data 获取指针 `译者注：文档中无此函数，但此函数的确存在`）。

若此类型是枚举，即 [flags](#qmetatypetypeflags-qmetatypeflags-const)() 包含 [QMetaType::IsEnumeration](#enum-qmetatypetypeflag)，且该枚举值是通过 [Q_ENUM](../../O/QObject/QObject.md#qenum) 注册的成员枚举类型，则此函数会返回其所属的 [QObject](../../O/QObject/QObject.md) 对象的元对象，否则返回 `nullptr`。

此函数在 Qt 5.5 中被引入。

**另请参阅：**[QMetaType::metaObjectForType](#static-const-qmetaobject-qmetatypemetaobjectfortypeint-type)() 和 [QMetaType::flags](#qmetatypetypeflags-qmetatypeflags-const)()。

----

### *[static]* const [QMetaObject](../../M/QMetaObject/QMetaObject.md) \*QMetaType::metaObjectForType(int *type*)

返回 `type` 类型对应的 [QMetaType::metaObject](#const-qmetaobject-qmetatypemetaobject-const)。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[metaObject](#const-qmetaobject-qmetatypemetaobject-const)()。

----

### ::QByteArray QMetaType::name() const

返回此 [QMetaType](../../M/QMetaType/QMetaType.md) 对应的类型名称，若无有效类型则返回空指针。

此函数在 Qt 5.15 中被引入。

**另请参阅：**[typeName](#static-const-char-qmetatypetypenameint-typeid)()。

----

### *[static]* template \<typename T\> bool QMetaType::registerComparators()

将用户注册类型 `T` 的比较运算符注册至元对象系统。要求 `T` 具有 `operator==` 和 `operator<` 运算符。若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* template \<typename From, typename To\> bool QMetaType::registerConverter()

将类型 `From` 到 `To` 的可能的隐式转换注册到元对象系统，若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

----

### *[static]* template \<typename MemberFunction, int\> bool QMetaType::registerConverter(MemberFunction *function*)

这是一个重载函数。

将形如 `To From::function() const` 的成员方法 `function` 作为从 `From` 到 `To` 的转换函数注册至元对象系统，若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

> 译者注：
>
> 第二个模板参数是官方使用 doxygen 生成文档时的变通写法，实际代码中的函数签名是 `template<typename From, typename To> static bool registerConverter(To(From::*function)() const)`。使用时无需指定 `int` 模板参数，在函数参数中直接填入用于转换的成员函数指针即可。

----

### *[static]* template \<typename MemberFunctionOk, char\> bool QMetaType::registerConverter(MemberFunctionOk *function*)

这是一个重载函数。

将形如 `To From::function(bool *ok) const` 的成员方法 `function` 作为从 `From` 到 `To` 的转换函数注册至元对象系统，若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

> 译者注：
>
> 第二个模板参数是官方使用 doxygen 生成文档时的变通写法，实际代码中的函数签名是 `template<typename From, typename To> static bool registerConverter(To(From::*function)(bool*) const)`。使用时无需指定 `char` 模板参数，在函数参数中直接填入用于转换的成员函数指针即可。

----

### *[static]* template \<typename UnaryFunction\> bool QMetaType::registerConverter(UnaryFunction *function*)

这是一个重载函数。

将把类型 `From` 转换为类型 `To` 的一元函数 `function` 注册至元对象系统，若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.2 中被引入。

> 译者注：
>
> 原文描述地非常晦涩，实际指的是任何可被 `To dst = function(src)` 方式调用的函数对象，包括全局函数、类静态函数、仿函数或 lamba 等，比上文另外两个 `registerConverter` 的约束更为宽松。

----

### *[static]* template \<typename T\> bool QMetaType::registerDebugStreamOperator()

将已注册类型 `T` 的 [QDebug](../../D/QDebug/QDebug.md) 流运算符注册至元对象系统，要求类型 `T` 具备流运算符 `operator<<(QDebug dbg, T)`。若注册成功则返回 `true`，否则返回 `false`。

----

### *[static]* template \<typename T\> bool QMetaType::registerEqualsComparator()

将已注册类型 `T` 的等号运算符注册至元对象系统，要求类型 `T` 具备等号运算符 `operator==`。若注册成功则返回 `true`，否则返回 `false`。

此函数在 Qt 5.5 中被引入。

----

### *[static]* bool QMetaType::save([QDataStream](../../D/QDataStream/QDataStream.md) &*stream*, int *type*, const void \**data*)

从数据流 `stream` 中读取对应 `type` 类型的对象至 `data` 中，若读取成功则返回 `true`，否则返回 `false`。

此类型必须在这之前通过 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)() 完成注册。

通常来说，您不需要显示调用此函数，而是应使用 [QVariant](#enum-qmetatypetype) 的 `operator>>()`，该运算符依赖 `load`() 来传递自定义类型。

**另请参阅：**[save](#static-bool-qmetatypesaveqdatastream-stream-int-type-const-void-data)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)()。

将 `type` 类型对应的 `data` 对象输出至数据流 `stream` 中，若读取成功则返回 `true`，否则返回 `false`。

此类型必须在这之前通过 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)() 完成注册。

通常来说，您不需要显示调用此函数，而是应使用 [QVariant](#enum-qmetatypetype) 的 `operator<<()`，该运算符依赖 `save`() 来传递自定义类型。

**另请参阅：**[load](#static-bool-qmetatypeloadqdatastream-stream-int-type-void-data)() 和 [qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)()。

----

### *[static]* int QMetaType::sizeOf(int *type*)

返回 `type` 对应类型的以字节为单位的大小（即 `sizeof(T)`，其中 `T` 是 `type` 对应的实际类型）。

此函数通常结合 [construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)() 使用，来进行对此类型的更底层的内存管理。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)()。

----

### int QMetaType::sizeOf() const

返回此类型的以字节为单位的大小（即 `sizeof(T)`，其中 `T` 是 [QMetaType](../../M/QMetaType/QMetaType.md) 对应的实际类型）。

此函数通常结合 [construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)() 使用，来进行对此类型的更底层的内存管理。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::construct](https://doc.qt.io/qt-5/qmetatype-obsolete.html#construct)() 和 [QMetaType::sizeOf](#static-int-qmetatypesizeofint-type)()。

----

### *[static]* int QMetaType::type(const char \**typeName*)

返回名为 `typeName` 的类型的元类型编号，若无此元类型则返回 [QMetaType::UnknownType](#enum-qmetatypetype)。

**另请参阅：**[isRegistered](#bool-qmetatypeisregistered-const)()，[typeName](#static-const-char-qmetatypetypenameint-typeid)() 和 [Type](#enum-qmetatypetype)。

----

### *[static]* int QMetaType::type(const ::QByteArray &*typeName*)

这是一个重载函数。

返回名为 `typeName` 的类型的元类型编号，若无此元类型则返回 `0`（`译者注：即`[QMetaType::UnknownType](#enum-qmetatypetype)）。

此函数在 Qt 5.5 中被引入。

**另请参阅：**[isRegistered](#bool-qmetatypeisregistered-const)() 和 [typeName](#static-const-char-qmetatypetypenameint-typeid)()。

----

### *[static]* [QMetaType::TypeFlags](#enum-qmetatypetypeflag) QMetaType::typeFlags(int *type*)

返回 `type` 类型的类型标志。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[QMetaType::TypeFlags](#enum-qmetatypetypeflag)。

----

### *[static]* const char \*QMetaType::typeName(int *typeId*)

返回 `typeId` 对应类型的类型名称，若该类型不存在则返回空指针。**返回的指针不可被删除。**

**另请参阅：**[type](#static-int-qmetatypetypeconst-char-typename)()，[isRegistered](#bool-qmetatypeisregistered-const)()，[Type](#enum-qmetatypetype) 和 [name](#qbytearray-qmetatypename-const)()。



## 相关非成员函数

### template \<typename T\> int qMetaTypeId()

返回类型 `T` 对应的元类型编号。若该类型未通过 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 声明，则会引发编译错误。

典型用法：

```cpp
int id = qMetaTypeId<QString>();    // id 是 QMetaType::QString
id = qMetaTypeId<MyStruct>();       // 若 MyStruct 未被声明，则会产生编译错误
```

[QMetaType::type](#static-int-qmetatypetypeconst-char-typename)() 返回值与 `qMetaTypeId()` 相同，但会基于类型名称进行运行时检索。[QMetaType::type](#static-int-qmetatypetypeconst-char-typename)() 会稍慢一些，但即使类型未注册也能编译成功。

此函数在 Qt 4.1 中被引入。

**另请参阅：**[Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 和 [QMetaType::type](#static-int-qmetatypetypeconst-char-typename)()。

----

### template \<typename T\> int qRegisterMetaType(const char \**typeName*)

将类型 `T` 通过类型名称 `typeName` 注册至元对象系统，并返回 [QMetaType](../../M/QMetaType/QMetaType.md) 使用的类型编号。任何包含一个公共默认构造函数、公共拷贝构造函数、公共析构函数的类或结构体均可被注册。

此函数要求类型 `T` 在此函数调用时被完整定义；对于指针类型，同样要求被指向的类型被完整定义（`译者注：即不可为前置声明类型`）。可以使用 [Q_DECLARE_OPAQUE_POINTER](#qdeclareopaquepointerpointertype)() 来注册前置声明类型的指针类型。

类型被注册后，可以在运行时动态地创建或销毁对象。

下述为注册 `MyClass` 类的示例：

```cpp
qRegisterMetaType<MyClass>("MyClass");
```

此函数可被用于注册类型别名，以便于将别名用于 [QMetaProperty](../../M/QMetaProperty/QMetaProperty.md) 或[队列连接](../../Q/Qt_Namespace/Qt_Namespace.md#enum_QtConnectionType)中。

```cpp
typedef QString CustomString;
qRegisterMetaType<CustomString>("CustomString");
```

**警告：**  此函数仅应被用于注册类型别名，其它场合请使用 [Q_DECLARE_METATYPE](#qdeclaremetatypetype) 和 [qMetaTypeId](#template-typename-t-int-qmetatypeid)()。

**另请参阅：**[qRegisterMetaTypeStreamOperators](#template-typename-t-void-qregistermetatypestreamoperatorsconst-char-typename)()，[isRegistered](#bool-qmetatypeisregistered-const)() 和 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)()。

----

### template \<typename T\> int qRegisterMetaType()

调用此函数来注册类型 `T`。`T` 必须被 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 所声明。返回此类型对应的元类型编号。

示例：

```cpp
int id = qRegisterMetaType<MyStruct>();
```

此函数要求类型 `T` 在此函数调用时被完整定义；对于指针类型，同样要求被指向的类型被完整定义（`译者注：即不可为前置声明类型`）。可以使用 [Q_DECLARE_OPAQUE_POINTER](#qdeclareopaquepointerpointertype)() 来注册前置声明类型的指针类型。

类型被注册后，可以在运行时动态地创建或销毁对象。

为了在 [QVariant](#enum-qmetatypetype) 中使用类型 `T`，使用 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 便已足够。若要在信号槽的队列连接中使用 `T`，则 `qRegisterMetaType<T>()` 必须在第一个连接建立前被调用。

同样地，若要在 [QObject::property](../../O/QObject/QObject.md#qvariant-qobjectpropertyconst-char-name-const)() 中使用 `T`，`qRegisterMetaType<T>()` 必须在这之前被调用。通常在使用到 `T` 的类的构造函数中，或在 `main()` 函数中调用。

此函数在 Qt 4.2 中被引入。

**另请参阅：**[Q_DECLARE_METATYPE](#qdeclaremetatypetype)()。

----

### template \<typename T\> void qRegisterMetaTypeStreamOperators(const char \**typeName*)

通过类型名称 `typeName` 将 `T` 的流运算符注册至元对象系统。

在此之后，该类型可通过 [QMetaType::load](#static-bool-qmetatypeloadqdatastream-stream-int-type-void-data)() 和 [QMetaType::save](#static-bool-qmetatypesaveqdatastream-stream-int-type-const-void-data)() 进行序列化和反序列化。这两个函数在将 [QVariant](#enum-qmetatypetype) 传递至数据流时被调用。

```cpp
qRegisterMetaTypeStreamOperators<MyClass>("MyClass");
```

流运算符需要具有下述的函数签名：

```cpp
QDataStream &operator<<(QDataStream &out, const MyClass &myObj);
QDataStream &operator>>(QDataStream &in, MyClass &myObj);
```

**另请参阅：**[qRegisterMetaType](#template-typename-t-int-qregistermetatype)()，[QMetaType::isRegistered](#bool-qmetatypeisregistered-const)() 和 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)()。

----

### bool operator!=(const [QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype) &*a*, const [QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype) &*b*)

这是一个重载函数。

若 [QMetaType](../../M/QMetaType/QMetaType.md) *a* 的类型与 [QMetaType](../../M/QMetaType/QMetaType.md) *b* 不同则返回 `true`，否则返回`false`。

此函数在 Qt 5.15 中被引入。

----

### bool operator==(const [QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype) &*a*, const [QMetaType](#qmetatypeqmetatypeconst-int-typeid--qmetatypeunknowntype) &*b*)

这是一个重载函数。

若 [QMetaType](../../M/QMetaType/QMetaType.md) *a* 的类型与 [QMetaType](../../M/QMetaType/QMetaType.md) *b* 相同则返回 `true`，否则返回`false`。

此函数在 Qt 5.15 中被引入。



## 宏定义文档

### Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE(*Container*)

此宏令容器类型 `Container` 作为关联型容器被注册至 [QMetaType](../../M/QMetaType/QMetaType.md)，即允许将 `Container<T, U>` 实例存入 [QVariant](#enum-qmetatypetype)，前提是 `T` 和 `U` 也已经被注册为 [QMetaType](../../M/QMetaType/QMetaType.md)。

**注意：** 所有 Qt 的关联型容器已被内置支持，无需使用此宏进行声明。`std::map` 容器也已被内置支持。

下述代码展示了 `Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE`() 的典型用法：

```cpp
#include <unordered_list>

Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE(std::unordered_map)

void someFunc()
{
    std::unordered_map<int, bool> container;
    QVariant var = QVariant::fromValue(container);
    // ...
}
```

> 译者注：
>
> 用户的自定义类型只需要通过 `Q_DECLARE_METATYPE(T)` 注册后，即可被已注册的所有容器使用，无需再注册 `Q_DECLARE_METATYPE(QMap<QString, T>)`。

----

### Q_DECLARE_METATYPE(*Type*)

此宏将类型 `Type` 注册至 [QMetaType](../../M/QMetaType/QMetaType.md) ，前提是该类型具备一个公共默认构造函数、公共拷贝构造函数和公共析构函数。这是把类型 `Type` 用于 [QVariant](#enum-qmetatypetype) 的前提。

此宏要求类型 `T` 在此函数调用时被完整定义；对于指针类型，同样要求被指向的类型被完整定义（`译者注：即不可为前置声明类型`）。可以使用 [Q_DECLARE_OPAQUE_POINTER](#qdeclareopaquepointerpointertype)() 来注册前置声明类型的指针类型。

理想情况下，此宏应被放置在该类型的声明位置之后。若不可行的话，也可以将其放置在一个私有头文件中，然后在每次在 [QVariant](#enum-qmetatypetype) 中使用此类型之前包含该头文件。

`Q_DECLARE_METATYPE`() 使此类型可被所有基于模板的函数使用，包括 [QVariant](#enum-qmetatypetype) 中的模板函数。注意，若想在信号槽的队列连接或 [QObject](../../O/QObject/QObject.md) 的属性系统中使用此类型，则还需要调用 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)()，因为该类型的名称会在运行时被解析。

此示例为 `Q_DECLARE_METATYPE`() 的典型用法：

```cpp
struct MyStruct
{
    int i;
    ...
};

Q_DECLARE_METATYPE(MyStruct)
```

若 `MyStruct` 处于命名空间中，则 `Q_DECLARE_METATYPE`() 宏必须在命令空间外使用：

```cpp
namespace MyNamespace
{
    ...
}

Q_DECLARE_METATYPE(MyNamespace::MyStruct)
```

当 `MyStruct` 被注册至 [QMetaType](../../M/QMetaType/QMetaType.md) 后，便可将其用于 [QVariant](#enum-qmetatypetype) 中”

```cpp
MyStruct s;
QVariant var;
var.setValue(s); // 将 v 拷贝至 QVariant

...

// 获取类型值
MyStruct s2 = var.value<MyStruct>();
```

下述类型已被自动注册，无需使用此宏：

- 继承自 [QObject](../../O/QObject/QObject.md) 的类型的指针；
- [QList](../../L/QList/QList.md)\<T\>，[QVector](../../V/QVector/QVector.md)\<T\>，[QQueue](../../Q/QQueue/QQueue.md)\<T\>，[QStack](../../S/QStack/QStack.md)\<T\>，[QSet](../../S/QSet/QSet.md)\<T\> 或 [QLinkedList](../../L/QLinkedList/QLinkedList.md)\<T\>，前提是 `T` 被注册为元类型；
- [QHash](https://doc.qt.io/qt-5/qhash.html#qhash)\<T1, T2\>，[QMap](../../M/QMap/QMap.md)\<T1, T2\> 或 [QPair](../../P/QPair/QPair.md)\<T1, T2\>，前提是 `T1` 和 `T2` 都被注册为元类型；
- [QPointer](../../P/QPointer/QPointer.md)\<T\>，[QSharedPointer](../../S/QSharedPointer/QSharedPointer.md)\<T\>，[QWeakPointer](../../W/QWeakPointer/QWeakPointer.md)\<T\>，前提是 `T` 为 [QObject](../../O/QObject/QObject.md) 的子类；
- 通过 [Q_ENUM](../../O/QObject/QObject.md#qenum) 或 [Q_FLAG](../../O/QObject/QObject.md#qflag) 注册的枚举类型；
- 包含 [Q_GADGET](../../O/QObject/QObject.md#qgadget) 宏的类。

**另请参阅：**[qRegisterMetaType](#template-typename-t-int-qregistermetatype)()。

----

### Q_DECLARE_OPAQUE_POINTER(*PointerType*)

此宏使得前置声明类型的指针类型 `PointerType` 可被 [Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 或 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)() 注册至 [QMetaType](../../M/QMetaType/QMetaType.md)。

此函数在 Qt 5.0 中被引入。

**另请参阅：**[Q_DECLARE_METATYPE](#qdeclaremetatypetype)() 和 [qRegisterMetaType](#template-typename-t-int-qregistermetatype)()。

---

### Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE(*Container*)

此宏令容器类型 `Container` 作为顺序容器被注册至 [QMetaType](../../M/QMetaType/QMetaType.md)，即允许将 `Container<T>` 实例存入 [QVariant](#enum-qmetatypetype)，前提是 `T` 已经被注册为 [QMetaType](../../M/QMetaType/QMetaType.md)。

**注意：** 所有 Qt 的顺序容器已被内置支持，无需使用此宏进行声明。`std::vector` 和 `std::list` 容器已也被内置支持。

下述代码展示了 `Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE`() 的典型用法：

```cpp
#include <deque>

Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE(std::deque)

void someFunc()
{
    std::deque<QFile*> container;
    QVariant var = QVariant::fromValue(container);
    // ...
}
```

> 译者注：
>
> 用户的自定义类型只需要通过 `Q_DECLARE_METATYPE(T)` 注册后，即可被已注册的所有容器使用，无需再注册 `Q_DECLARE_METATYPE(QVector<T>)`。

----

### Q_DECLARE_SMART_POINTER_METATYPE(*SmartPointer*)

此宏令智能指针类型 `SmartPointer` 作为智能指针被注册至 [QMetaType](../../M/QMetaType/QMetaType.md)，即允许将 `Container<T>` 实例存入 [QVariant](#enum-qmetatypetype)，前提是 `T` 已经被注册为 [QMetaType](../../M/QMetaType/QMetaType.md)。

**注意：**[QWeakPointer](../../W/QWeakPointer/QWeakPointer.md)，[QSharedPointer](../../S/QSharedPointer/QSharedPointer.md) 和 [QPointer](../../P/QPointer/QPointer.md) 已被内置支持，无需使用此宏进行声明。

下述代码展示了 `Q_DECLARE_SMART_POINTER_METATYPE`() 的典型用法：

```cpp
#include <memory>

Q_DECLARE_SMART_POINTER_METATYPE(std::shared_ptr)

void someFunc()
{
    auto smart_ptr = std::make_shared<QFile>();
    QVariant var = QVariant::fromValue(smart_ptr);
    // ...
    if (var.canConvert<QObject*>()) {
        QObject *sp = var.value<QObject*>();
        qDebug() << sp->metaObject()->className(); // Prints 'QFile'.
    }
}
```

> 译者注：
>
> 用户继承自 QObject 的自定义类型可直接被已注册的智能指针使用，无需再注册 `Q_DECLARE_METATYPE(QSharedPointer<T>)`。
>
> 与容器不同的是，通过 `Q_DECLARE_METATYPE(T)` 注册的自定义类型无法直接被已注册的智能指针使用，必须单独注册 `Q_DECLARE_METATYPE(QSharedPointer<T>)`。



## 已废弃成员

**[QMetaType](../QMetaType/QMetaType.md) 类的以下成员已被废弃。**它们仅为了保证老代码能够运行而保留，我们强烈反对在新代码中使用。



### 静态公共成员

| 返回类型            | 函数                                                         |
| ------------------- | ------------------------------------------------------------ |
| `(obsolete) `void * | **[construct](#static-void-qmetatypeconstructint-type-const-void-copy--nullptr)**(int *type*, const void **copy* = nullptr) |



### 成员函数文档

#### *[static]* void \*QMetaType::construct(int *type*, const void \**copy* = nullptr)

在给定的内存地址 `where` 上构造对应 `type` 类型的对象，该对象是 `copy` 的副本，并返回 `where`。若 `copy` 是空指针，则执行默认构造。

这是用于显示管理存储 `type` 类型对象的内存的底层函数。若不需要此类底层控制，则考虑使用 [create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)() 函数（也就是指，使用 `new` 而非 `placement new`）。

您必须确保 `where` 指向的内存区域大小足够存储 `type` 对应的数据，并且 `where` 地址需要对齐，对应类型的大小可通过 [sizeOf](#int-qmetatypesizeof-const)() 获取。

内存对齐的规则是对齐至类型的自然边界，也就是大于等于类型大小的2的n次方值，直至平台有效对齐宽度上限为止。对于特定用途来说，超过 `2 * sizeof(void*)` 的对齐宽度只是某些特定硬件指令所必需的（例如，x86 平台中对齐后的 SSE 读取和存储）。

此函数在 Qt 5.0 中被引入。



此函数已被废弃，仅为了保证老代码能够运行而保留，我们强烈反对在新代码中使用。

构造对应 `type` 类型的对象，该对象是 `copy` 的副本。`copy` 的默认值是 `nullptr`。

已弃用，该用新的静态函数 [QMetaType::create](#static-void-qmetatypecreateint-type-const-void-copy--nullptr)(int type, const void *copy)。

