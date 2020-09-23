
# QReadLocker

&emsp;&emsp;`QReadLocker` 是工具类，它简化了对读写锁，读访问的的锁定和解锁。[更多...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include<QReadLocker>`|
|qmake|`QT += core`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QReadLocker](#qreadlockerqreadlockerqreadwritelock-lock)**(QReadWrtiteLock \**lock*)|
||**[~QReadLocker](#qreadlockerqreadlocker)**()|
|QReadWriteLock *|**[readWriteLock](#qreadwritelock-qreadlockerreadwritelock-const)**() const|
|void|**[relock](#void-qreadlockerrelock)**()|
|void|**[unlock](#void-qreadlockerunlock)**()|



## 详细描述

&emsp;&emsp;`QReadLocker`（和 [QWriteLocker](../../W/QWriteLocker/QWriteLocker.md)）的目的是简化 [QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md) 的锁定和解锁。锁定和解锁语句、异常处理代码是很容易出错的，而且很难调试。`QReadLocker` 可以确保在此类情况下，锁的状态始终定义良好。

&emsp;&emsp;下面是一个使用 `QReadLocker` 锁定和解锁读写锁的示例：
```cpp
QReadWriteLock lock;

QByteArray readData()
{
    QReadLocker locker(&lock);
    ...
    return data;
}
```
等价于以下代码：
```cpp
QReadWriteLock lock;

QByteArray readData()
{
    lock.lockForRead();
    ...
    lock.unlock();
    return data;
}
```
&emsp;&emsp;[QMutexLocker](../../M/QMutexLocker/QMutexLocker.md) 文档展示了使用locker对象来大大简化编程的示例。

**另请参阅：** [QWriteLocker](../QMutexLocker/QMutexLocker.md)、[QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md)。


## 成员函数文档

### QReadLocker::QReadLocker(QReadWriteLock \**lock*)

&emsp;&emsp;构造一个 `QReadLocker` 并锁定用于读取的锁。当 `QReadLocker` 被销毁时，锁将被解锁。如果 `lock == nullptr`，则 `QReadLocker` 不执行任何操作。

**另请参阅：** [QReadWriteLock::lockForRead](../../R/QReadWriteLock/QReadWriteLock.md#void-qreadwritelocklockforread)()。



---
### QReadLocker::~QReadLocker()

&emsp;&emsp;销毁 `QReadLocker` 并解锁传递给构造函数的锁。

**另请参阅：** [QReadWriteLock::unlock](../../R/QReadWriteLock/QReadWriteLock.md#void-qreadwritelockunlock)()。


---
### QReadWriteLock *QReadLocker::readWriteLock() const

&emsp;&emsp;返回传递给构造函数的读写锁的指针。


---
### void QReadLocker::relock()

&emsp;&emsp;重新锁定。

**另请参阅：** [unlock](#void-qreadlockerunlock)()。


---
### void QReadLocker::unlock()

&emsp;&emsp;解锁。

**另请参阅：** [QReadWriteLock::unlock](../../R/QReadWriteLock/QReadWriteLock.md#void-qreadwritelockunlock)()。

