# QMutableMapIterator 类

template <typename Key, typename T> class QMutableMapIterator

QMutableMapIterator 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 Java 风格的非常量迭代器。[更多内容...](QMutableMapIterator.md#详细描述)

| 头文件: | #include <QMutableMapIterator> |
| ------: | :------------------------------ |
|  qmake: | QT += core                     |

- [所有成员列表，包括继承的成员](../../M/QMap/QMutableMapIterator-members.md)



## 公共成员函数

|                               | **[QMutableMapIterator](QMutableMapIterator.md#qmutablemapiteratorqmutablemapiteratorqmapkey-t-map)**(QMap<Key, T> &*map*) |
| -----------------------------: | :------------------------------------------------------------ |
| QMutableMapIterator<Key, T> & | **[operator=](QMutableMapIterator.md#qmutablemapiteratorkey-t-qmutablemapiteratoroperatorqmapkey-t-container)**(QMap<Key, T> &*container*) |
| bool                          | **[findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)**(const T &*value*) |
| bool                          | **[findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)**(const T &*value*) |
| bool                          | **[hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)**() const |
| bool                          | **[hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)**() const |
| const Key &                   | **[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)**() const |
| QMutableMapIterator::Item     | **[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)**() |
| QMutableMapIterator::Item     | **[peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)**() const |
| QMutableMapIterator::Item     | **[peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)**() const |
| QMutableMapIterator::Item     | **[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)**() |
| void                          | **[remove](QMutableMapIterator.md#void-qmutablemapiteratorremove)**() |
| void                          | **[setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)**(const T &*value*) |
| void                          | **[toBack](QMutableMapIterator.md#void-qmutablemapiteratortoback)**() |
| void                          | **[toFront](QMutableMapIterator.md#void-qmutablemapiteratortofront)**() |
| const T &                     | **[value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)**() const |
| T &                           | **[value](QMutableMapIterator.md#t-qmutablemapiteratorvalue)**() |



## 详细描述

[QMap](../../M/QMap/QMap.md) 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。Java 风格迭代器比 STL 风格迭代器更高级，更容易使用；同时也略微低效。

QMutableMapIterator<Key, T> 用来遍历并修改 [QMap](../../M/QMap/QMap.md) (或 [QMultiMap](../../M/QMultiMap/QMultiMap.md)) 。如果不想修改 map（或者 [QMap](../../M/QMap/QMap.md) 是 const 的），可以使用更快速的 [QMapIterator](../../M/QMapIterator/QMapIterator.md)。

QMutableMapIterator 构造函数接受 [QMap](../../M/QMap/QMap.md) 作为参数。构造后，迭代器位于 map 的最开始位置（第一个元素之前）。下面的例子演示如何顺序遍历所有元素：

```c++
QMap<int, QWidget *> map;
...
QMutableMapIterator<int, QWidget *> i(map);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 函数返回 map 中的下一个元素并将迭代器前移。[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 函数返回跳过的最后一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素*之间*而不是直接*指向*元素。第一次调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

下面的例子演示如何反序遍历元素：

```c++
QMutableMapIterator<int, QWidget *> i(map);
i.toBack();
while (i.hasPrevious()) {
    i.previous();
    qDebug() << i.key() << ": " << i.value();
}
```

如果想查找特定值的所有实例，循环使用 [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 或 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()。例如：

```c++
QMutableMapIterator<int, QWidget *> i(map);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

如果想在遍历 map 时移除元素，使用 [remove](QMutableMapIterator.md#void-qmutablemapiteratorremove)()。如果想修改元素的值，使用 [setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)()。

例子：

```c++
QMutableMapIterator<QString, QString> i(map);
while (i.hasNext()) {
    i.next();
    if (i.key() == i.value())
        i.remove();
}
```

该示例移除所有键和值相等的键值对。

任何时候，对于给定 map，只能有一个活动的可修改迭代器。而且，当迭代器处于活动状态时，不可以直接修改 map，因为这会使迭代器失效，并导致未定义行为。

**另请参阅** [QMapIterator](../../M/QMapIterator/QMapIterator.md) 和 [QMap::iterator](../../M/QMap/QMap-iterator.md)。

## 成员函数文档

### bool QMutableMapIterator::findPrevious(const T &*value*)

从当前迭代器位置开始向后查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值，迭代器将被移动到匹配元素的前面；否则，迭代器将被移动到容器的前端。

**另请参阅** [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)()。

### bool QMutableMapIterator::findNext(const T &*value*)

从当前迭代器位置开始向前查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值 *value*，迭代器将被移动到匹配元素的后面；否则，迭代器将被移动到容器的末端。

**另请参阅** [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()。

### const Key &QMutableMapIterator::key() const

调用遍历函数（[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()，[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()，[findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)()，[findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()）后，该函数返回跳过的最后一个元素的键。

调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 或 [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 后，[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 与 [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)().[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 相同。调用 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() 或 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)() 后，[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 与 [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)().[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 相同。

**另请参阅** [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)()。

### T &QMutableMapIterator::value()

这是一个重载函数。

返回调用遍历函数后跳过的最后一个元素值的非常量引用。

### QMutableMapIterator::Item QMutableMapIterator::peekPrevious() const

不移动迭代器而返回前一个元素。

对返回值调用 [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 获取元素的键，调用 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 获取元素的值。

对位于容器前端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)()，[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() 和 [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)()。

### QMutableMapIterator::Item QMutableMapIterator::previous()

返回前一个元素并将迭代器向后移动一个位置。

对返回值调用 [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 获取元素的键，调用 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 获取元素的值。

对位于容器前端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)()，[peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)() 和 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()。

### bool QMutableMapIterator::hasPrevious() const

如果该迭代器前面至少有一个元素，返回 `true`，即该迭代器不在容器的前端；否则返回 `false`。

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)() 和 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()。

### bool QMutableMapIterator::hasNext() const

如果该迭代器后面至少有一个元素，返回 `true`，即该迭代器不在容器的末端；否则返回 `false`。

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)() 和 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()。

### void QMutableMapIterator::toBack()

将迭代器移动到容器的末端（最后一个元素之后）。

**另请参阅** [toFront](QMutableMapIterator.md#void-qmutablemapiteratortofront)() 和 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()。

### void QMutableMapIterator::toFront()

将迭代器移动到容器的前端（第一个元素之前）。

**另请参阅** [toBack](QMutableMapIterator.md#void-qmutablemapiteratortoback)() 和 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()。

### [QMutableMapIterator](QMutableMapIterator.md#qmutablemapiteratorqmutablemapiteratorqmapkey-t-map)<Key, T> &QMutableMapIterator::operator=([QMap](../../M/QMap/QMap.md)<Key, T> &*container*)

将迭代器关联到 *container* 来遍历 map。迭代器将被移动到 map 的前端（第一个元素之前）。

**另请参阅** [toFront](QMutableMapIterator.md#void-qmutablemapiteratortofront)() 和 [toBack](QMutableMapIterator.md#void-qmutablemapiteratortoback)()。

### QMutableMapIterator::QMutableMapIterator([QMap](../../M/QMap/QMap.md)<Key, T> &*map*)

构造一个迭代器来遍历 *map*。迭代器将被移动到 map 的前端（第一个元素之前）。

**另请参阅** [operator=](QMutableMapIterator.md#qmutablemapiteratorkey-t-qmutablemapiteratoroperatorqmapkey-t-container)()。

### QMutableMapIterator::Item QMutableMapIterator::next()

返回下一个元素并将迭代器向前移动一个位置。

对返回值调用 [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 获取元素的键，调用 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)()，[peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)()和 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()。

### QMutableMapIterator::Item QMutableMapIterator::peekNext() const

不移动迭代器而返回下一个元素。

对返回值调用 [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 获取元素的键，调用 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)()，[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()和 [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)()。

### void QMutableMapIterator::remove()

移除使用遍历函数（[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()，[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()，[findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)()，[findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()）跳过的最后一个元素。

**另请参阅** [setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)().

### void QMutableMapIterator::setValue(const T &*value*)

用 *value* 替换使用遍历函数跳过的最后一个元素的值。

遍历函数包括 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()，[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()，[findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 和 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()。

**另请参阅** [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)()，[value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 和 [remove](QMutableMapIterator.md#void-qmutablemapiteratorremove)()。

### const T &QMutableMapIterator::value() const

调用遍历函数（[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()，[previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)()，[findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)()，[findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()）后，该函数返回跳过的最后一个元素的值。

调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 或 [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 后，value() 与 [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)().value() 相同。调用 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() 或 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)() 后，value() 与 [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)().value() 相同。

**另请参阅** [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 和 [setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)()。