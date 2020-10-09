# iterator 类

class [QMap](../../M/QMap/QMap.md)::iterator

[QMap::iterator](../../M/QMap/qmap-iterator.md) 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 STL 风格的常量类型迭代器。[更多...](QMap-iterator.md#详细描述)

- [所有成员列表，包括继承的成员](../../M/QMap/qmap-iterator-members.md)



## 公共成员类型

| typedef | **[iterator_category](QMap-iterator.md#typedef-iteratoriteratorcategory)** |
| ------- | ------------------------------------------------------------ |
|         |                                                              |



## 公共成员函数

|             | **[iterator](QMap-iterator.md#iteratoriterator)**() |
| ----------- | ------------------------------------------------------------ |
| const Key & | **[key](QMap-iterator.md#const-key-iteratorkey-const)**() const |
| T &         | **[value](QMap-iterator.md#t-iteratorvalue-const)**() const |
| bool        | **[operator!=](QMap-iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool        | **[operator!=](QMap-iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| T &         | **[operator\*](QMap-iterator.md#t-iteratoroperator-const)**() const |
| iterator    | **[operator+](QMap-iterator.md#iterator-iteratoroperatorint-j-const)**(int *j*) const |
| iterator &  | **[operator++](QMap-iterator.md#iterator-iteratoroperator)**() |
| iterator    | **[operator++](QMap-iterator.md#iterator-iteratoroperatorint)**(*int*) |
| iterator &  | **[operator+=](QMap-iterator.md#iterator-iteratoroperatorint-j)**(int *j*) |
| iterator    | **[operator-](QMap-iterator.md#iterator-iteratoroperatorint-j-const)**(int *j*) const |
| iterator &  | **[operator--](QMap-iterator.md#iterator-iteratoroperator)**() |
| iterator    | **[operator--](QMap-iterator.md#iterator-iteratoroperatorint)**(*int*) |
| iterator &  | **[operator-=](QMap-iterator.md#iterator-iteratoroperatorint-j)**(int *j*) |
| T *         | **[operator->](QMap-iterator.md#t-iteratoroperator-const)**() const |
| bool        | **[operator==](QMap-iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool        | **[operator==](QMap-iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |



## 详细描述

[QMap](../../M/QMap/QMap.md) 同时提供 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) 和 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)。STL 风格迭代器更底层，使用更笨拙；同时也稍快一些。对于已经了解 STL 的开发者来说更加熟悉。

[QMap](../../M/QMap/QMap.md)<Key, T>::iterator 用来遍历 [QMap](../../M/QMap/QMap.md) (或 [QMultiMap](../../M/QMultiMap/QMultiMap.md)) 并修改与特定键相关联的值（不能修改键）。如果想遍历常量 [QMap](../../M/QMap/QMap.md)，应该使用 [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md)。对于非常量 [QMap](../../M/QMap/QMap.md)，使用 [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md) 通常是好的编程实践，除非需要在遍历时改变 [QMap](../../M/QMap/QMap.md)。常量类型迭代器稍快一些并可以提高代码可读性。

[QMap::iterator](../../M/QMap/qmap-iterator.md) 的默认构造函数创建一个未初始化的迭代器。必须在开始遍历前使用 [QMap::begin](../../M/QMap/QMap.md#qmapiterator-qmapbegin)(), [QMap::end](../../M/QMap/QMap.md#qmapiterator-qmapend)() 或 [QMap::find](../../M/QMap/QMap.md#qmapiterator-qmapfindconst-key-key)() 等 [QMap](../../M/QMap/QMap.md) 函数初始化它。下面是一个典型的循环，该循环打印出 map 中的所有键值对：

```c++
QMap<QString, int> map;
map.insert("January", 1);
map.insert("February", 2);
...
map.insert("December", 12);

QMap<QString, int>::iterator i;
for (i = map.begin(); i != map.end(); ++i)
    cout << i.key() << ": " << i.value() << Qt::endl;
```

与无序存储元素的 [QHash](../../H/QHash/QHash.md) 不同，[QMap](../../M/QMap/QMap.md) 通过键的大小有序存储元素。相同键的元素（当 map 是 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 时）将按照从最新到最早插入的顺序连续出现。

让我们通过几个例子来了解哪些情况下可以用 [QMap::iterator](../../M/QMap/qmap-iterator.md) 而不能用 [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md)。下面的例子将存储在 [QMap](../../M/QMap/QMap.md) 中的每个值增加2：

```c++
QMap<QString, int>::iterator i;
for (i = map.begin(); i != map.end(); ++i)
    i.value() += 2;
```

下面的例子移除所有键字符串的首字符是下划线的元素：

```c++
QMap<QString, int>::iterator i = map.begin();
while (i != map.end()) {
    if (i.key().startsWith('_'))
        i = map.erase(i);
    else
        ++i;
}
```

[QMap::erase](../../M/QMap/QMap.md#qmapiterator-qmaperaseqmapiterator-pos)() 的调用从 map 中移除迭代器所指元素，返回指向下一个元素的迭代器。下面是另一个遍历时移除元素的方法：

```c++
QMap<QString, int>::iterator i = map.begin();
while (i != map.end()) {
    QMap<QString, int>::iterator prev = i;
    ++i;
    if (prev.key().startsWith('_'))
        map.erase(prev);
}
```

有人会写出像下面这样的代码：

```c++
// WRONG
while (i != map.end()) {
    if (i.key().startsWith('_'))
        map.erase(i);
    ++i;
}
```

然而，这会导致程序在 `++i` 处崩溃，因为调用完 [erase](../../M/QMap/QMap.md#qmapiterator-qmaperaseqmapiterator-pos)() 后，`i`变成悬空迭代器。

同一 map 可以使用多个迭代器。如果向 map 添加元素，已有的迭代器仍然有效。如果从 map 移除元素，指向被移除元素的迭代器会变成悬空迭代器。

**警告：** 隐式共享容器迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅 [隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md), [QMap::key_iterator](../../M/QMap/qmap-key-iterator.md), and [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md).

## 成员类型文档

### typedef iterator::iterator_category

*std::bidirectional_iterator_tag* 的别名，表明该迭代器是双向迭代器。

## 成员函数文档

### bool iterator::operator!=(const [const_iterator](../../M/QMap/qmap-const-iterator.md) &*other*) const

### bool iterator::operator!=(const [iterator](QMap-iterator.md#iteratoriterator) &*other*) const

如果 *other* 和本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QMap-iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### bool iterator::operator==(const [const_iterator](../../M/QMap/qmap-const-iterator.md) &*other*) const

### bool iterator::operator==(const [iterator](QMap-iterator.md#iteratoriterator) &*other*) const

如果 *other* 和本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QMap-iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### iterator::iterator()

构造一个未初始化的迭代器。

一定不要对未初始化的迭代器调用 [key](QMap-iterator.md#const-key-iteratorkey-const)(), [value](QMap-iterator.md#t-iteratorvalue-const)() 和 operator++() 等函数。使用前要用 operator=() 赋值。

**另请参阅** [QMap::begin](../../M/QMap/QMap.md#qmapiterator-qmapbegin)() 和 [QMap::end](../../M/QMap/QMap.md#qmapiterator-qmapend)().

### const Key &iterator::key() const

以常引用返回当前元素的键。

There is no direct way of changing an item's key through an iterator, although it can be done by calling [QMap::erase](../../M/QMap/QMap.md#qmapiterator-qmaperaseqmapiterator-pos)() followed by [QMap::insert](../../M/QMap/QMap.md#qmapiterator-qmapinsertconst-key-key-const-t-value)() or QMap::insertMulti().

**另请参阅** [value](QMap-iterator.md#t-iteratorvalue-const)().

### T &iterator::value() const

返回当前元素的值的可修改引用。

可以通过在赋值运算符左边使用 value() 修改元素的值，例如：

```c++
if (i.key() == "Hello")
    i.value() = "Bonjour";
```

**另请参阅** [key](QMap-iterator.md#const-key-iteratorkey-const)() 和 [operator*](QMap-iterator.md#t-iteratoroperator-const)().

### T &iterator::operator*() const

返回当前元素的值的可修改引用。

同 [value](QMap-iterator.md#t-iteratorvalue-const)().

**另请参阅** [key](QMap-iterator.md#const-key-iteratorkey-const)().

### [iterator](QMap-iterator.md#iteratoriterator) iterator::operator+(int *j*) const

Returns an iterator to the item at *j* positions forward from this iterator. (If *j* is negative, the iterator goes backward.)

This operation can be slow for large *j* values.

**另请参阅** [operator-](QMap-iterator.md#iterator-iteratoroperatorint-j-const)().

### [iterator](QMap-iterator.md#iteratoriterator) &iterator::operator++()

The prefix ++ operator (`++i`) advances the iterator to the next item in the map and returns an iterator to the new current item.

Calling this function on [QMap::end](../../M/QMap/QMap.md#qmapiterator-qmapend)() leads to undefined results.

**另请参阅** [operator--](QMap-iterator.md#iterator-iteratoroperator)().

### [iterator](QMap-iterator.md#iteratoriterator) iterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`i++`) advances the iterator to the next item in the map and returns an iterator to the previously current item.

### [iterator](QMap-iterator.md#iteratoriterator) &iterator::operator+=(int *j*)

Advances the iterator by *j* items. (If *j* is negative, the iterator goes backward.)

**另请参阅** [operator-=](QMap-iterator.md#iterator-iteratoroperatorint-j)() 和 [operator+](QMap-iterator.md#iterator-iteratoroperatorint-j-const)().

### [iterator](QMap-iterator.md#iteratoriterator) iterator::operator-(int *j*) const

Returns an iterator to the item at *j* positions backward from this iterator. (If *j* is negative, the iterator goes forward.)

This operation can be slow for large *j* values.

**另请参阅** [operator+](QMap-iterator.md#iterator-iteratoroperatorint-j-const)().

### [iterator](QMap-iterator.md#iteratoriterator) &iterator::operator--()

The prefix -- operator (`--i`) makes the preceding item current and returns an iterator pointing to the new current item.

Calling this function on [QMap::begin](../../M/QMap/QMap.md#qmapiterator-qmapbegin)() leads to undefined results.

**另请参阅** [operator++](QMap-iterator.md#iterator-iteratoroperator)().

### [iterator](QMap-iterator.md#iteratoriterator) iterator::operator--(*int*)

This is an overloaded function.

The postfix -- operator (`i--`) makes the preceding item current and returns an iterator pointing to the previously current item.

### [iterator](QMap-iterator.md#iteratoriterator) &iterator::operator-=(int *j*)

Makes the iterator go back by *j* items. (If *j* is negative, the iterator goes forward.)

**另请参阅** [operator+=](QMap-iterator.md#iterator-iteratoroperatorint-j)() 和 [operator-](QMap-iterator.md#iterator-iteratoroperatorint-j-const)().

### T *iterator::operator->() const

返回指向当前元素值的指针。

**另请参阅** [value](QMap-iterator.md#t-iteratorvalue-const)().