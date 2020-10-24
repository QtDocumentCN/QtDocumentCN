# const_iterator 类

class [QHash](../../H/QHash/QHash.md)::const_iterator

[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 类为 [QHash](../../H/QHash/QHash.md) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 STL 风格的常量迭代器。[更多内容...](QHash-const-iterator.md#详细描述)

- [所有成员列表，包括继承的成员](../../H/QHash/QHash-const-iterator-members.md)
- [废弃的成员](../../H/QHash/QHash-const-iterator-obsolete.md)



## 公共成员函数

|                  | **[const_iterator](QHash-const-iterator.md#const_iteratorconst_iteratorconst-iterator-other)**(const iterator &*other*) |
| ----------------: | :------------------------------------------------------------ |
|                  | **[const_iterator](QHash-const-iterator.md#const_iteratorconst_iterator)**() |
| const Key &      | **[key](QHash-const-iterator.md#const-key-const_iteratorkey-const)**() const |
| const T &        | **[value](QHash-const-iterator.md#const-t-const_iteratorvalue-const)**() const |
| bool             | **[operator!=](QHash-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const)**(const const_iterator &*other*) const |
| const T &        | **[operator\*](QHash-const-iterator.md#const-t-const_iteratoroperator-const)**() const |
| const_iterator & | **[operator++](QHash-const-iterator.md#const_iterator-const_iteratoroperator)**() |
| const_iterator   | **[operator++](QHash-const-iterator.md#const_iterator-const_iteratoroperatorint)**(*int*) |
| const T *        | **[operator->](QHash-const-iterator.md#const-t-const_iteratoroperator--const)**() const |
| bool             | **[operator==](QHash-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const-1)**(const const_iterator &*other*) const |



## 详细描述

[QHash](../../H/QHash/QHash.md) 同时提供 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) 和 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)。STL 风格迭代器更底层，使用更笨拙；同时也稍快一些。对于已经了解 STL 的开发者来说更加熟悉。

[QHash](../../H/QHash/QHash.md)<Key, T>::const_iterator 用来遍历 [QHash](../../H/QHash/QHash.md)（或 [QMultiHash](../../M/QMultiHash/QMultiHash.md)）。如果想在遍历时修改 [QHash](../../H/QHash/QHash.md)，必须使用 [QHash::iterator](../../H/QHash/QHash-iterator.md)。对于非常量 [QHash](../../H/QHash/QHash.md)，使用 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 通常也是好的编程实践，除非需要在遍历时改变 [QHash](../../H/QHash/QHash.md)。const 迭代器稍快一些并可以提高代码可读性。

[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 的默认构造函数创建一个未初始化的迭代器。必须在开始遍历前使用  [QHash::constBegin](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstbegin-const)()，[QHash::constEnd](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstend-const)() 或 [QHash::find](../../H/QHash/QHash.md#qhashiterator-qhashfindconst-key-key)() 等 [QHash](../../H/QHash/QHash.md) 函数初始化它。下面是一个典型的循环，该循环打印出 map 中的所有键值对：

```c++
QHash<QString, int> hash;
hash.insert("January", 1);
hash.insert("February", 2);
...
hash.insert("December", 12);

QHash<QString, int>::const_iterator i;
for (i = hash.constBegin(); i != hash.constEnd(); ++i)
    cout << i.key() << ": " << i.value() << Qt::endl;
```

与通过键的大小有序存储元素的 [QMap](../../M/QMap/QMap.md) 不同，[QHash](../../H/QHash/QHash.md) 无序存储元素。唯一的保证是共享同一键的元素（通过 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 的函数插入）将按照从最新到最早插入值的顺序连续出现。

同一哈希表可以使用多个迭代器。然而，需要注意任何对 [QHash](../../H/QHash/QHash.md) 的直接修改都可能完全改变哈希表中存储的元素顺序，因为该操作可能引起 [QHash](../../H/QHash/QHash.md) 重新散列其内部数据结构。如果需要长时间持有迭代器，建议使用 [QMap](../../M/QMap/QMap.md) 而非 [QHash](../../H/QHash/QHash.md)。

**警告：** 隐式共享容器迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QHash::iterator](../../H/QHash/QHash-iterator.md) 和 [QHashIterator](../../H/QHashIterator/QHashIterator.md)。

## 成员函数文档

### const_iterator::const_iterator(const [iterator](../../H/QHash/QHash-iterator.md) &*other*)

构造一个 *other* 的副本。

### const_iterator::const_iterator()

构造一个未初始化的迭代器。

一定不要对未初始化的迭代器调用 [key](QHash-const-iterator.md#const-key-const_iteratorkey-const)()，[value](QHash-const-iterator.md#const-t-const_iteratorvalue-const)() 和 operator++() 等函数。使用前要用 operator=() 赋值。

**另请参阅** [QHash::constBegin](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstbegin-const)() 和 [QHash::constEnd](../../H/QHash/QHash.md#qhashconst_iterator-qhashconstend-const)()。

### const Key &const_iterator::key() const

返回当前元素的键。

**另请参阅** [value](QHash-const-iterator.md#const-t-const_iteratorvalue-const)()。

### const T &const_iterator::value() const

返回当前元素的值。

**另请参阅** [key](QHash-const-iterator.md#const-key-const_iteratorkey-const)() 和 [operator*](QHash-const-iterator.md#const-t-const_iteratoroperator-const)()。

### bool const_iterator::operator!=(const [const_iterator](QHash-const-iterator.md#const_iteratorconst_iterator) &*other*) const

如果 *other* 与本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QHash-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const-1)()。

### const T &const_iterator::operator*() const

返回当前元素的值。

同 [value](QHash-const-iterator.md#const-t-const_iteratorvalue-const)()。

**另请参阅** [key](QHash-const-iterator.md#const-key-const_iteratorkey-const)()。

### [const_iterator](QHash-const-iterator.md#const_iteratorconst_iterator) &const_iterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到哈希表中的下一个元素并返回指向新位置元素的迭代器。

对 [QHash::end](../../H/QHash/QHash.md#qhashiterator-qhashend)() 调用该函数将导致未定义结果。

**另请参阅** [operator--](../../H/QHash/QHash-const-iterator-obsolete.md#const_iterator-const_iteratoroperator--)()。

### [const_iterator](QHash-const-iterator.md#const_iteratorconst_iterator) const_iterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到哈希表中的下一个元素并返回指向旧位置元素的迭代器。

### const T *const_iterator::operator->() const

返回指向当前元素值的指针。

**另请参阅** [value](QHash-const-iterator.md#const-t-const_iteratorvalue-const)()。

### bool const_iterator::operator==(const [const_iterator](QHash-const-iterator.md#const_iteratorconst_iterator) &*other*) const

如果 *other* 与本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QHash-const-iterator.md#bool-const_iteratoroperatorconst-const_iterator-other-const)()。