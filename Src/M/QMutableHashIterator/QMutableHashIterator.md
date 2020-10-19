# QMutableHashIterator Class

template <typename Key, typename T> class QMutableHashIterator

QMutableHashIterator 类为 [QHash](../../H/QHash/QHash.md) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 Java 风格的非常量迭代器。[更多内容...](QMutableHashIterator.md#详细描述)

| 头文件: | #include <QMutableHashIterator> |
| -------: | :------------------------------- |
| qmake:  | QT += core                      |

- [所有成员列表，包括继承的成员](../../H/QHash/QMutableHashIterator-members.md)
- [废弃的成员](../../H/QHash/QMutableHashIterator-obsolete.md)



## 公共成员函数

|                                | **[QMutableHashIterator](QMutableHashIterator.md#qmutablehashiteratorqmutablehashiteratorqhashkey-t-hash)**(QHash<Key, T> &*hash*) |
| ------------------------------: | :------------------------------------------------------------ |
| QMutableHashIterator<Key, T> & | **[operator=](QMutableHashIterator.md#qmutablehashiteratorkey-t-qmutablehashiteratoroperatorqhashkey-t-container)**(QHash<Key, T> &*container*) |
| bool                           | **[findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)**(const T &*value*) |
| bool                           | **[hasNext](QMutableHashIterator.md#bool-qmutablehashiteratorhasnext-const)**() const |
| const Key &                    | **[key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)**() const |
| QMutableHashIterator::Item     | **[next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)**() |
| QMutableHashIterator::Item     | **[peekNext](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratorpeeknext-const)**() const |
| void                           | **[remove](QMutableHashIterator.md#void-qmutablehashiteratorremove)**() |
| void                           | **[setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)**(const T &*value*) |
| void                           | **[toBack](QMutableHashIterator.md#void-qmutablehashiteratortoback)**() |
| void                           | **[toFront](QMutableHashIterator.md#void-qmutablehashiteratortofront)**() |
| const T &                      | **[value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)**() const |
| T &                            | **[value](QMutableHashIterator.md#t-qmutablehashiteratorvalue)**() |



## 详细描述

[QHash](../../H/QHash/QHash.md) 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。Java 风格迭代器比 STL 风格迭代器更高级，更容易使用；同时也略微低效。

QMutableHashIterator<Key, T> 用来遍历并修改 [QHash](../../H/QHash/QHash.md) (或 [QMultiHash](../../M/QMultiHash/QMultiHash.md)) 。如果不想修改 map（或者 [QHash](../../H/QHash/QHash.md) 是 const 的），可以使用更快速的 [QHashIterator](../../H/QHashIterator/QHashIterator.md)。

QMutableHashIterator 构造函数接受 [QHash](../../H/QHash/QHash.md) 为参数。构造后，迭代器位于哈希表的最开始位置（第一个元素之前）。下面的例子演示如何顺序遍历所有元素：

```c++
QHash<int, QWidget *> hash;
...
QMutableHashIterator<QString, QWidget *> i(hash);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() 函数返回哈希表中的下一个元素并将迭代器前移。[key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() 和 [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() 函数返回跳过的最后一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素*之间*而不是直接*指向*元素。第一次调用 [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

如果想查找特定值的所有实例，循环使用 [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()。例如：

```c++
QMutableHashIterator<int, QWidget *> i(hash);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

如果想在遍历哈希表时移除元素，使用 [remove](QMutableHashIterator.md#void-qmutablehashiteratorremove)()。如果想修改元素的值，使用 [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)()。

例子：

```c++
QMutableHashIterator<QString, QString> i(hash);
while (i.hasNext()) {
    i.next();
    if (i.key() == i.value())
        i.remove();
}
```

该示例移除所有键和值相等的键值对。

任何时候，对于给定哈希表，只能有一个活动的可修改迭代器。而且，当迭代器处于活动状态时，不可以（不通过迭代器）直接修改哈希表，因为这会使迭代器失效，并导致未定义行为。

**另请参阅** [QHashIterator](../../H/QHashIterator/QHashIterator.md) 和 [QHash::iterator](../../H/QHash/QHash-iterator.md)。

## 成员函数文档

### bool QMutableHashIterator::findNext(const T &*value*)

从当前迭代器位置开始向前查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值 *value*，迭代器将被移动到匹配元素的后面；否则，迭代器将被移动到容器的末端。

### const Key &QMutableHashIterator::key() const

调用遍历函数（[next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()，[findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()）后，该函数返回跳过的最后一个元素的键。

**另请参阅** [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)()。

### T &QMutableHashIterator::value()

这是一个重载函数。

返回调用遍历函数后跳过的最后一个元素值的非常量引用。

### bool QMutableHashIterator::hasNext() const

如果该迭代器后面至少有一个元素，返回 `true`，即该迭代器不在容器的末端；否则返回 `false`。

**另请参阅** [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()。

### void QMutableHashIterator::toBack()

将迭代器移动到容器的末端（最后一个元素之后）。

**另请参阅** [toFront](QMutableHashIterator.md#void-qmutablehashiteratortofront)()。

### void QMutableHashIterator::toFront()

将迭代器移动到容器的前端（第一个元素之前）。

**另请参阅** [toBack](QMutableHashIterator.md#void-qmutablehashiteratortoback)() 和 [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()。

### [QMutableHashIterator](QMutableHashIterator.md#qmutablehashiteratorqmutablehashiteratorqhashkey-t-hash)<Key, T> &QMutableHashIterator::operator=([QHash](../../H/QHash/QHash.md)<Key, T> &*container*)

将迭代器关联到 *container* 来遍历哈希表。迭代器将被移动到哈希表的前端（第一个元素之前）。

**另请参阅** [toFront](QMutableHashIterator.md#void-qmutablehashiteratortofront)() 和 [toBack](QMutableHashIterator.md#void-qmutablehashiteratortoback)()。

### QMutableHashIterator::QMutableHashIterator([QHash](../../H/QHash/QHash.md)<Key, T> &*hash*)

构造一个迭代器来遍历 *hash*。迭代器将被移动到哈希表的前端（第一个元素之前）。

**另请参阅** [operator=](QMutableHashIterator.md#qmutablehashiteratorkey-t-qmutablehashiteratoroperatorqhashkey-t-container)()。

### QMutableHashIterator::Item QMutableHashIterator::next()

返回下一个元素并将迭代器向前移动一个位置。

对返回值调用 [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() 获取元素的键，调用 [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMutableHashIterator.md#bool-qmutablehashiteratorhasnext-const)() 和 [peekNext](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratorpeeknext-const)()。

### QMutableHashIterator::Item QMutableHashIterator::peekNext() const

不移动迭代器而返回下一个元素。

对返回值调用 [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() 获取元素的键，调用 [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QMutableHashIterator.md#bool-qmutablehashiteratorhasnext-const)() 和 [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()。

### void QMutableHashIterator::remove()

移除使用遍历函数（[next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()，[findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()）跳过的最后一个元素。

**另请参阅** [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)()。

### void QMutableHashIterator::setValue(const T &*value*)

用 *value* 替换使用遍历函数跳过的最后一个元素的值。

遍历函数包括 [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() 和 [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()。

**另请参阅** [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)()，[value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() 和 [remove](QMutableHashIterator.md#void-qmutablehashiteratorremove)()。

### const T &QMutableHashIterator::value() const

调用遍历函数（[next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)()，[findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()）后，该函数返回跳过的最后一个元素的值。

**另请参阅** [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() 和 [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)()。