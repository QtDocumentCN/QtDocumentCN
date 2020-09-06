
# QRcursiveMutex

&emsp;&emsp;QRcursiveMutex类提供线程间的访问序列化。[更多...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include<QRcursiveMutex>`|
|qmake|`QT += core`|
|加入版本|Qt 5.14|
|继承自|`QMutex(private)`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QRecursiveMutex](#qrecursivemutexqrecursivemutex)**()|
||**[~QRecursiveMutex](#qrecursivemutexqrecursivemutex-1)**()|


## 详细描述

&emsp;&emsp;`QRecursiveMutex` 类是一个互斥体，与 [QMutex](../../M/QMutex/QMutex.md) 类似，与之API兼容。它与 `QMutex` 的不同之处在于，它可多次接受来自同一线程的 [lock](../../M/QMutex/QMutex.md#void-qmutexlock)() 调用。`QMutex` 在这种情况下会死锁。  
`QRecursiveMutex` 的构造和操作成本要高很多，因此尽可能使用纯 `QMutex`。然而，有时一个公共函数调用另一个公共函数，它们都需要锁定同一个互斥体。在这种情况下，您有两个选项：
* 将需要互斥锁保护的代码分解到私有函数中，私有函数假设在调用互斥体时 保留互斥体，并在调用私有实现函数之前在公共函数中锁定一个纯QMutex。
* 或者使用递归互斥锁，所以第二个公共函数希望锁定互斥锁，与第一个公共函数是否锁定没有多大关系了。

**另请参阅：** [QMutex](../../M/QMutex/QMutex.md)，[QMutexLocker](../QMutexLocker/QMutexLocker.md)，[QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md)，[QSemaphore](../../S/QSemaphore/QSemaphore.md) 和 [QWaitCondition](../../W/QWaitCondition/QWaitCondition.md)。



## 成员函数文档

### QRecursiveMutex::QRecursiveMutex()

&emsp;&emsp;构造一个新的递归互斥锁。互斥锁是在解锁状态下创建的。

**另请参阅：** [lock](../../M/QMutex/QMutex.md#void-qmutexlock)()、[unlock](../../M/QMutex/QMutex.md#void-qmutexunlock)()

---
### QRecursiveMutex::~QRecursiveMutex()

&emsp;&emsp;析构。

**警告：销毁锁定的互斥锁可能会导致未定义的行为。**




