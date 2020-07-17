[TOC]
# **QAbstractAudioDeviceInfo类**

----------
## **QAbstractAudioDeviceInfo是音频后端的基类**

| 属性| 方法|
| ------: |:------|
| Header: | `#include<QAbstractAudioDeviceInfo>` |
| qmake: | QT += multimedia|
|Inherits:|QObject|


----------

## **简述**

### **公共功能**

| 类型| 方法|
| ------: |:------|
|virtual QString|    deviceName() const = 0|
|virtual bool|    isFormatSupported(const QAudioFormat &format) const = 0|
|virtual QAudioFormat|    preferredFormat() const = 0|
|virtual QList<QAudioFormat::Endian>|    supportedByteOrders() = 0|
|virtual QList<int>|    supportedChannelCounts() = 0|
|virtual QStringList|    supportedCodecs() = 0|
|virtual QList<int>|    supportedSampleRates() = 0|
|virtual QList<int>|    supportedSampleSizes() = 0|
|virtual QList<QAudioFormat::SampleType>|    supportedSampleTypes() = 0|


----------

## **详细说明**


----------

QAbstractAudioDeviceInfo是音频后端的基类。

该类实现了QAudioDeviceInfo的音频功能，即QAudioDeviceInfo类中会保留一个QAbstractAudioDeviceInfo，并对其进行调用。关于QAbstractAudioDeviceInfo的实现的其它功能，你可以参考QAudioDeviceInfo的类与函数文档

----------

### **成员函数文档**

----------

**QString QAbstractAudioDeviceInfo::deviceName() const [纯虚函数]**
返回音频设备名称

----------

**bool QAbstractAudioDeviceInfo::isFormatSupported(const QAudioFormat &format) const [纯虚函数]**
传入参数QAudioFormat（音频流）类，如果QAbstractAudioDeviceInfo支持的话，返回true（真是不好翻译）

----------
**QAudioFormat QAbstractAudioDeviceInfo::preferredFormat() const [纯虚函数]**
返回QAbstractAudioDeviceInfo更加倾向于使用的音频流。

----------
**QList<QAudioFormat::Endian> QAbstractAudioDeviceInfo::supportedByteOrders() [纯虚函数]**
返回当前支持可用的字节顺序(QAudioFormat :: Endian)列表

----------
**QList<int> QAbstractAudioDeviceInfo::supportedChannelCounts() [纯虚函数]**
返回当前可用的通道（应该是这样翻译）列表

----------

**QStringList QAbstractAudioDeviceInfo::supportedCodecs() [纯虚函数]**
返回当前可用编解码器的列表

----------
**QList<int> QAbstractAudioDeviceInfo::supportedSampleRates() [纯虚函数]**
返回当前可用的采样率列表。(突然发现Google翻译真心吊啊)

----------
**QList<int> QAbstractAudioDeviceInfo::supportedSampleSizes() [纯虚函数]**
返回当前可用的样本大小列表。

----------
**QList<QAudioFormat::SampleType> QAbstractAudioDeviceInfo::supportedSampleTypes() [纯虚函数]**
返回当前可用样本类型的列表。



