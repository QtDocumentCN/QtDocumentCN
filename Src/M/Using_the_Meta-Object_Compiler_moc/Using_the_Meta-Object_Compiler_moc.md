# 使用元对象编译器(moc)





元对象编译器 `moc` 是用于处理 [Qt 的 C++ 扩展](../The_Meta-Object_System/The_Meta-Object_System.md) 的程序。

`moc` 工具会阅读 C++ 头文件。若在类定义中发现了 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏，则会建立一个 C++ 源文件，在其中包含了这些类的元对象代码。除此之外，元对象代码也被用于信号槽机制、运行时类型信息和动态属性系统。

`moc` 生成的 C++ 源文件需要随对应类的实现一同参与编译和链接。

若使用 [qmake](../../Q/QMake-Manual/QMake-Manual.md) 来创建构建文件，则会自动生成按需调用 `moc` 的构建规则，因此无需显示调用 `moc`。若想了解更多 `moc` 的背景信息，详见 [为何 Qt 使用 Moc 实现信号槽？](https://doc.qt.io/qt-5/why-moc.html)



## 使用方式

`moc` 通常会输入一个包含类声明的文件，例如：

```cpp
class MyClass : public QObject
{
    Q_OBJECT

public:
    MyClass(QObject *parent = 0);
    ~MyClass();

signals:
    void mySignal();

public slots:
    void mySlot();
};
```

除了上文中的信号槽，`moc` 在下一个范例中也被用于实现对象的属性。[Q_PROPERTY](../../O/QObject/QObject.md#qproperty)() 宏定义了一条属性，[Q_ENUM](../../O/QObject/QObject.md#qenum)() 则定义了一组在类内部可被 [property system](https://doc.qt.io/qt-5/properties.html) 使用的枚举类型。

在下述范例中，我们声明了一个使用枚举类型 `Priority` 的属性，该属性同样被命名为 `priority`，具备一个读函数 `priority()` 和一个写函数 `setPriority()`。

```cpp
class MyClass : public QObject
{
    Q_OBJECT
    Q_PROPERTY(Priority priority READ priority WRITE setPriority)
    Q_ENUMS(Priority)

public:
    enum Priority { High, Low, VeryHigh, VeryLow };

    MyClass(QObject *parent = 0);
    ~MyClass();

    void setPriority(Priority priority) { m_priority = priority; }
    Priority priority() const { return m_priority; }

private:
    Priority m_priority;
};
```

`Q_FLAGS()` 宏用于声明被用为标志位的枚举，即可以被**或**操作合并的值。另一个宏 [Q_CLASSINFO](../../O/QObject/QObject.md#qclassinfoname-value)() 则允许您为类的元对象添加`名称/值 `配对的附加信息。

```cpp
class MyClass : public QObject
{
    Q_OBJECT
    Q_CLASSINFO("Author", "Oscar Peterson")
    Q_CLASSINFO("Status", "Active")

public:
    MyClass(QObject *parent = 0);
    ~MyClass();
};
```

`moc` 产生的输出必须被编译并链接，就如同程序中的其它 C++ 代码一样，否则构建过程会在最终的链接阶段失败。若使用 `qmake`，则这些操作会被自动完成。当 `qmake` 运行时，它会解析项目的所有头文件，为包含 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏的文件生成调用 `moc` 的构建规则。

若类定义在 `myclass.h` 文件中，则 `moc` 的输出会被保存在 `moc_myclass.cpp` 文件中。该文件会如常规源文件一般，被编译生成为对象文件，如 Windows 中的 `moc_myclass.obj` 。该对象文件应被包含在链接对象文件列表中，用于参与程序最终的链接阶段。



## 编写调用 `moc` 的 `make` 规则

除了最简单的测试程序外，其它情况下都建议自动执行 `moc`。通过向 `makefile` 中添加一组规则，`make` 会在必要时执行 `moc` 并处理其输出内容。

我们推荐使用 [qmake](../Q/../QMake-Manual/QMake-Manual.html) 生成工具来构建您的 `makefile`。此工具会生成一个 `makefile` 文件来处理所有 `moc` 操作。

若您打算自行创建 `makefile`，可以参阅下文的小贴士来添加 `moc` 操作。

对于头文件中类声明内的 [Q_OBJECT](../../O/QObject/QObject.md#qobject) ，下文是使用 `GNU make` 的 `makefile` 规则：

```cpp
moc_%.cpp: %.h
        moc $(DEFINES) $(INCPATH) $< -o $@
```

若想更加灵活，则可以通过如下格式编写独立的规则：

```cpp
moc_foo.cpp: foo.h
        moc $(DEFINES) $(INCPATH) $< -o $@
```

您还需谨记将 `moc_foo.cpp` 添加到 `SOURCES` 变量（或者其它您喜欢的名称）中，并将 `moc_foo.o` 或 `moc_foo.obj` 添加至 `OBJECTS` 变量。

上文的两个范例都假定 `$(DEFINES)` 和 `$(INCPATH)` 变量会被展开为传递至 C++ 编译器的宏定义和包含路径，这些被 `moc` 用于对源文件进行预处理。

虽然我们倾向于将 C++ 源文件命名为 `.cpp`，您仍可根据喜好使用其它扩展名，如 `.C`、`.cc`、`.CC`、`.cxx` 和 `.c++`。

对于在实现文件(`.cpp`)中的类声明内的 [Q_OBJECT](../../O/QObject/QObject.md#qobject) ，我们建议使用类似下文的 `makefile` 规则：

```cpp
foo.o: foo.moc

foo.moc: foo.cpp
        moc $(DEFINES) $(INCPATH) -i $< -o $@
```

这确保了 `moc` 会在 `foo.cpp` 编译前执行，于是可以将：

```cpp
#include "foo.moc"
```

添加到 `foo.cpp`文件末尾，即可以感知到该文件中所有类定义的位置。



## 命令行选项

下表为 `moc` 提供的命令行选项：

| 选项                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| `-o<file>`          | 将输出写入 `<file>`，而非标注输出流(`stdout`)。              |
| `-f[<file>]`        | 强令输出内容中包含一条 `#include` 语句。对于扩展名是 `.h` 或 `.H` 开头的头文件，此选项默认启用。此选项对于不遵循标准命名约定的头文件尤其有用。`<file>` 部分是可选的。 |
| `-i`                | 不生成 `#include` 语句至输出内容。此选项可被用于对包含一个或多个类声明的 `C++` 文件执行 `moc`。您需要在 `.cpp` 中通过 `#include` 包含输出的元对象代码。 |
| `-nw`               | 不生成任何警告（不建议开启）。                               |
| `-p<path>`          | 另生成的 `#include` 语句中附加上 `<path>/` 前缀。            |
| `-I<dir>`           | 为头文件添加包含路径。                                       |
| `-E`                | 仅执行预处理，不生成元对象代码。                             |
| `-D<macro>[=<def>]` | 添加宏定义，通过可选参数指定值。                             |
| `-U<macro>`         | 取消宏定义。                                                 |
| `-M<key=value>`     | 为插件附加额外的元信息。若某个类指定了 [Q_PLUGIN_METADATA](https://doc.qt.io/qt-5/qtplugin.html#Q_PLUGIN_METADATA)，则该键值对会被添加至元数据。这些数据会出现在插件运行时解析的 `json` 对象中（通过 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md)）。此参数通常被用于为静态插件添加编译系统提供的信息。 |
| `@<file>`           | 从 `<file>` 中读取额外的命令行选项。该文件的每一行文本都被当作一条独立的选项，空行会被忽略。注意，此选项不支持在参数文件内使用（即参数文件不能包含另一个参数文件）。 |
| `-h`                | 显示使用说明和选项列表。                                     |
| `-v`                | 显示 `moc` 的版本号。                                        |
| `-Fdir`             | 用于 macOS。将 `dir` 指定的框架路径添加到头文件搜索路径列表顶部。这些路径会和 `-I` 制定的路径一同排布，以自左向右的顺序检索（详见 `gcc` 的 manpage）。通常使用 `-F /Library/Frameworks/` |

您可以显示告知 `moc` 不要解析头文件中的某些部分。`moc` 会定义预编译宏 `Q_MOC_RUN`，因此用

```cpp
#ifndef Q_MOC_RUN
    ...
#endif
```

包裹的代码会被 `moc` 跳过。



## 诊断

`moc` 在 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 类声明中检测到某些危险的或非法的代码结构时，会发出警告。

若在程序编译的最终步骤中出现链接错误，内容为 `YourClass::className()` 未定义，或者 `YourClass` 缺少虚表(`vtable`)，则意味着某些步骤出现错误。通常来说，您可能忘记编译 `moc` 生成的 C++ 代码，或者忘记 `#include` 它们，或者编译了但忘记将输出的对象文件添加到链接指令。若您是使用 `qmake`，尝试重新执行它来更新 `makefile`，这通常会很有用。



## 限制

`moc` 无法处理所有的 C++ 代码。最大的问题是模板类不能使用 [Q_OBJECT](../../O/QObject/QObject.md#qobject) 宏，例如：

```cpp
class SomeTemplate<int> : public QFrame
{
    Q_OBJECT
    ...

signals:
    void mySignal(int);
};
```

此代码结构是非法的。我们认为这些场合下有其它替代手法，所以移除这些限制的优先级并不高。



### 多继承要求 QObject 处于首位

若使用多继承，`moc` 会假定第一个被继承的类是 [QObject](../../O/QObject/QObject.md) 的子类。同样的，必须确保只有第一个被继承的类是 [QObject](../../O/QObject/QObject.md)。

```cpp
// 正确
class SomeClass : public QObject, public OtherClass
{
    ...
};
```

[QObject](../../O/QObject/QObject.md) **不支持**虚继承。



### 函数指针不能为信号槽参数

对于绝大多数使用函数指针作为信号槽参数的场景，我们都认为使用继承是更好的手段。下文是非法语法的示例：

```cpp
class SomeClass : public QObject
{
    Q_OBJECT

public slots:
    void apply(void (*apply)(List *, void *), char *); // 错误
};
```

但可以通过如下方式绕过限制：

```cpp
typedef void (*ApplyFunction)(List *, void *);

class SomeClass : public QObject
{
    Q_OBJECT

public slots:
    void apply(ApplyFunction, char *);
};
```

有时使用继承和虚函数来代替函数指针，会是更好的选择。

> 译者注：
>
> `moc` 并未携带完整的编译器前端，因此在识别函数指针嵌套语法时可能存在障碍。
>
> 因此可以推测，`moc` 可能无法正确识别过于复杂的模板参数，此时建议使用 `typedef` 或 `using` 指定较为简洁的别名。



### 信号槽参数中的枚举类型和类型别名必须包含完整修饰

[QObject::connect](../../O/QObject/QObject.md#static-qmetaobjectconnection-qobjectconnectconst-qobject-sender-const-char-signal-const-qobject-receiver-const-char-method-qtconnectiontype-type--qtautoconnection)() 通过文本对比来检查参数签名是否匹配。因此，[Alignment](../../Q/Qt_Namespace/Qt_Namespace.md#AlignmentFlag-enum) and [Qt::Alignment](../../Q/Qt_Namespace/Qt_Namespace.md#AlignmentFlag-enum) 被当作两个不同的类型。为绕过此限制，请确保声明信号槽和建立连接时都时使用完整修饰的数据类型。例如：

```cpp
class MyClass : public QObject
{
    Q_OBJECT

    enum Error {
        ConnectionRefused,
        RemoteHostClosed,
        UnknownError
    };

signals:
    void stateChanged(MyClass::Error error);
};
```

> 译者注：
>
> 这是 Qt 4 风格的 `connect()` 的历史问题，该接口使用 `SIGNAL` 和 `SLOT` 宏来生成信号槽参数，这两个宏的返回值是字符串类型，Qt 只能在运行时通过字符串匹配进行校验，极易产生纰漏。
>
> 同理，`qRegisterMetaType<TypeName>("TypeName")` 的函数参数，也是用于校验信号槽，也需遵循相同规范。
>
> 但若使用 Qt 5 的基于函数指针的方式，则无需考虑本小节的限制，也无需为 `qRegisterMetaType<T>()` 手动指定字符串名称。
>
> 更多信息，详见 `QObject::connect()`



### 嵌套类不能拥有信号槽

下文是错误代码结构的示例：

```cpp
class A
{
public:
    class B
    {
        Q_OBJECT

    public slots:   // 错误
        void b();
    };
};
```



### 信号槽返回值不能为引用

信号槽可以具备返回值，但返回引用会被当作返回 `void`。



### 只有信号槽可以出现在类的 `signals` 和 `slots` 区域中

若将信号槽之外的其它代码结构放置类的在 `signals` 或 `slots` 区域中，`moc` 将会报错。

> 译者注：
>
> 推荐使用 `Q_SIGNALS` 和 `Q_SLOTS` 单独标注信号槽，这样可以更精细地排列类成员布局，使得信号槽与其它成员按照能够逻辑关系排布，而非被 `signals` 或 `slots` 区域强行隔离开。



**另请参阅：** [元对象系统](https://doc.qt.io/qt-5/metaobjects.html)、[信号槽](https://doc.qt.io/qt-5/exceptionsafety.html#signals-and-slots) 和 [Qt 的属性系统](https://doc.qt.io/qt-5/properties.html)。