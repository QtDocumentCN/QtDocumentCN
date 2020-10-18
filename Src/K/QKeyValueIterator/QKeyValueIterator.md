# QKeyValueIterator Class

template <typename Key, typename T, typename Iterator> class QKeyValueIterator

Iterator over the key/value pairs of an associative container. [更多内容...](QKeyValueIterator.md#详细描述)

| 头文件: | #include <QKeyValueIterator> |
| -------: | :---------------------------- |
| qmake:  | QT += core                   |
| Since:  | Qt 5.10                      |

This class was introduced in Qt 5.10.

- [所有成员列表，包括继承的成员](../../K/QKeyValueIterator/QKeyValueIterator-members.md)



## 公共成员函数

|                                       | **[QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiteratoriterator-o)**(Iterator *o*) |
| -------------------------------------: | :------------------------------------------------------------ |
|                                       | **[QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)**() |
| Iterator                              | **[base](QKeyValueIterator.md#iterator-qkeyvalueiteratorbase-const)**() const |
| std::pair<Key, T>                     | **[operator\*](QKeyValueIterator.md#stdpairkey-t-qkeyvalueiteratoroperator-const)**() const |
| QKeyValueIterator<Key, T, Iterator> & | **[operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator)**() |
| QKeyValueIterator<Key, T, Iterator>   | **[operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperatorint)**(*int*) |
| QKeyValueIterator<Key, T, Iterator> & | **[operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--)**() |
| QKeyValueIterator<Key, T, Iterator>   | **[operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--int)**(*int*) |
| QKeyValueIterator::pointer            | **[operator->](QKeyValueIterator.md#qkeyvalueiteratorpointer-qkeyvalueiteratoroperator--const)**() const |



## 相关非成员函数

| bool | **[operator!=](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs)**(QKeyValueIterator<Key, T, Iterator> *lhs*, QKeyValueIterator<Key, T, Iterator> *rhs*) |
| ----: | :------------------------------------------------------------ |
| bool | **[operator==](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs-1)**(QKeyValueIterator<Key, T, Iterator> *lhs*, QKeyValueIterator<Key, T, Iterator> *rhs*) |



## 详细描述

The QKeyValueIterator class provides an STL-style iterator for returning key/value pairs from associative containers like [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) and [QMap](../../M/QMap/QMap.md). It supports the same API as the STL associative containers, i.e. getting a key/value pair when iterating through the container.

This will allow for better interoperability between [QMap](../../M/QMap/QMap.md), [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) and friends and STL-style algorithms.

**警告：** Iterators on implicitly shared containers do not work exactly like STL-iterators. You should avoid copying a container while iterators are active on that container. For more information, read [Implicit sharing iterator problem](https://doc.qt.io/qt-5/containers.html#implicit-sharing-iterator-problem).

## 成员函数文档

### QKeyValueIterator::QKeyValueIterator(Iterator *o*)

Constructs a QKeyValueIterator on top of *o*.

### QKeyValueIterator::QKeyValueIterator()

Constructs a default QKeyValueIterator.

### Iterator QKeyValueIterator::base() const

Returns the underlying iterator this [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md) is based on.

### std::pair<Key, T> QKeyValueIterator::operator*() const

Returns the current entry as a pair.

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> &QKeyValueIterator::operator++()

The prefix ++ operator (`++i`) advances the iterator to the next item in the container and returns the iterator.

**注意：** Advancing the iterator past its container's end() constitutes undefined behavior.

**另请参阅** [operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--)().

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> QKeyValueIterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`i++`) advances the iterator to the next item in the container and returns the iterator's prior value.

**注意：** Advancing the iterator past its container's end() constitutes undefined behavior.

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> &QKeyValueIterator::operator--()

The prefix -- operator (`--i`) backs the iterator up to the previous item in the container and returns the iterator.

**注意：** Backing up an iterator to before its container's begin() constitutes undefined behavior.

**另请参阅** [operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator)().

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> QKeyValueIterator::operator--(*int*)

This is an overloaded function.

The postfix -- operator (`i--`) backs the iterator up to the previous item in the container and returns the iterator's prior value.

**注意：** Backing up an iterator to before its container's begin() constitutes undefined behavior.

### QKeyValueIterator::pointer QKeyValueIterator::operator->() const

Returns the current entry as a pointer-like object to the pair.

This function was introduced in Qt 5.15.

**另请参阅** [operator*](QKeyValueIterator.md#stdpairkey-t-qkeyvalueiteratoroperator-const)().

## 相关非成员函数

### bool operator!=([QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *lhs*, [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *rhs*)

Returns `true` if *rhs* points to a different item than *lhs* otherwise returns `false`.

**另请参阅** [operator==](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs-1)().

### bool operator==([QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *lhs*, [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *rhs*)

Returns `true` if *rhs* points to the same item as *lhs* otherwise returns `false`.

**另请参阅** [operator!=](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs)().