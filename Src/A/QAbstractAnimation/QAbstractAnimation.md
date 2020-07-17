[TOC]
# **QAbstractAnimation 类**
------
## **QAbstractAnimation 是所有的动画相关的基类**
QAbstractAnimation 定义了所有动画类相关的基础功能，通过继承该类，你可以实现动画的其它功能，或者添加自定义的特效。

| 属性| 方法|
| ------: |:------|
| Header: | `#include<QAbstractAnimation>` |
| qmake: | QT+=core|
| Since: | Qt 4.6 |
|Inherits:|QObject|
|Inherited By|QAnimationGroup，QPauseAnimation，QVariantAnimation|


----------
## **简述**

### **公共类型**

| 属性| 方法|
| :------: |:------|
|enum |    DeletionPolicy { KeepWhenStopped, DeleteWhenStopped }|
|enum |    Direction { Forward, Backward }|
|enum |    State { Stopped, Paused, Running }|


----------


### **属性**
| 属性|
| :------ |
|currentLoop : const int|
|currentTime : int|
|direction : Direction|
|duration : const int|
|loopCount : int|
|state : const State|


----------


### **public函数**
| 属性| 函数名|
| ------: |:------|
|| QAbstractAnimation(QObject * parent = Q_NULLPTR)|
|virtual |    ~QAbstractAnimation() |
|int |    currentLoop() const|
|int |    currentLoopTime() const|
|int |    currentTime() const|
|Direction |    direction() const|
|virtual int |    duration() const = 0|
|QAnimationGroup *|    group() const|
|int |    loopCount() const|
|void |    setDirection(Direction direction)|
|void |    setLoopCount(int loopCount)|
|State |    state() const|
|int |    totalDuration() const|


----------


### **公有槽**
| 属性| 函数名|
| :------: |:------|
|void |    pause()|
|void |    resume()|
|void |    setCurrentTime(int msecs)|
|void |    setPaused(bool paused)|
|void |    start(QAbstractAnimation::DeletionPolicy policy = KeepWhenStopped)|
|void |    stop()|


----------


### **公有信号**
| 属性| 函数名|
| :------: |:------|
|void |    currentLoopChanged(int currentLoop)|
|void |    directionChanged(QAbstractAnimation::Direction newDirection)|
|void |    finished()|
|void |    stateChanged(QAbstractAnimation::State newState, QAbstractAnimation::State oldState)|


----------

### **protect函数**
| 属性| 函数名|
| :------: |:------|
|virtual void |    updateCurrentTime(int currentTime) = 0|
|virtual void |    updateDirection(QAbstractAnimation::Direction direction)|
|virtual void |    updateState(QAbstractAnimation::State newState, QAbstractAnimation::State oldState)|


----------
### **可以重写的protect函数**
| 属性| 函数名|
| :------: |:------|
|virtual bool |    event(QEvent *event)|


----------


## **详细说明**
QAbstractAnimation类是所有动画的基础
该类是所有动画类的基类。通过继承这个类，你可以创建自定义的动画。
动画的进度的当前时间由函数currentLoopTime()控制，动画从0毫秒开始到其最后的持续时间(duration())。该值在动画运行时会自动更新。也可以由函数setCurrentTime()来进行设置。
在任何时候，动画的状态都只有三种：Running, Stopped,Paused(枚举变量enum State)，可以通过函数start(),stop(),pause(),或者resume()来改变当前动画的状态。QAbstractAnimation在状态改变时将会发出信号stateChanged()。
通过设置loopCount属性，动画可以循环任意次数。当动画的时间到达duration()函数的返回值时，它将重置当前时间并继续运行。当duration为-1，将无限循环下去。当当前时间等于duration()时，并且处理最后一次循环时，动画将进入Stopped()状态，并发送finished()信号。
QAbstractAnimation为子类提供了纯虚函数来跟踪动画的进度:duration()和updateCurrentTime()。duration()函数提供动画的持续时间。(这特么不就是函数名字么？)。当动画时间变化时，QAbstractAnimation会调用updateCurrentTime()函数。通过重新实现该函数，你可以自己追踪动画的进度。不要在动画间隔之间来调用此功能，虽然此函数一分钟刷新60次。
通过重新实现updateState()函数，你可以自己追踪动画状态的改变，这对于不受时间驱动的动画特别有用
另见 QVariantAnimation ， QPropertyAnimation ， QAnimationGroup，The Animation Framework.

----------

## **成员变量文档**

----------


**enum QAbstractAnimation::DeletionPolicy**
| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::KeepWhenStopped|    0|动画停止时将不会删除|
|QAbstractAnimation::DeleteWhenStopped|    1| 动画停止时自动删除|


----------
**enum QAbstractAnimation::Direction**
该枚举描述了动画在运行时的方向
| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::KeepWhenStopped|    0|动画停止时将不会删除|
|QAbstractAnimation::DeleteWhenStopped|    1| 动画停止时自动删除|


----------
**enum QAbstractAnimation::State**
该枚举描述了动画的状态
| 函数| 值| 描述|
| :------: |:------:|:------|
|QAbstractAnimation::Stopped|    0|    动画未运行。这是QAbstractAnimation的初始状态，通过调用setCurrentTime()函数或者start()来启动动画。|
|QAbstractAnimation::Paused|    1|动画暂时，通过调用resume()函数恢复动画。|
|QAbstractAnimation::Running|    2|动画运行中。当控件处于事件循环时，QAbstractAnimation将更新时间，并会一直调用updateCurrentTime()。|


----------
## **文档属性**


**currentLoop : const int**

此属性为该动画当前的循环数
此属性描述了动画当前的循环数。默认的循环次数为1，所以当前的循环次数永远为0。如果循环总数为2的话，动画运行超过其duration或者重新开始，或者重置时间等等，总数则会减一。
当当前循环变化时，QAbstractAnimation会发出currentLoopChanged()信号

**调用函数**
| 属性| 函数名|
| :------: |:------|
|int |    currentLoop() const|

**通知信号**
| 属性| 函数名|
| :------: |:------|
|void |    currentLoopChanged(int currentLoop)|


----------

**currentTime : int**

此属性描述了动画当前的时间与进度
此属性描述了动画当前的时间，你可以通过调用函数setCurrentTime()来改变当前的时间。也可以通过调用start()函数让动画自己运行，随着动画的运行时间也会自己变化。
动画时间从0开始，以tatalDuration()函数结束。

**调用函数**
| 属性| 函数名|
| :------: |:------|
|int |    currentTime() const|
|void |    setCurrentTime(int msecs)|

**另参见函数loopCount()与currentLoopTime()**


----------

**direction : Direction**

该属性为动画运行时的方向
简单的说就是正常播放的方向，还是倒放的方向(官方文档也有点啰嗦了)
默认方向为Forward

**调用函数**
| 属性| 函数名|
| :------: |:------|
|Direction |    direction() const|
|void |    setDirection(Direction direction)|

**通知信号**
| 属性| 函数名|
| :------: |:------|
|void |    directionChanged(QAbstractAnimation::Direction newDirection)|


----------

**duration : const int**

该属性描述了动画已经播放的时间
如果duration为-1，则表示duration未定义，而且动画将会忽略loopCount属性。
**调用函数**
| 属性| 函数名|
| :------: |:------|
|virtual int |    duration() const = 0|


----------
**loopCount : int**

该属性保存了动画的循环次数
默认下，该值为1，表示该动画只播放一次。通过改变其值，动画也会改变循环的次数。当该值为-1时，动画将会永远循环。如果动画没有duration属性，loopCount则无效。默认值为1。
**调用函数**
| 属性| 函数名|
| :------: |:------|
|int |loopCount() const|
|void |    setLoopCount(int loopCount)|


----------
**state : const State**

动画状态
此功能描述了动画的当前状态。当动画状态改变时，QAbstractAnimation发出stateChanged()信号。

**调用函数**
| 属性| 函数名|
| :------: |:------|
|State |    state() const|

**通知信号**
| 属性| 函数名|
| :------: |:------|
|void |    stateChanged(QAbstractAnimation::State newState, QAbstractAnimation::State oldState)|


---------

## **成员函数**

----------


**QAbstractAnimation::QAbstractAnimation(QObject *parent = Q_NULLPTR)**

构造QAbstractAnimation的基类，并将parent参数传递给QObject的构造函数。
**另见QVariantAnimation， QAnimationGroup**


----------


**QAbstractAnimation::~QAbstractAnimation() [virtual]**

析构函数，当QAbstractAnimation运行结束后会自动销毁。如果QAbstractAnimation是QAnimationGroup的一部分，它会在破坏之前自动删除。

----------

**void QAbstractAnimation::currentLoopChanged(int currentLoop) [signal]**

当当前循环发生变化时，QAbstractAnimation会发出该信号。currentLoop()为当前循环
**注意:属性currentLoop()的通知信号**
**另见currentLoop()和loopCount()**

----------

**int QAbstractAnimation::currentLoopTime() const**

返回当前循环的当前时间。它的区间范围为[0 - duration()]
**另见 duration()和currentTime()

----------

**void QAbstractAnimation::directionChanged(QAbstractAnimation::Direction newDirection) [signal]**

每当方向改变时，QAbstractAnimation会发送此信号。newDirection为新的方向。
**注意：属性direction的通知信号**
**另见direction()**

----------
**int QAbstractAnimation::duration() const [pure virtual]**

这个纯虚函数返回QAbstractAnimation的持续时间，并定义QAbstractAnimation多久时间更新一次当前时间。duration是本地的，并且不包括循环总数。
当其值为-1时表示动画没有定义持续时间；动画将永远运行下去直到主动停止它。这对于非时间驱动的动画或者无法预测其持续时间的动画(例如游戏中自动播放的音乐背景)十分有用。
如果QAnimationGroup中的QAbstractAnimation是并行的，duration则是所有动画中最长的。如果
QAnimationGroup是线性顺序的，其duration是所有动画的总和。
**注意：QAbstractAnimation获得duration的函数**
**另见：loopCount()**

----------
**bool QAbstractAnimation::event（QEvent* event)  [virtual protected]**
QObject::event()的重新实现

----------
**void QAbstractAnimation::finished() [signal]**

QAbstractAnimation在动画停止之后发送此信号，并且表示已经结束
该信号在stateChanged()之后发送
**另见stateChanged()**

----------


**QAnimationGroup *QAbstractAnimation::group() const**
如果QAbstractAnimation是QAnimationGroup的一部分，则会返回QAnimationGroup的指针；否则返回NULL
**另见QAnimationGroup::addAnimation()**

----------

**void QAbstractAnimation::pause() [slot]**
暂停动画。当动画暂停时，state()将返回Paused。在调用函数resume()或者start()前，currentTime()的值将会保持不变。如果想从当前时间继续，则需要调用resume()函数。
** 另见start()，state(),resume()**

----------

**void QAbstractAnimation::resume()  [slot]**
暂停后恢复动画。当动画恢复时，QAbstractAnimation会发出resume()信号和stateChanged()信号。当前时间将不会变化。
**另见start(),pause(),state()**

----------
**void QAbstractAnimation::setPaused(bool paused)  [slot]**

如果paused为true，动画暂停。如果pause为false,动画恢复。
**另见 state(),pause(),resume().**

----------
**void QAbstractAnimation::start(QAbstractAnimation::DeletionPolicy policy = KeepWhenStopped)  [slot]**

开始动画。policy参数表示在动画结束后是否删除。动画启动时，会发出stateChanged()信号，state()会返回Running。当控件在到达event loop时，动画会自动播放，并在动画播放时会定期调用updateCurrentTime().
如果动画当前已经停止或者已经结束，调用该函数将会回滚动画并从头开始。当动画到达终点时，动画将会停止。或者当其循环次数大于1时也会从头开始。
如果动画正在运行时，调用该函数不会有任何变化。
**另见函数stop(),state()**

----------
**void QAbstractAnimation::stateChanged(QAbstractAnimation::State newState, QAbstractAnimation::State oldState)  [signal]**

每当动画的状态从oldState变为newState时，QAbstractAnimation会发出此信号。在调用virtual updateState()函数时也会发送此信号。
**注意：这是动画状态的通知信号**
**另见updateState()**

----------
**void QAbstractAnimation::stop() [slot]**

停止动画。当动画停止时，会发出stateChanged()信号，state()返回Stopped。当前时间不会变化。
如果动画到达终点后自己结束（比如currentLoopTime() == duration() 或者currentLoop() > loopCount() - 1）,则会发送finished()信号。
**另见start()和state()。

----------
**int QAbstractAnimation::totalDuration() const**

返货动画总和的有效持续时间（当然不只是一次的，肯定是loopCount()的总次数）
**另参见duration()和currentTime()**

----------
**void QAbstractAnimation::updateCurrentTime(int currentTime) [pure virtual protected]**
每次动画的currentTime发生变化时，就会调用这个纯虚函数。一般QAbstractAnimation的子类会重新实现这个函数，或者你自己实现
**另见 updateState()**

----------
**void QAbstractAnimation::updateDirection(QAbstractAnimation::Direction direction) [virtual protected]**

当动画的播放方向改变时，QAbstractAnimation会调用该虚函数。参数direction表示新的方向。
**另见setDirection(),direction()**

----------
**void QAbstractAnimation::updateState(QAbstractAnimation::State newState, QAbstractAnimation::State oldState)**

当动画的状态改变时，此函数会自动调用。
**另见start(),stop(),pause(),resume()

----------


