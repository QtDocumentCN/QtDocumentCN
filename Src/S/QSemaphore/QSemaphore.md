


# QSemaphore

&emsp;&emsp;QSemaphore类提供了一个通用的信号量。[更多内容...](#详细描述)

|属性|内容|
|-|-|
|头文件|`#include <QSemaphore>`|
|`qmake`|`QT += core`|

**注意：** 此类中所有函数都是[线程安全](../../R/Reentrancy_and_Thread-Safety/Reentrancy_and_Thread-Safety.md)的。




## 公共成员函数

|返回类型|函数|
|-|-|
||**[QSemaphore](#qsemaphoreqsemaphoreint-n--0)**(int *n* = 0)|
||**[~QSemaphore](#qsemaphoreqsemaphore)**()|
|void|**[acquire](#void-qsemaphoreacquireint-n--1)**(int *n* = 1) const|
|int|**[available](#int-qsemaphoreavailable-const)**() const|
|void|**[release](#void-qsemaphorereleaseint-n--1)**(int *n* = 1)|
|bool|**[tryAcquire](#bool-qsemaphoretryacquireint-n--1)**(int *n* = 1)|
|bool|**[tryAcquire](#bool-qsemaphoretryacquireint-n-int-timeout)**(int *n*, int *timeout* )|




## 详细描述

&emsp;&emsp;信号量是互斥量的泛化。虽然互斥量只能锁定一次，但可以多次获取信号。信号量通常用于保护一定数量的相同资源。  

&emsp;&emsp;信号量支持两个基本操作，[acquire](#void-qsemaphoreacquireint-n--1)() 和 [release](#void-qsemaphorereleaseint-n--1)()：

* [acquire](#void-qsemaphoreacquireint-n--1)(n) 尝试获取 n 个资源。如果没有那么多可用资源，调用将被阻塞，直到能够获取。
* [release](#void-qsemaphorereleaseint-n--1)(n) 释放 n 个资源。

&emsp;&emsp;还有 [tryAcquire](#bool-qsemaphoretryacquireint-n--1)() 函数，如果无法获取资源，它将立即返回；还有一个 [available](#int-qsemaphoreavailable-const)() 函数，可以随时返回可用资源的数量。

例如：

```cpp
    QSemaphore sem(5);      // sem.available() == 5

    sem.acquire(3);         // sem.available() == 2
    sem.acquire(2);         // sem.available() == 0
    sem.release(5);         // sem.available() == 5
    sem.release(5);         // sem.available() == 10

    sem.tryAcquire(1);      // sem.available() == 9, returns true
    sem.tryAcquire(250);    // sem.available() == 9, returns false
```

&emsp;&emsp;信号量的一个典型应用场景，是控制生产者线程和消费者线程对共享循环缓冲区的访问。[生产者消费者示例]()展示了如何使用 `QSemaphore` 来解决这个问题。

&emsp;&emsp;一个非计算信号量（`non-computing`）的例子是在餐馆就餐。用餐厅里的椅子数初始化信号量。当人们到达时，他们需要要一个座位。入座后，[available](#int-qsemaphoreavailable-const)() 将减少。当人们离开时，[available](#int-qsemaphoreavailable-const)() 会增加，允许更多的人进入。如果有一个 10 人的聚会，但是餐馆只有 9 个座位，那这 10 个人会等待空出位置。但是如果此时有一个 4 人的聚会，那么他们会入座（将可用的座位减少到 5 个，10 人聚会将等待更长时间）。

**另请参阅：** [QSemaphoreReleaser]()，[QMutex](../../M/QMutex/QMutex.md)，[QWaitCondition](../../W/QWaitCondition/QWaitCondition.md)，[QThread](../../T/QThread/QThread.md) 和 [生产者消费者示例]()。




## 成员类型文档

### QSemaphore::QSemaphore(int *n* = 0)

&emsp;&emsp;构造一个信号量并将其保护的资源数量初始化为 `n`（默认为0）。

**另请参阅：** [release](#void-qsemaphorereleaseint-n--1)()，[available](#int-qsemaphoreavailable-const)()。


---
### QSemaphore::~QSemaphore()

&emsp;&emsp;析构。

**警告：析构正在使用的信号量可能会导致未定义的行为。**


---
### void QSemaphore::acquire(int *n* = 1)

&emsp;&emsp;尝试获取由信号量保护的 n 个资源。如果 `n > available()`，则此调用将阻塞，直到有足够的资源可用。

**另请参阅：** [release](#void-qsemaphorereleaseint-n--1)()，[available](#int-qsemaphoreavailable-const)()，[tryAcquire](#bool-qsemaphoretryacquireint-n--1)()。


---
### int QSemaphore::available() const

&emsp;&emsp;返回信号量当前可用的资源数。返回值永远不会是负数。

**另请参阅：** [release](#void-qsemaphorereleaseint-n--1)()，[available](#int-qsemaphoreavailable-const)()。


---
### void QSemaphore::release(int *n* = 1)

&emsp;&emsp;释放 n 个信号量保护的资源。

&emsp;&emsp;这个函数也可以用来“创建”资源。例如：
```cpp
    QSemaphore sem(5);      // 信号量保护 5 个资源  sem.avilable() == 5
    sem.acquire(5);         // 请求 5 个资源       sem.avilable() == 0
    sem.release(5);         // 释放 5 个资源       sem.avilable() == 5
    sem.release(10);        // “创建” 10 个新资源  sem.avilable() == 15
```
&emsp;&emsp;[QSemaphoreReleaser](../../S/QSemaphoreReleaser/QSemaphoreReleaser.md) 是一个围绕此函数的 [RAII](https://zh.cppreference.com/w/cpp/language/raii) 包装器。

**另请参阅：** [acquire](#void-qsemaphoreacquireint-n--1)()，[available](#int-qsemaphoreavailable-const)()，[QSemaphoreReleaser](../../S/QSemaphoreReleaser/QSemaphoreReleaser.md)。


---
### bool QSemaphore::tryAcquire(int *n* = 1)

&emsp;&emsp;尝试获取由信号量保护的 n 个资源，并在成功时返回 `true`。如果 `available() < n`，此调用立即返回 `false`，而不获取任何资源。

例如：
```cpp
    QSemaphore sem(5);      // sem.available() == 5
    sem.tryAcquire(250);    // sem.available() == 5, returns false
    sem.tryAcquire(3);      // sem.available() == 2, returns true
```

**另请参阅：** [acquire](#void-qsemaphoreacquireint-n--1)()。


---
### bool QSemaphore::tryAcquire(int *n*, int *timeout*)

&emsp;&emsp;尝试获取由信号量保护的 n 个资源，并在成功时返回 `true`。如果 `available() < n`，此调用将等待 `timeout` 毫秒，以尝试获取。

**注意：传递一个负数作为超时相当于调用 `acquire()`，也就是说，如果 `timeout` 为负数，这个函数将永远等待资源可用。**

例如：
```cpp
    QSemaphore sem(5);            // sem.available() == 5
    sem.tryAcquire(250, 1000);    // sem.available() == 5, 等待 1000 毫秒，returns false
    sem.tryAcquire(3, 30000);     // sem.available() == 2, 立即返回，returns true
```

**另请参阅：** [acquire](#void-qsemaphoreacquireint-n--1)()。


