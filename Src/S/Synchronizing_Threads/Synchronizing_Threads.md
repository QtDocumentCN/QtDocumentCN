# 线程同步

尽管线程的初衷是让代码并行运行，还是有许多时候，线程必须停下来等待其他线程。举个例子，如果两个线程试着同时写入同一个变量，这个结果是不确定的。强制线程之间，一个线程暂停下来等待另一个线程，这样的原则称为*互斥*。它是一种保护共享资源(如数据)的常用技术。

## 低级同步原语

[QMutex](../../M/QMutex/QMutex.md) 是能够进行强制互斥的基础类。若一个线程为了访问共享数据而上了互斥锁，而此时，另一个线程试着锁上加锁，将会导致第二个线程进入睡眠状态，直到第一个线程完成任务，解锁它的互斥锁。

[QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md) 类似 [QMutex](../../M/QMutex/QMutex.md) ，只是前者区分了“读”与“写”访问权限。若一段数据没有进行写入，多个线程可以安全地同时从中读取数据。 [QMutex](../../M/QMutex/QMutex.md) 能强制多个线程轮流访问共享数据，而 [QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md) 允许同时读取，提高了并行度。

[QSemaphore](../../S/QSemaphore/QSemaphore.md) 是 [QMutex](../../M/QMutex/QMutex.md) 的泛化，它保护一定数量的相同资源。[QMutex](../../M/QMutex/QMutex.md)却与之相反，它仅保护一个资源。[信号量示例]() 是 [QSemaphore](../../S/QSemaphore/QSemaphore.md) 的一个使用典例：同步访问在生产者和使用者之间的循环缓冲区。

[QWaitCondition](../../W/QWaitCondition/QWaitCondition.md) 不进行强制互斥，而是提供一个条件变量来同步线程。当其他原语导致线程等到资源被解锁时才能访问， [QWaitCondition](../../W/QWaitCondition/QWaitCondition.md) 则让线程在符合特定条件时退出等待。为了让等待中的线程继续执行，调用 [wakeOne()]() 来唤醒一个随机的线程，或者调用 [wakeAll()]() 来同时唤醒所有线程。[等待条件示例]() 将告诉您如何使用 [QWaitCondition](../../W/QWaitCondition/QWaitCondition.md) 代替 [QSemaphore](../../S/QSemaphore/QSemaphore.md) 来解决生产者-消费者问题。

**注意：**Qt 的同步类依赖于使用正确对齐的指针。举个例子，您不能在 MSVC 中使用打包类。

这些线程同步类让方法线程变得安全。不过，这会导致性能损失，这就是为什么大多数 Qt 的方法没能实现线程安全。

## 风险

如果一个线程锁定了一个资源，却在没有使用完毕后解锁它，将会导致程序冻结，因为其他线程将永远无法访问该资源。这种情况有可能发生，例如，在异常抛出，强制当前函数返回时没有解锁资源。

另一个类似的场景是 *死锁* 。例如，假设线程 A 正在等待线程 B 解锁一个资源。若此时线程 B 也在等待线程 A 解锁另一个资源，那么两个线程持续相互等待，因此将造成程序冻结。

## 提供便利的类

[QMutexLocker](../../M/QMutexLocker/QMutexLocker.md)，[QReadLocker](../../R/QReadLocker/QReadLocker.md) 与 [QWriteLocker](../../W/QWriteLocker/QWriteLocker.md) 使得 [QMutex](../../M/QMutex/QMutex.md) 与 [QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md) 使用起来更加简单。这些类会在他们构造时锁定资源，在析构时自动解锁资源。设计它们的初衷是简化使用 [QMutex](../../M/QMutex/QMutex.md) 与 [QReadWriteLock](../../R/QReadWriteLock/QReadWriteLock.md) 的代码，降低资源被意外永久锁定的可能性。

## 高级事件队列

Qt 事件系统在线程间通信中非常有用。每个线程都有自己的事件循环。要使槽函数在另一个线程中调用(或任何可动态调用的方法)，可将该调用代码置入目标线程的事件循环中。这可让目标线程在槽函数开始运行前完成任务，而原始线程继续并行运行。

若要将调用代码置于事件循环中，可创建一个队列[信号槽]()连接。每当发出信号时，事件系统将记录它的参数。接收此信号的线程将会执行槽函数。此外，也可以使用 [QMetaObject::invokeMethod]()() ，达到同样效果的同时无需信号。在这两种情况下，必须使用[队列连接]()，因为[直接连接]()会绕过事件系统，在当前线程中立刻执行方法。

不同于低级原语，使用事件系统进行线程同步没有死锁的风险。不过，事件系统不会强制执行互斥。如果可动态调用的方法访问共享数据，则必须使用低级原语对其进行保护。

话说回来，Qt 的事件系统以及[隐式共享]()的数据结构，提供了传统线程锁定的替代方案。如果仅使用信号槽，且线程间无共享变量，多线程程序可以完全不使用低级原语。

**另请参阅** [QThread::exec]()() 以及 [线程与 QObject ]() 。