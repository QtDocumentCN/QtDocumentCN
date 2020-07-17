这里是文档翻译的模板，详情请见[贡献指南](https://github.com/QtDocumentCN/QtDocumentCN/blob/master/CONTRIBUTING.md)。

文档翻译的名词对照表可见[对照表](Comparison_Table.md)。

翻译文档结构为三层目录结构。

```markdown
# 类名
	## 公共成员类型
	## 公有成员函数
	## 成员类型文档
		### 类型1
		### 类型2
	## 成员函数文档
		### 函数1
		### 函数2
```



# 类名

这里填一些简述。

|   属性 | 方法                                                         |
| -----: | :----------------------------------------------------------- |
| 头文件 | `#include<QAbstractAnimation>`                               |
|  qmake | `QT+=core`                                                   |
|   自从 | Qt 4.6                                                       |
|   继承 | [QObject](O/QObject/QObject.md)                              |
|   派生 | [QAnimationGroup](A/QAnimationGroup/QAnimationGroup.md)，[QPauseAnimation](P/QPauseAnimation/QPauseAnimation.md)，[QVariantAnimation](V/QVariantAnimation/QVariantAnimation.md) |



## 公共成员类型

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| enum | [DeletionPolicy](A/QAbstractAnimation/QAbstractAnimation.md#enum-qabstractanimationdeletionpolicy) { KeepWhenStopped, DeleteWhenStopped } |
| enum | [Direction](A/QAbstractAnimation/QAbstractAnimation.md#enum-qabstractanimationdirection) { Forward, Backward } |
| enum | [State](A/QAbstractAnimation/QAbstractAnimation.md#enum-qabstractanimationstate) { Stopped, Paused, Running } |



## 属性

| 属性                                                         | 类型      | 属性                                                         | 类型        |
| :----------------------------------------------------------- | --------- | ------------------------------------------------------------ | ----------- |
| [currentLoop](A/QAbstractAnimation/QAbstractAnimation.md#currentloop--const-int) | const int | [duration](A/QAbstractAnimation/QAbstractAnimation.md#duration--const-int) | const int   |
| [currentTime](A/QAbstractAnimation/QAbstractAnimation.md#currenttime--int) | int       | [loopCount](A/QAbstractAnimation/QAbstractAnimation.md#loopcount--int) | int         |
| [direction](A/QAbstractAnimation/QAbstractAnimation.md#direction--direction) | Direction | [state](A/QAbstractAnimation/QAbstractAnimation.md#state--const-state) | const State |



## 公共成员函数

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|          | [QAbstractAnimation](A/QAbstractAnimation/QAbstractAnimation.md#qabstractanimationqabstractanimationqobject-parent--qnullptr)(QObject \**parent* = Q_NULLPTR) |
|  virtual | ~[QAbstractAnimation](A/QAbstractAnimation/QAbstractAnimation.md#virtual-qabstractanimationqabstractanimation)() |



## 公共槽

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|   void   | [pause](A/QAbstractAnimation/QAbstractAnimation.md#slot-void-qabstractanimationpause)() |
|   void   | [resume](A/QAbstractAnimation/QAbstractAnimation.md#slot-void-qabstractanimationresume)() |



## 信号

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|   void   | [currentLoopChanged](A/QAbstractAnimation/QAbstractAnimation.md#signal-void-qabstractanimationcurrentloopchangedint-currentloop)(int *currentLoop*) |
|   void   | [directionChanged](A/QAbstractAnimation/QAbstractAnimation.md#signal-void-qabstractanimationdirectionchangedqabstractanimationdirection-newdirection)(QAbstractAnimation::Direction *newDirection*) |



## 保护成员函数

|   返回类型   | 函数名                                                       |
| :----------: | :----------------------------------------------------------- |
| virtual void | [updateCurrentTime](A/QAbstractAnimation/QAbstractAnimation.md#pure-virtual-protected-void-qabstractanimationupdatecurrenttimeint-currenttime)(int *currentTime*) = 0 |
| virtual void | [updateDirection](A/QAbstractAnimation/QAbstractAnimation.md#virtual-protected-void-qabstractanimationupdatedirectionqabstractanimationdirectionenum-qabstractanimationdirection-direction)(QAbstractAnimation::Direction *direction*) |



## 重写保护成员函数

|   返回类型   | 函数名                                                       |
| :----------: | :----------------------------------------------------------- |
| virtual bool | [event](A/QAbstractAnimation/QAbstractAnimation.md#virtual-protected-bool-qabstractanimationeventqevent-event)(QEvent \**event*) |



## 详细介绍

这里填一些详细介绍。



## 成员变量文档

### enum QAbstractAnimation::DeletionPolicy

|                 函数                  |  值  | 描述                   |
| :-----------------------------------: | :--: | :--------------------- |
|  QAbstractAnimation::KeepWhenStopped  |  0   | 动画停止时不会被删除   |
| QAbstractAnimation::DeleteWhenStopped |  1   | 动画停止时会被自动删除 |


----------

### enum QAbstractAnimation::Direction

xxx

|             函数             |  值  | 描述                                              |
| :--------------------------: | :--: | :------------------------------------------------ |
| QAbstractAnimation::Forward  |  0   | “当前时间”随时间递增（即从0向终点/duration 移动） |
| QAbstractAnimation::Backward |  1   | ”当前时间“随时间递减（即从终点/duration 向0移动） |



## 属性文档

### currentLoop : const int

xxx

**存取函数**

| 返回类型 | 函数名                  |
| :------: | :---------------------- |
|   int    | **currentLoop**() const |

**通知信号**

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|   void   | [currentLoopChanged](A/QAbstractAnimation/QAbstractAnimation.md#signal-void-qabstractanimationcurrentloopchangedint-currentloop)(int *currentLoop*) |


----------

### currentTime : int

xxx

**存取函数**

| 返回类型 | 函数名                        |
| :------: | :---------------------------- |
|   int    | **currentTime**() const       |
|   void   | **setCurrentTime**(int msecs) |



## 成员类型文档

### enum **QAbstractSocket**::BindFlag | flags **QAbstractSocket**::BindMode

这里填该类型详细信息。

----

### XXX

这里填该类型详细信息。



## 成员函数文档

### QAbstractAnimation::**QAbstractAnimation**([QObject](O/QObject/QObject.md) *\*parent* = Q_NULLPTR)

构造 QAbstractAnimation 基类，并将 `parent` 参数传递给 [QObject](O/QObject/QObject.md) 的构造函数。

**另请参阅：**[QVariantAnimation](V/QVariantAnimation/QVariantAnimation.md) 和 [QAnimationGroup](A/QAnimationGroup/QAnimationGroup.md)

----------

###  **[signal]** void QAbstractAnimation::**currentLoopChanged**(int *currentLoop*)

每当当前循环发生变化时，[QAbstractAnimation](A/QAbstractAnimation/QAbstractAnimation.md) 会发射该信号。`currentLoop` 为当前循环。

**注意：**属性 `currentLoop` 的通知信号。

**另请参阅：**[currentLoop](A/QAbstractAnimation/QAbstractAnimation.md#currentloop--const-int)() 和 [loopCount](A/QAbstractAnimation/QAbstractAnimation.md#loopcount--int)()。

