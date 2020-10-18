
# QWaitCondition

&emsp;&emsp;`QWaitCondition` 提供一个用于同步线程的条件变量。[更多...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include<QWaitCondition>`|
|qmake|`QT += core`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。


## 公共成员函数

|返回类型|函数|
|-|-|
||**[QWaitCondition](#qwaitconditionqwaitcondition)**()|
||**[~QWaitCondition](#qwaitconditionqwaitcondition-1)**()|
|void|**[notify_all](#void-qwaitconditionnotifyall)**()|
|void|**[notify_one](#void-qwaitconditionnotifyone)**()|
|bool|**[wait](#bool-qwaitconditionwaitqmutex-lockedmutex-qdeadlinetimer-deadline--qdeadlinetimerqdeadlinetimerforever)**(QMutex \**lockedMutex*, QDeadlineTimer *deadline* = QDeadlineTimer(QDeadlineTimer::Forever))|
|bool|**[wait](#bool-qwaitconditionwaitqmutex-lockedmutex-unsigned-long-time)**(QMutex \**lockedMutex*, unsigned long *time*)|
|bool|**[wait](#bool-qwaitconditionwaitqreadwritelock-lockedreadwritelock-qdeadlinetimer-deadline--qdeadlinetimerqdeadlinetimerforever)**(QReadWriteLock \**lockedReadWriteLock*, QDeadlineTimer *deadline* = QDeadlineTimer(QDeadlineTimer::Forever))|
|bool|**[wait](#bool-qwaitconditionwaitqreadwritelock-lockedreadwritelock-unsigned-long-time)**(QReadWriteLock \**lockedReadWriteLock*, unsigned long *time*)|
|void|**[wakeAll](#void-qwaitconditionwakeall)**()|
|void|**[wakeOne](#void-qwaitconditionwakeone)**()|



## 详细描述

&emsp;&emsp;`QWaitCondition` 允许线程告诉其他线程某种条件已经满足。一个或多个线程可以被阻塞并等待 `QWaitCondition` 用 [wakeOne](#void-qwaitconditionwakeone)() 或 [wakeAll](#void-qwaitconditionwakeall)() 设置条件。使用 [wakeOne](#void-qwaitconditionwakeone)() 唤醒一个随机选择的线程，或使用 [wakeAll](#void-qwaitconditionwakeall)() 唤醒所有线程。  
&emsp;&emsp;例，假设我们有三个任务，当用户按下一个键时，应该执行某些任务。每个任务可以分成一个线程，每个线程都有一个 [run](../../T/QThread/QThread.md)() 主体，如下所示：
```cpp
forever {
    mutex.lock();
    keyPressed.wait(&mutex);
    do_something();
    mutex.unlock();
}
```
&emsp;&emsp;这里，`keyPressed` 变量是 `QWaitCondition` 类型的全局变量。  
&emsp;&emsp;第四个线程将读取按键，并在每次收到按键时唤醒其他三个线程，如下所示：
```cpp
forever {
    getchar();
    keyPressed.wakeAll();
}
```
&emsp;&emsp;唤醒三个线程的顺序是未知的。另外，如果某些线程在按下键时仍在 `do_something()` 中，它们将不会被唤醒（因为它们没有等待条件变量），因此该按键不会执行任务。这个问题可以通过使用计数器和 [QMutex](../../M/QMutex/QMutex.md)() 来解决。例如，下面是工作线程的新代码：
```cpp
forever {
    mutex.lock();
    keyPressed.wait(&mutex);
    ++count;
    mutex.unlock();

    do_something();

    mutex.lock();
    --count;
    mutex.unlock();
}
```
&emsp;&emsp;下面是第四个线程的代码：
```cpp
forever {
    getchar();

    mutex.lock();
    // Sleep until there are no busy worker threads
    while (count > 0) {
        mutex.unlock();
        sleep(1);
        mutex.lock();
    }
    keyPressed.wakeAll();
    mutex.unlock();
}
```
&emsp;&emsp;互斥量是必需的，因为当两个线程同时更改同一变量的值时，结果是不可预测的。  
&emsp;&emsp;等待条件是一个强大的线程同步原语。[Wait Conditions示例]()演示了如何使用 `QWaitCondition` 作为 [QSemaphore](../../S/QSemaphore/QSemaphore.md)() 的替代品，来控制生产者消费者的共享循环缓冲区的访问。

**另请参阅：** [QMutex](../../M/QMutex/QMutex.md)、[QSemaphore](../../S/QSemaphore/QSemaphore.md)、[QThread](../../T/QThread/QThread.md)() 和 [Wait Conditions示例]()。



## 成员函数文档

### QWaitCondition::QWaitCondition()

&emsp;&emsp;构造。

---
### QWaitCondition::~QWaitCondition()

&emsp;&emsp;析构。

---
### void QWaitCondition::notify_all()

&emsp;&emsp;用于STL兼容。它相当于 [wakeAll](#void-qwaitconditionwakeall)()。  
&emsp;&emsp;在 Qt 5.8 引入该函数。

---
### void QWaitCondition::notify_one()

&emsp;&emsp;用于STL兼容。它相当于 [wakeOne](#void-qwaitconditionwakeone)()。  
&emsp;&emsp;在 Qt 5.8 引入该函数。

---
### bool QWaitCondition::wait(QMutex \**lockedMutex*, QDeadlineTimer *deadline* = QDeadlineTimer(QDeadlineTimer::Forever))

&emsp;&emsp;释放 `lockedMutex` 并等待条件。`lockedMutex` 最初必须由调用线程锁定。如果 `lockedMutex` 未处于锁定状态，则行为未定义。如果 `lockedMutex` 是递归互斥体，则此函数将立即返回。`lockedMutex` 将被解锁，调用线程将阻塞，直到满足以下任一条件：

- 另一个线程调用 [wakeOne](#void-qwaitconditionwakeone)() 或 [wakeAll](#void-qwaitconditionwakeall)() 发出信号。在这种情况下，此函数将返回true。
- 截止日期已到。如果 `deadline` 是默认值 `QDeadlineTimer::Forever`，则永远不会超时（必须用信号通知事件）。如果等待超时，此函数将返回false。

&emsp;&emsp;`lockedMutex` 将返回到相同的锁定状态。提供此函数是为了允许原子从锁定状态转换到等待状态。
&emsp;&emsp;在 Qt 5.12 引入该函数。

**另请参阅：** [wakeOne](#void-qwaitconditionwakeone)()、[wakeAll](#void-qwaitconditionwakeall)()。

---
### bool QWaitCondition::wait(QMutex \**lockedMutex*, unsigned long *time*)

&emsp;&emsp;重载。

---
### bool QWaitCondition::wait(QReadWriteLock \**lockedReadWriteLock, QDeadlineTimer *deadline* = QDeadlineTimer(QDeadlineTimer::Forever))

&emsp;&emsp;释放 `lockedReadWriteLock` 并等待条件。`lockedReadWriteLock` 最初必须由调用线程锁定。如果 `lockedReadWriteLock` 未处于锁定状态，则此函数将立即返回。 `lockedReadWriteLock` 不能递归锁定，否则此函数将无法正确释放锁。`lockedReadWriteLock` 将被解锁，调用线程将阻塞，直到满足以下任一条件：

+ 另一个线程调用 [wakeOne](#void-qwaitconditionwakeone)() 或 [wakeAll](#void-qwaitconditionwakeall)() 发出信号。在这种情况下，此函数将返回true。
+ 截止日期已到。如果 `deadline` 是默认值 `QDeadlineTimer::Forever`，则永远不会超时（必须用信号通知事件）。如果等待超时，此函数将返回false。

&emsp;&emsp;`lockedReadWriteLock` 将返回到相同的锁定状态。提供此函数是为了允许原子从锁定状态转换到等待状态。  
&emsp;&emsp;在 Qt 5.12 引入该函数。

**另请参阅：** [wakeOne](#void-qwaitconditionwakeone)()、[wakeAll](#void-qwaitconditionwakeall)()。

---
### bool QWaitCondition::wait(QReadWriteLock \**lockedReadWriteLock*, unsigned long *time*)

&emsp;&emsp;重载。


---
### void QWaitCondition::wakeAll()

&emsp;&emsp;唤醒等待条件的所有线程。线程的唤醒顺序取决于操作系统的调度策略，无法控制或预测。

**另请参阅：** [wakeOne](#void-qwaitconditionwakeone)()。


---
### void QWaitCondition::wakeOne()

&emsp;&emsp;唤醒一个等待条件的线程。线程的唤醒顺序取决于操作系统的调度策略，无法控制或预测。  
&emsp;&emsp;如果要唤醒特定线程，解决方案通常是使用不同的等待条件，并让线程在不同的条件下等待。

**另请参阅：** [wakeAll](#void-qwaitconditionwakeall)()。
