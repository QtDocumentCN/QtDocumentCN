# API 设计规范

> 译者注：
>
> 本文不来自于 Qt 文档，而是来自于 Qt Wiki：[API_Design_Principles](https://wiki.qt.io/API_Design_Principles)
>
> API(Application Programming Interface)，应用开发接口，本文中也将 P 解释为 Programmer（开发者）。

Qt 最出名的特点之一是一致性强、易于学习、功能强大的 API。本文尝试对我们在设计 Qt 风格的 API 中积累的诀窍进行总结。其中许多准则都是通用的，其它的则是习惯性用法，我们主要为了保持接口一致性而继续遵循。

尽管这些准则主要面向公共接口，但也鼓励您在设计内部接口时使用相同的技术，这对与您合作开发的同僚会更加友好。

您可能也会有兴趣查阅 Jasmin Blanchette 的 [Little Manual of API Design (PDF)](https://people.mpi-inf.mpg.de/~jblanche/api-design.pdf)，或它的前身，由 Matthias Ettrich 编写的 [*Designing Qt-Style C++ APIs*](https://doc.qt.io/archives/qq/qq13-apis.html)。



## 优秀接口的六大特点

API 是面向开发者的，而 GUI 则是面向终端用户。API 中的 P 代表开发者(Programmer)，而非程序(Program)，目的是指出 API 由开发者，即人类（而非计算机）所使用这一特点。

Matthias 在 Qt 季刊弟13期，关于 API 设计的文章中，声称他坚信 API 应该是最小化但完备的，具备清晰而简洁的语义，符合直觉，被开发者，易于记忆，能够引导开发者编写高可读性的代码。

----

#### 最小化

最小化的 API 指包含尽可能少的公共成员和最少的类。这可让 API 更易于理解、记忆、调试和修改。

----

#### 完备性

完备的 API 意味着具备所有应有的功能。这可能会与最小化产生冲突。此外，若一个成员函数位于错误的类中，则大多数潜在的用户回无法找到它。

----

#### 清晰简洁的语义

与其它设计协作时，应该让您的设计做到最小例外。通用化会让事情更简单。特例可能存在，但不应成为关注的焦点。在处理特定问题时，不应让解决方案过度泛化。（例如，Qt 3 中的 `QMineSourceFactory` 本该被称作 `QImageLoader`，并且具备另一套 API。）

----

#### 复合直觉

如同计算机上其它内容，API 应复合直觉。不同的开发经验和技术背景会导致对复合直觉与否有不同的感知。复合直觉的 API 应能让中等经验的开发者无需阅读文档并直接使用，并让不知道这个 API 的开发者可以理解使用它编写的代码。

----

#### 易于记忆

为了让 API 易于记忆，请选择一组保持一致并足够精确的命名约定。使用可理解的模式和概念，并且避免缩写。

----

#### 可读性导向

编写代码只需要一次，但阅读（以及调试和修改）则会非常频繁。高可读性的代码通常需要花更多时间编写，但可以在产品的生命周期中节约更多的时间。

最后需要谨记，不同类型的用户会使用 API 的不同部分。在单纯地创建一个 Qt 类实例能非常直观的同时，希望用户在尝试继承它之前先阅读文档则是很合理的。



## 静态多态

相似的代码类应具有相似的 API。可以使用继承来实现——当运行时多态支持时，这是很合理的。但多态同时也可以体现在设计截断。例如，若将代码中的 `QProgressBar` 换为 `QSlider`，或将 `QString` 换为 `QByteArray`，他们间相似的 API 会另替换操作变得非常容易。这便是为何我们称之为“静态多态”。

静态多态同样可让记忆 API 和开发模式变得更加简单。结果是，对于一组有关联的类，相似的 API 通常比为每个类独立设计的完美 API 更加好用。

在 Qt 中，当不具备有足够说服力的原因时，我们更倾向于使用静态多态，而非继承。这减少了 Qt 的公共类数量，并让新用户更容易在文档中找到需要的内容。

----

### 好的

​    `QDialogBox` 和 `QMessageBox` 具有相似的 APi，以用于处理按钮（`addButton()`, `setStandardButtons()`，但无需继承自某些 "QAbstractButtonBox" 类。

----

### 坏的

​    `QAbstractSocket` 被 `QTcpSOcket` 和 `QUdpSocket` 所继承，但这两个类的交互方式差异很大。看起来并没有人使用过（或能够使用） `QAbstractSocket` 指针来进行通用且有效的操作。

----

### 存疑

​    `QBoxLayout` 是 `QHBoxLayout` 和 `QVBoxLayout` 的基类。优点：可以在工具栏中使用 `QBoxLayout`，调用 `setOrientation()` 来令其水平/垂直排布。缺点：引入额外的类，用户可能会写出形如 `((QBoxLayout *)hbox)->setOrientation(Qt::Vertical)` 的代码，而这是不合理的。



## 基于属性的 API

比较新的 Qt 类倾向于使用基于属性的 API，例如：

```c++
QTimer timer;
timer.setInterval(1000);
timer.setSingleShot(true);
timer.start(); 
```

此处的*属性*，指的是作为对象状态一部分的任何概念性的特征——无论是否是实际的 `Q_PROPERTY`。只要可行，用户都应该允许以任何顺序设置属性，也就是说，这些属性应该是正交的。例如，上文的代码也可以写为：

```c++
QTimer timer;
timer.setSingleShot(true);
timer.setInterval(1000);
timer.start();
```

为了方便，我们也可以这样写：

```c++
timer.start(1000);
```

类似的，对于 `QRegExp`，我们可以：

```c++
QRegExp regExp;
regExp.setCaseSensitive(Qt::CaseInsensitive);
regExp.setPattern(".");
regExp.setPatternSyntax(Qt::WildcardSyntax);
```

为了实现此类 API，内部的对象需要被惰性构造。例如在 `QRegExp` 的案例中，不应该在还不知道表达式使用何种语法之前，就在 `setPattern()` 中过早地编译 `.` 表达式。

属性通常是级联的，此时我们应该谨慎地处理。仔细考虑下当前样式提供的“默认图标大小”与 `QToolButton` 的 `iconSize` 属性：

```c++
toolButton->iconSize(); // 返回当前样式表的默认大小
toolButton->setStyle(otherStyle);
toolButton->iconSize(); // 返回 otherStyle 的默认大小
toolButton->setIconSize(QSize(52, 52));
toolButton->iconSize(); // 返回 (52, 52)
toolButton->setStyle(yetAnotherStyle);
toolButton->iconSize(); // 返回 (52, 52) 
```

注意，一旦 `iconSize` 被设置，它会被一直留存，此时修改当前样式不会影响它。这是 **好的**。有时，提供重置属性的渠道会很方便，这有两种实现方式：

- 传递一个特定值（如 `QSIze()`、`-1 `或 `Qt::Alignment(0)`）来指代“重置”；
- 提供显示的 `resetFoo()` 或 `unsetFoo()` 函数。

对于 `iconSize`，将 `QSize()`（即 `QSize(-1, -1)`）设为“重置”便足够了。

某些场景中，取值方法会返回值会与设置的内容不同。例如，若调用 `widget->setEnabled(true)`，可能通过 `widget->isEnabled()` 获得的依然是 `false`，因为父控件被禁用了。这并没问题，因为通常这正是我们要检查的状态（父控件被禁用时，子控件也应该变灰，表现为也被禁用，但同时在它内部，应该知道自己实际是“可用”的，并等待父控件可用后恢复状态），但必须在文档中正确地进行描述。

----

## QProperty

> 译者注：该类型为 Qt 6.0 引入，需要参见 Qt 6 类文档。
>
> 本文原文中的内容与现有的 Qt 6.0 预览版存在出入，因此暂不翻译本节，待官方进一步维护更新原文。



## C++ 特性

### 值 与 对象

> 译者注：此条原文无内容，待官方更新

----

### 指针 与 引用

作为输出参数，指针与引用哪个更好？

```c++
void getHsv(int *h, int *s, int *v) const void getHsv(int &h, int &s, int &v) const
```

绝大多数 C++ 数据都推荐尽可能使用引用，因为引用在感知上比指针“更安全更漂亮”。事实上，我们在 Qt 软件中更倾向于使用指针，因为这会令代码更加已读。如对比：

```c++
color.getHsv(&h, &s, &v);
color.getHsv(h, s, v);
```

第一行代码能很清晰地表示，`h`、`s`、`v` 对象有很大概率会被该函数调用所修改。

即便如此，由于编译器并不喜欢输出参数，在新 APi 中应该避免此用法，而是返回一个小结构体：

```c++
struct Hsv { int hue, saturation, value }; Hsv getHsv() const;
```

> 译者注：对于可能失败的带返回值的函数，Qt 倾向于返回数值，使用 `bool* ok = 0` 参数来存储调用结果，以便在不关心时忽略之。同样在 Qt 6 以后，该方式不再被建议使用，而是改用 `std::optional<T>` 返回类型。

----

### 传递常引用 与 传递值

若类型大于16字节，传递常引用。

若类型具有[非平凡的拷贝构造函数](https://zh.cppreference.com/w/cpp/language/copy_constructor#.E5.B9.B3.E5.87.A1.E5.A4.8D.E5.88.B6.E6.9E.84.E9.80.A0.E5.87.BD.E6.95.B0)或[非平凡的析构函数](https://zh.cppreference.com/w/cpp/language/destructor#.E5.B9.B3.E5.87.A1.E6.9E.90.E6.9E.84.E5.87.BD.E6.95.B0)，传递常引用来避免执行这些方法。

所有其它类型都应使用值传递。

范例：

```c++
void setAge(int age);
void setCategory(QChar cat);
void setName(QLatin1String name);
void setAlarm(const QSharedPointer<Alarm> &alarm); // 常引用远快于拷贝构造和析构
// QDate, QTime, QPoint, QPointF, QSize, QSizeF, QRect 都是其它应该值传递的好例子
```

----

### 虚函数

当 C++ 中的一个成员函数被声明为虚函数，这主要用于通过在子类中重写来自定义该函数的行为。将函数设为虚函数的目的是让对该函数的现有调用会被替代为访问自定义的代码分支。若在该类之外没人调用此函数，则在将其声明为虚函数之前需要小心斟酌：

```c++
 // Qt 3 中的 QTextEdit: 成员函数不需要作为虚函数的成员函数
virtual void resetFormat();
virtual void setUndoDepth( int d );
virtual void setFormat( QTextFormat &f, int flags );
virtual void ensureCursorVisible();
virtual void placeCursor( const QPoint &pos;, QTextCursorc = 0 );
virtual void moveCursor( CursorAction action, bool select );
virtual void doKeyboardAction( KeyboardAction action );
virtual void removeSelectedText( int selNum = 0 );
virtual void removeSelection( int selNum = 0 );
virtual void setCurrentFont( const QFont &f );
virtual void setOverwriteMode( bool b ) { overWrite = b; }
```

当 `QTextEdit` 从 Qt 3 迁移至 Qt 4 时，几乎所有虚函数都被移除。有趣的是（但并未预料到），并没有大量的抱怨。为什么？因为 Qt 3 并未使用 `QTextEdit` 的多态性，Qt 3 并不会调用这些函数——只有使用者会。简单来说，否则并没有任何理由去继承 `QTextEdit` 并重写这些方法——除非您自己会通过多态去调用它们。若您需要在您的应用程序，也就是 Qt 之外使用多态机制，您应该自行添加。

#### 避免使用虚函数

在 Qt 中，我们因为多种原因而尝试最小化虚函数的数量。每个虚函数调用都会让缺陷修复变得更难，因为会在调用图中插入一个不受控制的节点（使得调用结果无法预测）。人们会在虚函数中做非常疯狂的举措，例如：

- 发送事件
- 发送信号
- 重入事件循环（例如，打开一个模态文件对话框）
- 删除对象（例如，某些导致 `delete this` 的操作）

此外还有一些避免过度使用虚函数的原因：

- 无法在不破坏二进制兼容性的前提下增加、移动或删除虚函数
- 无法简便地重写虚函数
- 编译器通常几乎不会内敛虚函数调用
- 调用虚函数需要查询虚表，导致其比常规函数调用慢2-3倍
- 虚函数另类对象更难进行值拷贝（可能做到，但会表现得很混乱且不被推荐）

过去的经验告诉我们，没有虚函数地类会产生更少的错误，通常也导致更少的维护。

一个通用的经验法则是，除非从工具集或该类的主要使用者角度需要调用它，否则一个函数不应该是虚函数。

#### 虚对象 与 可复制性

多态对象和值类型的类并不是好朋友。

包含虚函数的类会有虚析构函数来避免基类析构时未清理子类数据导致的内存泄漏。

若需要以值语义拷贝、复制和对比一个类，则可能需要拷贝构造函数、赋值运算符重载和等于运算符重载：

```c++
class CopyClass {
  public:
    CopyClass();
    CopyClass(const CopyClass &other);
    ~CopyClass();
    CopyClass &operator=(const CopyClass &other);
    bool operator== (const CopyClass &other) const;
    bool operator!=(const CopyClass &other) const;
    virtual void setValue(int v);
};
```

若创建该类的子类，则代码中会开始发生意料外的行为。通常来说，若没有虚函数和虚构造函数，则人们无法创建依赖于多态特性的子类。因此一旦虚函数或虚析构函数被添加，这会马上成为建立子类的理由，事情从此变得复杂。*乍一看来，很容易觉得可以简单定义一下虚运算符重载*。但顺着这条路深入下去，会导致混乱和毁灭（例如无可读性的代码）。请研究下这段代码：

```c++
class OtherClass {
  public:
    const CopyClass &instance() const; // 此处会返回什么？我应该将返回值赋值给谁？
};
```

（此小节正在施工中）

----

### 不变性

C++ 提供了 `const` 关键字来标识不会改变或不会产生副作用的事物。它可被用于数值、指针和倍只想的内容，也可被作为成员函数的特殊属性来标识它不会修改对象的状态。

注意，`const` 自身并不提供太大的价值——许多语言甚至并未提供 `const` 关键字，但这并不会自动导致它们存在缺陷。事实上，若移除所有函数重载，并通过搜索替换移除 C++ 代码中的所有 `const` 标识，代码很可能依然能够编译并正确执行。使用实用主义导向来使用 `const` 是很重要的。

让我们看看 Qt 中使用 `const` 的 API 设计：

#### 输入参数：`const` 指针

使用指针输入参数的 `const` 成员函数几乎总是使用 `const` 指针。

若一个成员函数确实被声明为 `const`，这意味着它不具有副作用，也不会修改对象对外可见的状态。那么，为什么要需要非 `const` 的输入参数？需要牢记，`const` 成员函数经常会被其它 `const` 成员函数，在这些调用场合中，非 `const` 的指针并不容易得到（除非使用 `const_cast`，而我们应该尽可能避免使用它）。

修改之前：

```c++
bool QWidget::isVisibleTo(QWidget *ancestor) const;
bool QWidget::isEnabledTo(QWidget *ancestor) const;
QPoint QWidget::mapFrom(QWidget *ancestor, const QPoint &pos) const;
```

`QWidget` 声明了大量使用非 `const` 指针作为输入参数的 `const` 成员函数。注意，虽然这些函数不能修改调用的控件本身，但是可以修改传入的控件。这类成员函数经常会伴随 `const_cast` 所使用。此类成员函数使用 `const` 输入参数会更合适。

修改之后：

```c++
bool QWidget::isVisibleTo(const QWidget *ancestor) const;
bool QWidget::isEnabledTo(const QWidget *ancestor) const;
QPoint QWidget::mapFrom(const QWidget *ancestor, const QPoint &pos) const;
```

注意，我们在 `QGraphicsItem` 中修复了这些成员函数，但 `QWidget` 的修复需要等待 Qt 5：

```c++
bool isVisibleTo(const QGraphicsItem *parent) const;
QPointF mapFromItem (const QGraphicsItem *item, const QPointF &point) const; 
```

#### 返回值：`const` 值

函数的返回值，要么是引用类型，要么是[右值](https://zh.cppreference.com/w/cpp/language/value_category#.E5.8F.B3.E5.80.BC)。

非类类型的右值是不受[cv限定符](https://zh.cppreference.com/w/cpp/language/cv)影响的。因此，即使在语法上允许为其添加 `const` 修饰，这并不会产生效果，因为由于其访问权不允许对其做出修改。大多数现代编译器在编译此类代码时会打印警告信息。

当为类类型的右值添加 `const` 时，对该类的非 `const` 的成员函数的访问会被禁止，对其成员变量的直接操作也会被禁止。

不添加 `const` 允许此类操作，但很少有此类需求，因为这些修改会伴随右值对象生命周期的结束而消失，这会在当前语句的分号结束后发生。

例如：

```c++
struct Foo {
    void setValue(int v) { value = v; } int value;
};

Foo foo() { return Foo(); }
const Foo cfoo() { return Foo(); }
int main() {
    // 下述代码可以编译，foo() 返回非 const 右值，无法
    // 成为赋值目标（这通常需要左值），但对成员变量的访问
    // 是左值：
    foo().value = 1; // 可以编译，但该临时值在这个完整的表达式结束后会被抛弃
    
    // 下述代码可以编译，foo() 返回非 const 右值，无法
    // 成为赋值目标，但可以调用（甚至于非 const 的)成员函数：
    foo().setValue(1); // 可以编译，但该临时值在这个完整的表达式结束后会被抛弃
    
    // 下述代码无法编译，cfoo() 返回 const 右值，因此其
    // 成员变量是 const 授权，无法被赋值：
    cfoo().value = 1; // 无法编译
    
    // 下述代码无法编译，cfoo() 返回 const 右值，无法调用
    // 其非 const 的成员函数：
    cfoo().setValue(1); // 无法编译
}
```

#### 返回值：指针与 `const` 指针

`const` 成员函数应该返回指针还是 `const` 指针这个问题，令许多人发现 C++ 的“const 正确性”被瓦解了。该问题源于某些 `const` 成员函数，并不修改它们的内部状态，而是返回成员变量的非 `const` 指针。单纯返回一个指针并不会影响对象对外可见的状态，也不会修改它正在维护的状态。但这会令程序员获得间接地修改对象数据的权限。

下述范例展示了通过 `const` 成员函数返回的非 `const` 指针来规避不可变性的诸多方法之一：

```c++
QVariant CustomWidget::inputMethodQuery(Qt::InputMethodQuery query) const {
    moveBy(10, 10); // 无法编译！
    window()->childAt(mapTo(window(), rect().center()))->moveBy(10, 10); // 可以编译！
}
```

返回 `const` 指针的函数，至少在一定程度上，避免了此类（可能并不希望/非预期的）副作用。但哪些函数会考虑返回 `const` 指针，或一组 `const` 指针？若我们使用 const正确 的方案，即令任何 `const` 成员函数返回成员变量（或一组成员变量的指针）时都是用 `const` 指针形式。很不幸的是，实际中这会造就无法使用的 API：

```c++
QGraphicsScene scene;
// … 初始化场景
foreach (const QGraphicsItem *item, scene.items()) {
    item->setPos(qrand() % 500, qrand() % 500); // 无法编译！item 是 const 指针
}
```

`QGraphicsScene::items()` 是 `const` 成员函数，这可能会让人觉得应该返回 `const` 指针。

在 Qt 中，我们近乎只使用非 `const` 的模式。我们选择了实用主义之路：返回 `const` 指针更容易导致 `const_cast` 的过度使用，这比滥用返回的非 `const` 指针引发的问题更加频繁。

#### 返回类型：值 或 `const` 引用？

如果我们在返回对象时还保留了它的副本，返回 `const` 引用是最快的方法；然而，这在我们之后打算重构这个类时成为了限制（使用 d 指针惯用法，我们可以在任何时候修改 Qt 类的内存结构；但我们无法在不破坏二进制兼容性的前提下，将函数签名从 `const QFoo&` 改为 `QFoo`）。出于此原因，我们通常返回 `QFoo` 而非 `const QFoo&`，除了性能极端敏感，而重构并不是问题的少数场合（例如 `QList::at()`）。

#### `const` 与 对象的状态

`const`正确性 是 C 中的一场“圣战”（译者注：原文为 `vi-emacs discussion`），因为该原则在一些领域（如基于指针的函数）中是失效了。

但 `const` 成员函数的常规含义是值不会修改一个类对外可见的状态，状态在此处值“我自己的和我负责的”。这并不意味着 `const` 成员函数会改变它们自己的私有成员变量，但也不代表不能这么做。但通常来说，`const` 成员函数不会产生可见的副作用。例如：

```c++
QSize size = widget->sizeHint(); // const
widget->move(10, 10); // 非 const
```

代理对象负责处理对另一个对象的绘制工作，它的状态包含了它负责的内容，也就是包含它的绘制目标的状态。请求代理进行绘制是具有副作用的：这会改变正在被绘制的设备的外观（也意味着状态）。正因如此，令 `paint()` 成为 `const` 并不合理。任何视图控件或 `QIcon` 的 `paint()` 作为 `const` 都很不合理。没人会在 `const` 成员函数中去调用 `QIcon::paint()`，除非他们明确地像规避当前函数的 `const` 性质。而在这种场景中，显示的 `const_cast` 会是更好的选择：

```c++
// QAbstractItemDelegate::paint 是 const
void QAbstractItemDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const
// QGraphicsItem::paint 不是 const
void QGraphicsItem::paint(QPainter &painter, const QStyleOptionGraphicsItem &option, QWidget &widget = 0)
```

`const` 关键字不会为你**做任何事**，考虑将其移除，而非为一个成员函数提供 `const`/非 `const` 的重载版本。



## API Semantics and Documentation

What should you do when you pass -1 to a function? etc…

Warnings/fatals/etc

APIs need quality assurance. The first revision is never right;  you must test it. Make use cases by looking at code which uses this API  and verify that the code is readable.

Other tricks include having somebody else use the API with or  without documentation and documenting the class (both the class overview and the individual functions).

## The Art of Naming

Naming is probably the single most important issue when designing an API. What should the classes be called? What should the member functions be  called?

### General Naming Rules

A few rules apply equally well to all kinds of names. First, as I  mentioned earlier, do not abbreviate. Even obvious abbreviations such as "prev" for "previous" don't pay off in the long run, because the user  must remember which words are abbreviated.

Things naturally get worse if the API itself is inconsistent; for example, Qt 3 has activatePreviousWindow() and fetchPrev(). Sticking to the "no abbreviation" rule makes it simpler to create consistent APIs.

Another important but more subtle rule when designing classes is  that you should try to keep the namespace for subclasses clean. In Qt 3, this principle wasn't always followed. To illustrate this, we will take the example of a QToolButton. If you call name(), caption(), text(), or textLabel() on a QToolButton in Qt 3, what do you expect? Just try  playing around with a QToolButton in Qt Designer:

- The name property is inherited from QObject and refers to an internal object name that can be used for debugging and testing.
- The caption property is inherited from QWidget and refers to the  window title, which has virtually no meaning for QToolButtons, since  they usually are created with a parent.
- The text property is inherited from QButton and is normally used on the button, unless useTextLabel is true.
- The textLabel property is declared in QToolButton and is shown on the button if useTextLabel is true.

In the interest of readability, name is called objectName in Qt 4,  caption has become windowTitle, and there is no longer any textLabel  property distinct from text in QToolButton.

Documenting is also a good way of finding good names when you get stuck: just try to document the item (class, function, enum value,  etc.) and use your first sentence as inspiration. If you cannot find a  precise name, this is often a sign that the item shouldn't exist. If  everything else fails and you are convinced that the concept makes  sense, invent a new name. This is, after all, how "widget", "event",  "focus", and "buddy" came to be. 

### Naming Classes

Identify groups of classes instead of finding the perfect name for each  individual class. For example, All the Qt 4 model-aware item view  classes are suffixed with View (QListView, QTableView, and QTreeView),  and the corresponding item-based classes are suffixed with Widget  instead (QListWidget, QTableWidget, and QTreeWidget).

### Naming Enum Types and Values

The guiding principle is to avoid name clashes between enum values and to ensure readability code with reasonable verbosity.

#### Enums in Qt/global namespace

New enums in the Qt namespace should always use scoped/strong enumerators  by default. The scoping/strong typing ensures that there is no conflict  if the same enum value name is used multiple times:

```
 
```

`namespace Qt {  enum class Color {    Blue,    Orange,    Yellow  };  ``  enum class FavoriteColor {    Yellow,    Orange  }; } ``Color yellow = Qt::Color::Yellow; FavoriteColor yellow2 = Qt::FavoriteColor::Yellow; yellow2 = Qt::Orange; // error ```

``

When using scoped enums additional naming rules (repeating of enum type name inside enum value name) for are not necessary. 

#### Enums in classes

Enums inside a class do not have the same problem of names clashing, as they are already namespaced within the class. 

There are still reasons to prefer scoped enums inside classes, but this should be decided on a case by case basis.

If the enum values have a clear relation to the parent class, prefer un-scoped enums:

```
 
```

`class TouchPoint {  enum State {       Pressed,       Held,       Released  }; ``}; // The context is clear when used outside the class if (point.state() == TouchPoint::Pressed) ``  ... ``// As well as when used inside it if (state() == Pressed) ``  ... ```

``

Using scoped enums in this case would add redundant line noise:

```
 if (point.state() == TouchPoint::State::Pressed) 
```

`  ... ``if (state() == State::Pressed) ``  ... ```

``

Note that the context where the enum is used, such as the name of the getter that returns the enum value, might be enough information to  make a scoped enum redundant.

If the enum values do not have a natural relation to the class name, prefer scoped enums, e.g.:

```
 
```

`class QSslCertificate {  enum class PatternSyntax {       RegularExpression,       Wildcard,       FixedString  }; ``}; if (syntax == PatternSyntax::Wildcard) `` ... ```

`` Another option to avoid the name clash instead of scoped/strong enums is to embedded the enum type name into each enum value. This method was  extensively used in Qt 4 before scoped/strong enums were available.

```
 
```

`class Widget {      enum Corner {          TopLeftCorner,          BottomRightCorner,           …     }; };  ``tabWidget->setCornerWidget(widget, Widget::TopLeftCorner); ```

``

#### Enums in flags

When enumerator values can be OR'd together and be used as flags, the  traditional solution is to store the result of the OR in an int, which  isn't type-safe. Qt offers a template class QFlags<T>, where T is  the enum type. For convenience, Qt provides typedefs for the flag type  names, so you can type Qt::Alignment instead of  QFlags<Qt::AlignmentFlag>.

By convention, we give the enum type a singular name (since it  can only hold one flag at a time) and the "flags" type a plural name.  For example:

```
enum RectangleEdge { LeftEdge, RightEdge, … };
typedef QFlags<RectangleEdge> RectangleEdges; 
```

In some cases, the "flags" type has a singular name. In that case, the enum type is suffixed with Flag:

```
enum AlignmentFlag { AlignLeft, AlignTop, … };
typedef QFlags<AlignmentFlag> Alignment;
```

### Naming Functions and Parameters

The number one rule of function naming is that it should be clear from the  name whether the function has side-effects or not. In Qt 3, the const  function QString::simplifyWhiteSpace() violated this rule, since it  returned a QString instead of modifying the string on which it is  called, as the name suggests. In Qt 4, the function has been renamed  QString::simplified().

Parameter names are an important source of information to the  programmer, even though they don't show up in the code that uses the  API. Since modern IDEs show them while the programmer is writing code,  it's worthwhile to give decent names to parameters in the header files  and to use the same names in the documentation.

### Naming Boolean Getters, Setters, and Properties

Finding good names for the getter and setter of a bool property is always a  special pain. Should the getter be called checked() or isChecked()?  scrollBarsEnabled() or areScrollBarEnabled()?

In Qt 4, we used the following guidelines for naming the getter function:

- Adjectives are prefixed with 

  is-

  . Examples:

  - `isChecked()`
  - `isDown()`
  - `isEmpty()`
  - `isMovingEnabled()`

- However, adjectives applying to a plural noun have no prefix:

  - `scrollBarsEnabled(), not areScrollBarsEnabled()`

- Verbs have no prefix and don't use the third person (-s):

  - `acceptDrops(), not acceptsDrops()`
  - `allColumnsShowFocus()`

- Nouns generally have no prefix:

  - `autoCompletion(), not isAutoCompletion()`
  - `boundaryChecking()`

- Sometimes, having no prefix is misleading, in which case we prefix with 

  is-

  :

  - `isOpenGLAvailable(), not openGL()`
  - `isDialog(), not dialog()`



The name of the setter is derived from that of the getter by removing any is prefix and putting a set at the front of the name; for example,  setDown() and setScrollBarsEnabled(). The name of the property is the  same as the getter, but without the is prefix.

## Avoiding Common Traps

### The Convenience Trap

It is a common misconception that the less code you need to achieve  something, the better the API. Keep in mind that code is written more  than once but has to be understood over and over again. For example,

```
 
```

`QSlider *slider = new QSlider(12, 18, 3, 13, Qt::Vertical, 0, "volume"); ```

``

is much harder to read (and even to write) than

```
 
```

`QSlider *slider = new QSlider(Qt::Vertical); slider->setRange(12, 18); slider->setPageStep(3); slider->setValue(13); slider->setObjectName("volume"); ```

``

### The Boolean Parameter Trap

Boolean parameters often lead to unreadable code. In particular, it's almost  invariably a mistake to add a bool parameter to an existing function. In Qt, the traditional example is repaint(), which takes an optional bool  parameter specifying whether the background should be erased (the  default) or not. This leads to code such as

```
 
```

`widget->repaint(false); ```

``

which beginners might read as meaning, "Don't repaint!"

The thinking is apparently that the bool parameter saves one  function, thus helping reducing the bloat. In truth, it adds bloat; how  many Qt users know by heart what each of the next three lines does?

```
 
```

`widget->repaint(); widget->repaint(true); widget->repaint(false); ```

``

A somewhat better API might have been

```
 
```

`widget->repaint(); widget->repaintWithoutErasing(); ```

``

In Qt 4, we solved the problem by simply removing the possibility of repainting without erasing the widget. Qt 4's native support for  double buffering made this feature obsolete.

Here are a few more examples:

```
 
```

`widget->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Expanding, true); textEdit->insert("Where's Waldo?", true, true, false); QRegExp rx("moc_'***.c??", false, true);\*** ```

``

An obvious solution is to replace the bool parameters with enum  types. This is what we've done in Qt 4 with case sensitivity in QString. Compare:

```
 
```

`str.replace("USER", user, false); // Qt 3 str.replace("USER", user, Qt::CaseInsensitive); // Qt 4 ```

``

### The Copy Cat Trap

## Case Studies

### QProgressBar

To show some of these concepts in practice, we'll study the QProgressBar API of Qt 3 and compare it to the Qt 4 API. In Qt 3:

```
 
```

`class QProgressBar : public QWidget { … public: int totalSteps() const; int progress() const; ``const QString &progressString() const; bool percentageVisible() const; void setPercentageVisible(bool); ``void setCenterIndicator(bool on); bool centerIndicator() const; ``void setIndicatorFollowsStyle(bool); bool indicatorFollowsStyle() const; ``public slots: void reset(); virtual void setTotalSteps(int totalSteps); virtual void setProgress(int progress); void setProgress(int progress, int totalSteps); ``protected: virtual bool setIndicator(QString &progressStr, int progress, int totalSteps); … }; ```

``

The API is quite complex and inconsistent; for example, it's not  clear from the naming that reset(), setTotalSteps(), and setProgress()  are tightly related.

The key to improve the API is to notice that QProgressBar is  similar to Qt 4's QAbstractSpinBox class and its subclasses, QSpinBox,  QSlider and QDial. The solution? Replace progress and totalSteps with  minimum, maximum and value. Add a valueChanged() signal. Add a  setRange() convenience function.

The next observation is that progressString, percentage and  indicator really refer to one thing: the text that is shown on the  progress bar. Usually the text is a percentage, but it can be set to  anything using the setIndicator() function. Here's the new API:

```
 
```

`virtual QString text() const; void setTextVisible(bool visible); bool isTextVisible() const; ```

``

By default, the text is a percentage indicator. This can be changed by reimplementing text().

The setCenterIndicator() and setIndicatorFollowsStyle() functions in the Qt 3 API are two functions that influence alignment. They can  advantageously be replaced by one function, setAlignment():

```
 
```

`void setAlignment(Qt::Alignment alignment); ```

``

If the programmer doesn't call setAlignment(), the alignment is  chosen based on the style. For Motif-based styles, the text is shown  centered; for other styles, it is shown on the right hand side.

Here's the improved QProgressBar API:

```
 
```

`class QProgressBar : public QWidget { … public: void setMinimum(int minimum); int minimum() const; void setMaximum(int maximum); int maximum() const; void setRange(int minimum, int maximum); int value() const; ``virtual QString text() const; void setTextVisible(bool visible); bool isTextVisible() const; Qt::Alignment alignment() const; void setAlignment(Qt::Alignment alignment); ``public slots: void reset(); void setValue(int value); ``signals: void valueChanged(int value); … }; ```

``

### QAbstractPrintDialog & QAbstractPageSizeDialog

Qt 4.0 saw the apparition of two classes QAbstractPrintDialog and  QAbstractPageSizeDialog that served as base classes for QPrintDialog and QPageSizeDialog. This served no purpose at all, since none of Qt's APIs take a QAbstractPrint- or -PageSizeDialog pointer as an argument and  perform some operation on it. Using qdoc trickery, we've hidden them,  but they're the prototypical examples of needless abstract classes.

This is not to say *good* abstraction is wrong, and indeed  QPrintDialog probably should have a factory or some other mechanism for  changing it- as evidenced by the #ifdef QTOPIA_PRINTDIALOG in its  declaration.

### QAbstractItemModel

The details of the problems with model/view in Qt 4 are documented well  elsewhere, but an important generalization is that "QAbstractFoo" should not just be the union of all possible subclasses you can think of at  the time of writing. Such "union of all things" base classes are almost  never a good solution. QAbstractItemModel commits this error - it is  really just QTreeOfTablesModel, with the consequently complicated API  that causes… and which is then *inherited by all the nicer subclasses*,

Just adding abstraction does not make an API better automatically.

### QLayoutIterator & QGLayoutIterator

In Qt 3, creating a custom layout involved subclassing both QLayout and  QGLayoutIterator ("G" stands for generic). A QGLayoutIterator subclass  instance pointer was wrapped in a QLayoutIterator, which users could use like any other iterator class. QLayoutIterator made it possible to  write code like this:

```
 
```

`QLayoutIterator it = layout()->iterator(); QLayoutItem **child; while ((child = it.current()) != 0) {    if (child->widget() == myWidget) {        it.takeCurrent();        return;   }   ++it; ```

```
} 
```

In Qt 4, we killed QGLayoutIterator classes (and their internal  subclasses for box and grid layouts) and instead asked the QLayout  subclasses to reimplement itemAt(), takeAt(), and count().

### QImageSink

Qt 3 had a whole set of classes that allowed images to be incrementally  read and passed to an animation - the  QImageSource/Sink/QASyncIO/QASyncImageIO classes. Since all these were  ever used for was animated QLabels, it was total overkill.

The lesson is not to add abstraction to aide some very vague  future possibility. Keep it simple. When those future things come, it  will be a lot easier to factor them into a simple system than into a  complex one.

### other Qt3 vs. Qt4?

### QWidget::setWindowModified(bool)

### Q3Url vs. QUrl

### Q3TextEdit vs. QTextEdit

How all those virtual functions went a-goner…

### Qt's Clipping Story (naming of clipping fns)

When you set the clip rect, you actually set a region (should be setClipRegion(QRect) instead of setClipRect()).

(on the right, how it should have been…)