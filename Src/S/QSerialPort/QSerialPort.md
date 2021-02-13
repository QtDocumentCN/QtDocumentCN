# QSerialPort 类

QSerialPort 类用于访问串口。 [更多内容...](https://doc.qt.io/qt-5/qserialport.html#details)

|属性|方法|
|----:|:----|
|头文件:|`#include <QSerialPort>`|
|qmake:|`QT += serialport`|
|父类:|[QIODevice](https://doc.qt.io/qt-5/qiodevice.html)|

- [列出所有成员, 包括子类成员](https://doc.qt.io/qt-5/qserialport-members.html)
- [废弃的类](https://doc.qt.io/qt-5/qserialport-obsolete.html)

**注意:** 该类中的所有函数均为 [reentrant](https://doc.qt.io/qt-5/threads-reentrancy.html).



## 公共成员类型

|类型|方法|
|----:|:----|
|enum|[**BaudRate**](https://doc.qt.io/qt-5/qserialport.html#BaudRate-enum) {Baud1200, Baud2400, Baud4800, Baud9600, Baud19200, …, UnknownBaud }|
|enum|[**DataBits**](https://doc.qt.io/qt-5/qserialport.html#DataBits-enum) { Data5, Data6, Data7, Data8, UnknownDataBits }|
|enum|[**Direction**](https://doc.qt.io/qt-5/qserialport.html#Direction-enum) { Input, Output, AllDirections }|
|flags|[**Directions**](https://doc.qt.io/qt-5/qserialport.html#Direction-enum)|
|enum|[**FlowControl**](https://doc.qt.io/qt-5/qserialport.html#FlowControl-enum) { NoFlowControl, HardwareControl, SoftwareControl, UnknownFlowControl }|
|enum|[**Parity**](https://doc.qt.io/qt-5/qserialport.html#Parity-enum) { NoParity, EvenParity, OddParity, SpaceParity, MarkParity, UnknownParity }|
|enum|[**PinoutSignal**](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum) { NoSignal, TransmittedDataSignal, ReceivedDataSignal,  DataTerminalReadySignal, DataCarrierDetectSignal, …,  SecondaryReceivedDataSignal }|
|flags|[**PinoutSignals**](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum)|
|enum|[**SerialPortError**](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) { NoError, DeviceNotFoundError, PermissionError, OpenError, NotOpenError, …, UnknownError }|
|enum|[**StopBits**](https://doc.qt.io/qt-5/qserialport.html#StopBits-enum) { OneStop, OneAndHalfStop, TwoStop, UnknownStopBits }|



## 属性

|属性名|类型|
|----:|:----|
|[**baudRate**](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop)|qint32|
|[**breakEnabled**](https://doc.qt.io/qt-5/qserialport.html#breakEnabled-prop)|bool|
|[**dataBits**](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop)|dataBits|
|[**dataTerminalReady**](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop)|bool|
|[**error**](https://doc.qt.io/qt-5/qserialport.html#error-prop)|SerialPortError|
|[**flowControl**](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop)|FlowControl|
|[**parity**](https://doc.qt.io/qt-5/qserialport.html#parity-prop)|Parity|
|[**requestToSend**](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop)|bool|
|[**stopBits**](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop)|StopBits|



## 公共成员函数

|返回类型|函数名|
|----:|:----|
||[**QSerialPort**](https://doc.qt.io/qt-5/qserialport.html#QSerialPort-2)(const QSerialPortInfo &*serialPortInfo*, QObject **parent* = nullptr)|
||[**QSerialPort**](https://doc.qt.io/qt-5/qserialport.html#QSerialPort-1)(const QString &*name*, QObject **parent* = nullptr)|
||[**QSerialPort**](QObject **parent* = nullptr)|
|virtual|[**~QSerialPort**](https://doc.qt.io/qt-5/qserialport.html#dtor.QSerialPort)()|
|qint32|[**baudRate**](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop)(QSerialPort::Directions *directions* = AllDirections) const|
|                         bool | [**clear**](https://doc.qt.io/qt-5/qserialport.html#clear)(QSerialPort::Directions *directions* = AllDirections) |
|                         void | [**clearError**](https://doc.qt.io/qt-5/qserialport.html#error-prop)() |
|        QSerialPort::DataBits | [**dataBits**](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop)() const |
| QSerialPort::SerialPortError | [**error**](https://doc.qt.io/qt-5/qserialport.html#error-prop)() const |
|     QSerialPort::FlowControl | **[flowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop)**() const |
|                         bool | **[flush](https://doc.qt.io/qt-5/qserialport.html#flush)**() |
|          QSerialPort::Handle | **[handle](https://doc.qt.io/qt-5/qserialport.html#handle)**() const |
|                         bool | **[isBreakEnabled](https://doc.qt.io/qt-5/qserialport.html#breakEnabled-prop)**() const |
|                         bool | **[isDataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop)**() |
|                         bool | **[isRequestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop)**() |
|          QSerialPort::Parity | **[parity](https://doc.qt.io/qt-5/qserialport.html#parity-prop)**() const |
|   QSerialPort::PinoutSignals | **[pinoutSignals](https://doc.qt.io/qt-5/qserialport.html#pinoutSignals)**() |
|                      QString | **[portName](https://doc.qt.io/qt-5/qserialport.html#portName)**() const |
|                       qint64 | **[readBufferSize](https://doc.qt.io/qt-5/qserialport.html#readBufferSize)**() const |
|                         bool | **[sendBreak](https://doc.qt.io/qt-5/qserialport.html#sendBreak)**(int *duration* = 0) |
|                         bool | **[setBaudRate](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop)**(qint32 *baudRate*, QSerialPort::Directions *directions* = AllDirections) |
|                         bool | **[setBreakEnabled](https://doc.qt.io/qt-5/qserialport.html#breakEnabled-prop)**(bool *set* = true) |
|                         bool | **[setDataBits](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop)**(QSerialPort::DataBits *dataBits*) |
|                         bool | **[setDataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop)**(bool *set*) |
|                         bool | **[setFlowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop)**(QSerialPort::FlowControl *flowControl*) |
|                         bool | **[setParity](https://doc.qt.io/qt-5/qserialport.html#parity-prop)**(QSerialPort::Parity *parity*) |
|                         void | **[setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)**(const QSerialPortInfo &*serialPortInfo*) |
|                         void | **[setPortName](https://doc.qt.io/qt-5/qserialport.html#setPortName)**(const QString &*name*) |
|                         void | **[setReadBufferSize](https://doc.qt.io/qt-5/qserialport.html#setReadBufferSize)**(qint64 *size*) |
|                         bool | **[setRequestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop)**(bool *set*) |
|                         bool | **[setStopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop)**(QSerialPort::StopBits *stopBits*) |
|        QSerialPort::StopBits | **[stopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop)**() const |



## 重写公共成员函数

|返回类型|函数名|
|----:|:----|
|virtual bool|**[atEnd](https://doc.qt.io/qt-5/qserialport.html#atEnd)**() const override|
|virtual qint64|**[bytesAvailable](https://doc.qt.io/qt-5/qserialport.html#bytesAvailable)**() const override|
|virtual qint64|**[bytesToWrite](https://doc.qt.io/qt-5/qserialport.html#bytesToWrite)**() const override|
|virtual bool|**[canReadLine](https://doc.qt.io/qt-5/qserialport.html#canReadLine)**() const override|
|virtual void|**[close](https://doc.qt.io/qt-5/qserialport.html#close)**() override|
|virtual bool|**[isSequential](https://doc.qt.io/qt-5/qserialport.html#isSequential)**() const override|
|virtual bool|**[open](https://doc.qt.io/qt-5/qserialport.html#open)**(QIODevice::OpenMode *mode*) override|
|virtual bool|**[waitForBytesWritten](https://doc.qt.io/qt-5/qserialport.html#waitForBytesWritten)**(int *msecs* = 30000) override|
|virtual bool|**[waitForReadyRead](https://doc.qt.io/qt-5/qserialport.html#waitForReadyRead)**(int *msecs* = 30000) override|



## 信号

|返回类型|函数名|
|----:|:----|
|void|**[baudRateChanged](https://doc.qt.io/qt-5/qserialport.html#baudRateChanged)**(qint32 *baudRate*, QSerialPort::Directions *directions*)|
|void|**[breakEnabledChanged](https://doc.qt.io/qt-5/qserialport.html#breakEnabled-prop)**(bool *set*)|
|void|**[dataBitsChanged](https://doc.qt.io/qt-5/qserialport.html#dataBitsChanged)**(QSerialPort::DataBits *dataBits*)|
|void|**[dataTerminalReadyChanged](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReadyChanged)**(bool *set*)|
|void|**[errorOccurred](https://doc.qt.io/qt-5/qserialport.html#errorOccurred)**(QSerialPort::SerialPortError *error*)|
|void|**[flowControlChanged](https://doc.qt.io/qt-5/qserialport.html#flowControlChanged)**(QSerialPort::FlowControl *flow*)|
|void|**[parityChanged](https://doc.qt.io/qt-5/qserialport.html#parityChanged)**(QSerialPort::Parity *parity*)|
|void|**[requestToSendChanged](https://doc.qt.io/qt-5/qserialport.html#requestToSendChanged)**(bool *set*)|
|void|**[stopBitsChanged](https://doc.qt.io/qt-5/qserialport.html#stopBitsChanged)**(QSerialPort::StopBits *stopBits*)|



## 重写保护成员函数

|返回类型|函数名|
|----:|:----|
|virtual qint64|**[readData](https://doc.qt.io/qt-5/qserialport.html#readData)**(char **data*, qint64 *maxSize*) override|
|virtual qint64|**[readLineData](https://doc.qt.io/qt-5/qserialport.html#readLineData)**(char **data*, qint64 *maxSize*) override|
|virtual qint64|**[writeData](https://doc.qt.io/qt-5/qserialport.html#writeData)**(const char **data*, qint64 *maxSize*) override|



## 详细描述

您可以使用 [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html) 帮助类来获取可用串口的信息，这个类可以枚举系统中的所有串口，当您想使用某个串口时，使用这个类可以获得正确的串口名。可以通过把 QSerialPortInfo 类实例对象作为参数传递给  [setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)() 或 [setPortName](https://doc.qt.io/qt-5/qserialport.html#setPortName)() 方法来指定串口设备。

串口设置完毕以后，可以使用 [open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法以只读 (r/o)、只写 (w/o)、读写 (r/w) 模式打开串口。

**注意**: 串口总是以独占访问的方式打开，即其它进程或线程无法访问已经打开的串口。

请使用 [close](https://doc.qt.io/qt-5/qserialport.html#close)() 方法来关闭串口或取消串口读写操作。

串口打开以后，`QSerialPort` 会检查串口当前的配置并初始化。您可以使用 [setBaudRate](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop)(), [setDataBits](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop)(), [setParity](https://doc.qt.io/qt-5/qserialport.html#parity-prop)(), [setStopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop)(), 和 [setFlowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop)() 方法重新配置串口。

[QSerialPort::dataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop) 和 [QSerialPort::requestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop) 属性用来设置串口引脚信号，还可以使用 [pinoutSignals](https://doc.qt.io/qt-5/qserialport.html#pinoutSignals)() 方法来查询串口引脚信号。

当串口准备好时，可以用 [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 或 [write](https://doc.qt.io/qt-5/qiodevice.html#write)() 方法来读写串口。您还可以使用 [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)() 和 [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)() 这样的便捷方法读写串口。如果数据没有一次读完，剩下的数据会被接下来有新数据被添加至 `QSerialPort` 内部读缓冲器时再读出。您可以使用 [setReadBufferSize](https://doc.qt.io/qt-5/qserialport.html#setReadBufferSize)() 方法来设置串口读缓冲区的大小。

`QSerialPort` 提供了一组函数来暂停线程调用直到触发特定的信号。这些函数可以用来阻塞串口：

- [waitForReadyRead](https://doc.qt.io/qt-5/qserialport.html#waitForReadyRead)() 函数阻塞线程调用直到串口有新数据准备读出
- [waitForBytesWritten](https://doc.qt.io/qt-5/qserialport.html#waitForBytesWritten)() 函数阻塞线程调用直到有新数据被写进串口

阻塞串口代码示例：

```c++
int numRead = 0, numReadTotal = 0;
char buffer[50];

for (;;) {
    numRead  = serial.read(buffer, 50);

    // Do whatever with the array

    numReadTotal += numRead;
    if (numRead == 0 && !serial.waitForReadyRead())
        break;
}
```

如果 [waitForReadyRead()](https://doc.qt.io/qt-5/qiodevice.html#waitForReadyRead) 返回 `false`，说明串口连接已经关闭或者有错误出现。

如果串口出现错误，`QSerialPort` 将会发射 [errorOccurred](https://doc.qt.io/qt-5/qserialport.html#errorOccurred)() 信号。您还可以调用 [error](https://doc.qt.io/qt-5/qserialport.html#error-prop)() 方法来查询串口最近一次出现错误的类型。

**注意**: 在 `QSerialPort` 中，并非所有的错误都是以操作系统平台无关的方式处理。诸如帧、奇偶校验、终止条件这样的错误需要由应用程序代码来处理，可能需要使用设备描述符中的操作系统相关的 `ioctls` 和(或)解析串口数据流中的字节填充。 

编程阻塞串口与编程非阻塞串口完全不同。阻塞串口不需要事件循环，通常会让编程更简单。然而，在图形用户界面程序中，阻塞串口应该仅用于非图形用户界面线程，这样做可以避免用户界面卡顿。

若想更深入了解这方面内容，请参考 [example](https://doc.qt.io/qt-5/qtserialport-examples.html) 中的例程。

`QSerialPort` 类还可以与 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 和 [QDataStream](https://doc.qt.io/qt-5/qdatastream.html) 的流运算符(`<<()`和`>>()`)一起使用。有一点需要注意：在使用流运算符 `>>()` 之前请确保串口缓冲区有足够多的数据可读。

**另请参阅** [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html).



## 成员类型文档

### enum QSerialPort::BaudRate

---

该枚举描述了串口通信波特率。

**注意**: 该枚举仅列出了最常用的串口通信波特率。

|            常量            |    值    | 描述                                                         |
| :------------------------: | :------: | ------------------------------------------------------------ |
|  `QSerialPort::Baud1200`   |  `1200`  | 1200 比特/秒                                                 |
|  `QSerialPort::Baud2400`   |  `2400`  | 2400 比特/秒                                                 |
|  `QSerialPort::Baud4800`   |  `4800`  | 4800 比特/秒                                                 |
|  `QSerialPort::Baud9600`   |  `9600`  | 9600 比特/秒                                                 |
|  `QSerialPort::Baud19200`  | `19200`  | 19200 比特/秒                                                |
|  `QSerialPort::Baud38400`  | `38400`  | 38400 比特/秒                                                |
|  `QSerialPort::Baud57600`  | `57600`  | 57600 比特/秒                                                |
| `QSerialPort::Baud115200`  | `115200` | 115200 比特/秒                                               |
| `QSerialPort::UnknownBaud` |   `-1`   | 波特率未知。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |

**另请参阅** [QSerialPort::baudRate](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop).

### enum QSerialPort::DataBits

---

该枚举描述了每个字符所使用的数据比特数。

|              常量              |  值  | 描述                                                         |
| :----------------------------: | :--: | ------------------------------------------------------------ |
|      `QSerialPort::Data5`      | `5`  | 每个字符用5比特表示，用于波特码，常见于旧式设备，例如电传打字机 |
|      `QSerialPort::Data6`      | `6`  | 每个字符用6比特表示，很少这样用                              |
|      `QSerialPort::Data7`      | `7`  | 每个字符用7比特表示，用于ASCII码，常见于旧式设备，例如电传打字机 |
|      `QSerialPort::Data8`      | `8`  | 每个字符用8比特表示，大部分数据采用此格式，因为1个字节包含8比特。它在新应用中广泛使用 |
| `QSerialPort::UnknownDataBits` | `-1` | 比特数未知。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |

**另请参阅** [QSerialPort::dataBits](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop).

### enum QSerialPort::Direction

### flags QSerialPort::Directions

---

该枚举描述了串口数据传输方向。

**注意**: 在某些操作系统中(例如类 POSIX 系统)，该枚举对串口的输入/输出波特率单独设置。

|             常量             |        值        | 描述               |
| :--------------------------: | :--------------: | ------------------ |
|     `QSerialPort::Input`     |       `1`        | 输入方向           |
|    `QSerialPort::Output`     |       `2`        | 输出方向           |
| `QSerialPort::AllDirections` | `Input | Output` | 输入和输出同时进行 |

方向类型是 [QFlags](https://doc.qt.io/qt-5/qflags.html)<Direction> 的类型定义(`typedef`)，它保存了方向值的 OR 组合。

### enum QSerialPort::FlowControl

---

该枚举描述了串口使用的流控制方式。

|               常量                |  值  | 描述                                                         |
| :-------------------------------: | :--: | ------------------------------------------------------------ |
|   `QSerialPort::NoFlowControl`    | `0`  | 没有流控制                                                   |
|  `QSerialPort::HardwareControl`   | `1`  | 硬件流控制 (RTS/CTS)                                         |
|  `QSerialPort::SoftwareControl`   | `2`  | 软件流控制 (XON/XOFF)                                        |
| `QSerialPort::UnknownFlowControl` | `-1` | 流控制未知。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |

**另请参阅** [QSerialPort::flowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop).

### enum QSerial::Parity

---

该枚举描述了串口使用的奇偶校验模式。

|             常量             |  值  | 描述                                                         |
| :--------------------------: | :--: | ------------------------------------------------------------ |
|   `QSerialPort::NoParity`    | `0`  | 没有奇偶校验。这是最常见的奇偶校验设置。错误检测由通信协议完成 |
|  `QSerialPort::EvenParity`   | `2`  | 每个字符包含1比特奇偶校验，字符比特数为偶数(含奇偶校验位)    |
|   `QSerialPort::OddParity`   | `3`  | 每个字符包含1比特奇偶校验，字符比特数为奇数(含奇偶校验位)。它确保了每个字符至少有一次状态转换 |
|  `QSerialPort::SpaceParity`  | `4`  | 间隔奇偶校验。奇偶校验位在间隔信号中发送。它不提供错误检测信息 |
|  `QSerialPort::MarkParity`   | `5`  | 标志奇偶校验。奇偶校验位总是被置为标志信号(逻辑 `1`)。它不提供错误检测信息 |
| `QSerialPort::UnknownParity` | `-1` | 奇偶校验未知。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |

**另请参阅** [QSerialPort::parity](https://doc.qt.io/qt-5/qserialport.html#parity-prop).

### enum QSerialPort::PinoutSignal

### flags QSerialPort::PinoutSignals

---

该枚举用于描述串口引脚信号。

|                     常量                      |   值    | 描述                                                         |
| :-------------------------------------------: | :-----: | ------------------------------------------------------------ |
|            `QSerialPort::NoSignal`            | `0x00`  | 无信号                                                       |
|     `QSerialPort::TransmittedDataSignal`      | `0x01`  | TxD (发送数据)。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |
|       `QSerialPort::ReceivedDataSignal`       | `0x02`  | RxD (接收数据)。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |
|    `QSerialPort::DataTerminalReadySignal`     | `0x04`  | DTR (数据终端就绪)                                           |
|    `QSerialPort::DataCarrierDetectSignal`     | `0x08`  | DCD (数据载波检测)                                           |
|       `QSerialPort::DataSetReadySignal`       | `0x10`  | DSR (数据就绪)                                               |
|      `QSerialPort::RingIndicatorSignal`       | `0x20`  | RNG (振铃提示)                                               |
|      `QSerialPort::RequestToSendSignal`       | `0x40`  | RTS (请求发送)                                               |
|       `QSerialPort::ClearToSendSignal`        | `0x80`  | CTS (清除发送)                                               |
| `QSerialPort::SecondaryTransmittedDataSignal` | `0x100` | STD (辅助发送数据)                                           |
|  `QSerialPort::SecondaryReceivedDataSignal`   | `0x200` | SRD (辅助接收数据)                                           |

`PinoutSignals`类型是 [QFlags](https://doc.qt.io/qt-5/qflags.html)<PinoutSignal> 的类型定义(`typedef`)，它保存了`PinoutSignal`值的 OR 组合。

**另请参阅** [pinoutSignals](https://doc.qt.io/qt-5/qserialport.html#pinoutSignals)(), [QSerialPort::dataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop), 和 [QSerialPort::requestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop).

### enum QSerialPort::SerialPortError

---

该枚举描述了 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的错误类型。

|                   常量                   |  值  | 描述                                                         |
| :--------------------------------------: | :--: | ------------------------------------------------------------ |
|          `QSerialPort::NoError`          | `0`  | 没有错误                                                     |
|    `QSerialPort::DeviceNotFoundError`    | `1`  | 尝试打开一个不存在的串口设备                                 |
|      `QSerialPort::PermissionError`      | `2`  | 其它进程试图打开一个已经开启的串口设备或者用户没有足够的权限打开串口 |
|         `QSerialPort::OpenError`         | `3`  | 在当前对象中试图打开一个已经开启的串口                       |
|       `QSerialPort::NotOpenError`        | `13` | 在串口未开启时执行某个操作。这个值从 [QtSerialPort](https://doc.qt.io/qt-5/qtserialport-module.html) 5.2 开始使用 |
|        `QSerialPort::ParityError`        | `4`  | 读串口时硬件检测到奇偶校验错误。这个值已经废弃了。强烈建议您在新开发的代码中不使用这个值 |
|       `QSerialPort::FramingError`        | `5`  | 读串口时硬件检测到帧错误。这个值已经废弃了。强烈建议您在新开发的代码中不使用这个值 |
|    `QSerialPort::BreakConditionError`    | `6`  | 串口输入线上检测到终止条件。这个值已经废弃了。强烈建议您在新开发的代码中不使用这个值 |
|        `QSerialPort::WriteError`         | `7`  | 写串口时出现的 I/O 错误                                      |
|         `QSerialPort::ReadError`         | `8`  | 读串口时出现的 I/O 错误                                      |
|       `QSerialPort::ResourceError`       | `9`  | 当资源无法访问时出现的 I/O 错误。例如：当串口设备意外断开时  |
| `QSerialPort::UnsupportedOperationError` | `10` | 操作系统禁止或不支持请求的串口操作                           |
|       `QSerialPort::TimeoutError`        | `12` | 超时错误。这个值从 [QtSerialPort](https://doc.qt.io/qt-5/qtserialport-module.html) 5.2 开始使用 |
|       `QSerialPort::UnknownError`        | `11` | 未知错误                                                     |

**另请参阅** [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop).

### enum QSerialPort::StopBits

---

该枚举描述了串口停止位的比特数。

|              常量              |  值  | 描述                                                         |
| :----------------------------: | :--: | ------------------------------------------------------------ |
|     `QSerialPort::OneStop`     | `1`  | 1比特停止位                                                  |
| `QSerialPort::OneAndHalfStop`  | `3`  | 1.5比特停止位(仅适用于Windows系统)                           |
|     `QSerialPort::TwoStop`     | `2`  | 2比特停止位                                                  |
| `QSerialPort::UnknownStopBits` | `-1` | 停止位比特数未知。这个值已经废弃了。此处保留是为了兼容旧的代码。强烈建议您在新开发的代码中不使用这个值 |

**另请参阅** [QSerialPort::stopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop).



## 成员属性文档

### baudRate : [qint32](https://doc.qt.io/qt-5/qtglobal.html#qint32-typedef)

---

该属性为串口在指定方向(输入/输出)上的通信波特率。

如果串口波特率设置成功或者打开串口前设置好波特率，那么返回`true`，否则返回`false`并且把错误码置`1`。该错误码可以通过读取 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的值获得。您可以使用枚举 [QSerialPort::BaudRate](https://doc.qt.io/qt-5/qserialport.html#BaudRate-enum) 或者任何 `qint32` 型正整数值设置串口通信波特率。

**注意**: 如果在打开串口前设置该属性，那么真实的串口设置将会在串口打开后，在 [QSerialPort::open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法中自动完成。

**警告**: 所有操作系统均支持 [AllDirections](https://doc.qt.io/qt-5/qserialport.html#Direction-enum) 标志位设置，但 Windows 系统仅支持这种模式。

**警告**: 在 Windows 系统中无论串口输入还是输出，其波特率均相同。

该属性的默认值为 `Baud9600`，即 9600 比特/秒。

**存取函数**:

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|   qint32 | **baudRate**(QSerialPort::Directions *directions* = AllDirections) const |
|     bool | **setBaudRate**(qint32 *baudRate*, QSerialPort::Directions *directions* = AllDirections) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|     void | **[baudRateChanged](https://doc.qt.io/qt-5/qserialport.html#baudRateChanged)**(qint32 *baudRate*, QSerialPort::Directions *directions*) |



### breakEnabled : bool

---

该属性为串口是否终止传输的标志位。

若串口终止通信，则该属性为 `true`，否则为 `false`。

**注意**: 在设置或访问该属性前串口必须已经打开，否则返回 `false` 并且 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码将被置 `1`。这一点与常规的 Qt 类属性设置不同。然而，这种差异性源于该属性是通过操作系统内核与串口硬件之间的交互来设置的，因此 Qt 串口类属性与其它 Qt 类属性不完全等同。

该属性从 Qt 5.5 开始使用。

**存取函数**:

| 返回类型 | 函数名                                 |
| -------: | :-------------------------------------- |
|     bool | **isBreakEnabled**() const             |
|     bool | **setBreakEnabled**(bool *set* = true) |

**通知信号**:

| 返回类型 | 函数名                              |
| -------: | :---------------------------------- |
|     void | **breakEnabledChanged**(bool *set*) |



### dataBits : [DataBits](https://doc.qt.io/qt-5/qserialport.html#DataBits-enum)

---

该属性为串口数据帧中的比特数。

若设置成功或者打开串口前设置好该属性，那么返回`true`，否则返回`false`并且把错误码置`1`。该错误码可以通过读取 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的值获得。

**注意**: 如果在打开串口前设置该属性，那么真实的串口设置将会在串口打开后，在 [QSerialPort::open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法中自动完成。

该属性的默认值为 `Data8`，即数据帧为`8`比特。

**存取函数**:

|              返回类型 | 函数名                                            |
| --------------------: | :------------------------------------------------ |
| QSerialPort::DataBits | **dataBits**() const                              |
|                  bool | **setDataBits**(QSerialPort::DataBits *dataBits*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | ------------------------------------------------------------ |
|     void | **[dataBitsChanged](https://doc.qt.io/qt-5/qserialport.html#dataBitsChanged)**(QSerialPort::DataBits *dataBits*) |



### dataTerminalReady : bool

---

该属性为串口信号线 DTR 的状态(高或低)。

如果串口信号线 DTR 被置为高电平，则返回`true`，否则返回`false`.

**注意**: 在设置或访问该属性前串口必须已经打开，否则返回 `false` 并且 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码将被置 `1`。

**存取函数**:

| 返回类型 | 函数名                               |
| -------: | :----------------------------------- |
|     bool | **isDataTerminalReady**()            |
|     bool | **setDataTerminalReady**(bool *set*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | ------------------------------------------------------------ |
|     void | **[dataTerminalReadyChanged](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReadyChanged)**(bool *set*) |

**另请参阅** [pinoutSignals](https://doc.qt.io/qt-5/qserialport.html#pinoutSignals)().



### error : [SerialPortError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum)

---

该属性为串口的错误码。

串口设备会返回一个错误码。例如：如果函数 [open](https://doc.qt.io/qt-5/qserialport.html#open)() 返回`false`，或者读/写操作返回`-1`，该属性可以用来判断操作失败的原因。

当调用`clearError()`函数后，错误码会被置为默认值 [QSerialPort::NoError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum).

**存取函数**:

|                     返回类型 | 函数名            |
| ---------------------------: | :---------------- |
| QSerialPort::SerialPortError | **error**() const |
|                         void | **clearError**()  |



### flowControl : [FlowControl](https://doc.qt.io/qt-5/qserialport.html#FlowControl-enum)

---

该属性为串口使用的流控制方式。

若设置成功或者打开串口前设置好该属性，那么返回`true`，否则返回`false`并且把错误码置`1`。该错误码可以通过读取 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的值获得。

**注意**: 如果在打开串口前设置该属性，那么真实的串口设置将会在串口打开后，在 [QSerialPort::open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法中自动完成。

该属性的默认值为 [NoFlowControl](https://doc.qt.io/qt-5/qserialport.html#FlowControl-enum)，即没有流控制。

**存取函数**:

|                 返回类型 | 函数名                                                     |
| -----------------------: | :--------------------------------------------------------- |
| QSerialPort::FlowControl | **flowControl**() const                                    |
|                     bool | **setFlowControl**(QSerialPort::FlowControl *flowControl*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|     void | **[flowControlChanged](https://doc.qt.io/qt-5/qserialport.html#flowControlChanged)**(QSerialPort::FlowControl *flow*) |



### parity : [Parity](https://doc.qt.io/qt-5/qserialport.html#Parity-enum)

---

该属性为串口使用的奇偶校验模式。

若设置成功或者打开串口前设置好该属性，那么返回`true`，否则返回`false`并且把错误码置`1`。该错误码可以通过读取 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的值获得。

**注意**: 如果在打开串口前设置该属性，那么真实的串口设置将会在串口打开后，在 [QSerialPort::open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法中自动完成。

该属性的默认值为  [NoParity](https://doc.qt.io/qt-5/qserialport.html#Parity-enum)，即没有奇偶校验。

**存取函数**:

|            返回类型 | 函数名                                      |
| ------------------: | :------------------------------------------ |
| QSerialPort::Parity | **parity**() const                          |
|                bool | **setParity**(QSerialPort::Parity *parity*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|     void | **[parityChanged](https://doc.qt.io/qt-5/qserialport.html#parityChanged)**(QSerialPort::Parity *parity*) |



### requestToSend : bool

---

该属性为串口信号线 RTS 的状态(高或低)。

如果串口信号线 RTS 被置为高电平，则返回`true`，否则返回`false`.

**注意**: 在设置或访问该属性前串口必须已经打开，否则返回 `false` 并且 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码将被置 `1`。

**注意**: 在 [HardwareControl](https://doc.qt.io/qt-5/qserialport.html#FlowControl-enum) 模式下直接控制 RTS 信号会出错， 错误码 [UnsupportedOperationError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 会被置`1`，因为 RTS 信号由驱动自动控制。

**存取函数**:

| 返回类型 | 函数名                           |
| -------: | :------------------------------- |
|     bool | **isRequestToSend**()            |
|     bool | **setRequestToSend**(bool *set*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | ------------------------------------------------------------ |
|     void | **[requestToSendChanged](https://doc.qt.io/qt-5/qserialport.html#requestToSendChanged)**(bool *set*) |

**另请参阅** [pinoutSignals](https://doc.qt.io/qt-5/qserialport.html#pinoutSignals)().



### stopBits : [StopBits](https://doc.qt.io/qt-5/qserialport.html#StopBits-enum) 

---

该属性为串口帧的停止位比特数。

若设置成功或者打开串口前设置好该属性，那么返回`true`，否则返回`false`并且把错误码置`1`。该错误码可以通过读取 [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop) 属性的值获得。

**注意**: 如果在打开串口前设置该属性，那么真实的串口设置将会在串口打开后，在 [QSerialPort::open](https://doc.qt.io/qt-5/qserialport.html#open)() 方法中自动完成。

该属性的默认值为 [OneStop](https://doc.qt.io/qt-5/qserialport.html#StopBits-enum), 即`1`比特停止位。

**存取函数**:

|              返回类型 | 函数名                                            |
| --------------------: | :------------------------------------------------ |
| QSerialPort::StopBits | **stopBits**() const                              |
|                  bool | **setStopBits**(QSerialPort::StopBits *stopBits*) |

**通知信号**:

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|     void | **[stopBitsChanged](https://doc.qt.io/qt-5/qserialport.html#stopBitsChanged)**(QSerialPort::StopBits *stopBits*) |



## 成员函数文档

### QSerialPort::QSerialPort(const [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html) &*serialPortInfo*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

---

创建一个新的串口对象并指定父对象，用指定的帮助类 *serialPortInfo* 表示串口。

### QSerialPort::QSerialPort(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

---

创建一个新的串口对象并指定父对象，用指定的串口名来表示串口。

串口名必须符合特定的格式，详见 [setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)() 方法。

### QSerialPort::QSerialPort([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

---

创建一个新的串口对象并指定父对象。

### [signal] void QSerialPort::baudRateChanged([qint32](https://doc.qt.io/qt-5/qtglobal.html#qint32-typedef) *baudRate*, [QSerialPort::Directions](https://doc.qt.io/qt-5/qserialport.html#Direction-enum) *directions*)

---

当串口通信波特率改变时会触发该信号。新的波特率在参数 *baudRate* 中，数据传输方向在参数 *directions* 中。

**注意**: 这是 QSerialPort 类成员属性 [baudRate](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop) 的通知信号。

**另请参阅** [QSerialPort::baudRate](https://doc.qt.io/qt-5/qserialport.html#baudRate-prop).

### [signal] void QSerialPort::dataBitsChanged([QSerialPort::DataBits](https://doc.qt.io/qt-5/qserialport.html#DataBits-enum) *dataBits*)

---

当串口帧数据比特数改变时会触发该信号。新的帧数据比特数在参数 *dataBits* 中。

**注意**: 这是 QSerialPort 类成员属性 [dataBits](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop) 的通知信号。

**另请参阅** [QSerialPort::dataBits](https://doc.qt.io/qt-5/qserialport.html#dataBits-prop).

### [signal] void QSerialPort::dataTerminalReadyChanged(bool *set*)

---

当串口信号线 DTR 的电平状态改变时会触发该信号。新的电平状态(高或低)在参数 *set* 中。

**注意**: 这是 QSerialPort 类成员属性 [dataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop) 的通知信号。

**另请参阅** [QSerialPort::dataTerminalReady](https://doc.qt.io/qt-5/qserialport.html#dataTerminalReady-prop).

### [signal] void QSerialPort::errorOccurred([QSerialPort::SerialPortError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) *error*)

---

当串口出错时会触发该信号。错误类型码在参数 *error* 中。

此函数从 Qt 5.8 开始使用。

**另请参阅** [QSerialPort::error](https://doc.qt.io/qt-5/qserialport.html#error-prop).

### [signal] void QSerialPort::flowControlChanged([QSerialPort::FlowControl](https://doc.qt.io/qt-5/qserialport.html#FlowControl-enum) *flow*)

---

当串口流控制方式改变时会触发该信号。新的流控制方式在参数 *flow* 中。

**注意**: 这是 QSerialPort 类成员属性 [flowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop) 的通知信号。

**另请参阅** [QSerialPort::flowControl](https://doc.qt.io/qt-5/qserialport.html#flowControl-prop).

### [signal] void QSerialPort::parityChanged([QSerialPort::Parity](https://doc.qt.io/qt-5/qserialport.html#Parity-enum) *parity*)

---

当串口的奇偶校验模式改变时会触发该信号。新的奇偶校验模式在参数 *parity* 中。

**注意**: 这是 QSerialPort 类成员属性 [parity](https://doc.qt.io/qt-5/qserialport.html#parity-prop) 的通知信号。

**另请参阅** [QSerialPort::parity](https://doc.qt.io/qt-5/qserialport.html#parity-prop).

### [signal] void QSerialPort::requestToSendChanged(bool *set*)

---

当串口信号线 RTS 的电平状态改变时会触发该信号。新的电平状态(高或低)在参数  *set* 中。

**注意**: 这是 QSerialPort 类成员属性 [requestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop) 的通知信号。

**另请参阅** [QSerialPort::requestToSend](https://doc.qt.io/qt-5/qserialport.html#requestToSend-prop).

### [signal] void QSerialPort::stopBitsChanged([QSerialPort::StopBits](https://doc.qt.io/qt-5/qserialport.html#StopBits-enum) *stopBits*)

---

当串口帧停止位比特数改变时会触发该信号。新的帧停止位比特数在参数 *stopBits* 中。

**注意**: 这是 QSerialPort 类成员属性 [stopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop) 的通知信号。

**另请参阅** [QSerialPort::stopBits](https://doc.qt.io/qt-5/qserialport.html#stopBits-prop).

### [virtual] QSerialPort::~QSerialPort()

---

关闭串口，若有必要，销毁对象。

### [override virtual] bool QSerialPort::atEnd() const

---

该函数是 [QIODevice::atEnd](https://doc.qt.io/qt-5/qiodevice.html#atEnd)() 的重写函数。

若串口有更多数据待读取，函数返回`true`，否则返回`false`.

该函数常出现在循环中读取串口数据，代码示例：

```c++
// This slot is connected to QSerialPort::readyRead()
void QSerialPortClass::readyReadSlot()
{
    while (!port.atEnd()) {
        QByteArray data = port.read(100);
        ....
    }
}
```

**另请参阅** [bytesAvailable](https://doc.qt.io/qt-5/qserialport.html#bytesAvailable)() 和 [readyRead](https://doc.qt.io/qt-5/qiodevice.html#readyRead)().

### [override virtual] [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::bytesAvailable() const

---

该函数是 [QIODevice::bytesAvailable](https://doc.qt.io/qt-5/qiodevice.html#bytesAvailable)() 的重写函数。

函数返回串口待读取的数据字节数。

**另请参阅** [bytesToWrite](https://doc.qt.io/qt-5/qserialport.html#bytesToWrite)() 和 [read](https://doc.qt.io/qt-5/qiodevice.html#read)().

### [override virtual] [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::bytesToWrite() const

---

该函数是 [QIODevice::bytesToWrite](https://doc.qt.io/qt-5/qiodevice.html#bytesToWrite)() 的重写函数。

函数返回待写入串口的数据字节数。当控制交还给事件循环或者调用函数 [flush](https://doc.qt.io/qt-5/qserialport.html#flush)() 后，这些数据被写入串口。

**另请参阅** [bytesAvailable](https://doc.qt.io/qt-5/qserialport.html#bytesAvailable)() 和 [flush](https://doc.qt.io/qt-5/qserialport.html#flush)().

### [override virtual] bool QSerialPort::canReadLine() const

---

该函数是 [QIODevice::canReadLine](https://doc.qt.io/qt-5/qiodevice.html#canReadLine)() 的重写函数。

若可以从串口读取一行数据，函数返回`true`，否则返回`false`。

**另请参阅** [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)().

### bool QSerialPort::clear([QSerialPort::Directions](https://doc.qt.io/qt-5/qserialport.html#Direction-enum) *directions* = AllDirections)

---

清空串口输入/输出(取决于串口通信方向)缓冲区中的数据。包括清空内部类缓冲器和串口驱动缓冲区，并且终止后续的读/写串口操作。如果清空串口缓冲区成功，函数返回`true`，否则返回`false`。

**注意**: 清空串口缓冲区之前串口必须是打开的，否则函数返回`false`并且将 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码置`1`。

### [override virtual] void QSerialPort::close()

---

该函数是 [QIODevice::close](https://doc.qt.io/qt-5/qiodevice.html#close)() 的重写函数。

**注意**: 串口关闭前必须处于打开状态，否则会将 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码置`1`。

**另请参阅** [QIODevice::close](https://doc.qt.io/qt-5/qiodevice.html#close)().

### bool QSerialPort::flush()

---

该函数以非阻塞的方式把内部写缓冲区中的数据尽可能的写入串口。若写入成功，返回返回`true`，否则返回`false`。

调用该函数把缓冲区中的数据立即发送至串口，成功发送的数据字节数取决于操作系统。大部分情况下无需调用此函数，因为当控制权交还给事件循环后，[QSerialPort](https://doc.qt.io/qt-5/qserialport.html) 类会自动发送数据。当没有事件循环时，调用 [waitForBytesWritten](https://doc.qt.io/qt-5/qserialport.html#waitForBytesWritten)() 函数。

**注意**: 在把缓冲区数据写入串口前串口必须处于打开状态，否则函数返回`false`并且将 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码置`1`。

**另请参阅** [write](https://doc.qt.io/qt-5/qiodevice.html#write)() 和 [waitForBytesWritten](https://doc.qt.io/qt-5/qserialport.html#waitForBytesWritten)().

### QSerialPort::Handle QSerialPort::handle() const

---

如果操作系统支持并且串口是打开的，返回原生串口句柄，否则返回`-1`。

**警告**: 该函数仅限专家使用并且需要承担相应的风险。并且该函数在 Qt 的小版本中不保证兼容性。

该函数从 Qt 5.2 开始使用。

### [override virtual] bool QSerialPort::isSequential() const

---

该函数是 [QIODevice::isSequential](https://doc.qt.io/qt-5/qiodevice.html#isSequential)() 的重写函数。

该函数总是返回`true`，因为串口为顺序设备。

### [override virtual] bool QSerialPort::open([QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*)

---

该函数是 [QIODevice::open](https://doc.qt.io/qt-5/qiodevice.html#open)(QIODevice::OpenMode mode) 的重写函数。

使用 [OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) 模式打开串口。若串口打开成功，函数返回`true`，否则返回`false`并且将错误码置`1`，该错误码可以通过调用 [error](https://doc.qt.io/qt-5/qserialport.html#error-prop)() 方法获得。

**注意**: 若串口可以成功打开但不能成功设置串口参数时，该函数返回`false`。在这种情况下，串口会自动关闭，从而避免串口设置错误。

**警告**: 该函数的参数 *mode* 只能是  [QIODevice::ReadOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum), [QIODevice::WriteOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum),或 [QIODevice::ReadWrite](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum). 

**另请参阅** [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) and [setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)().

### [QSerialPort::PinoutSignals](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum) QSerialPort::pinoutSignals()

---

以位图格式返回串口信号线的状态。

您可以通过把该函数的返回值和一个模板做逻辑与运算来配置串口信号线的状态。这个模板是[QSerialPort::PinoutSignals](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum) 的期望枚举值。

**注意**: 该函数执行系统调用以确保串口能正常返回信号线状态。这一点是非常必要的，尤其是当底层操作系统不能提供关于串口信号线状态的通知时。

**注意**: 执行该函数之前，串口必须是打开的，否则函数返回 [NoSignal](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum) 并且将 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码置`1`。

### [QString](https://doc.qt.io/qt-5/qstring.html) QSerialPort::portName() const

---

返回串口名，该名字由函数 [setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)() 设置或者通过 [QSerialPort](https://doc.qt.io/qt-5/qserialport.html) 类构造函数传递。返回的名字是简略版的串口名，它从设备地址的内部变量系统提取和转换而来。转换算法因系统而异：

| 操作系统  | 简要描述                                                     |
| :-------: | :----------------------------------------------------------- |
|  Windows  | 从系统设备地址中移除前缀`"\\.\"`或`"//./"`，返回剩余的字符串 |
| Unix, BSD | 从系统设备地址中移除前缀`"/dev/"`，返回剩余的字符串          |

**另请参阅** [setPortName](https://doc.qt.io/qt-5/qserialport.html#setPortName)(), [setPort](https://doc.qt.io/qt-5/qserialport.html#setPort)(), 和 [QSerialPortInfo::portName](https://doc.qt.io/qt-5/qserialportinfo.html#portName)().

### [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::readBufferSize() const

---

返回串口读缓冲区的大小。此返回值决定了程序调用 [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 或 [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)() 方法最多能读取多少字节数据。若返回值为`0`，则串口读缓冲区没有大小限制，数据不会因为读缓冲区不足而丢失。

**另请参阅** [setReadBufferSize](https://doc.qt.io/qt-5/qserialport.html#setReadBufferSize)() 和 [read](https://doc.qt.io/qt-5/qiodevice.html#read)().

### [override virtual protected] [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::readData(char **data*, [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *maxSize*)

---

该函数是 [QIODevice::readData](https://doc.qt.io/qt-5/qiodevice.html#readData)(char *data, qint64 maxSize) 的重写函数。

### [override virtual protected] [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::readLineData(char **data*, [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *maxSize*)

---

该函数是 [QIODevice::readLineData](https://doc.qt.io/qt-5/qiodevice.html#readLineData)(char *data, qint64 maxSize) 的重写函数。

### bool QSerialPort::sendBreak(int *duration* = 0)

---

若在串口异步通信中使用停止位，在 *duration* 毫秒的时间内连续发送值为`0`的比特流。若发送成功，函数返回`true`，否则返回`false`。

若函数参数 *duration* 的值为`0`，那么值为`0`的比特流至少发送`0.25`秒，但不超过`0.5`秒。

若函数参数 *duration* 的值不等于`0`，那么传输值为`0`的比特流的时间长度取决于具体实现。

**注意**: 执行该函数之前，串口必须是打开的，否则函数返回 [NoSignal](https://doc.qt.io/qt-5/qserialport.html#PinoutSignal-enum) 并且将 [NotOpenError](https://doc.qt.io/qt-5/qserialport.html#SerialPortError-enum) 错误码置`1`。

**另请参阅** [setBreakEnabled](https://doc.qt.io/qt-5/qserialport.html#breakEnabled-prop)().

### void QSerialPort::setPort(const [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html) &*serialPortInfo*)

---

该函数用于设置串口，串口参数在 *serialPortInfo* 类实例中。

**另请参阅** [portName](https://doc.qt.io/qt-5/qserialport.html#portName)() 和 [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html).

### void QSerialPort::setPortName(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

---

设置串口名。

串口名字既可以用简略版的名字也可以用包好系统设备地址的全名。

**另请参阅** [portName](https://doc.qt.io/qt-5/qserialport.html#portName)() 和 [QSerialPortInfo](https://doc.qt.io/qt-5/qserialportinfo.html).

### void QSerialPort::setReadBufferSize([qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *size*)

---

设置串口内部读缓冲区的大小为 *size* 字节。

如果 *size* 不为`0`，那么串口读缓冲区不会超过 *size* 字节。如果 *size* 为`0`，那么串口读缓冲区没有大小限制，所有读入串口的数据都将被缓存。 *size* 的默认值为`0`。

该函数在一些情况下非常有用，比如仅需要在特定时间读串口(例如实时流应用)或者需要防止串口读入太多数据从而造成内存耗尽的情形。

**另请参阅** [readBufferSize](https://doc.qt.io/qt-5/qserialport.html#readBufferSize)() 和 [read](https://doc.qt.io/qt-5/qiodevice.html#read)().

### [override virtual] bool QSerialPort::waitForBytesWritten(int *msecs* = 30000)

---

该函数是[QIODevice::waitForBytesWritten(int msecs)](https://doc.qt.io/qt-5/qiodevice.html#waitForBytesWritten) 的重写函数。

该函数会阻塞串口通信线程直至最后一个字节写入到串口并且触发了 [bytesWritten()](https://doc.qt.io/qt-5/qiodevice.html#bytesWritten) 信号。函数经过 *msecs* 毫秒后超时， *msecs* 的默认值是`30000`毫秒，如果 *msecs* 的值为`-1`，那么该函数不会超时。

如果成功触发 [bytesWritten](https://doc.qt.io/qt-5/qiodevice.html#bytesWritten)() 信号，函数将返回`true`，否则返回`false`(写串口过程中出错或者操作超时)。

### [override virtual] bool QSerialPort::waitForReadyRead(int *msecs* = 30000)

---

该函数是 [QIODevice::waitForReadyRead(int msecs)](https://doc.qt.io/qt-5/qiodevice.html#waitForReadyRead) 的重写函数。

该函数会阻塞串口通信线程直至新数据已经准备好读入串口并且触发了 [readyRead()](https://doc.qt.io/qt-5/qiodevice.html#readyRead) 信号。函数经过 *msecs* 毫秒后超时， *msecs* 的默认值是`30000`毫秒，如果 *msecs* 的值为`-1`，那么该函数不会超时。

如果成功触发 [readyRead](https://doc.qt.io/qt-5/qiodevice.html#readyRead)() 信号并且串口读缓冲区有新数据，函数将返回`true`，否则返回`false`(读串口过程中出错或者操作超时)。

**另请参阅** [waitForBytesWritten](https://doc.qt.io/qt-5/qserialport.html#waitForBytesWritten)().

### [override virtual protected] [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QSerialPort::writeData(const char **data*, [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *maxSize*)

---

该函数是 [QIODevice::writeData(const char *data, qint64 maxSize)](https://doc.qt.io/qt-5/qiodevice.html#writeData) 的重写函数。