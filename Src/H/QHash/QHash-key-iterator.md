# key_iterator Class

class [QHash](https://doc.qt.io/qt-5/qhash.html#qhash)::key_iterator

The [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) class provides an STL-style const iterator for [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) and [QMultiHash](../../M/QMultiHash/QMultiHash.md) keys. [更多内容...](QHash-key-iterator.md#详细描述)

This class was introduced in Qt 5.6.

- [所有成员列表，包括继承的成员](https://doc.qt.io/qt-5/qhash-key-iterator-members.html)
- [废弃的成员](https://doc.qt.io/qt-5/qhash-key-iterator-obsolete.html)



## 公共成员函数

| const_iterator | **[base](QHash-key-iterator.md#const_iterator-key_iteratorbase-const)**() const |
| --------------: | :------------------------------------------------------------ |
| bool           | **[operator!=](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)**(key_iterator *other*) const |
| const Key &    | **[operator\*](QHash-key-iterator.md#const-key-key_iteratoroperator-const)**() const |
| key_iterator & | **[operator++](QHash-key-iterator.md#key_iterator-key_iteratoroperator)**() |
| key_iterator   | **[operator++](QHash-key-iterator.md#key_iterator-key_iteratoroperatorint)**(*int*) |
| const Key *    | **[operator->](QHash-key-iterator.md#const-key-key_iteratoroperator-const)**() const |
| bool           | **[operator==](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)**(key_iterator *other*) const |



## 详细描述

[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) is essentially the same as [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) with the difference that operator*() and operator->() return a key instead of a value.

For most uses [QHash::iterator](../../H/QHash/QHash-iterator.md) and [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) should be used, you can easily access the key by calling [QHash::iterator::key](https://doc.qt.io/qt-5/qhash-iterator.html#key)():

```
for (QHash<int, QString>::const_iterator it = hash.cbegin(), end = hash.cend(); it != end; ++it) {
    cout << "The key: " << it.key() << Qt::endl
    cout << "The value: " << it.value() << Qt::endl;
    cout << "Also the value: " << (*it) << Qt::endl;
}
```

However, to have interoperability between [QHash](https://doc.qt.io/qt-5/qhash.html#qhash)'s keys and STL-style algorithms we need an iterator that dereferences to a key instead of a value. With [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) we can apply an algorithm to a range of keys without having to call [QHash::keys](../../H/QHash/QHash.md#qlistkey-qhashkeys-const)(), which is inefficient as it costs one [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) iteration and memory allocation to create a temporary [QList](../../L/QList/QList.md).

```
// Inefficient, keys() is expensive
QList<int> keys = hash.keys();
int numPrimes = std::count_if(keys.cbegin(), keys.cend(), isPrimeNumber);
qDeleteAll(hash2.keys());

// Efficient, no memory allocation needed
int numPrimes = std::count_if(hash.keyBegin(), hash.keyEnd(), isPrimeNumber);
qDeleteAll(hash2.keyBegin(), hash2.keyEnd());
```

[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) is const, it's not possible to modify the key.

The default [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) constructor creates an uninitialized iterator. You must initialize it using a [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) function like [QHash::keyBegin](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeybegin-const)() or [QHash::keyEnd](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeyend-const)().

**警告：** Iterators on implicitly shared containers do not work exactly like STL-iterators. You should avoid copying a container while iterators are active on that container. For more information, read [Implicit sharing iterator problem](https://doc.qt.io/qt-5/containers.html#implicit-sharing-iterator-problem).

**另请参阅** [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) and [QHash::iterator](../../H/QHash/QHash-iterator.md).

## 成员函数文档

### [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html) key_iterator::base() const

Returns the underlying [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html) this [key_iterator](https://doc.qt.io/qt-5/qhash-key-iterator.html) is based on.

### bool key_iterator::operator!=(key_iterator *other*) const

Returns `true` if *other* points to a different item than this iterator; otherwise returns `false`.

**另请参阅** [operator==](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)().

### const Key &key_iterator::operator*() const

Returns the current item's key.

### key_iterator &key_iterator::operator++()

The prefix ++ operator (`++i`) advances the iterator to the next item in the hash and returns an iterator to the new current item.

Calling this function on [QHash::keyEnd](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeyend-const)() leads to undefined results.

**另请参阅** [operator--](https://doc.qt.io/qt-5/qhash-key-iterator-obsolete.html#operator--)().

### key_iterator key_iterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`i++`) advances the iterator to the next item in the hash and returns an iterator to the previous item.

### const Key *key_iterator::operator->() const

Returns a pointer to the current item's key.

### bool key_iterator::operator==(key_iterator *other*) const

Returns `true` if *other* points to the same item as this iterator; otherwise returns `false`.

**另请参阅** [operator!=](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)().