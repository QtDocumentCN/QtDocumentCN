

# QMutexLocker

&emsp;&emsp;`QMutexLocker` 是一个工具类，它能非常方便地将互斥量锁定以及解锁。[更多内容...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include <QMutexLocker>`|
|`qmake`|`QT += core`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QMutexLocker](#qmutexlockerqmutexlockerqrecursivemutex-mutex)**(QRecursiceMutex \**mutex*)|
||**[QMutexLocker](#qmutexlockerqmutexlockerqmutex-mutex)**(QMutex \**mutex*)|
||**[~QmutexLocker](#qmutexlockerqmutexlocker)**()|
|QMutex \*|**[mutex](#qmutex-qmutexlockermutex-const)**() const|
|void|**[relock](#void-qmutexlockerrelock)**()|
|void|**[unlock](#void-qmutexlockerunlock)**()|


## 详细描述

&emsp;&emsp;在复杂的函数、语句或异常处理代码中锁定和解锁 [QMutex](../QMutex/QMutex.md) 很容易出错，而且很难调试。`QMutexLocker` 可用于此类情况，以确保互斥量的状态始终定义良好。

&emsp;&emsp;`QMutexLocker` 应该在需要锁定 [QMutex](../QMutex/QMutex.md) 的函数中创建。在创建 `QMutexLocker` 时互斥量被锁定。您可以使用 `unlock()` 和 `relock()` 解锁和重新锁定互斥体。如果锁定，则当 `QMutexLocker` 被销毁时，互斥量将被解锁。

&emsp;&emsp;例如，此复杂函数在进入函数时锁定 `QMutex`，并在所有出口点解锁互斥量：

```cpp
    int complexFunction(int flag)
    {
        mutex.lock();

        int retVal = 0;

        switch (flag) {
        case 0:
        case 1:
            retVal = moreComplexFunction(flag);
            break;
        case 2:
            {
                int status = anotherFunction();
                if (status < 0) {
                    mutex.unlock();
                    return -2;
                }
                retVal = status + flag;
            }
            break;
        default:
            if (flag > 10) {
                mutex.unlock();
                return -1;
            }
            break;
        }

        mutex.unlock();
        return retVal;
    }
```

&emsp;&emsp;该示例在开发过程中会变得更加复杂，也更加容易出错。
&emsp;&emsp;使用 `QMutexLocker` 可大大简化代码，且可读性更好：

```cpp
    int complexFunction(int flag)
    {
        QMutexLocker locker(&mutex);

        int retVal = 0;

        switch (flag) {
        case 0:
        case 1:
            return moreComplexFunction(flag);
        case 2:
            {
                int status = anotherFunction();
                if (status < 0)
                    return -2;
                retVal = status + flag;
            }
            break;
        default:
            if (flag > 10)
                return -1;
            break;
        }

        return retVal;
    }
```

&emsp;现在，当 `QMutexLocker` 对象被销毁时（当函数返回时，因为 `locker` 是一个栈变量），互斥量将始终被解锁。

&emsp;&emsp;同样的原则也适用于抛出和捕获异常的代码。在将异常传递给调用函数之前，如果函数未在锁定互斥量的函数中捕获到异常，则无法解锁互斥体。

（`译者注：在进入被调函数后，被调函数锁定互斥量（使用QMutex::lock()），在执行过程中发生异常，异常被调用函数获取，被调函数就没有正确执行解锁。`）

&emsp;&emsp;`QMutexLocker` 还提供一个 `mutex()` 成员函数，该函数返回`QMutexLocker` 正在其上操作的互斥体。这对于需要访问互斥体的代码非常有用，例如 `QWaitCondition::wait()`。例如：

```cpp
    class SignalWaiter
    {
    private:
        QMutexLocker locker;

    public:
        SignalWaiter(QMutex *mutex)
            : locker(mutex)
        {
        }

        void waitForSignal()
        {
            ...
            while (!signalled)
                waitCondition.wait(locker.mutex());
            ...
        }
    };
```

**另请参阅：** [QReadLockr](../../R/QReadLocker/QReadLocker.md)，[QWriteLocker](../../W/QWriteLocker/QWriteLocker.md)，[QMutex](../QMutex/QMutex.md)。




## 成员函数文档

### QMutexLocker::QMutexLocker(QRecursiveMutex \**mutex*)

&emsp;&emsp;构造一个 `QMutexLocker` 并锁定互斥量。当 `QMutexLocker` 被销毁时，互斥量将被解锁（[unlock](#void-qmutexlockerunlock)()）。如果 `mutex` 为空，那么 `QMutexLocker` 不执行任何操作。

&emsp;&emsp;在 Qt5.14 中引入该函数。

**另请参阅：** [QMutex::lock()](../QMutex/QMutex.md#void-qmutexlock)


---
### QMutexLocker::QMutexLocker(QMutex \**mutex*)

&emsp;&emsp; 构造一个  并锁定互斥量。当 `QMutexLocker` 被销毁时，互斥量将被解锁。如果 `mutex` 为空，那么 `QMutexLocker` 不执行任何操作。

**另请参阅：** [QMutex::lock()](../QMutex/QMutex.md#void-qmutexlock)


---
### QMutexLocker::~QMutexLocker()

&emsp;&emsp;销毁 `QMutexLocker` 并解除锁定构造函数中锁定的互斥量。

**另请参阅：** [QMutex::unlock()](../QMutex/QMutex.md#void-qmutexunlock)

### [QMutex](../QMutex/QMutex.md) \*QMutexLocker::mutex() const

&emsp;&emsp;返回 `QMutexLocker` 正在操作的互斥量。

---
### void QMutexLocker::relock()

&emsp;&emsp;重新锁定，未上锁的互斥量。

**另请参阅：** [unlock()](#void-qmutexlockerunlock)


---
### void QMutexLocker::unlock()

&emsp;&emsp;解锁这个互斥量。您可以使用 `relock()` 再次锁定它。销毁时不需要锁定。

**另请参阅：** [relock()](#void-qmutexlockerrelock)

