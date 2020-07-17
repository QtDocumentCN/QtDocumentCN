[TOC]
#**QAbstractAudioOutput类**

----------

## **QAbstractAudioOutput类是音频后端的基类**

|  属性  | 方法|
|------:|:------|
|头文件包含:|```    #include <QAbstractAudioOutput>```|
|qmake写法:|    QT += multimedia|
|继承:|    QObject|


----------

## **简述**

### **public函数**
|  类型  | 函数名|
|------:|:------|
|virtual int|    bufferSize() const = 0|
|virtual int|    bytesFree() const = 0|
|virtual QString|    category() const|
|virtual qint64|    elapsedUSecs() const = 0|
|virtual QAudio::Error|    error() const = 0|
|virtual QAudioFormat|    format() const = 0|
|virtual int |notifyInterval() const = 0|
|virtual int|periodSize() const = 0|
|virtual qint64|    processedUSecs() const = 0|
|virtual void    |reset() = 0|
|virtual void    |resume() = 0|
|virtual void|    setBufferSize(int value) = 0|
|virtual void|    setCategory(const QString &)|
|virtual void|    setFormat(const QAudioFormat &fmt) = 0|
|virtual void|    setNotifyInterval(int ms) = 0|
|virtual void|    setVolume(qreal volume)|
|virtual void|    start(QIODevice *device) = 0|
|virtual QIODevice *|    start() = 0|
|virtual QAudio::State|    state() const = 0|
|virtual void|    stop() = 0|
|virtual void|    suspend() = 0|
|virtual qreal|    volume() const|


----------

### **信号**
|  类型  | 函数名|
|------:|:------|
|void |    errorChanged(QAudio::Error error)|
|void |    notify()|
|void |    stateChanged(QAudio::State state)|


----------
## **详细描述**
QAbstractAudioOutput类是音频后端的基类。
QAbstractAudioOutput类是QAudioOutput类的实现类。QAudioOutput的实现实际上是调用的QAbstractAudioOutput类，有关实现相关的功能，请参考QAudioOutput()类中的函数说明。

----------

## **成员函数**

----------
**int QAbstractAudioOutput::bufferSize() const [纯虚函数]**
以字节为单位，返回音频缓冲区的大小。

*另见setBufferSize()函数*

----------

**int QAbstractAudioOutput :: bytesFree ()const [纯虚函数]**
返回音频缓冲区的可用空间(以字节为单位)

----------

**QString QAbstractAudioOutput::category() const [虚函数 virtual]**
音频缓冲区的类别（官方文档没有，这是我个人经验，当然可能有误，望指正）
*另见setCategory()*

----------

**qint64 QAbstractAudioOutput::elapsedUSecs() const [纯虚函数 pure virtual]**
返回调用start()函数之后的毫秒数，包括处于空闲状态的时间和挂起状态的时间。

----------

**QAudio::Error QAbstractAudioOutput::error() const [纯虚函数 pure virtual]**
返回错误状态。

----------

**void QAbstractAudioOutput::errorChanged(QAudio::Error error) [信号 signal]**
当错误状态改变时，该信号被发射。

----------

**QAudioFormat QAbstractAudioOutput :: format （）const [纯虚函数 pure virtual]**
返回正在使用的QAudioFormat()类
*另见setFormat()*

----------

**void QAbstractAudioOutput::notify() [信号 signal]**
当函数setNotifyInterval(x)函数已经调用，即音频数据的时间间隔已经被设置时。该信号被发射。（就是调用setNotifyInterval(x)后，这个信号会被发射。官方文档讲的好详细啊=。=）

----------

**int QAbstractAudioOutput::notifyInterval() const [纯虚函数 pure virtual]**
以毫秒为单位，返回时间间隔
*另见函数setNotifyInterval()*

----------

**int QAbstractAudioOutput::periodSize() const [纯虚函数 pure virtual]**
以字节为单位返回周期大小。

----------

**qint64 QAbstractAudioOutput::processedUSecs() const [纯虚函数 pure virtual]**
返回自调用start()函数后处理的音频数据量(单位为毫秒)

----------

**void QAbstractAudioOutput::reset() [纯虚函数 pure virtual]**
将所有音频数据放入缓冲区，并将缓冲区重置为零。

----------

**void QAbstractAudioOutput::resume() [纯虚函数 pure virtual]**
继续处理暂停后的音频数据 (也就是暂停后继续的意思呗)

----------

**void QAbstractAudioOutput::setBufferSize(int value) [纯虚函数 pure virtual]**
重新设置音频缓冲区的大小（以字节为单位 即输入参数value）
*另见bufferSize()函数*

----------
**void QAbstractAudioOutput::setCategory(const QString &) [虚函数 virtual]**
*参见函数category()*

----------

**void QAbstractAudioOutput::setFormat(const QAudioFormat &fmt) [纯虚函数 pure virtual]**
QAbstractAudioOutput设置QAudioFormat类，只有当QAudio状态为QAudio::StoppedState时，音频格式才会被设置成功。
*另见函数format()*

----------

**void QAbstractAudioOutput::setNotifyInterval(int ms) [纯虚函数 pure virtual]**
设置发送notify()信号的时间间隔。这个ms并不是实时处理的音频数据中的ms数。这个时间间隔是平台相关的。
*另见notifyInterval()*

----------

**void QAbstractAudioOutput::setVolume(qreal volume) [虚函数 virtual]**
设置音量。音量的范围为[0.0 - 1.0]。
*另见函数volume()*

----------

**void QAbstractAudioOutput::start(QIODevice *device) [纯虚函数 pure virtual]**
调用start()函数时，输入参数QIODevice*类型的变量device，用于音频后端处理数据传输。

----------

**QIODevice *QAbstractAudioOutput::start() [纯虚函数 pure virtual]**
返回一个指向正在处理数据传输的QIODevice类型的指针，这个指针是可以被写入的，用于处理音频数据。(参考上边的函数是咋写入的）

----------

**QAudio::State QAbstractAudioOutput::state() const [纯虚函数 pure virtual]**
返回音频处理的状态。

----------

**void QAbstractAudioOutput::stateChanged(QAudio::State state) [信号 signal]**
当音频状态变化的时候，该信号被发射

----------

**void QAbstractAudioOutput::stop() [纯虚函数 pure virtual]**
停止音频输出

----------

**void QAbstractAudioOutput::suspend() [纯虚函数 pure virtual]**
停止处理音频数据，保存处理的音频数据。（就是暂停的意思啊=。=）

----------

**qreal QAbstractAudioOutput::volume() const [虚函数 virtual]**
返回音量。音量范围为[0.0 - 1.0]
*另参阅函数setVolume()*

----------



