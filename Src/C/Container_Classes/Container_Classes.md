# 容器

## 引言

Qt 提供了一系列基于模板的通用容器类，可以用于存储指定类型的元素。例如，如果你需要一个可动态调整大小的[QString]()数组，那么你可以使用[QVector<QString>]()。

这些类的设计目标是比 STL 容器更轻量，更安全，更易用。如果你不熟悉 STL，或想更有“ Qt 范”，使用这些类代替 STL 会是更好的选择。

这些类都是[隐式共享]()和[可重入]()的，并且针对几个方面做了优化，一是速度，二是较低的内存占用，三是尽可能少的内联代码，减少生成程序的体积。另外，在所有线程都以只读的方式访问容器时，这些类是线程安全的。

要遍历容器中的元素，你可以使用两种风格的迭代器：[Java 风格的迭代器]()和[ STL 风格的迭代器]()。Java 风格的迭代器有更好的易用性和更高级的函数，而 STL 风格的迭代器则在效率上会略有优势，并且可以用于 Qt 和 STL 提供的[泛型算法]()中。

Qt 还提供了[foreach]()关键字，可以方便地遍历容器。

**注**：从 Qt 5.14 开始，绝大部分容器类已经支持范围构造函数，但需要注意的是[QMultiMap]()是一个例外。我们推荐使用该特性代替各种from/to方法。例如：

> 译者注：这里的from/to方法指的是Qt容器类提供的以from/to开头的转换方法，如`QVector::toList`

```cpp
QVector<int> vector{1, 2, 3, 4, 4, 5};
QSet<int> set(vector.begin(), vector.end());
/*
    Will generate a QSet containing 1, 2, 4, 5.
*/
```

## 容器类

Qt 提供了以下几种顺序容器：[QList]()，[QLinkedList]()，[QVector]()，[QStack]()和[QQueue]()。对于大多数的应用，[QList]()是最适用的。虽然其基于数组实现，但支持在头部和尾部快速插入。如果确实需要一个基于链表的列表，你可以使用`QLinkedList`；如果要求元素以连续内存的形式保存，那么可以使用[QVector]()。[QStack]()和[QQueue]()提供了 LIFO 和 FIFO 语义的支持。

Qt也提供了一系列关联容器：[QMap]()，[QMultiMap]()，[QHash]()，[QMultiHash]()和[QSet]()。"Multi" 容器可以方便地支持键值一对多的情形。“HASH” 容器提供了快速查找的能力，这是通过使用哈希函数代替对有序集合进行二分查找实现的。

较为特殊的是[QCache]()和[QContiguousCache]()，这两个类提供了在有限的缓存中快速查找元素的能力。

| 类  | 综述  |
|:---:|:---:|
| [QList<T>]()  |  这是目前使用最普遍的容器类，其保存了一个元素类型为`T`的列表，支持通过索引访问。[QList]()内部通过数组实现，以确保基于索引的访问足够快。<br/> 元素可以通过[]()和[]()插入到首尾，也可以通过[]()插入到列表中间，和其他容器类不同的是，QList为生成尽可能少的代码做了高度优化。QStringList继承于QList<String>。 |
| [QLinkedList<T>]()  | 这个类和QList很像，不同的是这个类使用迭代器进行而不是整形索引对元素进行访问。和QList相比，其在中间插入大型列表时其性能更优，而且其具有更好的迭代器语义。（在QLinkedList中，指向一个元素的迭代器只要该元素存在，则会一直保持有效，而在QList的迭代器则可能会在任意的元素插入或删除后失效。）  |
| [QVector<T>]()  | 这个类以数组的形式保存给定类型的元素，在内存中元素彼此相邻。在一个vector的头部或中部插入可能会相当慢，因为这可能会导致大量元素需要在内存中移动一个位置。  |
| [QVarLengthArray<T, Prealloc>]()  |  这个类提供了一个底层的变长数组，在速度极其重要的情况下可以用来代替QVector |
| [QStack<T>]()  |  这个类继承于QVector，用于为”后进，先出”（LIFO ）提供便捷的语义支持。其为QVector添加了以下方法：push()，pop()和top() |
| [QQueue<T>]()  |  这个类继承于QVector，用于为”先进，先出”（FIFO ）提供便捷的语义支持。其为QVector添加了以下方法：enqueue()，dequeue()和head()  |
| [QSet<T>]()  | 这个类提供了一个单值数学集合，支持快速查找  |
| [QMap<Key, T>]()  | 这个类提供了一个将类型为`Key`的键映射到类型为`T`的值的字典（关联数组）。通常情况下键值是一一对应的。QMap根据`Key`进行排序，如果排序无关紧要，使用QHash代替速度会更快  |
| [QMultiMap<Key, T>]()  | 这个类继承于QMap，其为诸如键值一对多的多值映射提供了一个友好的接口  |
| [QHash<Key, T>]()  | 这个类几乎与QMap有完全一致的 API ，但查找效率会有明显的提高。QHash的数据是无序的。  |
| [QMultiHash<T>]()  |  这个类继承于QMap，其为多值映射提供了一个友好的接口 |

容器可以嵌套。例如在键为QString，值为QList<int>时，完全有可能使用QMap<QString, QList<int>>。

容器类的定义位于和容器同名的独立头文件中（例如，`<QLinkedList>`）。为了方便，在<QtContainerFwd>中对所有容器类进行了前置声明。

保存在各个容器中的值类型可以是任意`可复制数据类型`。为了满足这一要求，该类型必须提供一个复制构造函数和一个赋值运算符。某些操作可能还要求类型支持默认构造函数。对于大多数你想要在容器中保存的类型都满足这些要求，包括基本类型，如 **int** ， **double**，指针类型，以及 Qt 数据类型，如 QString，QDate和QTime，但并不包括QObject及其子类（QWidget，QDialog，QTimer等）。如果你尝试实例化一个QList<QWidget>，编译器将会抱怨道QWidget的复制构造函数和赋值运算符被禁用了。如果需要在容器中保存这些类型的元素，可以保存其指针，如QList<QWidget *>。

下面是一个满足可赋值数据类型要求的自定义数据类型的例子：

``` cpp
class Employee
{
public:
    Employee() {}
    Employee(const Employee &other);

    Employee &operator=(const Employee &other);

private:
    QString myName;
    QDate myDateOfBirth;
};
```

如果我们没有提供一个复制构造函数或一个赋值运算符，C++ 将会提供一个表现为逐个复制成员的默认实现。在上面的例子中，默认行为就足够了。同样的，如果没有提供默认构造函数，C++ 会提供一个默认构造函数，对成员进行默认构造。尽管没有提供任何的构造函数或赋值运算符，下面的数据类型可以被保存于容器中。

``` cpp
struct Movie
{
    int id;
    QString title;
    QDate releaseDate;
};
```

一些容器对它们所能保存的数据类型有额外的要求。举个例子，QMap<Key, T>的键类型 Key 必须提供 **`operator<()`** 方法。这些特殊要求在类的详细描述中有说明。在某些情况下，特定函数会有特定的要求，这在函数的描述中有说明。如果条件不满足，编译器将总是会报错。

Qt容器提供了`operator<<()`和`operator>>()`，因此这些类可以很方便地通过QDataStream进行读写。这意味着存储在容器中的元素类型也必须支持`operator<<()`和`operator>>()`。支持这一点是很简单的；以下是我们使上面的`Movie`结构体支持这一点所做的改动：

``` cpp
QDataStream &operator<<(QDataStream &out, const Movie &movie)
{
    out << (quint32)movie.id << movie.title
        << movie.releaseDate;
    return out;
}

QDataStream &operator>>(QDataStream &in, Movie &movie)
{
    quint32 id;
    QDate date;

    in >> id >> movie.title >> date;
    movie.id = (int)id;
    movie.releaseDate = date;
    return in;
}
```

某些容器类的文档中会提到`默认值`；举个例子，QVector会自动使用默认值初始化其元素；QMap::value() 在指定键不存在时会返回一个默认值。对于大部分的值类型，这就是简单地代表通过默认构造函数创建的值（例如对于QString即空字符串）。但是对于基本类型，如 **int** 和 **double** 和指针类型，C++ 语言并没有规定任何的初始化方式，因此在这些情况下，Qt 容器将会自动将其初始化为0。
