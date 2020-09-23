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



# QTransform

QTransform为2D坐标系提供坐标转化

|   属性 | 方法                                                         |
| -----: | :----------------------------------------------------------- |
| 头文件 | `#include <QTransform>`                               |
|  qmake | `QT+=gui`                                                   |
|   自从 | Qt 4.3                                                      |


---

## 公共成员类型

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| enum | TransformationType { TxNone, TxTranslate, TxScale, TxRotate, TxShear, TxProject }|




## 属性

| 属性                                                         | 类型      | 属性                                                         | 类型        |
| :----------------------------------------------------------- | --------- | ------------------------------------------------------------ | ----------- |
| [currentLoop](A/QAbstractAnimation/QAbstractAnimation.md#currentloop--const-int) | const int | [duration](A/QAbstractAnimation/QAbstractAnimation.md#duration--const-int) | const int   |
| [currentTime](A/QAbstractAnimation/QAbstractAnimation.md#currenttime--int) | int       | [loopCount](A/QAbstractAnimation/QAbstractAnimation.md#loopcount--int) | int         |
| [direction](A/QAbstractAnimation/QAbstractAnimation.md#direction--direction) | Direction | [state](A/QAbstractAnimation/QAbstractAnimation.md#state--const-state) | const State |

------------

## 公共成员函数

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|          |QTransform(qreal m11, qreal m12, qreal m21, qreal m22, qreal dx, qreal dy)|
|          |QTransform(qreal m11, qreal m12, qreal m13, qreal m21, qreal m22, qreal m23, qreal m31, qreal m32, qreal m33 = 1.0)|
|          |QTransform()|
|QTransform &|	operator=(const QTransform &matrix)|
|qreal	|m11() const|
|qreal	|m12() const|
|qreal	|m13() const|
|qreal	|m21() const|
|qreal	|m22() const|
|qreal	|m23() const|
|qreal	|m31() const|
|qreal	|m32() const|
|qreal	|m33() const|
|QTransform|	adjoint() const|
|qreal|	determinant() const|
|qreal	|dx() const|
|qreal|	dy() const|
|QTransform	|inverted(bool *invertible = nullptr) const|
|bool	|isAffine() const|
|bool	|isIdentity() const|
|bool	|isInvertible() const|
|bool	|isRotating() const|
|bool	|isScaling() const|
|bool	|isTranslating() const|
|void	|map(qreal x, qreal y, qreal *tx, qreal *ty) const|
|QPoint|	map(const QPoint &point) const|
|QPointF|	map(const QPointF &p) const|
|QLine	|map(const QLine &l) const|
|QLineF	|map(const QLineF &line) const|
|QPolygonF|	map(const QPolygonF &polygon) const|
|QPolygon|	map(const QPolygon &polygon) const|
|QRegion|	map(const QRegion &region) const|
|QPainterPath|	map(const QPainterPath &path) const|
|void	|map(int x, int y, int *tx, int *ty) const|
|QRectF	|mapRect(const QRectF &rectangle) const|
|QRect|	mapRect(const QRect &rectangle) const|
|QPolygon|	mapToPolygon(const QRect &rectangle) const|
|void	|reset()|
|QTransform &|	rotate(qreal angle, Qt::Axis axis = Qt::ZAxis)|
|QTransform &|	rotateRadians(qreal angle, Qt::Axis axis = Qt::ZAxis)|
|QTransform &|	scale(qreal sx, qreal sy)|
|void	|setMatrix(qreal m11, qreal m12, qreal m13, qreal m21, qreal m22, qreal m23, qreal m31, qreal m32, qreal m33)|
|QTransform &|	shear(qreal sh, qreal sv)|
|QTransform &|	translate(qreal dx, qreal dy)|
|QTransform|	transposed() const|
|QTransform::TransformationType	|type() const|
|QVariant|	operator QVariant() const|
|bool|	operator!=(const QTransform &matrix) const|
|QTransform	|operator*(const QTransform &matrix) const|
|QTransform &|	operator*=(const QTransform &matrix)|
|QTransform &|	operator*=(qreal scalar)|
|QTransform &|	operator+=(qreal scalar)|
|QTransform &|	operator-=(qreal scalar)|
|QTransform &|	operator/=(qreal scalar)|
|bool	|operator==(const QTransform &matrix) const|

--------

## 静态公共成员函数

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|QTransform|	fromScale(qreal sx, qreal sy)|
|QTransform|	fromTranslate(qreal dx, qreal dy)|
|bool	|quadToQuad(const QPolygonF &one, const QPolygonF &two, QTransform &trans)|
|bool	|quadToSquare(const QPolygonF &quad, QTransform &trans)|
|bool	|squareToQuad(const QPolygonF &quad, QTransform &trans)|

---------

## 相关非成员函数

| 返回类型 | 函数名                                                       |
| :------: | :----------------------------------------------------------- |
|bool|	qFuzzyCompare(const QTransform &t1, const QTransform &t2)|
|uint|	qHash(const QTransform &key, uint seed = 0)|
|QPainterPath|	operator*(const QPainterPath &path, const QTransform &matrix)|
|QPoint	|operator*(const QPoint &point, const QTransform &matrix)|
|QPointF|	operator*(const QPointF &point, const QTransform &matrix)|
|QLineF|	operator*(const QLineF &line, const QTransform &matrix)|
|QLine|	operator*(const QLine &line, const QTransform &matrix)|
|QPolygon|	operator*(const QPolygon &polygon, const QTransform &matrix)|
|QPolygonF|	operator*(const QPolygonF &polygon, const QTransform &matrix)|
|QRegion|	operator*(const QRegion &region, const QTransform &matrix)|
|QDataStream &|	operator<<(QDataStream &stream, const QTransform &matrix)|
|QDataStream &|	operator>>(QDataStream &stream, QTransform &matrix)|

------------------


## 详细介绍

这里填一些详细介绍。

一个转化是指如何平移，缩放，剪切，旋转或投影坐标系，通常在渲染图形时使用。

QTransform与QMatrix的不同之处在于，它是真正的3x3矩阵，允许映射变换。QTransform的toAffine()方法允许将QTransform强制转换为QMatrix。如果在矩阵上指定了映射变换，则该变换将导致其数据丢失。

QTransform是Qt中推荐的坐标转换类。

QTransform 可以使用函数 `setMatrix(), scale(), rotate(), translate() , shear()` 来构建 ,或者，可以通过应用基本矩阵运算来构建它。也可以在构造矩阵时对其进行定义，并可以使用`reset()`函数将其重置为恒等矩阵（默认值）

QTransform类支持基本图元的映射：可以使用`map()`函数将给定的点，线，多边形，区域或绘画路径映射到此矩阵定义的坐标系。如果是矩形，可以使用`mapRect()`函数转换其坐标。也可以使用`mapToPolygon()`函数将矩形转换为多边形（映射到由此矩阵定义的坐标系）。

`QTransform`提供`isIdentity()`函数，来判断是否为单位矩阵(在矩阵的乘法中，有一种矩阵起着特殊的作用，如同数的乘法中的1，这种矩阵被称为单位矩阵。它是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为1。除此以外全都为0。via百度百科)， `isInvertible()` 函数来判断矩阵是否可逆(i.e. AB = BA = I).`inverted()`函数提供一个翻转的拷贝矩阵(否则返回单位矩阵)，`adjoint()` 函数来判断矩阵是否为共轭矩阵。另外，`QTransform`提供了determinant()函数，该函数返回矩阵的行列式。

最后，QTransform类支持矩阵乘法，加法和减法，并且可以比较该类的其它对象。

### 渲染图形


--------------------

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

**注意：** 属性 `currentLoop` 的通知信号。

**另请参阅：** [currentLoop](A/QAbstractAnimation/QAbstractAnimation.md#currentloop--const-int)() 和 [loopCount](A/QAbstractAnimation/QAbstractAnimation.md#loopcount--int)()。

