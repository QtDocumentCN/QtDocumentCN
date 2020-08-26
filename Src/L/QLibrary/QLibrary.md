# QLibrary Class

Qlibrary用于运行时加载库。

| 属性 | 内容 |
| ------- | ---------------------------------------------- |
| 头文件: | `#include <QLibrary>`                            |
| qmake:  | QT += core                                     |
| 继承于: | [QObject](../../S/QObject/QQbject.md) |

**注意：** 此类中全部函数可重入。



## 公共成员类型
|  类型  | 名称 |
| ----- | ------------------------------------------------------------ |
| enum  | **[LoadHint](#enum-qlibraryloadhint-flags-qlibraryloadhints)** { ResolveAllSymbolsHint, ExportExternalSymbolsHint, LoadArchiveMemberHint, PreventUnloadHint, DeepBindHint } |
| flags | **[LoadHints](#enum-qlibraryloadhint-flags-qlibraryloadhints)** |



## 属性

- **[fileName](#filename--qstring)** : QString
- **[loadHints](#loadhints--loadhints)** : LoadHints



## 公共成员函数

| 类型 | 函数名 |
| ---- | ------ |
|                     | **[QLibrary](#qlibraryqlibraryconst-qstring-filename-const-qstring-version-qobject-parent--nullptr)**(const QString &*fileName*, const QString &*version*, QObject **parent* = nullptr) |
|                     | **[QLibrary](#qlibraryqlibraryconst-qstring-filename-int-vernum-qobject-parent--nullptr)**(const QString &*fileName*, int *verNum*, QObject **parent* = nullptr) |
|                     | **[QLibrary](#qlibraryqlibraryconst-qstring-filename-qobject-parent--nullptr)**(const QString &*fileName*, QObject **parent* = nullptr) |
|                     | **[QLibrary](#qlibraryqlibraryqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual             | **[~QLibrary](#virtualqlibraryqlibrary)**() |
| QString             | **[errorString](#qstring-qlibraryerrorstring-const)**() const |
| QString             | **[fileName](#filename--qstring)**() const |
| bool                | **[isLoaded](#bool-qlibraryisloaded-const)**() const |
| bool                | **[load](#bool-qlibraryload)**()      |
| QLibrary::LoadHints | **[loadHints](#loadhints--loadhints)**() const |
| QFunctionPointer    | **[resolve](-> #qfunctionpointer-qlibraryresolveconst-char-symbol)**(const char **symbol*) |
| void                | **[setFileName](#filename--qstring)**(const QString &*fileName*) |
| void                | **[setFileNameAndVersion](#void-qlibrarysetfilenameandversionconst-qstring-filename-int-versionnumber)**(const QString &*fileName*, int *versionNumber*) |
| void                | **[setFileNameAndVersion](#void-qlibrarysetfilenameandversionconst-qstring-filename-const-qstring-version)**(const QString &*fileName*, const QString &*version*) |
| void                | **[setLoadHints](#loadhints--loadhints)**(QLibrary::LoadHints *hints*) |
| bool                | **[unload](#bool-qlibraryunload)**()  |



## 静态公共成员

|  类型  | 函数名|
|---|---|
| bool             | **[isLibrary](#isLibrary)**(const QString &*fileName*) |
| QFunctionPointer | **[resolve](#staticqfunctionpointer-qlibraryresolveconst-qstring-filename-const-char-symbol)**(const QString &*fileName*, const char **symbol*) |
| QFunctionPointer | **[resolve](#staticqfunctionpointer-qlibraryresolveconst-qstring-filename-int-vernum-const-charsymbol)**(const QString &*fileName*, int *verNum*, const char **symbol*) |
| QFunctionPointer | **[resolve](#staticqfunctionpointer-qlibraryresolveconst-qstring-filename-const-qstring-version-const-char-symbol)**(const QString &*fileName*, const QString &*version*, const char **symbol*) |



## 详细描述

QLibrary的实例用于操作一个动态链接库文件（文中称为库，也就是DLL）。QLibrary提供访问库中函数的一种平台无关方式。您可以在构造时传递库文件名，也可以通过 [setFileName](#filename--qstring)() 给对象显式设置。加载库时，QLibrary在所有系统指定的位置搜索 (例如： Unix上的 `LD_LIBRARY_PATH`), 除非文件名是绝对路径。

如果文件路径是绝对路径，则会首先尝试在这个位置加载。如果找不到，QLibrary尝试不同系统相关的前后缀的文件名，比如Unix系的前缀“lib”，后缀“.so”，Mac及IOS的后缀".dylib"，Windows的后缀".dll"。

如果文件路径不是绝对路径，Qlibrary改变搜索顺序，首先尝试系统特定的前后缀，之后是特定文件路径。

这让使用除去前后缀的库基本名称来指定库文件变得可能。因此代码可以在不同操作系统里执行，但不用太多代码尝试各种文件名称。

最重要的函数是 [load](#bool-qlibraryload)() 用于动态加载库，[isLoaded](#bool-qlibraryisloaded-const)() 用于检查是否加载成功，以及 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 来解析库中的符号。如果库还没加载，[resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 函数隐式地加载这个库。多个QLibrary实例访问同一个物理库文件是可行的。一旦被加载，库在内存中一直保留到程序结束。您可以通过 [unload](#bool-qlibraryunload)() 尝试卸载一个库，但如果有其他QLibrary实例在使用同一个库文件，调用会失败。只有在每一个实例都调用过 [unload](#bool-qlibraryunload)() 后，库才会真正卸载。

Qlibrary 的一种典型用法是解析库中的导出符号，并调用其对应的C语言函数。这叫做显式链接，对应于隐式链接。隐式链接是构建中的链接可执行文件和静态库的步骤。

下面的代码片段加载了个库，解析"mysymbol"符号，并在一切就绪的情况下调用这个函数。如果出现了问题， 例如库文件不存在或者符号未定义，函数指针将会是`nullptr`，且不会调用。

```
QLibrary myLib("mylib");
typedef void (*MyPrototype)();
MyPrototype myFunction = (MyPrototype) myLib.resolve("mysymbol");
if (myFunction)
    myFunction();
```



符号必须作为C函数导出，[resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)()才能工作。这意味着用C++编译器编译的函数必须由`extern "C"`块包裹。在Windows上，还要求导出函数要使用`dllexport`宏；实现详情见 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)()。方便起见，[resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 函数有静态形式，您可以在不现实加载库的情况下使用：

```
typedef void (*MyPrototype)();
MyPrototype myFunction =
        (MyPrototype) QLibrary::resolve("mylib", "mysymbol");
if (myFunction)
    myFunction();
```

**另请参阅：** [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html).



## 成员类型介绍

### enum QLibrary::LoadHint flags QLibrary::LoadHints

这个枚举描述了可能的可以用来改变库的加载行为的指示。这些取值指示在库加载后如何解析符号，通过 [setLoadHints](#loadhints--loadhints)() 指定。

| 常量                                  | 值     | 描述                                                         |
| ------------------------------------- | ------ | ------------------------------------------------------------ |
| `QLibrary::ResolveAllSymbolsHint`     | `0x01` | 在加载库的时候解析符号，而不是简单等到 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 调用。 |
| `QLibrary::ExportExternalSymbolsHint` | `0x02` | 导出库中未解析的符号和外部符号，这些符号可以在后续动态加载的库中解析。 |
| `QLibrary::LoadArchiveMemberHint`     | `0x04` | 运行库的文件名指定压缩包中的特定对象。如果设置了这个指示，文件名包含一个路径，其指向归档文件，接着是其中的成员名称。 |
| `QLibrary::PreventUnloadHint`         | `0x08` | 阻止库从地址空间通过close()卸载。如果之后再有open()调用，库中的静态变量不会重新初始化。 |
| `QLibrary::DeepBindHint`              | `0x10` | Instructs the linker to prefer definitions in the loaded library over exported definitions in the loading application when resolving external symbols in the loaded library. This option is only supported on Linux.<br />命令链接器在解析加载过的库中的外部符号时，优先使用加载了的库中的定义，而不是在应用程序加载中的定义。【译者注：翻译存疑，故保留原文参考，详情参考globc--dlopen()--RTLD_DEEPBIND】 |

LoadHints是一个 [QFlags](https://doc.qt.io/qt-5/qflags.html)`<LoadHint>` 类型的typedef。 它储存了LoadHint取值的**OR**（位或）方式的组合。

**另请参阅：** [loadHints](#loadhints--loadhints).



## 属性文档

### fileName : [QString](../../S/QString/QString.md)

这个属性容纳库的文件名。

我们建议忽略库的后缀名，因为Qlibrary会自动寻找带有合适后缀名的文件。 (参见 [isLibrary](#isLibrary)())

当加载库时，在所有系统指定的位置搜索 (例如： Unix上的 `LD_LIBRARY_PATH`)，除非文件名是绝对路径。加载成功后，fileName() 返回返回库文件的全名。如果在构造对象或setFileName() 中包含路径，讲返回文件的全路径。

例如在Unix平台成功加载"GL"库后，fileName() 会返回 "libGL.so"。如果传递参数的文件路径是 "/usr/lib/libGL", fileName() 会返回 "/usr/lib/libGL.so"。

**访问函数:**

|类型|函数名|
| ------- | ------------------------------------------ |
| QString | **fileName**() const                       |
| void    | **setFileName**(const QString &*fileName*) |

----

### loadHints : [LoadHints](#enum-qlibraryloadhint-flags-qlibraryloadhints)

给 [load](#bool-qlibraryload)() 函数一些关于如何执行的指示。

您可以对于符号如何解析做指示。通常来说，符号不是在加载库时解析的，而是惰性解析的（也就是调用 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 时）。如果您设置loadHints 为[ResolveAllSymbolsHint](#enum-qlibraryloadhint-flags-qlibraryloadhints)，那么如果平台支持，所有符号会在库加载时一齐解析。

设置 [ExportExternalSymbolsHint](#enum-qlibraryloadhint-flags-qlibraryloadhints) 会使库中的外部符号在后续库解析中可用。



如果设置了 [LoadArchiveMemberHint](#enum-qlibraryloadhint-flags-qlibraryloadhints) ，文件名会被分解为两部分：归档文件的路径和归档成员的名称. 例如,  [fileName](#filename--qstring) `libGL.a(shr_64.o)` 指向归档文件 `libGL.a`中的库文件 `shr_64.o` . 这个特性只在AIX平台生效。

loadHints 的解释是平台相关的，如果您用这些特效，您大概已经对编译的系统平台做了一些假设。因此请仅在您明白您这些操作的结果的情况下设置这些指示。

默认情况下，此属性没有设置任何flag，所有库文件会惰性加载，并且不会导出共其他动态链接库使用的外部符号。

**注意：** 在库已经加载后设置这个属性没有效果。 并且 loadHints() 不会体现出这些修改。

**注意：** 这个属性是所有指向同一个库的 [QLibrary](#QLibrary-Class) 实例共享的。

**访问函数：**

|类型|函数名|
| ------- | ------------------------------------------ |
| QLibrary::LoadHints | **loadHints**() const                         |
| void                | **setLoadHints**(QLibrary::LoadHints *hints*) |



## 成员函数文档

### QLibrary::QLibrary(const [QString](../../S/QString/QString.md) &*fileName*, const [QString](../../S/QString/QString.md) &*version*, [QObject](../../S/QObject/QQbject.md#QObject) **parent* = nullptr)

基于给定的父对象 *parent* 构造一个库对象。它会加载文件名*fileName*、完整版本号 *version* 指定的库文件。如今，版本号在Windows上被忽略。

我们建议在 *fileName* 中忽略文件名的前后缀，因为QLibrary会基于不同平台自动寻找合适的前后缀。比如Unix系的前缀“lib”，后缀“.so”，Mac及IOS的后缀".dylib"，Windows的后缀".dll"。（参见[fileName](#filename--qstring) ）

----

### QLibrary::QLibrary(const [QString](../../S/QString/QString.md) &*fileName*, int *verNum*, [QObject](../../S/QObject/QQbject.md#QObject) **parent* = nullptr)

基于给定的父对象 *parent* 构造一个库对象。它会加载文件名*fileName*、主版本号 *verNum* 指定的库文件。如今，版本号在Windows上被忽略。

我们建议在 *fileName* 中忽略文件名的前后缀，因为QLibrary会基于不同平台自动寻找合适的前后缀。比如Unix系的前缀“lib”，后缀“.so”，Mac及IOS的后缀".dylib"，Windows的后缀".dll"。（参见[fileName](#filename--qstring) ）

----

### QLibrary::QLibrary(const [QString](../../S/QString/QString.md) &*fileName*, [QObject](../../S/QObject/QQbject.md#QObject) **parent* = nullptr)

基于给定的父对象 *parent* 构造一个库对象。它会加载文件名*fileName* 指定的库文件。

我们建议在 *fileName* 中忽略文件名的前后缀，因为QLibrary会基于不同平台自动寻找合适的前后缀。比如Unix系的前缀“lib”，后缀“.so”，Mac及IOS的后缀".dylib"，Windows的后缀".dll"。（参见[fileName](#filename--qstring) ）

----

### QLibrary::QLibrary([QObject](../../S/QObject/QQbject.md#QObject) **parent* = nullptr)

基于给定的父对象 *parent* 构造一个库对象。

----

### `[virtual]`QLibrary::~QLibrary()

删除此QLibrary对象。

除非显式调用 [unload](#bool-qlibraryunload)()，库会在一直驻留在内存中，知道应用结束。

**另请参阅：** [isLoaded](#bool-qlibraryisloaded-const)() 和 [unload](#bool-qlibraryunload)().

----

### [QString](../../S/QString/QString.md) QLibrary::errorString() const

返回一个描述上一个发生的错误的文本字符串。截至现在，errorString 只会在 [load](#bool-qlibraryload)(), [unload](#bool-qlibraryunload)() 或 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 调用由于一些原因失败时才会设置。

此函数引入自：Qt 4.2.

----

### `[static]`bool QLibrary::isLibrary(const [QString](../../S/QString/QString.md) &*fileName*)

如果 *fileName* 包含一个合法的可加载的后缀，返回true；否则返回false。

|     平台      |          合法后缀          |
| :-----------: | :------------------------: |
|    Windows    |       `.dll`, `.DLL`       |
|  Unix/Linux   |           `.so`            |
|      AIX      |            `.a`            |
|     HP-UX     |   `.sl`, `.so` (HP-UXi)    |
| macOS and iOS | `.dylib`, `.bundle`, `.so` |

Unix平台上的名字后的版本号会被忽略。

----

### bool QLibrary::isLoaded() const

如果库已经被加载，返回true，否则返回false。

**另请参阅：** [load](#bool-qlibraryload)().

----

### bool QLibrary::load()

加载一个库，如果成功加载则返回true；否则返回false。因为 [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 内部会自动调用此方法，您没必要显示调用这个函数。如果在某些情况下您想提前加载库，您可以主动调用它。

**另请参阅：** [unload](#bool-qlibraryunload)().

----

### [QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const char **symbol*)

返回导出符号 *symbol* 对应的地址。如果需要，库会自动加载。如果库无法加载或符号无法解析，返回 `nullptr` 。



例如：

```
typedef int (*AvgFunction)(int, int);

AvgFunction avg = (AvgFunction) library->resolve("avg");
if (avg)
    return avg(5, 8);
else
    return -1;
```

符号必须作为C语言函数导出。这意味着如果使用C++编译器，函数必须由 `extern "C"` 包裹。在Windows平台，您还必须显式通过 `__declspec(dllexport)` 指导编译器导出符号，例如：

```
extern "C" MY_EXPORT int avg(int a, int b)
{
    return (a + b) / 2;
}
```

宏 `MY_EXPORT` 定义如下

```
#ifdef Q_OS_WIN
#define MY_EXPORT __declspec(dllexport)
#else
#define MY_EXPORT
#endif
```

----

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](../../S/QString/QString.md) &*fileName*, const char **symbol*)

这是一个重载函数。

加载文件名 *fileName* 对应的库，并返回 *symbol* 对应导出符号的地址。注意 *fileName* 不应该包含平台相关前后缀（详情见 [fileName](#filename--qstring)）. 库会一直保留到应用程序退出。

如果库无法加载或符号无法解析，返回 `nullptr` 。

**另请参阅：** [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)().

----

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](../../S/QString/QString.md) &*fileName*, int *verNum*, const char**symbol*)

这是一个重载函数。

加载文件名 *fileName* 、主版本号 *verNum* 对应的库，并返回 *symbol* 对应导出符号的地址。注意 *fileName* 不应该包含平台相关前后缀（详情见 [fileName](#filename--qstring)）. 库会一直保留到应用程序退出。*version* 参数在 Windows 上无效。

如果库无法加载或符号无法解析，返回 `nullptr` 。

**另请参阅：** [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)().

----

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](../../S/QString/QString.md) &*fileName*, const [QString](../../S/QString/QString.md) &*version*, const char **symbol*)

这是一个重载函数。

加载文件名 *fileName* 、完整版本号 *version* 对应的库，并返回 *symbol* 对应导出符号的地址。注意 *fileName* 不应该包含平台相关前后缀（详情见 [fileName](#filename--qstring)）. 库会一直保留到应用程序退出。*version* 参数在 Windows 上无效。

如果库无法加载或符号无法解析，返回 `nullptr` 。

此函数引入自：Qt 4.4.

**另请参阅：** [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)().



### void QLibrary::setFileNameAndVersion(const [QString](../../S/QString/QString.md) &*fileName*, int *versionNumber*)

设置 [fileName](#filename--qstring) 属性，以及相对应的文件名和版本号信息。*versionNumber* 参数在 Windows 上无效。

**另请参阅：** [setFileName](#filename--qstring)().



### void QLibrary::setFileNameAndVersion(const [QString](../../S/QString/QString.md) &*fileName*, const [QString](../../S/QString/QString.md) &*version*)

设置 [fileName](#filename--qstring) 属性，以及相对应的文件名和完整版本号信息。*version* 参数在 Windows 上无效。

此函数引入自：Qt 4.4.

**另请参阅：** [setFileName](#filename--qstring)().



### bool QLibrary::unload()

卸载一个库；如果成功返回`true`，否则`false`。

在应用程序结束是，此函数自动调用，因此您不应该手动调用。

如果有其他 [QLibrary](#QLibrary-Class) 示例在使用同一个库，调用会失败。卸载只会在所有实例都调用过此函数之后发生。

注意：在 Mac OS X 10.3 (Panther)，无法卸载动态链接库。

**另请参阅：** [resolve](#qfunctionpointer-qlibraryresolveconst-char-symbol)() 和 [load](#bool-qlibraryload)().