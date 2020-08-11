# QFile Class

QFile 类提供读写文件的接口。 

| 属性 | 方法 |
| ------------- | ------------------------------------------------------------ |
| Header:       | #include <QFile>                                             |
| qmake:        | QT += core                                                   |
| Inherits:     | [QFileDevice](https://doc.qt.io/qt-5/qfiledevice.html)       |
| Inherited By: | [QTemporaryFile](https://doc.qt.io/qt-5/qtemporaryfile.html) |

- [包含继承成员的成员列表](https://doc.qt.io/qt-5/qfile-members.html)
- [废弃的成员](https://doc.qt.io/qt-5/qfile-obsolete.html)

**注意：** 类中所有函数都是 [可重入的](https://doc.qt.io/qt-5/threads-reentrancy.html).



## 公共成员类型

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| typedef | **[DecoderFn](https://doc.qt.io/qt-5/qfile.html#DecoderFn-typedef)** |



## 公共成员函数

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
|         | **[QFile](https://doc.qt.io/qt-5/qfile.html#QFile-3)**(const QString &*name*, QObject **parent*) |
|         | **[QFile](https://doc.qt.io/qt-5/qfile.html#QFile-2)**(QObject **parent*) |
|         | **[QFile](https://doc.qt.io/qt-5/qfile.html#QFile-1)**(const QString &*name*) |
|         | **[QFile](https://doc.qt.io/qt-5/qfile.html#QFile)**()       |
| virtual | **[~QFile](https://doc.qt.io/qt-5/qfile.html#dtor.QFile)**() |
| bool    | **[copy](https://doc.qt.io/qt-5/qfile.html#copy)**(const QString &*newName*) |
| bool    | **[exists](https://doc.qt.io/qt-5/qfile.html#exists-1)**() const |
| bool    | **[link](https://doc.qt.io/qt-5/qfile.html#link)**(const QString &*linkName*) |
| bool    | **[moveToTrash](https://doc.qt.io/qt-5/qfile.html#moveToTrash)**() |
| bool    | **[open](https://doc.qt.io/qt-5/qfile.html#open-1)**(FILE **fh*, QIODevice::OpenMode *mode*, QFileDevice::FileHandleFlags *handleFlags* = DontCloseHandle) |
| bool    | **[open](https://doc.qt.io/qt-5/qfile.html#open-2)**(int *fd*, QIODevice::OpenMode *mode*, QFileDevice::FileHandleFlags *handleFlags* = DontCloseHandle) |
| bool    | **[remove](https://doc.qt.io/qt-5/qfile.html#remove)**()     |
| bool    | **[rename](https://doc.qt.io/qt-5/qfile.html#rename)**(const QString &*newName*) |
| void    | **[setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)**(const QString &*name*) |
| QString | **[symLinkTarget](https://doc.qt.io/qt-5/qfile.html#symLinkTarget-1)**() const |



## 重载公共函数

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| virtual QString                  | **[fileName](https://doc.qt.io/qt-5/qfile.html#fileName)**() const override |
| virtual bool                     | **[open](https://doc.qt.io/qt-5/qfile.html#open)**(QIODevice::OpenMode *mode*) override |
| virtual QFileDevice::Permissions | **[permissions](https://doc.qt.io/qt-5/qfile.html#permissions)**() const override |
| virtual bool                     | **[resize](https://doc.qt.io/qt-5/qfile.html#resize)**(qint64 *sz*) override |
| virtual bool                     | **[setPermissions](https://doc.qt.io/qt-5/qfile.html#setPermissions)**(QFileDevice::Permissions *permissions*) override |
| virtual qint64                   | **[size](https://doc.qt.io/qt-5/qfile.html#size)**() const override |



## 静态公共成员

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| bool                     | **[copy](https://doc.qt.io/qt-5/qfile.html#copy-1)**(const QString &*fileName*, const QString &*newName*) |
| QString                  | **[decodeName](https://doc.qt.io/qt-5/qfile.html#decodeName)**(const QByteArray &*localFileName*) |
| QString                  | **[decodeName](https://doc.qt.io/qt-5/qfile.html#decodeName-1)**(const char **localFileName*) |
| QByteArray               | **[encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)**(const QString &*fileName*) |
| bool                     | **[exists](https://doc.qt.io/qt-5/qfile.html#exists)**(const QString &*fileName*) |
| bool                     | **[link](https://doc.qt.io/qt-5/qfile.html#link-1)**(const QString &*fileName*, const QString &*linkName*) |
| bool                     | **[moveToTrash](https://doc.qt.io/qt-5/qfile.html#moveToTrash-1)**(const QString &*fileName*, QString **pathInTrash* = nullptr) |
| QFileDevice::Permissions | **[permissions](https://doc.qt.io/qt-5/qfile.html#permissions-1)**(const QString &*fileName*) |
| bool                     | **[remove](https://doc.qt.io/qt-5/qfile.html#remove-1)**(const QString &*fileName*) |
| bool                     | **[rename](https://doc.qt.io/qt-5/qfile.html#rename-1)**(const QString &*oldName*, const QString &*newName*) |
| bool                     | **[resize](https://doc.qt.io/qt-5/qfile.html#resize-1)**(const QString &*fileName*, qint64 *sz*) |
| bool                     | **[setPermissions](https://doc.qt.io/qt-5/qfile.html#setPermissions-1)**(const QString &*fileName*, QFileDevice::Permissions *permissions*) |
| QString                  | **[symLinkTarget](https://doc.qt.io/qt-5/qfile.html#symLinkTarget)**(const QString &*fileName*) |



## 详细描述

QFile 是用于读写文本及二进制的文件及[资源](https://doc.qt.io/qt-5/resources.html)的I/O设备。 一个QFile可以单独使用，或者更简单的，可以与 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 或 [QDataStream](https://doc.qt.io/qt-5/qdatastream.html) 一同使用。

文件名通常在构造时传递，但也可以在随时使用 [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)()设置。QFile 需要目录分隔符为 '/' 而不是依照操作系统。其他分隔符 (如 '\\') 不受支持。

您可以通过 [exists](https://doc.qt.io/qt-5/qfile.html#exists-1)() 判断文件是否存在。（更多操作系统相关的操作在 [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 和 [QDir](https://doc.qt.io/qt-5/qdir.html) 中提供）

文件通过 [open](https://doc.qt.io/qt-5/qfile.html#open)() 打开，通过 [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 关闭，通过 [flush](https://doc.qt.io/qt-5/qfiledevice.html#flush)() 刷新。数据通常使用 [QDataStream](https://doc.qt.io/qt-5/qdatastream.html) or [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 读写，但您也可以使用 由 [QIODevice](https://doc.qt.io/qt-5/qiodevice.html) 的继承函数 [read](https://doc.qt.io/qt-5/qiodevice.html#read)(), [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)(), [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)(), [write](https://doc.qt.io/qt-5/qiodevice.html#write)()。单字符的操作也可以使用 [getChar](https://doc.qt.io/qt-5/qiodevice.html#getChar)(), [putChar](https://doc.qt.io/qt-5/qiodevice.html#putChar)(), and [ungetChar](https://doc.qt.io/qt-5/qiodevice.html#ungetChar)()。

 [size](https://doc.qt.io/qt-5/qfile.html#size)() 返回文件大小。您可以通过 [pos](https://doc.qt.io/qt-5/qfiledevice.html#pos)() 获取当前文件位置，或通过 [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)() 移动到新的位置（译者注：此句中的“位置”指文件内操作的字节位置）。当您读到文件结尾， [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 返回 `true`。



### 直接读文件

如下例子逐行地直接读取文本文件：

```
    QFile file("in.txt");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    while (!file.atEnd()) {
        QByteArray line = file.readLine();
        process_line(line);
    }
```

 [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) flag传递给 [open](https://doc.qt.io/qt-5/qfile.html#open)() ，其告诉Qt将Windows风格的换行符 ("\r\n") 转换为 C++风格的换行符("\n")。默认情况下，QFile 假设为二进制模式读取，不做字节转换。



### 通过流来读文件

如下例子逐行地通过 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 读取文本文件：

```
    QFile file("in.txt");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QTextStream in(&file);
    while (!in.atEnd()) {
        QString line = in.readLine();
        process_line(line);
    }
```



[QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 会特意把8位文件中字节数据转换为QString中16位UTF-16字符。默认情况下，其假设用户使用系统默认编码（例如unix平台上是UTF-8；详情参看 [QTextCodec::codecForLocale](https://doc.qt.io/qt-5/qtextcodec.html#codecForLocale)() ）。编码可以通过 [QTextStream::setCodec](https://doc.qt.io/qt-5/qtextstream.html#setCodec)() 改变。

要写入文本，您可以使用左移运算符运算符 operator<<()，在 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 中，其重载用于讲右侧内容追加的左侧，示例如下：

```
    QFile file("out.txt");
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
        return;

    QTextStream out(&file);
    out << "The magic number is: " << 49 << "\n";
```

[QDataStream](https://doc.qt.io/qt-5/qdatastream.html) 和上文很相似，详情请见相当应类的文档。

当你使用 QFile, [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 以及 [QDir](https://doc.qt.io/qt-5/qdir.html) 来访问系统中文件，你可以使用Unicode文件名。在Unix平台，文件名会转换为8位编码。如果您想使用C++标准API (`<cstdio>` 或 `<iostream>`) 或平台相关API来访问文件而不是使用 QFile，你可以使用 [encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)() 和 [decodeName](https://doc.qt.io/qt-5/qfile.html#decodeName)() 来在Unicode文件名和8位文件名间转换。

在Unix平台，有一些特殊的系统文件 (例如  `/proc` 下的文件) ，对于这些文件，[size](https://doc.qt.io/qt-5/qfile.html#size)() 会返回0，但你依然可以读取更多数据；这些数据在你调用 [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 时即时产生。在这种情况下，您便不能使用 [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 来判断是否已经没有更多数据。(因为 [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 通过文件大小是否到达结尾)。然而您可以通过连续调用 [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)(),  [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 或 [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)() 指导没有数据来替代此功能。下面的例子使用 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 逐行读取`/proc/modules` ：

```
    QFile file("/proc/modules");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QTextStream in(&file);
    QString line = in.readLine();
    while (!line.isNull()) {
        process_line(line);
        line = in.readLine();
    }
```



### 信号

不像其他 [QIODevice](https://doc.qt.io/qt-5/qiodevice.html) 的实现，例如 [QTcpSocket](https://doc.qt.io/qt-5/qtcpsocket.html)，QFile 不会发出 [aboutToClose](https://doc.qt.io/qt-5/qiodevice.html#aboutToClose)(), [bytesWritten](https://doc.qt.io/qt-5/qiodevice.html#bytesWritten)(), 及 [readyRead](https://doc.qt.io/qt-5/qiodevice.html#readyRead)() 这些信号。这个实现细节意味着 QFile 不适用于读写某些特定类型的文件，比如Unix上的设备文件。



### 平台相关信息

文件权限和Unix和Windows上的处理并不相同。在Unix平台上，一个非 [可写入](https://doc.qt.io/qt-5/qiodevice.html#isWritable) 的目录，文件无法创建。但对于Windows并不一定如此，例如 'My Documents' （我的文档）目录通常不可写入，但是在其中依然可以创建文件。

Qt对于文件权限的理解有局限，尤其对于 [QFile::setPermissions](https://doc.qt.io/qt-5/qfile.html#setPermissions)() 有影响。在Windows上，仅当没有任何 Write* flags被设置时，Qt 会设置旧版的只读 flag。Qt不会操作访问过滤表（access control lists , ACLs）这是的此函数在NTFS卷上基本上没什么用。对于VFAT格式的U盘，倒是有可能可用。POSIX 的 ACLs 也不会被修改。

**另请参见** [QTextStream](https://doc.qt.io/qt-5/qtextstream.html), [QDataStream](https://doc.qt.io/qt-5/qdatastream.html), [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html), [QDir](https://doc.qt.io/qt-5/qdir.html), 以及 [The Qt Resource System](https://doc.qt.io/qt-5/resources.html)。



## 成员类型文档

### typedef QFile::DecoderFn

这个类型定义了一个如下形式的函数的指针：

```
QString myDecoderFunc(const QByteArray &localFileName);
```

**另请参见** [setDecodingFunction](https://doc.qt.io/qt-5/qfile-obsolete.html#setDecodingFunction)().



## Member Function Documentation

### QFile::QFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent*)

Constructs a new file object with the given *parent* to represent the file with the specified *name*.

### QFile::QFile([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent*)

Constructs a new file object with the given *parent*.

### QFile::QFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

Constructs a new file object to represent the file with the given *name*.

### QFile::QFile()

Constructs a QFile object.

### `[virtual]`QFile::~QFile()

Destroys the file object, closing it if necessary.

### bool QFile::copy(const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

Copies the file currently specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() to a file called *newName*. Returns `true` if successful; otherwise returns `false`.

Note that if a file with the name *newName* already exists, copy() returns `false` (i.e. [QFile](https://doc.qt.io/qt-5/qfile.html) will not overwrite it).

The source file is closed before it is copied.

**另请参见** [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[static]`bool QFile::copy(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

This is an overloaded function.

Copies the file *fileName* to *newName*. Returns `true` if successful; otherwise returns `false`.

If a file with the name *newName* already exists, copy() returns `false` (i.e., [QFile](https://doc.qt.io/qt-5/qfile.html) will not overwrite it).

**另请参见** [rename](https://doc.qt.io/qt-5/qfile.html#rename)().

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::decodeName(const [QByteArray](https://doc.qt.io/qt-5/qbytearray.html) &*localFileName*)

This does the reverse of [QFile::encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)() using *localFileName*.

**另请参见** [encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)().

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::decodeName(const char **localFileName*)

This is an overloaded function.

Returns the Unicode version of the given *localFileName*. See [encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)() for details.

### `[static]`[QByteArray](https://doc.qt.io/qt-5/qbytearray.html) QFile::encodeName(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

Converts *fileName* to the local 8-bit encoding determined by the user's locale. This is sufficient for file names that the user chooses. File names hard-coded into the application should only use 7-bit ASCII filename characters.

**另请参见** [decodeName](https://doc.qt.io/qt-5/qfile.html#decodeName)().

### `[static]`bool QFile::exists(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

Returns `true` if the file specified by *fileName* exists; otherwise returns `false`.

**注意：** If *fileName* is a symlink that points to a non-existing file, false is returned.

### bool QFile::exists() const

This is an overloaded function.

Returns `true` if the file specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() exists; otherwise returns `false`.

**另请参见** [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() and [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[override virtual]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::fileName() const

Reimplements: [QFileDevice::fileName](https://doc.qt.io/qt-5/qfiledevice.html#fileName)() const.

Returns the name set by [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)() or to the [QFile](https://doc.qt.io/qt-5/qfile.html) constructors.

**另请参见** [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)() and [QFileInfo::fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)().

### bool QFile::link(const [QString](https://doc.qt.io/qt-5/qstring.html) &*linkName*)

Creates a link named *linkName* that points to the file currently specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)(). What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix). Returns `true` if successful; otherwise returns `false`.

This function will not overwrite an already existing entity in the file system; in this case, `link()` will return false and set [error()](https://doc.qt.io/qt-5/qfiledevice.html#error) to return [RenameError](https://doc.qt.io/qt-5/qfiledevice.html#FileError-enum).

**注意：** To create a valid link on Windows, *linkName* must have a `.lnk` file extension.

**另请参见** [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[static]`bool QFile::link(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*linkName*)

This is an overloaded function.

Creates a link named *linkName* that points to the file *fileName*. What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix). Returns `true` if successful; otherwise returns `false`.

**另请参见** [link](https://doc.qt.io/qt-5/qfile.html#link)().

### bool QFile::moveToTrash()

Moves the file specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() to the trash. Returns `true` if successful, and sets the [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() to the path at which the file can be found within the trash; otherwise returns `false`.

**注意：** On systems where the system API doesn't report the location of the file in the trash, [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() will be set to the null string once the file has been moved. On systems that don't have a trash can, this function always returns false.

This function was introduced in Qt 5.15.

### `[static]`bool QFile::moveToTrash(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QString](https://doc.qt.io/qt-5/qstring.html) **pathInTrash* = nullptr)

This is an overloaded function.

Moves the file specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() to the trash. Returns `true` if successful, and sets *pathInTrash* (if provided) to the path at which the file can be found within the trash; otherwise returns `false`.

**注意：** On systems where the system API doesn't report the path of the file in the trash, *pathInTrash* will be set to the null string once the file has been moved. On systems that don't have a trash can, this function always returns false.

This function was introduced in Qt 5.15.

### `[override virtual]`bool QFile::open([QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*)

Reimplements: [QIODevice::open](https://doc.qt.io/qt-5/qiodevice.html#open)(QIODevice::OpenMode mode).

Opens the file using [OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*, returning true if successful; otherwise false.

The *mode* must be [QIODevice::ReadOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum), [QIODevice::WriteOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum), or [QIODevice::ReadWrite](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum). It may also have additional flags, such as [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) and [QIODevice::Unbuffered](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum).

**注意：** In [WriteOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) or [ReadWrite](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) mode, if the relevant file does not already exist, this function will try to create a new file before opening it.

**另请参见** [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) and [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### bool QFile::open(FILE **fh*, [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*, [QFileDevice::FileHandleFlags](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) *handleFlags* = DontCloseHandle)

This is an overloaded function.

Opens the existing file handle *fh* in the given *mode*. *handleFlags* may be used to specify additional options. Returns `true` if successful; otherwise returns `false`.

Example:

```
#include <stdio.h>

void printError(const char* msg)
{
    QFile file;
    file.open(stderr, QIODevice::WriteOnly);
    file.write(msg, qstrlen(msg));        // write to stderr
    file.close();
}
```

When a [QFile](https://doc.qt.io/qt-5/qfile.html) is opened using this function, behaviour of [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() is controlled by the [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) flag. If [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) is specified, and this function succeeds, then calling [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() closes the adopted handle. Otherwise, [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() does not actually close the file, but only flushes it.

**Warning:**

1. If *fh* does not refer to a regular file, 例如, it is `stdin`, `stdout`, or `stderr`, you may not be able to [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)(). [size](https://doc.qt.io/qt-5/qfile.html#size)() returns `0` in those cases. See [QIODevice::isSequential](https://doc.qt.io/qt-5/qiodevice.html#isSequential)() for more information.
2. Since this function opens the file without specifying the file name, you cannot use this [QFile](https://doc.qt.io/qt-5/qfile.html) with a [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html).

**Note for the Windows Platform**

*fh* must be opened in binary mode (i.e., the mode string must contain 'b', as in "rb" or "wb") when accessing files and other random-access devices. Qt will translate the end-of-line characters if you pass [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) to *mode*. Sequential devices, such as stdin and stdout, are unaffected by this limitation.

You need to enable support for console applications in order to use the stdin, stdout and stderr streams at the console. To do this, add the following declaration to your application's project file:

```
CONFIG += console
```

**另请参见** [close](https://doc.qt.io/qt-5/qfiledevice.html#close)().

### bool QFile::open(int *fd*, [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*, [QFileDevice::FileHandleFlags](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) *handleFlags* = DontCloseHandle)

This is an overloaded function.

Opens the existing file descriptor *fd* in the given *mode*. *handleFlags* may be used to specify additional options. Returns `true` if successful; otherwise returns `false`.

When a [QFile](https://doc.qt.io/qt-5/qfile.html) is opened using this function, behaviour of [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() is controlled by the [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) flag. If [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) is specified, and this function succeeds, then calling [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() closes the adopted handle. Otherwise, [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() does not actually close the file, but only flushes it.

The [QFile](https://doc.qt.io/qt-5/qfile.html) that is opened using this function is automatically set to be in raw mode; this means that the file input/output functions are slow. If you run into performance issues, you should try to use one of the other open functions.

**Warning:** If *fd* is not a regular file, e.g, it is 0 (`stdin`), 1 (`stdout`), or 2 (`stderr`), you may not be able to [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)(). In those cases, [size](https://doc.qt.io/qt-5/qfile.html#size)() returns `0`. See [QIODevice::isSequential](https://doc.qt.io/qt-5/qiodevice.html#isSequential)() for more information.

**Warning:** Since this function opens the file without specifying the file name, you cannot use this [QFile](https://doc.qt.io/qt-5/qfile.html) with a [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html).

**另请参见** [close](https://doc.qt.io/qt-5/qfiledevice.html#close)().

### `[override virtual]`[QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFile::permissions() const

Reimplements: [QFileDevice::permissions](https://doc.qt.io/qt-5/qfiledevice.html#permissions)() const.

**另请参见** [setPermissions](https://doc.qt.io/qt-5/qfile.html#setPermissions)().

### `[static]`[QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFile::permissions(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

This is an overloaded function.

Returns the complete OR-ed together combination of [QFile::Permission](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) for *fileName*.

### bool QFile::remove()

Removes the file specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)(). Returns `true` if successful; otherwise returns `false`.

The file is closed before it is removed.

**另请参见** [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[static]`bool QFile::remove(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

This is an overloaded function.

Removes the file specified by the *fileName* given.

Returns `true` if successful; otherwise returns `false`.

**另请参见** [remove](https://doc.qt.io/qt-5/qfile.html#remove)().

### bool QFile::rename(const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

Renames the file currently specified by [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() to *newName*. Returns `true` if successful; otherwise returns `false`.

If a file with the name *newName* already exists, rename() returns `false` (i.e., [QFile](https://doc.qt.io/qt-5/qfile.html) will not overwrite it).

The file is closed before it is renamed.

If the rename operation fails, Qt will attempt to copy this file's contents to *newName*, and then remove this file, keeping only *newName*. If that copy operation fails or this file can't be removed, the destination file *newName* is removed to restore the old state.

**另请参见** [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[static]`bool QFile::rename(const [QString](https://doc.qt.io/qt-5/qstring.html) &*oldName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

This is an overloaded function.

Renames the file *oldName* to *newName*. Returns `true` if successful; otherwise returns `false`.

If a file with the name *newName* already exists, rename() returns `false` (i.e., [QFile](https://doc.qt.io/qt-5/qfile.html) will not overwrite it).

**另请参见** [rename](https://doc.qt.io/qt-5/qfile.html#rename)().

### `[override virtual]`bool QFile::resize([qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *sz*)

Reimplements: [QFileDevice::resize](https://doc.qt.io/qt-5/qfiledevice.html#resize)(qint64 sz).

### `[static]`bool QFile::resize(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *sz*)

This is an overloaded function.

Sets *fileName* to size (in bytes) *sz*. Returns `true` if the resize succeeds; false otherwise. If *sz* is larger than *fileName* currently is the new bytes will be set to 0, if *sz* is smaller the file is simply truncated.

**Warning:** This function can fail if the file doesn't exist.

**另请参见** [resize](https://doc.qt.io/qt-5/qfile.html#resize)().

### void QFile::setFileName(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

Sets the *name* of the file. The name can have no path, a relative path, or an absolute path.

Do not call this function if the file has already been opened.

If the file name has no path or a relative path, the path used will be the application's current directory path *at the time of the [open](https://doc.qt.io/qt-5/qfile.html#open)()* call.

Example:

```
QFile file;
QDir::setCurrent("/tmp");
file.setFileName("readme.txt");
QDir::setCurrent("/home");
file.open(QIODevice::ReadOnly);      // opens "/home/readme.txt" under Unix
```

Note that the directory separator "/" works for all operating systems supported by Qt.

**另请参见** [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)(), [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html), and [QDir](https://doc.qt.io/qt-5/qdir.html).

### `[override virtual]`bool QFile::setPermissions([QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) *permissions*)

Reimplements: [QFileDevice::setPermissions](https://doc.qt.io/qt-5/qfiledevice.html#setPermissions)(QFileDevice::Permissions permissions).

Sets the permissions for the file to the *permissions* specified. Returns `true` if successful, or `false` if the permissions cannot be modified.

**Warning:** This function does not manipulate ACLs, which may limit its effectiveness.

**另请参见** [permissions](https://doc.qt.io/qt-5/qfile.html#permissions)() and [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().

### `[static]`bool QFile::setPermissions(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum)*permissions*)

This is an overloaded function.

Sets the permissions for *fileName* file to *permissions*.

### `[override virtual]`[qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QFile::size() const

Reimplements: [QFileDevice::size](https://doc.qt.io/qt-5/qfiledevice.html#size)() const.

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::symLinkTarget(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

Returns the absolute path of the file or directory referred to by the symlink (or shortcut on Windows) specified by *fileName*, or returns an empty string if the *fileName* does not correspond to a symbolic link.

This name may not represent an existing file; it is only a string. [QFile::exists](https://doc.qt.io/qt-5/qfile.html#exists-1)() returns `true` if the symlink points to an existing file.

This function was introduced in Qt 4.2.

### [QString](https://doc.qt.io/qt-5/qstring.html) QFile::symLinkTarget() const

This is an overloaded function.

Returns the absolute path of the file or directory a symlink (or shortcut on Windows) points to, or a an empty string if the object isn't a symbolic link.

This name may not represent an existing file; it is only a string. [QFile::exists](https://doc.qt.io/qt-5/qfile.html#exists-1)() returns `true` if the symlink points to an existing file.

This function was introduced in Qt 4.2.

**另请参见** [fileName](https://doc.qt.io/qt-5/qfile.html#fileName)() and [setFileName](https://doc.qt.io/qt-5/qfile.html#setFileName)().