[TOC]
# **QAbstractBarSeries**
 
----------
 
## **QAbstractBarSeries是所有柱状图/条形图系列的基类**

 
|  属性  | 方法|
|------:|:------|
|头文件:|`#include<QAbstractBarSeries>`|
|实例化:|AbstractBarSeries|
|继承:  |QAbstractSeries|
|派生:|QBarSeries, QHorizontalBarSeries, QHorizontalPercentBarSeries, QHorizontalStackedBarSeries, QPercentBarSeries, and QStackedBarSeries|
 
 
----------
 
## **简述**
 
----------
### **公共类型**
 
|  类型  | 方法|
|------:|:------|
|enum |    LabelsPosition { LabelsCenter, LabelsInsideEnd, LabelsInsideBase, LabelsOutsideEnd }|
 
 
----------
 
 
### **属性**
|  函数名  | 类型|
|------:|:------|
| barWidth :| qreal|
|count : |const int|
| labelsAngle :| qreal|
5个属性继承自QAbstractSeries
1个属性继承自QObject

 
----------
 
### **Public Functions**
 
|  类型  | 函数名|
|------:|:------|
|virtual |    ~QAbstractBarSeries()|
|bool |    append(QBarSet *set)|
|bool |    append(QList<QBarSet *> sets)|
|QList<QBarSet *>|    barSets() const|
|qreal |    barWidth() const|
|void |    clear()|
|int |    count() const|
|bool |    insert(int index, QBarSet *set)|
|bool |    isLabelsVisible() const|
|qreal     |labelsAngle() const|
|QString |    labelsFormat() const|
|QAbstractBarSeries::LabelsPosition |    labelsPosition() const|
|bool |    remove(QBarSet *set)|
|void |    setBarWidth(qreal width)|
|void |    setLabelsAngle(qreal angle)|
|void |    setLabelsFormat(const QString &format)|
|void|     setLabelsPosition(QAbstractBarSeries::LabelsPosition position)|
|void     |setLabelsVisible(bool visible = true)|
|bool |    take(QBarSet *set)|
15个公共函数继承自QAbstractSeries
32个公共函数继承自QObject
 
----------
 
### **信号**
 
|  类型  | 函数名|
|------:|:------|
|void |barsetsAdded(QList<QBarSet *> sets)|
|void |barsetsRemoved(QList<QBarSet *> sets)|
|void |    clicked(int index, QBarSet *barset)|
|void |    countChanged()|
|void |    doubleClicked(int index, QBarSet *barset)|
|void |    hovered(bool status, int index, QBarSet *barset)|
|void |    labelsAngleChanged(qreal angle)|
|void |    labelsFormatChanged(const QString &format)|
|void |    labelsPositionChanged(QAbstractBarSeries::LabelsPosition position)|
|void |    labelsVisibleChanged()|
|void |    pressed(int index, QBarSet *barset)|
|void |    released(int index, QBarSet *barset)|


----------


### **额外继承的**
1个公共槽继承自QObject
11个静态成员函数继承自QObject
9个保护函数继承自QObject

----------
 
## **详细说明**

QAbstractBarSeries类是所有条形柱的抽象类。

在条形图中，条形柱被定义为包含一种数据的集合。条形柱的位置由其类别与数值来决定。条形柱组合则是属于同一类别的条形柱。条形柱的显示则是由创建图表的时候决定的。

如果使用QValueAxis来代替QBarCategoryAxis当做图表的主轴。那么条形柱别按照索引值来分类。

可以参考Qt Example（example 这里我还没有来得及翻译）

----------
## 成员类型

enum QAbstractBarSeries::LabelsPosition**

这个枚举值表示的是条形柱标签的位置：

| 枚举值 | 数值 | 描述 |
|------:|:------|:------|
| QAbstractBarSeries::LabelsCenter| 0 | 中部 |
| QAbstractBarSeries::LabelsInsideEnd | 1 | 顶部 |
| QAbstractBarSeries::LabelsInsideBase | 2 | 底部 |
| QAbstractBarSeries::LabelsOutsideEnd | 3 | 外部 |

