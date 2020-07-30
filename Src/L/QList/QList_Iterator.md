# iterator Class

class [QList](../../L/QList/QList.md)::iterator

The [QList::iterator](https://doc.qt.io/qt-5/qlist-iterator.html) class provides an STL-style non-const iterator for [QList](../../L/QList/QList.md) and [QQueue](../../Q/QQueue/QQueue.md). [More...](QList_Iterator.md#detailed-description)

- [List of all members, including inherited members](https://doc.qt.io/qt-5/qlist-iterator-members.html)



## Public Types

| typedef | **[iterator_category](QList_Iterator.md#typedef-iteratoriteratorcategory)** |
| ------- | ------------------------------------------------------------ |
|         |                                                              |



## Public Functions

|            | **[iterator](QList_Iterator.md#iteratoriteratorconst-iterator-other)**(const iterator &*other*) |
| ---------- | ------------------------------------------------------------ |
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



## Detailed Description

[QList](../../L/QList/QList.md) features both [STL-style iterators](https://doc.qt.io/qt-5/containers.html#stl-style-iterators) and [Java-style iterators](https://doc.qt.io/qt-5/containers.html#java-style-iterators). The STL-style iterators are more low-level and more cumbersome to use; on the other hand, they are slightly faster and, for developers who already know STL, have the advantage of familiarity.

[QList](../../L/QList/QList.md)<T>::iterator allows you to iterate over a [QList](../../L/QList/QList.md)<T> (or [QQueue](../../Q/QQueue/QQueue.md)<T>) and to modify the list item associated with the iterator. If you want to iterate over a const [QList](../../L/QList/QList.md), use [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) instead. It is generally good practice to use [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) on a non-const [QList](../../L/QList/QList.md) as well, unless you need to change the [QList](../../L/QList/QList.md) through the iterator. Const iterators are slightly faster, and can improve code readability.

The default [QList::iterator](https://doc.qt.io/qt-5/qlist-iterator.html) constructor creates an uninitialized iterator. You must initialize it using a [QList](../../L/QList/QList.md) function like [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)(), [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)(), or [QList::insert](../../L/QList/QList.md#void-qlistinsertint-i-const-t-value)() before you can start iterating. Here's a typical loop that prints all the items stored in a list:

```
QList<QString> list;
list.append("January");
list.append("February");
...
list.append("December");

QList<QString>::iterator i;
for (i = list.begin(); i != list.end(); ++i)
    cout << *i << Qt::endl;
```

Let's see a few examples of things we can do with a [QList::iterator](https://doc.qt.io/qt-5/qlist-iterator.html) that we cannot do with a [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html). Here's an example that increments every value stored in a [QList](../../L/QList/QList.md)<int> by 2:

```
QList<int>::iterator i;
for (i = list.begin(); i != list.end(); ++i)
    *i += 2;
```

Most [QList](../../L/QList/QList.md) functions accept an integer index rather than an iterator. For that reason, iterators are rarely useful in connection with [QList](../../L/QList/QList.md). One place where STL-style iterators do make sense is as arguments to [generic algorithms](https://doc.qt.io/qt-5/qtalgorithms.html).

For example, here's how to delete all the widgets stored in a [QList](../../L/QList/QList.md)<[QWidget](../../W/QWidget/QWidget.md) *>:

```
QList<QWidget *> list;
...
qDeleteAll(list.begin(), list.end());
```

Multiple iterators can be used on the same list. However, be aware that any non-const function call performed on the [QList](../../L/QList/QList.md) will render all existing iterators undefined. If you need to keep iterators over a long period of time, we recommend that you use QLinkedList rather than [QList](../../L/QList/QList.md).

**Warning:** Iterators on implicitly shared containers do not work exactly like STL-iterators. You should avoid copying a container while iterators are active on that container. For more information, read [Implicit sharing iterator problem](https://doc.qt.io/qt-5/containers.html#implicit-sharing-iterator-problem).

**See also** [QList::const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) and [QMutableListIterator](../../M/QMutableListIterator/QMutableListIterator.md).

## Member Type Documentation

### typedef iterator::iterator_category

A synonym for *std::random_access_iterator_tag* indicating this iterator is a random access iterator.

## Member Function Documentation

### bool iterator::operator>=(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator>=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if the item pointed to by this iterator is greater than or equal to the item pointed to by the *other* iterator.

### bool iterator::operator>(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator>(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if the item pointed to by this iterator is greater than the item pointed to by the *other* iterator.

### bool iterator::operator<=(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator<=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if the item pointed to by this iterator is less than or equal to the item pointed to by the *other* iterator.

### bool iterator::operator<(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator<(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if the item pointed to by this iterator is less than the item pointed to by the *other* iterator.

### bool iterator::operator!=(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator!=(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if *other* points to a different item than this iterator; otherwise returns `false`.

**See also** [operator==](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### bool iterator::operator==(const [const_iterator](https://doc.qt.io/qt-5/qlist-const-iterator.html) &*other*) const

### bool iterator::operator==(const [iterator](QList_Iterator.md#iteratoriterator) &*other*) const

Returns `true` if *other* points to the same item as this iterator; otherwise returns `false`.

**See also** [operator!=](QList_Iterator.md#bool-iteratoroperatorconst-iterator-other-const)().

### iterator::iterator(const [iterator](QList_Iterator.md#iteratoriterator) &*other*)

Constructs a copy of *other*.

### iterator::iterator()

Constructs an uninitialized iterator.

Functions like operator*() and operator++() should not be called on an uninitialized iterator. Use operator=() to assign a value to it before using it.

**See also** [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)() and [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)().

### T &iterator::operator*() const

Returns a modifiable reference to the current item.

You can change the value of an item by using operator*() on the left side of an assignment, for example:

```
if (*it == "Hello")
    *it = "Bonjour";
```

**See also** [operator->](QList_Iterator.md#t-iteratoroperator-const)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator+(iterator::difference_type *j*) const

Returns an iterator to the item at *j* positions forward from this iterator. (If *j* is negative, the iterator goes backward.)

**See also** [operator-](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)() and [operator+=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)().

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator++()

The prefix ++ operator (`++it`) advances the iterator to the next item in the list and returns an iterator to the new current item.

Calling this function on [QList::end](../../L/QList/QList.md#qlistiterator-qlistend)() leads to undefined results.

**See also** [operator--](QList_Iterator.md#iterator-iteratoroperator)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator++(*int*)

This is an overloaded function.

The postfix ++ operator (`it++`) advances the iterator to the next item in the list and returns an iterator to the previously current item.

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator+=(iterator::difference_type *j*)

Advances the iterator by *j* items. (If *j* is negative, the iterator goes backward.)

**See also** [operator-=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)() and [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator-(iterator::difference_type *j*) const

Returns an iterator to the item at *j* positions backward from this iterator. (If *j* is negative, the iterator goes forward.)

**See also** [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)() and [operator-=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)().

### int iterator::operator-([iterator](QList_Iterator.md#iteratoriterator) *other*) const

Returns the number of items between the item pointed to by *other* and the item pointed to by this iterator.

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator--()

The prefix -- operator (`--it`) makes the preceding item current and returns an iterator to the new current item.

Calling this function on [QList::begin](../../L/QList/QList.md#qlistiterator-qlistbegin)() leads to undefined results.

**See also** [operator++](QList_Iterator.md#iterator-iteratoroperator)().

### [iterator](QList_Iterator.md#iteratoriterator) iterator::operator--(*int*)

This is an overloaded function.

The postfix -- operator (`it--`) makes the preceding item current and returns an iterator to the previously current item.

### [iterator](QList_Iterator.md#iteratoriterator) &iterator::operator-=(iterator::difference_type *j*)

Makes the iterator go back by *j* items. (If *j* is negative, the iterator goes forward.)

**See also** [operator+=](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j)() and [operator-](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().

### T *iterator::operator->() const

Returns a pointer to the current item.

**See also** [operator*](QList_Iterator.md#t-iteratoroperator-const)().

### T &iterator::operator[](iterator::difference_type *j*) const

Returns a modifiable reference to the item at position *this + *j*.

This function is provided to make [QList](../../L/QList/QList.md) iterators behave like C++ pointers.

**See also** [operator+](QList_Iterator.md#iterator-iteratoroperatoriteratordifferencetype-j-const)().