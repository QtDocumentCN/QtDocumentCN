# QMapIterator 类

template <typename Key, typename T> class QMapIterator

QMapIterator 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 Java 风格的常量迭代器。[更多内容...](QMapIterator.md#详细描述)

| 头文件: | #include <QMapIterator> |
| ------: | :----------------------- |
|  qmake: | QT += core              |

- [所有成员列表，包括继承的成员](../../M/QMap/QMapiterator-members.md)



## 公共成员函数

|                        | **[QMapIterator](QMapIterator.md#qmapiteratorqmapiteratorconst-qmapkey-t-map)**(const QMap<Key, T> &*map*) |
| ----------------------: | :------------------------------------------------------------ |
| QMapIterator<Key, T> & | **[operator=](QMapIterator.md#qmapiteratorkey-t-qmapiteratoroperatorconst-qmapkey-t-container)**(const QMap<Key, T> &*container*) |
| bool                   | **[findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)**(const T &*value*) |
| bool                   | **[findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)**(const T &*value*) |
| bool                   | **[hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)**() const |
| bool                   | **[hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)**() const |
| const Key &            | **[key](QMapIterator.md#const-key-qmapiteratorkey-const)**() const |
| QMapIterator::Item     | **[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)**()  |
| QMapIterator::Item     | **[peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)**() const |
| QMapIterator::Item     | **[peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)**() const |
| QMapIterator::Item     | **[previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)**() |
| void                   | **[toBack](QMapIterator.md#void-qmapiteratortoback)**() |
| void                   | **[toFront](QMapIterator.md#void-qmapiteratortofront)**() |
| const T &              | **[value](QMapIterator.md#const-t-qmapiteratorvalue-const)**() const |



## 详细描述

[QMap](../../M/QMap/QMap.md) 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。Java 风格迭代器比 STL 风格迭代器更高级，更容易使用；同时也略微低效。

QMapIterator<Key, T> 用来遍历 [QMap](../../M/QMap/QMap.md) (或 [QMultiMap](../../M/QMultiMap/QMultiMap.md))。如果想在遍历时修改 map，要使用 [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md)。

QMapIterator 构造函数接受 [QMap](../../M/QMap/QMap.md) 作为参数。构造后，迭代器位于 map 的最开始位置（第一个元素之前）。下面的例子演示如何顺序遍历所有元素：

```c++
QMap<int, QWidget *> map;
...
QMapIterator<int, QWidget *> i(map);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 函数返回 map 中的下一个元素并将迭代器前移。[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 和 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 函数返回跳过的最后一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素*之间*而不是直接*指向*元素。第一次调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

下面的例子演示如何反序遍历元素：

```c++
QMapIterator<int, QWidget *> i(map);
i.toBack();
while (i.hasPrevious()) {
    i.previous();
    qDebug() << i.key() << ": " << i.value();
}
```

如果想查找特定值的所有实例，循环使用 [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)() 或 [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()。例如：

```c++
QMapIterator<int, QWidget *> i(map);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

同一 map 可以使用多个迭代器。如果在 QMapIterator 处于活动状态时修改 map，QMapIterator 将继续在原 map 上遍历，而忽略修改后的副本。

**另请参阅** [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md) 和 [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md).

## 成员函数文档

### bool QMapIterator::findPrevious(const T &*value*)

从当前迭代器位置开始向后查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值，迭代器将被移动到匹配元素的前面；否则，迭代器将被移动到容器的前端。

**另请参阅** [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)()。

### bool QMapIterator::findNext(const T &*value*)

从当前迭代器位置开始向前查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值 *value*，迭代器将被移动到匹配元素的后面；否则，迭代器将被移动到容器的末端。

**另请参阅** [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()。

### const Key &QMapIterator::key() const

调用遍历函数（[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)()，[previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)()，[findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)()，[findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()）后，该函数返回跳过的最后一个元素的键。

调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 或 [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)() 后，[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 与 [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)().[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 相同。调用 [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)() 或 [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)() 后，[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 与 [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 相同。

**另请参阅** [value](QMapIterator.md#const-t-qmapiteratorvalue-const)()。

### QMapIterator::Item QMapIterator::peekPrevious() const

不移动迭代器而返回前一个元素。

对返回值调用 [key](QMapIterator.md#const-key-qmapiteratorkey-const)() 获取元素的键，调用 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 获取元素的值。

对位于容器前端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)()，[previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)() 和 [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().

### QMapIterator::Item QMapIterator::previous()

返回前一个元素并将迭代器向后移动一个位置。

对返回值调用 [key](QMapIterator.md#const-key-qmapiteratorkey-const)() 获取元素的键，调用 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 获取元素的值。

对位于容器前端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)()，[peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)() 和 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)()。

### bool QMapIterator::hasPrevious() const

如果该迭代器前面至少有一个元素，返回 `true`，即该迭代器不在容器的前端；否则返回 `false`。

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)() 和 [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)()。

### bool QMapIterator::hasNext() const

如果该迭代器后面至少有一个元素，返回 `true`，即该迭代器不在容器的末端；否则返回 `false`。

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)() 和 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)()。

### void QMapIterator::toBack()

将迭代器移动到容器的末端（最后一个元素之后）。

**另请参阅** [toFront](QMapIterator.md#void-qmapiteratortofront)() 和 [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)()。

### void QMapIterator::toFront()

将迭代器移动到容器的前端（第一个元素之前）。

**另请参阅** [toBack](QMapIterator.md#void-qmapiteratortoback)() 和 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)()。

### [QMapIterator](QMapIterator.md#qmapiteratorqmapiteratorconst-qmapkey-t-map)<Key, T> &QMapIterator::operator=(const [QMap](../../M/QMap/QMap.md)<Key, T> &*container*)

将迭代器关联到 *container* 来遍历 map。迭代器将被移动到 map 的前端（第一个元素之前）。

**另请参阅** [toFront](QMapIterator.md#void-qmapiteratortofront)() 和 [toBack](QMapIterator.md#void-qmapiteratortoback)()。

### QMapIterator::QMapIterator(const [QMap](../../M/QMap/QMap.md)<Key, T> &*map*)

构造一个迭代器来遍历 *map*。迭代器将被移动到 map 的前端（第一个元素之前）。

**另请参阅** [operator=](QMapIterator.md#qmapiteratorkey-t-qmapiteratoroperatorconst-qmapkey-t-container)()。

### QMapIterator::Item QMapIterator::next()

返回下一个元素并将迭代器向前移动一个位置。

对返回值调用 [key](QMapIterator.md#const-key-qmapiteratorkey-const)() 获取元素的键，调用 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)()，[peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)() 和 [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)()。

### QMapIterator::Item QMapIterator::peekNext() const

不移动迭代器而返回下一个元素。

对返回值调用 [key](QMapIterator.md#const-key-qmapiteratorkey-const)() 获取元素的键，调用 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)()，[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 和 [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)()。

### const T &QMapIterator::value() const

调用遍历函数（[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)()，[previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)()，[findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)()，[findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()）后，该函数返回跳过的最后一个元素的值。

调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 或 [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)() 后，value() 与 [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)().value() 相同。调用 [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)() 或 [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)() 后，value() 与 [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().value() 相同。

**另请参阅** [key](QMapIterator.md#const-key-qmapiteratorkey-const)()。