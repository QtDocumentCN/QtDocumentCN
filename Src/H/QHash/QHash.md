# QHash 类

template <typename Key, typename T> class QHash

QHash 类是一种模板类，提供基于哈希表的字典类结构。[更多内容...](QHash.md#详细描述)

| 头文件:   | #include <QHash>                                     |
| -------------: | :---------------------------------------------------- |
| qmake:        | QT += core                                           |
| 派生类: | [QMultiHash](../../M/QMultiHash/QMultiHash.md) |

- [所有成员列表，包括继承的成员](../../M/QHash/QHash-members.md)
- [废弃的成员](../../M/QHash/QHash-obsolete.md)

**注意：** 该类中的所有函数都是[可重入的](../../T/Threads-Reentrancy/Threads-Reentrancy.md)。



## 公共成员类型

| class   | **[const_iterator](../../H/QHash/QHash-const-iterator.md)** |
| -------: | :------------------------------------------------------------ |
| class   | **[iterator](../../H/QHash/QHash-iterator.md)** |
| class   | **[key_iterator](../../H/QHash/QHash-key-iterator.md)** |
| typedef | **[ConstIterator](QHash.md#typedef-qhashconstiterator)** |
| typedef | **[Iterator](QHash.md#typedef-qhashiterator)** |
| typedef | **[const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator)** |
| typedef | **[difference_type](QHash.md#typedef-qhashdifference_type)** |
| typedef | **[key_type](QHash.md#typedef-qhashkey_type)** |
| typedef | **[key_value_iterator](QHash.md#typedef-qhashkey_value_iterator)** |
| typedef | **[mapped_type](QHash.md#typedef-qhashmapped_type)** |
| typedef | **[size_type](QHash.md#typedef-qhashsize_type)** |



## 公共成员函数

|                                                     | **[QHash](QHash.md#template-typename-inputiterator-qhashqhashinputiterator-begin-inputiterator-end)**(InputIterator *begin*, InputIterator *end*) |
| --------------------------------------------------: | :----------------------------------------------------------- |
|                                                     | **[QHash](QHash.md#qhashqhashqhashk-v-other)**(QHash<K, V> &&*other*) |
|                                                     | **[QHash](QHash.md#qhashqhashconst-qhashk-v-other)**(const QHash<K, V> &*other*) |
|                                                     | **[QHash](QHash.md#qhashqhashstdinitializer_liststdpairkey-t--list)**(std::initializer_list<std::pair<Key, T> > *list*) |
|                                                     | **[QHash](QHash.md#qhashqhash)**()                           |
|                                       QHash<K, V> & | **[operator=](QHash.md#qhashk-v-qhashoperatorqhashk-v-other)**(QHash<K, V> &&*other*) |
|                                       QHash<K, V> & | **[operator=](QHash.md#qhashk-v-qhashoperatorconst-qhashk-v-other)**(const QHash<K, V> &*other*) |
|                                                     | **[~QHash](QHash.md#qhashqhash-1)**()                        |
|                                     QHash::iterator | **[begin](QHash.md#qhashiterator-qhashbegin)**()             |
|                               QHash::const_iterator | **[begin](QHash.md#qhashconst_iterator-qhashbegin-const)**() const |
|                                                 int | **[capacity](QHash.md#int-qhashcapacity-const)**() const     |
|                               QHash::const_iterator | **[cbegin](QHash.md#qhashconst_iterator-qhashcbegin-const)**() const |
|                               QHash::const_iterator | **[cend](QHash.md#qhashconst_iterator-qhashcend-const)**() const |
|                                                void | **[clear](QHash.md#void-qhashclear)**()                      |
|                               QHash::const_iterator | **[constBegin](QHash.md#qhashconst_iterator-qhashconstbegin-const)**() const |
|                               QHash::const_iterator | **[constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)**() const |
|                               QHash::const_iterator | **[constFind](QHash.md#qhashconst_iterator-qhashconstfindconst-key-key-const)**(const Key &*key*) const |
|                     QHash::const_key_value_iterator | **[constKeyValueBegin](QHash.md#qhashconst_key_value_iterator-qhashconstkeyvaluebegin-const)**() const |
|                     QHash::const_key_value_iterator | **[constKeyValueEnd](QHash.md#qhashconst_key_value_iterator-qhashconstkeyvalueend-const)**() const |
|                                                bool | **[contains](QHash.md#bool-qhashcontainsconst-key-key-const)**(const Key &*key*) const |
|                                                 int | **[count](QHash.md#int-qhashcountconst-key-key-const)**(const Key &*key*) const |
|                                                 int | **[count](QHash.md#int-qhashcount-const)**() const           |
|                                                bool | **[empty](QHash.md#bool-qhashempty-const)**() const          |
|                                     QHash::iterator | **[end](QHash.md#qhashiterator-qhashend)**()                 |
|                               QHash::const_iterator | **[end](QHash.md#qhashconst_iterator-qhashend-const)**() const |
|             QPair<QHash::iterator, QHash::iterator> | **[equal_range](QHash.md#qpairqhashiterator-qhashiterator-qhashequal_rangeconst-key-key)**(const Key &*key*) |
| QPair<QHash::const_iterator, QHash::const_iterator> | **[equal_range](QHash.md#qpairqhashconst_iterator-qhashconst_iterator-qhashequal_rangeconst-key-key-const)**(const Key &*key*) const |
|                                     QHash::iterator | **[erase](QHash.md#qhashiterator-qhasheraseqhashconst_iterator-pos)**(QHash::const_iterator *pos*) |
|                                     QHash::iterator | **[erase](QHash.md#qhashiterator-qhasheraseqhashiterator-pos)**(QHash::iterator *pos*) |
|                                     QHash::iterator | **[find](QHash.md#qhashiterator-qhashfindconst-key-key)**(const Key &*key*) |
|                               QHash::const_iterator | **[find](QHash.md#qhashconst_iterator-qhashfindconst-key-key-const)**(const Key &*key*) const |
|                                     QHash::iterator | **[insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)**(const Key &*key*, const T &*value*) |
|                                                void | **[insert](QHash.md#void-qhashinsertconst-qhashk-v-other)**(const QHash<K, V> &*other*) |
|                                                bool | **[isEmpty](QHash.md#bool-qhashisempty-const)**() const      |
|                                           const Key | **[key](QHash.md#const-key-qhashkeyconst-t-value-const)**(const T &*value*) const |
|                                           const Key | **[key](QHash.md#const-key-qhashkeyconst-t-value-const-key-defaultkey-const)**(const T &*value*, const Key &*defaultKey*) const |
|                                 QHash::key_iterator | **[keyBegin](QHash.md#qhashkey_iterator-qhashkeybegin-const)**() const |
|                                 QHash::key_iterator | **[keyEnd](QHash.md#qhashkey_iterator-qhashkeyend-const)**() const |
|                           QHash::key_value_iterator | **[keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)**() |
|                     QHash::const_key_value_iterator | **[keyValueBegin](QHash.md#qhashconst_key_value_iterator-qhashkeyvaluebegin-const)**() const |
|                           QHash::key_value_iterator | **[keyValueEnd](QHash.md#qhashkey_value_iterator-qhashkeyvalueend)**() |
|                     QHash::const_key_value_iterator | **[keyValueEnd](QHash.md#qhashconst_key_value_iterator-qhashkeyvalueend-const)**() const |
|                                          QList<Key> | **[keys](QHash.md#qlistkey-qhashkeys-const)**() const        |
|                                          QList<Key> | **[keys](QHash.md#qlistkey-qhashkeysconst-t-value-const)**(const T &*value*) const |
|                                                 int | **[remove](QHash.md#int-qhashremoveconst-key-key)**(const Key &*key*) |
|                                                void | **[reserve](QHash.md#void-qhashreserveint-size)**(int *size*) |
|                                                 int | **[size](QHash.md#int-qhashsize-const)**() const             |
|                                                void | **[squeeze](QHash.md#void-qhashsqueeze)**()                  |
|                                                void | **[swap](QHash.md#void-qhashswapqhashk-v-other)**(QHash<K, V> &*other*) |
|                                                   T | **[take](QHash.md#t-qhashtakeconst-key-key)**(const Key &*key*) |
|                                             const T | **[value](QHash.md#const-t-qhashvalueconst-key-key-const)**(const Key &*key*) const |
|                                             const T | **[value](QHash.md#const-t-qhashvalueconst-key-key-const-t-defaultvalue-const)**(const Key &*key*, const T &*defaultValue*) const |
|                                            QList<T> | **[values](QHash.md#qlistt-qhashvalues-const)**() const      |
|                                                bool | **[operator!=](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const)**(const QHash<K, V> &*other*) const |
|                                                bool | **[operator==](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const-1)**(const QHash<K, V> &*other*) const |
|                                                 T & | **[operator[]](QHash.md#t-qhashoperatorconst-key-key)**(const Key &*key*) |
|                                             const T | **[operator[]](QHash.md#const-t-qhashoperatorconst-key-key-const)**(const Key &*key*) const |



## 相关非成员函数

| int           | **[qGlobalQHashSeed](QHash.md#int-qglobalqhashseed)**() |
| -------------: | :------------------------------------------------------------ |
| uint          | **[qHash](../../S/QSslDiffieHellmanParameters/QSslDiffieHellmanParameters.md#uint-qhashconst-qssldiffiehellmanparameters-dhparam-uint-seed--0)**(const QSslDiffieHellmanParameters &*dhparam*, uint *seed*) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)**(const QUrl &*url*, uint *seed* = 0) |
| uint          | **[qHash](https://doc.qt.io/qt-5/qhash-proxy.html#qHash-1)**(const QOcspResponse &*response*, uint *seed*) |
| uint          | **[qHash](QHash.md#template-typename-key-typename-t-uint-qhashconst-qhashkey-t-key-uint-seed--0)**(const QHash<Key, T> &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-key-typename-t-uint-qhashconst-qhashkey-t-key-uint-seed--0)**(const QBitArray &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-key-typename-t-uint-qhashconst-qhashkey-t-key-uint-seed--0)**(char *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-key-typename-t-uint-qhashconst-qhashkey-t-key-uint-seed--0)**(const QDateTime &*key*, uint *seed* = 0) |
| uint          | **[qHash](https://doc.qt.io/qt-5/qhash-proxy.html#qHash-2)**(QSslEllipticCurve *curve*, uint *seed*) |
| uint          | **[qHash](QHash.md#uint-qhashqlatin1string-key-uint-seed--0)**(QLatin1String *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashqlatin1string-key-uint-seed--0)**(uchar *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashqlatin1string-key-uint-seed--0)**(const QDate &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashsigned-char-key-uint-seed--0)**(signed char *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashsigned-char-key-uint-seed--0)**(const QTime &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-t-uint-qhashconst-qsett-key-uint-seed--0)**(const QSet<T> &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-t-uint-qhashconst-qsett-key-uint-seed--0)**(const T **key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#template-typename-t-uint-qhashconst-qsett-key-uint-seed--0)**(ushort *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashshort-key-uint-seed--0)**(short *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashuint-key-uint-seed--0)**(uint *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashuint-key-uint-seed--0)**(const QPair<T1, T2> &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashint-key-uint-seed--0)**(int *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashint-key-uint-seed--0)**(const std::pair<T1, T2> &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qversionnumber-key-uint-seed--0)**(const QVersionNumber &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qversionnumber-key-uint-seed--0)**(ulong *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashlong-key-uint-seed--0)**(long *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashquint64-key-uint-seed--0)**(quint64 *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashqint64-key-uint-seed--0)**(qint64 *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashfloat-key-uint-seed--0)**(float *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashdouble-key-uint-seed--0)**(double *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashlong-double-key-uint-seed--0)**(long double *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qchar-key-uint-seed--0)**(const Char *key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qbytearray-key-uint-seed--0)**(const QByteArray &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qstring-key-uint-seed--0)**(const QString &*key*, uint *seed* = 0) |
| uint          | **[qHash](QHash.md#uint-qhashconst-qstringref-key-uint-seed--0)**(const QStringRef &*key*, uint *seed* = 0) |
| uint          | **[qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)**(const void **p*, size_t *len*, uint *seed* = 0) |
| uint          | **[qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)**(InputIterator *first*, InputIterator *last*, uint *seed* = 0) |
| uint          | **[qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)**(InputIterator *first*, InputIterator *last*, uint *seed* = 0) |
| void          | **[qSetGlobalQHashSeed](QHash.md#void-qsetglobalqhashseedint-newseed)**(int *newSeed*) |
| QDataStream & | **[operator<<](QHash.md#template-typename-key-typename-t-qdatastream-operatorqdatastream-out-const-qhashkey-t-hash)**(QDataStream &*out*, const QHash<Key, T> &*hash*) |
| QDataStream & | **[operator>>](QHash.md#template-typename-key-typename-t-qdatastream-operatorqdatastream-in-qhashkey-t-hash)**(QDataStream &*in*, QHash<Key, T> &*hash*) |



## 详细描述

QHash<Key, T> 是一种 Qt 泛型[容器类](../../C/Container_Classes/Container_Classes.md)。该类存储键值对，可以用相关联的键非常快速地查找值。

QHash 的功能与 [QMap](../../M/QMap/QMap.md) 非常相似。二者的区别在于：

- QHash 的查找速度比 [QMap](../../M/QMap/QMap.md) 快。（详情请看[算法复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度) 。）
- 遍历 [QMap](../../M/QMap/QMap.md) 时，元素总是按照键的顺序排好序的。而遍历 QHash时，元素的顺序是任意的。
- [QMap](../../M/QMap/QMap.md) 的键类型必须提供 operator<() 运算符。QHash 的键类型必须提供 operator==() 运算符和名为 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 的全局哈希函数 (参考 [qHash 哈希函数](QHash.md#qhash-哈希函数))。

下面是一个键类型为 [QString](../../S/QString/QString.md)，值类型为 `int` 的 QHash 的示例：

```c++
QHash<QString, int> hash;
```

可以使用 operator[]() 运算符将键值对插入到哈希表中：

```c++
hash["one"] = 1;
hash["three"] = 3;
hash["seven"] = 7;
```

上面的代码将3个键值对插入到 QHash 中：("one", 1)，("three", 3) 和 ("seven", 7)。另外一种向哈希表中插入元素的方法是使用 [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)()：

```c++
hash.insert("twelve", 12);
```

使用 operator[]() 运算符或 [value](QHash.md#const-t-qhashvalueconst-key-key-const)() 查找值：

```c++
int num1 = hash["thirteen"];
int num2 = hash.value("thirteen");
```

如果哈希表中不存在指定的键，这些函数返回[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。

如果想检查哈希表中是否包含特定键，使用 [contains](QHash.md#bool-qhashcontainsconst-key-key-const)()：

```c++
int timeout = 30;
if (hash.contains("TIMEOUT"))
    timeout = hash.value("TIMEOUT");
```

还有一个 [value](QHash.md#const-t-qhashvalueconst-key-key-const)() 的重载函数，如果哈希表中不存在指定键的元素，该函数使用第2个参数作为默认值：

```c++
int timeout = hash.value("TIMEOUT", 30);
```

一般推荐使用 [contains](QHash.md#bool-qhashcontainsconst-key-key-const)() 和 [value](QHash.md#const-t-qhashvalueconst-key-key-const)() 而不是 operator[]() 运算符查找哈希表中的键。原因是如果哈希表中不存在相同键的元素，operator[]() 运算符会默默地将一个元素插入到哈希表中（除非哈希表是 const 的）。例如，下面的代码片段将在内存中创建1000个元素：

```c++
// 错误
QHash<int, QWidget *> hash;
...
for (int i = 0; i < 1000; ++i) {
    if (hash[i] == okButton)
        cout << "Found button at index " << i << Qt::endl;
}
```

为了避免这个问题，将上面代码中的 `hash[i]` 替换为 `hash.value(i)`。

QHash 内部使用哈希表来执行查找。哈希表自动增长和收缩以保证在不浪费太多内存的情况下快速查找。如果已经大概知道 QHash 将包含多少元素，可以通过调用 [reserve](QHash.md#void-qhashreserveint-size)() 来控制哈希表的大小，但是不能保证一定获得更好的性能。还可以调用 [capacity](QHash.md#int-qhashcapacity-const)() 来获取哈希表的大小。

如果想遍历 QHash 中存储的所有键值对，可以使用迭代器。QHash 同时提供 [Java 风格迭代器](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器)（[QHashIterator](../../H/QHashIterator/QHashIterator.md) 和 [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md)）和 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)（[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 和 [QHash::iterator](../../H/QHash/QHash-iterator.md)）。下面是使用 Java 风格迭代器遍历 QHash<[QString](../../S/QString/QString.md), int> 的方法：

```c++
QHashIterator<QString, int> i(hash);
while (i.hasNext()) {
    i.next();
    cout << i.key() << ": " << i.value() << Qt::endl;
}
```

下面是相同的代码，不过这次使用 STL 风格迭代器：

```c++
QHash<QString, int>::const_iterator i = hash.constBegin();
while (i != hash.constEnd()) {
    cout << i.key() << ": " << i.value() << Qt::endl;
    ++i;
}
```

QHash 是无序的，所以迭代器的顺序是不可预测的。如果需要通过键排序，使用 [QMap](../../M/QMap/QMap.md)。

通常，QHash 每个键只允许有一个值。如果用已经存在的键调用 [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)()，先前的值将被删除。例如：

```c++
hash.insert("plenty", 100);
hash.insert("plenty", 2000);
// hash.value("plenty") == 2000
```

如果只想从哈希表中获取值（而不是键），也可以使用 [foreach](../../C/Container_Classes/Container_Classes.md#foreach-关键字)：

```c++
QHash<QString, int> hash;
...
foreach (int value, hash)
    cout << value << Qt::endl;
```

移除元素有几种方法。一种是调用 [remove](QHash.md#int-qhashremoveconst-key-key)()；该函数移除指定键的所有元素。另一种方法是使用 [QMutableHashIterator::remove](../../M/QMutableHashIterator/QMutableHashIterator.md#void-qmutablehashiteratorremove)()。另外，还可以使用 [clear](QHash.md#void-qhashclear)() 清除整个哈希表。

QHash 键和值的数据类型必须是[可赋值数据类型](../../C/Container_Classes/Container_Classes.md#容器类)。不能存储 [QWidget](../../W/QWidget/QWidget.md) 作为值；而应该存储 [QWidget](../../W/QWidget/QWidget.md) *。



#### qHash() 哈希函数

QHash 的键类型除了必须是可赋值数据类型外，还有一个额外要求：它必须提供 operator==() 运算符，并且在键类型的命名空间内还必须有一个为键类型参数返回哈希值的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数。

该 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数基于键计算数值。可以使用任何可以想到的算法计算，只要保证相同参数返回相同值就可以。也就是说，如果 `e1 == e2`，那么 `qHash(e1) == qHash(e2)` 也保持成立。然而，为了获得更好的性能，[qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数应该尽最大可能对不同的键返回不同的哈希值。

对于键类型 `K`，[qHash](QHash.md#qhash-哈希函数) 函数必须是下面两种签名之一：

```c++
uint qHash(K key);
uint qHash(const K &key);

uint qHash(K key, uint seed);
uint qHash(const K &key, uint seed);
```

两个参数的重载函数接受一个无符号整数参数，该参数用来随机化哈希函数的计算。这个种子由 QHash 提供，为了阻止一种[算法复杂度攻击](QHash.md#算法复杂度攻击)。 如果同时定义单参数和两个参数的重载函数，QHash 将使用后者（注意，你可以定义两个参数的版本，并对 seed 参数使用默认值）。

下面是可以在 QHash 中作为键使用的 C++ 和 Qt 类型的不完全列表：任何整数类型（char，unsigned long 等），任何指针类型，[QChar](../../C/QChar/QChar.md)，[QString](../../S/QString/QString.md) 和 [QByteArray](../../B/QByteArray/QByteArray.md)。对于所有这些类型，`<QHash>` 头文件会定义 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数，该函数计算合适的哈希值。 其它许多 Qt 类也会为其类型声明 [qHash](QHash.md#qhash-哈希函数) 重载函数；具体请参考类文档。

如果想使用其它类型作为键，请确保提供 operator==() 运算符并实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数。

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

inline bool operator==(const Employee &e1, const Employee &e2)
{
    return e1.name() == e2.name()
           && e1.dateOfBirth() == e2.dateOfBirth();
}

inline uint qHash(const Employee &key, uint seed)
{
    return qHash(key.name(), seed) ^ key.dateOfBirth().day();
}

#endif // EMPLOYEE_H
```

上例中，我们依赖 Qt 的全局 [qHash](QHash.md#qhash-哈希函数)(const [QString](../../S/QString/QString.md) &, uint) 函数取得雇员名字的哈希值，然后将这个值与雇员的出生日期求异或，来为同名雇员生成各自唯一的哈希值。

注意，Qt 提供的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 重载函数的实现可能在任何时候改变。**一定不能**依赖于这个假定，认为不同 Qt 版本的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数（对于相同的输入）会计算出相同的结果。



#### 算法复杂度攻击

所有哈希表都容易受到一种特殊类型的拒绝服务攻击，攻击者预先仔细计算好一组不同的键，用这些键在哈希表的同一个 bucket 中（甚至具有相同哈希值）进行散列。攻击的目的是在数据输入表中时达到最坏情形的算法行为（O(n) 而不是平均的 O(1)，详情参考[算法复杂度](../../C/Container_Classes/Container_Classes.md#算法复杂度)）。

为了避免这种最坏情形的行为，可以在 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 计算哈希值时通过随机种子进行掺杂，抵消攻击的程度。 该种子由 QHash 自动生成，每个进程单独一个，由 QHash 传给两个参数的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 重载函数的第2个参数。

QHash 的这种随机化处理默认是激活的。尽管如此，使用者不应该依赖于特定的 QHash 顺序，这可能是在调试或回归测试等临时需要这种确定性行为的时候。要想关闭随机化处理，可以将环境变量 `QT_HASH_SEED` 设置为 0，或者使用参数 0 调用 [qSetGlobalQHashSeed](QHash.md#void-qsetglobalqhashseedint-newseed)() 函数。

**另请参阅** [QHashIterator](../../H/QHashIterator/QHashIterator.md), [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md), [QMap](../../M/QMap/QMap.md) 和 [QSet](../../S/QSet/QSet.md).

## 成员类型文档

### typedef QHash::ConstIterator

[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 的 Qt 风格的别名。

### typedef QHash::Iterator

[QHash::iterator](../../H/QHash/QHash-iterator.md) 的 Qt 风格的别名。

### typedef QHash::const_key_value_iterator

[QMap::const_key_value_iterator](../../M/QMap/QMap.md#typedef-qmapconst_key_value_iterator) 类型定义为 [QHash](QHash.md#qhash-哈希函数) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 STL 风格迭代器。

除了 operator*() 运算符返回的是键值对而不是值之外，QHash::const_key_value_iterator 基本和 [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) 相同。

Qt 5.10 中引入该类型定义。

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md)。

### typedef QHash::difference_type

ptrdiff_t 的类型别名。为兼容 STL 提供。

### typedef QHash::key_type

Key 的类型别名。为兼容 STL 提供。

### typedef QHash::key_value_iterator

QHash::key_value_iterator 类型定义为 [QHash](QHash.md#qhash-哈希函数) 和 [QMultiHash](../../M/QMultiHash/QMultiHash.md) 提供 STL 风格迭代器。

除了 operator*() 运算符返回的是键值对而不是值之外，QHash::key_value_iterator 基本和 [QHash::iterator](../../H/QHash/QHash-iterator.md) 相同。

Qt 5.10 中引入该类型定义。

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md)。

### typedef QHash::mapped_type

T 的类型别名。为兼容 STL 提供。

### typedef QHash::size_type

int 的类型别名。为兼容 STL 提供。

## 成员函数文档

### template <typename InputIterator> QHash::QHash(InputIterator *begin*, InputIterator *end*)

用迭代器范围 [*begin*, *end*) 内每个元素的副本构造一个哈希表。需要满足下列两个条件之一：迭代范围内的元素是包含 `first` 和 `second` 数据成员的对象（像 `QPair`，`std::pair` 等），分别可以转换为 `Key` 类型和 `T` 类型；或者迭代器必须含有 `key()` 和 `value()` 成员函数，分别返回可以转换为 `Key` 类型的键和 `T` 类型的值。

Qt 5.14 中引入该函数。

### QHash::QHash([QHash](QHash.md#qhashqhash)<K, V> &&*other*)

移动构造一个 QHash 实例，使该实例指向 *other* 所指向的同一对象。

Qt 5.2 中引入该函数。

### QHash::QHash(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

构造一个 *other* 的副本。

该操作需要[常数时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)，因为 QHash 是[隐式共享](../../I/Implicit-sharing/Implicit-sharing.md)的。这使得从一个函数返回  QHash 非常快。如果共享实例被修改了，它将以[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)被复制一份（写时拷贝）。

**另请参阅** [operator=](QHash.md#qhashk-v-qhashoperatorconst-qhashk-v-other)()。

### QHash::QHash(std::initializer_list<std::pair<Key, T> > *list*)

用初始化列表 *list* 中每个元素的副本构造一个哈希表。

只有当程序在 C++11 模式下编译时，该函数才可用。

Qt 5.1 中引入该函数。

### QHash::QHash()

构造一个空哈希表。

**另请参阅** [clear](QHash.md#void-qhashclear)()。

### [QHash](QHash.md#qhashqhash)<K, V> &QHash::operator=([QHash](QHash.md#qhashqhash)<K, V> &&*other*)

移动赋值 *other* 到该 [QHash](QHash.md#qhash-哈希函数)实例。

Qt 5.2 中引入该函数。

### [QHash](QHash.md#qhashqhash)<K, V> &QHash::operator=(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

将 *other* 赋值给该哈希表并返回该哈希表的引用。

### QHash::~QHash()

析构哈希表。该哈希表中值的引用及所有该哈希表的迭代器都将失效。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::begin()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first item in the hash.

**另请参阅** [constBegin](QHash.md#qhashconst_iterator-qhashconstbegin-const)() 和 [end](QHash.md#qhashiterator-qhashend)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::begin() const

这是一个重载函数。

### int QHash::capacity() const

返回 [QHash](QHash.md#qhash-哈希函数) 内部哈希表中的 bucket 数。

该函数的唯一目的是提供一种调节 [QHash](QHash.md#qhash-哈希函数) 内存使用的方法。一般很少需要调用该函数。如果想知道哈希表中的元素数，请调用 [size](QHash.md#int-qhashsize-const)()。

**另请参阅** [reserve](QHash.md#void-qhashreserveint-size)() 和 [squeeze](QHash.md#void-qhashsqueeze)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::cbegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一个元素。

Qt 5.0 中引入该函数。

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() 和 [cend](QHash.md#qhashconst_iterator-qhashcend-const)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::cend() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一个元素之后的假想元素。

Qt 5.0 中引入该函数。

**另请参阅** [cbegin](QHash.md#qhashconst_iterator-qhashcbegin-const)() 和 [end](QHash.md#qhashiterator-qhashend)()。

### void QHash::clear()

从哈希表中移除所有元素。

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一个元素。

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() 和 [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一个元素之后的假想元素。

**另请参阅** [constBegin](QHash.md#qhashconst_iterator-qhashconstbegin-const)() 和 [end](QHash.md#qhashiterator-qhashend)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constFind(const Key &*key*) const

返回常量类型（译者注：原文没有const）的迭代器，指向哈希表中键为 *key* 的元素。

如果哈希表不包含键为 *key* 的元素，该函数返回  [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)()。

Qt 4.1 中引入该函数。

**另请参阅** [find](QHash.md#qhashiterator-qhashfindconst-key-key)() 和 [QMultiHash::constFind](../../M/QMultiHash/QMultiHash.md#typename-qhashkey-tconst_iterator-qmultihashconstfindconst-key-key-const-t-value-const)()。

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::constKeyValueBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一项.

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)()。

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::constKeyValueEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [constKeyValueBegin](QHash.md#qhashconst_key_value_iterator-qhashconstkeyvaluebegin-const)()。

### bool QHash::contains(const Key &*key*) const

如果该哈希表包含键为 *key* 的元素，返回 `true`；否则返回 `false`。

**另请参阅** [count](QHash.md#int-qhashcount-const)() 和 [QMultiHash::contains](../../M/QMultiHash/QMultiHash.md#bool-qmultihashcontainsconst-key-key-const-t-value-const)()。

### int QHash::count(const Key &*key*) const

返回与键 *key* 相关联的元素个数。

**另请参阅** [contains](QHash.md#bool-qhashcontainsconst-key-key-const)() 和 [insertMulti](../../H/QHash/QHash-obsolete.md#qhashiterator-qhashinsertmulticonst-key-key-const-t-value)()。

### int QHash::count() const

这是一个重载函数。

同 [size](QHash.md#int-qhashsize-const)()。

### bool QHash::empty() const

该函数为兼容 STL 提供。与 [isEmpty](QHash.md#bool-qhashisempty-const)() 等价，如果哈希表为空，返回 `true`；否则返回 `false`。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::end()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一个元素之后的假想元素。

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() 和 [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::end() const

这是一个重载函数。

### [QPair](../../P/QPair/QPair.md)<[QHash::iterator](../../H/QHash/QHash-iterator.md), [QHash::iterator](../../H/QHash/QHash-iterator.md)> QHash::equal_range(const Key &*key*)

返回一对迭代器界定与 *key* 相关联的值的范围 `[first, second)`。如果范围为空，则两个迭代器都为 [end](QHash.md#qhashiterator-qhashend)()。

Qt 5.7 中引入该函数。

### [QPair](../../P/QPair/QPair.md)<[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md), [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)> QHash::equal_range(const Key &*key*) const

这是一个重载函数。

Qt 5.7 中引入该函数。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::erase([QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) *pos*)

从哈希表中移除迭代器 *pos* 指向的键值对，返回指向哈希表中下一个元素的迭代器。

与 [remove](QHash.md#int-qhashremoveconst-key-key)() 和 [take](QHash.md#t-qhashtakeconst-key-key)() 不同，该函数绝不会使 [QHash](QHash.md#qhash-哈希函数) 重新散列其内部数据结构。这意味着可以在迭代时安全调用该函数而不会影响哈希表中元素的顺序。例如：

```c++
QHash<QObject *, int> objectHash;
...
QHash<QObject *, int>::iterator i = objectHash.find(obj);
while (i != objectHash.end() && i.key() == obj) {
    if (i.value() == 0) {
        i = objectHash.erase(i);
    } else {
        ++i;
    }
}
```

Qt 5.7 中引入该函数。

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)()，[take](QHash.md#t-qhashtakeconst-key-key)() 和 [find](QHash.md#qhashiterator-qhashfindconst-key-key)()。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::erase([QHash::iterator](../../H/QHash/QHash-iterator.md) *pos*)

这是一个重载函数。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::find(const Key &*key*)

返回迭代器，指向哈希表中键为 *key* 的元素。

如果哈希表不包含键为 *key* 的元素，函数返回 [end](QHash.md#qhashiterator-qhashend)().

如果哈希表包含多个键为 *key* 的元素，函数返回指向最新插入的那个值的迭代器。其它值可以通过递增迭代器取得。例如，下面的代码遍历同一键的所有元素：

```c++
QHash<QString, int> hash;
...
QHash<QString, int>::const_iterator i = hash.find("HDR");
while (i != hash.end() && i.key() == "HDR") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

**另请参阅** [value](QHash.md#const-t-qhashvalueconst-key-key-const)()，[values](QHash.md#qlistt-qhashvalues-const)() 和 [QMultiHash::find](../../M/QMultiHash/QMultiHash.md#typename-qhashkey-titerator-qmultihashfindconst-key-key-const-t-value)()。

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::find(const Key &*key*) const

这是一个重载函数。

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::insert(const Key &*key*, const T &*value*)

用键 *key* 和值 *value* 插入一个新元素。

如果已经存在键为 *key* 的元素，该元素的值将被 *value* 替换。

如果有多个键为 *key* 的元素，最新插入的元素的值将被 *value* 替换。

### void QHash::insert(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

将 *other* 哈希表中的所有元素插入到本哈希表中。

如果一个键同时在两个哈希表中出现，其值将被 *other* 中存储的值替换。

**注意:** 如果 *other* 中同一键关联多个元素，则该键的最终值未定义。

Qt 5.15 中引入该函数。

### bool QHash::isEmpty() const

如果哈希表中不包含元素，返回 `true`；否则返回 `false`。

**另请参阅** [size](QHash.md#int-qhashsize-const)()。

### const Key QHash::key(const T &*value*) const

返回与值 *value* 对应的第一个键。

如果哈希表不包含值为 *value* 的元素，函数返回[默认构造的键](../../C/Container_Classes/Container_Classes.md#容器类).

该函数可能会比较慢（[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QHash ](QHash.md#qhash-哈希函数)的内部数据结构是以快速查找键而不是值为目标来优化的。

**另请参阅** [value](QHash.md#const-t-qhashvalueconst-key-key-const)() 和 [keys](QHash.md#qlistkey-qhashkeys-const)()。

### const Key QHash::key(const T &*value*, const Key &*defaultKey*) const

这是一个重载函数。

返回与值 *value* 对应的第一个键，如果哈希表不包含值为 *value* 的元素，返回 *defaultKey*。

该函数可能会比较慢（[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QHash](QHash.md#qhash-哈希函数) 的内部数据结构是以快速查找键而不是值为目标来优化的。

Qt 4.3 中引入该函数。

### [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) QHash::keyBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一个键。

Qt 5.6 中引入该函数。

**另请参阅** [keyEnd](QHash.md#qhashkey_iterator-qhashkeyend-const)()。

### [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) QHash::keyEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的最后一个元素之后的假想元素的键。

Qt 5.6 中引入该函数。

**另请参阅** [keyBegin](QHash.md#qhashkey_iterator-qhashkeybegin-const)()。

### [QHash::key_value_iterator](QHash.md#typedef-qhashkey_value_iterator) QHash::keyValueBegin()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueEnd](QHash.md#qhashkey_value_iterator-qhashkeyvalueend)()。

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::keyValueBegin() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中的第一项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueEnd](QHash.md#qhashkey_value_iterator-qhashkeyvalueend)()。

### [QHash::key_value_iterator](QHash.md#typedef-qhashkey_value_iterator) QHash::keyValueEnd()

返回 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)()。

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::keyValueEnd() const

返回常量类型的 [STL 风格迭代器](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器)，指向哈希表中最后一项之后的假想项。

Qt 5.10 中引入该函数。

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)()。

### [QList](../../L/QList/QList.md)<Key> QHash::keys() const

以任意顺序返回哈希表中所有键的列表。在哈希表中多次出现的键（当该方法应用在 [QMultiHash ](../../M/QMultiHash/QMultiHash.md)时）也会在列表中多次出现。

键的顺序将确保与通过 [values](QHash.md#qlistt-qhashvalues-const)() 返回的值的顺序相同。

**另请参阅** [QMultiMap::uniqueKeys](../../M/QMultiMap/QMultiMap.md#qlistkey-qmultimapuniquekeys-const)()，[values](QHash.md#qlistt-qhashvalues-const)() 和 [key](QHash.md#const-key-qhashkeyconst-t-value-const)()。

### [QList](../../L/QList/QList.md)<Key> QHash::keys(const T &*value*) const

这是一个重载函数。

以任意顺序返回所有与值 *value* 相关联的键的列表。

该函数可能会比较慢（[线性时间](../../C/Container_Classes/Container_Classes.md#算法复杂度)），因为 [QHash](QHash.md#qhash-哈希函数) 的内部数据结构是以快速查找键而不是值为目标来优化的。

### int QHash::remove(const Key &*key*)

从哈希表中移除所有键为 *key* 的元素。返回被移除的元素个数，如果键存在，则为1，否则为0。

**另请参阅** [clear](QHash.md#void-qhashclear)()，[take](QHash.md#t-qhashtakeconst-key-key)() 和 [QMultiHash::remove](../../M/QMultiHash/QMultiHash.md#int-qmultihashremoveconst-key-key-const-t-value)()。

### void QHash::reserve(int *size*)

确保 [QHash](QHash.md#qhash-哈希函数) 的内部哈希表包含至少 *size* 数量的 bucket。

该函数对于需要构建大型哈希表，并且不想重复分配内存的使用者来说很有用。例如：

```c++
QHash<QString, int> hash;
hash.reserve(20000);
for (int i = 0; i < 20000; ++i)
    hash.insert(keys[i], values[i]);
```

理想情况下，*size* 应该比哈希表中期望的最大元素数略大。*size* 不一定必须是质数，因为 [QHash](QHash.md#qhash-哈希函数) 内部总会使用一个质数。如果 *size* 预估小了，可能发生的最坏情形就是 [QHash](QHash.md#qhash-哈希函数) 会变慢一点。

一般很少需要调用该函数。[QHash](QHash.md#qhash-哈希函数) 的内部哈希表会自动收缩或增长来保证不浪费太多内存的情况下达到最优性能。 

**另请参阅** [squeeze](QHash.md#void-qhashsqueeze)() 和 [capacity](QHash.md#int-qhashcapacity-const)()。

### int QHash::size() const

返回哈希表中的元素个数。

**另请参阅** [isEmpty](QHash.md#bool-qhashisempty-const)() 和 [count](QHash.md#int-qhashcount-const)()。

### void QHash::squeeze()

减少 [QHash](QHash.md#qhash-哈希函数) 内部哈希表的大小以节约内存。

该函数的唯一目的是提供一种调节 [QHash](QHash.md#qhash-哈希函数) 内存使用的方法。一般很少需要调用该函数。

**另请参阅** [reserve](QHash.md#void-qhashreserveint-size)() 和 [capacity](QHash.md#int-qhashcapacity-const)()。

### void QHash::swap([QHash](QHash.md#qhashqhash)<K, V> &*other*)

将哈希表 *other* 与本哈希表。该操作非常快，永远不失败。

Qt 4.8 中引入该函数。

### T QHash::take(const Key &*key*)

从哈希表中移除键为 *key* 的元素，返回键 *key* 所关联的值。

如果哈希表中不存在该元素，该函数简单返回一个[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。如果哈希表中有多个键为 key 的元素，只移除最新插入的元素并返回值。

如果不使用返回值，使用 [remove](QHash.md#int-qhashremoveconst-key-key)() 更高效一些。

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)()。

### const T QHash::value(const Key &*key*) const

返回键 *key* 关联的值。

如果哈希表不包含键为 *key* 的元素，该函数返回[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)。如果哈希表中有多个键为 key 的元素，返回最新插入的元素的值。

**另请参阅** [key](QHash.md#const-key-qhashkeyconst-t-value-const)()，[values](QHash.md#qlistt-qhashvalues-const)()，[contains](QHash.md#bool-qhashcontainsconst-key-key-const)() 和 [operator[\]](QHash.md#t-qhashoperatorconst-key-key)()。

### const T QHash::value(const Key &*key*, const T &*defaultValue*) const

这是一个重载函数。

如果哈希表不包含键为 *key* 的元素，该函数返回 *defaultValue*。

### [QList](../../L/QList/QList.md)<T> QHash::values() const

以任意顺序返回哈希表中所有值的列表。如果一个键关联到多个值，该键的所有值都将被放入列表中，而不只是最新插入的值。

顺序将确保与通过 [keys](QHash.md#qlistkey-qhashkeys-const)() 返回的键的顺序相同。

**另请参阅** [keys](QHash.md#qlistkey-qhashkeys-const)() 和 [value](QHash.md#const-t-qhashvalueconst-key-key-const)()。

### bool QHash::operator!=(const [QHash](QHash.md#qhashqhash)<K, V> &*other*) const

如果 *other* 与本哈希表不相等，返回 `true`，否则返回 `false`。

如果两个哈希表包含相同的键值对，则认为二者相等。

该函数需要值类型实现 `operator==()`。

**另请参阅** [operator==](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const-1)()。

### bool QHash::operator==(const [QHash](QHash.md#qhashqhash)<K, V> &*other*) const

如果 *other* 与本哈希表相等，返回 `true`，否则返回 `false`。

如果两个哈希表包含相同的键值对，则认为二者相等。

该函数需要值类型实现 `operator==()`。

**另请参阅** [operator!=](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const)()。

### T &QHash::operator[](const Key &*key*)

返回键 *key* 所关联的值的可修改引用。

如果哈希表不包含键为 *key* 的元素，该函数用键 *key* 插入一个[默认构造的值](../../C/Container_Classes/Container_Classes.md#容器类)，并返回该值的引用。如果哈希表包含多个键为 *key* 的元素，该函数返回最新插入的那个值的引用。

**另请参阅** [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)() 和 [value](QHash.md#const-t-qhashvalueconst-key-key-const)()。

### const T QHash::operator[](const Key &*key*) const

这是一个重载函数。

同 [value](QHash.md#const-t-qhashvalueconst-key-key-const)()。

## 相关非成员函数

### int qGlobalQHashSeed()

返回当前全局 [QHash](QHash.md#qhash-哈希函数) 种子。

任何新创建的 [QHash](QHash.md#qhash-哈希函数) 都会设置该种子。请参考 [qHash](QHash.md#qhash-哈希函数) 了解 [QHash](QHash.md#qhash-哈希函数) 如何使用该种子。

Qt 5.6 中引入该函数。

**另请参阅** [qSetGlobalQHashSeed](QHash.md#void-qsetglobalqhashseedint-newseed)。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QUrl](../../U/QUrl/QUrl.md) &*url*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *url* 的哈希值。如果指定了 *seed*，该值用于初始化哈希表。

Qt 5.0 中引入该函数。

### template <typename Key, typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QHash](QHash.md#qhashqhash)<Key, T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来 seed 计算。

类型 `T` 必须被 qHash() 支持。

Qt 5.8 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QBitArray](../../B/QBitArray/QBitArray.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(char *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QDateTime](../../D/QDateTime/QDateTime.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([QLatin1String](../../L/QLatin1String/QLatin1String.md) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([uchar](../../G/QtGlobal/QtGlobal.md#typedef-uchar) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QDate](../../D/QDate/QDate.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(signed char *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QTime](../../T/QTime/QTime.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### template <typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QSet](../../S/QSet/QSet.md)<T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

哈希值不依赖于 *key* 中元素的顺序，即包含相同元素的 set 散列相同的值。

Qt 5.5 中引入该函数。

### template <typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const T **key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([ushort](../../G/QtGlobal/QtGlobal.md#typedef-ushort) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(short *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### template <typename T1, typename T2> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QPair](../../P/QPair/QPair.md)<T1, T2> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

类型 `T1` 和 `T2` 必须被 qHash() 支持。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(int *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### template <typename T1, typename T2> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const std::pair<T1, T2> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

类型 `T1` 和 `T2` 必须被 qHash() 支持。

**注意：** 该函数的返回类型与下面函数调用的返回类型*不同* ：

```
qHash(qMakePair(key.first, key.second), seed);
```

两个函数使用不同的哈希算法；因为二进制兼容的限制，我们不能在 Qt 6 之前修改 [QPair](../../P/QPair/QPair.md) 算法使其与 std::pair 保持一致。

Qt 5.7 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QVersionNumber](../../V/QVersionNumber/QVersionNumber.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.6 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([ulong](../../G/QtGlobal/QtGlobal.md#typedef-ulong) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(long *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([quint64](../../G/QtGlobal/QtGlobal.md#typedef-quint64) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([qint64](../../G/QtGlobal/QtGlobal.md#typedef-qint64) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(float *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.3 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(double *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.3 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(long double *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.3 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QChar](../../C/QChar/QChar.md) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QByteArray](../../B/QByteArray/QByteArray.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QString](../../S/QString/QString.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QStringRef](../../S/QStringRef/QStringRef.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *key* 的哈希值，使用 *seed* 来随机化计算结果。

Qt 5.0 中引入该函数。

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashBits(const void **p*, size_t *len*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回 *p* 指向的大小为 *len* 的内存块的哈希值，使用 *seed* 来随机化计算结果。

仅使用该函数为自定义类型实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数。例如，下面是一个如何为 std::vector<int> 实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数的例子：

```c++
inline uint qHash(const std::vector<int> &key, uint seed = 0)
{
    if (key.empty())
        return seed;
    else
        return qHashBits(&key.front(), key.size() * sizeof(int), seed);
}
```

上面的例子利用了 std::vector 连续存储数据的优势。如果不是这种情况，或者包含的类型 has padding，应该使用 [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)()。

需要再次强调，qHashBits() 的实现 - 与 Qt 提供的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数一样 - 可能在任何时候改变。**一定不能** 依赖于这个假定，认为不同 Qt 版本的 qHashBits() 函数（对于相同的输入）会计算出相同的结果。

Qt 5.4 中引入该函数。

**另请参阅** [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)() 和 [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)()。

### template <typename InputIterator> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashRange(InputIterator *first*, InputIterator *last*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回范围 [*first*,*last*) 的哈希值，使用 *seed* 来随机化计算结果，该函数依次对每个元素执行 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)()，然后将所有哈希值组合成一个值。

该函数的返回值依赖于范围中元素的顺序。这意味着

```c++
{0, 1, 2}
```

和

```c++
{1, 2, 0}
```

散列成**不同的** 值。如果顺序不重要，例如，对于哈希表，要使用 [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)()。如果想散列原始内存，使用 [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)()。

仅使用该函数为自定义类型实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数。例如，下面是一个如何为 std::vector<int> 实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数的例子：

```c++
inline uint qHash(const std::vector<int> &key, uint seed = 0)
{
    return qHashRange(key.begin(), key.end(), seed);
}
```

需要再次强调，qHashRange() 的实现 - 与 Qt 提供的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数一样 - 可能在任何时候改变。**一定不能** 依赖于这个假定，认为不同 Qt 版本的 qHashRange() 函数（对于相同的输入）会计算出相同的结果，即使该元素类型的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数可以。

Qt 5.5 中引入该函数。

**另请参阅** [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)() 和 [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)()。

### template <typename InputIterator> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashRangeCommutative(InputIterator *first*, InputIterator *last*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

返回范围 [*first*,*last*) 的哈希值，使用 *seed* 来随机化计算结果，该函数依次对每个元素执行 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)()，然后将所有哈希值组合成一个值。

该函数的返回值不依赖于范围中元素的顺序。这意味着

```c++
{0, 1, 2}
```

和

```c++
{1, 2, 0}
```

散列成**相同的** 值。如果顺序重要，例如，对于 vector 和数组， 要使用 [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)()。如果想散列原始内存，使用 [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)()。

仅使用该函数为自定义类型实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数。例如，下面是一个如何为 std::unordered_set<int> 实现 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数的例子：

```c++
inline uint qHash(const std::unordered_set<int> &key, uint seed = 0)
{
    return qHashRangeCommutative(key.begin(), key.end(), seed);
}
```

需要再次强调，qHashRangeCommutative() 的实现 - 与 Qt 提供的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数一样 - 可能在任何时候改变。**一定不能** 依赖于这个假定，认为不同 Qt 版本的 qHashRangeCommutative() 函数（对于相同的输入）会计算出相同的结果，即使该元素类型的 [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() 函数可以。

Qt 5.5 中引入该函数。

**另请参阅** [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)() 和 [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)()。

### void qSetGlobalQHashSeed(int *newSeed*)

将全局 [QHash](QHash.md#qhash-哈希函数) 种子设置为 *newSeed*。

只有在测试和调试时才需要手动设置全局 [QHash](QHash.md#qhash-哈希函数) 种子值，此时需要 [QHash](QHash.md#qhash-哈希函数) 具有确定的和可复制的行为。我们不鼓励在产品代码中这么做因为这会使软件容易受到 [算法复杂度攻击](QHash.md#算法复杂度攻击)。

从 Qt 5.10 开始，只能在 0 和 -1 之间设置值。传递 -1 将重新初始化全局 [QHash](QHash.md#qhash-哈希函数) 种子为一个随机值，传递 0 用来为 C++ 基本类型（例如 `int`）和字符串类型（[QString](../../S/QString/QString.md)，[QByteArray](../../B/QByteArray/QByteArray.md)）请求稳定算法。

任何新创建的 [QHash](QHash.md#qhash-哈希函数) 都会设置种子值。参考 [qHash](QHash.md#qhash-哈希函数) 了解 [QHash](QHash.md#qhash-哈希函数) 如何使用种子。

如果设置了环境变量 `QT_HASH_SEED`，调用该函数什么也不做。

Qt 5.6 中引入该函数。

**另请参阅** [qGlobalQHashSeed](QHash.md#int-qglobalqhashseed)。

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator<<([QDataStream](../../D/QDataStream/QDataStream.md) &*out*, const [QHash](QHash.md#qhashqhash)<Key, T> &*hash*)

将哈希表 *hash* 写出到流 *out*。

该函数需要键和值类型实现 `operator<<()`。

**另请参阅** [Serializing Qt Data Types](../../D/QDataStream/datastreamformat.md)。

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator>>([QDataStream](../../D/QDataStream/QDataStream.md) &*in*, [QHash](QHash.md#qhashqhash)<Key, T> &*hash*)

从流 *in* 读入数据到哈希表 *hash*。

该函数需要键和值类型实现 `operator>>()`。

**另请参阅** [Serializing Qt Data Types](../../D/QDataStream/datastreamformat.md)。
