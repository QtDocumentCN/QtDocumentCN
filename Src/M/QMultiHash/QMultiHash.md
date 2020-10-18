# QMultiHash Class

template <typename Key, typename T> class QMultiHash

The QMultiHash class is a convenience [QHash](../../H/QHash/QHash.md) subclass that provides multi-valued hashes. [更多内容...](QMultiHash.md#详细描述)

| 头文件:   | #include <QMultiHash>                      |
| ---------: | :------------------------------------------ |
| qmake:    | QT += core                                 |
| 派生类: | [QHash](../../H/QHash/QHash.md) |

- [所有成员列表，包括继承的成员](../../H/QHash/QMultiHash-members.md)

**注意：** 该类中的所有函数都是[可重入的](../../T/Threads-Reentrancy/Threads-Reentrancy.md)。



## 公共成员函数

|                                        | **[QMultiHash](QMultiHash.md#qmultihashqmultihashconst-qhashkey-t-other)**(const QHash<Key, T> &*other*) |
| --------------------------------------: | :------------------------------------------------------------ |
|                                        | **[QMultiHash](QMultiHash.md#template-typename-inputiterator-qmultihashqmultihashinputiterator-begin-inputiterator-end)**(InputIterator *begin*, InputIterator *end*) |
|                                        | **[QMultiHash](QMultiHash.md#qmultihashqmultihashstdinitializer_liststdpairkey-t--list)**(std::initializer_list<std::pair<Key, T> > *list*) |
|                                        | **[QMultiHash](QMultiHash.md#qmultihashqmultihash)**() |
| typename QHash<Key, T>::const_iterator | **[constFind](QMultiHash.md#typename-qhashkey-tconst_iterator-qmultihashconstfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| bool                                   | **[contains](QMultiHash.md#bool-qmultihashcontainsconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| int                                    | **[count](QMultiHash.md#int-qmultihashcountconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QHash<Key, T>::iterator       | **[find](QMultiHash.md#typename-qhashkey-titerator-qmultihashfindconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QHash<Key, T>::const_iterator | **[find](QMultiHash.md#typename-qhashkey-tconst_iterator-qmultihashfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QHash<Key, T>::iterator       | **[insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| int                                    | **[remove](QMultiHash.md#int-qmultihashremoveconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QHash<Key, T>::iterator       | **[replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| void                                   | **[swap](QMultiHash.md#void-qmultihashswapqmultihashk-v-other)**(QMultiHash<K, V> &*other*) |
| QList<Key>                             | **[uniqueKeys](QMultiHash.md#qlistkey-qmultihashuniquekeys-const)**() const |
| QMultiHash<K, V> &                     | **[unite](QMultiHash.md#qmultihashk-v-qmultihashuniteconst-qmultihashk-v-other)**(const QMultiHash<K, V> &*other*) |
| QList<T>                               | **[values](QMultiHash.md#qlistt-qmultihashvaluesconst-key-key-const)**(const Key &*key*) const |
| QMultiHash<K, V>                       | **[operator+](QMultiHash.md#qmultihashk-v-qmultihashoperatorconst-qmultihashk-v-other-const)**(const QMultiHash<K, V> &*other*) const |
| QMultiHash<K, V> &                     | **[operator+=](QMultiHash.md#qmultihashk-v-qmultihashoperatorconst-qmultihashk-v-other)**(const QMultiHash<K, V> &*other*) |



## 相关非成员函数

| uint | **[qHash](QMultiHash.md#template-typename-key-typename-t-uint-qhashconst-qmultihashkey-t-key-uint-seed--0)**(const QMultiHash<Key, T> &*key*, uint *seed* = 0) |
| ----: | :------------------------------------------------------------ |
|      |                                                              |



## 详细描述

QMultiHash<Key, T> is one of Qt's generic [容器类](../../C/Container_Classes/Container_Classes.md). It inherits [QHash](../../H/QHash/QHash.md) and extends it with a few convenience functions that make it more suitable than [QHash](../../H/QHash/QHash.md) for storing multi-valued hashes. A multi-valued hash is a hash that allows multiple values with the same key.

Because QMultiHash inherits [QHash](../../H/QHash/QHash.md), all of [QHash](../../H/QHash/QHash.md)'s functionality also applies to QMultiHash. For example, you can use [isEmpty](../../H/QHash/QHash.md#bool-qhashisempty-const)() to test whether the hash is empty, and you can traverse a QMultiHash using [QHash](../../H/QHash/QHash.md)'s iterator classes (for example, [QHashIterator](../../H/QHashIterator/QHashIterator.md)). But opposed to [QHash](../../H/QHash/QHash.md), it provides an [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)() function will allow the insertion of multiple items with the same key. The [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)() function corresponds to [QHash::insert](../../H/QHash/QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)(). It also provides convenient operator+() and operator+=().

Unlike [QMultiMap](../../M/QMultiMap/QMultiMap.md), QMultiHash does not provide and ordering of the inserted items. The only guarantee is that items that share the same key will appear consecutively, from the most recently to the least recently inserted value.

Example:

```
QMultiHash<QString, int> hash1, hash2, hash3;

hash1.insert("plenty", 100);
hash1.insert("plenty", 2000);
// hash1.size() == 2

hash2.insert("plenty", 5000);
// hash2.size() == 1

hash3 = hash1 + hash2;
// hash3.size() == 3
```

Unlike [QHash](../../H/QHash/QHash.md), QMultiHash provides no operator[]. Use [value](../../H/QHash/QHash.md#const-t-qhashvalueconst-key-key-const)() or [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)() if you want to access the most recently inserted item with a certain key.

If you want to retrieve all the values for a single key, you can use values(const Key &key), which returns a [QList](../../L/QList/QList.md)<T>:

```
QList<int> values = hash.values("plenty");
for (int i = 0; i < values.size(); ++i)
    cout << values.at(i) << Qt::endl;
```

The items that share the same key are available from most recently to least recently inserted.

A more efficient approach is to call [find](QMultiHash.md#typename-qhashkey-titerator-qmultihashfindconst-key-key-const-t-value)() to get the STL-style iterator for the first item with a key and iterate from there:

```
QMultiHash<QString, int>::iterator i = hash.find("plenty");
while (i != hash.end() && i.key() == "plenty") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

QMultiHash's key and value data types must be [可赋值数据类型](../../C/Container_Classes/Container_Classes.md#容器类). You cannot, for example, store a [QWidget](../../W/QWidget/QWidget.md) as a value; instead, store a [QWidget](../../W/QWidget/QWidget.md) *. In addition, QMultiHash's key type must provide operator==(), and there must also be a [qHash](../../H/QHash/QHash.md#qhash-哈希函数)() function in the type's namespace that returns a hash value for an argument of the key's type. See the [QHash](../../H/QHash/QHash.md) documentation for details.

**另请参阅** [QHash](../../H/QHash/QHash.md), [QHashIterator](../../H/QHashIterator/QHashIterator.md), [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md), and [QMultiMap](../../M/QMultiMap/QMultiMap.md).

## 成员函数文档

### QMultiHash::QMultiHash(const [QHash](../../H/QHash/QHash.md)<Key, T> &*other*)

Constructs a copy of *other* (which can be a [QHash](../../H/QHash/QHash.md) or a QMultiHash).

**另请参阅** [operator=](../../H/QHash/QHash.md#qhashk-v-qhashoperatorconst-qhashk-v-other)().

### template <typename InputIterator> QMultiHash::QMultiHash(InputIterator *begin*, InputIterator *end*)

Constructs a multi-hash with a copy of each of the elements in the iterator range [*begin*, *end*). Either the elements iterated by the range must be objects with `first` and `second` data members (like `QPair`, `std::pair`, etc.) convertible to `Key` and to `T` respectively; or the iterators must have `key()` and `value()` member functions, returning a key convertible to `Key` and a value convertible to `T` respectively.

This function was introduced in Qt 5.14.

### QMultiHash::QMultiHash(std::initializer_list<std::pair<Key, T> > *list*)

Constructs a multi-hash with a copy of each of the elements in the initializer list *list*.

This function is only available if the program is being compiled in C++11 mode.

This function was introduced in Qt 5.1.

### QMultiHash::QMultiHash()

Constructs an empty hash.

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::const_iterator QMultiHash::constFind(const Key &*key*, const T &*value*) const

Returns an iterator pointing to the item with the *key* and the *value* in the hash.

If the hash contains no such item, the function returns [constEnd](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstend-const)().

This function was introduced in Qt 4.3.

**另请参阅** [QHash::constFind](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstfindconst-key-key-const)().

### bool QMultiHash::contains(const Key &*key*, const T &*value*) const

Returns `true` if the hash contains an item with the *key* and *value*; otherwise returns `false`.

This function was introduced in Qt 4.3.

**另请参阅** [QHash::contains](../../H/QHash/QHash.md#bool-qhashcontainsconst-key-key-const)().

### int QMultiHash::count(const Key &*key*, const T &*value*) const

Returns the number of items with the *key* and *value*.

This function was introduced in Qt 4.3.

**另请参阅** [QHash::count](../../H/QHash/QHash.md#int-qhashcount-const)().

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::find(const Key &*key*, const T &*value*)

Returns an iterator pointing to the item with the *key* and *value*. If the hash contains no such item, the function returns [end](../../H/QHash/QHash.md#qhashiterator-qhashend)().

If the hash contains multiple items with the *key* and *value*, the iterator returned points to the most recently inserted item.

This function was introduced in Qt 4.3.

**另请参阅** [QHash::find](../../H/QHash/QHash.md#qhashiterator-qhashfindconst-key-key)().

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::const_iterator QMultiHash::find(const Key &*key*, const T &*value*) const

This is an overloaded function.

This function was introduced in Qt 4.3.

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::insert(const Key &*key*, const T &*value*)

Inserts a new item with the *key* and a value of *value*.

If there is already an item with the same key in the hash, this function will simply create a new one. (This behavior is different from [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)(), which overwrites the value of an existing item.)

**另请参阅** [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)().

### int QMultiHash::remove(const Key &*key*, const T &*value*)

Removes all the items that have the *key* and the value *value* from the hash. Returns the number of items removed.

This function was introduced in Qt 4.3.

**另请参阅** [QHash::remove](../../H/QHash/QHash.md#int-qhashremoveconst-key-key)().

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::replace(const Key &*key*, const T &*value*)

Inserts a new item with the *key* and a value of *value*.

If there is already an item with the *key*, that item's value is replaced with *value*.

If there are multiple items with the *key*, the most recently inserted item's value is replaced with *value*.

**另请参阅** [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)().

### void QMultiHash::swap([QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

Swaps hash *other* with this hash. This operation is very fast and never fails.

This function was introduced in Qt 4.8.

### [QList](../../L/QList/QList.md)<Key> QMultiHash::uniqueKeys() const

Returns a list containing all the keys in the map. Keys that occur multiple times in the map occur only once in the returned list.

This function was introduced in Qt 5.13.

**另请参阅** [keys](../../H/QHash/QHash.md#qlistkey-qhashkeys-const)() and [values](QMultiHash.md#qlistt-qmultihashvaluesconst-key-key-const)().

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &QMultiHash::unite(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

Inserts all the items in the *other* hash into this hash and returns a reference to this hash.

This function was introduced in Qt 5.13.

**另请参阅** [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)().

### [QList](../../L/QList/QList.md)<T> QMultiHash::values(const Key &*key*) const

This is an overloaded function.

Returns a list of all the values associated with the *key*, from the most recently inserted to the least recently inserted.

**另请参阅** [count](QMultiHash.md#int-qmultihashcountconst-key-key-const-t-value-const)() and [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)().

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> QMultiHash::operator+(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*) const

Returns a hash that contains all the items in this hash in addition to all the items in *other*. If a key is common to both hashes, the resulting hash will contain the key multiple times.

**另请参阅** [operator+=](QMultiHash.md#qmultihashk-v-qmultihashoperatorconst-qmultihashk-v-other)().

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &QMultiHash::operator+=(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

Inserts all the items in the *other* hash into this hash and returns a reference to this hash.

**另请参阅** [unite](QMultiHash.md#qmultihashk-v-qmultihashuniteconst-qmultihashk-v-other)() and [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)().

## 相关非成员函数

### template <typename Key, typename T> [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) qHash(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<Key, T> &*key*, [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

Type `T` must be supported by qHash().

This function was introduced in Qt 5.8.