# QKeyValueIterator 类

template <typename Key, typename T, typename Iterator> class QKeyValueIterator

关联容器的键值对类型的迭代器。[更多内容...](QKeyValueIterator.md#详细描述)

| 头文件: | #include <QKeyValueIterator> |
| -------: | :---------------------------- |
| qmake:  | QT += core                   |
| Since:  | Qt 5.10                      |

Qt 5.10 中引入该类。

- [所有成员列表，包括继承的成员](../../K/QKeyValueIterator/QKeyValueIterator-members.md)



## 公共成员函数

|                                       | **[QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiteratoriterator-o)**(Iterator *o*) |
| -------------------------------------: | :------------------------------------------------------------ |
|                                       | **[QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)**() |
| Iterator                              | **[base](QKeyValueIterator.md#iterator-qkeyvalueiteratorbase-const)**() const |
| std::pair<Key, T>                     | **[operator\*](QKeyValueIterator.md#stdpairkey-t-qkeyvalueiteratoroperator-const)**() const |
| QKeyValueIterator<Key, T, Iterator> & | **[operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator)**() |
| QKeyValueIterator<Key, T, Iterator>   | **[operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperatorint)**(*int*) |
| QKeyValueIterator<Key, T, Iterator> & | **[operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--)**() |
| QKeyValueIterator<Key, T, Iterator>   | **[operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--int)**(*int*) |
| QKeyValueIterator::pointer            | **[operator->](QKeyValueIterator.md#qkeyvalueiteratorpointer-qkeyvalueiteratoroperator--const)**() const |



## 相关非成员函数

| bool | **[operator!=](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs)**(QKeyValueIterator<Key, T, Iterator> *lhs*, QKeyValueIterator<Key, T, Iterator> *rhs*) |
| ----: | :------------------------------------------------------------ |
| bool | **[operator==](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs-1)**(QKeyValueIterator<Key, T, Iterator> *lhs*, QKeyValueIterator<Key, T, Iterator> *rhs*) |



## 详细描述

QKeyValueIterator 类为关联容器如 [QHash](https://doc.qt.io/qt-5/qhash.html#qhash) 和 [QMap](../../M/QMap/QMap.md) 返回的键值对提供 STL 风格的迭代器。该类支持与 STL 关联容器相同的接口，即遍历容器时取得键值对。

这将改善 [QMap](../../M/QMap/QMap.md)，[QHash](https://doc.qt.io/qt-5/qhash.html#qhash) 及其相关类与 STL 风格算法之间的互操作性。

**警告：** 隐式共享容器的迭代器的工作方式和 STL 迭代器不完全相同。当容器的迭代器还处于活动状态时，应该避免拷贝容器。更多信息请参阅[隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题)。

## 成员函数文档

### QKeyValueIterator::QKeyValueIterator(Iterator *o*)

在迭代器 *o* 之上构造 QKeyValueIterator。

### QKeyValueIterator::QKeyValueIterator()

构造一个默认 QKeyValueIterator。

### Iterator QKeyValueIterator::base() const

返回该 [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md) 基于的底层迭代器。

### std::pair<Key, T> QKeyValueIterator::operator*() const

以键值对返回当前元素。

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> &QKeyValueIterator::operator++()

前置 ++ 运算符（`++i`）将迭代器向前移动到容器中的下一个元素并返回迭代器。

**注意：** 将迭代器向前移动到容器的 end() 之后将导致未定义行为。

**另请参阅** [operator--](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator--)().

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> QKeyValueIterator::operator++(*int*)

这是一个重载函数。

后置 ++ 运算符（`i++`）将迭代器向前移动到容器中的下一个元素并返回指向旧位置元素的迭代器。

**注意：** 将迭代器向前移动到容器的 end() 之后将导致未定义行为。

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> &QKeyValueIterator::operator--()

前置 -- 运算符（`--i`）将迭代器向后前移动到容器中的前一个元素并返回迭代器。

**注意：** 将迭代器向后移动到容器的 begin() 之前将导致未定义行为。

**另请参阅** [operator++](QKeyValueIterator.md#qkeyvalueiteratorkey-t-iterator-qkeyvalueiteratoroperator)().

### [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> QKeyValueIterator::operator--(*int*)

这是一个重载函数。

后置 -- 运算符（`i--`）将迭代器向后前移动到容器中的前一个元素并返回指向旧位置元素的迭代器。

**注意：** 将迭代器向后移动到容器的 begin() 之前将导致未定义行为。

### QKeyValueIterator::pointer QKeyValueIterator::operator->() const

返回指向当前元素的键值对类型的指针。

Qt 5.15 中引入该函数。

**另请参阅** [operator*](QKeyValueIterator.md#stdpairkey-t-qkeyvalueiteratoroperator-const)()。

## 相关非成员函数

### bool operator!=([QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *lhs*, [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *rhs*)

如果 *rhs* 与 *lhs* 指向的元素不同，返回 `true`，否则返回 `false`。

**另请参阅** [operator==](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs-1)()。

### bool operator==([QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *lhs*, [QKeyValueIterator](QKeyValueIterator.md#qkeyvalueiteratorqkeyvalueiterator)<Key, T, Iterator> *rhs*)

如果 *rhs* 与 *lhs* 指向的元素相同，返回 `true`，否则返回 `false`。

**另请参阅** [operator!=](QKeyValueIterator.md#bool-operatorqkeyvalueiteratorkey-t-iterator-lhs-qkeyvalueiteratorkey-t-iterator-rhs)()。