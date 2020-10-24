# iterator 类

class [QHash](../../H/QHash/QHash.md)::iterator

[QHash::iterator](../../H/QHash/QHash-iterator.md) 为 [QHash](../../H/QHash/QHash.md) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 STL 风格的非常量迭代器。[更多内容...](QHash-iterator.md#详细描述)

- [所有成员列表，包括继承的成员](https://doc.qt.io/qt-5/qhash-iterator-members.html)
- [废弃的成员](https://doc.qt.io/qt-5/qhash-iterator-obsolete.html)



## 公共成员函数

|             | **[iterator](QHash-iterator.md#iteratoriterator)**() |
| -----------: | :------------------------------------------------------------ |
| const Key & | **[key](QHash-iterator.md#const-key-iteratorkey-const)**() const |
| T &         | **[value](QHash-iterator.md#t-iteratorvalue-const)**() const |
| bool        | **[operator!=](QHash-iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool        | **[operator!=](QHash-iterator.md#bool-iteratoroperatorconst-const_iterator-other-const)**(const const_iterator &*other*) const |
| T &         | **[operator\*](QHash-iterator.md#t-iteratoroperator-const)**() const |
| iterator &  | **[operator++](QHash-iterator.md#iterator-iteratoroperator)**() |
| iterator    | **[operator++](QHash-iterator.md#iterator-iteratoroperatorint)**(*int*) |
| T *         | **[operator->](QHash-iterator.md#t-iteratoroperator--const)**() const |
| bool        | **[operator==](QHash-iterator.md#bool-iteratoroperatorconst-iterator-other-const-1)**(const iterator &*other*) const |
| bool        | **[operator==](QHash-iterator.md#bool-iteratoroperatorconst-const_iterator-other-const-1)**(const const_iterator &*other*) const |



## 详细描述

[QHash](../../H/QHash/QHash.md) 同时提供 [STL-style iterators](https://doc.qt.io/qt-5/containers.html#stl-style-iterators) 和 [Java-style iterators](https://doc.qt.io/qt-5/containers.html#java-style-iterators)。STL 风格迭代器更底层，使用更笨拙；同时也稍快一些。对于已经了解 STL 的开发者来说更加熟悉。

[QHash](../../H/QHash/QHash.md)<Key, T>::iterator 用来遍历 [QHash](../../H/QHash/QHash.md) (或 [QMultiHash](../../M/QMultiHash/QMultiHash.md)) 并修改与特定键相关联的值（不能修改键）。如果想遍历常量 [QHash](../../H/QHash/QHash.md)，应该使用 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)。对于非常量 [QHash](../../H/QHash/QHash.md)，使用 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 通常是也好的编程实践，除非需要在遍历时改变 [QHash](../../H/QHash/QHash.md)。常量类型的迭代器稍快一些并可以提高代码可读性。

[QHash::iterator](../../H/QHash/QHash-iterator.md) 的默认构造函数创建一个未初始化的迭代器。必须在开始遍历前使用 [QHash::begin](../../H/QHash/QHash.md#qhashiterator-qhashbegin)()， [QHash::end](../../H/QHash/QHash.md#qhashiterator-qhashend)()，或 [QHash::find](../../H/QHash/QHash.md#qhashiterator-qhashfindconst-key-key)() 等 [QHash](../../H/QHash/QHash.md) 函数初始化它。下面是一个典型的循环，该循环打印出哈希表中的所有键值对：

```c++
QHash<QString, int> hash;
hash.insert("January", 1);
hash.insert("February", 2);
...
hash.insert("December", 12);

QHash<QString, int>::iterator i;
for (i = hash.begin(); i != hash.end(); ++i)
    cout << i.key() << ": " << i.value() << Qt::endl;
```

与通过键的大小有序存储元素的 [QMap](../../M/QMap/QMap.md) 不同，[QHash](../../H/QHash/QHash.md) 无序存储元素。

让我们通过几个例子来了解哪些情况下可以用 [QHash::iterator](../../H/QHash/QHash-iterator.md) 而不能用 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)。下面的例子将存储在 [QHash](../../H/QHash/QHash.md) 中的每个值增加2：

```c++
QHash<QString, int>::iterator i;
for (i = hash.begin(); i != hash.end(); ++i)
    i.value() += 2;
```

下面的例子移除所有键字符串的首字符是下划线的元素：

```c++
QHash<QString, int>::iterator i = hash.begin();
while (i != hash.end()) {
    if (i.key().startsWith('_'))
        i = hash.erase(i);
    else
        ++i;
}
```

对 [QHash::erase](../../H/QHash/QHash.md#qhashiterator-qhasheraseqhashconst_iterator-pos)() 的调用从哈希表中移除迭代器所指元素，返回指向下一个元素的迭代器。下面是另一个在遍历时移除元素的方法：

```c++
QHash<QString, int>::iterator i = hash.begin();
while (i != hash.end()) {
    QHash<QString, int>::iterator prev = i;
    ++i;
    if (prev.key().startsWith('_'))
        hash.erase(prev);
}
```

有人会写出像下面这样的代码：

```c++
// WRONG
while (i != hash.end()) {
    if (i.key().startsWith('_'))
        hash.erase(i);
    ++i;
}
```

然而，这会导致程序在 `++i` 处崩溃，因为调用完 [erase](../../H/QHash/QHash.md#qhashiterator-qhasheraseqhashconst_iterator-pos)() 后，`i`成为悬空迭代器。

同一哈希表可以使用多个迭代器。然而，需要注意任何对 [QHash](../../H/QHash/QHash.md) 的直接修改都可能完全改变哈希表中存储的元素顺序，因为该操作可能引起 [QHash](../../H/QHash/QHash.md) 重新散列其内部数据结构。有一个例外是 [QHash::erase](../../H/QHash/QHash.md#qhashiterator-qhasheraseqhashconst_iterator-pos)()。该函数可以在迭代时安全调用，不会影响哈希表中元素的顺序。如果需要长时间持有迭代器，建议使用 [QMap](../../M/QMap/QMap.md) 而非 [QHash](../../H/QHash/QHash.md)。

**警告：** 隐式共享容器迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)，[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 和 [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md)。

## 成员函数文档

### bool iterator::operator!=(const [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html) &*other*) const

### bool iterator::operator!=(const [iterator](QHash-iterator.md#iteratoriterator) &*other*) const

如果 *other* 与本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QHash-iterator.md#bool-iteratoroperatorconst-iterator-other-const-1)()。

### bool iterator::operator==(const [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html) &*other*) const

### bool iterator::operator==(const [iterator](QHash-iterator.md#iteratoriterator) &*other*) const

如果 *other* 与本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QHash-iterator.md#bool-iteratoroperatorconst-iterator-other-const)()。

### iterator::iterator()

构造一个未初始化的迭代器。

一定不要对未初始化的迭代器调用 [key](QHash-iterator.md#const-key-iteratorkey-const)()，[value](QHash-iterator.md#t-iteratorvalue-const)() 和 operator++() 等函数。使用前要用 operator=() 赋值。

**另请参阅** [QHash::begin](../../H/QHash/QHash.md#qhashiterator-qhashbegin)() 和 [QHash::end](../../H/QHash/QHash.md#qhashiterator-qhashend)()。

### const Key &iterator::key() const

以常引用返回当前元素的键。

不能直接通过迭代器改变元素的键，尽管可以通过调用 [QHash::erase](../../H/QHash/QHash.md#qhashiterator-qhasheraseqhashconst_iterator-pos)() 后再调用 [QHash::insert](../../H/QHash/QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)() 的方式来改变键。

**另请参阅** [value](QHash-iterator.md#t-iteratorvalue-const)()。

### T &iterator::value() const

返回当前元素值的可修改引用。

可以通过在赋值运算符左边使用 value() 来修改元素的值，例如：

```c++
if (i.key() == "Hello")
    i.value() = "Bonjour";
```

**另请参阅** [key](QHash-iterator.md#const-key-iteratorkey-const)() 和 [operator*](QHash-iterator.md#t-iteratoroperator-const)()。

### T &iterator::operator*() const

返回当前元素值的可修改引用。

同 [value](QHash-iterator.md#t-iteratorvalue-const)()。

**另请参阅** [key](QHash-iterator.md#const-key-iteratorkey-const)()。

### [iterator](QHash-iterator.md#iteratoriterator) &iterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到哈希表中的下一个元素并返回指向新位置元素的迭代器。

对 [QHash::end](../../H/QHash/QHash.md#qhashiterator-qhashend)() 调用该函数将导致未定义结果。

**另请参阅** [operator--](https://doc.qt.io/qt-5/qhash-iterator-obsolete.html#operator--)()。

### [iterator](QHash-iterator.md#iteratoriterator) iterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到哈希表中的下一个元素并返回指向旧位置元素的迭代器。

### T *iterator::operator->() const

返回指向当前元素值的指针。

**另请参阅** [value](QHash-iterator.md#t-iteratorvalue-const)()。