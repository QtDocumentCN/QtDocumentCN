[TOC]



# QTimer Class

QTimer提供了重复和信号槽的定时器。

| 属性     | 方法                                  |
| -------- | ------------------------------------- |
| 头文件： | #include <QTimer>                     |
| qmake:   | QT += core                            |
| 继承：   | [QObject](../../O/QObject/QObject.md) |

## 属性

| 属性名        | 类型          |
| ------------- | ------------- |
| active        | const bool    |
| singleShot    | bool          |
| interval      | int           |
| timeType      | Qt::TimerType |
| remainingTime | const int     |

## 公有成员函数



| 类型                      | 函数名                                                       |
| ------------------------- | ------------------------------------------------------------ |
|                           | [QTimer](qtimer.html#QTimer)(QObject **parent* = nullptr)    |
| virtual                   | [~QTimer](qtimer.html#dtor.QTimer)()                         |
| QMetaObject::Connection   | [callOnTimeout](qtimer.html#callOnTimeout)(Functor *slot*, Qt::ConnectionType *connectionType* = ...) |
| QMetaObject::Connection   | [callOnTimeout](qtimer.html#callOnTimeout-1)(const QObject **context*, Functor *slot*, Qt::ConnectionType *connectionType* = ...) |
| QMetaObject::Connection   | [callOnTimeout](qtimer.html#callOnTimeout-2)(const QObject **receiver*, PointerToMemberFunction *slot*, Qt::ConnectionType *connectionType* = ...) |
| int                       | [interval](qtimer.html#interval-prop)() const                |
| std::chrono::milliseconds | [intervalAsDuration](qtimer.html#intervalAsDuration)() const |
| bool                      | [isActive](qtimer.html#isActive)() const                     |
| bool                      | [isSingleShot](qtimer.html#singleShot-prop)() const          |
| int                       | [remainingTime](qtimer.html#remainingTime-prop)() const      |
| std::chrono::milliseconds | [remainingTimeAsDuration](qtimer.html#remainingTimeAsDuration)() const |
| void                      | [setInterval](qtimer.html#interval-prop)(int *msec*)         |
| void                      | [setInterval](qtimer.html#interval-prop)(std::chrono::milliseconds *value*) |
| void                      | [setSingleShot](qtimer.html#singleShot-prop)(bool *singleShot*) |
| void                      | [setTimerType](qtimer.html#timerType-prop)(Qt::TimerType *atype*) |
| void                      | [start](qtimer.html#start-2)(std::chrono::milliseconds *msec*) |
| int                       | [timerId](qtimer.html#timerId)() const                       |
| Qt::TimerType             | [timerType](qtimer.html#timerType-prop)() const              |

- 32个共有成员函数继承自[QObject](../../O/QObject/QObject.md)

## 公有槽函数

| 类型 | 函数名                                 |
| ---- | -------------------------------------- |
| void | [start](qtimer.html#start)(int *msec*) |
| void | [start](qtimer.html#start-1)()         |
| void | [stop](qtimer.html#stop)()             |

- 一个公有槽函数继承自[QObject](../../O/QObject/QObject.md)

## 信号

| 类型 | 函数名                           |
| ---- | -------------------------------- |
| void | [timeout](qtimer.html#timeout)() |

- 2个信号继承自[QObject](../../O/QObject/QObject.md)



## 静态公有成员函数

| 类型              | 函数名                                                       |
| ----------------- | ------------------------------------------------------------ |
| void              | [singleShot](qtimer.html#singleShot)(int *msec*, const QObject **receiver*, const char **member*) |
| void              | [singleShot](qtimer.html#singleShot-1)(int *msec*, Qt::TimerType *timerType*, const QObject **receiver*, const char **member*) |
| void              | [singleShot](qtimer.html#singleShot-2)(int *msec*, const QObject **receiver*, PointerToMemberFunction *method*) |
| void              | [singleShot](qtimer.html#singleShot-3)(int *msec*, Qt::TimerType *timerType*, const QObject **receiver*, PointerToMemberFunction *method*) |
| void              | [singleShot](qtimer.html#singleShot-4)(int *msec*, Functor *functor*) |
| void              | [singleShot](qtimer.html#singleShot-5)(int *msec*, Qt::TimerType *timerType*, Functor *functor*) |
| void              | [singleShot](qtimer.html#singleShot-6)(int *msec*, const QObject **context*, Functor *functor*) |
| void              | [singleShot](qtimer.html#singleShot-7)(int *msec*, Qt::TimerType *timerType*, const QObject **context*, Functor *functor*) |
| void              | [singleShot](qtimer.html#singleShot-8)(std::chrono::milliseconds *msec*, const QObject **receiver*, const char **member*) |
| void              | [singleShot](qtimer.html#singleShot-9)(std::chrono::milliseconds *msec*, Qt::TimerType *timerType*, const QObject **receiver*, const char **member*) |
| const QMetaObject | [staticMetaObject](qtimer.html#staticMetaObject-var)         |

- 10个静态公有成员函数继承自[QObject](../../O/QObject/QObject.md)

## 重新实现保护成员函数

| 类型         | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | [timerEvent](qtimer.html#timerEvent)(QTimerEvent **e*) override |

- 9个保护成员函数继承自[QObject](../../O/QObject/QObject.md)

## 详细描述

[QTimer](qtimer.html) 类提供重复和单次定时器。

The [QTimer](qtimer.html) 类为定时器提供了高级编程接口。 要使用它，请创建一个[QTimer](qtimer.html), 将 [timeout](qtimer.html#timeout)() 信号连接到相应的插槽, 然后调用 [start](qtimer.html#start-1)(). 从那时起，它将以固定时间间隔发出 [timeout](qtimer.html#timeout)() 信号。

一秒 (1000 毫秒) 定时器的示例 (来自 [Analog Clock](../qtwidgets/qtwidgets-widgets-analogclock-example.html) 例子):

```
QTimer *timer = new QTimer(this);
      connect(timer, SIGNAL(timeout()), this, SLOT(update()));
      timer->start(1000);
```

从那时起，update()槽函数每秒都被调用。

你可以调用[setSingleShot](qtimer.html#singleShot-prop)(true)仅触发一次定时器。你也可以使用静态[QTimer::singleShot](qtimer.html#singleShot)() 函数在特定的时间内调用一个槽函数

```
      QTimer::singleShot(200, this, SLOT(updateCaption()));
```



在多线程应用，你可以使用QTimer在任何一个有事件循环的线程。使用[QThread::exec](qthread.html#exec)()，开启一个非GUI线程的事件循环。Qt使用[线程亲和性]()定义哪一个线程会发出[timeout()](qtimer.html#timeout)信号。因此，你必须在指定线程内开启和关闭定时器， 它不可能开启一个定时器从另一个线程。

在特殊案例里，窗口系统的事件队列中的所有事件都已处理后，超时为0的定时器将立即超时。 在提供快速的用户界面时，这可以用来完成繁重的工作：

```
  QTimer *timer = new QTimer(this);
      connect(timer, SIGNAL(timeout()), this, SLOT(processOneThing()));
      timer->start();

```



从那以后，processOneThing()将会被重复调用。应该以始终快速返回（通常在处理一个数据项之后）的方式编写。 因此，Qt一处理完定时器上所有工作后，就能够分发事件提供给用户接口和停止定时器。对于GUI应用来说，这是典型的方法实现繁重工作。但如今越来越多应用了多线程，我们期待0毫秒的定时器对象会逐渐被[QThread](../../T/QThread/QThread.md)取代。

##　精度和时间分辨率

定时器的精度依赖底层操作系统和硬件。大多数定时器支持1毫秒的分辨率，尽管在许多实际情况下定时器的精度将不等于该分辨率。

定时器的精度依靠[timer type](qt.html#TimerType-enum)。

对于[Qt::PreciseTimer](qt.html#TimerType-enum), [QTimer](qtimer.html)会尽量保持一毫秒的精度。精确的定时器也永远不会比预期的超时。对于[Qt::CoarseTimer](qt.html#TimerType-enum) 和 [Qt::VeryCoarseTimer](qt.html#TimerType-enum) 类型, [QTimer](qtimer.html) 可能会早于我们预期中唤醒, 在这些类型的范围内: 5% 的间隔 [Qt::CoarseTimer](qt.html#TimerType-enum) 和 500 毫秒 [Qt::VeryCoarseTimer](qt.html#TimerType-enum).

如果操作系统繁忙或是不能提供所需精度，所有的时间类型都可能会晚于我们期待的。在这种超时溢出的情况下，即使多个超时已过期，Qt也会仅发出一次，然后将恢复原始间隔。

## 精度和定时器分辨率

另一周使用 [QTimer](qtimer.html) 的方法是调用 [QObject::startTimer](qobject.html#startTimer)() 为你的对象 和更新实现[QObject::timerEvent](qobject.html#timerEvent)() 事件 在类内处理 (必须继承 [QObject](qobject.html)).  [timerEvent](qtimer.html#timerEvent)() 的缺点是 不支持单次定时器或信号的高级功能。另一种选择是[QBasicTimer](qbasictimer.html)。通常，与直接使用 [QObject::startTimer](qobject.html#startTimer)() 相比，它不那么麻烦。 有关这三种方法的概述，请参见 [Timers](timers.html) 。

有些操作系统可能会限制定时器的使用数量，Qt尽量工作在这些范围之内。

另外参见 [QBasicTimer](qbasictimer.html), [QTimerEvent](qtimerevent.html), [QObject::timerEvent](qobject.html#timerEvent)(), [Timers](timers.html), [Analog Clock Example](../qtwidgets/qtwidgets-widgets-analogclock-example.html), 和 [Wiggly Example](../qtwidgets/qtwidgets-widgets-wiggly-example.html).



## 属性文档



| 属性名 | 类型       |
| ------ | ---------- |
| active | const bool |

如果定时器正在执行，这个属性是true, 否则是false。

**访问函数**

| 类型 | 函数名                                   |
| ---- | ---------------------------------------- |
| bool | [isActive](qtimer.html#isActive)() const |





| 属性名   | 类型 |
| -------- | ---- |
| interval | int  |

此属性保存超时间隔（以毫秒为单位）

一旦处理完窗口系统事件队列中的所有事件，超时间隔为0的[QTimer](qtimer.html) 就会超时。

此属性的默认值为0。 设置活动定时器的间隔会改变 [timerId](qtimer.html#timerId)()。

**访问函数：**

| 类型 | 函数名                                         |
| ---- | ---------------------------------------------- |
| int  | interval() const                               |
| void | setInterval(int *msec*)                        |
| void | setInterval(std::chrono::milliseconds *value*) |

另外参见 [singleShot](qtimer.html#singleShot-prop).

###

| 属性名        | 类型      |
| ------------- | --------- |
| remainingTime | const int |

此属性保留剩余时间（以毫秒为单位）

返回定时器的剩余值（以毫秒为单位），直到超时为止。 如果定时器处于非活动状态，则返回值为-1。 如果定时器过期，则返回值为0。

此属性在Qt 5.0中引入。

**访问函数：**

| 类型 | 函数名                |
| ---- | --------------------- |
| int  | remainingTime() const |

另外参见 [interval](qtimer.html#interval-prop).

###

| 属性名     | 类型 |
| ---------- | ---- |
| singleShot | bool |

此属性保持定时器是否为单次定时器。

单触发定时器仅触发一次，非单触发定时器每[interval](qtimer.html#interval-prop)毫秒触发一次。

此属性的默认值是false。

**访问函数：**

| 类型 | 函数名                           |
| ---- | -------------------------------- |
| bool | isSingleShot() const             |
| void | setSingleShot(bool *singleShot*) |

另外参见 [interval](qtimer.html#interval-prop) 和 [singleShot](qtimer.html#singleShot)().

###

| 类型      | 属性名                                  |
| --------- | --------------------------------------- |
| timerType | [Qt::TimerType](qt.html#TimerType-enum) |

控制定时器的精度。

默认的属性是  Qt::CoarseTimer。

**访问函数：**

| 类型          | 函数名                              |
| ------------- | ----------------------------------- |
| Qt::TimerType | timerType() const                   |
| void          | setTimerType(Qt::TimerType *atype*) |

另外参见 [Qt::TimerType](qt.html#TimerType-enum)。

### 成员函数文档

### QTimer::QTimer([QObject](qobject.html#QObject) **parent* = nullptr)

使用给定的*parent* 构造一个定时器。



### [virtual] QTimer::~QTimer()

销毁定时器。

### [Q](qmetaobject-connection.html)MetaObject::Connection QTimer::callOnTimeout(Functor *slot*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *connectionType* = ...)

这是一个重载函数。

创建一个从[timeout](qtimer.html#timeout)() 信号到slot的连接，并返回一个连接句柄。

为了方便提供了这个方法。它等价于调用：

```
It's equivalent to calling QObject::connect(timer, &QTimer::timeout, timer, slot, connectionType).
```

在Qt5.12引入该函数。

另外参见 [QObject::connect](qobject.html#connect)() 和 [timeout](qtimer.html#timeout)().

###  [Q](qmetaobject-connection.html)MetaObject::Connection QTimer::callOnTimeout(const [QObject](qobject.html#QObject) **context*, Functor *slot*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *connectionType* = ...)

此函数重载 [callOnTimeout](qtimer.html#callOnTimeout)().

创建一个从 [timeout](qtimer.html#timeout)() 信号到slot的连接，将其放置在context的特定事件循环中，并返回该连接的句柄。

为了方便提供了这个方法。它等价于调用：

```
QObject::connect(timer, &QTimer::timeout, context, slot, connectionType).
```

在Qt5.12引入该函数。

另外参见 [QObject::connect](qobject.html#connect)() 和 [timeout](qtimer.html#timeout)().

###  [Q](qmetaobject-connection.html)MetaObject::Connection QTimer::callOnTimeout(const [QObject](qobject.html#QObject) **receiver*, PointerToMemberFunction *slot*, [Qt::ConnectionType](qt.html#ConnectionType-enum) *connectionType* = ...)

此函数重载 [callOnTimeout](qtimer.html#callOnTimeout)().

创建一个从 [timeout](qtimer.html#timeout)() 信号到slot的连接，将其放置在context的特定事件循环中，并返回该连接的句柄。

为了方便提供了这个方法。它等价于调用：

```
QObject::connect(timer, &QTimer::timeout, receiver, slot, connectionType).
```

在Qt5.12引入该函数。

另外参见 [QObject::connect](qobject.html#connect)() 和 [timeout](qtimer.html#timeout)().

### std::chrono::milliseconds QTimer::intervalAsDuration() const

以std::chrono::milliseconds 对象的形式返回此定时器的间隔。

在Qt5.8引入该函数。

另外参见 [interval](qtimer.html#interval-prop).

###  bool QTimer::isActive() const

如果定时器正在运行（正在等待），则返回true；否则，返回false。 否则返回false。

**注意:** 获取函数来自属性active。

### std::chrono::milliseconds QTimer::remainingTimeAsDuration() const

以std :: chrono :: milliseconds对象的形式返回此定时器对象中剩余的时间。 如果此定时器到期或过期，则返回的值为std :: chrono :: milliseconds :: zero（）。 如果找不到剩余时间或定时器未激活，则此函数返回负值持续时间。

在Qt5.8引入该函数。

### [static] void QTimer::singleShot(int *msec*, const [QObject](qobject.html#QObject) **receiver*, const char **member*)

在给定的时间间隔后，此静态函数调用slot。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

```
Example:

  #include <QApplication>
  #include <QTimer>

  int main(int argc, char *argv[])
  {
      QApplication app(argc, argv);
      QTimer::singleShot(600000, &app, SLOT(quit()));
      ...
      return app.exec();
  }
```

这个示例程序自动在10分钟(600,000毫秒)触发。

*receiver* 是接收对象，而 *member* 是插槽。 时间间隔是 *msec* 毫秒。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

### [static] void QTimer::singleShot(int *msec*, [Qt::TimerType](qt.html#TimerType-enum) *timerType*, const [QObject](qobject.html#QObject) **receiver*, const char **member*)

这是一个重载函数。

在给定的时间间隔后，此静态函数调用slot。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

*receiver* 是接收对象，而 *member* 是插槽。 时间间隔是 *msec* 毫秒。 *timerType* 影响了定时器的精度。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

另外参见 [start](qtimer.html#start-1)().

###  [static] void QTimer::singleShot(int *msec*, const [QObject](qobject.html#QObject) **receiver*, PointerToMemberFunction *method*)

这是一个重载函数。

在给定的时间间隔后，此静态函数调用slot。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

*receiver* 是接收对象，而 *member* 是插槽。 时间间隔是 *msec* 毫秒。

如果在间隔发生之前销毁了*receiver*，则不会调用该方法。 该函数将在*receiver*的线程中运行。 接收者的线程必须具有正在运行的Qt事件循环。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)().

###  [static] void QTimer::singleShot(int *msec*, [Qt::TimerType](qt.html#TimerType-enum) *timerType*, const [QObject](qobject.html#QObject) **receiver*, PointerToMemberFunction *method*)

这是一个重载函数。

在给定的时间间隔后，此静态函数调用slot。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

*receiver* 是接收对象，而 *member* 是插槽。 时间间隔是 *msec* 毫秒。 *timerType* 影响了定时器的精度。

如果在间隔发生之前销毁了*receiver*，则不会调用该方法。 该函数将在*receiver*的线程中运行。 接收者的线程必须具有正在运行的Qt事件循环。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [static] void QTimer::singleShot(int *msec*, Functor *functor*)

这是一个重载函数。

在给定的时间间隔后，此静态函数将调用*functor*。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

时间间隔是*msec* 毫秒。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [static] void QTimer::singleShot(int *msec*, [Qt::TimerType](qt.html#TimerType-enum) *timerType*, Functor *functor*)

这是一个重载函数。

在给定的时间间隔后，此静态函数将调用*functor*。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

时间间隔是*msec* 毫秒。 *timerType* 影响了定时器的精度。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [static] void QTimer::singleShot(int *msec*, const [QObject](qobject.html#QObject) **context*, Functor *functor*)

这是一个重载函数。

在给定的时间间隔后，此静态函数将调用*functor*。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

时间间隔是*msec* 毫秒。

如果*context*在间隔发生之前被破坏，则不会调用该方法。 该函数将在*context*线程中运行。 上下文的线程必须具有正在运行的Qt事件循环。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)()。

### [static] void QTimer::singleShot(int *msec*, [Qt::TimerType](qt.html#TimerType-enum) *timerType*, const [QObject](qobject.html#QObject) **context*, Functor *functor*)

这是一个重载函数。

在给定的时间间隔后，此静态函数将调用*functor*。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

时间间隔是*msec* 毫秒。 *timerType* 影响了定时器的精度。

如果*context*在间隔发生之前被破坏，则不会调用该方法。 该函数将在*context*线程中运行。 上下文的线程必须具有正在运行的Qt事件循环。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.4引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [static] void QTimer::singleShot(std::chrono::milliseconds *msec*, const [QObject](qobject.html#QObject) **receiver*, const char **member*)

这是一个重载函数。

时间间隔是*msec* 毫秒。 *timerType* 影响了定时器的精度。非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

The *receiver*是接收对象，而*member* 是插槽。时间间隔是 *msec*。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.8引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [static] void QTimer::singleShot(std::chrono::milliseconds *msec*, [Qt::TimerType](qt.html#TimerType-enum) *timerType*, const [QObject](qobject.html#QObject) **receiver*, const char **member*)

这是一个重载函数。

在给定的时间间隔后，此静态函数将调用slot。

非常方便去使用这个函数。因为你不需要关心timerEvent或创造一个局部的QTimer对象。

*receiver*是接收对象，*member*是插槽。 msec在持续时间对象毫秒中给出。 timerType影响定时器的准确性。

**注意：** 该函数是[可重入](../../T/threads-reentrancy.html)。

在Qt5.8引入该函数。

另外参见 [start](qtimer.html#start-1)().

### [slot] void QTimer::start(int *msec*)

以*msec*毫秒的超时间隔启动或重新启动定时器。

如果定时器已经在运行，它将被[stopped](qtimer.html＃stop)并重新启动。如果[singleShot](qtimer.html#singleShot-prop) 是 true, 则定时器将仅激活一次。

### [slot] void QTimer::start()

重载start()函数。

以[interval](qtimer.html#interval-prop).中指定的超时时间启动或重新启动定时器。

如果定时器已经运行，它将[stopped](qtimer.html#stop) 和重新启动。

如果 [singleShot](qtimer.html#singleShot-prop) 是 true, 则定时器将仅激活一次。

### void QTimer::start(std::chrono::milliseconds *msec*)

这是重载函数。

以*msec*毫秒的持续时间启动或重启定时器。

如果定时器已经运行，它将[stopped](qtimer.html#stop) 和重新启动。

如果 [singleShot](qtimer.html#singleShot-prop) 是 true, 则定时器将仅激活一次。

### 在Qt5.8引入该函数。

### [slot] void QTimer::stop()

停止定时器。

另外参见 [start](qtimer.html#start-1)().

### [signal] void QTimer::timeout()

定时器超时时发出此信号。

**注意**：这是一个私人信号。 它可以用于信号连接，但不能由用户发射。

另外参见 [interval](qtimer.html#interval-prop), [start](qtimer.html#start-1)(), 和 [stop](qtimer.html#stop)().

###  [override virtual protected] void QTimer::timerEvent([QTimerEvent](qtimerevent.html) **e*)

重新实现自 [QObject::timerEvent](qobject.html#timerEvent)()。

###  int QTimer::timerId() const

如果定时器正在运行，则返回定时器的ID。 否则返回-1。



