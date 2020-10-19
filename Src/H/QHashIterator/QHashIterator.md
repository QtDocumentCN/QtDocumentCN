# QHashIterator Class

template <typename Key, typename T> class QHashIterator

QHashIterator 类为 [QHash](../../H/QHash/QHash.md) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 Java 风格的常量迭代器。[更多内容...](QHashIterator.md#详细描述)

| 头文件: | #include <QHashIterator> |
| -------: | :------------------------ |
| qmake:  | QT += core               |

- [所有成员列表，包括继承的成员](../../H/QHash/QHashIterator-members.md)
- [废弃的成员](../../H/QHash/QHashIterator-obsolete.md)



## 公共成员函数

|                         | **[QHashIterator](QHashIterator.md#qhashiteratorqhashiteratorconst-qhashkey-t-hash)**(const QHash<Key, T> &*hash*) |
| -----------------------: | :------------------------------------------------------------ |
| QHashIterator<Key, T> & | **[operator=](QHashIterator.md#qhashiteratorkey-t-qhashiteratoroperatorconst-qhashkey-t-container)**(const QHash<Key, T> &*container*) |
| bool                    | **[findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)**(const T &*value*) |
| bool                    | **[hasNext](QHashIterator.md#bool-qhashiteratorhasnext-const)**() const |
| const Key &             | **[key](QHashIterator.md#const-key-qhashiteratorkey-const)**() const |
| QHashIterator::Item     | **[next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)**() |
| QHashIterator::Item     | **[peekNext](QHashIterator.md#qhashiteratoritem-qhashiteratorpeeknext-const)**() const |
| void                    | **[toBack](QHashIterator.md#void-qhashiteratortoback)**() |
| void                    | **[toFront](QHashIterator.md#void-qhashiteratortofront)**() |
| const T &               | **[value](QHashIterator.md#const-t-qhashiteratorvalue-const)**() const |



## 详细描述

[QHash](../../H/QHash/QHash.md) 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。Java 风格迭代器比 STL 风格迭代器更高级，更容易使用；同时也略微低效。

QHashIterator<Key, T> 用来遍历 [QHash](../../H/QHash/QHash.md) (或 [QMultiHash](../../M/QMultiHash/QMultiHash.md))。如果想在遍历时修改哈希表，要使用  [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md)。

QHashIterator 构造函数接受 [QHash](../../H/QHash/QHash.md) 作为参数。构造后，迭代器位于哈希表的最开始位置（第一个元素之前）。下面的例子演示如何顺序遍历所有元素：

```c++
QHash<int, QWidget *> hash;
...
QHashIterator<int, QWidget *> i(hash);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() 函数返回哈希表中的下一个元素并将迭代器前移。[key](QHashIterator.md#const-key-qhashiteratorkey-const)() 和 [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() 函数返回跳过的最后一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素*之间*而不是直接*指向*元素。第一次调用 [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

如果想查找特定值的所有实例，循环使用 [findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)()。例如：

```c++
QHashIterator<int, QWidget *> i(hash);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

同一哈希表可以使用多个迭代器。如果在 QHashIterator处于活动状态时修改哈希表，QHashIterator 将继续在原哈希表上遍历，而忽略修改后的副本。

**另请参阅** [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md) 和 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md).

## 成员函数文档

### bool QHashIterator::findNext(const T &*value*)

从当前迭代器位置开始向前查找值 *value*。如果找到值为 *value* 的键值对，返回 `true`；否则返回 `false`。

调用该函数后，如果找到值 *value*，迭代器将被移动到匹配元素的后面；否则，迭代器将被移动到容器的末端。

### const Key &QHashIterator::key() const

调用遍历函数（([next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)()，[findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)()）后，该函数返回跳过的最后一个元素的键。

**另请参阅** [value](QHashIterator.md#const-t-qhashiteratorvalue-const)()。

### bool QHashIterator::hasNext() const

如果该迭代器后面至少有一个元素，返回 `true`，即该迭代器不在容器的末端；否则返回 `false`。

**另请参阅** [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)()。

### void QHashIterator::toBack()

将迭代器移动到容器的末端（最后一个元素之后）。

**另请参阅** [toFront](QHashIterator.md#void-qhashiteratortofront)()。

### void QHashIterator::toFront()

将迭代器移动到容器的前端（第一个元素之前）。

**另请参阅** [toBack](QHashIterator.md#void-qhashiteratortoback)() 和 [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)()。

### [QHashIterator](QHashIterator.md#qhashiteratorqhashiteratorconst-qhashkey-t-hash)<Key, T> &QHashIterator::operator=(const [QHash](../../H/QHash/QHash.md)<Key, T> &*container*)

将迭代器关联到 *container* 来遍历哈希表。迭代器将被移动到哈希表的前端（第一个元素之前）。

**另请参阅** [toFront](QHashIterator.md#void-qhashiteratortofront)() 和 [toBack](QHashIterator.md#void-qhashiteratortoback)()。

### QHashIterator::QHashIterator(const [QHash](../../H/QHash/QHash.md)<Key, T> &*hash*)

构造一个迭代器来遍历 *hash*。迭代器将被移动到哈希表的前端（第一个元素之前）。

**另请参阅** [operator=](QHashIterator.md#qhashiteratorkey-t-qhashiteratoroperatorconst-qhashkey-t-container)()。

### QHashIterator::Item QHashIterator::next()

返回下一个元素并将迭代器向前移动一个位置。

对返回值调用 [key](QHashIterator.md#const-key-qhashiteratorkey-const)() 获取元素的键，调用 [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QHashIterator.md#bool-qhashiteratorhasnext-const)() 和 [peekNext](QHashIterator.md#qhashiteratoritem-qhashiteratorpeeknext-const)()。

### QHashIterator::Item QHashIterator::peekNext() const

不移动迭代器而返回下一个元素。

对返回值调用 [key](QHashIterator.md#const-key-qhashiteratorkey-const)() 获取元素的键，调用 [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() 获取元素的值。

对位于容器末端的迭代器调用该函数将导致未定义结果。

**另请参阅** [hasNext](QHashIterator.md#bool-qhashiteratorhasnext-const)() 和 [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)(。

### const T &QHashIterator::value() const

调用遍历函数（[next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)()，[findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)()）后，该函数返回跳过的最后一个元素的值。

**另请参阅** [key](QHashIterator.md#const-key-qhashiteratorkey-const)()。