# QList Class

`template <typename T> class QList`

QList 类是一个用于提供列表支持的模板类。[更多...](QList.md#details)

|               |                                                                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 头文件:       | #include \<QList>                                                                                                                      |
| qmake:        | QT += core                                                                                                                               |
| 子类: | [QByteArrayList](../../B/QByteArrayList/QByteArrayList.md), [QItemSelection](../../I/QItemSelection/QItemSelection.md), [QQueue](../../Q/QQueue/QQueue.md) 和 [QStringList](../../S/QStringList/QStringList.md) |

**注意：** 本页面提到的方法都是[可重入的](../../T/Thread_Reentrancy/Thread_Reentrancy.md)。

## 公共成员类型

|         |                                                                           |
| ------- | ------------------------------------------------------------------------- |
| class   | **[const_iterator](QList_Const_Iterator.md)**                          |
| class   | **[iterator](QList_Iterator.md)**                                       |
| typedef | **[ConstIterator](QList.md#typedef-qlistconstiterator)**                     |
| typedef | **[Iterator](QList.md#typedef-qlistiterator)**                               |
| typedef | **[const_pointer](QList.md#typedef-qlistconstpointer)**                    |
| typedef | **[const_reference](QList.md#typedef-qlistconstreference)**                |
| typedef | **[const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator)** |
| typedef | **[difference_type](QList.md#typedef-qlistdifferencetype)**                |
| typedef | **[pointer](QList.md#typedef-qlistpointer)**                                 |
| typedef | **[reference](QList.md#typedef-qlistreference)**                             |
| typedef | **[reverse_iterator](QList.md#typedef-qlistreverseiterator)**              |
| typedef | **[size_type](QList.md#typedef-qlistsizetype)**                            |
| typedef | **[value_type](QList.md#typedef-qlistvaluetype)**                          |

## 公共成员方法

|                                 |                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------- |
|                                 | **[QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)**(InputIterator *first*, InputIterator *last*)       |
|                                 | **[QList](QList.md#qlistqliststdinitializerlistt-args)**(std::initializer_list<T> *args*)                |
|                                 | **[QList](QList.md#qlistqlistqlistt-other)**(QList<T> &&*other*)                              |
|                                 | **[QList](QList.md#qlistqlistconst-qlistt-other)**(const QList<T> &*other*)                         |
|                                 | **[QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)**()                                                    |
| QList<T> &                    | **[operator=](QList.md#qlistt-qlistoperatorqlistt-other)**(QList<T> &&*other*)                    |
| QList<T> &                    | **[operator=](QList.md#qlistt-qlistoperatorqlistt-other)**(const QList<T> &*other*)                 |
|                                 | **[~QList](QList.md#qlistqlist)**()                                             |
| void                            | **[append](QList.md#void-qlistappendconst-t-value)**(const T &*value*)                                  |
| void                            | **[append](QList.md#void-qlistappendconst-qlistt-value)**(const QList<T> &*value*)                       |
| const T &                       | **[at](QList.md#const-t-qlistatint-i-const)**(int *i*) const                                             |
| T &                             | **[back](QList.md#t-qlistback)**()                                                      |
| const T &                       | **[back](QList.md#const-t-qlistback-const)**() const                                              |
| QList::iterator                 | **[begin](QList.md#qlistiterator-qlistbegin)**()                                                    |
| QList::const_iterator          | **[begin](QList.md#qlistconstiterator-qlistbegin-const)**() const                                            |
| QList::const_iterator          | **[cbegin](QList.md#qlistconstiterator-qlistcbegin-const)**() const                                            |
| QList::const_iterator          | **[cend](QList.md#qlistconstiterator-qlistcend-const)**() const                                                |
| void                            | **[clear](QList.md#void-qlistclear)**()                                                    |
| QList::const_iterator          | **[constBegin](QList.md#qlistconstiterator-qlistconstbegin-const)**() const                                    |
| QList::const_iterator          | **[constEnd](QList.md#qlistconstiterator-qlistconstend-const)**() const                                        |
| const T &                       | **[constFirst](QList.md#const-t-qlistconstfirst-const)**() const                                    |
| const T &                       | **[constLast](QList.md#const-t-qlistconstlast-const)**() const                                      |
| bool                            | **[contains](QList.md#bool-qlistcontainsconst-t-value-const)**(const T &*value*) const                        |
| int                             | **[count](QList.md#int-qlistcountconst-t-value-const)**(const T &*value*) const                              |
| int                             | **[count](QList.md#int-qlistcount-const)**() const                                            |
| QList::const_reverse_iterator | **[crbegin](QList.md#qlistconstreverseiterator-qlistcrbegin-const)**() const                                          |
| QList::const_reverse_iterator | **[crend](QList.md#qlistconstreverseiterator-qlistcrend-const)**() const                                              |
| bool                            | **[empty](QList.md#bool-qlistempty-const)**() const                                              |
| QList::iterator                 | **[end](QList.md#qlistiterator-qlistend)**()                                                        |
| QList::const_iterator          | **[end](QList.md#qlistconstiterator-qlistend-const)**() const                                                |
| bool                            | **[endsWith](QList.md#bool-qlistendswithconst-t-value-const)**(const T &*value*) const                        |
| QList::iterator                 | **[erase](QList.md#qlistiterator-qlisteraseqlistiterator-pos)**(QList::iterator *pos*)                               |
| QList::iterator                 | **[erase](QList.md#qlistiterator-qlisteraseqlistiterator-begin-qlistiterator-end)**(QList::iterator *begin*, QList::iterator *end*)    |
| T &                             | **[first](QList.md#t-qlistfirst)**()                                                    |
| const T &                       | **[first](QList.md#const-t-qlistfirst-const)**() const                                            |
| T &                             | **[front](QList.md#t-qlistfront)**()                                                    |
| const T &                       | **[front](QList.md#const-t-qlistfront-const)**() const                                            |
| int                             | **[indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)**(const T &*value*, int *from* = 0) const          |
| void                            | **[insert](QList.md#void-qlistinsertint-i-const-t-value)**(int *i*, const T &*value*)                         |
| QList::iterator                 | **[insert](QList.md#qlistiterator-qlistinsertqlistiterator-before-const-t-value)**(QList::iterator *before*, const T &*value*)      |
| bool                            | **[isEmpty](QList.md#bool-qlistisempty-const)**() const                                          |
| T &                             | **[last](QList.md#t-qlistlast)**()                                                      |
| const T &                       | **[last](QList.md#const-t-qlistlast-const)**() const                                              |
| int                             | **[lastIndexOf](QList.md#int-qlistlastindexofconst-t-value-int-from--1-const)**(const T &*value*, int *from* = -1) const |
| int                             | **[length](QList.md#int-qlistlength-const)**() const                                            |
| QList<T>                      | **[mid](QList.md#qlistt-qlistmidint-pos-int-length--1-const)**(int *pos*, int *length* = -1) const                      |
| void                            | **[move](QList.md#void-qlistmoveint-from-int-to)**(int *from*, int *to*)                                  |
| void                            | **[pop_back](QList.md#void-qlistpopback)**()                                             |
| void                            | **[pop_front](QList.md#void-qlistpopfront)**()                                           |
| void                            | **[prepend](QList.md#void-qlistprependconst-t-value)**(const T &*value*)                                |
| void                            | **[push_back](QList.md#void-qlistpushbackconst-t-value)**(const T &*value*)                           |
| void                            | **[push_front](QList.md#void-qlistpushfrontconst-t-value)**(const T &*value*)                         |
| QList::reverse_iterator        | **[rbegin](QList.md#qlistreverseiterator-qlistrbegin)**()                                                  |
| QList::const_reverse_iterator | **[rbegin](QList.md#qlistconstreverseiterator-qlistrbegin-const)**() const                                          |
| int                             | **[removeAll](QList.md#int-qlistremoveallconst-t-value)**(const T &*value*)                            |
| void                            | **[removeAt](QList.md#void-qlistremoveatint-i)**(int *i*)                                       |
| void                            | **[removeFirst](QList.md#void-qlistremovefirst)**()                                        |
| void                            | **[removeLast](QList.md#void-qlistremovelast)**()                                          |
| bool                            | **[removeOne](QList.md#bool-qlistremoveoneconst-t-value)**(const T &*value*)                            |
| QList::reverse_iterator        | **[rend](QList.md#qlistreverseiterator-qlistrend)**()                                                      |
| QList::const_reverse_iterator | **[rend](QList.md#qlistconstreverseiterator-qlistrend-const)**() const                                              |
| void                            | **[replace](QList.md#void-qlistreplaceint-i-const-t-value)**(int *i*, const T &*value*)                       |
| void                            | **[reserve](QList.md#void-qlistreserveint-alloc)**(int *alloc*)                                     |
| int                             | **[size](QList.md#typedef-qlistsizetype)**() const                                                |
| bool                            | **[startsWith](QList.md#bool-qliststartswithconst-t-value-const)**(const T &*value*) const                    |
| void                            | **[swap](QList.md#void-qlistswapqlistt-other)**(QList<T> &*other*)                                   |
| void                            | **[swapItemsAt](QList.md#void-qlistswapitemsatint-i-int-j)**(int *i*, int *j*)                        |
| T                               | **[takeAt](QList.md#t-qlisttakeatint-i)**(int *i*)                                           |
| T                               | **[takeFirst](QList.md#t-qlisttakefirst)**()                                            |
| T                               | **[takeLast](QList.md#t-qlisttakelast)**()                                              |
| QSet<T>                       | **[toSet](QList.md#qsett-qlisttoset-const)**() const                                              |
| std::list<T>                  | **[toStdList](QList.md#stdlistt-qlisttostdlist-const)**() const                                      |
| QVector<T>                    | **[toVector](QList.md#qvectort-qlisttovector-const)**() const                                        |
| T                               | **[value](QList.md#typedef-qlistvaluetype)**(int *i*) const                                       |
| T                               | **[value](QList.md#t-qlistvalueint-i-const-t-defaultvalue-const)**(int *i*, const T &*defaultValue*) const            |
| bool                            | **[operator!=](QList.md#bool-qlistoperatorconst-qlistt-other-const)**(const QList<T> &*other*) const     |
| QList<T>                      | **[operator+](QList.md#qlistt-qlistoperatorconst-qlistt-other-const)**(const QList<T> &*other*) const           |
| QList<T> &                    | **[operator+=](QList.md#qlistt-qlistoperatorconst-qlistt-other)**(const QList<T> &*other*)             |
| QList<T> &                    | **[operator+=](QList.md#qlistt-qlistoperatorconst-t-value)**(const T &*value*)                    |
| QList<T> &                    | **[operator<<](QList.md#qlistt-qlistoperatorconst-qlistt-other)**(const QList<T> &*other*)           |
| QList<T> &                    | **[operator<<](QList.md#qlistt-qlistoperatorconst-t-value)**(const T &*value*)                  |
| bool                            | **[operator==](QList.md#bool-qlistoperatorconst-qlistt-other-const)**(const QList<T> &*other*) const       |
| T &                             | **[operator[]](QList.md#t-qlistoperator)**(int *i*)                             |
| const T &                       | **[operator[]](QList.md#const-t-qlistoperator-const)**(int *i*) const                     |

## 静态公共成员

|            |                                                                         |
| ---------- | ----------------------------------------------------------------------- |
| QList<T> | **[fromSet](QList.md#static-qlistt-qlistfromsetconst-qsett-set)**(const QSet<T> &*set*)               |
| QList<T> | **[fromStdList](QList.md#static-qlistt-qlistfromstdlistconst-stdlistt-list)**(const std::list<T> &*list*) |
| QList<T> | **[fromVector](QList.md#static-qlistt-qlistfromvectorconst-qvectort-vector)**(const QVector<T> &*vector*)   |

## 相关非成员函数

|               |                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------- |
| uint          | **[qHash](QList.md#template-typename-t-uint-qhashconst-qlistt-key-uint-seed--0)**(const QList<T> &*key*, uint *seed* = 0)                        |
| bool          | **[operator<](QList.md#qlistt-qlistoperatorconst-qlistt-other)**(const QList<T> &*lhs*, const QList<T> &*rhs*)     |
| QDataStream & | **[operator<<](QList.md#template-typename-t-qdatastream-operatorqdatastream-out-const-qlistt-list)**(QDataStream &*out*, const QList<T> &*list*) |
| bool          | **[operator<=](QList.md#template-typename-t-bool-operatorconst-qlistt-lhs-const-qlistt-rhs)**(const QList<T> &*lhs*, const QList<T> &*rhs*) |
| bool          | **[operator>](QList.md#template-typename-t-bool-operatorconst-qlistt-lhs-const-qlistt-rhs)**(const QList<T> &*lhs*, const QList<T> &*rhs*)     |
| bool          | **[operator>=](QList.md#template-typename-t-bool-operatorconst-qlistt-lhs-const-qlistt-rhs)**(const QList<T> &*lhs*, const QList<T> &*rhs*) |
| QDataStream & | **[operator>>](QList.md#template-typename-t-qdatastream-operatorqdatastream-in-qlistt-list)**(QDataStream &*in*, QList<T> &*list*)           |

## 详细描述

QList<T> 是 [Qt 泛型容器](../../C/Container_Classes/Container_Classes.md)之一，通过列表保存元素，提供了基于索引的快速访问以及基于索引的插入和删除功能。

QList<T>，QLinkedList<T> 和 [QVector](../../V/QVector/QVector.md)<T> 提供了类似的接口和功能。 大部分情况下它们之间是可以互相替换的，但可能会带来一些性能问题。这里有一个各自适用场景的总结：

- [QVector](../../V/QVector/QVector.md) 应当是你的默认首选。[QVector](../../V/QVector/QVector.md)<T> 的性能通常要优于 QList<T>, 因为 [QVector](../../V/QVector/QVector.md)<T> 总是在内存中连续存储其元素，而 QList<T> 则只会在`sizeof(T) <= sizeof(void*)` 且通过 [Q_DECLARE_TYPEINFO](../../G/QtGlobal/QtGlobal.md#qdeclaretypeinfotype-flags) 将 T 声明为 `Q_MOVABLE_TYPE` 或 `Q_PRIMITIVE_TYPE` 的情况下才会这么做，否则将会在堆上分配其元素的内存。[QList 使用利弊分析](http://marcmutz.wordpress.com/effective-qt/containers/#containers-qlist) 一文对此做了解释。
- 然而，QList 在 Qt API 中总是被用来传递参数和保存返回值，和这些 API 交互时请使用 QList。
- 如果你需要一个真正的基于链表实现的列表，以保证列表中间插入元素是[常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)以及基于迭代器而不是索引来访问元素，你可以使用 QLinkedList。

**注意:** [QVector](../../V/QVector/QVector.md) 和 [QVarLengthArray](../../V/QVarLengthArray/QVarLengthArray.md) 都提供了对 C 数组内存布局的兼容，但 QList 不保证这一点。这一点在你的应用需要和 C API 交互时可能会非常重要。

**注意:** QLinkedList 的迭代器和在堆上分配内存的 QList 的引用只要其指向的元素还在容器中，将会一直保持有效。但 [QVector](../../V/QVector/QVector.md) 和非在堆上分配内存的的 QList 的迭代器以及引用并不保证这一点。

内部实现中，如果 `sizeof(T) <= sizeof(void*)` 且通过 [Q_DECLARE_TYPEINFO](../../G/QtGlobal/QtGlobal.md#qdeclaretypeinfotype-flags) 将 T 声明为 `Q_MOVABLE_TYPE` 或 `Q_PRIMITIVE_TYPE` 时，QList<T> 将表现为一个 T 类型的数组。否则，QList<T> 表现为一个 T* 类型的数组，元素实际在堆上分配内存。

基于数组的实现的 QList 支持快速插入和基于索引的访问。[prepend](QList.md#void-qlistprependconst-t-value)() and [append](QList.md#void-qlistappendconst-t-value)() 操作也非常快，因为 QList 在内部数组的头尾均预分配了内存。（详见[算法复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)）

注意，如果上面的条件不能满足，每一次追加或插入一个新的元素都需要在堆上分配这个新元素的内存。这会导致在有大量元素的追加和插入时使用 [QVector](../../V/QVector/QVector.md) 成为一个更好的选择，因为 [QVector](../../V/QVector/QVector.md) 可以在一次性为多个元素在堆上分配内存。

另一个需要注意的是内部数组在列表的整个生命周期内只会不断增大，永远不会缩小。内部数组将会在列表析构时调用的析构函数或列表被赋予另一个列表时调用的赋值运算符函数中被析构。

下方是使用 QList 保存整型数字和使用 QList 保存 [QDate](../../D/QDate/QDate.md) 的例子:

``` cpp
QList<int> integerList;
QList<QDate> dateList;
```

Qt 提供了 [QStringList](../../S/QStringList/QStringList.md) 类，其继承于 QList<[QString](../../S/QString/QString.md)> ，提供了一些快捷方法，例如 [QStringList::join](../../S/QStringList/QStringList.md#qstring-qstringlistjoinconst-qstring-separator-const)() 和 [QStringList::filter](../../S/QStringList/QStringList.md#qstringlist-qstringlistfilterconst-qstring-str-qtcasesensitivity-cs--qtcasesensitive-const)()。[QString::split](../../S/QString/QString.md#qstringlist-qstringsplitconst-qstring-sep-qtsplitbehavior-behavior--qtkeepemptyparts-qtcasesensitivity-cs--qtcasesensitive-const)() 用于从 QString 创建 QStringList。

QList 以列表的形式保存元素，默认构造函数会创建一个空列表，你可以使用带有初始化列表的构造函数创建出一个带有元素的的列表：

``` cpp
QList<QString> list = { "one", "two", "three" };
```

QList 提供了这些基础方法用于添加，移动和删除元素：[insert](QList.md#void-qlistinsertint-i-const-t-value)(), [replace](QList.md#void-qlistreplaceint-i-const-t-value)(), [removeAt](QList.md#void-qlistremoveatint-i)(), [move](QList.md#void-qlistmoveint-from-int-to)() 和 [swap](QList.md#void-qlistswapqlistt-other)()。另外，它还提供了下列快捷方法：[append](QList.md#void-qlistappendconst-t-value)(), [operator`<<`](QList.md#qlistt-qlistoperatorconst-qlistt-other)(), [operator+=](QList.md#qlistt-qlistoperatorconst-qlistt-other)(), [prepend](QList.md#void-qlistprependconst-t-value)(), [removeFirst](QList.md#void-qlistremovefirst)() 和 [removeLast](QList.md#void-qlistremovelast)()。

[operator`<<`](QList.md#qlistt-qlistoperatorconst-qlistt-other)() 可以方便地添加多个元素到列表中:

``` cpp
list << "four" << "five";
```

和 C++ 数组一样，QList 索引从 0 开始。要访问在指定位置的元素，你可以使用 `operator[]()`。对于非常量列表，`operator[]()` 用于返回一个元素的引用，可以被用在赋值运算符的左侧（译注：即可作为左值）：

``` cpp
if (list[0] == "Bob")
    list[0] = "Robert";
```

由于对于大小大于一个指针或不可移动的元素类型，QList 基于该类型的指针数组实现，因此该操作需要([常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度))。对于只读访问，一个可替代的语法是使用 [at](QList.md#const-t-qlistatint-i-const)()：

``` cpp
for (int i = 0; i < list.size(); ++i) {
    if (list.at(i) == "Jane")
        cout << "Found Jane at position " << i << Qt::endl;
}
```

[at](QList.md#const-t-qlistatint-i-const)() 可能会比 `operator[]()` 快，因为其永远不会导致[深拷贝](../../I/Implicit_Sharing/Implicit_Sharing.md#深拷贝)的发生。

从列表中移除一个元素，然后对其做一些处理是一个很常用的操作。QList 提供了 [takeAt](QList.md#t-qlisttakeatint-i)(), [takeFirst](QList.md#t-qlisttakefirst)() 和 [takeLast](QList.md#t-qlisttakelast)() 来实现该操作。下面是一个将元素逐个从列表中移除并对该元素调用 `delete` 的循环实现：

``` cpp
QList<QWidget *> list;
..。
while (!list.isEmpty())
    delete list.takeFirst();
```

在列表两端插入或删除元素是非常快的（通常是[常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度))，因为QList在内部缓存的两端都预分配了额外的内存空间用于支持列表两端的快速增长。

如果需要在列表中查找所有特定值的元素的索引，可以使用 [indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)() 或 [lastIndexOf](QList.md#int-qlistlastindexofconst-t-value-int-from--1-const)()。前一个用于从给定的索引位置向列表尾部方向查找，后一个则相反。二者都会在找到时返回匹配元素的索引，未找到时返回 -1。例如:

``` cpp
int i = list.indexOf("Jane");
if (i != -1)
    cout << "Jane 首次出现的位置是 " << i << Qt::endl;
```

如果你仅仅是想简单地检查特定值是否存在于列表中，可以使用 [contains](QList.md#bool-qlistcontainsconst-t-value-const)()。如果你想要统计特定值在列表中出现的次数，可以使用 [count](QList.md#int-qlistcount-const)()。如果你想将所有特定值替换为一个另一个指定值，可以使用 [replace](QList.md#void-qlistreplaceint-i-const-t-value)()。

QList 中的元素类型必须是 [可赋值数据类型](../../C/Container_Classes/Container_Classes.md#可赋值类型)。绝大部分常用数据类型都满足这一点，但某些情况编译器可能会报错，例如以值的形式保存 [QWidget](../../W/QWidget/QWidget.md)，可改成保存 [QWidget](../../W/QWidget/QWidget.md) * 来代替。一些方法会有额外的要求，例如，[indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)() 和 [lastIndexOf](QList.md#int-qlistlastindexofconst-t-value-int-from--1-const)() 要求值类型支持 `operator==()` 运算符。这些要求在每个函数的文档中有说明。

正如其他的容器类一样，QList 提供了 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)([QListIterator](../../L/QListIterator/QListIterator.md) 和 [QMutableListIterator](../../M/QMutableListIterator/QMutableListIterator.md)) 和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) ([QList::const_iterator](QList_Const_Iterator.md) 和 [QList::iterator](QList_Iterator.md))。实际使用中，这些迭代器其实很少被使用，因为你可以使用列表索引。QList 的实现使得直接基于索引访问的方式实现和使用迭代器一样快。

QList 并 *不* 支持通过其元素的引用来进行插入，头部追加，尾部追加和替换，这样做会导致你的应用崩溃并显示错误信息。

为了使 QList 尽可能高效，其成员函数在使用前并不会对输入进行校验，但 [isEmpty](QList.md#bool-qlistisempty-const)() 例外，成员函数通常会假定列表 *不* 为空。带有索引值作为参数的的成员函数总是会假定索引值位于合法的范围内。这意味着 QList 成员函数可能会调用失败。如果在编译时定义了 `QT_NO_DEBUG`，这些错误将不会被检测到。而如果 *没有* 定义 `QT_NO_DEBUG`，此类错误将会通过 [Q_ASSERT](../../G/QtGlobal/QtGlobal.md#void-qasserttest)() 或 [Q_ASSERT_X](../../G/QtGlobal/QtGlobal.md#void-qassertxtest-const-char-where-const-char-what)() 被检测到并显示对应的错误信息。

为了避免在在列表可能为空时报错，在调用其他成员函数前应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 检查。如果你必须传递一个可能不在有效范围内的索引值，应先检查其是否小于 [size](QList.md#typedef-qlistsizetype)() 的返回值且 *不* 小于0。

### 更多成员

如果 T 是 [QByteArray](../../B/QByteArray/QByteArray.md) 类型，这个类会提供更多可以使用的成员，详见 [QByteArrayList](../../B/QByteArrayList/QByteArrayList.md)。

如果 T 是 [QString](../../S/QString/QString.md) 类型，这个类提供了这些额外的成员函数：[filter](../../S/QStringList/QStringList.md#qstringlist-qstringlistfilterconst-qstring-str-qtcasesensitivity-cs--qtcasesensitive-const), [join](../../S/QStringList/QStringList.md#qstring-qstringlistjoinconst-qstring-separator-const), [removeDuplicates](../../S/QStringList/QStringList.md#int-qstringlistremoveduplicates), [sort](../../S/QStringList/QStringList.md#void-qstringlistsortqtcasesensitivity-cs--qtcasesensitive)。

### 使用 Qt 容器的更多信息

如果想要详细了解 Qt 和 STL 对应容器之间的对比，可阅读 [理解 Qt 容器](http://marcmutz.wordpress.com/effective-qt/containers/)一文。

**另请参阅：** [QListIterator](../../L/QListIterator/QListIterator.md), [QMutableListIterator](../../M/QMutableListIterator/QMutableListIterator.md), [QLinkedList](../../L/QLinkedList/QLinkedList.md) 和 [QVector](../../V/QVector/QVector.md)。

## 成员类型文档

### typedef QList::ConstIterator

Qt 风格的 [QList::const_iterator](QList_Const_Iterator.md) 的同义词。

### typedef QList::Iterator

Qt 风格的 [QList::iterator](QList_Iterator.md) 的同义词。

### typedef QList::const_pointer

`const T *` 的类型别名，提供了对 STL 的兼容。

### typedef QList::const_reference

`const T &` 的类型别名，提供了对 STL 的兼容。

### typedef QList::const_reverse_iterator

QList::const_reverse_iterator 仅仅是 `std::reverse_iterator<const_iterator>` 的类型别名，用于提供 STL 风格的 [QList](../../L/QList/QList.md) 常量反向迭代器。

**警告：** 支持隐式共享的容器的迭代器的行为和 STL 迭代器并不完全一样。当这类容器的迭代器在使用时你应当避免容器的拷贝。更多信息请阅读 [隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题) 一文。

该类型在 Qt 5.6 中引入。

**另请参阅** [QList::rbegin](QList.md#qlistreverseiterator-qlistrbegin)(), [QList::rend](QList.md#qlistreverseiterator-qlistrend)(), [QList::reverse_iterator](QList.md#typedef-qlistreverseiterator) 和[QList::const_iterator](QList_Const_Iterator.md)。

### typedef QList::difference_type

`ptrdiff_t` 的别名，提供了对 STL 的兼容。

### typedef QList::pointer

`T *` 的别名，提供了对 STL 的兼容。

### typedef QList::reference

`T &` 的别名，提供了对 STL 的兼容。

### typedef QList::reverse_iterator

QList::reverse_iterator 仅仅是 `std::reverse_iterator<iterator>` 的类型别名，用于提供 STL 风格的 [QList](../../L/QList/QList.md) 非常量反向迭代器。

**警告：** 支持隐式共享的容器的迭代器的行为和 STL 迭代器并不完全一样。当这类容器的迭代器在使用时你应当避免容器的拷贝。更多信息请阅读 [隐式共享迭代器问题](../../C/Container_Classes/Container_Classes.md#隐式共享迭代器问题) 一文。

该类型在 Qt 5.6 中引入。

**另请参阅** [QList::rbegin](QList.md#qlistreverseiterator-qlistrbegin)(), [QList::rend](QList.md#qlistreverseiterator-qlistrend)(), [QList::const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator) 和 [QList::iterator](QList_Iterator.md)。

### typedef QList::size_type

`int` 类型的别名，提供了对 STL 的兼容。

### typedef QList::value_type

`T` 类型的别名，提供了对 STL 的兼容。

## 成员函数文档

### template <typename InputIterator> QList::QList(InputIterator *first*, InputIterator *last*)

使用迭代器范围 [*first*, *last*)指定的内容构造一个 QList。

`InputIterator` 的值类型必须可转换为 `T`。

该方法在 Qt 5.14 中引入。

### QList::QList(std::initializer_list<T> *args*)

从由 *args* 指定的 std::initializer_list 构造一个列表。

此构造函数仅在编译器支持 C++11 初始化列表特性时可用。

该方法在 Qt 4.8 中引入。

### QList::QList([QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &&*other*)

移动构造一个 QList 实例，使它和 *other* 指向同一个对象。

该方法在 Qt 5.2 中引入。

### QList::QList(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*)

构造一个 *other* 的拷贝。

该操作为 [常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)，因为 QList 是[隐式共享](../../I/Implicit_Sharing/Implicit_Sharing.md)的，所以一个函数返回 QList 是非常快的。如果一个共享实例被修改了，其将会被复制一份（写时拷贝），复杂度为[线性时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)。

**另请参阅** [operator=](QList.md#qlistt-qlistoperatorqlistt-other)()。

### QList::QList()

构造一个空列表。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator=([QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &&*other*)

移动赋值 *other* 给该 [QList](../../L/QList/QList.md) 实例。

该方法在 Qt 5.2 中引入。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator=(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*)

将 *other* 赋值给当前列表，然后返回当前列表的引用。

### QList::~QList()

析构列表。列表中的值的引用及所有的迭代器都将失效。

### void QList::append(const T &*value*)

插入 *value* 到列表尾部。

示例：

``` cpp
QList<QString> list;
list.append("one");
list.append("two");
list.append("three");
// list: ["one", "two", "three"]
```

该方法等同于 list.insert([size](QList.md#typedef-qlistsizetype)(), *value*)。

如果该列表是非共享的，那么此操作通常会非常快（均摊下来为 [常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为[QList](../../L/QList/QList.md) 在内部缓存的两端都预分配了额外的内存空间用于支持列表两端的快速增长。

**另请参阅** [operator`<<`](QList.md#qlistt-qlistoperatorconst-qlistt-other)(), [prepend](QList.md#void-qlistprependconst-t-value)() 和 [insert](QList.md#void-qlistinsertint-i-const-t-value)()。

### void QList::append(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*value*)

这是个重载函数。

插入另一个列表 *value* 中的元素到列表尾部。

该方法在 Qt 4.5 中引入。

**另请参阅** [operator`<<`](QList.md#qlistt-qlistoperatorconst-qlistt-other)() 和 [operator+=](QList.md#qlistt-qlistoperatorconst-qlistt-other)()。

### const T &QList::at(int *i*) const

返回位于列表索引位置为 *i* 的元素。*i* 必须是列表中合法的索引位置 (例如，0 `<=` *i* `<` [size](QList.md#typedef-qlistsizetype)()）。

该方法非常快，为([常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度))。

**另请参阅** [value](QList.md#typedef-qlistvaluetype)() 和 [operator[]](QList.md#t-qlistoperator)()。

### T &QList::back()

该方法用于提供对 STL 的兼容，等同于 [last](QList.md#t-qlistlast)()。该方法要求列表不能为空， 如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

### const T &QList::back() const

这是个重载函数。

### [QList::iterator](QList_Iterator.md) QList::begin()

返回一个指向列表第一个元素的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)

**另请参阅** [constBegin](QList.md#qlistconstiterator-qlistconstbegin-const)() 和 [end](QList.md#qlistiterator-qlistend)()。

### [QList::const_iterator](QList_Const_Iterator.md) QList::begin() const

这是个重载函数。

### [QList::const_iterator](QList_Const_Iterator.md) QList::cbegin() const

返回指向列表中第一个元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

该方法在 Qt 5.0 中引入。

**另请参阅** [begin](QList.md#qlistiterator-qlistbegin)() and [cend](QList.md#qlistconstiterator-qlistcend-const)()。

### [QList::const_iterator](QList_Const_Iterator.md) QList::cend() const

返回一个指向位于最后一个元素之后的虚拟元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

该方法在 Qt 5.0 中引入。

**另请参阅** [cbegin](QList.md#qlistconstiterator-qlistcbegin-const)() and [end](QList.md#qlistiterator-qlistend)()。

### void QList::clear()

移除列表中所有的元素。

**另请参阅** [removeAll](QList.md#int-qlistremoveallconst-t-value)()。

### [QList::const_iterator](QList_Const_Iterator.md) QList::constBegin() const

返回指向列表中第一个元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

**另请参阅** [begin](QList.md#qlistiterator-qlistbegin)() 和 [constEnd](QList.md#qlistconstiterator-qlistconstend-const)()。

### [QList::const_iterator](QList_Const_Iterator.md) QList::constEnd() const

返回一个指向位于最后一个元素之后的虚拟元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

**另请参阅** [constBegin](QList.md#qlistconstiterator-qlistconstbegin-const)() 和 [end](QList.md#qlistiterator-qlistend)()。

### const T &QList::constFirst() const

返回一个列表中第一个元素的常量引用，列表必须不为空。如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

该方法在 Qt 5.6 中引入。

**另请参阅** [constLast](QList.md#const-t-qlistconstlast-const)(), [isEmpty](QList.md#bool-qlistisempty-const)() 和 [first](QList.md#t-qlistfirst)()。

### const T &QList::constLast() const

返回一个列表中最后一个元素的常量引用，列表必须不为空。如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

该方法在 Qt 5.6 中引入。

**另请参阅** [constFirst](QList.md#const-t-qlistconstfirst-const)(), [isEmpty](QList.md#bool-qlistisempty-const)() 和 [last](QList.md#t-qlistlast)()。

### bool QList::contains(const T &*value*) const

如果列表中包含 *value* 则返回 `true`，否则返回`false`。

该方法要求值类型实现了 `operator==()`。

**另请参阅** [indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)() 和 [count](QList.md#int-qlistcount-const)()。

### int QList::count(const T &*value*) const

返回 *value* 在列表中的出现次数。

该方法要求值类型实现了 `operator==()`。

**另请参阅** [contains](QList.md#bool-qlistcontainsconst-t-value-const)() 和 [indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)()。

### int QList::count() const

返回列表中元素的数量。该方法的性能等同于 [size](QList.md#typedef-qlistsizetype)()。

### [QList::const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator) QList::crbegin() const

返回指向逆序列表的第一个元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

该方法在 Qt 5.6 中引入。

**另请参阅** [begin](QList.md#qlistiterator-qlistbegin)(), [rbegin](QList.md#qlistreverseiterator-qlistrbegin)() 和 [rend](QList.md#qlistreverseiterator-qlistrend)()。

### [QList::const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator) QList::crend() const

返回指向逆序列表的最后一个元素的下一个元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

该方法在 Qt 5.6 中引入。

**另请参阅** [end](QList.md#qlistiterator-qlistend)(), [rend](QList.md#qlistreverseiterator-qlistrend)() 和 [rbegin](QList.md#qlistreverseiterator-qlistrbegin)()。

### bool QList::empty() const

该方法用于提供对 STL 的兼容，等同于 [isEmpty](QList.md#bool-qlistisempty-const)()，当列表为空时返回 `true`。

### [QList::iterator](QList_Iterator.md) QList::end()

返回一个指向位于最后一个元素之后的虚拟元素的常量 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)。

**另请参阅** [begin](QList.md#qlistiterator-qlistbegin)() 和 [constEnd](QList.md#qlistconstiterator-qlistconstend-const)()。

### [QList::const_iterator](QList_Const_Iterator.md) QList::end() const

这是个重载函数。

### bool QList::endsWith(const T &*value*) const

如果列表非空且最后一个元素等于 *value* 则返回`true` 否则返回 `false`。

该方法在 Qt 4.5 中引入。

**另请参阅** [isEmpty](QList.md#bool-qlistisempty-const)() 和 [contains](QList.md#bool-qlistcontainsconst-t-value-const)()。

### [QList::iterator](QList_Iterator.md) QList::erase([QList::iterator](QList_Iterator.md) *pos*)

从列表中移除和迭代器 *pos* 关联的元素，然会返回列表中下一个元素的迭代器 (可能是 [end](QList.md#qlistiterator-qlistend)())。

**另请参阅** [insert](QList.md#void-qlistinsertint-i-const-t-value)() 和 [removeAt](QList.md#void-qlistremoveatint-i)()。

### [QList::iterator](QList_Iterator.md) QList::erase([QList::iterator](QList_Iterator.md) *begin*, [QList::iterator](QList_Iterator.md) *end*)

这是个重载函数。

移除从 *begin* 到 (但不包括) *end* 的所有元素，然会返回调用该方法之前 *end* 所指向元素的迭代器。

### T &QList::first()

返回列表中第一个元素的引用，列表必须非空。如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

**另请参阅** [constFirst](QList.md#const-t-qlistconstfirst-const)(), [last](QList.md#t-qlistlast)() 和 [isEmpty](QList.md#bool-qlistisempty-const)()。

### const T &QList::first() const

这是个重载函数。

### ` [static]`  [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> QList::fromSet(const [QSet](../../S/QSet/QSet.md)<T> &*set*)

返回一个包含且仅包含 *set* 中所有的数据的 [QList](../../L/QList/QList.md) 对象。[QList](../../L/QList/QList.md) 中元素的顺序是未定义的。

示例:

``` cpp
QSet<int> set;
set << 20 << 30 << 40 << ... << 70;

QList<int> list = QList<int>::fromSet(set);
std::sort(list.begin(), list.end());
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [fromVector](QList.md#static-qlistt-qlistfromvectorconst-qvectort-vector)(), [toSet](QList.md#qsett-qlisttoset-const)() 和 [QSet::toList](../../S/QSet/QSet.md#qlistt-qsettolist-const)()。

### ` [static]  `[QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> QList::fromStdList(const std::list<T> &*list*)

返回一个包含且仅包含 *list* 中所有的数据的 [QList](../../L/QList/QList.md) 对象。[QList](../../L/QList/QList.md) 中元素的顺序和 *list* 一致。

示例：

``` cpp
std::list<double> stdlist;
list.push_back(1.2);
list.push_back(0.5);
list.push_back(3.14);

QList<double> list = QList<double>::fromStdList(stdlist);
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [toStdList](QList.md#stdlistt-qlisttostdlist-const)() 和 [QVector::fromStdVector](../../V/QVector/QVector.md#static-qvectort-qvectorfromstdvectorconst-stdvectort-vector)()。

### ` [static]  `[QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> QList::fromVector(const [QVector](../../V/QVector/QVector.md)<T> &*vector*)

返回包含且仅包含 *vector* 中所有的元素的 [QList](../../L/QList/QList.md) 对象。

示例：

``` cpp
QVector<double> vect;
vect << 20.0 << 30.0 << 40.0 << 50.0;

QList<double> list = QVector<T>::fromVector(vect);
// list: [20.0, 30.0, 40.0, 50.0]
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [fromSet](QList.md#static-qlistt-qlistfromsetconst-qsett-set)(), [toVector](QList.md#qvectort-qlisttovector-const)() 和 [QVector::toList](../../V/QVector/QVector.md#qlistt-qvectortolist-const)()。

### T &QList::front()

该方法用于提供对 STL 的兼容，等同于 [first](QList.md#t-qlistfirst)()。要求列表不能为空， 如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

### const T &QList::front() const

这是个重载函数。

### int QList::indexOf(const T &*value*, int *from* = 0) const

返回从索引位置 *from* 开始向列表尾部方向搜索，在列表中 *value* 第一次出现的索引位置。如果没有找到则返回 -1。

示例：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "B" << "A";
list.indexOf("B");          // 返回 1
list.indexOf("B", 1);       // 返回 1
list.indexOf("B", 2);       // 返回 3
list.indexOf("X");          // 返回 -1
```

该方法要求值类型实现了 `operator==()`。

需要注意的是 [QList](../../L/QList/QList.md) 和 C 数组类似，索引也是从 0 开始。除了上面提到的值，其他的负索引值不被支持。

**另请参阅** [lastIndexOf](QList.md#int-qlistlastindexofconst-t-value-int-from--1-const)() 和 [contains](QList.md#bool-qlistcontainsconst-t-value-const)()。

### void QList::insert(int *i*, const T &*value*)

将 *value* 插入到列表的索引位置 *i*。

如果 *i* == 0，该值将会被追加到列表头部。如果 *i* == [size](QList.md#typedef-qlistsizetype)()，该值将会被追加到列表尾部。

示例：

``` cpp
QList<QString> list;
list << "alpha" << "beta" << "delta";
list.insert(2, "gamma");
// list: ["alpha", "beta", "gamma", "delta"]
```

**另请参阅** [append](QList.md#void-qlistappendconst-t-value)(), [prepend](QList.md#void-qlistprependconst-t-value)(), [replace](QList.md#void-qlistreplaceint-i-const-t-value)() 和 [removeAt](QList.md#void-qlistremoveatint-i)()。

### [QList::iterator](QList_Iterator.md) QList::insert([QList::iterator](QList_Iterator.md) *before*, const T &*value*)

这是个重载函数。

将 *value* 插入到迭代器 *before* 指向元素的前面，并返回一个指向插入元素的迭代器。需要注意的是传递给该函数的迭代器在调用完成后将会失效，返回的迭代器可以用来代替它。

### bool QList::isEmpty() const

如果列表中没有任何元素则返回 `true` ，否则返回 `false`。

**另请参阅** [size](QList.md#typedef-qlistsizetype)()。

### T &QList::last()

返回列表最后一个元素的引用，列表必须非空。如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

**另请参阅** [constLast](QList.md#const-t-qlistconstlast-const)(), [first](QList.md#t-qlistfirst)() 和 [isEmpty](QList.md#bool-qlistisempty-const)()。

### const T &QList::last() const

这是个重载函数。

### int QList::lastIndexOf(const T &*value*, int *from* = -1) const

返回从索引位置 *from* 开始向列表头部方向搜索，在列表中 *value* 最后一次出现的索引位置。如果 *from* 是 -1，将会从最后一个元素开始搜索。如果没有找到则返回 -1。

示例：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "B" << "A";
list.lastIndexOf("B");      // 返回 3
list.lastIndexOf("B", 3);   // 返回 3
list.lastIndexOf("B", 2);   // 返回 1
list.lastIndexOf("X");      // 返回 -1
```

该方法要求值类型实现了 `operator==()`。

需要注意的是 [QList](../../L/QList/QList.md) 和 C 数组类似，索引也是从 0 开始。除了上面提到的值，其他的负索引值不被支持。

**另请参阅** [indexOf](QList.md#int-qlistindexofconst-t-value-int-from--0-const)()。

### int QList::length() const

该方法等同于 [count](QList.md#int-qlistcount-const)()。

该方法在 Qt 4.5 中引入。

**另请参阅** [count](QList.md#int-qlistcount-const)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> QList::mid(int *pos*, int *length* = -1) const

返回一个包含从列表的 *pos* 位置开始的元素的子列表，如果 *length* 为 -1（默认值），那么从 *pos* 开始的所有元素都会被子列表包含，否则子列表将会包含 *length* 个（如果剩余元素个数不足*length* 则为剩下的全部）元素。

### void QList::move(int *from*, int *to*)

将位于索引位置 *from* 的元素移动到索引位置 *to*。

示例：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "D" << "E" << "F";
list.move(1, 4);
// list: ["A", "C", "D", "E", "B", "F"]
```

等同于 insert(*to*, [takeAt](QList.md#t-qlisttakeatint-i)(*from*))。该方法会假定 *from* 和 *to* 都不小于 0 且小于 [size](QList.md#typedef-qlistsizetype)()。为了避免调用出错，应提前检查 *from* 和 *to* 是否不小于 0 且小于 [size](QList.md#typedef-qlistsizetype)()。

**另请参阅** [swap](QList.md#void-qlistswapqlistt-other)(), [insert](QList.md#void-qlistinsertint-i-const-t-value)() 和 [takeAt](QList.md#t-qlisttakeatint-i)()。

### void QList::pop_back()

该方法用于提供对 STL 的兼容，等同于 [removeLast](QList.md#void-qlistremovelast)()。该方法要求列表不能为空，如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

### void QList::pop_front()

该方法用于提供对 STL 的兼容，等同于 [removeFirst](QList.md#void-qlistremovefirst)()。该方法要求列表不能为空，如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

### void QList::prepend(const T &*value*)

在列表头部插入 *value* 。

示例：

``` cpp
QList<QString> list;
list.prepend("one");
list.prepend("two");
list.prepend("three");
// list: ["three", "two", "one"]
```

该方法等同于 list.insert(0, *value*)。

如果该列表是非共享的,那么此操作通常会非常快（均摊下来为 [常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QList](../../L/QList/QList.md) 在内部缓存的两端都预分配了额外的内存空间用于支持列表两端的快速增长。

**另请参阅** [append](QList.md#void-qlistappendconst-t-value)() 和 [insert](QList.md#void-qlistinsertint-i-const-t-value)()。

### void QList::push_back(const T &*value*)

该方法用于提供对 STL 的兼容，等同于 [append](QList.md#void-qlistappendconst-t-value)(*value*)。

### void QList::push_front(const T &*value*)

该方法用于提供对 STL 的兼容，等同于 [prepend](QList.md#void-qlistprependconst-t-value)(*value*)。

### [QList::reverse_iterator](QList.md#typedef-qlistreverseiterator) QList::rbegin()

返回一个指向列表在逆序遍历时第一个元素 [STL 风格](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)的反向迭代器。

该方法在 Qt 5.6 中引入。

**另请参阅** [begin](QList.md#qlistiterator-qlistbegin)(), [crbegin](QList.md#qlistconstreverseiterator-qlistcrbegin-const)() 和 [rend](QList.md#qlistreverseiterator-qlistrend)()。

### [QList::const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator) QList::rbegin() const

这是个重载函数。

该方法在 Qt 5.6 中引入。

### int QList::removeAll(const T &*value*)

移除列表中所有值为 *value* 的元素，然后返回移除的数量。

示例：

``` cpp
QList<QString> list;
list << "sun" << "cloud" << "sun" << "rain";
list.removeAll("sun");
// list: ["cloud", "rain"]
```

该方法要求值类型实现了 `operator==()`。

**另请参阅** [removeOne](QList.md#bool-qlistremoveoneconst-t-value)(), [removeAt](QList.md#void-qlistremoveatint-i)(), [takeAt](QList.md#t-qlisttakeatint-i)() 和 [replace](QList.md#void-qlistreplaceint-i-const-t-value)()。

### void QList::removeAt(int *i*)

移除位于索引位置 *i* 的元素。*i* 必须是列表中的合法索引位置 (即 0 `<=` *i* `<` [size](QList.md#typedef-qlistsizetype)())。

**另请参阅** [takeAt](QList.md#t-qlisttakeatint-i)(), [removeFirst](QList.md#void-qlistremovefirst)(), [removeLast](QList.md#void-qlistremovelast)() 和 [removeOne](QList.md#bool-qlistremoveoneconst-t-value)()。

### void QList::removeFirst()

移除列表中的第一个元素，等同于调用 [removeAt](QList.md#void-qlistremoveatint-i)(0)。该方法要求列表不能为空，如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

**另请参阅** [removeAt](QList.md#void-qlistremoveatint-i)() 和 [takeFirst](QList.md#t-qlisttakefirst)()。

### void QList::removeLast()

移除列表中最后一个元素，等同于调用 [removeAt](QList.md#void-qlistremoveatint-i)([size](QList.md#typedef-qlistsizetype)() - 1)。该方法要求列表不能为空，如果列表可能为空，应先调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

**另请参阅** [removeAt](QList.md#void-qlistremoveatint-i)() 和 [takeLast](QList.md#t-qlisttakelast)()。

### bool QList::removeOne(const T &*value*)

移除列表中第一个值为 *value* 的元素，若找到并移除成功则返回 `true`，否则返回 `false`。

示例：

``` cpp
QList<QString> list;
list << "sun" << "cloud" << "sun" << "rain";
list.removeOne("sun");
// list: ["cloud", "sun", "rain"]
```

该方法要求值类型实现了 `operator==()`。

该方法在 Qt 4.4 中引入。

**另请参阅** [removeAll](QList.md#int-qlistremoveallconst-t-value)(), [removeAt](QList.md#void-qlistremoveatint-i)(), [takeAt](QList.md#t-qlisttakeatint-i)() 和 [replace](QList.md#void-qlistreplaceint-i-const-t-value)()。

### [QList::reverse_iterator](QList.md#typedef-qlistreverseiterator) QList::rend()

返回一个指向列表在逆序遍历下最后一个元素的后一个元素的 [STL 风格](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)的反向迭代器。

该方法在 Qt 5.6 中引入。

**另请参阅** [end](QList.md#qlistiterator-qlistend)(), [crend](QList.md#qlistconstreverseiterator-qlistcrend-const)() 和 [rbegin](QList.md#qlistreverseiterator-qlistrbegin)()。

### [QList::const_reverse_iterator](QList.md#typedef-qlistconstreverseiterator) QList::rend() const

这是个重载函数。

该方法在 Qt 5.6 中引入。

### void QList::replace(int *i*, const T &*value*)

将位于索引位置 *i* 的元素替换为 *value*。*i* 必须是列表中合法的索引位置 (即 0 `<=` *i* `<` [size](QList.md#typedef-qlistsizetype)())。

**另请参阅** [operator[]](QList.md#t-qlistoperator)() 和 [removeAt](QList.md#void-qlistremoveatint-i)()。

### void QList::reserve(int *alloc*)

预留 *alloc* 个元素的空位。

如果 *alloc* 比当前列表的长度要小，则无事发生。

如果你可以提前预知接下来将会有多少元素追加到列表中，可以使用该方法避免 [QList](../../L/QList/QList.md) 内部数组重复分配内存。需要注意的是如果内部数组保存的是元素指针，则仅会仅预分配保存指针的数组的内存。

该方法在 Qt 4.7 中引入。

### int QList::size() const

返回列表中元素的个数。

**另请参阅** [isEmpty](QList.md#bool-qlistisempty-const)() 和 [count](QList.md#int-qlistcount-const)()。

### bool QList::startsWith(const T &*value*) const

如果列表非空且第一个元素等于 *value* 则返回 `true` ，否则返回 `false`。

该方法在 Qt 4.5 中引入。

**另请参阅** [isEmpty](QList.md#bool-qlistisempty-const)() 和 [contains](QList.md#bool-qlistcontainsconst-t-value-const)()。

### void QList::swap([QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*)

交换列表  *other* 和当前列表。该操作非常快且绝对不会失败。

该方法在 Qt 4.8 中引入。

### void QList::swapItemsAt(int *i*, int *j*)

交换位于索引位置 *i* 和 *j* 的元素。该方法会假定 *from* 和 *to* 都不小于 0 且小于 [size](QList.md#typedef-qlistsizetype)()。为了避免调用出错，请提前检查 *from* 和 *to* 是否不小于 0 且小于 [size](QList.md#typedef-qlistsizetype)()。

示例：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "D" << "E" << "F";
list.swapItemsAt(1, 4);
// list: ["A", "E", "C", "D", "B", "F"]
```

该方法在 Qt 5.13 中引入。

**另请参阅** [move](QList.md#void-qlistmoveint-from-int-to)()。

### T QList::takeAt(int *i*)

移除位于索引位置 *i* 的元素并返回该元素。 *i* 必须是列表中合法的索引位置 (即 0 `<=` *i* `<` [size](QList.md#typedef-qlistsizetype)())。

如果并不需要返回值，使用 [removeAt](QList.md#void-qlistremoveatint-i)() 会更高效。

**另请参阅** [removeAt](QList.md#void-qlistremoveatint-i)(), [takeFirst](QList.md#t-qlisttakefirst)() 和 [takeLast](QList.md#t-qlisttakelast)()。

### T QList::takeFirst()

移除列表中第一个元素并返回该元素，等同于 [takeAt](QList.md#t-qlisttakeatint-i)(0)。该方法会假定列表非空，为了避免调用失败，应提前调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

如果该列表是非共享的，那么此操作将花费[常量时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)。

如果不需要返回值，使用 [removeFirst](QList.md#void-qlistremovefirst)() 会更高效。

**另请参阅** [takeLast](QList.md#t-qlisttakelast)(), [takeAt](QList.md#t-qlisttakeatint-i)() 和 [removeFirst](QList.md#void-qlistremovefirst)()。

### T QList::takeLast()

移除列表中最后一个元素并返回该元素。等同于 [takeAt](QList.md#t-qlisttakeatint-i)([size](QList.md#typedef-qlistsizetype)() - 1)。该方法会假定列表非空，为了避免调用失败，应提前调用 [isEmpty](QList.md#bool-qlistisempty-const)() 进行检查。

如果该列表是非共享的，那么此操作将花费[常量时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)。

如果不需要返回值，使用 [removeLast](QList.md#void-qlistremovelast)() 会更高效。

**另请参阅** [takeFirst](QList.md#t-qlisttakefirst)(), [takeAt](QList.md#t-qlisttakeatint-i)() 和 [removeLast](QList.md#void-qlistremovelast)()。

### [QSet](../../S/QSet/QSet.md)<T> QList::toSet() const

返回一个包含且仅包含该 [QList](../../L/QList/QList.md) 中所有数据的 [QSet](../../S/QSet/QSet.md) 。由于 [QSet](../../S/QSet/QSet.md) 不允许有重复的数据，因此得到的 [QSet](../../S/QSet/QSet.md) 中的元素可能会少于原列表。

示例：

``` cpp
QStringList list;
list << "Julia" << "Mike" << "Mike" << "Julia" << "Julia";

QSet<QString> set = list.toSet();
set.contains("Julia");  // 返回 true
set.contains("Mike");   // 返回 true
set.size();             // 返回 2
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [toVector](QList.md#qvectort-qlisttovector-const)(), [fromSet](QList.md#static-qlistt-qlistfromsetconst-qsett-set)() 和 [QSet::fromList](../../S/QSet/QSet.md#static-qsett-qsetfromlistconst-qlistt-list)()。

### std::list<T> QList::toStdList() const

返回一个包含且仅包含该 [QList](../../L/QList/QList.md) 中所有数据的 std::list。

示例：

``` cpp
QList<double> list;
list << 1.2 << 0.5 << 3.14;

std::list<double> stdlist = list.toStdList();
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [fromStdList](QList.md#static-qlistt-qlistfromstdlistconst-stdlistt-list)() 和 [QVector::toStdVector](../../V/QVector/QVector.md#stdvectort-qvectortostdvector-const)()。

### [QVector](../../V/QVector/QVector.md)<T> QList::toVector() const

返回一个包含且仅包含该 [QList](../../L/QList/QList.md) 中所有数据的 [QVector](../../V/QVector/QVector.md) 对象。

示例：

``` cpp
QStringList list;
list << "Sven" << "Kim" << "Ola";

QVector<QString> vect = list.toVector();
// vect: ["Sven", "Kim", "Ola"]
```

**注意:** 从 Qt 5.14 开始，Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)支持范围构造函数，建议用来取代这个方法。

**另请参阅** [toSet](QList.md#qsett-qlisttoset-const)(), [fromVector](QList.md#static-qlistt-qlistfromvectorconst-qvectort-vector)() 和 [QVector::fromList](../../V/QVector/QVector.md#static-qvectort-qvectorfromlistconst-qlistt-list)()。

### T QList::value(int *i*) const

返回位于索引位置 *i* 的元素的值。

如果索引 *i* 越界了，该方法会返回一个[默认值](../../C/Container_Classes/Container_Classes.md#default-constructed-value)。如果想确保索引位于边界内，你可以使用 [at](QList.md#const-t-qlistatint-i-const)() 来代替，同时也会略快一些。

**另请参阅** [at](QList.md#const-t-qlistatint-i-const)() 和 [operator[]](QList.md#t-qlistoperator)()。

### T QList::value(int *i*, const T &*defaultValue*) const

这是个重载函数。

如果索引 *i* 越界了，该方法会返回 *defaultValue*。

### bool QList::operator!=(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*) const

如果 *other* 不等于该列表则返回 `true`，否则返回 `false`。

当且仅当两个列表以相同的顺序包含相同的值时两个列表才被认为是相等的。

该方法要求值类型实现了 `operator==()`。

**另请参阅** [operator==](QList.md#bool-qlistoperatorconst-qlistt-other-const)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> QList::operator+(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*) const

返回一个包含了 *other* 列表中所有元素附加在该列表之后得到的全部元素的列表。

**另请参阅** [operator+=](QList.md#qlistt-qlistoperatorconst-qlistt-other)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator+=(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*)

将 *other* 列表中所有元素追加到当前列表尾部并返回当前列表的引用。

**另请参阅** [operator+](QList.md#qlistt-qlistoperatorconst-qlistt-other-const)() 和 [append](QList.md#void-qlistappendconst-t-value)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator+=(const T &*value*)

这是个重载函数。

追加值 *value* 到列表中。

**另请参阅** [append](QList.md#void-qlistappendconst-t-value)() 和 [operator<<](QList.md#qlistt-qlistoperatorconst-qlistt-other)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator<<(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*)

将 *other* 列表中所有元素追加到当前列表尾部并返回当前列表的引用。

**另请参阅** [operator+=](QList.md#qlistt-qlistoperatorconst-qlistt-other)() 和 [append](QList.md#void-qlistappendconst-t-value)()。

### [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &QList::operator<<(const T &*value*)

这是个重载函数。

追加值 *value* 到列表中。

### bool QList::operator==(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*other*) const

如果 *other* 等于该列表则返回 `true`，否则返回 `false`。

当且仅当两个列表以相同的顺序包含相同的值时两个列表才被认为是相等的。

该方法要求值类型实现了 `operator==()`。

**另请参阅** [operator!=](QList.md#bool-qlistoperatorconst-qlistt-other-const)()。

### T &QList::operator[](int *i*)

以可修改的引用返回位于索引位置 *i* 的元素。*i* 必须是列表中一个合法的索引位置 (即 0 `<=` *i* `<` [size](QList.md#typedef-qlistsizetype)())。

如果对一个处于共享状态的列表调用该方法，则会触发对所有元素的拷贝。否则该方法运行时间开销为[常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)。如果你不打算修改列表，你用当使用 [QList::at](QList.md#const-t-qlistatint-i-const)()。

**另请参阅** [at](QList.md#const-t-qlistatint-i-const)() 和 [value](QList.md#typedef-qlistvaluetype)()。

### const T &QList::operator[](int *i*) const

这是个重载函数。

等同于 [at](QList.md#const-t-qlistatint-i-const)()。 该方法运行时间开销为 [常量时间复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)。

## 相关非成员函数

### template <typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回一个 *key* 的哈希值，可通过 *seed* 设置计算的种子。

该方法要求值类型 `T` 提供 qHash() 的重载。

该方法在 Qt 5.6 中引入。

### template <typename T> bool operator<(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*lhs*, const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*rhs*)

如果列表 *lhs* 按[字典序小于](http://en.cppreference.com/w/cpp/algorithm/lexicographical_compare) *rhs* 则返回 `true`; 否则返回 `false`。

该方法要求值类型实现了 `operator<()`。

该方法在 Qt 5.6 中引入。

### template <typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator<<([QDataStream](../../D/QDataStream/QDataStream.md) &*out*, const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*list*)

将列表 *list* 写入流 *out* 中。

该方法要求值类型实现了 `operator<<()`。

**另请参阅** [QDataStream 操作符格式](../../D/DataStreamFormat/DataStreamFormat.md)。

### template <typename T> bool operator<=(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*lhs*, const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*rhs*)

如果列表 *lhs* 按[字典序小于或等于](http://en.cppreference.com/w/cpp/algorithm/lexicographical_compare) *rhs* 则返回 `true`; 否则返回 `false`。

该方法要求值类型实现了 `operator<()`。

该方法在 Qt 5.6 中引入。

### template <typename T> bool operator>(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*lhs*, const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*rhs*)

如果列表 *lhs* 按[字典序大于](http://en.cppreference.com/w/cpp/algorithm/lexicographical_compare) *rhs* 则返回 `true`; 否则返回 `false`。

该方法要求值类型实现了 `operator<()`。

该方法在 Qt 5.6 中引入。

### template <typename T> bool operator>=(const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*lhs*, const [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*rhs*)

如果列表 *lhs* 按[字典序大于或等于](http://en.cppreference.com/w/cpp/algorithm/lexicographical_compare) *rhs* 则返回 `true`; 否则返回 `false`。

该方法要求值类型实现了 `operator<()`。

该方法在 Qt 5.6 中引入。

### template <typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator>>([QDataStream](../../D/QDataStream/QDataStream.md) &*in*, [QList](QList.md#template-typename-inputiterator-qlistqlistinputiterator-first-inputiterator-last)<T> &*list*)

从流 *in* 中读取一个列表到 *list*。

该方法要求值类型实现了 `operator>>()`。

**另请参阅** [QDataStream 操作符格式](../../D/DataStreamFormat/DataStreamFormat.md)。



## 已废弃成员

**下述的 [QList](../../L/QList/QList.md) 成员已被废弃。** 仅为保证旧代码的正常运行而被保留。我们强烈建议在新代码中不要再使用这些成员。

### 公共成员函数

|   |   |   |
|---|---|---|
| `(obsolete)` void  | **[swap](QList_Obsolete_Members.md#void-qlistswapint-i-int-j)**(int _i_, int _j_)  |

### 成员函数文档

#### void QList::swap(int _i_, int _j_)

此方法已废弃。仅为保证旧代码的正常运行而被保留。我们强烈建议在新代码中不要再使用这些成员。

使用 [swapItemsAt](../../O/TODO/TODO.md#void-qlistswapitemsatint-i-int-j)() 代替。

**另请参阅** [move](../../O/TODO/TODO.md#void-qlistmoveint-from-int-to)() 和 [swapItemsAt](../../O/TODO/TODO.md#void-qlistswapitemsatint-i-int-j)().
