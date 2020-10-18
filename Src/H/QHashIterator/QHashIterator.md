# QHashIterator Class

template <typename Key, typename T> class QHashIterator

The QHashIterator class provides a Java-style const iterator for [QHash](../../H/QHash/QHash.md) and [QMultiHash](../../M/QMultiHash/QMultiHash.md). [更多内容...](QHashIterator.md#详细描述)

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

[QHash](../../H/QHash/QHash.md) has both [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) and [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器). The Java-style iterators are more high-level and easier to use than the STL-style iterators; on the other hand, they are slightly less efficient.

QHashIterator<Key, T> allows you to iterate over a [QHash](../../H/QHash/QHash.md) (or a [QMultiHash](../../M/QMultiHash/QMultiHash.md)). If you want to modify the hash as you iterate over it, use [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md) instead.

The QHashIterator constructor takes a [QHash](../../H/QHash/QHash.md) as argument. After construction, the iterator is located at the very beginning of the hash (before the first item). Here's how to iterate over all the elements sequentially:

```
QHash<int, QWidget *> hash;
...
QHashIterator<int, QWidget *> i(hash);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

The [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() function returns the next item in the hash and advances the iterator. The [key](QHashIterator.md#const-key-qhashiteratorkey-const)() and [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() functions return the key and value of the last item that was jumped over.

Unlike STL-style iterators, Java-style iterators point *between* items rather than directly *at* items. The first call to [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() advances the iterator to the position between the first and second item, and returns the first item; the second call to [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)() advances the iterator to the position between the second and third item; and so on.

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

If you want to find all occurrences of a particular value, use [findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)() in a loop. For example:

```
QHashIterator<int, QWidget *> i(hash);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

Multiple iterators can be used on the same hash. If the hash is modified while a QHashIterator is active, the QHashIterator will continue iterating over the original hash, ignoring the modified copy.

**另请参阅** [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md) and [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md).

## 成员函数文档

### bool QHashIterator::findNext(const T &*value*)

Searches for *value* starting from the current iterator position forward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just after the matching item; otherwise, the iterator is positioned at the back of the container.

### const Key &QHashIterator::key() const

Returns the key of the last item that was jumped over using one of the traversal functions ([next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)(), [findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)()).

**另请参阅** [value](QHashIterator.md#const-t-qhashiteratorvalue-const)().

### bool QHashIterator::hasNext() const

Returns `true` if there is at least one item ahead of the iterator, i.e. the iterator is *not* at the back of the container; otherwise returns `false`.

**另请参阅** [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)().

### void QHashIterator::toBack()

Moves the iterator to the back of the container (after the last item).

**另请参阅** [toFront](QHashIterator.md#void-qhashiteratortofront)().

### void QHashIterator::toFront()

Moves the iterator to the front of the container (before the first item).

**另请参阅** [toBack](QHashIterator.md#void-qhashiteratortoback)() and [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)().

### [QHashIterator](QHashIterator.md#qhashiteratorqhashiteratorconst-qhashkey-t-hash)<Key, T> &QHashIterator::operator=(const [QHash](../../H/QHash/QHash.md)<Key, T> &*container*)

Makes the iterator operate on *hash*. The iterator is set to be at the front of the hash (before the first item).

**另请参阅** [toFront](QHashIterator.md#void-qhashiteratortofront)() and [toBack](QHashIterator.md#void-qhashiteratortoback)().

### QHashIterator::QHashIterator(const [QHash](../../H/QHash/QHash.md)<Key, T> &*hash*)

Constructs an iterator for traversing *hash*. The iterator is set to be at the front of the hash (before the first item).

**另请参阅** [operator=](QHashIterator.md#qhashiteratorkey-t-qhashiteratoroperatorconst-qhashkey-t-container)().

### QHashIterator::Item QHashIterator::next()

Returns the next item and advances the iterator by one position.

Call [key](QHashIterator.md#const-key-qhashiteratorkey-const)() on the return value to obtain the item's key, and [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QHashIterator.md#bool-qhashiteratorhasnext-const)() and [peekNext](QHashIterator.md#qhashiteratoritem-qhashiteratorpeeknext-const)().

### QHashIterator::Item QHashIterator::peekNext() const

Returns the next item without moving the iterator.

Call [key](QHashIterator.md#const-key-qhashiteratorkey-const)() on the return value to obtain the item's key, and [value](QHashIterator.md#const-t-qhashiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QHashIterator.md#bool-qhashiteratorhasnext-const)() and [next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)().

### const T &QHashIterator::value() const

Returns the value of the last item that was jumped over using one of the traversal functions ([next](QHashIterator.md#qhashiteratoritem-qhashiteratornext)(), [findNext](QHashIterator.md#bool-qhashiteratorfindnextconst-t-value)()).

**另请参阅** [key](QHashIterator.md#const-key-qhashiteratorkey-const)().