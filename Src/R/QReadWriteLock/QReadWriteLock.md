
# QReadWriteLock

&emsp;&emsp;`QReadWriteLock` 类提供读写锁定。[更多...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include<QReadWriteLock>`|
|qmake|`QT += core`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。


## 公共成员类型

|类型|名称|
|-|-|
|enmu|**[RecursionMode](#enum-qreadwritelockrecursionmode)** { Recursive, NonRecursive}|


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QReadWriteLock](#qreadwritelockqreadwritelockqreadwritelockrecursionmode-recursionmode--nonrecursive)**(QReadWriteLock::RecursionMode *recursionMode* = NonRecursive)|
||**[~QReadWriteLock](#qreadwritelockqreadwritelock)**()|
|void|**[lockForRead](#void-qreadwritelocklockforread)**()|
|void|**[lockForeWrite](#void-qreadwritelocklockforwrite)**()|
|bool|**[tryLockForRead](#bool-qreadwritelocktrylockforread)**()|
|bool|**[tryLockForRead](#bool-qreadwritelocktrylockforreadint-timeout)**(int *timeout*)|
|bool|**[trylockForWrite](#bool-qreadwritelocktrylockforwrite)**()|
|bool|**[trylockForWrite](#bool-qreadwritelocktrylockforwriteint-timeout)**(int *timeout*)|
|void|**[unlock](#void-qreadwritelockunlock)**()|


## 详细描述

&emsp;&emsp;读写锁是一种用于保护读写资源的同步工具。如果希望允许多个线程同时进行只读访问，那么这种类型的锁很有用，但是只要一个线程想写入资源，那么它就必须阻止所有其他线程，直到写入完成。  
&emsp;&emsp;在许多情况下，`QReadWriteLock` 是 [QMutex](../../M/QMutex/QMutex.md) 强有力的竞争对手。`QReadWriteLock` 在多并发读，少量写的情况下，有较好的执行效果。  
例如：
```cpp
QReadWriteLock lock;

void ReaderThread::run()
{
    ...
    lock.lockForRead();
    read_file();
    lock.unlock();
    ...
}

void WriterThread::run()
{
    ...
    lock.lockForWrite();
    write_file();
    lock.unlock();
    ...
}
```
&emsp;&emsp;为了确保写者永远不会被读者阻塞，如果有写者被阻塞，则读者将无法获取锁，即使该锁当前正被其他读者访问。另外，如果一个写者正在写，而另一个写者想进入，则该写者将优先于其他可能正在等待的读者。  
&emsp;&emsp;与 `QMutex` 类似，当使用 `QReadWriteLock::Recursive` 作为 `QReadWriteLock::RecursiveMode` 参数构造时，`QReadWriteLock` 可以被同一线程递归锁定。在这种情况下，[unlock](#void-qreadwritelockunlock)() 的调用次数必须与 [lockForWrite](#void-qreadwritelocklockforwrite)() 或 [lockForRead](#void-qreadwritelocklockforread)() 的调用次数相同。请注意，当尝试递归锁定时，不能更改锁类型，也就是说，在已经为写入而锁定的线程中，不可能为读取而锁定（反之亦然）。

**另请参阅：** [QReadLock](../../R/QReadLock/QReadLock.md)、[QWriteLock](../../R/QWriteLock/QWriteLock.md)、[QMutex](../../M/QMutex/QMutex.md)、[QSemaphore](../../S/QSemaphore/QSemaphore.md)。


## 成员类型文档

### enum QReadWriteLock::RecursionMode

|常量|值|描述|
|-|-|-|
|QReadWriteLock::Recursive|1|&emsp;&emsp;在这种模式下，线程可以多次锁定同一个 `QReadWriteLock`。`QReadWriteLock` 在执行相应数量的 [unlock](#void-qreadwritelockunlock)() 调用之前不会解锁。|
|QReadWriteLock::NonRecursive|0|&emsp;&emsp;在这种模式下，线程只能锁定 `QReadWriteLock` 一次。|
**另请参阅：**[QReadWriteLock](#qreadwritelockqreadwritelockqreadwritelockrecursionmode-recursionmode--nonrecursive)()。


## 成员函数文档

### QReadWriteLock::QReadWriteLock(QReadWriteLock::RecursionMode recursionMode = NonRecursive)

&emsp;&emsp;构造一个 `recursionMode` 模式的 `QReadWriteLock`。  
&emsp;&emsp;默认 [NonRecursive](#enum-qreadwritelockrecursionmode)。  
&emsp;&emsp;在 Qt 4.4 引入该函数。

**另请参阅：** [lockForRead](#void-qreadwritelocklockforread)()、[lockForWrite](#void-qreadwritelocklockforwrite)()、[RecursiveMode](#enum-qreadwritelockrecursionmode)。


---
### QReadWriteLock::~QReadWriteLock()

&emsp;&emsp;解锁，并析构。

**警告：销毁正在使用的读写锁可能会导致未定义的行为。**


---
### void QReadWriteLock::lockForRead()

&emsp;&emsp;读锁定。如果另一个线程正写锁定，则此函数将阻塞当前线程。  
&emsp;&emsp;如果线程已写锁定，则不可读锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForRead](#void-qreadwritelocklockforread)()、[tryLockForRead](#bool-qreadwritelocktrylockforread)()。


---
### void QReadWriteLock::lockForWrite()

&emsp;&emsp;写锁定。如果另一个线程（包括当前线程）为读或写而锁定（除非锁是使用 `QReadWriteLock::Recursive` 模式创建的），则此函数将阻塞当前线程。
&emsp;&emsp;如果线程已读锁定，则不可写锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForWrite](#void-qreadwritelocklockforwrite)()、[tryLockForWrite](#bool-qreadwritelocktrytrylockforwrite)()。


---
### bool QReadWriteLock::tryLockForRead()

&emsp;&emsp;尝试读锁定。如果获得了锁，此函数将返回 `true`，否则将返回 `false`，而不是等待锁变为可用，即不阻塞。  
&emsp;&emsp;如果另一个线程已写锁定，则读锁定尝试将失败。  
&emsp;&emsp;如果获得了锁，请务必使用 [unlock](#void-qreadwritelockunlock)() 解锁，然后另一个线程才能成功地将其写锁定。  
&emsp;&emsp;如果线程已写锁定，则不可读锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForRead](#void-qreadwritelocklockforread)()。


---
### bool QReadWriteLock::tryLockForRead(int *timeout*)

&emsp;&emsp;重载函数。  
&emsp;&emsp;尝试读锁定。如果获得了锁，此函数返回 `true`，否则返回 `false`。如果另一个线程已写锁定，则此函数最多将等待 `timeout` 毫秒。

**注意：传递一个负数作为超时值相当于调用 [lockForRead](#void-qreadwritelocklockforread)()，即当 `timeout` 值为负数时，此函数将永远等待，直到读锁定为止。**

&emsp;&emsp;如果获得了锁，请务必使用 [unlock](#void-qreadwritelockunlock)() 解锁，然后另一个线程才能成功地将其写锁定。  
&emsp;&emsp;如果线程已读锁定，则不可写锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForRead](#void-qreadwritelocklockforread)()。


---
### bool QReadWriteLock::tryLockForWrite()

&emsp;&emsp;尝试锁定以进行写入。如果获取的锁为 `true`，则立即返回 `false`。  
&emsp;&emsp;如果另一个线程已锁定，则写锁定尝试将失败。  
&emsp;&emsp;如果获得了锁，请务必使用 [unlock](#void-qreadwritelockunlock)() 解锁，然后另一个线程才能成功地将其锁定。  
&emsp;&emsp;如果线程已读锁定，则不可写锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForWrite](#void-qreadwritelocklockforwrite)()。



---
### bool QReadWriteLock::tryLockForWrite(int timeout)

&emsp;&emsp;重载函数。  
&emsp;&emsp;尝试写锁定。如果获得了锁，此函数返回 `true`，否则返回 `false`。如果另一个线程已写锁定，则此函数最多将等待 `timeout` 毫秒。

**注意：传递一个负数作为超时值相当于调用 [lockForWrite](#void-qreadwritelocklockforwrite)()，即当 `timeout` 值为负数时，此函数将永远等待，直到读锁定为止。**

&emsp;&emsp;如果获得了锁，请务必使用 [unlock](#void-qreadwritelockunlock)() 解锁，然后另一个线程才能成功地将其写锁定。  
&emsp;&emsp;如果线程已读锁定，则不可写锁定。

**另请参阅：** [unlock](#void-qreadwritelockunlock)()、[lockForWrite](#void-qreadwritelocklockforwrite)()。


---
### void QReadWriteLock::unlock()

&emsp;&emsp;解锁。  
&emsp;&emsp;试图解锁未锁定的锁是错误的，将导致程序终止。

**另请参阅：** [lockForRead](#void-qreadwritelocklockforread)()、[lockForWrite](#void-qreadwritelocklockforwrite)()、[tryLockForRead](#bool-qreadwritelocktrylockforread)()、[trylockForWrite](#bool-qreadwritelocktrylockforwrite)()。

