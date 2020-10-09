# QMutableMapIterator 类

template <typename Key, typename T> class QMutableMapIterator

QMutableMapIterator 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 Java 风格的非常量类型迭代器。[更多...](QMutableMapIterator.md#详细描述)

| 头文件: | #include <QMutableMapIterator> |
| ------: | ------------------------------ |
|  qmake: | QT += core                     |

- [所有成员列表，包括继承的成员](../../M/QMap/qmutablemapiterator-members.md)



## 公共成员函数

|                               | **[QMutableMapIterator](QMutableMapIterator.md#qmutablemapiteratorqmutablemapiteratorqmapkey-t-map)**(QMap<Key, T> &*map*) |
| ----------------------------- | ------------------------------------------------------------ |
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

[QMap](../../M/QMap/QMap.md) 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。Java 风格迭代器比 STL 风格迭代器更高级，更容易使用；t同时也略微低效。

QMutableMapIterator<Key, T> 用来遍历并修改 [QMap](../../M/QMap/QMap.md) (或 [QMultiMap](../../M/QMultiMap/QMultiMap.md)) 。如果不想修改 map（或者 [QMap](../../M/QMap/QMap.md) 是 const 的），可以使用更快速的 [QMapIterator](../../M/QMapIterator/QMapIterator.md)。

QMutableMapIterator 构造函数接受 [QMap](../../M/QMap/QMap.md) 作为参数。构造后，迭代器位于 map 的最开始位置（第一个元素之前）。下面的例子演示如何按顺序遍历所有元素：

```c++
QMap<int, QWidget *> map;
...
QMutableMapIterator<int, QWidget *> i(map);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

[next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 函数返回 map 中的下一个元素并将迭代器前移。[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() 函数返回刚刚跳过去的上一个元素的键和值。

与 STL 风格迭代器不同，Java 风格迭代器指向元素之间而不是直接指向元素。第一次调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 前移迭代器到第一个和第二个元素之间的位置，并返回第一个元素；第二次调用 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() 前移迭代器到第二个和第三个元素之间的位置；以此类推。

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

如果想查找特定值的所有实例，在循环中使用 [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 或 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()。例如：

```c++
QMutableMapIterator<int, QWidget *> i(map);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

如果想在遍历 map 时移除元素，使用 [remove](QMutableMapIterator.md#void-qmutablemapiteratorremove)()。如果想修改元素的值，使用[setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)()。

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

**另请参阅** [QMapIterator](../../M/QMapIterator/QMapIterator.md) and [QMap::iterator](https://doc.qt.io/qt-5/qmap-iterator.html).

## 成员函数文档

### bool QMutableMapIterator::findPrevious(const T &*value*)

Searches for *value* starting from the current iterator position backward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just before the matching item; otherwise, the iterator is positioned at the front of the container.

**另请参阅** [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)().

### bool QMutableMapIterator::findNext(const T &*value*)

Searches for *value* starting from the current iterator position forward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just after the matching item; otherwise, the iterator is positioned at the back of the container.

**另请参阅** [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)().

### const Key &QMutableMapIterator::key() const

Returns the key of the last item that was jumped over using one of the traversal functions ([next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)(), [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)(), [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)(), [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()).

After a call to [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() or [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)(), [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() is equivalent to [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)().[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)(). After a call to [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() or [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)(), [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() is equivalent to [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)().[key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)().

**另请参阅** [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)().

### T &QMutableMapIterator::value()

This is an overloaded function.

Returns a non-const reference to the value of the last item that was jumped over using one of the traversal functions.

### QMutableMapIterator::Item QMutableMapIterator::peekPrevious() const

Returns the previous item without moving the iterator.

Call [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() on the return value to obtain the item's key 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the front of the container leads to undefined results.

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)(), [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() 和 [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)().

### QMutableMapIterator::Item QMutableMapIterator::previous()

Returns the previous item and moves the iterator back by one position.

Call [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() on the return value to obtain the item's key 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the front of the container leads to undefined results.

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)(), [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)() 和 [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)().

### bool QMutableMapIterator::hasPrevious() const

Returns `true` if there is at least one item behind the iterator, i.e. the iterator is *not* at the front of the container; otherwise returns `false`.

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)() and [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)().

### bool QMutableMapIterator::hasNext() const

Returns `true` if there is at least one item ahead of the iterator, i.e. the iterator is *not* at the back of the container; otherwise returns `false`.

**另请参阅** [hasPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorhasprevious-const)() and [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)().

### void QMutableMapIterator::toBack()

Moves the iterator to the back of the container (after the last item).

**另请参阅** [toFront](QMutableMapIterator.md#void-qmutablemapiteratortofront)() and [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)().

### void QMutableMapIterator::toFront()

Moves the iterator to the front of the container (before the first item).

**另请参阅** [toBack](QMutableMapIterator.md#void-qmutablemapiteratortoback)() and [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)().

### [QMutableMapIterator](QMutableMapIterator.md#qmutablemapiteratorqmutablemapiteratorqmapkey-t-map)<Key, T> &QMutableMapIterator::operator=([QMap](../../M/QMap/QMap.md)<Key, T> &*container*)

Makes the iterator operate on *map*. The iterator is set to be at the front of the map (before the first item).

**另请参阅** [toFront](QMutableMapIterator.md#void-qmutablemapiteratortofront)() and [toBack](QMutableMapIterator.md#void-qmutablemapiteratortoback)().

### QMutableMapIterator::QMutableMapIterator([QMap](../../M/QMap/QMap.md)<Key, T> &*map*)

Constructs an iterator for traversing *map*. The iterator is set to be at the front of the map (before the first item).

**另请参阅** [operator=](QMutableMapIterator.md#qmutablemapiteratorkey-t-qmutablemapiteratoroperatorqmapkey-t-container)().

### QMutableMapIterator::Item QMutableMapIterator::next()

Returns the next item and advances the iterator by one position.

Call [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() on the return value to obtain the item's key 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)(), [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)()和 [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)().

### QMutableMapIterator::Item QMutableMapIterator::peekNext() const

Returns a reference to the next item without moving the iterator.

Call [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() on the return value to obtain the item's key 和 [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMutableMapIterator.md#bool-qmutablemapiteratorhasnext-const)(), [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)()和 [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)().

### void QMutableMapIterator::remove()

Removes the last item that was jumped over using one of the traversal functions ([next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)(), [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)(), [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)(), [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()).

**另请参阅** [setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)().

### void QMutableMapIterator::setValue(const T &*value*)

Replaces the value of the last item that was jumped over using one of the traversal functions with *value*.

The traversal functions are [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)(), [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)(), [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)() 和 [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)().

**另请参阅** [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)(), [value](QMutableMapIterator.md#const-t-qmutablemapiteratorvalue-const)()和 [remove](QMutableMapIterator.md#void-qmutablemapiteratorremove)().

### const T &QMutableMapIterator::value() const

Returns the value of the last item that was jumped over using one of the traversal functions ([next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)(), [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)(), [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)(), [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)()).

After a call to [next](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratornext)() or [findNext](QMutableMapIterator.md#bool-qmutablemapiteratorfindnextconst-t-value)(), value() is equivalent to [peekPrevious](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeekprevious-const)().value(). After a call to [previous](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorprevious)() or [findPrevious](QMutableMapIterator.md#bool-qmutablemapiteratorfindpreviousconst-t-value)(), value() is equivalent to [peekNext](QMutableMapIterator.md#qmutablemapiteratoritem-qmutablemapiteratorpeeknext-const)().value().

**另请参阅** [key](QMutableMapIterator.md#const-key-qmutablemapiteratorkey-const)() and [setValue](QMutableMapIterator.md#void-qmutablemapiteratorsetvalueconst-t-value)().