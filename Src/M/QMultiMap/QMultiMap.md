# QMultiMap Class

template <typename Key, typename T> class QMultiMap

QMultiMap 类是一个便利的 [QMap](../../M/QMap/QMap.md) 派生类，提供多值映射功能。[更多内容...](QMultiMap.md#详细描述)

| 头文件: | #include <QMultiMap>         |
| ------: | :---------------------------- |
|  qmake: | QT += core                   |
|   基类: | [QMap](../../M/QMap/QMap.md) |

- [所有成员列表，包括继承的成员](../../M/QMultiMap/QMultiMap-members.md)

**注意：** 该类中的所有函数都是[可重入的](../../T/Threads-Reentrancy/Threads-Reentrancy.md)。



## 公共成员函数

|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimapconst-qmapkey-t-other)**(const QMap<Key, T> &*other*) |
| -------------------------------------: | :------------------------------------------------------------ |
|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimapstdinitializerliststdpairkey-t--list)**(std::initializer_list<std::pair<Key, T> > *list*) |
|                                       | **[QMultiMap](QMultiMap.md#qmultimapqmultimap)**()           |
| typename QMap<Key, T>::const_iterator | **[constFind](QMultiMap.md#typename-qmapkey-tconst_iterator-qmultimapconstfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| bool                                  | **[contains](QMultiMap.md#bool-qmultimapcontainsconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| int                                   | **[count](QMultiMap.md#int-qmultimapcountconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QMap<Key, T>::iterator       | **[find](QMultiMap.md#typename-qmapkey-titerator-qmultimapfindconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::const_iterator | **[find](QMultiMap.md#typename-qmapkey-tconst_iterator-qmultimapfindconst-key-key-const-t-value-const)**(const Key &*key*, const T &*value*) const |
| typename QMap<Key, T>::iterator       | **[insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::iterator       | **[insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinserttypename-qmapkey-tconst_iterator-pos-const-key-key-const-t-value)**(typename QMap<Key, T>::const_iterator *pos*, const Key &*key*, const T &*value*) |
| int                                   | **[remove](QMultiMap.md#int-qmultimapremoveconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| typename QMap<Key, T>::iterator       | **[replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
| void                                  | **[swap](QMultiMap.md#void-qmultimapswapqmultimapkey-t-other)**(QMultiMap<Key, T> &*other*) |
| QList<Key>                            | **[uniqueKeys](QMultiMap.md#qlistkey-qmultimapuniquekeys-const)**() const |
| QMultiMap<K, V> &                     | **[unite](QMultiMap.md#qmultimapk-v-qmultimapuniteconst-qmultimapk-v-other)**(const QMultiMap<K, V> &*other*) |
| QList<T>                              | **[values](QMultiMap.md#qlistt-qmultimapvaluesconst-key-key-const)**(const Key &*key*) const |
| QMultiMap<K, V>                       | **[operator+](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other-const)**(const QMultiMap<K, V> &*other*) const |
| QMultiMap<K, V> &                     | **[operator+=](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other)**(const QMultiMap<K, V> &*other*) |



## 详细描述

QMultiMap<Key, T> 是一种 Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)。它继承 [QMap](../../M/QMap/QMap.md) 并扩展了一些功能，使之可以存储多值映射。多值映射是一种允许将多个值关联到同一个键的映射；[QMap](../../M/QMap/QMap.md) 不允许多值映射。

因为 QMultiMap 继承 [QMap](../../M/QMap/QMap.md)，所有  [QMap](../../M/QMap/QMap.md) 的功能也适用于 QMultiMap。例如，可以使用 [isEmpty](../../M/QMap/QMap.md#bool-qmapisempty-const)() 测试 map 是否为空，可以使用 [QMap](../../M/QMap/QMap.md) 的迭代器类（例如 [QMapIterator](../../M/QMapIterator/QMapIterator.md)）遍历 QMultiMap。除此之外，它还提供 [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)() 函数来插入值，如果要插入的键已经存在，该函数不会覆盖已有的值，而 [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)() 函数则不同，如果 map 中已经存在要插入的键，该函数会覆盖已经存在的值。此外，该类还提供方便的 operator+() 和 operator+=() 运算符。

例子：

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

与 [QMap](../../M/QMap/QMap.md) 不同，QMultiMap 不提供 operator[] 运算符。如果想用特定键访问最新插入的元素，使用 [value](../../M/QMap/QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() 或 [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)()。

如果想取得单个键关联的所有值，可以使用 values(const Key &key)，该函数返回一个 [QList](../../L/QList/QList.md)<T>：

```c++
QList<int> values = map.values("plenty");
for (int i = 0; i < values.size(); ++i)
    cout << values.at(i) << Qt::endl;
```

共享同一键的元素按照从最新到最早插入的顺序返回。

如果习惯用 STL 风格迭代器，可以传递键调用 [find](QMultiMap.md#typename-qmapkey-titerator-qmultimapfindconst-key-key-const-t-value)() 取得第一个元素的迭代器，从该元素开始遍历：

```c++
QMultiMap<QString, int>::iterator i = map.find("plenty");
while (i != map.end() && i.key() == "plenty") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

QMultiMap 键和值的数据类型必须是[可赋值数据类型](../../C/Container_Classes/Container_Classes.md#容器类)。这涵盖了大多数可能会遇到的数据类型，但是编译器不会允许存储类似 [QWidget](../../W/QWidget/QWidget.md) 这样的对象作为值，应该存储 [QWidget](../../W/QWidget/QWidget.md) *。另外，QMultiMap 的键类型必须提供 operator<() 运算符。 具体请参考 [QMap](../../M/QMap/QMap.md) 文档。

**另请参阅** [QMap](../../M/QMap/QMap.md)，[QMapIterator](../../M/QMapIterator/QMapIterator.md)，[QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md)。

## 成员函数文档

### QMultiMap::QMultiMap(const [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T> &*other*)

构造一个 *other* 的副本（可能是一个 [QMap](../../M/QMap/QMap.md) 或 QMultiMap）。

**另请参阅** [operator=](../../M/QMap/QMap.md#qmapkey-t-qmapoperatorconst-qmapkey-t-other)()。

### QMultiMap::QMultiMap(std::initializer_list<std::pair<Key, T> > *list*)

用初始化列表 *list* 中每个元素的副本构造一个 multi-map。

只有当程序在 C++11 模式下编译时，该函数才可用。

Qt 5.1 中引入该函数。

### QMultiMap::QMultiMap()

构造一个空 map。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator QMultiMap::constFind(const Key &*key*, const T &*value*) const

返回迭代器，指向 map 中键为 *key*，值为 *value* 的元素。

如果 map 中不包含这样的元素，该函数返回 [constEnd](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstend-const)()。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::constFind](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstfindconst-key-key-const)().

### bool QMultiMap::contains(const Key &*key*, const T &*value*) const

如果该 map 包含键为 *key*，值为 *value* 的元素，返回 `true`；否则返回 `false`。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::contains](../../M/QMap/QMap.md#bool-qmapcontainsconst-key-key-const)()。

### int QMultiMap::count(const Key &*key*, const T &*value*) const

返回键为 *key*，值为 *value* 的元素个数。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::count](../../M/QMap/QMap.md#int-qmapcount-const)()。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::find(const Key &*key*, const T &*value*)

返回迭代器，指向 map 中键为 *key*，值为 *value* 的元素。

如果 map 中不包含这样的元素，该函数返回 [end](../../M/QMap/QMap.md#qmapiterator-qmapend)()。

如果 map 包含多个键为 *key* （译者注：以及值为 *value*）的元素，函数返回指向最新插入的那个值的迭代器。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)()。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator QMultiMap::find(const Key &*key*, const T &*value*) const

这是一个重载函数。

返回常量迭代器，指向 map 中键为 *key*，值为 *value* 的元素。

如果 map 中不包含这样的元素，该函数返回 [end](../../M/QMap/QMap.md#qmapiterator-qmapend)()。

如果 map 包含多个键为 *key*（译者注：以及值为 *value*）的元素，函数返回指向最新插入的那个值的常量迭代器。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)()。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::insert(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果 map 中已经存在相同键的元素，该函数将创建一个新元素。（这与 [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)() 不同，replace() 是覆盖已经存在元素的值。)

**另请参阅** [replace](QMultiMap.md#typename-qmapkey-titerator-qmultimapreplaceconst-key-key-const-t-value)()。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::insert(typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::const_iterator *pos*, const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素，*pos* 用来提示插入位置。

如果以 [constBegin](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstbegin-const)() 作为插入位置提示，表明 *key* 比 map 中的任何键都小，而 [constEnd](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstend-const)() 则建议 *key* 大于 map 中的任何键。否则提示应该满足条件 (*pos* - 1).[key](../../M/QMap/QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)() < *key* <= pos.[key](../../M/QMap/QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)()。如果提示 *pos* 是错误的，其将被忽略，并以常规方式插入。

如果 map 中已经存在相同键的元素，该函数将创建一个新元素。

**注意：** 需小心对待提示。提供从旧的共享实例取得的迭代器可能引起崩溃，还会有默默污染 map 和 *pos* 的 map 的风险。

Qt 5.1 中引入该函数。

### int QMultiMap::remove(const Key &*key*, const T &*value*)

从 map 中移除所有键为 *key*，值为 *value* 的元素。返回被移除元素的个数。

Qt 4.3 中引入该函数。

**另请参阅** [QMap::remove](../../M/QMap/QMap.md#int-qmapremoveconst-key-key)()。

### typename [QMap](../../M/QMap/QMap.md#qmapqmap)<Key, T>::iterator QMultiMap::replace(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果已经存在键为 *key* 的元素，该元素的值将被 *value* 替换。

如果有多个键为 *key* 的元素，最新插入的元素的值将被 *value* 替换。

**另请参阅** [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)()。

### void QMultiMap::swap([QMultiMap](QMultiMap.md#qmultimapqmultimap)<Key, T> &*other*)

将 map *other* 与本 map 交换。该操作非常快，永远不失败。

Qt 4.8 中引入该函数。

### [QList](../../L/QList/QList.md)<Key> QMultiMap::uniqueKeys() const

以升序返回 map 中所有键的列表。在 map 中多次出现的键在返回的列表中只出现一次。

Qt 4.2 中引入该函数。

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &QMultiMap::unite(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*)

将 *other* map 中的所有元素插入到本 map 中。如果一个键在两个 map 中同时存在，结果 map 将多次包含这个键。

### [QList](../../L/QList/QList.md)<T> QMultiMap::values(const Key &*key*) const

按照从最新到最早插入的顺序，返回所有与键 *key* 相关联的值的列表。

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> QMultiMap::operator+(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*) const

返回一个 map，该 map 包含本 map 和 *other* map 中的所有元素。如果一个键在两个 map 中同时存在，结果 map 将多次包含这个键。

**另请参阅** [operator+=](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other)()。

### [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &QMultiMap::operator+=(const [QMultiMap](QMultiMap.md#qmultimapqmultimap)<K, V> &*other*)

将 *other* map 中的所有元素插入到本 map 中，返回本 map 的引用。

**另请参阅** [insert](QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)() 和 [operator+](QMultiMap.md#qmultimapk-v-qmultimapoperatorconst-qmultimapk-v-other-const)()。