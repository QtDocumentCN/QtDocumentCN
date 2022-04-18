# QTimeLine Class

QTimeLine类提供用于控制动画的时间线。

| 头文件: | #include <QTimeLine>                           |
| ------- | ---------------------------------------------- |
| qmake:  | QT += core                                     |
| Since:  | Qt 4.2                                         |
| 父类:   | [QObject](../../O/QObject/QObject.md) |

## 公共类型

| 类型 | 方法                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[Direction](https://doc.qt.io/qt-5/qtimeline.html#Direction-enum)** { Forward, Backward } |
| enum | **[State](https://doc.qt.io/qt-5/qtimeline.html#State-enum)** { NotRunning, Paused, Running } |

## 属性

| **[currentTime](https://doc.qt.io/qt-5/qtimeline.html#currentTime-prop)** : int | **[easingCurve](https://doc.qt.io/qt-5/qtimeline.html#easingCurve-prop)** : QEasingCurve |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[direction](https://doc.qt.io/qt-5/qtimeline.html#direction-prop)** : Direction | **[loopCount](https://doc.qt.io/qt-5/qtimeline.html#loopCount-prop)** : int |
| **[duration](https://doc.qt.io/qt-5/qtimeline.html#duration-prop)** : int | **[updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop)** : int |

## 公共成员函数

| 类型                 | 函数名                                                       |
| -------------------- | ------------------------------------------------------------ |
|                      | **[QTimeLine](https://doc.qt.io/qt-5/qtimeline.html#QTimeLine)**(int *duration* = 1000, QObject **parent* = nullptr) |
| virtual              | **[~QTimeLine](https://doc.qt.io/qt-5/qtimeline.html#dtor.QTimeLine)**() |
| int                  | **[currentFrame](https://doc.qt.io/qt-5/qtimeline.html#currentFrame)**() const |
| int                  | **[currentTime](https://doc.qt.io/qt-5/qtimeline.html#currentTime-prop)**() const |
| qreal                | **[currentValue](https://doc.qt.io/qt-5/qtimeline.html#currentValue)**() const |
| QTimeLine::Direction | **[direction](https://doc.qt.io/qt-5/qtimeline.html#direction-prop)**() const |
| int                  | **[duration](https://doc.qt.io/qt-5/qtimeline.html#duration-prop)**() const |
| QEasingCurve         | **[easingCurve](https://doc.qt.io/qt-5/qtimeline.html#easingCurve-prop)**() const |
| int                  | **[endFrame](https://doc.qt.io/qt-5/qtimeline.html#endFrame)**() const |
| int                  | **[frameForTime](https://doc.qt.io/qt-5/qtimeline.html#frameForTime)**(int *msec*) const |
| int                  | **[loopCount](https://doc.qt.io/qt-5/qtimeline.html#loopCount-prop)**() const |
| void                 | **[setDirection](https://doc.qt.io/qt-5/qtimeline.html#direction-prop)**(QTimeLine::Direction *direction*) |
| void                 | **[setDuration](https://doc.qt.io/qt-5/qtimeline.html#duration-prop)**(int *duration*) |
| void                 | **[setEasingCurve](https://doc.qt.io/qt-5/qtimeline.html#easingCurve-prop)**(const QEasingCurve &*curve*) |
| void                 | **[setEndFrame](https://doc.qt.io/qt-5/qtimeline.html#setEndFrame)**(int *frame*) |
| void                 | **[setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)**(int *startFrame*, int *endFrame*) |
| void                 | **[setLoopCount](https://doc.qt.io/qt-5/qtimeline.html#loopCount-prop)**(int *count*) |
| void                 | **[setStartFrame](https://doc.qt.io/qt-5/qtimeline.html#setStartFrame)**(int *frame*) |
| void                 | **[setUpdateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop)**(int *interval*) |
| int                  | **[startFrame](https://doc.qt.io/qt-5/qtimeline.html#startFrame)**() const |
| QTimeLine::State     | **[state](https://doc.qt.io/qt-5/qtimeline.html#state)**() const |
| int                  | **[updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop)**() const |
| virtual qreal        | **[valueForTime](https://doc.qt.io/qt-5/qtimeline.html#valueForTime)**(int *msec*) const |

## 公共槽函数

| 返回类型 | 函数名                                                       |
| -------- | ------------------------------------------------------------ |
| void     | **[resume](https://doc.qt.io/qt-5/qtimeline.html#resume)**() |
| void     | **[setCurrentTime](https://doc.qt.io/qt-5/qtimeline.html#currentTime-prop)**(int *msec*) |
| void     | **[setPaused](https://doc.qt.io/qt-5/qtimeline.html#setPaused)**(bool *paused*) |
| void     | **[start](https://doc.qt.io/qt-5/qtimeline.html#start)**()   |
| void     | **[stop](https://doc.qt.io/qt-5/qtimeline.html#stop)**()     |
| void     | **[toggleDirection](https://doc.qt.io/qt-5/qtimeline.html#toggleDirection)**() |

## 信号

| 返回类型 | 函数名                                                       |
| -------- | ------------------------------------------------------------ |
| void     | **[finished](https://doc.qt.io/qt-5/qtimeline.html#finished)**() |
| void     | **[frameChanged](https://doc.qt.io/qt-5/qtimeline.html#frameChanged)**(int *frame*) |
| void     | **[stateChanged](https://doc.qt.io/qt-5/qtimeline.html#stateChanged)**(QTimeLine::State *newState*) |
| void     | **[valueChanged](https://doc.qt.io/qt-5/qtimeline.html#valueChanged)**(qreal *value*) |

## 重写保护成员函数

| 返回类型     | 函数名                                                       |
| ------------ | ------------------------------------------------------------ |
| virtual void | **[timerEvent](https://doc.qt.io/qt-5/qtimeline.html#timerEvent)**(QTimerEvent **event*) override |

## 详细介绍

它通常用于周期性地调用槽函数来使 GUI 控件设置动画效果。您可以通过以毫秒为单位为QTimeline的构造函数来构建时间线。时间轴的持续时间描述了动画将运行多长时间。然后通过调用setframerange（）设置合适的帧范围。最后将FrameChanged（）信号连接到您希望动画的窗口小部件中的合适插槽（例如，QProgressBar中的SetValue（））。当您继续调用 start ()时，QTimeLine 将进入 Running 状态，并开始定期发送 framecchanged ()信号 ，使您的小部件的连接属性的值从较低端增长到较高端，并以一个稳定的速率增长到帧范围的较高端。可以通过调用 setUpdateInterval ()来指定更新间隔。完成后，QTimeLine 进入 NotRunning 状态，并发出 finished ()。

例子:

```c++
...
progressBar = new QProgressBar(this);
progressBar->setRange(0, 100);

// Construct a 1-second timeline with a frame range of 0 - 100
QTimeLine *timeLine = new QTimeLine(1000, this);
timeLine->setFrameRange(0, 100);
connect(timeLine, &QTimeLine::frameChanged, progressBar, &QProgressBar::setValue);

// Clicking the push button will start the progress bar animation
pushButton = new QPushButton(tr("Start animation"), this);
connect(pushButton, &QPushButton::clicked, timeLine, &QTimeLine::start);
...
```

默认情况下，时间线从开始到结束运行一次，您必须在此时间线上再次调用 start ()以重新启动。要使时间线循环，可以调用 setLoopCount () ，传递在完成之前时间线应该运行的次数。还可以通过调用 setDirection ()更改方向，从而使时间线向后运行。您还可以在时间轴运行时调用 setestated ()来暂停和取消暂停。对于交互控制，提供了 setCurrentTime ()函数，它直接设置时间线的时间位置。尽管在 NotRunning 状态下最有用(例如，连接到 QSlider 中的 valueChanged ()信号) ，但是这个函数可以在任何时候调用。

框架界面对于标准部件很有用，但 QTimeLine 可以用来控制任何类型的动画。QTimeLine 的核心在 valueForTime ()函数中，该函数在给定时间内生成介于0和1之间的值。此值通常用于描述动画的步骤，其中0是动画的第一步，1是最后一步。在运行时，QTimeLine 通过调用 valueForTime ()和发出 valueChanged ()生成0到1之间的值。默认情况下，valueForTime ()应用插值算法来生成这些值。可以通过调用 setEasingCurve ()从一组预定义的时间线算法中进行选择。

请注意，默认情况下，QTimeLine 使用 QEasingCurve: : InOutSine，它提供一个缓慢增长的值，然后稳定增长，最后缓慢增长。对于自定义时间线，可以重新实现 valueForTime () ，在这种情况下，忽略 QTimeLine 的 easingCurve 属性。

**另请参阅** [QProgressBar](https://doc.qt.io/qt-5/qprogressbar.html) 和 [QProgressDialog](https://doc.qt.io/qt-5/qprogressdialog.html).

## 成员类型文档

### enum QTimeLine::Direction

此枚举描述处于 [Running](https://doc.qt.io/qt-5/qtimeline.html#State-enum)状态时的时间线方向。

| 函数                  | 值   | 描述                                              |
| --------------------- | ---- | ------------------------------------------------- |
| `QTimeLine::Forward`  | `0`  | “当前时间”随时间递增（即从0向终点/duration 移动） |
| `QTimeLine::Backward` | `1`  | ”当前时间“随时间递减（即从终点/duration 向0移动） |

**另请参阅** [setDirection](https://doc.qt.io/qt-5/qtimeline.html#direction-prop)().

### enum QTimeLine::State

此枚举描述时间线的状态。

| 函数                    | 值   | 描述                                                         |
| ----------------------- | ---- | ------------------------------------------------------------ |
| `QTimeLine::NotRunning` | `0`  | 时间线没有运行。这是 QTimeLine 的初始状态，状态 QTimeLine 在完成时重新进入。当前时间、帧和值保持不变，直到调用 setCurrentTime ()或调用 start ()启动时间线。 |
| `QTimeLine::Paused`     | `1`  | 时间线暂停（即暂时暂停）。调用setPaused（false）将恢复时间线活动。 |
| `QTimeLine::Running`    | `2`  | 时间轴正在运行。虽然控件在事件循环中，QTimeline将以规则的间隔更新其当前时间，并在适当时发出ValueChanged（）和FrameChanged（）。 |

**另请参阅** [state](https://doc.qt.io/qt-5/qtimeline.html#state)() and [stateChanged](https://doc.qt.io/qt-5/qtimeline.html#stateChanged)().

## 属性文档

### currentTime : int

此属性保存时间线的当前时间。

当 QTimeLine 处于 Running 状态时，此值将作为时间轴持续时间和方向的函数不断更新。否则，它是上次调用 stop ()时的当前值，或者是由 setCurrentTime ()设置的值。

默认情况下，此属性包含值0。

**访问函数:**

| 返回类型 | 函数名                         |
| -------- | ------------------------------ |
| int      | **currentTime**() const        |
| void     | **setCurrentTime**(int *msec*) |

### direction : [Direction](https://doc.qt.io/qt-5/qtimeline.html#Direction-enum)

该属性持有时间线的方向，当QTimeLine处于Running状态时。

这个方向表示时间是从0向时间线持续时间移动，还是从持续时间的值开始，在调用start()后向0移动。

默认情况下，这个属性被设置为Forward。

**访问函数:**

| 返回类型             | 函数名                                             |
| -------------------- | -------------------------------------------------- |
| QTimeLine::Direction | **direction**() const                              |
| void                 | **setDirection**(QTimeLine::Direction *direction*) |

### duration : int

这个属性持有时间线的总持续时间，单位是毫秒。

默认情况下，这个值是1000（即1秒），但你可以通过向QTimeLine的构造函数传递一个持续时间，或通过调用setDuration()来改变它。持续时间必须大于0。

注意：改变持续时间并不会导致当前时间被重置为零或新的持续时间。你还需要用所需的值调用setCurrentTime()。

**访问函数:**

| 返回类型 | 函数名                          |
| -------- | ------------------------------- |
| int      | **duration**() const            |
| void     | **setDuration**(int *duration*) |

### easingCurve : [QEasingCurve](https://doc.qt.io/qt-5/qeasingcurve.html)

指定时间线将使用的缓和曲线。如果重新实现 valueForTime () ，则忽略此值。如果设置了 easingCurve 和 curvechape，则最后一个属性集将覆盖前一个属性集。

**访问函数:**

| QEasingCurve | **easingCurve**() const                         |
| ------------ | ----------------------------------------------- |
| void         | **setEasingCurve**(const QEasingCurve &*curve*) |

**另请参阅** [valueForTime](https://doc.qt.io/qt-5/qtimeline.html#valueForTime)().

### loopCount : int

此属性保存时间线在完成之前应循环的次数。

循环数为0意味着时间线将永远循环下去。

默认情况下，此属性包含值1。

**访问函数:**

| int  | **loopCount**() const         |
| ---- | ----------------------------- |
| void | **setLoopCount**(int *count*) |

### updateInterval : int

此属性保存每次 QTimeLine 更新其当前时间之间的时间(毫秒)。

当更新当前时间时，如果当前值更改，QTimeLine 将发出 valueChanged () ，如果帧更改，则发出 frameChanged ()。

默认情况下，间隔为40毫秒，相当于每秒25次更新。

**访问函数:**

| int  | **updateInterval**() const            |
| ---- | ------------------------------------- |
| void | **setUpdateInterval**(int *interval*) |

## 成员函数文档

### QTimeLine::QTimeLine(int *duration* = 1000, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

构建一个持续时间为毫秒的时间线。 并将 `parent` 参数传递给 [QObject](https://file+.vscode-resource.vscode-webview.net/d%3A/GithubRepo/QtDocumentCN/Src/O/QObject/QObject.md) 的构造函数。默认的持续时间是1000毫秒。

### `[signal]`void QTimeLine::finished()

这个信号在QTimeLine结束时（即达到其时间线的终点）发出，并且不循环。

**注意**：这是一个私有信号。它可以在信号连接中使用，但不能由用户发射。

### `[signal]`void QTimeLine::frameChanged(int *frame*)

当处于运行状态时，QTimeLine会以固定的时间间隔发出这个信号，但只有当当前的帧发生变化时才会发出。 frame是当前的帧数。

**注意**：这是一个私有信号。它可以在信号连接中使用，但不能由用户发射。

**另请参阅** [QTimeLine::setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)() and [QTimeLine::updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop).

### `[slot]`void QTimeLine::resume()

从当前时间开始恢复时间线。QTimeLine将重新进入运行状态，一旦进入事件循环，它将定期更新其当前时间、帧和值。

与start()相反，这个函数在恢复之前不会重新启动时间线。

**另请参阅** [start](https://doc.qt.io/qt-5/qtimeline.html#start)(), [updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop)(), [frameChanged](https://doc.qt.io/qt-5/qtimeline.html#frameChanged)(), and [valueChanged](https://doc.qt.io/qt-5/qtimeline.html#valueChanged)().

### `[slot]`void QTimeLine::setPaused(bool *paused*)

如果paused为true，时间线被暂停，导致QTimeLine进入Paused状态。在start()或setPaused(false)被调用之前，不会有更新的信号。如果paused为false，时间线将被恢复，并继续进行它的工作。

**另请参阅** [state](https://doc.qt.io/qt-5/qtimeline.html#state)() and [start](https://doc.qt.io/qt-5/qtimeline.html#start)().

### `[slot]`void QTimeLine::start()

启动时间线。QTimeLine将进入运行状态，一旦进入事件循环，它将以固定的时间间隔更新其当前的时间、框架和值。默认的时间间隔是40ms（即每秒25次）。你可以通过调用setUpdateInterval()来改变更新间隔。

时间线将从位置0开始，如果向后走，则从终点开始。如果你想在不重启的情况下恢复停止的时间线，你可以调用resume()代替。

**另请参阅** [resume](https://doc.qt.io/qt-5/qtimeline.html#resume)(), [updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop)(), [frameChanged](https://doc.qt.io/qt-5/qtimeline.html#frameChanged)(), and [valueChanged](https://doc.qt.io/qt-5/qtimeline.html#valueChanged)().

### `[signal]`void QTimeLine::stateChanged([QTimeLine::State](https://doc.qt.io/qt-5/qtimeline.html#State-enum) *newState*)

每当QTimeLine的状态发生变化时，这个信号就会被发射出来。新的状态是newState。

**注意**：这是一个私有信号。它可以在信号连接中使用，但不能由用户发射。

### `[slot]`void QTimeLine::stop()

停止时间线，使QTimeLine进入NotRunning状态。

**另请参阅** [start](https://doc.qt.io/qt-5/qtimeline.html#start)().

### `[slot]`void QTimeLine::toggleDirection()

切换时间线的方向。如果方向是向前，它就变成向后，反之亦然。

**另请参阅** [setDirection](https://doc.qt.io/qt-5/qtimeline.html#direction-prop)().

### `[signal]`void QTimeLine::valueChanged([qreal](https://doc.qt.io/qt-5/qtglobal.html#qreal-typedef) *value*)

当处于运行状态时，QTimeLine会定期发射这个信号，但只有当当前值发生变化时才会发射。 值是当前值。值是0.0和1.0之间的数字。

**注意**：这是一个私有信号。它可以在信号连接中使用，但不能由用户发射。

**另请参阅** [QTimeLine::setDuration](https://doc.qt.io/qt-5/qtimeline.html#duration-prop)(), [QTimeLine::valueForTime](https://doc.qt.io/qt-5/qtimeline.html#valueForTime)(), and [QTimeLine::updateInterval](https://doc.qt.io/qt-5/qtimeline.html#updateInterval-prop).

### `[virtual]`QTimeLine::~QTimeLine()

析构QTimeLine

### int QTimeLine::currentFrame() const

返回与当前时间对应的帧。

**另请参阅** [currentTime](https://doc.qt.io/qt-5/qtimeline.html#currentTime-prop)(), [frameForTime](https://doc.qt.io/qt-5/qtimeline.html#frameForTime)(), and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### [qreal](https://doc.qt.io/qt-5/qtglobal.html#qreal-typedef) QTimeLine::currentValue() const

返回对应于当前时间的值。

**另请参阅** [valueForTime](https://doc.qt.io/qt-5/qtimeline.html#valueForTime)() and [currentFrame](https://doc.qt.io/qt-5/qtimeline.html#currentFrame)().

### int QTimeLine::endFrame() const

返回结束帧，这是对应于时间线结束的帧（即当前值为1的帧）。

**另请参阅** [setEndFrame](https://doc.qt.io/qt-5/qtimeline.html#setEndFrame)() and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### int QTimeLine::frameForTime(int *msec*) const

返回与时间毫秒对应的帧。根据valueForTime（）返回的值，使用开始帧和结束帧的线性插值计算该值。

**另请参阅** [valueForTime](https://doc.qt.io/qt-5/qtimeline.html#valueForTime)() and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### void QTimeLine::setEndFrame(int *frame*)

设置结束帧，即对应于时间线结束的帧（即当前值为1的帧）。

**另请参阅** [endFrame](https://doc.qt.io/qt-5/qtimeline.html#endFrame)(), [startFrame](https://doc.qt.io/qt-5/qtimeline.html#startFrame)(), and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### void QTimeLine::setFrameRange(int *startFrame*, int *endFrame*)

设置时间线的帧计数器，从startFrame开始，到end和endFrame为止。对于每个时间值，当你调用currentFrame()或frameForTime()时，QTimeLine将通过插值找到相应的帧，使用valueForTime()的返回值。

当处于运行状态时，当帧发生变化时，QTimeLine也会发出 frameChanged() 信号。

**另请参阅** [startFrame](https://doc.qt.io/qt-5/qtimeline.html#startFrame)(), [endFrame](https://doc.qt.io/qt-5/qtimeline.html#endFrame)(), [start](https://doc.qt.io/qt-5/qtimeline.html#start)(), and [currentFrame](https://doc.qt.io/qt-5/qtimeline.html#currentFrame)().

### void QTimeLine::setStartFrame(int *frame*)

设置起始帧，也就是对应于时间线开始的那一帧（即当前值为0的那一帧）。

**另请参阅** [startFrame](https://doc.qt.io/qt-5/qtimeline.html#startFrame)(), [endFrame](https://doc.qt.io/qt-5/qtimeline.html#endFrame)(), and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### int QTimeLine::startFrame() const

返回起始帧，也就是对应于时间线开始的那一帧（即当前值为0的那一帧）。

**另请参阅** [setStartFrame](https://doc.qt.io/qt-5/qtimeline.html#setStartFrame)() and [setFrameRange](https://doc.qt.io/qt-5/qtimeline.html#setFrameRange)().

### [QTimeLine::State](https://doc.qt.io/qt-5/qtimeline.html#State-enum) QTimeLine::state() const

返回时间线的状态。

**另请参阅** [start](https://doc.qt.io/qt-5/qtimeline.html#start)(), [setPaused](https://doc.qt.io/qt-5/qtimeline.html#setPaused)(), and [stop](https://doc.qt.io/qt-5/qtimeline.html#stop)().

### `[override virtual protected]`void QTimeLine::timerEvent([QTimerEvent](https://doc.qt.io/qt-5/qtimerevent.html) **event*)

重写函数: [QObject::timerEvent](https://doc.qt.io/qt-5/qobject.html#timerEvent)(QTimerEvent *event).

### `[virtual]`[qreal](https://doc.qt.io/qt-5/qtglobal.html#qreal-typedef) QTimeLine::valueForTime(int *msec*) const

返回时间*毫秒*的时间线值。根据曲线形状的不同，返回的值始终在0和1之间。如果*msec*为0，则默认实现始终返回0。重新实现此功能，为时间线提供自定义曲线形状。

**另请参阅** [CurveShape](https://doc.qt.io/qt-5/qtimeline-obsolete.html#CurveShape-enum) and [frameForTime](https://doc.qt.io/qt-5/qtimeline.html#frameForTime)().