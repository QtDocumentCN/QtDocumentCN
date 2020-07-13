[TOC]
# **QAbstractAxis**

----------

## **QAbstractAxis类是用于专门处理坐标轴的类**

|  属性  | 方法|
|------:|:------|
|头文件:|`    #include <QAbstractAxis>`|
|实例化:|    AbstractAxis|
|继承:    |QObject|
|派生:|QBarCategoryAxis, QDateTimeAxis, QLogValueAxis, and QValueAxis|


----------

## **简述**

----------
### **公共类型**

|  类型  | 方法|
|------:|:------|
|enum |    AxisType { AxisTypeNoAxis, AxisTypeValue, AxisTypeBarCategory, AxisTypeCategory, AxisTypeDateTime, AxisTypeLogValue }|
|flags |    AxisTypes|


----------


### **属性**
|  函数名  | 类型|
|------:|:------|
| alignment :| const Qt::Alignment|
|color : |QColor|
| gridLineColor :| QColor|
| gridLinePen :| QPen|
| gridVisible : |bool|
|  labelsAngle : |int|
|  labelsBrush : |QBrush|
| labelsColor : |QColor|
| labelsFont : |QFont|
|  labelsVisible : |bool|
| linePen : |QPen|
| lineVisible :| bool|
| minorGridLineColor :| QColor|
| minorGridLinePen :| QPen|
| minorGridVisible :| bool|
| orientation : |const Qt::Orientation|
|reverse : |bool|
|shadesBorderColor :| QColor|
|shadesBrush : |QBrush|
|    shadesColor : |QColor|
|    shadesPen :| QPen|
|    shadesVisible : |bool|
|    titleBrush : |QBrush|
|    titleFont :| QFont|
|  titleText :| QString|
|  titleVisible : |bool|
|  visible : |bool|


----------

### **Public Functions**

|  类型  | 函数名|
|------:|:------|
|    |~QAbstractAxis()|
|Qt::Alignment |    alignment() const|
|QColor |    gridLineColor()|
|QPen |    gridLinePen() const|
|void |    hide()|
|bool |    isGridLineVisible() const|
|bool |    isLineVisible() const|
|bool |    isMinorGridLineVisible() const|
|bool |    isReverse() const|
|bool |    isTitleVisible() const|
|bool |    isVisible() const|
|int |    labelsAngle() const|
|QBrush |    labelsBrush() const|
|QColor |    labelsColor() const|
|QFont |    labelsFont() const|
|bool |    labelsVisible() const|
|QPen |    linePen() const|
|QColor |    linePenColor() const|
|QColor |    minorGridLineColor()|
|QPen |    minorGridLinePen() const|
|Qt::Orientation |    orientation() const|
|void    |setGridLineColor(const QColor &color)|
|void |    setGridLinePen(const QPen &pen)|
|void |    setGridLineVisible(bool visible = true)|
|void    |setLabelsAngle(int angle)|
|void |    setLabelsBrush(const QBrush &brush)|
|void |    setLabelsColor(QColor color)|
|void |    setLabelsFont(const QFont &font)|
|void |    setLabelsVisible(bool visible = true)|
|void |    setLinePen(const QPen &pen)|
|void |    setLinePenColor(QColor color)|
|void    |setLineVisible(bool visible = true)|
|void |    setMax(const QVariant &max)|
|void |    setMin(const QVariant &min)|
|void |    setMinorGridLineColor(const QColor &color)|
|void|    setMinorGridLinePen(const QPen &pen)|
|void |    setMinorGridLineVisible(bool visible = true)|
|void |    setRange(const QVariant &min, const QVariant &max)|
|void |    setReverse(bool reverse = true)|
|void |    setShadesBorderColor(QColor color)|
|void |    setShadesBrush(const QBrush &brush)|
|void |    setShadesColor(QColor color)|
|void |    setShadesPen(const QPen &pen)|
|void |    setShadesVisible(bool visible = true)|
|void |    setTitleBrush(const QBrush &brush)|
|void |    setTitleFont(const QFont &font)|
|void |    setTitleText(const QString &title)|
|void |    setTitleVisible(bool visible = true)|
|void |    setVisible(bool visible = true)|
|QColor |    shadesBorderColor() const|
|QBrush |    shadesBrush() const|
|QColor |    shadesColor() const|
|QPen |    shadesPen() const|
|bool |    shadesVisible() const|
|void |    show()|
|QBrush |    titleBrush() const|
|QFont |    titleFont() const|
|QString |    titleText() const|
|virtual AxisType |    type() const = 0|


----------

### **信号**

|  类型  | 函数名|
|------:|:------|
|void |    colorChanged(QColor color)|
|void |    gridLineColorChanged(const QColor &color)|
|void |    gridLinePenChanged(const QPen &pen)|
|void |    gridVisibleChanged(bool visible)|
|void |    labelsAngleChanged(int angle)|
|void |    labelsBrushChanged(const QBrush &brush)|
|void |    labelsColorChanged(QColor color)|
|void |    labelsFontChanged(const QFont &font)|
|void |    labelsVisibleChanged(bool visible)|
|void |    linePenChanged(const QPen &pen)|
|void |    lineVisibleChanged(bool visible)|
|void |    minorGridLineColorChanged(const QColor &color)|
|void |    minorGridLinePenChanged(const QPen &pen)|
|void |    minorGridVisibleChanged(bool visible)|
|void |    reverseChanged(bool reverse)|
|void |    shadesBorderColorChanged(QColor color)|
|void |    shadesBrushChanged(const QBrush &brush)|
|void |    shadesColorChanged(QColor color)|
|void |    shadesPenChanged(const QPen &pen)|
|void |    shadesVisibleChanged(bool visible)|
|void |    titleBrushChanged(const QBrush &brush)|
|void |    titleFontChanged(const QFont &font)|
|void |    titleTextChanged(const QString &text)|
|void |    titleVisibleChanged(bool visible)|
|void |    visibleChanged(bool visible)|


----------

## **详细说明**

----------
QAbstractAxis是专门用于处理坐标轴的基类。

每一个连续的序列可以绑定到一个或者多个水平轴和垂直轴，但是不同域的混合轴的类型是不支持的。比如在同一个方向指定QValueAxis和QLogValueAxis。

每个轴的元素（比如轴线，标题，标签，网格线，阴影，可见性）都是可以控制的。

----------


## **成员变量**

**enum QAbstractAxis::AxisType**
**flags QAbstractAxis::AxisTypes**

----------

***这个枚举类型指定了轴对象的类型***

|  变量  | 值|
|------:|:------|
|QAbstractAxis::AxisTypeNoAxis|    0x0|
|QAbstractAxis::AxisTypeValue|    0x1|
|QAbstractAxis::AxisTypeBarCategory|    0x2|
|QAbstractAxis::AxisTypeCategory|    0x4|
|QAbstractAxis::AxisTypeDateTime|    0x8|
|QAbstractAxis::AxisTypeLogValue|    0x10|

`AxisTypes`是`QFlags<AxisType>`的typedef。它是AxisType类型的组合。
（也就是个宏呗）

----------
**alignment : const Qt::Alignment**
该属性是轴的对齐属性
其值可以为 Qt::AlignLeft, Qt::AlignRight, Qt::AlignBottom, or Qt::AlignTop.
**相关函数**

|  类型  | 函数名|
|------:|:------|
|Qt::Alignment |    alignment() const|


----------
**color : QColor**
该属性是指坐标轴与刻度的颜色

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QColor |    linePenColor() const|
|void    |setLinePenColor(QColor color)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void |    colorChanged(QColor color)|


----------

**gridLineColor : QColor**
该属性是指网格线的颜色

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QColor    |gridLineColor()|
|void|    setGridLineColor(const QColor &color)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    gridLineColorChanged(const QColor &color)|


----------


**gridLinePen : QPen**
该属性是指绘制网格线的笔

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QPen|    gridLinePen() const|
|void|    setGridLinePen(const QPen &pen)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    gridLinePenChanged(const QPen &pen)|


----------

**gridVisible : bool**
该属性是网格线是否可见

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QPen|    gridLinePen() const|
|void|    setGridLinePen(const QPen &pen)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    gridLinePenChanged(const QPen &pen)|


----------


**labelsAngle : int**
该属性以度数保存轴坐标的角度

**相关函数**

|  类型  | 函数名|
|------:|:------|
|int|    labelsAngle() const|
|void|    setLabelsAngle(int angle)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    labelsAngleChanged(int angle)|


----------


**labelsBrush : QBrush**
该属性表示用于绘制标签的画笔
只有画刷的颜色是相关的（这句话其实我不太理解Only the color of the brush is relevant.）

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QBrush |    labelsBrush() const|
|void    |setLabelsBrush(const QBrush &brush)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void |    labelsBrushChanged(const QBrush &brush)|


----------

**labelsColor : QColor**
该属性表示轴标签的颜色

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QColor|    labelsColor() const|
|void|    setLabelsColor(QColor color)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    labelsColorChanged(QColor color)|


----------

**labelsFont : QFont**
该属性表示轴标签的字体信息

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QFont|    labelsFont() const|
|void|    setLabelsFont(const QFont &font)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    labelsFontChanged(const QFont &font)|


----------

**labelsVisible : bool**
该属性表示轴标签是否可见

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    labelsVisible() const|
|void|    setLabelsVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    labelsVisibleChanged(bool visible)|


----------

**linePen : QPen**
该属性表示绘制轴线的笔相关

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QPen|    linePen() const|
|void|    setLinePen(const QPen &pen)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    linePenChanged(const QPen &pen)|


----------

**lineVisible : bool**
该属性表示轴线是否可见

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool    |isLineVisible() const|
|void|    setLineVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    lineVisibleChanged(bool visible)|


----------

**minorGridLineColor : QColor**
该属性表示副格线的颜色
仅适用于支持副网格线的轴

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QColor |    minorGridLineColor()|
|void    |setMinorGridLineColor(const QColor &color)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    minorGridLineColorChanged(const QColor &color)|


----------

**minorGridLinePen : QPen**
该属性表示副格线的笔
仅适用于支持副网格线的轴

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QPen|    minorGridLinePen() const|
|void|    setMinorGridLinePen(const QPen &pen)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    minorGridLinePenChanged(const QPen &pen)|


----------

**minorGridVisible : bool**
该属性表示副格线是否可见
仅适用于支持副网格线的轴

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    isMinorGridLineVisible() const|
|void|    setMinorGridLineVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void    |minorGridVisibleChanged(bool visible)|


----------

**orientation : const Qt::Orientation**
该属性表示坐标轴的方向。
当坐标轴被添加到图表时，该属性为Qt::Horizontal或者Qt::Vertical

**相关函数**

|  类型  | 函数名|
|------:|:------|
|Qt::Orientation|    orientation() const|


----------

**reverse : bool**
该属性表示是否使用反转轴。
该值默认为false。
反转轴由直线，样条，散列图系列以及笛卡尔图表组成的区域支持。如果一个方向相反，或者行为为定义，则所有相同方向的所有轴必须保持一致。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    isReverse() const|
|void|    setReverse(bool reverse = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    reverseChanged(bool reverse)|


----------

**shadesBorderColor : QColor**
该属性表示坐标轴阴影的边框（笔）颜色

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QColor|    shadesBorderColor() const|
|void|    setShadesBorderColor(QColor color)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    shadesBorderColorChanged(QColor color)|


----------

**shadesBrush : QBrush**
该属性表示用于绘制轴阴影的画笔（网格线之间的区域）

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QPen|    shadesPen() const|
|void|    setShadesPen(const QPen &pen)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    shadesPenChanged(const QPen &pen)|


----------

**shadesVisible : bool**
该属性表示轴阴影是否可见

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    shadesVisible() const|
|void|    setShadesVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    shadesVisibleChanged(bool visible)|


----------

**titleBrush : QBrush**
该属性表示用于绘制坐标轴标题文本的画笔。
只影响画刷的颜色。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QBrush|    titleBrush() const|
|void|    setTitleBrush(const QBrush &brush)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    titleBrushChanged(const QBrush &brush)|


----------

**titleFont : QFont**
该属性表示坐标轴标题的字体。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QFont|    titleFont() const|
|void|    setTitleFont(const QFont &font)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    titleFontChanged(const QFont &font)|


----------

**titleText : QString**
该属性表示坐标轴的标题
默认为空，坐标轴的标题支持HTML的格式。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|QString|    titleText() const|
|void|    setTitleText(const QString &title)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    titleTextChanged(const QString &text)|


----------

**titleVisible : bool**
该属性表示坐标轴的可见性。
默认值为true。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    isTitleVisible() const|
|void|    setTitleVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    titleVisibleChanged(bool visible)|


----------

**visible : bool**
该属性表示坐标轴的可见性。

**相关函数**

|  类型  | 函数名|
|------:|:------|
|bool|    isVisible() const|
|void|    setVisible(bool visible = true)|

**通知信号**

|  类型  | 函数名|
|------:|:------|
|void|    visibleChanged(bool visible)|


----------

##**成员函数**

----------

**QAbstractAxis::~QAbstractAxis()**
析构函数，销毁轴对象，当一个坐标轴添加到图表时，该图表获得该坐标轴的所有权。

----------

**void QAbstractAxis::colorChanged(QColor color) [信号]**
当坐标轴的颜色变化时，该信号被发射。
注意：属性color的通知信号。

----------

**void QAbstractAxis::gridLineColorChanged(const QColor &color) [信号]**
当绘制网格线的笔的颜色改变时，该信号被发射。
注意：属性gridLineColor的通知信号。

----------

**QPen QAbstractAxis::gridLinePen() const**
返回用于绘制网格的笔。
注意:属性gridLinePen的Getter函数。
另参见函数setGridLinePen()。

----------

**void QAbstractAxis :: gridLinePenChanged（const QPen＆pen） [信号]**
当用于绘制网格线的笔变化时，会发出此信号。
注意:属性gridLinePen的通知信号。

----------

**void QAbstractAxis::gridVisibleChanged(bool visible) [信号]**
当坐标轴的网格线的可见性变化时，发出该信号。
注意:属性gridVisible的通知信号。

----------

**void QAbstractAxis::hide()**
使坐标轴，阴影，标签，网格线不可见。

----------

**void QAbstractAxis::labelsAngleChanged(int angle) [信号]**
当坐标轴标签的角度变化时，发出该信号。
注意：属性标签角度的通知信号

----------

**QBrush QAbstractAxis::labelsBrush() const**
返回用于绘制标签的画笔。
注意:属性labelsBrush的Getter函数。
另参见setLabelsBrush().

----------

**void QAbstractAxis::labelsBrushChanged(const QBrush &brush) [信号]**
当用于绘制坐标轴标签的画笔改变时，会发出此信号。
属性Brush的通知信号。

----------

**void QAbstractAxis :: labelsColorChanged（QColor color） [信号signal]**
当坐标轴标签的颜色改变时，会发出此信号。
属性labelsColor的通知信号。

----------

**QFont QAbstractAxis::labelsFont()const **
返回用于绘制标签的字体。 
注意:属性labelsFont的Getter函数。
另参见函数setLabelsFont()。

----------

**void QAbstractAxis :: labelsFontChanged（const QFont＆font）[信号]**
当坐标轴的字体改变时，会发出此信号。
属性labelsFont的通知信号。

----------

**void QAbstractAxis::labelsVisibleChanged(bool visible) [信号]**
当坐标轴标签的可见性变化时，会发出此信号。
属性labelsVisible的通知信号。

----------

**QPen QAbstractAxis::linePen() const**
返回用于绘制轴线与刻度线的笔。
注意:属性linePen的Getter函数。
另参阅函数setLinePen()。

----------

**void QAbstractAxis::linePenChanged(const QPen &pen) [信号]**
当绘制坐标轴的笔变化时，会发出此信号。
注意:属性linePen的通知信号。

----------

**void QAbstractAxis::lineVisibleChanged(bool visible) [信号]**
当坐标轴线的可见性变化时，会发出此信号。
注意:属性lineVisible的通知信号。

----------

**void QAbstractAxis::minorGridLineColorChanged(const QColor &color) [信号]**
当绘制副格线的笔的颜色变化时，该信号被发射。
注意:属性minorGridLineColor的通知信号。

----------

**void QAbstractAxis::minorGridLinePenChanged(const QPen &pen) [信号]**
当绘制副格线的笔变化时，该信号被发射。
注意：属性minorGridLinePen的通知信号。

----------

**void QAbstractAxis::minorGridVisibleChanged(bool visible) [信号]**
当绘制副格线的可见性变化时，该信号被发射。
注意:属性minorGridVisible的通知信号。

----------

**Qt::Orientation QAbstractAxis::orientation() const**
返回坐标轴的方向(垂直或者水平)
注意:坐标轴方向的Getter函数。

----------

**void QAbstractAxis::setGridLinePen(const QPen &pen)**
设置绘制网格线的笔。
注意:gridLinePen的Setter函数。
另参见函数gridLinePen()。

----------

**void QAbstractAxis::setLabelsBrush(const QBrush &brush)**
设置用于绘制标签的画笔。
注意:属性LabelsBrush的Setter函数。
另参阅labelsBrush().

----------

**void QAbstractAxis::setLabelsFont(const QFont &font)**
设置用于绘制标签的字体相关
注意:属性labelsFont的Setter函数。
另参阅函数labelsFont()。

----------

**void QAbstractAxis::setLinePen(const QPen &pen)**
设置用于绘制坐标轴线和刻度线的笔。
注意：属性linePen的Setter函数。
另参见函数linePen（）。

----------

**void QAbstractAxis::setLineVisible(bool visible = true)**
设置坐标轴线与刻度线是否可见。
注意:属性lineVisible的Setter函数
另参见函数isLineVisible()。

----------

**void QAbstractAxis::setMax(const QVariant &max)**
设置坐标轴上显示的最大值。根据当前坐标轴的类型，最大值参数会被转换为适当的值。如果转化失败，该函数设置无效。

----------

**void QAbstractAxis::setMin(const QVariant &min)**
设置坐标轴上显示的最小值。根据当前坐标轴的类型，最小值参数会被转换为适当的值。如果转化失败，该函数设置无效。

----------

**void QAbstractAxis::setRange(const QVariant &min, const QVariant &max)**
设置坐标轴的范围。根据当前坐标轴的类型，最大值最小值会被转换为适当的值。如果转化失败，该函数设置无效。

----------

**void QAbstractAxis::setShadesBrush(const QBrush &brush)**
设置用于绘制阴影的画笔。
注意：属性shadesBrush的Setter函数。
另参见函数shadesBrush().

----------

**void QAbstractAxis::setShadesPen(const QPen &pen)**
设置用于绘制阴影的笔。
注意：属性shadesPen的Setter函数。
另参见函数shadesPen().

----------

**void QAbstractAxis::setTitleBrush(const QBrush &brush)**
设置用于绘制标题的画笔。
注意：属性titleBrush的Setter函数。
另参见函数titleBrush().

----------

**void QAbstractAxis::setTitleFont(const QFont &font)**
设置用于绘制标题的笔。
注意：属性titleFont的Setter函数。
另参见函数titleFont().

----------

**void QAbstractAxis::setVisible(bool visible = true)**
设置坐标轴，阴影，标签，网格线是否可见。
注意：属性visible的Setter函数。
另参见函数isVisible().

----------

**void QAbstractAxis::shadesBorderColorChanged(QColor color) [信号signal]**
当绘制坐标轴边框的颜色变化时，会发出此信号。
注意:属性shadesBorderColor的通知信号。

----------

**QBrush QAbstractAxis::shadesBrush() const**
返回用于绘制阴影的画笔。
注意：属性shadesBrush()的Getter函数。
另参阅函数setShadesBrush().

----------

**void QAbstractAxis::shadesBrushChanged(const QBrush &brush) [信号signal]**
当绘制坐标轴阴影的画刷变化时，会发出此信号。
注意:属性shadesBrush()的通知信号。

----------

**void QAbstractAxis::shadesColorChanged(QColor color) [信号signal]**
当绘制坐标轴阴影颜色发生变化时，会发出此信号。
注意:属性shadesColor()的通知信号。

----------

**QPen QAbstractAxis::shadesPen() const**
返回用于绘制阴影的笔。
注意:属性shadesPen()的Getter函数
另参阅函数setShadesPen().

----------

**void QAbstractAxis::shadesPenChanged(const QPen &pen) [信号signal]**
当绘制坐标轴阴影的笔发生变化时，会发出此信号。
注意:属性shadesPen()的通知信号。

----------

**void QAbstractAxis::shadesVisibleChanged(bool visible) [信号signal]**
当坐标轴的阴影可见性变化时，会发出此信号。
注意:属性shadesVisible()的通知信号。

----------

**void QAbstractAxis::show()**
使坐标轴，阴影，标签，网格线可见。

----------

**QBrush QAbstractAxis::titleBrush() const**
返回用于绘制标题的画刷
注意:属性titleBrush的Getter函数
另参阅函数setTitleBrush()

----------

**void QAbstractAxis::titleBrushChanged(const QBrush &brush) [信号signal]**
当绘制坐标轴标题的画刷变化时，该信号被发射
注意:titleBrush的通知信号。

----------

**QFont QAbstractAxis::titleFont() const**
返回绘制标题的笔相关属性。
注意：titleFont的Getter函数
另参阅函数setTitleFont()

----------

**void QAbstractAxis::titleFontChanged(const QFont &font) [信号 signal]**
当坐标轴标题的字体属性更改时，会发出此信号。
注意:titleFont的通知信号。

----------

**void QAbstractAxis::titleTextChanged(const QString &text) [信号 signal]**
当坐标轴标题的文本内容改变时，会发出此信号。
注意:titleText的通知信号。

----------

**void QAbstractAxis::titleVisibleChanged(bool visible) [信号 signal]**
当坐标轴的标题文本的可见性变化时，会发出此信号。
注意:titleVisible的通知信号

----------

**AxisType QAbstractAxis::type() const**
返回坐标轴的类型

----------

**void QAbstractAxis::visibleChanged(bool visible)**
当坐标轴的可见性变化时，会发出此信号。
注意：坐标轴的visible的通知信号


