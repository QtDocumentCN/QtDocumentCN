# QSerialPortInfo 类

QSerialPortInfo 类提供了系统中现有串口的相关信息。 [更多内容...](https://doc.qt.io/qt-5/qserialportinfo.html#details)

|属性|方法|
|----:|:----|
|头文件:|`#include <QSerialPortInfo>`|
|qmake:|`QT += serialport`|
|始自:|Qt 5.1|

- [列出所有成员, 包括子类成员](https://doc.qt.io/qt-5/qserialportinfo-members.html)
- [废弃的类](https://doc.qt.io/qt-5/qserialportinfo-obsolete.html)



## 公共成员函数

|返回类型|函数名|
|----:|:----|
||**[QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo-3)**(const QSerialPortInfo &*other*)|
|| **[QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo-2)**(const QString &*name*) |
|                   | **[QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo-1)**(const QSerialPort &*port*) |
|                   | **[QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo)**() |
| QSerialPortInfo & | **[operator=](https://doc.qt.io/qt-5/qserialportinfo.html#operator-eq)**(const QSerialPortInfo &*other*) |
|                   | **[~QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#dtor.QSerialPortInfo)**() |
|           QString | **[description](https://doc.qt.io/qt-5/qserialportinfo.html#description)**() const |
|              bool | **[hasProductIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasProductIdentifier)**() const |
|              bool | **[hasVendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasVendorIdentifier)**() const |
|              bool | **[isNull](https://doc.qt.io/qt-5/qserialportinfo.html#isNull)**() const |
|           QString | **[manufacturer](https://doc.qt.io/qt-5/qserialportinfo.html#manufacturer)**() const |
|           QString | **[portName](https://doc.qt.io/qt-5/qserialportinfo.html#portName)**() const |
|           quint16 | **[productIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#productIdentifier)**() const |
|           QString | **[serialNumber](https://doc.qt.io/qt-5/qserialportinfo.html#serialNumber)**() const |
|              void | **[swap](https://doc.qt.io/qt-5/qserialportinfo.html#swap)**(QSerialPortInfo &*other*) |
|           QString | **[systemLocation](https://doc.qt.io/qt-5/qserialportinfo.html#systemLocation)**() const |
|           quint16 | **[vendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#vendorIdentifier)**() const |



## 静态公共成员函数

|返回类型|函数名|
|----:|:----|
|QList<QSerialPortInfo>|**[availablePorts](https://doc.qt.io/qt-5/qserialportinfo.html#availablePorts)**()|
|QList<qint32>|**[standardBaudRates](https://doc.qt.io/qt-5/qserialportinfo.html#standardBaudRates)**()|



## 详细描述

使用静态函数生成 QSerialPortInfo 类实例对象列表。列表中的每一个对象代表一个串口设备，可以通过串口名、系统地址、设备描述以及制造商查询串口。 QSerialPortInfo 类还可以用作 [QSerialPort](https://doc.qt.io/qt-5/qserialport.html) 类成员方法 setPort() 的输入参数。

**另请参阅** [QSerialPort](https://doc.qt.io/qt-5/qserialport.html).



## 成员函数文档

### QSerialPortInfo::QSerialPortInfo(const [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo) &*other*)

---

构造 QSerialPortInfo 类实例 *other* 的副本。

### QSerialPortInfo::QSerialPortInfo(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

---

构造串口名为 *name* 的 QSerialPortInfo 类实例。

该构造函数在现有的串口设备中按照名称检索名为 *name* 的串口，找到后为那个串口构造串口信息类实例。

### QSerialPortInfo::QSerialPortInfo(const [QSerialPort](https://doc.qt.io/qt-5/qserialport.html) &*port*)

---

从串口 *port* 构造 QSerialPortInfo 类实例。

### QSerialPortInfo::QSerialPortInfo()

---

构造一个空的 QSerialPortInfo 类实例。

**另请参阅** [isNull](https://doc.qt.io/qt-5/qserialportinfo.html#isNull)().

### [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo) &QSerialPortInfo::operator=(const [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo) &*other*)

---

将 QSerialPortInfo 类实例 *other* 赋值给另一个 QSerialPortInfo 类实例。

### QSerialPortInfo::~QSerialPortInfo()

---

销毁 QSerialPortInfo 类实例，销毁后该实例的引用无效。

### [static] [QList](https://doc.qt.io/qt-5/qlist.html)[<QSerialPortInfo>](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo) QSerialPortInfo::availablePorts()

---

该函数返回系统中现有串口设备列表。

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPortInfo::description() const

---

该函数返回描述串口的字符串，若没有描述字符串，则返回空字符串。

**另请参阅** [manufacturer](https://doc.qt.io/qt-5/qserialportinfo.html#manufacturer)() 和 [serialNumber](https://doc.qt.io/qt-5/qserialportinfo.html#serialNumber)().

### bool QSerialPortInfo::hasProductIdentifier() const

---

若串口设备有`16`位产品编号，函数返回`true`，否则返回`false`。

**另请参阅** [productIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#productIdentifier)(), [vendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#vendorIdentifier)(), 和 [hasVendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasVendorIdentifier)().

### bool QSerialPortInfo::hasVendorIdentifier() const

---

若串口设备有`16`位厂商编号，函数返回`true`，否则返回`false`。

**另请参阅** [vendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#vendorIdentifier)(), [productIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#productIdentifier)(), 和 [hasProductIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasProductIdentifier)().

### bool QSerialPortInfo::isNull() const

---

若 QSerialPortInfo 类实例没有串口定义，函数返回`true`，否则返回`false`。

**另请参阅** [isBusy](https://doc.qt.io/qt-5/qserialportinfo-obsolete.html#isBusy)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPortInfo::manufacturer() const

---

返回串口设备制造商字符串，若该串口没有制造商字符串，则返回空字符串。

**另请参阅** [description](https://doc.qt.io/qt-5/qserialportinfo.html#description)() 和 [serialNumber](https://doc.qt.io/qt-5/qserialportinfo.html#serialNumber)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPortInfo::portName() const

---

返回串口名。

**另请参阅** [systemLocation](https://doc.qt.io/qt-5/qserialportinfo.html#systemLocation)().

### [quint16](https://doc.qt.io/qt-5/qtglobal.html#quint16-typedef) QSerialPortInfo::productIdentifier() const

---

若串口设备有`16`位产品编号，函数返回产品编号，否则返回`0`。

**另请参阅** [hasProductIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasProductIdentifier)(), [vendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#vendorIdentifier)(), 和 [hasVendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasVendorIdentifier)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPortInfo::serialNumber() const

---

若串口设备有序列号，函数返回序列号字符串，否则返回空字符串。

**注意**: 串口序列号可能包含字母。

该函数从 Qt 5.3 开始使用。

**另请参阅** [description](https://doc.qt.io/qt-5/qserialportinfo.html#description)() 和 [manufacturer](https://doc.qt.io/qt-5/qserialportinfo.html#manufacturer)().

### [static] [QList](https://doc.qt.io/qt-5/qlist.html)[<qint32>](https://doc.qt.io/qt-5/qtglobal.html#qint32-typedef) QSerialPortInfo::standardBaudRates()

---

返回目标操作系统支持的标准串口通信波特率列表。

### void QSerialPortInfo::swap([QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html#QSerialPortInfo) &*other*)

---

用 [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html) 类实例 *other* 与当前 [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html) 类实例互换。此操作非常快并且从不失败。

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPortInfo::systemLocation() const

---

返回串口设备的系统地址。

**另请参阅** [portName](https://doc.qt.io/qt-5/qserialportinfo.html#portName)().

### [quint16](https://doc.qt.io/qt-5/qtglobal.html#quint16-typedef) QSerialPortInfo::vendorIdentifier() const

---

若串口设备有`16`位厂商编号，函数返回厂商编号，否则返回`0`。

**另请参阅** [hasVendorIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasVendorIdentifier)(), [productIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#productIdentifier)(), 和 [hasProductIdentifier](https://doc.qt.io/qt-5/qserialportinfo.html#hasProductIdentifier)().