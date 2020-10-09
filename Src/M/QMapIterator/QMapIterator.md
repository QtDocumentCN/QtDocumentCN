# QMapIterator 类

template <typename Key, typename T> class QMapIterator

QMapIterator 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 Java 风格的常量类型迭代器。[更多...](QMapIterator.md#详细描述)

| 头文件: | #include <QMapIterator> |
| ------: | ----------------------- |
|  qmake: | QT += core              |

- [所有成员列表，包括继承的成员](../../M/QMap/qmapiterator-members.md)



## 公共成员函数

|                        | **[QMapIterator](QMapIterator.md#qmapiteratorqmapiteratorconst-qmapkey-t-map)**(const QMap<Key, T> &*map*) |
| ---------------------- | ------------------------------------------------------------ |
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

QMapIterator 构造函数接受 [QMap](../../M/QMap/QMap.md) 作为参数。构造后，迭代器位于 map 的最开始位置（第一个元素之前）。下面的例子演示如何按顺序遍历所有元素：

```c++
QMap<int, QWidget *> map;
...
QMapIterator<int, QWidget *> i(map);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 函数返回 map 中的下一个元素并将迭代器前移。[key](QMapIterator.md#const-key-qmapiteratorkey-const)() 和 [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() 函数返回刚刚跳过去的上一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素之间而不是直接指向元素。第一次调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

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

如果想查找特定值的所有实例，在循环中使用 [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)() 或 [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()。例如：

```c++
QMapIterator<int, QWidget *> i(map);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

同一 map 可以使用多个迭代器。如果在 QMapIterator 处于活动状态时修改 map，QMapIterator 将继续在原 map 上遍历，并忽略修改后的副本。

**另请参阅** [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md) and [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md).

## 成员函数文档

### bool QMapIterator::findPrevious(const T &*value*)

Searches for *value* starting from the current iterator position backward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just before the matching item; otherwise, the iterator is positioned at the front of the container.

**另请参阅** [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)().

### bool QMapIterator::findNext(const T &*value*)

Searches for *value* starting from the current iterator position forward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just after the matching item; otherwise, the iterator is positioned at the back of the container.

**另请参阅** [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)().

### const Key &QMapIterator::key() const

Returns the key of the last item that was jumped over using one of the traversal functions ([next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)(), [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)(), [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)(), [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()).

After a call to [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() or [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)(), [key](QMapIterator.md#const-key-qmapiteratorkey-const)() is equivalent to [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)().[key](QMapIterator.md#const-key-qmapiteratorkey-const)(). After a call to [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)() or [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)(), [key](QMapIterator.md#const-key-qmapiteratorkey-const)() is equivalent to [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().[key](QMapIterator.md#const-key-qmapiteratorkey-const)().

**另请参阅** [value](QMapIterator.md#const-t-qmapiteratorvalue-const)().

### QMapIterator::Item QMapIterator::peekPrevious() const

Returns the previous item without moving the iterator.

Call [key](QMapIterator.md#const-key-qmapiteratorkey-const)() on the return value to obtain the item's key, and [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the front of the container leads to undefined results.

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)(), [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)(), and [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().

### QMapIterator::Item QMapIterator::previous()

Returns the previous item and moves the iterator back by one position.

Call [key](QMapIterator.md#const-key-qmapiteratorkey-const)() on the return value to obtain the item's key, and [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the front of the container leads to undefined results.

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)(), [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)(), and [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)().

### bool QMapIterator::hasPrevious() const

Returns `true` if there is at least one item behind the iterator, i.e. the iterator is *not* at the front of the container; otherwise returns `false`.

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)() and [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)().

### bool QMapIterator::hasNext() const

Returns `true` if there is at least one item ahead of the iterator, i.e. the iterator is *not* at the back of the container; otherwise returns `false`.

**另请参阅** [hasPrevious](QMapIterator.md#bool-qmapiteratorhasprevious-const)() and [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)().

### void QMapIterator::toBack()

Moves the iterator to the back of the container (after the last item).

**另请参阅** [toFront](QMapIterator.md#void-qmapiteratortofront)() and [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)().

### void QMapIterator::toFront()

Moves the iterator to the front of the container (before the first item).

**另请参阅** [toBack](QMapIterator.md#void-qmapiteratortoback)() and [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)().

### [QMapIterator](QMapIterator.md#qmapiteratorqmapiteratorconst-qmapkey-t-map)<Key, T> &QMapIterator::operator=(const [QMap](../../M/QMap/QMap.md)<Key, T> &*container*)

Makes the iterator operate on *map*. The iterator is set to be at the front of the map (before the first item).

**另请参阅** [toFront](QMapIterator.md#void-qmapiteratortofront)() and [toBack](QMapIterator.md#void-qmapiteratortoback)().

### QMapIterator::QMapIterator(const [QMap](../../M/QMap/QMap.md)<Key, T> &*map*)

Constructs an iterator for traversing *map*. The iterator is set to be at the front of the map (before the first item).

**另请参阅** [operator=](QMapIterator.md#qmapiteratorkey-t-qmapiteratoroperatorconst-qmapkey-t-container)().

### QMapIterator::Item QMapIterator::next()

Returns the next item and advances the iterator by one position.

Call [key](QMapIterator.md#const-key-qmapiteratorkey-const)() on the return value to obtain the item's key, and [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)(), [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)(), and [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)().

### QMapIterator::Item QMapIterator::peekNext() const

Returns the next item without moving the iterator.

Call [key](QMapIterator.md#const-key-qmapiteratorkey-const)() on the return value to obtain the item's key, and [value](QMapIterator.md#const-t-qmapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMapIterator.md#bool-qmapiteratorhasnext-const)(), [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)(), and [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)().

### const T &QMapIterator::value() const

Returns the value of the last item that was jumped over using one of the traversal functions ([next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)(), [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)(), [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)(), [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)()).

After a call to [next](QMapIterator.md#qmapiteratoritem-qmapiteratornext)() or [findNext](QMapIterator.md#bool-qmapiteratorfindnextconst-t-value)(), value() is equivalent to [peekPrevious](QMapIterator.md#qmapiteratoritem-qmapiteratorpeekprevious-const)().value(). After a call to [previous](QMapIterator.md#qmapiteratoritem-qmapiteratorprevious)() or [findPrevious](QMapIterator.md#bool-qmapiteratorfindpreviousconst-t-value)(), value() is equivalent to [peekNext](QMapIterator.md#qmapiteratoritem-qmapiteratorpeeknext-const)().value().

**另请参阅** [key](QMapIterator.md#const-key-qmapiteratorkey-const)().