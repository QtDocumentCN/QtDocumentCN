# 迭代器类

类 [QList](../../L/QList/QList.md)::iterator

[QList::iterator](QList_Iterator.md) 类为 [QList](../../L/QList/QList.md) 和 [QQueue](../../Q/QQueue/QQueue.md) 提供了 STL 风格的非常量迭代器. [更多...](QList_Iterator.md#详细描述)


## 公共成员类型

|         |                                                              |
| ------- | ------------------------------------------------------------ |
| typedef | **[iterator_category](QList_Iterator.md#typedef-iteratoriteratorcategory)** |



## 公共成员函数

|            |                                                              |
| ---------- | ------------------------------------------------------------ |
|            | **[iterator](QList_Iterator.md#iteratoriteratorconst-iterator-other)**(const iterator &*other*) |
|            | **[iterator](QList_Iterator.md#iteratoriterator)**() |
| bool       | **[operator!=](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator!=](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| T &        | **[operator\*](QList_Iterator.md#t-iteratoroperator-const)**() const |
| iterator   | **[operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)**(iterator::difference_type *j*) const |
| iterator & | **[operator++](QList_Iterator.md#iterator-iteratoroperator)**() |
| iterator   | **[operator++](QList_Iterator.md#iterator-iteratoroperatorint)**(*int*) |
| iterator & | **[operator+=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)**(iterator::difference_type *j*) |
| iterator   | **[operator-](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)**(iterator::difference_type *j*) const |
| int        | **[operator-](QList_Iterator.md#int-iteratoroperatoriterator-other-const)**(iterator *other*) const |
| iterator & | **[operator--](QList_Iterator.md#iterator-iteratoroperator)**() |
| iterator   | **[operator--](QList_Iterator.md#iterator-iteratoroperatorint)**(*int*) |
| iterator & | **[operator-=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)**(iterator::difference_type *j*) |
| T *        | **[operator->](QList_Iterator.md#t-iteratoroperator-const)**() const |
| bool       | **[operator<](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator<](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool       | **[operator<=](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator<=](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool       | **[operator==](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator==](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool       | **[operator>](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator>](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool       | **[operator>=](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)**(const iterator &*other*) const |
| bool       | **[operator>=](QList_Iterator.md#bool-iteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| T &        | **[operator[\]](QList_Iterator.md#t-iteratoroperator-const)**(iterator::difference_type *j*) const |



## 详细描述

[QList](../../L/QList/QList.md) 同时支持 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) 和 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)。STL 风格迭代器更偏底层且易用性较差，但在性能上更胜一筹，且对熟悉 STL 的开发者来说能更快上手。

[QList](../../L/QList/QList.md)<T>::iterator 允许你遍历一个 [QList](../../L/QList/QList.md)<T> (或一个 [QQueue](../../Q/QQueue/QQueue.md)<T>) 以及修改列表中和迭代器关联的元素。如果需要遍历一个常量 [QList](../../L/QList/QList.md)，你可以使用 [QList::const_iterator](QList_Const_Iterator.md) 来代替。除非你需要通过迭代器修改一个非常量 [QList](../../L/QList/QList.md)，否则对非常量 [QList](../../L/QList/QList.md) 也继续使用 [QList::const_iterator](QList_Const_Iterator.md) 通常是一个最佳实践。常量迭代器速度上略快，并且可以提升代码可读性。

 [QList::iterator](QList_Iterator.md) 的默认构造函数会创建一个未初始化的迭代器。在迭代之前你必须通过 [QList](../../L/QList/QList.md) 的方法，如 [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)(), [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)(), 或 [QList::insert](../../L/QList/QList.md#void-qlistinsertint-i-const-t-value)() 将其初始化。这是一个常见的打印列表中保存的所有元素的循环:

``` cpp
QList<QString> list;
list.append("January");
list.append("February");
...
list.append("December");

QList<QString>::iterator i;
for (i = list.begin(); i != list.end(); ++i)
    cout << *i << Qt::endl;
```

接下来我们来看几个 [QList::iterator](QList_Iterator.md) 可以实现但 [QList::const_iterator](QList_Const_Iterator.md) 不可以实现的例子。这是一个将保存在 [QList](../../L/QList/QList.md)<int> 的每个元素的值增加2的例子：

```
QList<int>::iterator i;
for (i = list.begin(); i != list.end(); ++i)
    *i += 2;
```

大多数 [QList](../../L/QList/QList.md) 的方法接收一个整型索引而不是一个迭代器作为参数。因此，迭代器实际上在和 [QList](../../L/QList/QList.md) 交互时很少被使用。一个 STL 风格迭代器非常有使用意义的地方是作为[泛型算法](../../A/QtAlgorithms.md)的参数。

例如，下列代码展示了如何删除保存在一个 [QList](../../L/QList/QList.md)<[QWidget](../../W/QWidget/QWidget.md) *> 中的所有物件：

```
QList<QWidget *> list;
...
qDeleteAll(list.begin(), list.end());
```

多个迭代器可以作用在同一个列表上。然而，需要注意的是对该 [QList](../../L/QList/QList.md) 进行任意非常量的方法调用都会使所有已存在的迭代器状态变成未定义。如果需要在一个比较长周期内保证迭代器有效，我们建议你使用 QLinkedList 而不是 [QList](../../L/QList/QList.md)。

**警告：** 支持隐式共享的容器的迭代器的行为和 STL 迭代器并不完全一样。当这类容器的迭代器在使用时你应当避免容器的拷贝。更多信息请阅读 [隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题) 一文。

**另请参见** [QList::const_iterator](QList_Const_Iterator.md) 和 [QMutableListIterator](../../M/QMutableListIterator/QMutableListIterator.md).

## 成员类型文档

### typedef iterator::iterator_category

等同于 *std::random_access_iterator_tag* ，指示该迭代器是一个随机访问迭代器。

## 成员函数文档

### bool iterator::operator>=(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator>=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值大于等于 *other* 迭代器指向的元素的值则返回 `true`。

### bool iterator::operator>(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator>(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值大于 *other* 迭代器指向的元素的值则返回 `true`。

### bool iterator::operator<=(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator<=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值小于等于 *other* 迭代器指向的元素的值则返回 `true`。

### bool iterator::operator<(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator<(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值小于 *other* 迭代器指向的元素的值则返回 `true`。

### bool iterator::operator!=(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator!=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值不等于 *other* 迭代器指向的元素的值则返回 `true`。

**另请参见** [operator==](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### bool iterator::operator==(const [const_iterator](QList_Const_Iterator.md) &*other*) const

### bool iterator::operator==(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

如果该迭代器指向的元素的值等于 *other* 迭代器指向的元素的值则返回 `true`。

**另请参见** [operator!=](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### iterator::iterator(const [iterator](QList_Iterator.md#iteratoriterator) &*other*)

构造一个 *other* 的副本。

### iterator::iterator()

构造一个未初始化的迭代器。

类似于 operator*() and operator++() 的方法不允许对未初始化的迭代器调用，在使用前先通过 operator=() 进行赋值。

**另请参见** [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)() 和 [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)().

### T &iterator::operator*() const

返回一个可修改当前元素的引用。

你可以通过在赋值操作左侧使用 operator*() 来改变一个元素的值。例如：

```
if (*it == "Hello")
    *it = "Bonjour";
```

**另请参见** [operator->](QList_Iterator.md#t-iteratoroperator-const)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator+(iterator::difference_type *j*) const

返回一个指向当前迭代器向列表尾部移动 *j* 步的位置的元素的迭代器。(如果 *j* 为负值，则迭代器向列表头部移动。)

**另请参见** [operator-](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)() 和 [operator+=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)().

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator++()

前缀 ++ 运算符(`++it`)将迭代器向列表尾部移动到列表中的下一个元素并返回一个指向移动后的元素的迭代器。

对 [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)() 调用该方法是未定义行为。

**另请参见** [operator--](QList_Iterator.md#iterator-iteratoroperator)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator++(*int*)

这是一个重载函数。

后缀 ++ 运算符(`++it`)将迭代器向列表尾部移动到列表中的下一个元素并返回一个指向移动前的元素的迭代器。

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator+=(iterator::difference_type *j*)

将该迭代器列表尾部移动 *j* 个元素。(如果 *j* 为负值，则向列表头部移动)

**另请参见** [operator-=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)() 和 [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator-(iterator::difference_type *j*) const

返回一个指向当前迭代器向列表头部移动 *j* 步的位置的元素的迭代器。(如果 *j* 为负值，则迭代器向列表尾部移动。)

**另请参见** [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)() 和 [operator-=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)().

### int iterator::operator-([iterator](QList_Iterator.md#iteratoriterator) *other*) const

返回 *other* 指向的元素和该迭代器指向元素之间间隔的元素个数。

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator--()

前缀 -- 运算符(`--it`)将迭代器向列表头部移动到列表中的上一个元素并返回一个指向移动后的元素的迭代器。

对 [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)() 调用该方法是未定义行为。

**另请参见** [operator++](QList_Iterator.md#iterator-iteratoroperator)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator--(*int*)

这是一个重载函数。

前缀 -- 运算符(`--it`)将迭代器向列表头部移动到列表中的上一个元素并返回一个指向移动前的元素的迭代器。

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator-=(iterator::difference_type *j*)

将迭代器向列表头部回退 *j* 元素。(如果 *j* 为负值，则迭代器向列表尾部移动。)

**另请参见** [operator+=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)() 和 [operator-](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().

### T *iterator::operator->() const

返回一个指向当前元素的指针。

**另请参见** [operator*](QList_Iterator.md#t-iteratoroperator-const)().

### T &iterator::operator[](iterator::difference_type *j*) const

返回一个可修改位于 *this* + *j* 的元素的引用。

提供该方法是为了使 [QList](../../L/QList/QList.md) 迭代器行为类似 C++ 指针。

**另请参见** [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().
