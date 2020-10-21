# key_iterator 类

class [QMap](../../M/QMap/QMap.md)::key_iterator

[QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 的键提供 STL 风格的常量类型迭代器。[更多内容...](QMap-key-iterator.md#详细描述)

Qt 5.6 中引入该类。

- [所有成员列表，包括继承的成员](../../M/QMap/QMap-key-iterator-members.md)



## 公共成员函数

| const_iterator | **[base](QMap-key-iterator.md#const_iterator-key_iteratorbase-const)**() const |
| --------------: | :------------------------------------------------------------ |
| bool           | **[operator!=](QMap-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)**(key_iterator *other*) const |
| const Key &    | **[operator\*](QMap-key-iterator.md#const-key-key_iteratoroperator-const)**() const |
| key_iterator & | **[operator++](QMap-key-iterator.md#key_iterator-key_iteratoroperator)**() |
| key_iterator   | **[operator++](QMap-key-iterator.md#key_iterator-key_iteratoroperatorint)**(*int*) |
| key_iterator & | **[operator--](QMap-key-iterator.md#key_iterator-key_iteratoroperator--)**() |
| key_iterator   | **[operator--](QMap-key-iterator.md#key_iterator-key_iteratoroperator--int)**(*int*) |
| const Key *    | **[operator->](QMap-key-iterator.md#const-key-key_iteratoroperator--const)**() const |
| bool           | **[operator==](QMap-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const-1)**(key_iterator *other*) const |



## 详细描述

除了 operator*() 和 operator->() 返回键而不是值以外，[QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) 基本和 [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 相同。

多数情况下应该使用 [QMap::iterator](../../M/QMap/QMap-iterator.md) 和 [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md)，通过调用 [QMap::iterator::key](../../M/QMap/QMap-iterator.md#key)() 可以很容易地取得键：

```c++
for (QMap<int, QString>::const_iterator it = map.cbegin(), end = map.cend(); it != end; ++it) {
    cout << "The key: " << it.key() << Qt::endl
    cout << "The value: " << it.value() << Qt::endl;
    cout << "Also the value: " << (*it) << Qt::endl;
}
```

然而，如果想对 [QMap](../../M/QMap/QMap.md) 的键应用 STL 算法，就需要一个能解引用出键而不是值的迭代器。通过 [QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) 就能直接对一组键应用 STL 算法而不必调用 [QMap::keys](../../M/QMap/QMap.md#qlistkey-qmapkeys-const)()，这个函数比较低效，因为它首先要遍历一遍 [QMap](../../M/QMap/QMap.md)，然后分配内存创建一个临时的 [QList](../../L/QList/QList.md)。

```c++
// Inefficient, keys() is expensive
QList<int> keys = map.keys();
int numPrimes = std::count_if(map.cbegin(), map.cend(), isPrimeNumber);
qDeleteAll(map2.keys());

// Efficient, no memory allocation needed
int numPrimes = std::count_if(map.keyBegin(), map.keyEnd(), isPrimeNumber);
qDeleteAll(map2.keyBegin(), map2.keyEnd());
```

[QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) 是 const 的，键是不可能被修改的。

[QMap::key_iterator](../../M/QMap/QMap-key-iterator.md)  的默认构造函数创建一个未初始化的迭代器。必须使用 [QMap::keyBegin](../../M/QMap/QMap.md#qmapkey_iterator-qmapkeybegin-const)() 或 [QMap::keyEnd](../../M/QMap/QMap.md#qmapkey_iterator-qmapkeyend-const)() 等 [QMap](../../M/QMap/QMap.md) 函数来初始化它。

**警告：** 隐式共享容器的迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 和 [QMap::iterator](../../M/QMap/QMap-iterator.md)。

## 成员函数文档

### [const_iterator](../../M/QMap/QMap-const-iterator.md) key_iterator::base() const

返回该 [key_iterator](../../M/QMap/QMap-key-iterator.md) 基于的底层 [const_iterator](../../M/QMap/QMap-const-iterator.md)。

### bool key_iterator::operator!=(key_iterator *other*) const

如果 *other* 与本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QMap-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const-1)()。

### const Key &key_iterator::operator*() const

返回当前元素的键。

### key_iterator &key_iterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到 map（译者注：原文是 hash，应为笔误。）中的下一个元素并返回指向新位置元素的迭代器。

对 [QMap::keyEnd](../../M/QMap/QMap.md#qmapkey_iterator-qmapkeyend-const)() 调用该函数将导致未定义结果。

**另请参阅** [operator--](QMap-key-iterator.md#key_iterator-key_iteratoroperator--)()。

### key_iterator key_iterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到 map（译者注：原文是 hash，应为笔误。）中的下一个元素并返回指向旧位置元素的迭代器。

### key_iterator &key_iterator::operator--()

前置 -- 运算符（`--i`）使前一个元素成为当前元素并返回指向新位置元素的迭代器。

对 [QMap::keyBegin](../../M/QMap/QMap.md#qmapkey_iterator-qmapkeybegin-const)() 调用该函数将导致未定义结果。

**另请参阅** [operator++](QMap-key-iterator.md#key_iterator-key_iteratoroperator)()。

### key_iterator key_iterator::operator--(*int*)

这是一个重载函数。

后置 -- 运算符（`i--`）使前一个元素成为当前元素并返回指向旧位置元素的迭代器。

### const Key *key_iterator::operator->() const

返回指向当前元素键的指针。

### bool key_iterator::operator==(key_iterator *other*) const

如果 *other* 与本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QMap-key-iterator.md#bool-key_iteratoroperatorkey_iterator-other-const)()。