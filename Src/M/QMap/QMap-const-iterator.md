# const_iterator 类

class [QMap](../../M/QMap/QMap.md)::const_iterator

[QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 STL 风格的常量迭代器。[更多内容...](QMap-const-iterator.md#详细描述)

- [所有成员列表，包括继承的成员](../../M/QMap/QMap-const-iterator-members.md)



## 公共成员类型

| typedef | **[iterator_category](QMap-const-iterator.md#typedef-const_iteratoriterator_category)** |
| -------: | :------------------------------------------------------------ |
|         |                                                              |



## 公共成员函数

|                  | **[const_iterator](QMap-const-iterator.md#const_iteratorconst_iteratorconst-iterator-other)**(const iterator &*other*) |
| ----------------: | :------------------------------------------------------------ |
|                  | **[const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator)**() |
| const Key &      | **[key](QMap-const-iterator.md#const-key-const_iteratorkey-const)**() const |
| const T &        | **[value](QMap-const-iterator.md#const-t-const_iteratorvalue-const)**() const |
| bool             | **[operator!=](QMap-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const)**(const const_iterator &*other*) const |
| const T &        | **[operator\*](QMap-const-iterator.md#const-t-const_iteratoroperator-const)**() const |
| const_iterator   | **[operator+](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint-j-const)**(int *j*) const |
| const_iterator & | **[operator++](QMap-const-iterator.md#const_iterator-const_iteratoroperator)**() |
| const_iterator   | **[operator++](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint)**(*int*) |
| const_iterator & | **[operator+=](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint-j)**(int *j*) |
| const_iterator   | **[operator-](QMap-const-iterator.md#const_iterator-const_iteratoroperator-int-j-const)**(int *j*) const |
| const_iterator & | **[operator--](QMap-const-iterator.md#const_iterator-const_iteratoroperator--)**() |
| const_iterator   | **[operator--](QMap-const-iterator.md#const_iterator-const_iteratoroperator--int)**(*int*) |
| const_iterator & | **[operator-=](QMap-const-iterator.md#const_iterator-const_iteratoroperator-int-j)**(int *j*) |
| const T *        | **[operator->](QMap-const-iterator.md#const-t-const_iteratoroperator--const)**() const |
| bool             | **[operator==](QMap-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const-1)**(const const_iterator &*other*) const |



## 详细描述

[QMap](../../M/QMap/QMap.md) 同时提供 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)和 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)。STL 风格迭代器更底层，使用更笨拙；同时也稍快一些。对于已经了解 STL 的开发者来说更加熟悉。

[QMap](../../M/QMap/QMap.md)<Key, T>::const_iterator 用来遍历 [QMap](../../M/QMap/QMap.md)（或[QMultiMap](../../M/QMultiMap/QMultiMap.md)）。如果想在遍历时修改 [QMap](../../M/QMap/QMap.md)，必须使用[QMap::iterator](../../M/QMap/QMap-iterator.md)。对于非常量 [QMap](../../M/QMap/QMap.md)，使用 [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 通常是好的编程实践，除非需要在遍历时改变 [QMap](../../M/QMap/QMap.md)。const 迭代器稍快一些并可以提高代码可读性。

[QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 的默认构造函数创建一个未初始化的迭代器。必须在开始遍历前使用 [QMap::constBegin](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstbegin-const)()，[QMap::constEnd](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstend-const)() 或 [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)() 等 [QMap](../../M/QMap/QMap.md) 函数初始化它。下面是一个典型的循环，该循环打印出 map 中的所有键值对：

```c++
QMap<QString, int> map;
map.insert("January", 1);
map.insert("February", 2);
...
map.insert("December", 12);

QMap<QString, int>::const_iterator i;
for (i = map.constBegin(); i != map.constEnd(); ++i)
    cout << i.key() << ": " << i.value() << Qt::endl;
```

与无序存储元素的 [QHash](../../H/QHash/QHash.md) 不同，[QMap](../../M/QMap/QMap.md) 通过键的大小有序存储元素。相同键的元素（因为 map 是一个 [QMultiMap](../../M/QMultiMap/QMultiMap.md)）将按照从最新到最早插入的顺序连续出现。

同一 map 可以使用多个迭代器。如果向 map 添加元素，已有的迭代器仍然有效。如果从 map 移除元素，指向被移除元素的迭代器会变成悬空迭代器。

**警告：**隐式共享容器迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QMap::iterator](../../M/QMap/QMap-iterator.md)，[QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) 和 [QMapIterator](../../M/QMapIterator/QMapIterator.md).

## 成员类型文档

### typedef const_iterator::iterator_category

*std::bidirectional_iterator_tag* 的别名，表明该迭代器是双向迭代器。

## 成员函数文档

### const_iterator::const_iterator(const [iterator](../../M/QMap/QMap-iterator.md) &*other*)

构造一个 *other* 的副本。

### const_iterator::const_iterator()

构造一个未初始化的迭代器。

一定不要对未初始化的迭代器调用 [key](QMap-const-iterator.md#const-key-const_iteratorkey-const)()，[value](QMap-const-iterator.md#const-t-const_iteratorvalue-const)() 和 operator++() 等函数。使用前要用 operator=() 赋值。

**另请参阅** [QMap::constBegin](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstbegin-const)() 和 [QMap::constEnd](../../M/QMap/QMap.md#qmapconst_iterator-qmapconstend-const)()。

### const Key &const_iterator::key() const

返回当前元素的键。

**另请参阅** [value](QMap-const-iterator.md#const-t-const_iteratorvalue-const)()。

### const T &const_iterator::value() const

返回当前元素的值。

**另请参阅** [key](QMap-const-iterator.md#const-key-const_iteratorkey-const)() 和 [operator*](QMap-const-iterator.md#const-t-const_iteratoroperator-const)()。

### bool const_iterator::operator!=(const [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &*other*) const

如果 *other* 与本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QMap-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const-1)()。

### const T &const_iterator::operator*() const

返回当前元素的值。

同 [value](QMap-const-iterator.md#const-t-const_iteratorvalue-const)()。

**另请参阅** [key](QMap-const-iterator.md#const-key-const_iteratorkey-const)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) const_iterator::operator+(int *j*) const

返回迭代器，指向该迭代器之前 *j* 个位置的元素。（如果 *j* 为负，则为之后 *j* 个位置。）

*j* 值较大时，该操作会比较慢。

**另请参阅** [operator-](QMap-const-iterator.md#const_iterator-const_iteratoroperator-int-j-const)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &const_iterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到 map 中的下一个元素并返回指向新位置元素的迭代器。

对 [QMap::end](../../M/QMap/QMap.md#qmapiterator-qmapend)() 调用该函数将导致未定义结果。

**另请参阅** [operator--](QMap-const-iterator.md#const_iterator-const_iteratoroperator--)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) const_iterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到 map 中的下一个元素并返回指向旧位置元素的迭代器。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &const_iterator::operator+=(int *j*)

使迭代器前进 *j* 个元素。（如果 *j* 为负，则后退 *j* 个位置。）

*j* 值较大时，该操作会比较慢。

**另请参阅** [operator-=](QMap-const-iterator.md#const_iterator-const_iteratoroperator-int-j)() 和 [operator+](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint-j-const)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) const_iterator::operator-(int *j*) const

返回迭代器，指向该迭代器之后 *j* 个位置的元素。（如果 *j* 为负，则为之前 *j* 个位置。）

*j* 值较大时，该操作会比较慢。

**另请参阅** [operator+](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint-j-const)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &const_iterator::operator--()

前置 -- 运算符（`--i`）使前一个元素成为当前元素并返回指向新位置元素的迭代器。

对 [QMap::begin](../../M/QMap/QMap.md#qmapiterator-qmapbegin)() 调用该函数将导致未定义结果。

**另请参阅** [operator++](QMap-const-iterator.md#const_iterator-const_iteratoroperator)()。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) const_iterator::operator--(*int*)

这是一个重载函数。

后置 -- 运算符（`i--`）使前一个元素成为当前元素并返回指向旧位置元素的迭代器。

### [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &const_iterator::operator-=(int *j*)

使迭代器后退 *j* 个元素。（如果 *j* 为负，则前进 *j* 个位置。）

*j* 值较大时，该操作会比较慢。

**另请参阅** [operator+=](QMap-const-iterator.md#const_iterator-const_iteratoroperatorint-j)() 和 [operator-](QMap-const-iterator.md#const_iterator-const_iteratoroperator-int-j-const)()。

### const T *const_iterator::operator->() const

返回指向当前元素值的指针。

**另请参阅** [value](QMap-const-iterator.md#const-t-const_iteratorvalue-const)()。

### bool const_iterator::operator==(const [const_iterator](QMap-const-iterator.md#const_iteratorconst_iterator) &*other*) const

如果 *other* 与本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QMap-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const)()。