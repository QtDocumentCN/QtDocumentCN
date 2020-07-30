# const_iterator Class

class [QList](../../L/QList/QList.md)::const_iterator

The [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) class provides an STL-style const iterator for [QList](../../L/QList/QList.md) and [QQueue](../../Q/QQueue/QQueue.md). [More...](QList_Const_Iterator.md#detailed-description)

- [List of all members, including inherited members](https://doc.qt.io/qt-5/qlist-const-iterator-members.html)



## Public Types

| typedef | **[iterator_category](QList_Const_Iterator.md#typedef-constiteratoriteratorcategory)** |
| ------- | ------------------------------------------------------------ |
|         |                                                              |



## Public Functions

|                  | **[const_iterator](QList_Const_Iterator.md#constiteratorconstiteratorconst-iterator-other)**(const iterator &*other*) |
| ---------------- | ------------------------------------------------------------ |
|                  | **[const_iterator](QList_Const_Iterator.md#constiteratorconstiteratorconst-constiterator-other)**(const const_iterator &*other*) |
|                  | **[const_iterator](QList_Const_Iterator.md#constiteratorconstiterator)**() |
| bool             | **[operator!=](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| const T &        | **[operator\*](QList_Const_Iterator.md#const-t-constiteratoroperator-const)**() const |
| const_iterator   | **[operator+](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)**(const_iterator::difference_type *j*) const |
| const_iterator & | **[operator++](QList_Const_Iterator.md#constiterator-constiteratoroperator)**() |
| const_iterator   | **[operator++](QList_Const_Iterator.md#constiterator-constiteratoroperatorint)**(*int*) |
| const_iterator & | **[operator+=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)**(const_iterator::difference_type *j*) |
| const_iterator   | **[operator-](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)**(const_iterator::difference_type *j*) const |
| int              | **[operator-](QList_Const_Iterator.md#int-constiteratoroperatorconstiterator-other-const)**(const_iterator *other*) const |
| const_iterator & | **[operator--](QList_Const_Iterator.md#constiterator-constiteratoroperator)**() |
| const_iterator   | **[operator--](QList_Const_Iterator.md#constiterator-constiteratoroperatorint)**(*int*) |
| const_iterator & | **[operator-=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)**(const_iterator::difference_type *j*) |
| const T *        | **[operator->](QList_Const_Iterator.md#const-t-constiteratoroperator-const)**() const |
| bool             | **[operator<](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool             | **[operator<=](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool             | **[operator==](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool             | **[operator>](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| bool             | **[operator>=](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)**(const const_iterator &*other*) const |
| const T &        | **[operator[\]](QList_Const_Iterator.md#const-t-constiteratoroperator-const)**(const_iterator::difference_type *j*) const |



## Detailed Description

[QList](../../L/QList/QList.md) provides both [STL-style iterators](https://doc.qt.io/qt-5/containers.html#stl-style-iterators) and [Java-style iterators](https://doc.qt.io/qt-5/containers.html#java-style-iterators). The STL-style iterators are more low-level and more cumbersome to use; on the other hand, they are slightly faster and, for developers who already know STL, have the advantage of familiarity.

[QList](../../L/QList/QList.md)<T>::const_iterator allows you to iterate over a [QList](../../L/QList/QList.md)<T> (or a [QQueue](../../Q/QQueue/QQueue.md)<T>). If you want to modify the [QList](../../L/QList/QList.md) as you iterate over it, use [QList::iterator](https://doc.qt.io/qt-5/qlist-iterator.html) instead. It is generally good practice to use [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) on a non-const [QList](../../L/QList/QList.md) as well, unless you need to change the [QList](../../L/QList/QList.md) through the iterator. Const iterators are slightly faster, and can improve code readability.

The default [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) constructor creates an uninitialized iterator. You must initialize it using a [QList](../../L/QList/QList.md) function like [QList::constBegin](../../L/QList/QList.md#qlistconstiterator-qlistconstbegin-const)(), [QList::constEnd](../../L/QList/QList.md#qlistconstiterator-qlistconstend-const)(), or [QList::insert](../../L/QList/QList.md#void-qlistinsertint-i-const-t-value)() before you can start iterating. Here's a typical loop that prints all the items stored in a list:

```
QList<QString> list;
list.append("January");
list.append("February");
...
list.append("December");

QList<QString>::const_iterator i;
for (i = list.constBegin(); i != list.constEnd(); ++i)
    cout << *i << Qt::endl;
```

Most [QList](../../L/QList/QList.md) functions accept an integer index rather than an iterator. For that reason, iterators are rarely useful in connection with [QList](../../L/QList/QList.md). One place where STL-style iterators do make sense is as arguments to [generic algorithms](https://doc.qt.io/qt-5/qtalgorithms.html).

For example, here's how to delete all the widgets stored in a [QList](../../L/QList/QList.md)<[QWidget](../../W/QWidget/QWidget.md) *>:

```
QList<QWidget *> list;
...
qDeleteAll(list.constBegin(), list.constEnd());
```

Multiple iterators can be used on the same list. However, be aware that any non-const function call performed on the [QList](../../L/QList/QList.md) will render all existing iterators undefined. If you need to keep iterators over a long period of time, we recommend that you use QLinkedList rather than [QList](../../L/QList/QList.md).

**Warning:** Iterators on implicitly shared containers do not work exactly like STL-iterators. You should avoid copying a container while iterators are active on that container. For more information, read [Implicit sharing iterator problem](https://doc.qt.io/qt-5/containers.html#implicit-sharing-iterator-problem).

**See also** [QList::iterator](https://doc.qt.io/qt-5/qlist-iterator.html) and [QListIterator](../../L/QListIterator/QListIterator.md).

## Member Type Documentation

### typedef const_iterator::iterator_category

A synonym for *std::random_access_iterator_tag* indicating this iterator is a random access iterator.

## Member Function Documentation

### const_iterator::const_iterator(const [iterator](https://doc.qt.io/qt-5/qlist-iterator.html) &*other*)

Constructs a copy of *other*.

### const_iterator::const_iterator(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*)

Constructs a copy of *other*.

### const_iterator::const_iterator()

Constructs an uninitialized iterator.

Functions like operator*() and operator++() should not be called on an uninitialized iterator. Use operator=() to assign a value to it before using it.

**See also** [QList::constBegin](../../L/QList/QList.md#qlistconstiterator-qlistconstbegin-const)() and [QList::constEnd](../../L/QList/QList.md#qlistconstiterator-qlistconstend-const)().

### bool const_iterator::operator!=(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if *other* points to a different item than this iterator; otherwise returns `false`.

**See also** [operator==](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)().

### const T &const_iterator::operator*() const

Returns the current item.

**See also** [operator->](QList_Const_Iterator.md#const-t-constiteratoroperator-const)().

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) const_iterator::operator+(const_iterator::difference_type *j*) const

Returns an iterator to the item at *j* positions forward from this iterator. (If *j* is negative, the iterator goes backward.)

**See also** [operator-](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)() and [operator+=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)().

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &const_iterator::operator++()

The prefix ++ operator (`++it`) advances the iterator to the next item in the list and returns an iterator to the new current item.

Calling this function on [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)() leads to undefined results.

**See also** [operator--](QList_Const_Iterator.md#constiterator-constiteratoroperator)().

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) const_iterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`it++`) advances the iterator to the next item in the list and returns an iterator to the previously current item.

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &const_iterator::operator+=(const_iterator::difference_type *j*)

Advances the iterator by *j* items. (If *j* is negative, the iterator goes backward.)

**See also** [operator-=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)() and [operator+](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)().

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) const_iterator::operator-(const_iterator::difference_type *j*) const

Returns an iterator to the item at *j* positions backward from this iterator. (If *j* is negative, the iterator goes forward.)

**See also** [operator+](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)() and [operator-=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)().

### int const_iterator::operator-([const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) *other*) const

Returns the number of items between the item pointed to by *other* and the item pointed to by this iterator.

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &const_iterator::operator--()

The prefix -- operator (`--it`) makes the preceding item current and returns an iterator to the new current item.

Calling this function on [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)() leads to undefined results.

**See also** [operator++](QList_Const_Iterator.md#constiterator-constiteratoroperator)().

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) const_iterator::operator--(*int*)

This is an overloaded function.

The postfix -- operator (`it--`) makes the preceding item current and returns an iterator to the previously current item.

### [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &const_iterator::operator-=(const_iterator::difference_type *j*)

Makes the iterator go back by *j* items. (If *j* is negative, the iterator goes forward.)

**See also** [operator+=](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j)() and [operator-](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)().

### const T *const_iterator::operator->() const

Returns a pointer to the current item.

**See also** [operator*](QList_Const_Iterator.md#const-t-constiteratoroperator-const)().

### bool const_iterator::operator<(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if the item pointed to by this iterator is less than the item pointed to by the *other* iterator.

### bool const_iterator::operator<=(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if the item pointed to by this iterator is less than or equal to the item pointed to by the *other* iterator.

### bool const_iterator::operator==(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if *other* points to the same item as this iterator; otherwise returns `false`.

**See also** [operator!=](QList_Const_Iterator.md#bool-constiteratoroperatorconst-constiterator-other-const)().

### bool const_iterator::operator>(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if the item pointed to by this iterator is greater than the item pointed to by the *other* iterator.

### bool const_iterator::operator>=(const [const_iterator](QList_Const_Iterator.md#constiteratorconstiterator) &*other*) const

Returns `true` if the item pointed to by this iterator is greater than or equal to the item pointed to by the *other* iterator.

### const T &const_iterator::operator[](const_iterator::difference_type *j*) const

Returns the item at position *this + *j*.

This function is provided to make [QList](../../L/QList/QList.md) iterators behave like C++ pointers.

**See also** [operator+](QList_Const_Iterator.md#constiterator-constiteratoroperatorconstiteratordifferencetype-j-const)().