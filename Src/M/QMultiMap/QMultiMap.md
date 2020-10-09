# QMultiMap Class

template <typename Key, typename T> class QMultiMap

QMultiMap 类是 [QMap](../../M/QMap/QMap.md) 的派生类，提供多值映射机能。[更多...](QMultiMap.md#详细描述)

| 头文件: | #include <QMultiMap>         |
| ------: | ---------------------------- |
|  qmake: | QT += core                   |
|   基类: | [QMap](../../M/QMap/QMap.md) |

- [所有成员列表，包括继承的成员](../../M/QMultiMap/qmultimap-members.md)

**注意：**该类中的所有函数都是[可重入的](../../T/Threads-Reentrancy/Threads-Reentrancy.md)。



## 公共成员函数

|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimapconst-qmapkey-t-other)**(const QMap<Key, T> &*other*) |
| ------------------------------------- | ------------------------------------------------------------ |
|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimapstdinitializerliststdpairkey-t--list)**(std::initializer_list<std::pair<Key, T> > *list*) |
|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimap)**() |
| typename QMap<Key, T>::const_iterator | **[constFind](QMultiMap.md#typename-qmapkey-tconstiterator-qmultimapconstfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| bool                                  | **[contains](QMultiMap.md#bool-qmultimapcontainsconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| int                                   | **[count](QMultiMap.md#int-qmultimapcountconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QMap<Key, T>::iterator       | **[find](QMultiMap.md#typename-qmapkey-titerator-qmultimapfindconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::const_iterator | **[find](QMultiMap.md#typename-qmapkey-tconstiterator-qmultimapfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QMap<Key, T>::iterator       | **[insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::iterator       | **[insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinserttypename-qmapkey-tconstiterator-pos-const-key-key-const-t-value)**(typename QMap<Key, T>::const_iterator *pos*, const Key &*key*, const T &*value*) |
| int                                   | **[remove](QMultiMap.md#int-qmultimapremoveconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::iterator       | **[replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| void                                  | **[swap](QMultiMap.md#void-qmultimapswapqmultimapkey-t-other)**(QMultiMap<Key, T> &*other*) |
| QList<Key>                            | **[uniqueKeys](QMultiMap.md#qlistkey-qmultimapuniquekeys-const)**() const |
| QMultiMap<K, V> &                     | **[unite](QMultiMap.md#qmultimapk-v-qmultimapuniteconst-qmultimapk-v-other)**(const QMultiMap<K, V> &*other*) |
| QList<T>                              | **[values](QMultiMap.md#qlistt-qmultimapvaluesconst-key-key-const)**(const Key &*key*) const |
| QMultiMap<K, V>                       | **[operator+](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other-const)**(const QMultiMap<K, V> &*other*) const |
| QMultiMap<K, V> &                     | **[operator+=](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other)**(const QMultiMap<K, V> &*other*) |



## 详细描述

QMultiMap<Key, T> 是一种 Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)。它继承 [QMap](../../M/QMap/QMap.md) 并扩展了若干功能，使之可以存储多值映射。多值映射是一种允许将多个值关联到同一个键的映射；[QMap](../../M/QMap/QMap.md) 不允许多值映射。

因为 QMultiMap 继承 [QMap](../../M/QMap/QMap.md)，所有  [QMap](../../M/QMap/QMap.md) 的功能也适用于 QMultiMap。例如，可以使用 [isEmpty](../../M/QMap/QMap.md#bool-qmapisempty-const)() 测试 map 是否为空，可以使用 [QMap](../../M/QMap/QMap.md)的迭代器类（例如 [QMapIterator](../../M/QMapIterator/QMapIterator.md)）遍历 QMultiMap。除此之外，它还提供一种 [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)() 函数，可以插入但不会覆盖属于同一键的之前插入的值。and a [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)() function that corresponds which does overwite an existing value if they key is already in the map. It also provides convenient operator+() and operator+=().

Example:

```c++
QMultiMap<QString, int> map1, map2, map3;

map1.insert("plenty", 100);
map1.insert("plenty", 2000);
// map1.size() == 2

map2.insert("plenty", 5000);
// map2.size() == 1

map3 = map1 + map2;
// map3.size() == 3
```

Unlike [QMap](../../M/QMap/QMap.md), QMultiMap provides no operator[]. Use [value](../../M/QMap/QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() or [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)() if you want to access the most recently inserted item with a certain key.

If you want to retrieve all the values for a single key, you can use values(const Key &key), which returns a [QList](../../L/QList/QList.md)<T>:

```c++
QList<int> values = map.values("plenty");
for (int i = 0; i < values.size(); ++i)
    cout << values.at(i) << Qt::endl;
```

The items that share the same key are available from most recently to least recently inserted.

If you prefer the STL-style iterators, you can call [find](QMultiMap.md#typename-qmapkey-titerator-qmultimapfindconst-key-key-const-t-value)() to get the iterator for the first item with a key and iterate from there:

```c++
QMultiMap<QString, int>::iterator i = map.find("plenty");
while (i != map.end() && i.key() == "plenty") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

QMultiMap's key and value data types must be [assignable data types](https://doc.qt.io/qt-5/containers.html#assignable-data-types). This covers most data types you are likely to encounter, but the compiler won't let you, for example, store a [QWidget](../../W/QWidget/QWidget.md) as a value; instead, store a [QWidget](../../W/QWidget/QWidget.md) *. In addition, QMultiMap's key type must provide operator<(). See the [QMap](../../M/QMap/QMap.md) documentation for details.

**另请参阅** [QMap](../../M/QMap/QMap.md), [QMapIterator](../../M/QMapIterator/QMapIterator.md), [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md), and [QMultiHash](../../M/QMultiHash/QMultiHash.md).

## Member Function Documentation

### QMultiMap::QMultiMap(const [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T> &*other*)

Constructs a copy of *other* (which can be a [QMap](../../M/QMap/QMap.md) or a QMultiMap).

**另请参阅** [operator=](../../M/QMap/QMap.md#qmapkey-t-qmapoperatorconst-qmapkey-t-other)().

### QMultiMap::QMultiMap(std::initializer_list<std::pair<Key, T> > *list*)

Constructs a multi-map with a copy of each of the elements in the initializer list *list*.

This function is only available if the program is being compiled in C++11 mode.

This function was introduced in Qt 5.1.

### QMultiMap::QMultiMap()

Constructs an empty map.

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator QMultiMap::constFind(const Key &*key*, const T &*value*) const

Returns an iterator pointing to the item with key *key* and the value *value* in the map.

If the map contains no such item, the function returns [constEnd](../../M/QMap/QMap.md#qmapconstiterator-qmapconstend-const)().

This function was introduced in Qt 4.3.

**另请参阅** [QMap::constFind](../../M/QMap/QMap.md#qmapconstiterator-qmapconstfindconst-key-key-const)().

### bool QMultiMap::contains(const Key &*key*, const T &*value*) const

Returns `true` if the map contains an item with key *key* and value *value*; otherwise returns `false`.

This function was introduced in Qt 4.3.

**另请参阅** [QMap::contains](../../M/QMap/QMap.md#bool-qmapcontainsconst-key-key-const)().

### int QMultiMap::count(const Key &*key*, const T &*value*) const

Returns the number of items with key *key* and value *value*.

This function was introduced in Qt 4.3.

**另请参阅** [QMap::count](../../M/QMap/QMap.md#int-qmapcount-const)().

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::find(const Key &*key*, const T &*value*)

Returns an iterator pointing to the item with key *key* and value *value* in the map.

If the map contains no such item, the function returns [end](../../M/QMap/QMap.md#qmapiterator-qmapend)().

If the map contains multiple items with key *key*, this function returns an iterator that points to the most recently inserted value.

This function was introduced in Qt 4.3.

**另请参阅** [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)().

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator QMultiMap::find(const Key &*key*, const T &*value*) const

This is an overloaded function.

Returns a const iterator pointing to the item with the given *key* and *value* in the map.

If the map contains no such item, the function returns [end](../../M/QMap/QMap.md#qmapiterator-qmapend)().

If the map contains multiple items with the specified *key*, this function returns a const iterator that points to the most recently inserted value.

This function was introduced in Qt 4.3.

**另请参阅** [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)().

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::insert(const Key &*key*, const T &*value*)

Inserts a new item with the key *key* and a value of *value*.

If there is already an item with the same key in the map, this function will simply create a new one. (This behavior is different from [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)(), which overwrites the value of an existing item.)

**另请参阅** [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)().

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::insert(typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator *pos*, const Key &*key*, const T &*value*)

Inserts a new item with the key *key* and value *value* and with hint *pos* suggesting where to do the insert.

If [constBegin](../../M/QMap/QMap.md#qmapconstiterator-qmapconstbegin-const)() is used as hint it indicates that the *key* is less than any key in the map while [constEnd](../../M/QMap/QMap.md#qmapconstiterator-qmapconstend-const)() suggests that the *key* is larger than any key in the map. Otherwise the hint should meet the condition (*pos* - 1).[key](../../M/QMap/QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)() < *key* <= pos.[key](../../M/QMap/QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)(). If the hint *pos* is wrong it is ignored and a regular insert is done.

If there is already an item with the same key in the map, this function will simply create a new one.

**Note:** Be careful with the hint. Providing an iterator from an older shared instance might crash but there is also a risk that it will silently corrupt both the map and the *pos* map.

This function was introduced in Qt 5.1.

### int QMultiMap::remove(const Key &*key*, const T &*value*)

Removes all the items that have the key *key* and the value *value* from the map. Returns the number of items removed.

This function was introduced in Qt 4.3.

**另请参阅** [QMap::remove](../../M/QMap/QMap.md#int-qmapremoveconst-key-key)().

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::replace(const Key &*key*, const T &*value*)

Inserts a new item with the key *key* and a value of *value*.

If there is already an item with the key *key*, that item's value is replaced with *value*.

If there are multiple items with the key *key*, the most recently inserted item's value is replaced with *value*.

**另请参阅** [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)().

### void QMultiMap::swap([QMultiMap](QMultiMap.md#qmultimapqmultimap)<Key, T> &*other*)

Swaps map *other* with this map. This operation is very fast and never fails.

This function was introduced in Qt 4.8.

### [QList](../../L/QList/QList.md)<Key> QMultiMap::uniqueKeys() const

Returns a list containing all the keys in the map in ascending order. Keys that occur multiple times in the map occur only once in the returned list.

This function was introduced in Qt 4.2.

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &QMultiMap::unite(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*)

Inserts all the items in the *other* map into this map. If a key is common to both maps, the resulting map will contain the key multiple times.

### [QList](../../L/QList/QList.md)<T> QMultiMap::values(const Key &*key*) const

Returns a list containing all the values associated with key *key*, from the most recently inserted to the least recently inserted one.

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> QMultiMap::operator+(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*) const

Returns a map that contains all the items in this map in addition to all the items in *other*. If a key is common to both maps, the resulting map will contain the key multiple times.

**另请参阅** [operator+=](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other)().

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &QMultiMap::operator+=(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*)

Inserts all the items in the *other* map into this map and returns a reference to this map.

**另请参阅** [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)() and [operator+](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other-const)().