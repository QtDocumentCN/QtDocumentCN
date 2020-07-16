# 容器

## 引言

Qt 提供了一系列基于模板的通用容器类，可以用于存储指定类型的元素。例如，如果你需要一个可动态调整大小的[QString]()数组，那么你可以使用[QVector<QString>]()。

这些类的设计目标是比 STL 容器更轻量，更安全，更易用。如果你不熟悉 STL，或想更有“ Qt 范”，使用这些类代替 STL 会是更好的选择。

这些类都是[隐式共享]()和[可重入]()的，并且针对几个方面做了优化，一是速度，二是较低的内存占用，三是尽可能少的内联代码，减少生成程序的体积。另外，在所有线程都以只读的方式访问容器时，这些类是线程安全的。

要遍历容器中的元素，你可以使用两种风格迭代器：[Java 风格迭代器]()和[ STL 风格迭代器]()。Java 风格迭代器有更好的易用性和更高级的函数，而 STL 风格迭代器则在效率上会略有优势，并且可以用于 Qt 和 STL 提供的[泛型算法]()中。

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

# 迭代器类

迭代器提供了一个统一的方式去访问容器中的元素。Qt 容器类提供了两种风格迭代器：Java 风格迭代器和 STL 风格迭代器。两种迭代器均会在容器中的数据被修改或因调用非 const 成员函数导致数据从隐式共享拷贝中分离后失效。

## Java 风格迭代器

Java 风格迭代器在 Qt4 中引入，作为标准使用在Qt应用中。和 STL 风格迭代器相比，其易用性更高，代价是性能略低。该风格迭代器 API 以 Java 迭代器类为原型设计。

对于每一个容器类，同时提供了两种数据类型的Java风格迭代器：一种支持只读访问，另一种支持读写访问。

|Containers|Read-only iterator|Read-write iterator|
|---|---|---|
|QList<T>, QQueue<T>|QListIterator<T>|QMutableListIterator<T>|
|QLinkedList<T>|QLinkedListIterator<T>|QMutableLinkedListIterator<T>|
|QVector<T>, QStack<T>|QVectorIterator<T>|QMutableVectorIterator<T>|
|QSet<T>|QSetIterator<T>|QMutableSetIterator<T>|
|QMap<Key, T>, QMultiMap<Key, T>|QMapIterator<Key, T>|QMutableMapIterator<Key, T>|
|QHash<Key, T>, QMultiHash<Key, T>|QHashIterator<Key, T>|QMutableHashIterator<Key, T>|

在接下来的讨论中，我们将重点关注QList和QMap。QLinkedList，QVector和QSet的迭代器类型和QList有完全一样的接口，类似的，QHash和QMap的迭代器类型的接口也是相同的。

和 STL 风格迭代器（下一节介绍）不同，Java 风格迭代器指向的是元素间隙而不是元素本身。因此，Java 风格迭代器可以指向容器最前（在第一个元素之前），也可以指向容器最后（在最后一个元素之后），还可以指向两个元素之间。下图用红色箭头展示了一个四个元素的列表容器合法的迭代器位置。

![Java style iterator](./java_style_iterator.svg)

这是一个通过循环迭代有序遍历QList<QString>中的所有元素并打印到终端的常用写法：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "D";

QListIterator<QString> i(list);
while (i.hasNext())
    qDebug() << i.next();
```

它的工作原理如下：需要被迭代的QList对象作为参数传递给QListIterator的构造函数。此时迭代器位于列表中第一个元素的前面（位于元素“A“之前）。接着我们调用hasNext()检查迭代器之后是否有元素，如果有，我们调用next()跳过这个元素。next()方法会返回其跳过的元素。对于QList<QString>类型，元素的类型为QString。

下列代码展示了如何反向迭代一个QList：

``` cpp
QListIterator<QString> i(list);
i.toBack();
while (i.hasPrevious())
    qDebug() << i.previous();
```

这段代码的逻辑和前向迭代是对称的除了在开始我们调用了toBack()将迭代器移动到列表中最后一个元素之后。

下图说明了在迭代器上调用next()和previous()产生的效果：

![list iterator](./list_iterator.svg)

下表总结了QListIterator的 API：

|Function|Behavior|
|---|---|
|toFront()|移动迭代器到列表最前（第一个元素之前）|
|toBack()|移动迭代器到列表最后（最后一个元素之后）|
|hasNext()|如果迭代器不在列表最后则返回真|
|next()|返回下一个元素并将迭代器前移一位|
|peekNext()|不移动迭代器，仅返回迭代器下一个元素|
|hasPrevious()|如果迭代器不在列表最前则返回真|
|previous()|返回前一个元素并将迭代器后移一位|
|peekPrevious()|不移动迭代器，仅返回迭代器前一个元素|

QListIterator没有提供任何在迭代列表时插入或删除元素的方法。要实现这一点，你必须使用QMutableListIterator。这是一个使用QMutableListIterator从QList<init>中移除所有奇数的例子：

``` cpp
QMutableListIterator<int> i(list);
while (i.hasNext()) {
    if (i.next() % 2 != 0)
        i.remove();
}
```

next()方法会在每次循环时调用，用于跳过下一个元素。remove()方法用于移除上一个我们跳过的元素。对remove()方法的调用不会导致迭代器的失效，因此继续使用迭代器是安全的。这种方式在反向迭代时也是没问题的。

``` cpp
QMutableListIterator<int> i(list);
i.toBack();
while (i.hasPrevious()) {
    if (i.previous() % 2 != 0)
        i.remove();
}
```

如果仅仅想修改已存在元素的值，我们可以使用setValue()。下列代码中，我们将所有大于128的值替换成128：

``` cpp
QMutableListIterator<int> i(list);
while (i.hasNext()) {
    if (i.next() > 128)
        i.setValue(128);
}
```

正如remove()，setValue()对我们跳过的最后一个元素进行操作。如果我们向前迭代，这个元素就是迭代器之前的元素；如果我们向后迭代，这个元素就是迭代器之后的元素。

next() 方法返回的是列表中元素的非常量引用，对于简单的操作，我们并不需要调用setValue()。

``` cpp
QMutableListIterator<int> i(list);
while (i.hasNext())
    i.next() *= 2;
```

正如上面提到的，QLinkedList，QVector和QSet的迭代器的API和QList的完全一致。接下来我们来看看在某些方面不太一样的QMapIterator，因为其用于迭代（键，值）对。

和QListIterator一样，QMapIterator提供了 toFront(), toBack(), hasNext(), next(), peekNext(), hasPrevious(), previous() 和 peekPrevious()方法。我们可以对next(), peekNext(), previous() 或 peekPrevious()返回的对象调用key()和value()方法来获得键和值。

下列代码用于移除所有首都名以”`city`“结尾的（首都名，国家名）键值对。

```
QMap<QString, QString> map;
map.insert("Paris", "France");
map.insert("Guatemala City", "Guatemala");
map.insert("Mexico City", "Mexico");
map.insert("Moscow", "Russia");
...

QMutableMapIterator<QString, QString> i(map);
while (i.hasNext()) {
    if (i.next().key().endsWith("City"))
        i.remove();
}
```

QMapIterator也提供了key()和value()方法用于操作迭代器及迭代器上一个跳过的元素的键和值。举个例子，下列代码用于将QMap的内容拷贝到QHash中。

``` cpp
QMap<int, QWidget *> map;
QHash<int, QWidget *> hash;

QMapIterator<int, QWidget *> i(map);
while (i.hasNext()) {
    i.next();
    hash.insert(i.key(), i.value());
}
```

如果想要迭代遍历所有值相同的元素，我们可以使用findNext()和findPrevious()。这里的例子用于移除带有指定值的元素。

``` cpp
QMutableMapIterator<int, QWidget *> i(map);
while (i.findNext(widget))
    i.remove();
```

## STL风格迭代器

STL 风格迭代器在 Qt 2.0 中被引入，可用于 Qt 和 STL 的泛型算法，且为速度做了优化。

对于每一个容器类，同时提供了两种类型的 STL 风格迭代器：一种支持只读访问，另一种支持读写访问。

|容器|只读迭代器|读写迭代器|
|---|---|---|
|QList<T>, QQueue<T>|QList<T>::const_iterator|QList<T>::iterator|
|QLinkedList<T>|QLinkedList<T>::const_iterator|QLinkedList<T>::iterator|
|QVector<T>, QStack<T>|QVector<T>::const_iterator|QVector<T>::iterator|
|QSet<T>|QSet<T>::const_iterator|QSet<T>::iterator|
|QMap<Key, T>, QMultiMap<Key, T>|QMap<Key, T>::const_iterator|QMap<Key, T>::iterator|
|QHash<Key, T>, QMultiHash<Key, T>|QHash<Key, T>::const_iterator|QHash<Key, T>::iterator|

STL 风格迭代器的 API 以 数组指针为原型设计。例如，`++`运算符将迭代器向前移动至下一个元素，`*`运算符返回迭代器指向的元素。实际上，对于QVector和QStack这类元素存储在连续内存的容器来说，读写迭代器类型仅仅是`T *`的别名，只读迭代器是`const T *`的一个别名。

在接下来的讨论中，我们将重点关注QList和QMap。QLinkedList，QVector和QSet的迭代器类型和QList有完全一样的接口，类似的，QHash和QMap的迭代器类型的接口也是相同的。

这是一个通过循环迭代有序遍历QList<QString>中的所有元素并将它们转成小写的常见写法：

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "D";

QList<QString>::iterator i;
for (i = list.begin(); i != list.end(); ++i)
    *i = (*i).toLower();
```

和 Java 风格迭代器不同，STL 风格迭代器直接指向元素本身。容器的begin()方法会返回一个指向容器第一个元素的迭代器，end() 方法返回的迭代器指向一个虚拟的元素，该元素位于容器最后一个元素的下一个位置。end() 标记了一个非法的位置，永远不要对其解引用。其通常被用作循环的结束条件。对于空列表，begin() 和 end()是相等的，因此我们永远不会执行循环。

下图用红色箭头展示了一个四个元素的列表容器中合法的迭代器位置。

![STL Style Iterator](./stl_style_iterator.svg)

使用 STL 风格迭代器反向遍历可以通过反向迭代器实现

``` cpp
QList<QString> list;
list << "A" << "B" << "C" << "D";

QList<QString>::reverse_iterator i;
for (i = list.rbegin(); i != list.rend(); ++i)
    *i = i->toLower();
}
```

上面的代码片段中，我们通过一元运算符`*`来获取保存在指定迭代器位置的元素（此处类型为QString），并对其调用了 QString::toLower() 方法。大部分C++编译器也同时支持`i->toLower()`这种写法，但也有一些不支持。

对于只读访问，你可以使用const_iterator, constBegin(), and constEnd()。例如：

``` cpp
QList<QString>::const_iterator i;
for (i = list.constBegin(); i != list.constEnd(); ++i)
    qDebug() << *i;
```

下表整理了STL风格迭代器的API



|表达式|行为|
|---|---|
|*i|返回当前元素|
|++i|向前移动迭代器至下一元素|
|i += n|向前移动迭代器 n 次|
|--i|向后移动迭代器至前一个元素|
|i -= n|向后移动迭代器 n 次|
|i - j|返回迭代器 i 和 j 间隔的元素个数|

`++`和`--`运算符既可以作为前缀(`++i`，`--i`) ，也可以作为后缀(`i++`，`i--`)运算符。前缀版本先修改迭代器，然后返回修改后的迭代器的引用。后缀版本在修改迭代器之前先将其复制一份，然后返回副本。在返回值被忽略的表达式中，我们建议使用前缀版本，因为这样会略快一点。

对于非常量迭代器类型，一元运算符`*`的返回值可以作为赋值运算符的左侧。

对于QMap和QHash，`*`运算符返回一个元素的值，如果你想获取键，可以调用迭代器的key()方法。相对应的，迭代器类型也提供了value()用于获取值。下面是一个将QMap中所有元素打印到终端的例子：

``` cpp
QMap<int, int> map;
...
QMap<int, int>::const_iterator i;
for (i = map.constBegin(); i != map.constEnd(); ++i)
    qDebug() << i.key() << ':' << i.value();
```

正是因为隐式共享，调用一个返回容器的函数的开销不会很大。Qt API 中包含几十个返回一个QList或QStringList的函数（例如QSplitter::sizes()）。如果需要通过 STL 迭代器遍历这些返回值，你应当总是将返回的容器复制一份然后迭代其副本。例如：

``` cpp
// 正确
const QList<int> sizes = splitter->sizes();
QList<int>::const_iterator i;
for (i = sizes.begin(); i != sizes.end(); ++i)
    ...

// 错误
QList<int>::const_iterator i;
for (i = splitter->sizes().begin();
        i != splitter->sizes().end(); ++i)
    ...
```

如果函数返回的是一个容器的常量或非常量引用，那么是不存在这个问题的。

### 隐式共享迭代器问题

隐式共享给 STL 风格迭代器带来了另一个后果是：当一个容器的迭代器在使用时你应当避免复制该容器。迭代器指向了一个内部结构，当你复制容器时你需要特别小心的处理迭代器。比如：

``` cpp
QVector<int> a, b;
a.resize(100000); // 创建一个填充0的大数组.

QVector<int>::iterator i = a.begin();
// 迭代器i的错误用法:
b = a;
/*
    现在我们应当小心地使用迭代器`i`，因为 i 指向的是共享的数据。
    如果我们执行 *i = 4 那么我们可能改变共享的实例（两个数组共享）
    这个行为和 STL 容器是不同的。在 Qt 中不要这样做。
*/

a[0] = 5;
/*
    容器 a 现在已经和共享数据脱离，
    即使 i 之前是容器 a 的迭代器，但现在它是作为 b 的迭代器而存在。
    此时 (*i) == 0
*/

b.clear(); // 此时 i 彻底失效

int j = *i; // 未定义行为!
/*
    b 中的数据（即i 指向的）已经被释放，
    在 STL 容器中这是有明确定义的（(*i) == 5），
    但对于 QVector 来说这样做很有可能导致崩溃。
*/
```

> 译注：STL 容器`std::vector`在调用clear()方法后内存不会被释放，因此迭代器并不会立即失效

上面的例子仅仅说明了QVector的问题，但实际上所有支持隐式共享的容器都存在该问题。

# foreach 关键字


如果仅仅是需要有序迭代容器中的每个元素，你可以使用 Qt 提供的关键字 `foreach`。这个关键字对 C++ 语言的一个特定于 Qt 的补充，其通过预处理器实现。

使用的语法是：`foreach(变量，容器) 语句`。下面是一个使用`foreach`迭代QLinkedList<QString>的例子：

``` cpp
QLinkedList<QString> list;
...
QString str;
foreach (str, list)
    qDebug() << str;
```

和使用迭代器实现相同功能的代码相比，使用`foreach`的代码明显简洁很多。

``` cpp
QLinkedList<QString> list;
...
QLinkedListIterator<QString> i(list);
while (i.hasNext())
    qDebug() << i.next();
```

除了数据类型包含逗号（例如 QPair<int, int>）以外，用于迭代的变量可以在`foreach`语句中被定义：

``` cpp
QLinkedList<QString> list;
...
foreach (const QString &str, list)
    qDebug() << str;
```

和其他 C++ 循环结构类似，你可以使用大括号将循环体包围，也可以使用`break`跳出循环。

``` cpp
QLinkedList<QString> list;
...
foreach (const QString &str, list) {
    if (str.isEmpty())
        break;
    qDebug() << str;
}
```

对于 QMap 和 QHash，`foreach` 会自动访问（键，值）对中的值，因此你不需要再调用容器的 values() 方法（这样可能会产生不必要的复制，见后续说明）。如果你想要同时迭代键和值，可以使用迭代器（会更快），或者也可以先获取所有的键，再通过它们获取对应的值：

``` cpp
QMap<QString, int> map;
...
foreach (const QString &str, map.keys())
    qDebug() << str << ':' << map.value(str);
```

对于一个多值映射：

``` cpp
QMultiMap<QString, int> map;
...
foreach (const QString &str, map.uniqueKeys()) {
    foreach (int i, map.values(str))
        qDebug() << str << ':' << i;
}
```

当进入一个`foreach`循环，Qt 会自动产生一个容器的副本。如果在迭代过程中修改了容器，并不会影响到这次循环。（如果没有修改容器，副本依然会占用空间，但由于隐式共享的缘故，复制一个容器是非常快的）。

因为`foreach`会产生容器的副本，使用是个变量的非常量引用也是无法修改原容器的，它仅仅会影响副本，这可能不是你想要的。

一个对 Qt 的`foreach`循环的替代方案是 C++ 11 或更新标准中引入的基于范围的`for`循环。然而，基于范围的`for`循环可能强行导致 Qt 容器脱离，但`foreach`不会。由于使用`foreach`总是会复制一份容器，对 STL 容器来说这通常会导致一定的开销。如果不知道用哪个，建议对 Qt 容器选择`foreach`，而对 STL 容器选择基于范围的`for`循环。

除了`foreach`，Qt 还提供了一个`forever`伪关键字用于执行无限循环。

``` cpp
forever {
    ...
}
```

如果你担心命名空间污染，你可以在`.pro`文件中添加以下代码以禁用这些宏：

```
CONFIG += no_keywords
```
