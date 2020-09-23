# 元对象系统

Qt 的元对象系统提供了对象间通信的信号槽机制、运行时类型信息，以及动态属性系统。

元对象系统基于以下三者：

1. [QObject](../../O/QObject/QObject.md) 类，提供了便于利用元对象系统的基类；
2. [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏，放置于类声明的私有域，用于激活元对象系统特性，例如动态属性和信号槽；
3. [元对象编译器](../Using_the_Meta-Object_Compiler_moc/Using_the_Meta-Object_Compiler_moc.md) (`moc`)，为每个 [QObject](../../O/QObject/QObject.md) 的子类提供实现元对象特性的代码生成。

`moc` 工具读取 C++ 源文件，若在其中找到包含 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏的类声明，则会创建另一个 C++ 源文件，并在其中填充用于实现元对象得的代码。该生成的源文件需要通过 `#include`' 包含至对应类的源文件，或者更常见的是将其加入编译列表，并于对应类的实现一同链接。

除了为跨对象通信提供了 [信号槽机制](../../S/Signals_and_Slots/Signals_and_Slots.md) （引入此系统的主要原因）， 元对象系统还提供了下列额外特性：

- [QObject::metaObject](../../O/QObject/QObject.md#virtual-const-qmetaobject-qobjectmetaobject-const)() 返回该类对应的 [元对象](../../M/QMetaObject/QMetaObject.md)。
- [QMetaObject::className](../../M/QMetaObject/QMetaObject.md#const-char-qmetaobjectclassname-const)() 在运行时以字符串形式返回该类的类名，并且不需要依赖 C++ 编译器的运行时类型信息(RTTI)支持；
- [QObject::inherits](../../O/QObject/QObject.md#bool-qobjectinheritsconst-char-classname-const)() 函数返回该对象所属类型，是否派生自 [QObject](../../O/QObject/QObject.md) 继承树中的指定类型；
- [QObject::tr](../../O/QObject/QObject.md#static-qstring-qobjecttrconst-char-sourcetext-const-char-disambiguation--nullptr-int-n--1)() 和 [QObject::trUtf8](../../O/QObject/QObject.md)() 为 [国际化](../../I/Internationalization/Internationalization.md) 支持提供字符串翻译；
- [QObject::setProperty](../../O/QObject/QObject.md#bool-qobjectsetpropertyconst-char-name-const-qvariant-value)() 和 [QObject::property](../../O/QObject/QObject.md#qvariant-qobjectpropertyconst-char-name-const)() 用于通过属性名称，动态设置和读取属性值；
- [QMetaObject::newInstance](https://doc.qt.io/qt-5/qmetaobject.html#newInstance)() 构建指定类的新实例。

我们还可以对 [QObject](../../O/QObject/QObject.md) 进行 [qobject_cast](../../O/QObject/QObject.md#template-typename-t-t-qobjectcastqobject-object)() 操作，该函数与标准 C++ 的 `dynamic_cast()` 表现类似，但优点时不需要 RTTI 支持，并且可以跨越动态库边界运作。它会尝试将输入指针转换为尖括号中的指针类型，若类型正确则返回非空指针（在运行时作出判断），若对象类型不兼容则返回 `nullptr`。

例如，假设 `MyWidget` 继承自 [QWidget](../../W/QWidget/QWidget.md) 类，并声明了 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏：

```c++
    QObject *obj = new MyWidget;
```

`QObject *` 类型的变量 `obj` 实际指向一个 `MyWidget` 对象，于是我们可以进行如下转换：

```c++
    QWidget *widget = qobject_cast<QWidget *>(obj);
```

从 [QObject](../../O/QObject/QObject.md) 到 [QWidget](../../W/QWidget/QWidget.md) 的转换成功进行，因为该对象实际是 [QWidget](../../W/QWidget/QWidget.md) 的子类 `MyWidget`。由于我们知道 `obj` 是 `MyWidget` 类型，我们可以将其转换为 `MyWidget *`：

```c++
    MyWidget *myWidget = qobject_cast<MyWidget *>(obj);
```

转换至 `MyWidget` 的操作可以成功进行，因为 [qobject_cast](../../O/QObject/QObject.md#template-typename-t-t-qobjectcastqobject-object)() 并不会将 Qt 内置类型和自定义类型区别对待。（译者注：Qt 是在运行时通过读取元对象信息进行动态转换，开发者可通过 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏让自定义类型支持被 [qobject_cast](../../O/QObject/QObject.md#template-typename-t-t-qobjectcastqobject-object)() 进行转换）

```c++
    QLabel *label = qobject_cast<QLabel *>(obj);
    // label is 0
```

另一个例子，转换为 [QLabel](../../L/QLabel/QLabel.md) 的操作失败了，该指针会被置零。但此机制也让运行时基于转换结果来区别处理不同类型成为可能：

```c++
    if (QLabel *label = qobject_cast<QLabel *>(obj)) {
        label->setText(tr("Ping"));
    } else if (QPushButton *button = qobject_cast<QPushButton *>(obj)) {
        button->setText(tr("Pong!"));
    }
```

虽然可以使用 [QObject](../../O/QObject/QObject.md) 作为基类，但不定义 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏，也不生成元对象代码，但这也意味着信号槽以及本文提到所有的其它机制无法使用。从元对象系统的视角来看，没有元对象代码的 [QObject](../../O/QObject/QObject.md) 的子类（译者注：即未使用 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏）等价于它最近的一个包含元对象代码的父类，这也意味着，例如，[QMetaObject::className](https://doc.qt.io/qt-5/qmetaobject.html#className)() 不会返回该类的类名，而是会返回父类的类名。

因此，我们强烈建议在所有 [QObject](../../O/QObject/QObject.md) 的子类中都使用 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏，无论它们是否用到了信号槽和动态属性。

**另请参阅：**[QMetaObject](../../M/QMetaObject/QMetaObject.md)，[Qt 的属性系统](../../P/The_Property_System/The_Property_System.md) 以及 [信号与槽](../../S/Signals_and_Slots/Signals_and_Slots.md)。