# QHash Class

template <typename Key, typename T> class QHash

The QHash class is a template class that provides a hash-table-based dictionary. [更多内容...](QHash.md#详细描述)

| 头文件:   | #include <QHash>                                     |
| -------------: | :---------------------------------------------------- |
| qmake:        | QT += core                                           |
| 基类: | [QObject](../../O/QObject/QObject.md) |
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
| uint          | **[qHash](QHash.md#uint-qhashconst-qchar-key-uint-seed--0)**(const QChar *key*, uint *seed* = 0) |
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

QHash<Key, T> is one of Qt's generic [container classes](../../C/Container_Classes/Container_Classes.md). It stores (key, value) pairs and provides very fast lookup of the value associated with a key.

QHash provides very similar functionality to [QMap](../../M/QMap/QMap.md). The differences are:

- QHash provides faster lookups than [QMap](../../M/QMap/QMap.md). (See [Algorithmic Complexity](../../C/Container_Classes/Container_Classes.md#算法复杂度) for details.)
- When iterating over a [QMap](../../M/QMap/QMap.md), the items are always sorted by key. With QHash, the items are arbitrarily ordered.
- The key type of a [QMap](../../M/QMap/QMap.md) must provide operator<(). The key type of a QHash must provide operator==() and a global hash function called [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() (see [qHash](QHash.md#qhash-哈希函数)).

Here's an example QHash with [QString](../../S/QString/QString.md) keys and `int` values:

```
QHash<QString, int> hash;
```

To insert a (key, value) pair into the hash, you can use operator[]():

```
hash["one"] = 1;
hash["three"] = 3;
hash["seven"] = 7;
```

This inserts the following three (key, value) pairs into the QHash: ("one", 1), ("three", 3), and ("seven", 7). Another way to insert items into the hash is to use [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)():

```
hash.insert("twelve", 12);
```

To look up a value, use operator[]() or [value](QHash.md#const-t-qhashvalueconst-key-key-const)():

```
int num1 = hash["thirteen"];
int num2 = hash.value("thirteen");
```

If there is no item with the specified key in the hash, these functions return a [default-constructed value](../../C/Container_Classes/Container_Classes.md#容器类).

If you want to check whether the hash contains a particular key, use [contains](QHash.md#bool-qhashcontainsconst-key-key-const)():

```
int timeout = 30;
if (hash.contains("TIMEOUT"))
    timeout = hash.value("TIMEOUT");
```

There is also a [value](QHash.md#const-t-qhashvalueconst-key-key-const)() overload that uses its second argument as a default value if there is no item with the specified key:

```
int timeout = hash.value("TIMEOUT", 30);
```

In general, we recommend that you use [contains](QHash.md#bool-qhashcontainsconst-key-key-const)() and [value](QHash.md#const-t-qhashvalueconst-key-key-const)() rather than operator[]() for looking up a key in a hash. The reason is that operator[]() silently inserts an item into the hash if no item exists with the same key (unless the hash is const). For example, the following code snippet will create 1000 items in memory:

```
// WRONG
QHash<int, QWidget *> hash;
...
for (int i = 0; i < 1000; ++i) {
    if (hash[i] == okButton)
        cout << "Found button at index " << i << Qt::endl;
}
```

To avoid this problem, replace `hash[i]` with `hash.value(i)` in the code above.

Internally, QHash uses a hash table to perform lookups. This hash table automatically grows and shrinks to provide fast lookups without wasting too much memory. You can still control the size of the hash table by calling [reserve](QHash.md#void-qhashreserveint-size)() if you already know approximately how many items the QHash will contain, but this isn't necessary to obtain good performance. You can also call [capacity](QHash.md#int-qhashcapacity-const)() to retrieve the hash table's size.

If you want to navigate through all the (key, value) pairs stored in a QHash, you can use an iterator. QHash provides both [Java-style iterators](../../C/Container_Classes/Container_Classes.md#Java-风格迭代器) ([QHashIterator](../../H/QHashIterator/QHashIterator.md) and [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md)) and [STL-style iterators](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) ([QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) and [QHash::iterator](../../H/QHash/QHash-iterator.md)). Here's how to iterate over a QHash<[QString](../../S/QString/QString.md), int> using a Java-style iterator:

```
QHashIterator<QString, int> i(hash);
while (i.hasNext()) {
    i.next();
    cout << i.key() << ": " << i.value() << Qt::endl;
}
```

Here's the same code, but using an STL-style iterator:

```
QHash<QString, int>::const_iterator i = hash.constBegin();
while (i != hash.constEnd()) {
    cout << i.key() << ": " << i.value() << Qt::endl;
    ++i;
}
```

QHash is unordered, so an iterator's sequence cannot be assumed to be predictable. If ordering by key is required, use a [QMap](../../M/QMap/QMap.md).

Normally, a QHash allows only one value per key. If you call [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)() with a key that already exists in the QHash, the previous value is erased. For example:

```
hash.insert("plenty", 100);
hash.insert("plenty", 2000);
// hash.value("plenty") == 2000
```

If you only need to extract the values from a hash (not the keys), you can also use [foreach](../../C/Container_Classes/Container_Classes.md#foreach-关键字):

```
QHash<QString, int> hash;
...
foreach (int value, hash)
    cout << value << Qt::endl;
```

Items can be removed from the hash in several ways. One way is to call [remove](QHash.md#int-qhashremoveconst-key-key)(); this will remove any item with the given key. Another way is to use [QMutableHashIterator::remove](../../M/QMutableHashIterator/QMutableHashIterator.md#void-qmutablehashiteratorremove)(). In addition, you can clear the entire hash using [clear](QHash.md#void-qhashclear)().

QHash's key and value data types must be [assignable data types](../../C/Container_Classes/Container_Classes.md#容器类). You cannot, for example, store a [QWidget](../../W/QWidget/QWidget.md) as a value; instead, store a [QWidget](../../W/QWidget/QWidget.md) *.



#### qHash() 哈希函数

A QHash's key type has additional requirements other than being an assignable data type: it must provide operator==(), and there must also be a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() function in the type's namespace that returns a hash value for an argument of the key's type.

The [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() function computes a numeric value based on a key. It can use any algorithm imaginable, as long as it always returns the same value if given the same argument. In other words, if `e1 == e2`, then `qHash(e1) == qHash(e2)` must hold as well. However, to obtain good performance, the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() function should attempt to return different hash values for different keys to the largest extent possible.

For a key type `K`, the [qHash](QHash.md#qhash-哈希函数) function must have one of these signatures:

```
uint qHash(K key);
uint qHash(const K &key);

uint qHash(K key, uint seed);
uint qHash(const K &key, uint seed);
```

The two-arguments overloads take an unsigned integer that should be used to seed the calculation of the hash function. This seed is provided by QHash in order to prevent a family of [algorithmic complexity attacks](QHash.md#算法复杂度攻击). If both a one-argument and a two-arguments overload are defined for a key type, the latter is used by QHash (note that you can simply define a two-arguments version, and use a default value for the seed parameter).

Here's a partial list of the C++ and Qt types that can serve as keys in a QHash: any integer type (char, unsigned long, etc.), any pointer type, [QChar](../../C/QChar/QChar.md), [QString](../../S/QString/QString.md), and [QByteArray](../../B/QByteArray/QByteArray.md). For all of these, the `<QHash>` header defines a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() function that computes an adequate hash value. Many other Qt classes also declare a [qHash](QHash.md#qhash-哈希函数) overload for their type; please refer to the documentation of each class.

If you want to use other types as the key, make sure that you provide operator==() and a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() implementation.

Example:

```
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

In the example above, we've relied on Qt's global [qHash](QHash.md#qhash-哈希函数)(const [QString](../../S/QString/QString.md) &, uint) to give us a hash value for the employee's name, and XOR'ed this with the day they were born to help produce unique hashes for people with the same name.

Note that the implementation of the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overloads offered by Qt may change at any time. You **must not** rely on the fact that [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() will give the same results (for the same inputs) across different Qt versions.



#### 算法复杂度攻击

All hash tables are vulnerable to a particular class of denial of service attacks, in which the attacker carefully pre-computes a set of different keys that are going to be hashed in the same bucket of a hash table (or even have the very same hash value). The attack aims at getting the worst-case algorithmic behavior (O(n) instead of amortized O(1), see [Algorithmic Complexity](../../C/Container_Classes/Container_Classes.md#算法复杂度) for the details) when the data is fed into the table.

In order to avoid this worst-case behavior, the calculation of the hash value done by [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() can be salted by a random seed, that nullifies the attack's extent. This seed is automatically generated by QHash once per process, and then passed by QHash as the second argument of the two-arguments overload of the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() function.

This randomization of QHash is enabled by default. Even though programs should never depend on a particular QHash ordering, there may be situations where you temporarily need deterministic behavior, for example for debugging or regression testing. To disable the randomization, define the environment variable `QT_HASH_SEED` to have the value 0. Alternatively, you can call the [qSetGlobalQHashSeed](QHash.md#void-qsetglobalqhashseedint-newseed)() function with the value 0.

**另请参阅** [QHashIterator](../../H/QHashIterator/QHashIterator.md), [QMutableHashIterator](../../M/QMutableHashIterator/QMutableHashIterator.md), [QMap](../../M/QMap/QMap.md), and [QSet](../../S/QSet/QSet.md).

## 成员类型文档

### typedef QHash::ConstIterator

Qt-style synonym for [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md).

### typedef QHash::Iterator

Qt-style synonym for [QHash::iterator](../../H/QHash/QHash-iterator.md).

### typedef QHash::const_key_value_iterator

The [QMap::const_key_value_iterator](../../M/QMap/QMap.md#typedef-qmapconst_key_value_iterator) typedef provides an STL-style const iterator for [QHash](QHash.md#qhash-哈希函数) and [QMultiHash](../../M/QMultiHash/QMultiHash.md).

QHash::const_key_value_iterator is essentially the same as [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) with the difference that operator*() returns a key/value pair instead of a value.

This typedef was introduced in Qt 5.10.

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md).

### typedef QHash::difference_type

Typedef for ptrdiff_t. Provided for STL compatibility.

### typedef QHash::key_type

Typedef for Key. Provided for STL compatibility.

### typedef QHash::key_value_iterator

The [QMap::key_value_iterator](../../M/QMap/QMap.md#typedef-qmapkey_value_iterator) typedef provides an STL-style iterator for [QHash](QHash.md#qhash-哈希函数) and [QMultiHash](../../M/QMultiHash/QMultiHash.md).

QHash::key_value_iterator is essentially the same as [QHash::iterator](../../H/QHash/QHash-iterator.md) with the difference that operator*() returns a key/value pair instead of a value.

This typedef was introduced in Qt 5.10.

**另请参阅** [QKeyValueIterator](../../K/QKeyValueIterator/QKeyValueIterator.md).

### typedef QHash::mapped_type

Typedef for T. Provided for STL compatibility.

### typedef QHash::size_type

Typedef for int. Provided for STL compatibility.

## 成员函数文档

### template <typename InputIterator> QHash::QHash(InputIterator *begin*, InputIterator *end*)

Constructs a hash with a copy of each of the elements in the iterator range [*begin*, *end*). Either the elements iterated by the range must be objects with `first` and `second` data members (like `QPair`, `std::pair`, etc.) convertible to `Key` and to `T` respectively; or the iterators must have `key()` and `value()` member functions, returning a key convertible to `Key` and a value convertible to `T` respectively.

This function was introduced in Qt 5.14.

### QHash::QHash([QHash](QHash.md#qhashqhash)<K, V> &&*other*)

Move-constructs a QHash instance, making it point at the same object that *other* was pointing to.

This function was introduced in Qt 5.2.

### QHash::QHash(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

Constructs a copy of *other*.

This operation occurs in [constant time](../../C/Container_Classes/Container_Classes.md#算法复杂度), because QHash is [implicitly shared](../../I/Implicit-sharing/Implicit-sharing.md). This makes returning a QHash from a function very fast. If a shared instance is modified, it will be copied (copy-on-write), and this takes [linear time](../../C/Container_Classes/Container_Classes.md#算法复杂度).

**另请参阅** [operator=](QHash.md#qhashk-v-qhashoperatorconst-qhashk-v-other)().

### QHash::QHash(std::initializer_list<std::pair<Key, T> > *list*)

Constructs a hash with a copy of each of the elements in the initializer list *list*.

This function is only available if the program is being compiled in C++11 mode.

This function was introduced in Qt 5.1.

### QHash::QHash()

Constructs an empty hash.

**另请参阅** [clear](QHash.md#void-qhashclear)().

### [QHash](QHash.md#qhashqhash)<K, V> &QHash::operator=([QHash](QHash.md#qhashqhash)<K, V> &&*other*)

Move-assigns *other* to this [QHash](QHash.md#qhash-哈希函数) instance.

This function was introduced in Qt 5.2.

### [QHash](QHash.md#qhashqhash)<K, V> &QHash::operator=(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

Assigns *other* to this hash and returns a reference to this hash.

### QHash::~QHash()

Destroys the hash. References to the values in the hash and all iterators of this hash become invalid.

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::begin()

Returns an [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first item in the hash.

**另请参阅** [constBegin](QHash.md#qhashconst_iterator-qhashconstbegin-const)() and [end](QHash.md#qhashiterator-qhashend)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::begin() const

This is an overloaded function.

### int QHash::capacity() const

Returns the number of buckets in the [QHash](QHash.md#qhash-哈希函数)'s internal hash table.

The sole purpose of this function is to provide a means of fine tuning [QHash](QHash.md#qhash-哈希函数)'s memory usage. In general, you will rarely ever need to call this function. If you want to know how many items are in the hash, call [size](QHash.md#int-qhashsize-const)().

**另请参阅** [reserve](QHash.md#void-qhashreserveint-size)() and [squeeze](QHash.md#void-qhashsqueeze)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::cbegin() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first item in the hash.

This function was introduced in Qt 5.0.

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() and [cend](QHash.md#qhashconst_iterator-qhashcend-const)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::cend() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary item after the last item in the hash.

This function was introduced in Qt 5.0.

**另请参阅** [cbegin](QHash.md#qhashconst_iterator-qhashcbegin-const)() and [end](QHash.md#qhashiterator-qhashend)().

### void QHash::clear()

Removes all items from the hash.

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constBegin() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first item in the hash.

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() and [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constEnd() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary item after the last item in the hash.

**另请参阅** [constBegin](QHash.md#qhashconst_iterator-qhashconstbegin-const)() and [end](QHash.md#qhashiterator-qhashend)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::constFind(const Key &*key*) const

Returns an iterator pointing to the item with the *key* in the hash.

If the hash contains no item with the *key*, the function returns [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)().

This function was introduced in Qt 4.1.

**另请参阅** [find](QHash.md#qhashiterator-qhashfindconst-key-key)() and [QMultiHash::constFind](../../M/QMultiHash/QMultiHash.md#typename-qhashkey-tconst_iterator-qmultihashconstfindconst-key-key-const-t-value-const)().

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::constKeyValueBegin() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)().

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::constKeyValueEnd() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary entry after the last entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [constKeyValueBegin](QHash.md#qhashconst_key_value_iterator-qhashconstkeyvaluebegin-const)().

### bool QHash::contains(const Key &*key*) const

Returns `true` if the hash contains an item with the *key*; otherwise returns `false`.

**另请参阅** [count](QHash.md#int-qhashcount-const)() and [QMultiHash::contains](../../M/QMultiHash/QMultiHash.md#bool-qmultihashcontainsconst-key-key-const-t-value-const)().

### int QHash::count(const Key &*key*) const

Returns the number of items associated with the *key*.

**另请参阅** [contains](QHash.md#bool-qhashcontainsconst-key-key-const)() and [insertMulti](../../H/QHash/QHash-obsolete.md#qhashiterator-qhashinsertmulticonst-key-key-const-t-value)().

### int QHash::count() const

This is an overloaded function.

Same as [size](QHash.md#int-qhashsize-const)().

### bool QHash::empty() const

This function is provided for STL compatibility. It is equivalent to [isEmpty](QHash.md#bool-qhashisempty-const)(), returning true if the hash is empty; otherwise returns `false`.

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::end()

Returns an [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary item after the last item in the hash.

**另请参阅** [begin](QHash.md#qhashiterator-qhashbegin)() and [constEnd](QHash.md#qhashconst_iterator-qhashconstend-const)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::end() const

This is an overloaded function.

### [QPair](../../P/QPair/QPair.md)<[QHash::iterator](../../H/QHash/QHash-iterator.md), [QHash::iterator](../../H/QHash/QHash-iterator.md)> QHash::equal_range(const Key &*key*)

Returns a pair of iterators delimiting the range of values `[first, second)`, that are stored under *key*. If the range is empty then both iterators will be equal to [end](QHash.md#qhashiterator-qhashend)().

This function was introduced in Qt 5.7.

### [QPair](../../P/QPair/QPair.md)<[QHash::const_iterator](../../H/QHash/QHash-const-iterator.md), [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md)> QHash::equal_range(const Key &*key*) const

This is an overloaded function.

This function was introduced in Qt 5.7.

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::erase([QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) *pos*)

Removes the (key, value) pair associated with the iterator *pos* from the hash, and returns an iterator to the next item in the hash.

Unlike [remove](QHash.md#int-qhashremoveconst-key-key)() and [take](QHash.md#t-qhashtakeconst-key-key)(), this function never causes [QHash](QHash.md#qhash-哈希函数) to rehash its internal data structure. This means that it can safely be called while iterating, and won't affect the order of items in the hash. For example:

```
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

This function was introduced in Qt 5.7.

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)(), [take](QHash.md#t-qhashtakeconst-key-key)(), and [find](QHash.md#qhashiterator-qhashfindconst-key-key)().

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::erase([QHash::iterator](../../H/QHash/QHash-iterator.md) *pos*)

This is an overloaded function.

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::find(const Key &*key*)

Returns an iterator pointing to the item with the *key* in the hash.

If the hash contains no item with the *key*, the function returns [end](QHash.md#qhashiterator-qhashend)().

If the hash contains multiple items with the *key*, this function returns an iterator that points to the most recently inserted value. The other values are accessible by incrementing the iterator. For example, here's some code that iterates over all the items with the same key:

```
QHash<QString, int> hash;
...
QHash<QString, int>::const_iterator i = hash.find("HDR");
while (i != hash.end() && i.key() == "HDR") {
    cout << i.value() << Qt::endl;
    ++i;
}
```

**另请参阅** [value](QHash.md#const-t-qhashvalueconst-key-key-const)(), [values](QHash.md#qlistt-qhashvalues-const)(), and [QMultiHash::find](../../M/QMultiHash/QMultiHash.md#typename-qhashkey-titerator-qmultihashfindconst-key-key-const-t-value)().

### [QHash::const_iterator](../../H/QHash/QHash-const-iterator.md) QHash::find(const Key &*key*) const

This is an overloaded function.

### [QHash::iterator](../../H/QHash/QHash-iterator.md) QHash::insert(const Key &*key*, const T &*value*)

Inserts a new item with the *key* and a value of *value*.

If there is already an item with the *key*, that item's value is replaced with *value*.

If there are multiple items with the *key*, the most recently inserted item's value is replaced with *value*.

### void QHash::insert(const [QHash](QHash.md#qhashqhash)<K, V> &*other*)

Inserts all the items in the *other* hash into this hash.

If a key is common to both hashes, its value will be replaced with the value stored in *other*.

**Note:** If *other* contains multiple entries with the same key then the final value of the key is undefined.

This function was introduced in Qt 5.15.

### bool QHash::isEmpty() const

Returns `true` if the hash contains no items; otherwise returns false.

**另请参阅** [size](QHash.md#int-qhashsize-const)().

### const Key QHash::key(const T &*value*) const

Returns the first key mapped to *value*.

If the hash contains no item with the *value*, the function returns a [default-constructed key](../../C/Container_Classes/Container_Classes.md#容器类).

This function can be slow ([linear time](../../C/Container_Classes/Container_Classes.md#算法复杂度)), because [QHash](QHash.md#qhash-哈希函数)'s internal data structure is optimized for fast lookup by key, not by value.

**另请参阅** [value](QHash.md#const-t-qhashvalueconst-key-key-const)() and [keys](QHash.md#qlistkey-qhashkeys-const)().

### const Key QHash::key(const T &*value*, const Key &*defaultKey*) const

This is an overloaded function.

Returns the first key mapped to *value*, or *defaultKey* if the hash contains no item mapped to *value*.

This function can be slow ([linear time](../../C/Container_Classes/Container_Classes.md#算法复杂度)), because [QHash](QHash.md#qhash-哈希函数)'s internal data structure is optimized for fast lookup by key, not by value.

This function was introduced in Qt 4.3.

### [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) QHash::keyBegin() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first key in the hash.

This function was introduced in Qt 5.6.

**另请参阅** [keyEnd](QHash.md#qhashkey_iterator-qhashkeyend-const)().

### [QHash::key_iterator](../../H/QHash/QHash-key-iterator.md) QHash::keyEnd() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary item after the last key in the hash.

This function was introduced in Qt 5.6.

**另请参阅** [keyBegin](QHash.md#qhashkey_iterator-qhashkeybegin-const)().

### [QHash::key_value_iterator](QHash.md#typedef-qhashkey_value_iterator) QHash::keyValueBegin()

Returns an [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [keyValueEnd](QHash.md#qhashkey_value_iterator-qhashkeyvalueend)().

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::keyValueBegin() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the first entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [keyValueEnd](QHash.md#qhashkey_value_iterator-qhashkeyvalueend)().

### [QHash::key_value_iterator](QHash.md#typedef-qhashkey_value_iterator) QHash::keyValueEnd()

Returns an [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary entry after the last entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)().

### [QHash::const_key_value_iterator](QHash.md#typedef-qhashconst_key_value_iterator) QHash::keyValueEnd() const

Returns a const [STL-style iterator](../../C/Container_Classes/Container_Classes.md#STL-风格迭代器) pointing to the imaginary entry after the last entry in the hash.

This function was introduced in Qt 5.10.

**另请参阅** [keyValueBegin](QHash.md#qhashkey_value_iterator-qhashkeyvaluebegin)().

### [QList](../../L/QList/QList.md)<Key> QHash::keys() const

Returns a list containing all the keys in the hash, in an arbitrary order. Keys that occur multiple times in the hash (because the method is operating on a [QMultiHash](../../M/QMultiHash/QMultiHash.md)) also occur multiple times in the list.

The order is guaranteed to be the same as that used by [values](QHash.md#qlistt-qhashvalues-const)().

**另请参阅** [QMultiMap::uniqueKeys](../../M/QMultiMap/QMultiMap.md#qlistkey-qmultimapuniquekeys-const)(), [values](QHash.md#qlistt-qhashvalues-const)(), and [key](QHash.md#const-key-qhashkeyconst-t-value-const)().

### [QList](../../L/QList/QList.md)<Key> QHash::keys(const T &*value*) const

This is an overloaded function.

Returns a list containing all the keys associated with value *value*, in an arbitrary order.

This function can be slow ([linear time](../../C/Container_Classes/Container_Classes.md#算法复杂度)), because [QHash](QHash.md#qhash-哈希函数)'s internal data structure is optimized for fast lookup by key, not by value.

### int QHash::remove(const Key &*key*)

Removes all the items that have the *key* from the hash. Returns the number of items removed which is 1 if the key exists in the hash, and 0 otherwise.

**另请参阅** [clear](QHash.md#void-qhashclear)(), [take](QHash.md#t-qhashtakeconst-key-key)(), and [QMultiHash::remove](../../M/QMultiHash/QMultiHash.md#int-qmultihashremoveconst-key-key-const-t-value)().

### void QHash::reserve(int *size*)

Ensures that the [QHash](QHash.md#qhash-哈希函数)'s internal hash table consists of at least *size* buckets.

This function is useful for code that needs to build a huge hash and wants to avoid repeated reallocation. For example:

```
QHash<QString, int> hash;
hash.reserve(20000);
for (int i = 0; i < 20000; ++i)
    hash.insert(keys[i], values[i]);
```

Ideally, *size* should be slightly more than the maximum number of items expected in the hash. *size* doesn't have to be prime, because [QHash](QHash.md#qhash-哈希函数) will use a prime number internally anyway. If *size* is an underestimate, the worst that will happen is that the [QHash](QHash.md#qhash-哈希函数) will be a bit slower.

In general, you will rarely ever need to call this function. [QHash](QHash.md#qhash-哈希函数)'s internal hash table automatically shrinks or grows to provide good performance without wasting too much memory.

**另请参阅** [squeeze](QHash.md#void-qhashsqueeze)() and [capacity](QHash.md#int-qhashcapacity-const)().

### int QHash::size() const

Returns the number of items in the hash.

**另请参阅** [isEmpty](QHash.md#bool-qhashisempty-const)() and [count](QHash.md#int-qhashcount-const)().

### void QHash::squeeze()

Reduces the size of the [QHash](QHash.md#qhash-哈希函数)'s internal hash table to save memory.

The sole purpose of this function is to provide a means of fine tuning [QHash](QHash.md#qhash-哈希函数)'s memory usage. In general, you will rarely ever need to call this function.

**另请参阅** [reserve](QHash.md#void-qhashreserveint-size)() and [capacity](QHash.md#int-qhashcapacity-const)().

### void QHash::swap([QHash](QHash.md#qhashqhash)<K, V> &*other*)

Swaps hash *other* with this hash. This operation is very fast and never fails.

This function was introduced in Qt 4.8.

### T QHash::take(const Key &*key*)

Removes the item with the *key* from the hash and returns the value associated with it.

If the item does not exist in the hash, the function simply returns a [default-constructed value](../../C/Container_Classes/Container_Classes.md#容器类). If there are multiple items for *key* in the hash, only the most recently inserted one is removed.

If you don't use the return value, [remove](QHash.md#int-qhashremoveconst-key-key)() is more efficient.

**另请参阅** [remove](QHash.md#int-qhashremoveconst-key-key)().

### const T QHash::value(const Key &*key*) const

Returns the value associated with the *key*.

If the hash contains no item with the *key*, the function returns a [default-constructed value](../../C/Container_Classes/Container_Classes.md#容器类). If there are multiple items for the *key* in the hash, the value of the most recently inserted one is returned.

**另请参阅** [key](QHash.md#const-key-qhashkeyconst-t-value-const)(), [values](QHash.md#qlistt-qhashvalues-const)(), [contains](QHash.md#bool-qhashcontainsconst-key-key-const)(), and [operator[\]](QHash.md#t-qhashoperatorconst-key-key)().

### const T QHash::value(const Key &*key*, const T &*defaultValue*) const

This is an overloaded function.

If the hash contains no item with the given *key*, the function returns *defaultValue*.

### [QList](../../L/QList/QList.md)<T> QHash::values() const

Returns a list containing all the values in the hash, in an arbitrary order. If a key is associated with multiple values, all of its values will be in the list, and not just the most recently inserted one.

The order is guaranteed to be the same as that used by [keys](QHash.md#qlistkey-qhashkeys-const)().

**另请参阅** [keys](QHash.md#qlistkey-qhashkeys-const)() and [value](QHash.md#const-t-qhashvalueconst-key-key-const)().

### bool QHash::operator!=(const [QHash](QHash.md#qhashqhash)<K, V> &*other*) const

Returns `true` if *other* is not equal to this hash; otherwise returns `false`.

Two hashes are considered equal if they contain the same (key, value) pairs.

This function requires the value type to implement `operator==()`.

**另请参阅** [operator==](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const-1)().

### bool QHash::operator==(const [QHash](QHash.md#qhashqhash)<K, V> &*other*) const

Returns `true` if *other* is equal to this hash; otherwise returns false.

Two hashes are considered equal if they contain the same (key, value) pairs.

This function requires the value type to implement `operator==()`.

**另请参阅** [operator!=](QHash.md#bool-qhashoperatorconst-qhashk-v-other-const)().

### T &QHash::operator[](const Key &*key*)

Returns the value associated with the *key* as a modifiable reference.

If the hash contains no item with the *key*, the function inserts a [default-constructed value](../../C/Container_Classes/Container_Classes.md#容器类) into the hash with the *key*, and returns a reference to it. If the hash contains multiple items with the *key*, this function returns a reference to the most recently inserted value.

**另请参阅** [insert](QHash.md#qhashiterator-qhashinsertconst-key-key-const-t-value)() and [value](QHash.md#const-t-qhashvalueconst-key-key-const)().

### const T QHash::operator[](const Key &*key*) const

This is an overloaded function.

Same as [value](QHash.md#const-t-qhashvalueconst-key-key-const)().

## Related Non-Members

### int qGlobalQHashSeed()

Returns the current global [QHash](QHash.md#qhash-哈希函数) seed.

The seed is set in any newly created [QHash](QHash.md#qhash-哈希函数). See [qHash](QHash.md#qhash-哈希函数) about how this seed is being used by [QHash](QHash.md#qhash-哈希函数).

This function was introduced in Qt 5.6.

**另请参阅** [qSetGlobalQHashSeed](QHash.md#void-qsetglobalqhashseedint-newseed).

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QUrl](../../U/QUrl/QUrl.md) &*url*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *url*. If specified, *seed* is used to initialize the hash.

This function was introduced in Qt 5.0.

### template <typename Key, typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QHash](QHash.md#qhashqhash)<Key, T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

Type `T` must be supported by qHash().

This function was introduced in Qt 5.8.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QBitArray](../../B/QBitArray/QBitArray.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(char *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QDateTime](../../D/QDateTime/QDateTime.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([QLatin1String](../../L/QLatin1String/QLatin1String.md) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([uchar](../../G/QtGlobal/QtGlobal.md#typedef-uchar) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QDate](../../D/QDate/QDate.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(signed char *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QTime](../../T/QTime/QTime.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### template <typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QSet](../../S/QSet/QSet.md)<T> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

The hash value is independent of the order of elements in *key*, that is, sets that contain the same elements hash to the same value.

This function was introduced in Qt 5.5.

### template <typename T> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const T **key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([ushort](../../G/QtGlobal/QtGlobal.md#typedef-ushort) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(short *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### template <typename T1, typename T2> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QPair](../../P/QPair/QPair.md)<T1, T2> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

Types `T1` and `T2` must be supported by qHash().

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(int *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### template <typename T1, typename T2> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const std::pair<T1, T2> &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

Types `T1` and `T2` must be supported by qHash().

**Note:** The return type of this function is *not* the same as that of

```
qHash(qMakePair(key.first, key.second), seed);
```

The two functions use different hashing algorithms; due to binary compatibility constraints, we cannot change the [QPair](../../P/QPair/QPair.md) algorithm to match the std::pair one before Qt 6.

This function was introduced in Qt 5.7.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QVersionNumber](../../V/QVersionNumber/QVersionNumber.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.6.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([ulong](../../G/QtGlobal/QtGlobal.md#typedef-ulong) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(long *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([quint64](../../G/QtGlobal/QtGlobal.md#typedef-quint64) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash([qint64](../../G/QtGlobal/QtGlobal.md#typedef-qint64) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(float *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.3.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(double *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.3.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(long double *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.3.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QChar](../../C/QChar/QChar.md) *key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QByteArray](../../B/QByteArray/QByteArray.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QString](../../S/QString/QString.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHash(const [QStringRef](../../S/QStringRef/QStringRef.md) &*key*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the *key*, using *seed* to seed the calculation.

This function was introduced in Qt 5.0.

### [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashBits(const void **p*, size_t *len*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the memory block of size *len* pointed to by *p*, using *seed* to seed the calculation.

Use this function only to implement [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() for your own custom types. For example, here's how you could implement a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overload for std::vector<int>:

```
inline uint qHash(const std::vector<int> &key, uint seed = 0)
{
    if (key.empty())
        return seed;
    else
        return qHashBits(&key.front(), key.size() * sizeof(int), seed);
}
```

This takes advantage of the fact that std::vector lays out its data contiguously. If that is not the case, or the contained type has padding, you should use [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)() instead.

It bears repeating that the implementation of qHashBits() - like the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overloads offered by Qt - may change at any time. You **must not** rely on the fact that qHashBits() will give the same results (for the same inputs) across different Qt versions.

This function was introduced in Qt 5.4.

**另请参阅** [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)() and [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)().

### template <typename InputIterator> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashRange(InputIterator *first*, InputIterator *last*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the range [*first*,*last*), using *seed* to seed the calculation, by successively applying [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() to each element and combining the hash values into a single one.

The return value of this function depends on the order of elements in the range. That means that

```
{0, 1, 2}
```

and

```
{1, 2, 0}
```

hash to **different** values. If order does not matter, for example for hash tables, use [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)() instead. If you are hashing raw memory, use [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)().

Use this function only to implement [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() for your own custom types. For example, here's how you could implement a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overload for std::vector<int>:

```
inline uint qHash(const std::vector<int> &key, uint seed = 0)
{
    return qHashRange(key.begin(), key.end(), seed);
}
```

It bears repeating that the implementation of qHashRange() - like the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overloads offered by Qt - may change at any time. You **must not** rely on the fact that qHashRange() will give the same results (for the same inputs) across different Qt versions, even if [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() for the element type would.

This function was introduced in Qt 5.5.

**另请参阅** [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)() and [qHashRangeCommutative](QHash.md#template-typename-inputiterator-uint-qhashrangecommutativeinputiterator-first-inputiterator-last-uint-seed--0)().

### template <typename InputIterator> [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) qHashRangeCommutative(InputIterator *first*, InputIterator *last*, [uint](../../G/QtGlobal/QtGlobal.md#typedef-uint) *seed* = 0)

Returns the hash value for the range [*first*,*last*), using *seed* to seed the calculation, by successively applying [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() to each element and combining the hash values into a single one.

The return value of this function does not depend on the order of elements in the range. That means that

```
{0, 1, 2}
```

and

```
{1, 2, 0}
```

hash to the **same** values. If order matters, for example, for vectors and arrays, use [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)() instead. If you are hashing raw memory, use [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)().

Use this function only to implement [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() for your own custom types. For example, here's how you could implement a [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overload for std::unordered_set<int>:

```
inline uint qHash(const std::unordered_set<int> &key, uint seed = 0)
{
    return qHashRangeCommutative(key.begin(), key.end(), seed);
}
```

It bears repeating that the implementation of qHashRangeCommutative() - like the [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() overloads offered by Qt - may change at any time. You **must not** rely on the fact that qHashRangeCommutative() will give the same results (for the same inputs) across different Qt versions, even if [qHash](QHash.md#uint-qhashconst-qurl-url-uint-seed--0)() for the element type would.

This function was introduced in Qt 5.5.

**另请参阅** [qHashBits](QHash.md#uint-qhashbitsconst-void-p-size_t-len-uint-seed--0)() and [qHashRange](QHash.md#template-typename-inputiterator-uint-qhashrangeinputiterator-first-inputiterator-last-uint-seed--0)().

### void qSetGlobalQHashSeed(int *newSeed*)

Sets the global [QHash](QHash.md#qhash-哈希函数) seed to *newSeed*.

Manually setting the global [QHash](QHash.md#qhash-哈希函数) seed value should be done only for testing and debugging purposes, when deterministic and reproducible behavior on a [QHash](QHash.md#qhash-哈希函数) is needed. We discourage to do it in production code as it can make your application susceptible to [algorithmic complexity attacks](QHash.md#算法复杂度攻击).

From Qt 5.10 and onwards, the only allowed values are 0 and -1. Passing the value -1 will reinitialize the global [QHash](QHash.md#qhash-哈希函数) seed to a random value, while the value of 0 is used to request a stable algorithm for C++ primitive types types (like `int`) and string types ([QString](../../S/QString/QString.md), [QByteArray](../../B/QByteArray/QByteArray.md)).

The seed is set in any newly created [QHash](QHash.md#qhash-哈希函数). See [qHash](QHash.md#qhash-哈希函数) about how this seed is being used by [QHash](QHash.md#qhash-哈希函数).

If the environment variable `QT_HASH_SEED` is set, calling this function will result in a no-op.

This function was introduced in Qt 5.6.

**另请参阅** [qGlobalQHashSeed](QHash.md#int-qglobalqhashseed).

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator<<([QDataStream](../../D/QDataStream/QDataStream.md) &*out*, const [QHash](QHash.md#qhashqhash)<Key, T> &*hash*)

Writes the hash *hash* to stream *out*.

This function requires the key and value types to implement `operator<<()`.

**另请参阅** [Serializing Qt Data Types](../../D/QDataStream/datastreamformat.md).

### template <typename Key, typename T> [QDataStream](../../D/QDataStream/QDataStream.md) &operator>>([QDataStream](../../D/QDataStream/QDataStream.md) &*in*, [QHash](QHash.md#qhashqhash)<Key, T> &*hash*)

Reads a hash from stream *in* into *hash*.

This function requires the key and value types to implement `operator>>()`.

**另请参阅** [Serializing Qt Data Types](../../D/QDataStream/datastreamformat.md).