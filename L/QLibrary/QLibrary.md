还是正在编写
Reserved by 顾晓 until 2020-08-16

# QLibrary Class

Qlibrary用于运行时加载库。

| 属性 | 内容 |
| ------- | ---------------------------------------------- |
| 头文件: | `#include <QLibrary>`                            |
| qmake:  | QT += core                                     |
| 继承于: | [QObject](https://doc.qt.io/qt-5/qobject.html) |

**注意：** 此类中全部函数可重入。



## 公共成员类型
|  类型  | 名称 |
| ----- | ------------------------------------------------------------ |
| enum  | **[LoadHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)** { ResolveAllSymbolsHint, ExportExternalSymbolsHint, LoadArchiveMemberHint, PreventUnloadHint, DeepBindHint } |
| flags | **[LoadHints](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)** |



## 属性

- **[fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)** : QString
- **[loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop)** : LoadHints



## 公共成员函数

| 类型 | 函数名 |
| ---- | ------ |
|                     | **[QLibrary](https://doc.qt.io/qt-5/qlibrary.html#QLibrary-3)**(const QString &*fileName*, const QString &*version*, QObject **parent* = nullptr) |
|                     | **[QLibrary](https://doc.qt.io/qt-5/qlibrary.html#QLibrary-2)**(const QString &*fileName*, int *verNum*, QObject **parent* = nullptr) |
|                     | **[QLibrary](https://doc.qt.io/qt-5/qlibrary.html#QLibrary-1)**(const QString &*fileName*, QObject **parent* = nullptr) |
|                     | **[QLibrary](https://doc.qt.io/qt-5/qlibrary.html#QLibrary)**(QObject **parent* = nullptr) |
| virtual             | **[~QLibrary](https://doc.qt.io/qt-5/qlibrary.html#dtor.QLibrary)**() |
| QString             | **[errorString](https://doc.qt.io/qt-5/qlibrary.html#errorString)**() const |
| QString             | **[fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)**() const |
| bool                | **[isLoaded](https://doc.qt.io/qt-5/qlibrary.html#isLoaded)**() const |
| bool                | **[load](https://doc.qt.io/qt-5/qlibrary.html#load)**()      |
| QLibrary::LoadHints | **[loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop)**() const |
| QFunctionPointer    | **[resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)**(const char **symbol*) |
| void                | **[setFileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)**(const QString &*fileName*) |
| void                | **[setFileNameAndVersion](https://doc.qt.io/qt-5/qlibrary.html#setFileNameAndVersion)**(const QString &*fileName*, int *versionNumber*) |
| void                | **[setFileNameAndVersion](https://doc.qt.io/qt-5/qlibrary.html#setFileNameAndVersion-1)**(const QString &*fileName*, const QString &*version*) |
| void                | **[setLoadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop)**(QLibrary::LoadHints *hints*) |
| bool                | **[unload](https://doc.qt.io/qt-5/qlibrary.html#unload)**()  |



## 静态公共成员

|  类型  | 函数名|
|---|---|
| bool             | **[isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)**(const QString &*fileName*) |
| QFunctionPointer | **[resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve-1)**(const QString &*fileName*, const char **symbol*) |
| QFunctionPointer | **[resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve-2)**(const QString &*fileName*, int *verNum*, const char **symbol*) |
| QFunctionPointer | **[resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve-3)**(const QString &*fileName*, const QString &*version*, const char **symbol*) |



## 详细描述

An instance of a QLibrary object operates on a single shared object file (which we call a "library", but is also known as a "DLL"). A QLibrary provides access to the functionality in the library in a platform independent way. You can either pass a file name in the constructor, or set it explicitly with [setFileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)(). When loading the library, QLibrary searches in all the system-specific library locations (例如： `LD_LIBRARY_PATH`on Unix), unless the file name has an absolute path.

If the file name is an absolute path then an attempt is made to load this path first. If the file cannot be found, QLibrary tries the name with different platform-specific file prefixes, like "lib" on Unix and Mac, and suffixes, like ".so" on Unix, ".dylib" on the Mac, or ".dll" on Windows.

If the file path is not absolute then QLibrary modifies the search order to try the system-specific prefixes and suffixes first, followed by the file path specified.

This makes it possible to specify shared libraries that are only identified by their basename (i.e. without their suffix), so the same code will work on different operating systems yet still minimise the number of attempts to find the library.

The most important functions are [load](https://doc.qt.io/qt-5/qlibrary.html#load)() to dynamically load the library file, [isLoaded](https://doc.qt.io/qt-5/qlibrary.html#isLoaded)() to check whether loading was successful, and [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() to resolve a symbol in the library. The [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() function implicitly tries to load the library if it has not been loaded yet. Multiple instances of QLibrary can be used to access the same physical library. Once loaded, libraries remain in memory until the application terminates. You can attempt to unload a library using [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)(), but if other instances of QLibrary are using the same library, the call will fail, and unloading will only happen when every instance has called [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)().

A typical use of QLibrary is to resolve an exported symbol in a library, and to call the C function that this symbol represents. This is called "explicit linking" in contrast to "implicit linking", which is done by the link step in the build process when linking an executable against a library.

The following code snippet loads a library, resolves the symbol "mysymbol", and calls the function if everything succeeded. If something goes wrong, 例如： the library file does not exist or the symbol is not defined, the function pointer will be `nullptr` and won't be called.

```
QLibrary myLib("mylib");
typedef void (*MyPrototype)();
MyPrototype myFunction = (MyPrototype) myLib.resolve("mysymbol");
if (myFunction)
    myFunction();
```

The symbol must be exported as a C function from the library for [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() to work. This means that the function must be wrapped in an `extern "C"` block if the library is compiled with a C++ compiler. On Windows, this also requires the use of a `dllexport` macro; see [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() for the details of how this is done. For convenience, there is a static [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() function which you can use if you just want to call a function in a library without explicitly loading the library first:

```
typedef void (*MyPrototype)();
MyPrototype myFunction =
        (MyPrototype) QLibrary::resolve("mylib", "mysymbol");
if (myFunction)
    myFunction();
```

**看看别的：** [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html).

## 成员类型介绍

### enum QLibrary::LoadHint flags QLibrary::LoadHints

This enum describes the possible hints that can be used to change the way libraries are handled when they are loaded. These values indicate how symbols are resolved when libraries are loaded, and are specified using the [setLoadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop)() function.

| Constant                              | Value  | Description                                                  |
| ------------------------------------- | ------ | ------------------------------------------------------------ |
| `QLibrary::ResolveAllSymbolsHint`     | `0x01` | Causes all symbols in a library to be resolved when it is loaded, not simply when [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() is called. |
| `QLibrary::ExportExternalSymbolsHint` | `0x02` | Exports unresolved and external symbols in the library so that they can be resolved in other dynamically-loaded libraries loaded later. |
| `QLibrary::LoadArchiveMemberHint`     | `0x04` | Allows the file name of the library to specify a particular object file within an archive file. If this hint is given, the filename of the library consists of a path, which is a reference to an archive file, followed by a reference to the archive member. |
| `QLibrary::PreventUnloadHint`         | `0x08` | Prevents the library from being unloaded from the address space if close() is called. The library's static variables are not reinitialized if open() is called at a later time. |
| `QLibrary::DeepBindHint`              | `0x10` | Instructs the linker to prefer definitions in the loaded library over exported definitions in the loading application when resolving external symbols in the loaded library. This option is only supported on Linux. |

The LoadHints type is a typedef for [QFlags](https://doc.qt.io/qt-5/qflags.html)<LoadHint>. It stores an OR combination of LoadHint values.

**看看别的：** [loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop).

## Property Documentation

### fileName : [QString](https://doc.qt.io/qt-5/qstring.html)

This property holds the file name of the library

We recommend omitting the file's suffix in the file name, since [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) will automatically look for the file with the appropriate suffix (see [isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)()).

When loading the library, [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) searches in all system-specific library locations (for example, `LD_LIBRARY_PATH` on Unix), unless the file name has an absolute path. After loading the library successfully, fileName() returns the fully-qualified file name of the library, including the full path to the library if one was given in the constructor or passed to setFileName().

For example, after successfully loading the "GL" library on Unix platforms, fileName() will return "libGL.so". If the file name was originally passed as "/usr/lib/libGL", fileName() will return "/usr/lib/libGL.so".

**Access functions:**

| QString | **fileName**() const                       |
| ------- | ------------------------------------------ |
| void    | **setFileName**(const QString &*fileName*) |

### loadHints : [LoadHints](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)

Give the [load](https://doc.qt.io/qt-5/qlibrary.html#load)() function some hints on how it should behave.

You can give some hints on how the symbols are resolved. Usually, the symbols are not resolved at load time, but resolved lazily, (that is, when [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() is called). If you set the loadHints to [ResolveAllSymbolsHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum), then all symbols will be resolved at load time if the platform supports it.

Setting [ExportExternalSymbolsHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum) will make the external symbols in the library available for resolution in subsequent loaded libraries.

If [LoadArchiveMemberHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum) is set, the file name is composed of two components: A path which is a reference to an archive file followed by the second component which is the reference to the archive member. For instance, the [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop) `libGL.a(shr_64.o)` will refer to the library `shr_64.o` in the archive file named `libGL.a`. This is only supported on the AIX platform.

The interpretation of the load hints is platform dependent, and if you use it you are probably making some assumptions on which platform you are compiling for, so use them only if you understand the consequences of them.

By default, none of these flags are set, so libraries will be loaded with lazy symbol resolution, and will not export external symbols for resolution in other dynamically-loaded libraries.

**注意：** Setting this property after the library has been loaded has no effect and loadHints() will not reflect those changes.

**注意：** This property is shared among all [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) instances that refer to the same library.

**Access functions:**

| QLibrary::LoadHints | **loadHints**() const                         |
| ------------------- | --------------------------------------------- |
| void                | **setLoadHints**(QLibrary::LoadHints *hints*) |

## Member Function Documentation

### QLibrary::QLibrary(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*version*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a library object with the given *parent* that will load the library specified by *fileName* and full version number *version*. Currently, the version number is ignored on Windows.

We recommend omitting the file's suffix in *fileName*, since QLibrary will automatically look for the file with the appropriate suffix in accordance with the platform, 例如： ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop).)

### QLibrary::QLibrary(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, int *verNum*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a library object with the given *parent* that will load the library specified by *fileName* and major version number *verNum*. Currently, the version number is ignored on Windows.

We recommend omitting the file's suffix in *fileName*, since QLibrary will automatically look for the file with the appropriate suffix in accordance with the platform, 例如： ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop).)

### QLibrary::QLibrary(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a library object with the given *parent* that will load the library specified by *fileName*.

We recommend omitting the file's suffix in *fileName*, since QLibrary will automatically look for the file with the appropriate suffix in accordance with the platform, 例如： ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop).)

### QLibrary::QLibrary([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a library with the given *parent*.

### `[virtual]`QLibrary::~QLibrary()

Destroys the [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) object.

Unless [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)() was called explicitly, the library stays in memory until the application terminates.

**看看别的：** [isLoaded](https://doc.qt.io/qt-5/qlibrary.html#isLoaded)() and [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QLibrary::errorString() const

Returns a text string with the description of the last error that occurred. Currently, errorString will only be set if [load](https://doc.qt.io/qt-5/qlibrary.html#load)(), [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)() or [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() for some reason fails.

This function was introduced in Qt 4.2.

### `[static]`bool QLibrary::isLibrary(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

Returns `true` if *fileName* has a valid suffix for a loadable library; otherwise returns `false`.

|   Platform    |       Valid suffixes       |
| :-----------: | :------------------------: |
|    Windows    |       `.dll`, `.DLL`       |
|  Unix/Linux   |           `.so`            |
|      AIX      |            `.a`            |
|     HP-UX     |   `.sl`, `.so` (HP-UXi)    |
| macOS and iOS | `.dylib`, `.bundle`, `.so` |

Trailing versioning numbers on Unix are ignored.

### bool QLibrary::isLoaded() const

Returns `true` if the library is loaded; otherwise returns `false`.

**看看别的：** [load](https://doc.qt.io/qt-5/qlibrary.html#load)().

### bool QLibrary::load()

Loads the library and returns `true` if the library was loaded successfully; otherwise returns `false`. Since [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() always calls this function before resolving any symbols it is not necessary to call it explicitly. In some situations you might want the library loaded in advance, in which case you would use this function.

**看看别的：** [unload](https://doc.qt.io/qt-5/qlibrary.html#unload)().

### [QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const char **symbol*)

Returns the address of the exported symbol *symbol*. The library is loaded if necessary. The function returns `nullptr` if the symbol could not be resolved or if the library could not be loaded.

Example:

```
typedef int (*AvgFunction)(int, int);

AvgFunction avg = (AvgFunction) library->resolve("avg");
if (avg)
    return avg(5, 8);
else
    return -1;
```

The symbol must be exported as a C function from the library. This means that the function must be wrapped in an `extern "C"` if the library is compiled with a C++ compiler. On Windows you must also explicitly export the function from the DLL using the `__declspec(dllexport)`compiler directive, for example:

```
extern "C" MY_EXPORT int avg(int a, int b)
{
    return (a + b) / 2;
}
```

with `MY_EXPORT` defined as

```
#ifdef Q_OS_WIN
#define MY_EXPORT __declspec(dllexport)
#else
#define MY_EXPORT
#endif
```

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const char **symbol*)

This is an overloaded function.

Loads the library *fileName* and returns the address of the exported symbol *symbol*. Note that *fileName* should not include the platform-specific file suffix; (see [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)). The library remains loaded until the application exits.

The function returns `nullptr` if the symbol could not be resolved or if the library could not be loaded.

**看看别的：** [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)().

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, int *verNum*, const char**symbol*)

This is an overloaded function.

Loads the library *fileName* with major version number *verNum* and returns the address of the exported symbol *symbol*. Note that *fileName*should not include the platform-specific file suffix; (see [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)). The library remains loaded until the application exits. *verNum* is ignored on Windows.

The function returns `nullptr` if the symbol could not be resolved or if the library could not be loaded.

**看看别的：** [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)().

### `[static]`[QFunctionPointer](https://doc.qt.io/qt-5/qtglobal.html#QFunctionPointer-typedef) QLibrary::resolve(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*version*, const char **symbol*)

This is an overloaded function.

Loads the library *fileName* with full version number *version* and returns the address of the exported symbol *symbol*. Note that *fileName* should not include the platform-specific file suffix; (see [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)). The library remains loaded until the application exits. *version* is ignored on Windows.

The function returns `nullptr` if the symbol could not be resolved or if the library could not be loaded.

This function was introduced in Qt 4.4.

**看看别的：** [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)().

### void QLibrary::setFileNameAndVersion(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, int *versionNumber*)

Sets the [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop) property and major version number to *fileName* and *versionNumber* respectively. The *versionNumber* is ignored on Windows.

**看看别的：** [setFileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)().

### void QLibrary::setFileNameAndVersion(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*version*)

Sets the [fileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop) property and full version number to *fileName* and *version* respectively. The *version* parameter is ignored on Windows.

This function was introduced in Qt 4.4.

**看看别的：** [setFileName](https://doc.qt.io/qt-5/qlibrary.html#fileName-prop)().

### bool QLibrary::unload()

Unloads the library and returns `true` if the library could be unloaded; otherwise returns `false`.

This happens automatically on application termination, so you shouldn't normally need to call this function.

If other instances of [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) are using the same library, the call will fail, and unloading will only happen when every instance has called unload().

Note that on Mac OS X 10.3 (Panther), dynamic libraries cannot be unloaded.

**看看别的：** [resolve](https://doc.qt.io/qt-5/qlibrary.html#resolve)() and [load](https://doc.qt.io/qt-5/qlibrary.html#load)().