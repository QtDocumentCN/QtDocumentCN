# QMultiHash 类

template <typename Key, typename T> class QMultiHash

QMultiHash 类是一个便利的 [QHash](../../H/QHash/QHash.md) 派生类，提供多值哈希表功能。[更多内容...](QMultiHash.md#详细描述)

| 头文件:   | #include <QMultiHash>                      |
| ---------: | :------------------------------------------ |
| qmake:    | QT += core                                 |
| 基类: | [QHash](../../H/QHash/QHash.md) |

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

QMultiHash<Key, T> 是一种 Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)。它继承 [QHash](../../H/QHash/QHash.md) 并扩展了一些便利的功能，使之比 [QHash](../../H/QHash/QHash.md) 更适合存储多值哈希。多值哈希是一种允许将多个值关联到同一个键的哈希。

因为 QMultiHash 继承 [QHash](../../H/QHash/QHash.md)，所有 [QHash](../../H/QHash/QHash.md) 的功能也适用于 QMultiHash。例如，可以使用 [isEmpty](../../H/QHash/QHash.md#bool-qhashisempty-const)() 测试哈希表是否为空，可以使用 [QHash](../../H/QHash/QHash.md) 的迭代器类（例如 [QHashIterator](../../H/QHashIterator/QHashIterator.md)）遍历 QMultiHash。但是与 [QHash](../../H/QHash/QHash.md) 不同，QMultiHash 提供的 [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)() 函数允许同一个键插入多个元素。而 [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)() 函数对应于 [QHash::insert](../../H/QHash/QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)()。此外，该类还提供便利的 operator+() 和 operator+=() 运算符。

与 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 不同，QMultiHash 不对插入的元素排序。唯一的保证是共享同一键的元素将按照从最新到最早插入的顺序连续出现。

例子：

```c++
QMultiHash<QString, int> hash1, hash2, hash3;

hash1.insert("plenty", 100);
hash1.insert("plenty", 2000);
// hash1.size() == 2

hash2.insert("plenty", 5000);
// hash2.size() == 1

hash3 = hash1 + hash2;
// hash3.size() == 3
```

与 [QHash](../../H/QHash/QHash.md) 不同，QMultiHash 不提供 operator[] 运算符。如果想用特定键访问最新插入的元素，使用 [value](../../H/QHash/QHash.md#const-t-qhashvalueconst-key-key-const)() 或 [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)()。

如果想取得单个键关联的所有值，可以使用 values(const Key &key)，该函数返回一个 [QList](../../L/QList/QList.md)<T>：

```c++
QList<int> values = hash.values("plenty");
for (int i = 0; i < values.size(); ++i)
    cout << values.at(i) << Qt::endl;
```

共享同一键的元素按照从最新到最早插入的顺序返回。

更有效的方法是传递键调用 [find](QMultiHash.md#typename-qhashkey-titerator-qmultihashfindconst-key-key-const-t-value)() 取得第一个元素的 STL 风格迭代器，从该元素开始遍历：

```c++
QMultiHash<QString, int>::iterator i = hash.find("plenty");
while (i != hash.end() && i.key() == "plenty") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

QMultiHash 键和值的数据类型必须是[可赋值数据类型](../../C/Container_Classes/Container_Classes.md#容器类)。不能存储类似 [QWidget](../../W/QWidget/QWidget.md) 这样的对象作为值；应该存储 [QWidget](../../W/QWidget/QWidget.md) *。另外，QMultiHash 的键类型必须提供 operator==() 运算符， 并且在键类型的命名空间内还必须有一个为键类型参数返回哈希值的 [qHash](../../H/QHash/QHash.md#qhash-哈希函数)() 函数。具体请参考 [QHash](../../H/QHash/QHash.md) 文档。

**另请参阅** [QHash](../../H/QHash/QHash.md)，[QHashIterator](../../H/QHashIterator/QHashIterator.md)，[QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md)。

## 成员函数文档

### QMultiHash::QMultiHash(const [QHash](../../H/QHash/QHash.md)<Key, T> &*other*)

构造一个 *other* 的副本（可能是一个 [QHash](../../H/QHash/QHash.md) 或 QMultiHash）。

**另请参阅** [operator=](../../H/QHash/QHash.md#qhashk-v-qhashoperatorconst-qhashk-v-other)()。

### template <typename InputIterator> QMultiHash::QMultiHash(InputIterator *begin*, InputIterator *end*)

用迭代器范围 [*begin*, *end*) 内每个元素的副本构造一个多值哈希表。需要满足下列两个条件之一：迭代范围内的元素是包含 `first` 和 `second` 数据成员的对象（像 `QPair`，`std::pair`等），分别可以转换为 `Key` 类型和 `T` 类型；或者迭代器必须含有 `key()` 和 `value()` 成员函数，分别返回可以转换为 `Key` 类型的键 `T` 类型的值。

Qt 5.14 中引入该函数。

### QMultiHash::QMultiHash(std::initializer_list<std::pair<Key, T> > *list*)

用初始化列表 *list* 中每个元素的副本构造一个哈希表。

只有当程序在 C++11 模式下编译时，该函数才可用。

Qt 5.1 中引入该函数。

### QMultiHash::QMultiHash()

构造一个空哈希表。

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::const_iterator QMultiHash::constFind(const Key &*key*, const T &*value*) const

返回迭代器，指向哈希表中键为 *key*，值为 *value* 的元素。

如果哈希表中不包含这样的元素，该函数返回 [constEnd](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstend-const)()。

Qt 4.3 中引入该函数。

**另请参阅** [QHash::constFind](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstfindconst-key-key-const)().

### bool QMultiHash::contains(const Key &*key*, const T &*value*) const

如果该哈希表包含键为 *key*，值为 *value* 的元素，返回 `true`；否则返回 `false`。

Qt 4.3 中引入该函数。

**另请参阅** [QHash::contains](../../H/QHash/QHash.md#bool-qhashcontainsconst-key-key-const)().

### int QMultiHash::count(const Key &*key*, const T &*value*) const

返回键为 *key*，值为 *value* 的元素个数。

Qt 4.3 中引入该函数。

**另请参阅** [QHash::count](../../H/QHash/QHash.md#int-qhashcount-const)().

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::find(const Key &*key*, const T &*value*)

返回迭代器，指向键为 *key*，值为 *value* 的元素。如果哈希表中不包含这样的元素，该函数返回 [end](../../H/QHash/QHash.md#qhashiterator-qhashend)()。

如果哈希表包含多个键为 *key*，值为 *value* 的元素，迭代器指向最新插入的元素。

Qt 4.3 中引入该函数。

**另请参阅** [QHash::find](../../H/QHash/QHash.md#qhashiterator-qhashfindconst-key-key)().

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::const_iterator QMultiHash::find(const Key &*key*, const T &*value*) const

这是一个重载函数。

Qt 4.3 中引入该函数。

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::insert(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果哈希表中已经存在相同键的元素，该函数将创建一个新元素。（这与 [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)() 不同，replace() 是覆盖已经存在元素的值。)

**另请参阅** [replace](QMultiHash.md#typename-qhashkey-titerator-qmultihashreplaceconst-key-key-const-t-value)()。

### int QMultiHash::remove(const Key &*key*, const T &*value*)

从哈希表中移除所有键为 *key*，值为 *value* 的元素。返回被移除元素的个数。

Qt 4.3 中引入该函数。

**另请参阅** [QHash::remove](../../H/QHash/QHash.md#int-qhashremoveconst-key-key)()。

### typename [QHash](../../H/QHash/QHash.md)<Key, T>::iterator QMultiHash::replace(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果已经存在键为 *key* 的元素，该元素的值将被 *value* 替换。

如果有多个键为 *key* 的元素，最新插入的元素的值将被 *value* 替换。

**另请参阅** [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)()。

### void QMultiHash::swap([QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

将 *other* 哈希表与本哈希表。该操作非常快，永远不失败。

Qt 4.8 中引入该函数。

### [QList](../../L/QList/QList.md)<Key> QMultiHash::uniqueKeys() const

以升序返回哈希表中所有键的列表。在哈希表中多次出现的键在返回的列表中只出现一次。

Qt 5.13 中引入该函数。

**另请参阅** [keys](../../H/QHash/QHash.md#qlistkey-qhashkeys-const)() 和 [values](QMultiHash.md#qlistt-qmultihashvaluesconst-key-key-const)()。

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &QMultiHash::unite(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

将 *other* 哈希表中的所有元素插入到本哈希表中，返回本哈希表的引用。

Qt 5.13 中引入该函数。

**另请参阅** [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)()。

### [QList](../../L/QList/QList.md)<T> QMultiHash::values(const Key &*key*) const

这是一个重载函数。

按照从最新到最早插入的顺序，返回所有与键 *key* 相关联的值的列表。

**另请参阅** [count](QMultiHash.md#int-qmultihashcountconst-key-key-const-t-value-const)() 和 [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)().

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> QMultiHash::operator+(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*) const

返回一个哈希表，该哈希表包含本哈希表和 *other* 哈希表中的所有元素。如果一个键在两个哈希表中同时存在，结果哈希表将多次包含这个键。

**另请参阅** [operator+=](QMultiHash.md#qmultihashk-v-qmultihashoperatorconst-qmultihashk-v-other)()。

### [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &QMultiHash::operator+=(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<K, V> &*other*)

将 *other* 哈希表中的所有元素插入到本哈希表中，返回本哈希表的引用。

**另请参阅** [unite](QMultiHash.md#qmultihashk-v-qmultihashuniteconst-qmultihashk-v-other)() 和 [insert](QMultiHash.md#typename-qhashkey-titerator-qmultihashinsertconst-key-key-const-t-value)()。

## 相关非成员函数

### template <typename Key, typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QMultiHash](QMultiHash.md#qmultihashqmultihash)<Key, T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

类型 `T` 必须被 qHash() 支持。

Qt 5.8 中引入该函数。