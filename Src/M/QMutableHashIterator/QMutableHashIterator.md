# QMutableHashIterator Class

template <typename Key, typename T> class QMutableHashIterator

The QMutableHashIterator class provides a Java-style non-const iterator for [QHash](../../H/QHash/QHash.md) and [QMultiHash](../../M/QMultiHash/QMultiHash.md). [更多内容...](QMutableHashIterator.md#详细描述)

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

[QHash](../../H/QHash/QHash.md) has both [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) and [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器). The Java-style iterators are more high-level and easier to use than the STL-style iterators; on the other hand, they are slightly less efficient.

QMutableHashIterator<Key, T> allows you to iterate over a [QHash](../../H/QHash/QHash.md) (or a [QMultiHash](../../M/QMultiHash/QMultiHash.md)) and modify the hash. If you don't want to modify the hash (or have a const [QHash](../../H/QHash/QHash.md)), use the slightly faster [QHashIterator](../../H/QHashIterator/QHashIterator.md) instead.

The QMutableHashIterator constructor takes a [QHash](../../H/QHash/QHash.md) as argument. After construction, the iterator is located at the very beginning of the hash (before the first item). Here's how to iterate over all the elements sequentially:

```
QHash<int, QWidget *> hash;
...
QMutableHashIterator<QString, QWidget *> i(hash);
while (i.hasNext()) {
    i.next();
    qDebug() << i.key() << ": " << i.value();
}
```

The [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() function returns the next item in the hash and advances the iterator. The [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() and [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() functions return the key and value of the last item that was jumped over.

Unlike STL-style iterators, Java-style iterators point *between* items rather than directly *at* items. The first call to [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() advances the iterator to the position between the first and second item, and returns the first item; the second call to [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() advances the iterator to the position between the second and third item; and so on.

![img](https://doc.qt.io/qt-5/images/javaiterators1.png)

If you want to find all occurrences of a particular value, use [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)() in a loop. For example:

```
QMutableHashIterator<int, QWidget *> i(hash);
while (i.findNext(widget)) {
    qDebug() << "Found widget " << widget << " under key "
             << i.key();
}
```

If you want to remove items as you iterate over the hash, use [remove](QMutableHashIterator.md#void-qmutablehashiteratorremove)(). If you want to modify the value of an item, use [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)().

Example:

```
QMutableHashIterator<QString, QString> i(hash);
while (i.hasNext()) {
    i.next();
    if (i.key() == i.value())
        i.remove();
}
```

The example removes all (key, value) pairs where the key and the value are the same.

Only one mutable iterator can be active on a given hash at any time. Furthermore, no changes should be done directly to the hash while the iterator is active (as opposed to through the iterator), since this could invalidate the iterator and lead to undefined behavior.

**另请参阅** [QHashIterator](../../H/QHashIterator/QHashIterator.md) and [QHash::iterator](../../H/QHash/QHash-iterator.md).

## 成员函数文档

### bool QMutableHashIterator::findNext(const T &*value*)

Searches for *value* starting from the current iterator position forward. Returns `true` if a (key, value) pair with value *value* is found; otherwise returns `false`.

After the call, if *value* was found, the iterator is positioned just after the matching item; otherwise, the iterator is positioned at the back of the container.

### const Key &QMutableHashIterator::key() const

Returns the key of the last item that was jumped over using one of the traversal functions ([next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)(), [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()).

**另请参阅** [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)().

### T &QMutableHashIterator::value()

This is an overloaded function.

Returns a non-const reference to the value of the last item that was jumped over using one of the traversal functions.

### bool QMutableHashIterator::hasNext() const

Returns `true` if there is at least one item ahead of the iterator, i.e. the iterator is *not* at the back of the container; otherwise returns `false`.

**另请参阅** [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)().

### void QMutableHashIterator::toBack()

Moves the iterator to the back of the container (after the last item).

**另请参阅** [toFront](QMutableHashIterator.md#void-qmutablehashiteratortofront)().

### void QMutableHashIterator::toFront()

Moves the iterator to the front of the container (before the first item).

**另请参阅** [toBack](QMutableHashIterator.md#void-qmutablehashiteratortoback)() and [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)().

### [QMutableHashIterator](QMutableHashIterator.md#qmutablehashiteratorqmutablehashiteratorqhashkey-t-hash)<Key, T> &QMutableHashIterator::operator=([QHash](../../H/QHash/QHash.md)<Key, T> &*container*)

Makes the iterator operate on *hash*. The iterator is set to be at the front of the hash (before the first item).

**另请参阅** [toFront](QMutableHashIterator.md#void-qmutablehashiteratortofront)() and [toBack](QMutableHashIterator.md#void-qmutablehashiteratortoback)().

### QMutableHashIterator::QMutableHashIterator([QHash](../../H/QHash/QHash.md)<Key, T> &*hash*)

Constructs an iterator for traversing *hash*. The iterator is set to be at the front of the hash (before the first item).

**另请参阅** [operator=](QMutableHashIterator.md#qmutablehashiteratorkey-t-qmutablehashiteratoroperatorqhashkey-t-container)().

### QMutableHashIterator::Item QMutableHashIterator::next()

Returns the next item and advances the iterator by one position.

Call [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() on the return value to obtain the item's key, and [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMutableHashIterator.md#bool-qmutablehashiteratorhasnext-const)() and [peekNext](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratorpeeknext-const)().

### QMutableHashIterator::Item QMutableHashIterator::peekNext() const

Returns a reference to the next item without moving the iterator.

Call [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() on the return value to obtain the item's key, and [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)() to obtain the value.

Calling this function on an iterator located at the back of the container leads to undefined results.

**另请参阅** [hasNext](QMutableHashIterator.md#bool-qmutablehashiteratorhasnext-const)() and [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)().

### void QMutableHashIterator::remove()

Removes the last item that was jumped over using one of the traversal functions ([next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)(), [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()).

**另请参阅** [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)().

### void QMutableHashIterator::setValue(const T &*value*)

Replaces the value of the last item that was jumped over using one of the traversal functions with *value*.

The traversal functions are [next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)() and [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)().

**另请参阅** [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)(), [value](QMutableHashIterator.md#const-t-qmutablehashiteratorvalue-const)(), and [remove](QMutableHashIterator.md#void-qmutablehashiteratorremove)().

### const T &QMutableHashIterator::value() const

Returns the value of the last item that was jumped over using one of the traversal functions ([next](QMutableHashIterator.md#qmutablehashiteratoritem-qmutablehashiteratornext)(), [findNext](QMutableHashIterator.md#bool-qmutablehashiteratorfindnextconst-t-value)()).

**另请参阅** [key](QMutableHashIterator.md#const-key-qmutablehashiteratorkey-const)() and [setValue](QMutableHashIterator.md#void-qmutablehashiteratorsetvalueconst-t-value)().