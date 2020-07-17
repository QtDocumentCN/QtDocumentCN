[TOC]
# QAbstractAnimation 类
QAbstractAnimation 是所有的动画相关的基类。

QAbstractAnimation 定义了所有动画类相关的基础功能，通过继承该类，您可以实现动画的其它功能，或者添加自定义的特效。

| 属性| 方法|
| ------: |:------|
| 头文件 | `#include<QAbstractAnimation>` |
| qmake | `QT+=core` |
| 自从 | Qt 4.6 |
|继承|[QObject](../../O/QObject/QObject.md)|
|派生|[QAnimationGroup](../QAnimationGroup/QAnimationGroup.md)，[QPauseAnimation](../../P/QPauseAnimation/QPauseAnimation.md)，[QVariantAnimation](../../V/QVariantAnimation/QVariantAnimation.md)|



## 公共成员类型

| 类型| 方法|
| :------: |:------|
|enum | [DeletionPolicy](#enum-qabstractanimationdeletionpolicy) { KeepWhenStopped, DeleteWhenStopped } |
|enum | [Direction](#enum-qabstractanimationdirection) { Forward, Backward } |
|enum | [State](#enum-qabstractanimationstate) { Stopped, Paused, Running } |



## 属性

| 属性| 类型 | 属性 | 类型 |
| :------ | ------- | ------- | ------- |
|[currentLoop](#currentloop--const-int)|const int|[duration](#duration--const-int)|const int|
|[currentTime](#currenttime--int)|int|[loopCount](#loopcount--int)|int|
|[direction](#direction--direction)|Direction|[state](#state--const-state)|const State|



## 公共成员函数

| 返回类型 | 函数名|
| ------: |:------|
|| [QAbstractAnimation](#qabstractanimationqabstractanimationqobject-parent--qnullptr)(QObject \**parent* = Q_NULLPTR) |
|virtual | ~[QAbstractAnimation](#virtual-qabstractanimationqabstractanimation)() |
|int | [currentLoop](#currentloop--const-int)() const |
|int | [currentLoopTime](#int-qabstractanimationcurrentlooptime-const)() const |
|int | [currentTime](#currenttime--int)() const |
|Direction | [direction](#direction--direction)() const |
|virtual int | [duration](#pure-virtual-int-qabstractanimationduration-const)() const = 0 |
|QAnimationGroup *| [group](#qanimationgroup-qabstractanimationgroup-const)() const |
|int | [loopCount](#loopcount--int)() const |
|void | [setDirection](#direction--direction)(Direction *direction*) |
|void | [setLoopCount](#loopcount--int)(int *loopCount*) |
|State | [state](#state--const-state)() const |
|int | [totalDuration](#int-qabstractanimationtotalduration-const)() const |




## 公共槽
| 返回类型 | 函数名|
| :------: |:------|
|void | [pause](#slot-void-qabstractanimationpause)() |
|void | [resume](#slot-void-qabstractanimationresume)() |
|void | [setCurrentTime](#currenttime--int)(int *msecs*) |
|void | [setPaused](#slot-void-qabstractanimationsetpausedbool-paused)(bool *paused*) |
|void | [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)(QAbstractAnimation::DeletionPolicy *policy* = KeepWhenStopped) |
|void | [stop](#slot-void-qabstractanimationstop)() |




## 信号
| 返回类型 | 函数名|
| :------: |:------|
|void | [currentLoopChanged](#signal-void-qabstractanimationcurrentloopchangedint-currentloop)(int *currentLoop*) |
|void | [directionChanged](#signal-void-qabstractanimationdirectionchangedqabstractanimationdirection-newdirection)(QAbstractAnimation::Direction *newDirection*) |
|void | [finished](#signal-void-qabstractanimationfinished)() |
|void | [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)(QAbstractAnimation::State *newState*, QAbstractAnimation::State *oldState*) |



## 保护成员函数

| 返回类型 | 函数名|
| :------: |:------|
|virtual void | [updateCurrentTime](#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)(int *currentTime*) = 0 |
|virtual void | [updateDirection](#virtual-protected-void-qabstractanimationupdatedirectionqabstractanimationdirectionenum-qabstractanimationdirection-direction)(QAbstractAnimation::Direction *direction*) |
|virtual void | [updateState](#virtual-protected-void-qabstractanimationupdatestateqabstractanimationstateenum-qabstractanimationstate-newstate-qabstractanimationstateenum-qabstractanimationstate-oldstate)(QAbstractAnimation::State *newState*, QAbstractAnimation::State *oldState*) |



## 重写保护成员函数

| 返回类型 | 函数名|
| :------: |:------|
|virtual bool | [event](#virtual-protected-bool-qabstractanimationeventqevent-event)(QEvent \**event*) |




## 详细介绍
QAbstractAnimation 定义了所有动画共享的功能。通过继承这个类，您可以创建自定义的动画，并将其插入到动画框架中。

动画的进度的当前时间由当前时间([currentLoopTime](int-qabstractanimationcurrentlooptime-const)())控制，数值从0毫秒开始到其最后的持续时间([duration](#pure-virtual-int-qabstractanimationduration-const)())。该值在动画运行时会自动更新，也可以直接由 [setCurrentTime]()() 来设置。

在任何时候，动画的状态都只有三种：[Running](#enum-qabstractanimationstate)、[Stopped](#enum-qabstractanimationstate) 或 [Paused](#enum-qabstractanimationstate)——由枚举变量 [State](#enum-qabstractanimationstate)定义。可以通过函数 [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)()、[stop](#slot-void-qabstractanimationstop)() 、[pause](#slot-void-qabstractanimationpause)() 或 [resume](#slot-void-qabstractanimationresume)() 来改变当前动画的状态。动画开始时总会充值它的[当前时间]()。若被暂停，则继续播放后会从相同的“当前时间”继续。若动画停止，则无法继续，但会保留“当前时间”（直到再次开始）。QAbstractAnimation 在状态改变时将会发出信号 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)()。

通过设置 [loopCount](#loopcount--int) 属性，动画可以循环任意次数。当动画的时间到达 [duration](#pure-virtual-int-qabstractanimationduration-const)() 时，它将重置当前时间并继续运行。循环数为1（默认值）意味着动画只会播放一次。注意，若 `duration` 为-1，动画将无限播放，直到主动停止；当前时间会无限增长。当当前时间等于 [duration](#pure-virtual-int-qabstractanimationduration-const)() ，并且正在处理最后一次循环时，动画将进入 [Stopped](#enum-qabstractanimationstate) 状态，并发送 [finished]()() 信号。

QAbstractAnimation 为子类提供了纯虚函数来跟踪动画的进度：[duration](#pure-virtual-int-qabstractanimationduration-const)() 和 [updateCurrentTime](#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)()。[duration](#pure-virtual-int-qabstractanimationduration-const)() 函数用于提供动画的持续时间（如上文所述）。当动画时间变化时，动画框架会调用 [updateCurrentTime](#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)()。通过重新实现该函数，您可以追踪动画进度。注意：此函数的调用间隔和调用次数均未定义，虽然通常每秒会更新60次。

通过重新实现 [updateState](#virtual-protected-void-qabstractanimationupdatestateqabstractanimationstateenum-qabstractanimationstate-newstate-qabstractanimationstateenum-qabstractanimationstate-oldstate)()，您可以追踪动画状态的改变，这对于不受时间驱动的动画特别有用。

**另请参阅：**[QVariantAnimation](../../V/QVariantAnimation/QVariantAnimation.md)，[QPropertyAnimation](../../P/QPropertyAnimation/QPropertyAnimation.md)，[QAnimationGroup](../QAnimationGroup/QAnimationGroup.md) 和 [The Animation Framework](../The_Animation_Framework/The_Animation_Framework.md)。



## 成员变量文档

### enum QAbstractAnimation::DeletionPolicy

| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::KeepWhenStopped|    0|动画停止时不会被删除|
|QAbstractAnimation::DeleteWhenStopped|    1| 动画停止时会被自动删除 |


----------
### enum QAbstractAnimation::Direction

该枚举描述了动画在 [Running](#enum-qabstractanimationstate) 状态时的运行的方向。

| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::Forward|    0|“当前时间”随时间递增（即从0向终点/duration 移动）|
|QAbstractAnimation::Backward|    1| ”当前时间“随时间递减（即从终点/duration 向0移动） |


----------
### enum QAbstractAnimation::State

该枚举描述了动画的状态。

| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::Stopped|    0| 动画未运行。这是 [QAbstractAnimation](QAbstractAnimation.md) 的初始状态，也是 [[QAbstractAnimation]](QAbstractAnimation.md) 结束后的状态。除非 [setCurrentTime]()() 被调用，或者调用 [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)() 来启动动画，否则”当前时间“不会改变。 |
|QAbstractAnimation::Paused|    1|动画暂停（即使暂时挂起）。调用 [resume](#slot-void-qabstractanimationresume)() 将恢复动画。|
|QAbstractAnimation::Running|    2|动画运行中。当控制权处于事件循环中时，[QAbstractAnimation](QAbstractAnimation.md) 将会有规律地更新”当前时间“，并在适合地时机调用 [updateCurrentTime](#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)()。|



## 属性文档

### currentLoop : const int

此属性存储动画当前的循环数。

此属性描述了动画当前的循环数。默认的循环次数为1，所以当前的循环次数永远为0。若循环总数2的，当动画运行超过其 duration 时将重新开始，并将当前时间重置为0，当前循环数置为1，以此类推。

当当前循环变化时，[QAbstractAnimation](QAbstractAnimation.md) 会发出 [currentLoopChanged](#signal-void-qabstractanimationcurrentloopchangedint-currentloop)() 信号。

**存取函数**

| 返回类型 | 函数名                  |
| :------: | :---------------------- |
|   int    | **currentLoop**() const |

**通知信号**

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|   void   | [currentLoopChanged](#signal-void-qabstractanimationcurrentloopchangedint-currentloop)(int *currentLoop*) |


----------

### currentTime : int

此属性存储动画当前的时间与进度。

此属性描述了动画当前的时间。您可以通过 `setCurrentTime` 函数来修改当前时间，也可以调用 [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)() 让动画运行，当前时间会随动画播放进度自动设置。

动画的当前时间从0开始，在 [totalDuration](#int-qabstractanimationtotalduration-const)() 结束。

**存取函数**

| 返回类型 | 函数名                        |
| :------: | :---------------------------- |
|   int    | **currentTime**() const       |
|   void   | **setCurrentTime**(int msecs) |

 **另请参阅：**[loopCount](#loopcount--int) 和 [currentLoopTime](int-qabstractanimationcurrentlooptime-const)()。


----------

### direction : Direction

该属性存储动画在 [Running](#enum-qabstractanimationstate) 状态时的运行方向。

该方向表明了在 [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)() 被调用后，时间是从0向动画时长移动，还是从持续时间向0移动。

默认方向为 [Forward](#enum-qabstractanimationdirection)。

**存取函数**

| 返回类型 | 函数名|
| :------: |:------|
|Direction | **direction**() const |
|void | **setDirection**(Direction *direction*) |

**通知信号**

| 返回类型 | 函数名|
| :------: |:------|
|void | [directionChanged](#signal-void-qabstractanimationdirectionchangedqabstractanimationdirection-newdirection)(QAbstractAnimation::Direction *newDirection*) |


----------

### duration : const int

该属性存储动画的持续时间。

如果 `duration` 为-1，则表示 `duration` 未定义，此时动画将会忽略 `loopCount` 属性。

**存取函数**

| 属性| 函数名|
| :------: |:------|
|virtual int | [duration](#pure-virtual-int-qabstractanimationduration-const)() const = 0 |


----------
### loopCount : int

该属性存储动画的循环次数。

此属性用整形描述了动画的循环次数。默认值为1，表示该动画只播放一次，然后停止。通过修改其值，动画会改变循环的次数。当值为0时，动画完全不会运行；当值为-1时，动画将会永远循环直到主动停止。如果动画未设置 `duration` 属性则无法循环，即只会播放一次。
**存取函数**

| 属性| 函数名|
| :------: |:------|
|int |**loopCount**() const|
|void | **setLoopCount**(int *loopCount*) |


----------
### state : const State

动画状态。
此属性描述了动画的当前状态。当动画状态改变时，[QAbstractAnimation](QAbstractAnimation.md) 会发射 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)() 信号。

**存取函数**

| 属性| 函数名|
| :------: |:------|
|State | **state**() const |

**通知信号**

| 属性| 函数名|
| :------: |:------|
|void | [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)(QAbstractAnimation::State *newState*, QAbstractAnimation::State *oldState*) |



## 成员函数文档

### QAbstractAnimation::**QAbstractAnimation**([QObject](../../O/QObject/QObject.md) *\*parent* = Q_NULLPTR)

构造 QAbstractAnimation 基类，并将 `parent` 参数传递给 [QObject](../../O/QObject/QObject.md) 的构造函数。

**另请参阅：**[QVariantAnimation](../../V/QVariantAnimation/QVariantAnimation.md) 和 [QAnimationGroup](../QAnimationGroup/QAnimationGroup.md)

----------

###  **[signal]** void QAbstractAnimation::**currentLoopChanged**(int *currentLoop*)

每当当前循环发生变化时，[QAbstractAnimation](QAbstractAnimation.md) 会发射该信号。`currentLoop` 为当前循环。

**注意：**属性 `currentLoop` 的通知信号。

**另请参阅：**[currentLoop](#currentloop--const-int)() 和 [loopCount](#loopcount--int)()。

----

### **[signal]** void QAbstractAnimation::**directionChanged**([QAbstractAnimation::Direction](#enum-qabstractanimationdirection) *newDirection*)

每当方向改变时，[QAbstractAnimation](QAbstractAnimation.md) 会发射该信号。`newDirection` 为新方向。

**注意：**属性 `direction` 的通知信号。

**另请参阅：**[direction](#direction--direction)()。

----

### **[signal]** void QAbstractAnimation::**finished**()

 在动画停止并到达终点之后发送此信号。

该信号在 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)() 之后发射。

**另请参阅：**[stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)()。

----

### **[slot]** void QAbstractAnimation::**pause**()
暂停动画。当动画暂停时，[state](#state--const-state)() 返回 [Paused](#enum-qabstractanimationstate)。在调用 [resume](#slot-void-qabstractanimationresume)() 或 [start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)() 前，[currentTime](#currenttime--int)() 的值将会保持不变。若想从当前时间继续，则调用 [resume](#slot-void-qabstractanimationresume)()函数。

**另请参阅：**[start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)()，[state](#state--const-state)() 和 [resume](#slot-void-qabstractanimationresume)()。

----

### **[slot]** void QAbstractAnimation::**resume**()
暂停后恢复动画。当动画恢复时，会发射会发出 resumed() 信号和 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)() 信号。当前时间不会变化。

**另请参阅：**[start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)，[pause](#slot-void-qabstractanimationpause)() 和 [state](#state--const-state)()。

----

### **[slot]** void QAbstractAnimation::**setPaused**(bool *paused*)

若 `paused` 为 `true`，则暂停动画。若 `pause` 为 `false`，则恢复动画播放。

**另请参阅：**[state](#state--const-state)()，[pause](#slot-void-qabstractanimationpause)() 和 [resume](#slot-void-qabstractanimationresume)()。

----

### **[slot]** void QAbstractAnimation::**start**([QAbstractAnimation::DeletionPolicy](#enum-qabstractanimationdeletionpolicy) *policy* = KeepWhenStopped)

开始动画。`policy` 参数表示动画在结束后是否会被删除。动画启动时，会发射 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)() 信号，[state](#state--const-state)() 会返回 `Running`。当控制权回到事件循环时，动画会自动播放，并随播放进度周期性调用 [updateCurrentTime](#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)()，

若动画当前已被停止或者已经结束，调用 `start()` 将会充值动画并从头开始。当动画到达终点时，动画将会停止；或者当其循环次数大于1，则会从头开始。

若动画已经在运行中，此函数不会有任何操作。

**另请参阅：**[stop](#slot-void-qabstractanimationstop)() 和 [state](#state--const-state)()。

----

### **[signal]** void QAbstractAnimation::**stateChanged**([QAbstractAnimation::State](#enum-qabstractanimationstate) *newState*, [QAbstractAnimation::State](#enum-qabstractanimationstate) *oldState*)

每当动画的状态从 `oldState` 变为 `newState` 时，[QAbstractAnimation](QAbstractAnimation.md) 会发射此信号。此信号会在虚函数 [updateState](#virtual-protected-void-qabstractanimationupdatestateqabstractanimationstateenum-qabstractanimationstate-newstate-qabstractanimationstateenum-qabstractanimationstate-oldstate)()被调用后发射。

**注意：**属性 [state](#state--const-state) 的通知信号。

**另请参阅：**[updateState](#virtual-protected-void-qabstractanimationupdatestateqabstractanimationstateenum-qabstractanimationstate-newstate-qabstractanimationstateenum-qabstractanimationstate-oldstate)()。

----

### **[slot]** void QAbstractAnimation::**stop**()

停止动画。当动画停止时，会发射 [stateChanged](#signal-void-qabstractanimationstatechangedqabstractanimationstate-newstate-qabstractanimationstate-oldstate)() 信号，[state](#state--const-state)() 返回 `Stopped`。当前时间不会变化。

若动画到达终点后自动结束（比如 [currentLoopTime](int-qabstractanimationcurrentlooptime-const)() == [duration](#pure-virtual-int-qabstractanimationduration-const)()  或者 [currentLoop](#currentloop--const-int)() > [loopCount](#loopcount--int)() - 1）,则会发射 [finished](#signal-void-qabstractanimationfinished)() 信号。

**另请参阅：**[start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)() 和 [state](#state--const-state)()。

----

### **[virtual]** QAbstractAnimation::**~QAbstractAnimation**()

若在运行中则停止动画，然后销毁 [QAbstractAnimation](QAbstractAnimation.md)。若当前动画是 [QAnimationGroup](../QAbstractAnimation/QAnimationGroup.md) 的一部分，则会在销毁前被自动移除。

----------

### int QAbstractAnimation::**currentLoopTime**() const

返回当前循环中的当前时间。它的范围为0到 [duration](#pure-virtual-int-qabstractanimationduration-const)()。

**另请参阅：** [duration](#pure-virtual-int-qabstractanimationduration-const)() 和 [currentTime](#currenttime--int)()。

----------
### **[pure virtual]** int QAbstractAnimation::**duration**() const

此纯虚函数返回动画持续时间，并定义 [QAbstractAnimation](QAbstractAnimation.md) 应该多久更新一次当前时间。持续时间是本地的，并且不包括循环总数。

返回值-1表示动画没有定义持续时间，动画将永远运行下去，直到被主动停止。这对于非时间驱动的动画或者无法预测其持续时间的动画（例如游戏中事件驱动的音频回放）十分有用。

若该动画是并行的 [QAbstractAnimation](../QAbstractAnimation/QAbstractAnimation.md) 是并行的，则持续时间是所有动画中最长的。若此动画是顺序的 [QAnimationGroup](../QAnimationGroup/QAnimationGroup.md)，则持续时间是所有动画的总和。

**注意：**`duration` 属性的获取函数。

**另请参阅：**[loopCount](#loopcount--int)()。

----------
### **[virtual protected]** bool QAbstractAnimation::**event**([QEvent](../../E/QEvent/QEvent.md) \**event*)
[QObject::event](../../O/QObject/QObject.md#event)(QEvent *e) 的重新实现。

----------

### [QAnimationGroup](../QAnimationGroup/QAnimationGroup.md) \*QAbstractAnimation::**group**() const
若此动画是 [QAnimationGroup](../QAnimationGroup/QAnimationGroup.md) 的一部分，则会返回该动画组的指针，否则返回`nullptr`。

**另请参阅：**[QAnimationGroup::addAnimation](../QAnimationGroup/QAnimationGroup.md#addAnimation)()。

----------
### int QAbstractAnimation::**totalDuration**() const

返回动画的有效持续时间的综合，包含循环次数。
**另请参阅：**[duration](#pure-virtual-int-qabstractanimationduration-const)() 和 [currentTime](#currenttime--int)()。

----------
### **[pure virtual protected]** void QAbstractAnimation::**updateCurrentTime**(int *currentTime*)

此虚函数会当动画的 `currentTime` 每次发生变化时被调用。

**另请参阅：**[updateState](#virtual-protected-void-qabstractanimationupdatestateqabstractanimationstateenum-qabstractanimationstate-newstate-qabstractanimationstateenum-qabstractanimationstate-oldstate)()。

----------
### **[virtual protected]** void QAbstractAnimation::**updateDirection**([QAbstractAnimation::Direction](#enum-qabstractanimationdirection) *direction*)

此虚函数会在 [QAbstractAnimation](QAbstractAnimation.md) 的播放方向改变时被调用。参数 `direction` 表示新的方向。

**另请参阅：**[setDirection]()()，[direction](#direction--direction)()。

----------
### **[virtual protected]** void QAbstractAnimation::**updateState**([QAbstractAnimation::State](#enum-qabstractanimationstate) *newState*, [QAbstractAnimation::State](#enum-qabstractanimationstate) *oldState*)

此虚函数会在动画的状态改变从 `oldState` 切换为 `newState` 时被调用。

**另请参阅：**[start](#slot-void-qabstractanimationstartqabstractanimationdeletionpolicy-policy--keepwhenstopped)()，[stop](#slot-void-qabstractanimationstop)()，[pause](#slot-void-qabstractanimationpause)() 和 [resume](#slot-void-qabstractanimationresume)()。