# key_iterator 类

class [QMap](../../M/QMap/QMap.md)::key_iterator

[QMap::key_iterator](../../M/QMap/qmap-key-iterator.md) 类为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 的键提供 STL 风格的常量类型迭代器。[更多...](QMap-key-iterator.md#详细描述)

Qt 5.6 中引入该类。

- [所有成员列表，包括继承的成员](../../M/QMap/qmap-key-iterator-members.md)



## 公共成员函数

| const_iterator | **[base](QMap-key-iterator.md#constiterator-keyiteratorbase-const)**() const |
| -------------- | ------------------------------------------------------------ |
| bool           | **[operator!=](QMap-key-iterator.md#bool-keyiteratoroperatorkeyiterator-other-const)**(key_iterator *other*) const |
| const Key &    | **[operator\*](QMap-key-iterator.md#const-key-keyiteratoroperator-const)**() const |
| key_iterator & | **[operator++](QMap-key-iterator.md#keyiterator-keyiteratoroperator)**() |
| key_iterator   | **[operator++](QMap-key-iterator.md#keyiterator-keyiteratoroperatorint)**(*int*) |
| key_iterator & | **[operator--](QMap-key-iterator.md#keyiterator-keyiteratoroperator)**() |
| key_iterator   | **[operator--](QMap-key-iterator.md#keyiterator-keyiteratoroperatorint)**(*int*) |
| const Key *    | **[operator->](QMap-key-iterator.md#const-key-keyiteratoroperator-const)**() const |
| bool           | **[operator==](QMap-key-iterator.md#bool-keyiteratoroperatorkeyiterator-other-const)**(key_iterator *other*) const |



## 详细描述

[QMap::key_iterator](../../M/QMap/qmap-key-iterator.md) 除了 operator*() 和 operator->() 返回键而不是值以外，其它基本上和 [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md) 相同。

多数情况下应该使用 [QMap::iterator](../../M/QMap/qmap-iterator.md) 和 [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md) ，通过调用 [QMap::iterator::key](../../M/QMap/qmap-iterator.md#key)() 可以很容易地取得键：

```c++
for (QMap<int, QString>::const_iterator it = map.cbegin(), end = map.cend(); it != end; ++it) {
    cout << "The key: " << it.key() << Qt::endl
    cout << "The value: " << it.value() << Qt::endl;
    cout << "Also the value: " << (*it) << Qt::endl;
}
```

然而，如果想对 [QMap](../../M/QMap/QMap.md) 的键应用 STL 算法，就需要一个能解引用出键而不是值的迭代器。通过 [QMap::key_iterator](../../M/QMap/qmap-key-iterator.md) 就能直接对一组键应用 STL 算法而不必调用 [QMap::keys](../../M/QMap/QMap.md#qlistkey-qmapkeys-const)()，这个函数比较低效，因为它首先要遍历一遍 [QMap](../../M/QMap/QMap.md) ，然后分配内存创建一个临时的 [QList](../../L/QList/QList.md)。

```c++
// Inefficient, keys() is expensive
QList<int> keys = map.keys();
int numPrimes = std::count_if(map.cbegin(), map.cend(), isPrimeNumber);
qDeleteAll(map2.keys());

// Efficient, no memory allocation needed
int numPrimes = std::count_if(map.keyBegin(), map.keyEnd(), isPrimeNumber);
qDeleteAll(map2.keyBegin(), map2.keyEnd());
```

[QMap::key_iterator](../../M/QMap/qmap-key-iterator.md) 是 const 的，键是不可能被修改的。

[QMap::key_iterator](../../M/QMap/qmap-key-iterator.md)  的默认构造函数创建一个未初始化的迭代器。必须使用 [QMap::keyBegin](../../M/QMap/QMap.md#qmapkeyiterator-qmapkeybegin-const)() 或 [QMap::keyEnd](../../M/QMap/QMap.md#qmapkeyiterator-qmapkeyend-const)() 等 [QMap](../../M/QMap/QMap.md) 函数来初始化它。

**警告：** 隐式共享容器的迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅 [隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

**另请参阅** [QMap::const_iterator](../../M/QMap/qmap-const-iterator.md) 和 [QMap::iterator](../../M/QMap/qmap-iterator.md).

## 成员函数文档

### [const_iterator](../../M/QMap/qmap-const-iterator.md) key_iterator::base() const

Returns the underlying [const_iterator](../../M/QMap/qmap-const-iterator.md) this [key_iterator](../../M/QMap/qmap-key-iterator.md) is based on.

### bool key_iterator::operator!=(key_iterator *other*) const

如果 *other* 和本迭代器指向的元素不同，返回 `true`；否则返回 `false`。

**另请参阅** [operator==](QMap-key-iterator.md#bool-keyiteratoroperatorkeyiterator-other-const)().

### const Key &key_iterator::operator*() const

Returns the current item's key.

### key_iterator &key_iterator::operator++()

The prefix ++ operator (`++i`) advances the iterator to the next item in the hash 和 returns an iterator to the new current item.

Calling this function on [QMap::keyEnd](../../M/QMap/QMap.md#qmapkeyiterator-qmapkeyend-const)() leads to undefined results.

**另请参阅** [operator--](QMap-key-iterator.md#keyiterator-keyiteratoroperator)().

### key_iterator key_iterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`i++`) advances the iterator to the next item in the hash 和 returns an iterator to the previous item.

### key_iterator &key_iterator::operator--()

The prefix -- operator (`--i`) makes the preceding item current 和 returns an iterator pointing to the new current item.

Calling this function on [QMap::keyBegin](../../M/QMap/QMap.md#qmapkeyiterator-qmapkeybegin-const)() leads to undefined results.

**另请参阅** [operator++](QMap-key-iterator.md#keyiterator-keyiteratoroperator)().

### key_iterator key_iterator::operator--(*int*)

This is an overloaded function.

The postfix -- operator (`i--`) makes the preceding item current 和 returns an iterator pointing to the previous item.

### const Key *key_iterator::operator->() const

Returns a pointer to the current item's key.

### bool key_iterator::operator==(key_iterator *other*) const

如果 *other* 和本迭代器指向相同的元素，返回 `true`；否则返回 `false`。

**另请参阅** [operator!=](QMap-key-iterator.md#bool-keyiteratoroperatorkeyiterator-other-const)().