# QMap 类

template <typename Key, typename T> class QMap

QMap 类是一种模板类，提供基于红黑树的字典类结构。[更多内容...](QMap.md#详细描述)

| 头文件:       | #include <QMap>                                    |
| -------------: | :-------------------------------------------------- |
| qmake:        | QT += core                                         |
| 派生类: | [QMultiMap](../../M/QMultiMap/QMultiMap.md) |

- [所有成员列表，包括继承的成员](../../M/QMap/QMap-members.md)
- [废弃的成员](../../M/QMap/QMap-obsolete.md)

**注意：** 该类中的所有函数都是[可重入的](../../T/Threads-Reentrancy/Threads-Reentrancy.md)。



## 公共成员类型

| class   | **[const_iterator](../../M/QMap/QMap-const-iterator.md)**    |
| -------: | :------------------------------------------------------------ |
| class   | **[iterator](../../M/QMap/QMap-iterator.md)**                |
| class   | **[key_iterator](../../M/QMap/QMap-key-iterator.md)**        |
| typedef | **[ConstIterator](QMap.md#typedef-qmapconstiterator)**       |
| typedef | **[Iterator](QMap.md#typedef-qmapiterator)**                 |
| typedef | **[const_key_value_iterator](QMap.md#typedef-qmapconst_key_value_iterator)** |
| typedef | **[difference_type](QMap.md#typedef-qmapdifference_type)**   |
| typedef | **[key_type](QMap.md#typedef-qmapkey_type)**                 |
| typedef | **[key_value_iterator](QMap.md#typedef-qmapkey_value_iterator)** |
| typedef | **[mapped_type](QMap.md#typedef-qmapmappedtype)**            |
| typedef | **[size_type](QMap.md#typedef-qmapsize_type)**               |



## 公共成员函数

|                                                   | **[QMap](QMap.md#qmapqmapconst-typename-stdmapkey-t-other)**(const typename std::map<Key, T> &*other*) |
| ------------------------------------------------: | :----------------------------------------------------------- |
|                                                   | **[QMap](QMap.md#qmapqmapqmapkey-t-other)**(QMap<Key, T> &&*other*) |
|                                                   | **[QMap](QMap.md#qmapqmapconst-qmapkey-t-other)**(const QMap<Key, T> &*other*) |
|                                                   | **[QMap](QMap.md#qmapqmapstdinitializerliststdpairkey-t--list)**(std::initializer_list<std::pair<Key, T> > *list*) |
|                                                   | **[QMap](QMap.md#qmapqmap)**()                               |
|                                    QMap<Key, T> & | **[operator=](QMap.md#qmapkey-t-qmapoperatorqmapkey-t-other)**(QMap<Key, T> &&*other*) |
|                                    QMap<Key, T> & | **[operator=](QMap.md#qmapkey-t-qmapoperatorconst-qmapkey-t-other)**(const QMap<Key, T> &*other*) |
|                                                   | **[~QMap](QMap.md#qmapqmap-1)**()                            |
|                                    QMap::iterator | **[begin](QMap.md#qmapiterator-qmapbegin)**()                |
|                              QMap::const_iterator | **[begin](QMap.md#qmapconst_iterator-qmapbegin-const)**() const |
|                              QMap::const_iterator | **[cbegin](QMap.md#qmapconst_iterator-qmapcbegin-const)**() const |
|                              QMap::const_iterator | **[cend](QMap.md#qmapconst_iterator-qmapcend-const)**() const |
|                                              void | **[clear](QMap.md#void-qmapclear)**()                        |
|                              QMap::const_iterator | **[constBegin](QMap.md#qmapconst_iterator-qmapconstbegin-const)**() const |
|                              QMap::const_iterator | **[constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)**() const |
|                              QMap::const_iterator | **[constFind](QMap.md#qmapconst_iterator-qmapconstfindconst-key-key-const)**(const Key &*key*) const |
|                    QMap::const_key_value_iterator | **[constKeyValueBegin](QMap.md#qmapconst_key_value_iterator-qmapconstkeyvaluebegin-const)**() const |
|                    QMap::const_key_value_iterator | **[constKeyValueEnd](QMap.md#qmapconst_key_value_iterator-qmapconstkeyvalueend-const)**() const |
|                                              bool | **[contains](QMap.md#bool-qmapcontainsconst-key-key-const)**(const Key &*key*) const |
|                                               int | **[count](QMap.md#int-qmapcountconst-key-key-const)**(const Key &*key*) const |
|                                               int | **[count](QMap.md#int-qmapcount-const)**() const             |
|                                              bool | **[empty](QMap.md#bool-qmapempty-const)**() const            |
|                                    QMap::iterator | **[end](QMap.md#qmapiterator-qmapend)**()                    |
|                              QMap::const_iterator | **[end](QMap.md#qmapconst_iterator-qmapend-const)**() const  |
|             QPair<QMap::iterator, QMap::iterator> | **[equal_range](QMap.md#qpairqmapiterator-qmapiterator-qmapequalrangeconst-key-key)**(const Key &*key*) |
| QPair<QMap::const_iterator, QMap::const_iterator> | **[equal_range](QMap.md#qpairqmapconst_iterator-qmapconst_iterator-qmapequalrangeconst-key-key-const)**(const Key &*key*) const |
|                                    QMap::iterator | **[erase](QMap.md#qmapiterator-qmaperaseqmapiterator-pos)**(QMap::iterator *pos*) |
|                                    QMap::iterator | **[find](QMap.md#qmapiterator-qmapfindconst-key-key)**(const Key &*key*) |
|                              QMap::const_iterator | **[find](QMap.md#qmapconst_iterator-qmapfindconst-key-key-const)**(const Key &*key*) const |
|                                               T & | **[first](QMap.md#t-qmapfirst)**()                           |
|                                         const T & | **[first](QMap.md#const-t-qmapfirst-const)**() const         |
|                                       const Key & | **[firstKey](QMap.md#const-key-qmapfirstkey-const)**() const |
|                                    QMap::iterator | **[insert](QMap.md#qmapiterator-qmapinsertconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
|                                    QMap::iterator | **[insert](QMap.md#qmapiterator-qmapinsertqmapconst_iterator-pos-const-key-key-const-t-value)**(QMap::const_iterator *pos*, const Key &*key*, const T &*value*) |
|                                              void | **[insert](QMap.md#void-qmapinsertconst-qmapkey-t-map)**(const QMap<Key, T> &*map*) |
|                                              bool | **[isEmpty](QMap.md#bool-qmapisempty-const)**() const        |
|                                         const Key | **[key](QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)**(const T &*value*, const Key &*defaultKey* = Key()) const |
|                                QMap::key_iterator | **[keyBegin](QMap.md#qmapkey_iterator-qmapkeybegin-const)**() const |
|                                QMap::key_iterator | **[keyEnd](QMap.md#qmapkey_iterator-qmapkeyend-const)**() const |
|                          QMap::key_value_iterator | **[keyValueBegin](QMap.md#qmapkey_value_iterator-qmapkeyvaluebegin)**() |
|                    QMap::const_key_value_iterator | **[keyValueBegin](QMap.md#qmapconst_key_value_iterator-qmapkeyvaluebegin-const)**() const |
|                          QMap::key_value_iterator | **[keyValueEnd](QMap.md#qmapkey_value_iterator-qmapkeyvalueend)**() |
|                    QMap::const_key_value_iterator | **[keyValueEnd](QMap.md#qmapconst_key_value_iterator-qmapkeyvalueend-const)**() const |
|                                        QList<Key> | **[keys](QMap.md#qlistkey-qmapkeys-const)**() const          |
|                                        QList<Key> | **[keys](QMap.md#qlistkey-qmapkeysconst-t-value-const)**(const T &*value*) const |
|                                               T & | **[last](QMap.md#t-qmaplast)**()                             |
|                                         const T & | **[last](QMap.md#const-t-qmaplast-const)**() const           |
|                                       const Key & | **[lastKey](QMap.md#const-key-qmaplastkey-const)**() const   |
|                                    QMap::iterator | **[lowerBound](QMap.md#qmapiterator-qmaplowerboundconst-key-key)**(const Key &*key*) |
|                              QMap::const_iterator | **[lowerBound](QMap.md#qmapconst_iterator-qmaplowerboundconst-key-key-const)**(const Key &*key*) const |
|                                               int | **[remove](QMap.md#int-qmapremoveconst-key-key)**(const Key &*key*) |
|                                               int | **[size](QMap.md#int-qmapsize-const)**() const               |
|                                              void | **[swap](QMap.md#void-qmapswapqmapkey-t-other)**(QMap<Key, T> &*other*) |
|                                                 T | **[take](QMap.md#t-qmaptakeconst-key-key)**(const Key &*key*) |
|                                  std::map<Key, T> | **[toStdMap](QMap.md#stdmapkey-t-qmaptostdmap-const)**() const |
|                                    QMap::iterator | **[upperBound](QMap.md#qmapiterator-qmapupperboundconst-key-key)**(const Key &*key*) |
|                              QMap::const_iterator | **[upperBound](QMap.md#qmapconst_iterator-qmapupperboundconst-key-key-const)**(const Key &*key*) const |
|                                           const T | **[value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)**(const Key &*key*, const T &*defaultValue* = T()) const |
|                                          QList<T> | **[values](QMap.md#qlistt-qmapvalues-const)**() const        |
|                                              bool | **[operator!=](QMap.md#bool-qmapoperatorconst-qmapkey-t-other-const)**(const QMap<Key, T> &*other*) const |
|                                              bool | **[operator==](QMap.md#bool-qmapoperatorconst-qmapkey-t-other-const-1)**(const QMap<Key, T> &*other*) const |
|                                               T & | **[operator[]](QMap.md#t-qmapoperatorconst-key-key)**(const Key &*key*) |
|                                           const T | **[operator[]](QMap.md#const-t-qmapoperatorconst-key-key-const)**(const Key &*key*) const |



## 相关非成员函数

| QDataStream & | **[operator<<](QMap.md#template-typename-key-typename-t-qdatastream-operatorqdatastream-out-const-qmapkey-t-map)**(QDataStream &*out*, const QMap<Key, T> &*map*) |
| -------------: | :------------------------------------------------------------ |
| QDataStream & | **[operator>>](QMap.md#template-typename-key-typename-t-qdatastream-operatorqdatastream-in-qmapkey-t-map)**(QDataStream &*in*, QMap<Key, T> &*map*) |



## 详细描述

QMap<Key, T> 是一种 Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)。该类存储键值对，可以用相关联的键快速查找值。

QMap 的功能与 [QHash](../../H/QHash/QHash.md) 非常相似。二者的区别在于：

- [QHash](../../H/QHash/QHash.md) 的平均查找速度比 QMap 快。（详情请看[算法复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)。）
- 遍历 [QHash](../../H/QHash/QHash.md) 时，元素的顺序是任意的。而遍历 QMap 时，元素总是按照键的顺序排好序的。
- [QHash](../../H/QHash/QHash.md) 的键类型必须提供 operator==() 运算符和全局的 [qHash](../../H/QHash/QHash.md)(Key) 函数。QMap 的键类型必须提供 operator<() 运算符来确定全序。从 Qt5.8.1 起，即使底层的 operator<() 运算符没有提供全序，使用指针作为键类型也是安全的。

下面是一个键类型为 [QString](../../S/QString/QString.md)，值类型为 `int` 的 QMap 的示例：

```c++
QMap<QString, int> map;
```

可以使用 operator\[\]\(\) 运算符将键值对插入到 map 中：

```c++
map["one"] = 1;
map["three"] = 3;
map["seven"] = 7;
```

上面的代码将3个键值对插入到 QMap 中：("one", 1)，("three", 3) 和 ("seven", 7)。另外一种向 map 中插入元素的方法是使用 [insert](QMap.md#qmapiterator-qmapinsertconst-key-key-const-t-value)()：

```c++
map.insert("twelve", 12);
```

使用 operator\[\]\(\) 运算符或 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() 查找值：

```c++
int num1 = map["thirteen"];
int num2 = map.value("thirteen");
```

如果 map 中不存在指定的键，这些函数返回[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。

如果想检查 map 中是否包含特定键，使用 [contains](QMap.md#bool-qmapcontainsconst-key-key-const)()：

```c++
int timeout = 30;
if (map.contains("TIMEOUT"))
    timeout = map.value("TIMEOUT");
```

还有一个 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() 的重载函数，如果 map 中不存在指定键的元素，该函数使用第2个参数作为默认值：

```c++
int timeout = map.value("TIMEOUT", 30);
```

一般推荐使用 [contains](QMap.md#bool-qmapcontainsconst-key-key-const)() 和 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() 而不是 operator\[\]\(\) 运算符查找 map 中的键。原因是如果 map 中不存在相同键的元素，operator\[\]\(\) 运算符会默默地将一个元素插入到 map 中（除非 map 是 const 的）。例如，下面的代码片段将在内存中创建1000个元素：

```c++
// 错误
QMap<int, QWidget *> map;
...
for (int i = 0; i < 1000; ++i) {
    if (map[i] == okButton)
        cout << "Found button at index " << i << Qt::endl;
}
```

为了避免这个问题，将上面代码中的 `map[i]` 替换为 `map.value(i)`。

如果想遍历 QMap 中存储的所有键值对，可以使用迭代器。QMap 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)（[QMapIterator](../../M/QMapIterator/QMapIterator.md) 和 [QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md)）和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)（[QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 和 [QMap::iterator](../../M/QMap/QMap-iterator.md)）。下面是使用 Java 风格迭代器遍历 QMap<[QString](../../S/QString/QString.md), int> 的方法：

```c++
QMapIterator<QString, int> i(map);
while (i.hasNext()) {
    i.next();
    cout << i.key() << ": " << i.value() << Qt::endl;
}
```

下面是相同的代码，不过这次使用 STL 风格迭代器：

```c++
QMap<QString, int>::const_iterator i = map.constBegin();
while (i != map.constEnd()) {
    cout << i.key() << ": " << i.value() << Qt::endl;
    ++i;
}
```

上面的代码按照键的升序遍历各元素。

通常，QMap 每个键只允许有一个值。如果用已经存在的键调用 [insert](QMap.md#qmapiterator-qmapinsertconst-key-key-const-t-value)()，先前的值将被删除。例如：

```c++
map.insert("plenty", 100);
map.insert("plenty", 2000);
// map.value("plenty") == 2000
```

然而，可以使用派生类 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 在一个键中存储多个值。使用 values(const Key &key) 取得单个键关联的所有值，该函数返回一个 [QList](../../L/QList/QList.md)\<T\>：

```c++
QList<int> values = map.values("plenty");
for (int i = 0; i < values.size(); ++i)
    cout << values.at(i) << Qt::endl;
```

共享同一键的多个元素按照从最新到最早插入的顺序返回。另外一种方法是调用 [find](QMap.md#qmapiterator-qmapfindconst-key-key)() 取得 STL 风格迭代器，该迭代器指向共享同一键的多个元素中的第一个元素，然后从该元素开始遍历：

```c++
QMap<QString, int>::iterator i = map.find("plenty");
while (i != map.end() && i.key() == "plenty") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

如果只想从 map 中获取值（而不是键），也可以使用 [foreach](../../C/Container_Classes/Container_Classes.md#foreach-关键字)：

```c++
QMap<QString, int> map;
...
foreach (int value, map)
    cout << value << Qt::endl;
```

移除元素有几种方法。一种是调用 [remove](QMap.md#int-qmapremoveconst-key-key)()；该函数移除指定键的所有元素。另一种方法是使用 [QMutableMapIterator::remove](../../M/QMutableMapIterator/QMutableMapIterator.md#void-qmutablemapiteratorremove)()。另外，还可以使用 [clear](QMap.md#void-qmapclear)() 清除整个 map。

QMap 键和值的数据类型必须是[可赋值数据类型](../../C/Container_Classes/Container_Classes.md#容器类)。这涵盖了大多数可能会遇到的数据类型，但是编译器不会存储 [QWidget](../../W/QWidget/QWidget.md) 这样的对象作为值，应该存储 [QWidget](../../W/QWidget/QWidget.md) *。另外，QMap 的键类型必须提供 operator<() 运算符。QMap 用它来保持元素有序，并假定两个键 `x` 和 `y` 在 `x < y` 和 `y < x` 都不为 true 的情况下相等。

例子：

```c++
#ifndef EMPLOYEE_H
#define EMPLOYEE_H

class Employee
{
public:
    Employee() {}
    Employee(const QString &name, QDate dateOfBirth);
    ...

private:
    QString myName;
    QDate myDateOfBirth;
};

inline bool operator<(const Employee &e1, const Employee &e2)
{
    if (e1.name() != e2.name())
        return e1.name() < e2.name();
    return e1.dateOfBirth() < e2.dateOfBirth();
}

#endif // EMPLOYEE_H
```

该例中，先比较雇员名。如果雇员名相等，再比较二者的生日来分出大小。

**另请参阅** [QMapIterator](../../M/QMapIterator/QMapIterator.md)，[QMutableMapIterator](../../M/QMutableMapIterator/QMutableMapIterator.md)，[QHash](../../H/QHash/QHash.md) 和 [QSet](../../S/QSet/QSet.md).

## 成员类型文档

### typedef QMap::ConstIterator

[QMap](../../M/QMap/QMap.md)<Key, T>::const_iterator 的 Qt 风格的别名。

### typedef QMap::Iterator

[QMap](../../M/QMap/QMap.md)<Key, T>::iterator 的 Qt 风格的别名。

### typedef QMap::const_key_value_iterator

QMap::const_key_value_iterator 类型定义为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 STL 风格迭代器。

除了 operator *() 运算符返回的是键值对而不是值之外，QMap::const_key_value_iterator 基本和 [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) 相同。

Qt 5.10 中引入该类型定义。

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md)。

### typedef QMap::difference_type

ptrdiff_t 的类型别名。为兼容 STL 提供。

### typedef QMap::key_type

Key 的类型别名。为兼容 STL 提供。

### typedef QMap::key_value_iterator

QMap::key_value_iterator 类型定义为 [QMap](../../M/QMap/QMap.md) 和 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 提供 STL 风格迭代器。

除了 operator *() 运算符返回的是键值对而不是值之外，QMap::key_value_iterator 基本和 [QMap::iterator](../../M/QMap/QMap-iterator.md) 相同。

Qt 5.10 中引入该类型定义。

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md)。

### typedef QMap::mapped_type

T 的类型别名。为兼容 STL 提供。

### typedef QMap::size_type

int 的类型别名。为兼容 STL 提供。

## 成员函数文档

### QMap::QMap(const typename std::map<Key, T> &*other*)

构造一个 *other* 的副本。

**另请参阅** [toStdMap](QMap.md#stdmapkey-t-qmaptostdmap-const)()。

### QMap::QMap([QMap](QMap.md#qmapqmap)<Key, T> &&*other*)

移动构造一个 QMap 实例，使该实例指向 *other* 所指向的同一对象。

Qt 5.2 中引入该函数。

### QMap::QMap(const [QMap](QMap.md#qmapqmap)<Key, T> &*other*)

构造一个 *other* 的副本。

该操作需要[常数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)，因为 QMap 是[隐式共享](../../I/Implicit-sharing/Implicit-sharing.md)的。这使得从一个函数返回 QMap 非常快。如果共享实例被修改了，它将以[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)被复制一份（写时拷贝）。

**另请参阅** [operator=](QMap.md#qmapkey-t-qmapoperatorconst-qmapkey-t-other)()。

### QMap::QMap(std::initializer_list<std::pair<Key, T> > *list*)

用初始化列表 *list* 中每个元素的副本构造一个 map。

只有当程序在 C++11 模式下编译时，该函数才可用。

Qt 5.1 中引入该函数。

### QMap::QMap()

构造一个空 map。

**另请参阅** [clear](QMap.md#void-qmapclear)()。

### [QMap](QMap.md#qmapqmap)<Key, T> &QMap::operator=([QMap](QMap.md#qmapqmap)<Key, T> &&*other*)

移动赋值 *other* 到该 [QMap](../../M/QMap/QMap.md) 实例。

Qt 5.2 中引入该函数。

### [QMap](QMap.md#qmapqmap)<Key, T> &QMap::operator=(const [QMap](QMap.md#qmapqmap)<Key, T> &*other*)

将 *other* 赋值给该 map 并返回该 map 的引用。

### QMap::~QMap()

析构 map。该 map 中值的引用及所有该 map 的迭代器都将失效。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::begin()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一个元素。

**另请参阅** [constBegin](QMap.md#qmapconst_iterator-qmapconstbegin-const)() 和 [end](QMap.md#qmapiterator-qmapend)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::begin() const

这是一个重载函数。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::cbegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一个元素。

Qt 5.0 中引入该函数。

**另请参阅** [begin](QMap.md#qmapiterator-qmapbegin)() 和 [cend](QMap.md#qmapconst_iterator-qmapcend-const)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::cend() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一个元素之后的假想元素。

Qt 5.0 中引入该函数。

**另请参阅** [cbegin](QMap.md#qmapconst_iterator-qmapcbegin-const)() 和 [end](QMap.md#qmapiterator-qmapend)()。

### void QMap::clear()

从 map 中移除所有元素。

**另请参阅** [remove](QMap.md#int-qmapremoveconst-key-key)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::constBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一个元素。

**另请参阅** [begin](QMap.md#qmapiterator-qmapbegin)() 和 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::constEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一个元素之后的假想元素。

**另请参阅** [constBegin](QMap.md#qmapconst_iterator-qmapconstbegin-const)() 和 [end](QMap.md#qmapiterator-qmapend)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::constFind(const Key &*key*) const

返回常量类型的迭代器，指向 map 中键为 *key* 的元素。

如果 map 不包含键为 *key* 的元素，该函数返回 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)()。

Qt 4.1 中引入该函数。

**另请参阅** [find](QMap.md#qmapiterator-qmapfindconst-key-key)() 和 [QMultiMap::constFind](../../M/QMultiMap/QMultiMap.md#typename-qmapkey-tconst_iterator-qmultimapconstfindconst-key-key-const-t-value-const)()。

### [QMap::const_key_value_iterator](QMap.md#typedef-qmapconst_key_value_iterator) QMap::constKeyValueBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一项.

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QMap.md#qmapkey_value_iterator-qmapkeyvaluebegin)()。

### [QMap::const_key_value_iterator](QMap.md#typedef-qmapconst_key_value_iterator) QMap::constKeyValueEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [constKeyValueBegin](QMap.md#qmapconst_key_value_iterator-qmapconstkeyvaluebegin-const)()。

### bool QMap::contains(const Key &*key*) const

如果该 map 包含键为 *key* 的元素，返回 `true`；否则返回 `false`。

**另请参阅** [count](QMap.md#int-qmapcount-const)() 和 [QMultiMap::contains](../../M/QMultiMap/QMultiMap.md#bool-qmultimapcontainsconst-key-key-const-t-value-const)()。

### int QMap::count(const Key &*key*) const

返回与键 *key* 相关联的元素个数。

**另请参阅** [contains](QMap.md#bool-qmapcontainsconst-key-key-const)() 和 [QMultiMap::count](../../M/QMultiMap/QMultiMap.md#int-qmultimapcountconst-key-key-const-t-value-const)()。

### int QMap::count() const

这是一个重载函数。

同 [size](QMap.md#int-qmapsize-const)().

### bool QMap::empty() const

该函数为兼容 STL 提供。与 [isEmpty](QMap.md#bool-qmapisempty-const)() 等价，如果 map 为空，返回 `true`；否则返回 `false`。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::end()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一个元素之后的假想元素。

**另请参阅** [begin](QMap.md#qmapiterator-qmapbegin)() 和 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::end() const

这是一个重载函数。

### [QPair](../../P/QPair/QPair.md)<[QMap::iterator](../../M/QMap/QMap-iterator.md), [QMap::iterator](../../M/QMap/QMap-iterator.md)> QMap::equal_range(const Key &*key*)

返回一对迭代器界定与 *key* 相关联的值的范围 `[first, second)`。

### [QPair](../../P/QPair/QPair.md)<[QMap::const_iterator](../../M/QMap/QMap-const-iterator.md), [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md)> QMap::equal_range(const Key &*key*) const

这是一个重载函数。

Qt 5.6 中引入该函数。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::erase([QMap::iterator](../../M/QMap/QMap-iterator.md) *pos*)

从 map 中移除迭代器 *pos* 指向的键值对，返回指向 map 中下一个元素的迭代器。

**另请参阅** [remove](QMap.md#int-qmapremoveconst-key-key)()。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::find(const Key &*key*)

返回迭代器，指向 map 中键为 *key* 的元素。

如果 map 不包含键为 *key* 的元素，函数返回 [end](QMap.md#qmapiterator-qmapend)()。

如果 map 包含多个键为 *key* 的元素，函数返回指向最新插入的那个值的迭代器。其它值可以通过递增迭代器取得。例如，下面的代码遍历同一键的所有元素：

```c++
QMap<QString, int> map;
...
QMap<QString, int>::const_iterator i = map.find("HDR");
while (i != map.end() && i.key() == "HDR") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

**另请参阅** [constFind](QMap.md#qmapconst_iterator-qmapconstfindconst-key-key-const)()，[value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)()，[values](QMap.md#qlistt-qmapvalues-const)()，[lowerBound](QMap.md#qmapiterator-qmaplowerboundconst-key-key)()，[upperBound](QMap.md#qmapiterator-qmapupperboundconst-key-key)() 和 [QMultiMap::find](../../M/QMultiMap/QMultiMap.md#typename-qmapkey-titerator-qmultimapfindconst-key-key-const-t-value)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::find(const Key &*key*) const

这是一个重载函数。

### T &QMap::first()

返回指向 map 中第一个值的引用，即映射到最小键的值。该函数假定 map 不为空。

对于非共享 map（或者调用的是常量版本），该函数在[常数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)内完成。

Qt 5.2 中引入该函数。

**另请参阅** [last](QMap.md#t-qmaplast)()，[firstKey](QMap.md#const-key-qmapfirstkey-const)() 和 [isEmpty](QMap.md#bool-qmapisempty-const)()。

### const T &QMap::first() const

这是一个重载函数。

Qt 5.2 中引入该函数。

### const Key &QMap::firstKey() const

返回 map 中最小键的引用。该函数假定 map 不为空。

该操作在[常数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)内完成。

Qt 5.2 中引入该函数。

**另请参阅** [lastKey](QMap.md#const-key-qmaplastkey-const)()，[first](QMap.md#t-qmapfirst)()，[keyBegin](QMap.md#qmapkey_iterator-qmapkeybegin-const)() 和 [isEmpty](QMap.md#bool-qmapisempty-const)()。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::insert(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果已经存在键为 *key* 的元素，该元素的值将被 *value* 替换。

如果有多个键为 *key* 的元素，最新插入的元素的值将被 *value* 替换。

**另请参阅** [QMultiMap::insert](../../M/QMultiMap/QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)()。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::insert([QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) *pos*, const Key &*key*, const T &*value*)

这是一个重载函数。

用键 *key* 和值 *value* 插入一个新元素，*pos* 用来提示插入位置。

如果以 [constBegin](QMap.md#qmapconst_iterator-qmapconstbegin-const)() 作为插入位置提示，表明 *key* 比 map 中的任何键都小，而 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)() 则建议 *key*（严格）大于 map 中的任何键。否则提示应该满足条件 (*pos* - 1).[key](QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)() < *key* <= *pos*.[key](QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)()。如果提示 *pos* 是错误的，其将被忽略，并以常规方式插入。

如果已经存在键为 *key* 的元素，该元素的值将被 *value* 替换。

如果有多个键为 *key* 的元素，只会有一个元素的值被 *value* 替换。

如果提示是正确的，并且 map 未被共享，插入操作平均在[常数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)内完成。

从有序数据创建 map 时，从最大键的元素开始以 [constBegin](QMap.md#qmapconst_iterator-qmapconstbegin-const)() 作为提示插入，比按从小到大的顺序以 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)() 作为提示插入更快，因为 [constEnd](QMap.md#qmapconst_iterator-qmapconstend-const)() - 1 （用来检查提示是否合法）需要[对数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)。

**注意：** 需小心对待提示。提供从旧的共享实例取得的迭代器可能引起崩溃，还会有默默污染 map 和 *pos* 的 map 的风险。

Qt 5.1 中引入该函数。

**另请参阅** [QMultiMap::insert](../../M/QMultiMap/QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)()。

### void QMap::insert(const [QMap](QMap.md#qmapqmap)<Key, T> &*map*)

将 *map* 中的所有元素插入到本 map 中。

如果一个键同时在两个 map 中出现，其值将被传入的 *map* 中存储的值替换。

**注意:** 如果传入的 *map* 中同一键关联多个元素，则该键的最终值未定义。

Qt 5.15 中引入该函数。

**另请参阅** [QMultiMap::insert](../../M/QMultiMap/QMultiMap.md#typename-qmapkey-titerator-qmultimapinsertconst-key-key-const-t-value)()。

### bool QMap::isEmpty() const

如果 map 中不包含元素，返回 `true`；否则返回 `false`。

**另请参阅** [size](QMap.md#int-qmapsize-const)()。

### const Key QMap::key(const T &*value*, const Key &*defaultKey* = Key()) const

这是一个重载函数。

返回与值 *value* 对应的第一个键，如果 map 不包含值为 *value* 的元素，返回 *defaultKey*。如果没有提供 *defaultKey*，函数返回[默认构造的键](../../C/Container_Classes/Container_Classes.md#容器类)。

该函数可能会比较慢（[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QMap](../../M/QMap/QMap.md) 的内部数据结构是以快速查找键而不是值为目标来优化的。

Qt 4.3 中引入该函数。

**另请参阅** [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)() 和 [keys](QMap.md#qlistkey-qmapkeys-const)()。

### [QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) QMap::keyBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一个键。

Qt 5.6 中引入该函数。

**另请参阅** [keyEnd](QMap.md#qmapkey_iterator-qmapkeyend-const)() 和 [firstKey](QMap.md#const-key-qmapfirstkey-const)()。

### [QMap::key_iterator](../../M/QMap/QMap-key-iterator.md) QMap::keyEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的最后一个元素之后的假想元素的键。

Qt 5.6 中引入该函数。

**另请参阅** [keyBegin](QMap.md#qmapkey_iterator-qmapkeybegin-const)() 和 [lastKey](QMap.md#const-key-qmaplastkey-const)()。

### [QMap::key_value_iterator](QMap.md#typedef-qmapkey_value_iterator) QMap::keyValueBegin()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueEnd](QMap.md#qmapkey_value_iterator-qmapkeyvalueend)().

### [QMap::const_key_value_iterator](QMap.md#typedef-qmapconst_key_value_iterator) QMap::keyValueBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中的第一项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueEnd](QMap.md#qmapkey_value_iterator-qmapkeyvalueend)()。

### [QMap::key_value_iterator](QMap.md#typedef-qmapkey_value_iterator) QMap::keyValueEnd()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QMap.md#qmapkey_value_iterator-qmapkeyvaluebegin)()。

### [QMap::const_key_value_iterator](QMap.md#typedef-qmapconst_key_value_iterator) QMap::keyValueEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向 map 中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QMap.md#qmapkey_value_iterator-qmapkeyvaluebegin)()。

### [QList](../../L/QList/QList.md)\<Key\> QMap::keys() const

以升序返回 map 中所有键的列表。在 map 中多次出现的键（当该方法应用在 [QMultiMap](../../M/QMultiMap/QMultiMap.md) 时）也会在列表中多次出现。

键的顺序将确保与通过 [values](QMap.md#qlistt-qmapvalues-const)() 返回的值的顺序相同。

**另请参阅** [QMultiMap::uniqueKeys](../../M/QMultiMap/QMultiMap.md#qlistkey-qmultimapuniquekeys-const)()，[values](QMap.md#qlistt-qmapvalues-const)() 和 [key](QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)()。

### [QList](../../L/QList/QList.md)\<Key\> QMap::keys(const T &*value*) const

这是一个重载函数。

以升序返回所有与值 *value* 相关联的键的列表。

该函数可能会比较慢（[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QMap](../../M/QMap/QMap.md) 的内部数据结构是以快速查找键而不是值为目标来优化的。

### T &QMap::last()

返回 map 中最后一个值的引用，即映射到最大键的值。该函数假定 map 不为空。

对于非共享 map（或者调用的是常量版本)，该函数在[对数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)内完成。

Qt 5.2 中引入该函数。

**另请参阅** [first](QMap.md#t-qmapfirst)()，[lastKey](QMap.md#const-key-qmaplastkey-const)() 和 [isEmpty](QMap.md#bool-qmapisempty-const)()。

### const T &QMap::last() const

这是一个重载函数。

Qt 5.2 中引入该函数。

### const Key &QMap::lastKey() const

返回 map 中最大键的引用。该函数假定 map 不为空。

该函数在[对数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)内完成。

Qt 5.2 中引入该函数。

**另请参阅** [firstKey](QMap.md#const-key-qmapfirstkey-const)()，[last](QMap.md#t-qmaplast)()，[keyEnd](QMap.md#qmapkey_iterator-qmapkeyend-const)() 和 [isEmpty](QMap.md#bool-qmapisempty-const)()。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::lowerBound(const Key &*key*)

返回指向 map 中键 *key* 所关联的第一个元素的迭代器。如果 map 不包含键为 *key* 的元素，函数返回指向距离下一个键最近的元素的迭代器。

例子：

```c++
QMap<int, QString> map;
map.insert(1, "one");
map.insert(5, "five");
map.insert(10, "ten");

map.lowerBound(0);      // 返回指向 (1, "one") 的迭代器
map.lowerBound(1);      // 返回指向 (1, "one") 的迭代器
map.lowerBound(2);      // 返回指向 (5, "five") 的迭代器
map.lowerBound(10);     // 返回指向 (10, "ten") 的迭代器
map.lowerBound(999);    // 返回 end()
```

如果 map 包含多个键为 *key* 的元素，该函数返回指向最新插入的值的迭代器。其它值可以通过递增迭代器访问。例如，下面的例子遍历同一键所关联的所有元素：

```c++
QMap<QString, int> map;
...
QMap<QString, int>::const_iterator i = map.lowerBound("HDR");
QMap<QString, int>::const_iterator upperBound = map.upperBound("HDR");
while (i != upperBound) {
    cout << i.value() << Qt::endl;
    ++i;
}
```

**另请参阅** [upperBound](QMap.md#qmapiterator-qmapupperboundconst-key-key)() 和 [find](QMap.md#qmapiterator-qmapfindconst-key-key)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::lowerBound(const Key &*key*) const

这是一个重载函数。

### int QMap::remove(const Key &*key*)

从 map 中移除所有键为 *key* 的元素。返回被移除的元素个数，如果键存在，则为1，否则为0。

**另请参阅** [clear](QMap.md#void-qmapclear)()，[take](QMap.md#t-qmaptakeconst-key-key)() 和 [QMultiMap::remove](../../M/QMultiMap/QMultiMap.md#int-qmultimapremoveconst-key-key-const-t-value)()。

### int QMap::size() const

返回 map 中键值对的个数。

**另请参阅** [isEmpty](QMap.md#bool-qmapisempty-const)() 和 [count](QMap.md#int-qmapcount-const)()。

### void QMap::swap([QMap](QMap.md#qmapqmap)<Key, T> &*other*)

将 map *other* 与本 map 交换。该操作非常快，永远不失败。

Qt 4.8 中引入该函数。

### T QMap::take(const Key &*key*)

从 map 中移除键为 *key* 的元素，返回键 *key* 所关联的值。

如果 map 中不存在该元素，该函数简单返回一个[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。如果 map 中有多个键为 key 的元素，只移除最新插入的元素并返回值。

如果不使用返回值，使用 [remove](QMap.md#int-qmapremoveconst-key-key)() 更高效一些。

**另请参阅** [remove](QMap.md#int-qmapremoveconst-key-key)()。

### std::map<Key, T> QMap::toStdMap() const

返回与这个 [QMap](../../M/QMap/QMap.md) 相对应的 STL map。

### [QMap::iterator](../../M/QMap/QMap-iterator.md) QMap::upperBound(const Key &*key*)

返回迭代器，指向 map 中首个大于键 *key* 的元素。如果 map 不包含键为 *key* 的元素，该函数返回指向距离下一个键最近的元素的迭代器。

例子：

```c++
QMap<int, QString> map;
map.insert(1, "one");
map.insert(5, "five");
map.insert(10, "ten");

map.upperBound(0);      // 返回指向 (1, "one") 的迭代器
map.upperBound(1);      // 返回指向 (5, "five") 的迭代器
map.upperBound(2);      // 返回指向 (5, "five") 的迭代器
map.upperBound(10);     // 返回 end()
map.upperBound(999);    // 返回 end()
```

**另请参阅** [lowerBound](QMap.md#qmapiterator-qmaplowerboundconst-key-key)() 和 [find](QMap.md#qmapiterator-qmapfindconst-key-key)()。

### [QMap::const_iterator](../../M/QMap/QMap-const-iterator.md) QMap::upperBound(const Key &*key*) const

这是一个重载函数。

### const T QMap::value(const Key &*key*, const T &*defaultValue* = T()) const

返回键 *key* 关联的值。

如果 map 不包含键为 *key* 的元素，该函数返回 *defaultValue*。 如果没有指定 *defaultValue*，该函数返回[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。如果 map 中有多个键为 key 的元素，返回最新插入的元素的值。

**另请参阅** [key](QMap.md#const-key-qmapkeyconst-t-value-const-key-defaultkey--key-const)()，[values](QMap.md#qlistt-qmapvalues-const)()，[contains](QMap.md#bool-qmapcontainsconst-key-key-const)() 和 [operator[]](QMap.md#t-qmapoperatorconst-key-key)()。

### [QList](../../L/QList/QList.md)\<T\> QMap::values() const

按照键升序返回 map 中所有值的列表。如果一个键关联到多个值，该键的所有值都将被放入列表中，而不只是最新插入的值。

**另请参阅** [keys](QMap.md#qlistkey-qmapkeys-const)() 和 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)()。

### bool QMap::operator!=(const [QMap](QMap.md#qmapqmap)<Key, T> &*other*) const

如果 *other* 与本 map 不相等，返回 `true`，否则返回 `false`。

如果两个 map 包含相同的键值对，则认为二者相等。

该函数需要值类型实现 `operator==()`。

**另请参阅** [operator==](QMap.md#bool-qmapoperatorconst-qmapkey-t-other-const-1)()。

### bool QMap::operator==(const [QMap](QMap.md#qmapqmap)<Key, T> &*other*) const

如果 *other* 与本 map 相等，返回 `true`，否则返回 `false`。

如果两个 map 包含相同的键值对，则认为二者相等。

该函数需要值类型实现 `operator==()`。

**另请参阅** [operator!=](QMap.md#bool-qmapoperatorconst-qmapkey-t-other-const)()。

### T &QMap::operator\[\](const Key &*key*)

返回键 *key* 所关联的值的可修改引用。

如果 map 不包含键为 *key* 的元素，该函数用键 *key* 插入一个[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)，并返回该值的引用。如果 map 包含多个键为 *key* 的元素，该函数返回最新插入的那个值的引用。

**另请参阅** [insert](QMap.md#qmapiterator-qmapinsertconst-key-key-const-t-value)() 和 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)()。

### const T QMap::operator\[\](const Key &*key*) const

这是一个重载函数。

同 [value](QMap.md#const-t-qmapvalueconst-key-key-const-t-defaultvalue--t-const)()。

## 相关非成员函数

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator<<([QDataStream](../../D/QDataStream/QDataStream.md) &*out*, const [QMap](QMap.md#qmapqmap)<Key, T> &*map*)

将 *map* 写出到流 *out*。

该函数需要键和值类型实现 `operator<<()`。

**另请参阅** [QDataStream 运算符的格式](../../D/QDataStream/datastreamformat.md)。

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator>>([QDataStream](../../D/QDataStream/QDataStream.md) &*in*, [QMap](QMap.md#qmapqmap)<Key, T> &*map*)

从流 *in* 读入数据到 *map*。

该函数需要键和值类型实现 `operator>>()`。

**另请参阅** [QDataStream 运算符的格式](../../D/QDataStream/datastreamformat.md)。