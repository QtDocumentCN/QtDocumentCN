[TOC]
# **QAbstractAudioInput类**

----------


## **QAbstractAudioInput类为QAudioInput类提供了访问音频设备的方法。（通过插件的形式）**

| 属性| 方法|
| ------: |:------|
|Header:|`#include <QAbstractAudioInput>`|
|qmake:    |QT += multimedia|
|Inherits:|    QObject|


----------

## **简述**
### **公有的函数**

| 类型| 方法|
| ------: |:------|
|virtual int|    [bufferSize()](int-QAbstractAudioInputbufferSize-const-纯虚函数) const = 0|
|virtual int|    bytesReady() const = 0|
|virtual qint64|    elapsedUSecs() const = 0|
|virtual QAudio::Error|    error() const = 0|
|virtual QAudioFormat|    format() const = 0|
|virtual int|    notifyInterval() const = 0|
|virtual int|    periodSize() const = 0|
|virtual qint64|    processedUSecs() const = 0|
|virtual void|    reset() = 0|
|virtual void|    resume() = 0|
|virtual void|    setBufferSize(int value) = 0|
|virtual void    |setFormat(const QAudioFormat &fmt) = 0|
|virtual void|    setNotifyInterval(int ms) = 0|
|virtual void|    setVolume(qreal) = 0|
|virtual void    |start(QIODevice *device) = 0|
|virtual QIODevice*|    start() = 0|
|virtual QAudio::State|    state() const = 0|
|virtual void    |stop() = 0|
|virtual void|    suspend() = 0|
|virtual qreal    |volume() const = 0|


----------

### **信号**

| 类型| 方法|
| ------: |:------|
|void|    errorChanged(QAudio::Error error)|
|void|    notify()|
|void|    stateChanged(QAudio::State state)|


----------

## **详细描述**
QAbstractAudioInput类为QAudioInput类提供了访问音频设备的方法。（通过插件的形式）
QAudioDeviceInput类中保留了一个QAbstractAudioInput的实例，并且调用的函数与QAbstractAudioInput的一致（也就是说QAudioDeviceInput调用的函数实际上是QAbstractAudioInput的函数，就封装了一层相同函数名吧。可以自己看看源码。）。这意味着QAbstractAudioInput是实现音频功能的。有关功能的描述，可以参考QAudioInput类。
另见QAudioInput函数

----------

## **成员函数文档**

----------

### int QAbstractAudioInput::bufferSize() const [纯虚函数]
以毫秒为单位返回音频缓冲区的大小

----------
### int QAbstractAudioInput::bytesReady() const [纯虚函数]
以字节（bytes）为单位返回可读取的音频数据量

----------

### qint64 QAbstractAudioInput**::elapsedUSecs() const [纯虚函数]
返回调用start()函数以来的毫秒数，包括空闲时间与挂起状态的时间

----------
### QAudio::Error QAbstractAudioInput::error() const [纯虚函数]
返回错误的状态

----------

### void QAbstractAudioInput::errorChanged(QAudio::Error error) [信号signal]
当错误状态改变时，该信号被发射

----------
### QAudioFormat QAbstractAudioInput::format() const [纯虚函数]
返回正在使用的QAudioFormat(这个类是储存音频流相关的参数信息的)
另参见setFormat()函数

----------
### void QAbstractAudioInput::notify() [信号signal]
当音频数据的x ms通过函数setNotifyInterval()调用之后，这个信号会被发射。

----------
### int QAbstractAudioInput::notifyInterval() const [纯虚函数]
以毫秒为单位返回通知间隔

----------
### int QAbstractAudioInput::periodSize() const [纯虚函数]
以字节为单位返回其周期

----------
### qint64 QAbstractAudioInput::processedUSecs() const [纯虚函数]
返回自start()函数被调用之后处理的音频数据量(以毫秒为单位)

----------
### void QAbstractAudioInput::reset() [纯虚函数]
将所有音频数据放入缓冲区，并将缓冲区重置为零

----------

### void QAbstractAudioInput::resume() [纯虚函数]
在音频数据*暂停*后继续处理

----------

### void QAbstractAudioInput::setBufferSize(int value) [纯虚函数]
将音频缓冲区大小设置为value大小(以毫秒为单位)
另参阅bufferSize()函数

----------

### void QAbstractAudioInput::setFormat(const QAudioFormat &fmt) [纯虚函数]
设置音频格式，设置格式的时候只能在QAudio的状态为StoppedState时(QAudio::StoppedState)

----------

### void QAbstractAudioInput::setNotifyInterval(int ms) [纯虚函数]
设置发送notify()信号的时间间隔。这个ms时间间隔与操作系统平台相关，并不是实际的ms数。

----------

### void QAbstractAudioInput::setVolume(qreal) [纯虚函数]
另见volume()函数
（设置这里应该是设置音量的值，Volume在英文中有音量的意思，官方文档这里根本就没有任何说明，说去参考valume()函数，可是valume()说又去参考SetValume()函数，这是互相甩锅的节奏么？？？坑爹啊！！！)

----------

### void QAbstractAudioInput::start(QIODevice *device) [纯虚函数]
使用输入参数```QIODevice *device```来传输数据

----------

### QIODevice *QAbstractAudioInput::start() [纯虚函数]
返回一个指向正在用于正在处理数据QIODevice的指针。这个指针可以用来直接读取音频数据。

----------

### QAudio::State QAbstractAudioInput::state() const  [纯虚函数]
返回处理音频的状态

----------

### void QAbstractAudioInput::stateChanged(QAudio::State state) [信号signal]
当设备状态改变时，会发出这个信号

----------
### void QAbstractAudioInput::stop() [纯虚函数]
停止音频输入（因为这是个QAbstractAudioInput类啊，输入类啊，暂时这么解释比较合理。）

----------

### void QAbstractAudioInput::suspend() [纯虚函数]
停止处理音频数据，保存缓冲的音频数据

----------

### qreal QAbstractAudioInput::volume() const [纯虚函数]
另见setVolume()（内心os：参考我解释setVolume()函数的说明，这里应该是返回其音量）

----------



