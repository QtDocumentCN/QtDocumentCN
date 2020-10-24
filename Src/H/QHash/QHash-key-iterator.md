# key_iterator 类

class [QHash](https://doc.qt.io/qt-5/qhash.html#qhash)::key_iterator

[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 类为 [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 的键提供 STL 风格的常量类型迭代器。[更多内容...](QHash-key-iterator.md#详细描述)

Qt 5.6 中引入该类。

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

除了 operator*() 和 operator->() 返回键而不是值以外，[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 基本和 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 相同。

多数情况下应该使用 [QHash::iterator](../../H/QHash/QHash-iterator.md) 和 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)，通过调用 [QHash::iterator::key](https://doc.qt.io/qt-5/qhash-iterator.html#key)() 可以很容易地取得键：

```c++
for (QHash<int, QString>::const_iterator it = hash.cbegin(), end = hash.cend(); it != end; ++it) {
    cout << "The key: " << it.key() << Qt::endl
    cout << "The value: " << it.value() << Qt::endl;
    cout << "Also the value: " << (*it) << Qt::endl;
}
```

然而，如果想对 [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) 的键应用 STL 算法，就需要一个能解引用出键而不是值的迭代器。通过 [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 就能直接对一组键应用 STL 算法而不必调用 [QHash::keys](../../H/QHash/QHash.md#qlistkey-qhashkeys-const)()，这个函数比较低效，因为它首先要遍历一遍 [QHash](https://doc.qt.io/qt-5/qhash.html#qhash)，然后分配内存创建一个临时的 [QList](../../L/QList/QList.md)。

```c++
// Inefficient, keys() is expensive
QList<int> keys = hash.keys();
int numPrimes = std::count_if(keys.cbegin(), keys.cend(), isPrimeNumber);
qDeleteAll(hash2.keys());

// Efficient, no memory allocation needed
int numPrimes = std::count_if(hash.keyBegin(), hash.keyEnd(), isPrimeNumber);
qDeleteAll(hash2.keyBegin(), hash2.keyEnd());
```

[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 是 const 的，键是不可能被修改的。

[QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) 的默认构造函数创建一个未初始化的迭代器。必须使用 [QHash::keyBegin](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeybegin-const)() 或 [QHash::keyEnd](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeyend-const)() 等 [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) 函数来初始化它。

**警告：** 隐式共享容器的迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 和 [QHash::iterator](../../H/QHash/QHash-iterator.md)。

## 成员函数文档

### [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html) key_iterator::base() const

返回该 [key_iterator](https://doc.qt.io/qt-5/qhash-key-iterator.html) 基于的底层 [const_iterator](https://doc.qt.io/qt-5/qhash-const-iterator.html)。

### bool key_iterator::operator!=(key_iterator *other*) const

如果 *other* 与本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)()。

### const Key &key_iterator::operator*() const

返回当前元素的键。

### key_iterator &key_iterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到哈希表中的下一个元素并返回指向新位置元素的迭代器。

对 [QHash::keyEnd](../../H/QHash/QHash.md#qhashkey_iterator-qhashkeyend-const)() 调用该函数将导致未定义结果。

**另请参阅** [operator--](https://doc.qt.io/qt-5/qhash-key-iterator-obsolete.html#operator--)()。

### key_iterator key_iterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到哈希表中的下一个元素并返回指向旧位置元素的迭代器。

### const Key *key_iterator::operator->() const

返回指向当前元素键的指针。

### bool key_iterator::operator==(key_iterator *other*) const

如果 *other* 与本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QHash-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)()。