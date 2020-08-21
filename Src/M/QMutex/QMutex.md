
# QMutex

&emsp;&emsp;QMutex类提供线程间的访问序列化。[更多...](#详细描述)
|属性|内容|
|-|-|
|头文件|`#include<QMutex>`|
|qmake|`QT += core`|
|子类|`QRecursiveMutex`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。




## 公共成员类型

|类型|名称|
|-|-|
|enmu|**[RecursionMode](#enum-qmutexrecursionmode)** { Recursive, NonRecursive}|


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QMutex](#qmutexqmutexqmutexrecursionmode-mode)**(QMutex::RecursionMode *mode*)|
||**[QMutex](#qmutexqmutex)**()|
||**[~QMutex](#qmutexqmutex-1)**()|
|bool|**[isRecursive](#bool-qmutexisrecursive-const)**() const|
|void|**[lock](#void-qmutexlock)**()|
|bool|**[tryLock](#bool-qmutextrylockint-timeout--0)**(int *timeout* = 0)|
|bool|**[try_lock](#bool-qmutextrylock)**()|
|bool|**[try_lock_for](#template-typename-rep-typename-period-bool-qmutextrylockforstdchronodurationrep-period-duration)**(std::chrono::duration\<Rep, Period\> *duration*)|
|bool|**[try_lock_until](#template-typename-clock-typename-duration-bool-qmutextrylockuntilstdchronotimepointclock-duration-timepoint)**(std::chrono::time_point\<Clock, Duration\> *timePoint*)|
|void|**[unlock](#void-qmutexunlock)**()|




## 详细描述

&emsp;&emsp;QMutex的目的是保护对象、数据结构或代码段，以便一次只有一个线程可以访问它们（这类似于 `Java` `synchronized` 关键字）。最好通过 [QMutexLocker](../QMutexLocker.md) 来使用互斥量，这样可以很方便确保成对执行锁和解锁。
例如，假设有一个方法将消息打印到两行上：
```cpp
    int number = 6;

    void method1()
    {
        number *= 5;
        number /= 4;
    }

    void method2()
    {
        number *= 3;
        number /= 2;
    }
```
&emsp;&emsp;如果连续调用这两个方法，将发生以下情况：
```cpp
    // method1()
    number *= 5;        // number 30
    number /= 4;        // number  7

    // method2()
    number *= 3;        // number 21
    number /= 2;        // number 10
```
&emsp;&emsp;如果两个线程同时调用这两个方法，则可能会产生以下结果：
```cpp
    // 线程 1 调用 method1()
    number *= 5;        // number 30

    // 线程 2 调用 method2().
    //
    // 很可能线程 1 已被操作系统置于等待队列
    // 操作系统运行线程 2
    number *= 3;        // number 90
    number /= 2;        // number 45

    // 线程 1 执行完毕
    number /= 4;        // number 是 11，而不是 10
```
&emsp;&emsp;如果我们添加一个互斥量，我们就能得到我们想要的结果：
```cpp
    QMutex mutex;
    int number = 6;

    void method1()
    {
        mutex.lock();
        number *= 5;
        number /= 4;
        mutex.unlock();
    }

    void method2()
    {
        mutex.lock();
        number *= 3;
        number /= 2;
        mutex.unlock();
    }
```
&emsp;&emsp;在任何给定的时间只有一个线程可以修改 `number`，并正确执行。虽然这只是一个微不足道的例子，但也适用于其他需要有序执行的地方。
&emsp;&emsp;当你在一个线程中调用 [lock](#void-qmutexlock)() 时，在同一位置尝试调用 [lock](#void-qmutexlock)() 的其他线程将阻塞，直到获得锁的线程调用 [unlock](#void-qmutexunlock)()。替代 [lock](#void-qmutexlock)() 的非阻塞方法是 [tryLock](#bool-qmutextrylockint-timeout--0)()。
&emsp;&emsp;QMutex被优化为在非争用情况 （ the non-contended ）下速度更快。如果互斥体上没有争用，非递归QMutex将不会分配内存。它的构造和销毁几乎没有任何开销，这意味着将互斥体作为类的一部分是很好的做法。

**另请参阅：** [QRecursiceMutex](../../R/QRecursiceMutex.md)，[QMutexLocker](../QMutexLocker.md)，[QReadWriteLock](../../R/QReadWriteLock.md)，[QSemaphore](../../S/QSemaphore.md) 和 [QWaitCondition](../../R/QWaitCondition.md)。




## 成员类型文档

### enum QMutex::RecursionMode

|常量|值|描述|
|-|-|-|
|QMutex::Recursive|1|&emsp;&emsp;在这种模式下，一个线程可以多次锁定同一个互斥量，并且在调用相同数量的 [unlock](#void-qmutexunlock)() 之前，互斥体不会被解锁。对于这种情况，您应该使用 [QRecursiveMutex](../../R/QRecursiveMutex.md)。|
|QMutex::NonRecursive|0|&emsp;&emsp;在这种模式下，一个线程只能锁定一次。|

**另请参阅：**[QMutex](#qmutexqmutexrecursionmode-mode)()，[QRecursiveMutex](../../R/QRecursiveMutex.md)。




## 成员函数文档

### QMutex::QMutex(QMutex::RecursionMode *mode*)

&emsp;&emsp;构造一个互斥量，初始状态为未上锁。
&emsp;&emsp;如果 `mode` 是 `QMutex:：Recursive`，则线程可以多次锁定同一个互斥量，并且在调用相同数量的 [unlock](#void-qmutexunlock)() 之前，互斥量不会被解锁。否则，线程只能锁定互斥量一次。默认值为 `QMutex::NonRecursive`。

**另请参阅：** [lock](#void-qmutexlock)()，[unlock](#void-qmutexunlock)()。

---
### QMutex::QMutex()

&emsp;&emsp;构造一个互斥量，初始状态为未上锁。

---
### QMutex::~QMutex()

&emsp;&emsp;析构。

**警告：** 销毁锁定的互斥量可能会导致未定义的行为。

---
### bool QMutex::isRecursive() const

&emsp;&emsp;如果互斥量是递归的，则返回 `true`。
&emsp;&emsp;在 Qt 5.7 引入该函数。

---
### void QMutex::lock()

&emsp;&emsp;锁定互斥量。如果另一个线程锁定了该互斥量，那么这个调用将被阻塞，直到锁定线程将其解锁为止。
&emsp;&emsp;如果该互斥量是[递归互斥量](../../R/QRecursiveMutex.md)，则允许在同一线程的同一互斥体上多次调用此函数。如果这个互斥量是非递归互斥量，则当该互斥量递归锁定时，这个函数将死锁。

**另请参阅：** [unlock](#void-qmutexunlock)()。

---
### bool QMutex::tryLock(int *timeout* = 0)

&emsp;&emsp;尝试锁定互斥量。如果获得了锁，此函数返回 `true`；否则返回 `false`。如果另一个线程锁定了互斥量，则此函数最多将等待 `timeout` 毫秒，以尝试获取。

**注意：** 传递一个负数给 `timeout` 相当于调用 [lock](#void-qmutexlock)()。即，如果 `timeout` 为负数，这个函数将一直待，直到互斥量被锁定为止。

&emsp;&emsp;如果获得了锁，则必须使用 [unlock](#void-qmutexunlock)() 解锁，另一个线程才能成功锁定。
&emsp;&emsp;如果该互斥量是递归互斥量，则允许在同一线程的同一互斥量上多次调用此函数。如果此互斥量是非递归互斥量，则当尝试递归锁定互斥量时，此函数将始终返回 `false`。

**另请参阅：** [lock](#void-qmutexlock)()，[unlock](#void-qmutexunlock)()。

---
### bool QMutex::try_lock()

&emsp;&emsp;尝试锁定互斥量。如果获得了锁，此函数返回 `true`；否则返回 `false`。
&emsp;&emsp;提供此函数是为了与可锁定的标准库概念兼容。它相当于 [tryLock](#bool-qmutextrylockint-timeout--0)()。
&emsp;&emsp;在 Qt 5.8 引入该函数。

---
### template <typename Rep, typename Period> bool QMutex::try_lock_for(std::chrono::duration<Rep, Period> *duration*)


&emsp;&emsp;尝试锁定互斥量。如果获得了锁，此函数返回 `true`；否则返回 `false`。如果另一个线程锁定了互斥量，则此函数最多将等待 `duration` 这么长时间，以尝试获取。

**注意：** 传递一个负数给 `duration` 相当于调用 [try_lock](#bool-qmutextrylock)()。此行为与 [tryLock](#bool-qmutextrylockint-timeout--0)() 不同。

&emsp;&emsp;如果获得了锁，则必须使用 [unlock](#void-qmutexunlock)() 解锁，另一个线程才能成功锁定。
&emsp;&emsp;如果该互斥量是递归互斥量，则允许在同一线程的同一互斥量上多次调用此函数。如果此互斥量是非递归互斥量，则当尝试递归锁定互斥量时，此函数将始终返回 `false`。
&emsp;&emsp;在 Qt 5.8 引入该函数。

**另请参阅：** [lock](#void-qmutexlock)()，[unlock](#void-qmutexunlock)()。

---
### template <typename Clock, typename Duration> bool QMutex::try_lock_until(std::chrono::time_point<Clock, Duration> *timePoint*)


&emsp;&emsp;尝试锁定互斥量。如果获得了锁，此函数返回 `true`；否则返回 `false`。如果另一个线程锁定了互斥量，则此函数最多将等待 `timePoint` 这么长时间，以尝试获取。

**注意：** 传递一个负数给 `timePoint` 相当于调用 [try_lock](#bool-qmutextrylock)()。此行为与 [tryLock](#bool-qmutextrylockint-timeout--0)() 不同。

&emsp;&emsp;如果获得了锁，则必须使用 [unlock](#void-qmutexunlock)() 解锁，另一个线程才能成功锁定。
&emsp;&emsp;如果该互斥量是递归互斥量，则允许在同一线程的同一互斥量上多次调用此函数。如果此互斥量是非递归互斥量，则当尝试递归锁定互斥量时，此函数将始终返回 `false`。
&emsp;&emsp;在 Qt 5.8 引入该函数。

**另请参阅：** [lock](#void-qmutexlock)()，[unlock](#void-qmutexunlock)()。

---
### void QMutex::unlock()

&emsp;&emsp;解锁互斥量。**试图在不同线程中解锁互斥量会导致错误。解锁未锁定的互斥量会导致未定义的行为。**

**另请参阅：** [lock](#void-qmutexlock)()。
