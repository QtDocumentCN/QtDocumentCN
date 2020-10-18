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

**注意：** 类中所有函数都是 [可重入的](https://doc.qt.io/qt-5/threads-reentrancy.html)。



## 公共成员类型

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| typedef | **[DecoderFn](#typedef-qfiledecoderfn)** |



## 公共成员函数

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
|         | **[QFile](#qfileqfileconst-qstring-name-qobject-parent)**(const QString &*name*, QObject **parent*) |
|         | **[QFile](#qfileqfileqobject-parent)**(QObject **parent*) |
|         | **[QFile](#qfileqfileconst-qstring-name)**(const QString &*name*) |
|         | **[QFile](#qfileqfile)**()       |
| virtual | **[~QFile](#virtualqfileqfile)**() |
| bool    | **[copy](#bool-qfilecopyconst-qstring-newname)**(const QString &*newName*) |
| bool    | **[exists](#bool-qfileexists-const)**() const |
| bool    | **[link](#bool-qfilelinkconst-qstring-linkname)**(const QString &*linkName*) |
| bool    | **[moveToTrash](#bool-qfilemovetotrash)**() |
| bool    | **[open](#override-virtualbool-qfileopenqiodeviceopenmode-mode-1)**(FILE **fh*, QIODevice::OpenMode *mode*, QFileDevice::FileHandleFlags *handleFlags* = DontCloseHandle) |
| bool    | **[open](#override-virtualbool-qfileopenqiodeviceopenmode-mode-2)**(int *fd*, QIODevice::OpenMode *mode*, QFileDevice::FileHandleFlags *handleFlags* = DontCloseHandle) |
| bool    | **[remove](#bool-qfileremove)**()     |
| bool    | **[rename](h#bool-qfilerenameconst-qstring-newname)**(const QString &*newName*) |
| void    | **[setFileName](#void-qfilesetfilenameconst-qstring-name)**(const QString &*name*) |
| QString | **[symLinkTarget](#qstring-qfilesymlinktarget-const)**() const |



## 重写公共函数

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| virtual QString                  | **[fileName](#override-virtualqstring-qfilefilename-const)**() const override |
| virtual bool                     | **[open](#override-virtualbool-qfileopenqiodeviceopenmode-mode)**(QIODevice::OpenMode *mode*) override |
| virtual QFileDevice::Permissions | **[permissions](#override-virtualqfiledevicepermissions-qfilepermissions-const)**() const override |
| virtual bool                     | **[resize](#override-virtualbool-qfileresizeqint64-sz)**(qint64 *sz*) override |
| virtual bool                     | **[setPermissions](#override-virtualbool-qfilesetpermissionsqfiledevicepermissions-permissions)**(QFileDevice::Permissions *permissions*) override |
| virtual qint64                   | **[size](#size)**() const override |



## 静态公共成员

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| bool                     | **[copy](#staticbool-qfilecopyconst-qstring-filename-const-qstring-newname)**(const QString &*fileName*, const QString &*newName*) |
| QString                  | **[decodeName](#staticqstring-qfiledecodenameconst-qbytearray-localfilename)**(const QByteArray &*localFileName*) |
| QString                  | **[decodeName](#staticqstring-qfiledecodenameconst-char-localfilename)**(const char **localFileName*) |
| QByteArray               | **[encodeName](#staticqbytearray-qfileencodenameconst-qstring-filename)**(const QString &*fileName*) |
| bool                     | **[exists](#staticbool-qfileexistsconst-qstring-filename)**(const QString &*fileName*) |
| bool                     | **[link](#staticbool-qfilelinkconst-qstring-filename-const-qstring-linkname)**(const QString &*fileName*, const QString &*linkName*) |
| bool                     | **[moveToTrash](#staticbool-qfilemovetotrashconst-qstring-filename-qstring-pathintrash--nullptr)**(const QString &*fileName*, QString **pathInTrash* = nullptr) |
| QFileDevice::Permissions | **[permissions](#staticqfiledevicepermissions-qfilepermissionsconst-qstring-filename)**(const QString &*fileName*) |
| bool                     | **[remove](#staticbool-qfileremoveconst-qstring-filename)**(const QString &*fileName*) |
| bool                     | **[rename](#staticbool-qfilerenameconst-qstring-oldname-const-qstring-newname)**(const QString &*oldName*, const QString &*newName*) |
| bool                     | **[resize](#staticbool-qfileresizeconst-qstring-filename-qint64-sz)**(const QString &*fileName*, qint64 *sz*) |
| bool                     | **[setPermissions](#override-virtualbool-qfilesetpermissionsqfiledevicepermissions-permissions-1)**(const QString &*fileName*, QFileDevice::Permissions *permissions*) |
| QString                  | **[symLinkTarget](#staticqstring-qfilesymlinktargetconst-qstring-filename)**(const QString &*fileName*) |



## 详细描述

QFile 是用于读写文本及二进制的文件及[资源](https://doc.qt.io/qt-5/resources.html)的I/O设备。 一个QFile可以单独使用，或者更简单的，可以与 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 或 [QDataStream](https://doc.qt.io/qt-5/qdatastream.html) 一同使用。

文件名通常在构造时传递，但也可以在随时使用 [setFileName](#void-qfilesetfilenameconst-qstring-name)()设置。QFile 需要目录分隔符为 '/' 而不是依照操作系统。其他分隔符 (如 '\\') 不受支持。

您可以通过 [exists](#bool-qfileexists-const)() 判断文件是否存在。（更多操作系统相关的操作在 [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 和 [QDir](https://doc.qt.io/qt-5/qdir.html) 中提供）

文件通过 [open](#override-virtualbool-qfileopenqiodeviceopenmode-mode)() 打开，通过 [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 关闭，通过 [flush](https://doc.qt.io/qt-5/qfiledevice.html#flush)() 刷新。数据通常使用 [QDataStream](https://doc.qt.io/qt-5/qdatastream.html) or [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 读写，但您也可以使用 由 [QIODevice](https://doc.qt.io/qt-5/qiodevice.html) 的继承函数 [read](https://doc.qt.io/qt-5/qiodevice.html#read)(), [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)(), [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)(), [write](https://doc.qt.io/qt-5/qiodevice.html#write)()。单字符的操作也可以使用 [getChar](https://doc.qt.io/qt-5/qiodevice.html#getChar)(), [putChar](https://doc.qt.io/qt-5/qiodevice.html#putChar)(), and [ungetChar](https://doc.qt.io/qt-5/qiodevice.html#ungetChar)()。

 [size](#size)() 返回文件大小。您可以通过 [pos](https://doc.qt.io/qt-5/qfiledevice.html#pos)() 获取当前文件位置，或通过 [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)() 移动到新的位置（译者注：此句中的“位置”指文件内操作的字节位置）。当您读到文件结尾， [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 返回 `true`。



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

 [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) flag传递给 [open](#override-virtualbool-qfileopenqiodeviceopenmode-mode)() ，其告诉Qt将Windows风格的换行符 ("\r\n") 转换为 C++风格的换行符("\n")。默认情况下，QFile 假设为二进制模式读取，不做字节转换。



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

当你使用 QFile, [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 以及 [QDir](https://doc.qt.io/qt-5/qdir.html) 来访问系统中文件，你可以使用Unicode文件名。在Unix平台，文件名会转换为8位编码。如果您想使用C++标准API (`<cstdio>` 或 `<iostream>`) 或平台相关API来访问文件而不是使用 QFile，你可以使用 [encodeName](#staticqbytearray-qfileencodenameconst-qstring-filename)() 和 [decodeName](#staticqstring-qfiledecodenameconst-qbytearray-localfilename)() 来在Unicode文件名和8位文件名间转换。

在Unix平台，有一些特殊的系统文件 (例如  `/proc` 下的文件) ，对于这些文件，[size](#size)() 会返回0，但你依然可以读取更多数据；这些数据在你调用 [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 时即时产生。在这种情况下，您便不能使用 [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 来判断是否已经没有更多数据。(因为 [atEnd](https://doc.qt.io/qt-5/qfiledevice.html#atEnd)() 通过文件大小是否到达结尾)。然而您可以通过连续调用 [readAll](https://doc.qt.io/qt-5/qiodevice.html#readAll)(),  [read](https://doc.qt.io/qt-5/qiodevice.html#read)() 或 [readLine](https://doc.qt.io/qt-5/qiodevice.html#readLine)() 指导没有数据来替代此功能。下面的例子使用 [QTextStream](https://doc.qt.io/qt-5/qtextstream.html) 逐行读取`/proc/modules` ：

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

Qt对于文件权限的理解有局限，尤其对于 [QFile::setPermissions](#override-virtualbool-qfilesetpermissionsqfiledevicepermissions-permissions)() 有影响。在Windows上，仅当没有任何 Write* flags被设置时，Qt 会设置旧版的只读 flag。Qt不会操作访问过滤表（access control lists , ACLs）这是的此函数在NTFS卷上基本上没什么用。对于VFAT格式的U盘，倒是有可能可用。POSIX 的 ACLs 也不会被修改。

**另请参见** [QTextStream](https://doc.qt.io/qt-5/qtextstream.html), [QDataStream](https://doc.qt.io/qt-5/qdatastream.html), [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html), [QDir](https://doc.qt.io/qt-5/qdir.html), 以及 [The Qt Resource System](https://doc.qt.io/qt-5/resources.html)。



## 成员类型文档

### typedef QFile::DecoderFn

这个类型定义了一个如下形式的函数的指针：

```
QString myDecoderFunc(const QByteArray &localFileName);
```

**另请参见** [setDecodingFunction](https://doc.qt.io/qt-5/qfile-obsolete.html#setDecodingFunction)().



## 成员函数文档

### QFile::QFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent*)

构造基于给定的父对象 *parent* 、文件名 *name* 指定的QFile对象。

---

### QFile::QFile([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent*)

构造基于给定的父对象 *parent* 的QFile对象。

---

### QFile::QFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

构造文件名 *name* 指定的QFile对象。

---

### QFile::QFile()

构造一个QFile对象。

---

### `[virtual]`QFile::~QFile()

销毁此QFile对象，如需要会自动关闭文件。

---

### bool QFile::copy(const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

将当前 [fileName](#override-virtualqstring-qfilefilename-const)() 指定的文件复制为文件名 *newName* 指定的文件。如果成功，返回 `true` ；否则返回 `false`。

注意如果 *newName* 文件名的文件已存在，函数不会覆盖，直接返回 `false` 。

源文件会在复制前关闭。

**另请参见** [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[static]`bool QFile::copy(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

这是一个重载函数。

将文件 *fileName* 复制为文件名 *newName*。如果成功，返回 `true` ；否则返回 `false`。

注意如果 *newName* 文件名的文件已存在，函数不会覆盖，直接返回 `false` 。

**另请参见** [rename](#rename)().

---

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::decodeName(const [QByteArray](https://doc.qt.io/qt-5/qbytearray.html) &*localFileName*)

和 [QFile::encodeName](#staticqbytearray-qfileencodenameconst-qstring-filename)() 操作恰恰相反。返回 *localFileName* 的Unicode形式。

**另请参见** [encodeName](#staticqbytearray-qfileencodenameconst-qstring-filename)().

---

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::decodeName(const char **localFileName*)

这是一个重载函数。返回 *localFileName* 的Unicode形式。

详情参见 [encodeName](#staticqbytearray-qfileencodenameconst-qstring-filename)() 。

---

### `[static]`[QByteArray](https://doc.qt.io/qt-5/qbytearray.html) QFile::encodeName(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

基于用户区域设置，将 *fileName* 转换为本地的8为表示。这对于用户选择的文件名足够使用。硬编码到程序中的文件名应当只使用7位ASCII字符。

**另请参见** [decodeName](#staticqstring-qfiledecodenameconst-qbytearray-localfilename)().

---

### `[static]`bool QFile::exists(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

如果 *fileName* 对应的文件存在，返回 `true` 否则返回 `false`。

**注意：** 如果 *fileName* 是指向不存在文件的符号链接，返回 `false`。

---

### bool QFile::exists() const

这是一个重载函数。

如果  [fileName](#override-virtualqstring-qfilefilename-const)() 对应的文件存在，返回 `true` 否则返回 `false`。

**另请参见** [fileName](#override-virtualqstring-qfilefilename-const)() and [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[override virtual]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::fileName() const

重写函数： [QFileDevice::fileName](https://doc.qt.io/qt-5/qfiledevice.html#override-virtualqstring-qfilefilename-const)() const.

返回 [setFileName](#void-qfilesetfilenameconst-qstring-name)() 或构造函数设置的文件名。

**另请参见** [setFileName](#void-qfilesetfilenameconst-qstring-name)() and [QFileInfo::fileName](https://doc.qt.io/qt-5/qfileinfo.html#override-virtualqstring-qfilefilename-const)().

---

### bool QFile::link(const [QString](https://doc.qt.io/qt-5/qstring.html) &*linkName*)

创建一个名为 *linkName* 的、指向 [fileName](#override-virtualqstring-qfilefilename-const)() 文件的链接。链接的形式取决于底层文件系统（Windows上的快捷方式或Linux下的符号链接symlink）。如果成功，返回 `true` ；返回 `false`。

此函数不会覆盖文件系统上已经存在的链接；如果已存在，`link()` 将返回 `false` 并设置 [error()](https://doc.qt.io/qt-5/qfiledevice.html#error) 为 [RenameError](https://doc.qt.io/qt-5/qfiledevice.html#FileError-enum)。

**注意：** 对于Windows平台，一个合法的链接名称必须包含 `.lnk` 后缀名。

**另请参见** [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[static]`bool QFile::link(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*linkName*)

这是一个重载函数。

创建一个名为 *linkName* 的、指向 *fileName* 文件的链接。链接的形式取决于底层文件系统（Windows上的快捷方式或Linux下的符号链接symlink）。如果成功，返回 `true` ；否则返回 `false`。

**另请参见** [link](#bool-qfilelinkconst-qstring-linkname)().

---

### bool QFile::moveToTrash()

将 [fileName](#override-virtualqstring-qfilefilename-const)() 文件移入回收站。如果成功返回 `true` ，并将 [fileName](#override-virtualqstring-qfilefilename-const)() 设置为回收站中对应文件的路径；否则返回 `false`。

**注意：** 在API不能返回回收站中文件的路径的操作系统中，一旦文件被移动 [fileName](#override-virtualqstring-qfilefilename-const)() 会被设置为空字符串。在没有回收站的操作系统，此函数总返回 `false`。

此函数引入自： Qt 5.15.

---

### `[static]`bool QFile::moveToTrash(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QString](https://doc.qt.io/qt-5/qstring.html) **pathInTrash* = nullptr)

这是一个重载函数。

将 *fileName* 文件移入回收站。如果成功返回 `true` ，并将 **pathInTrash* 设置为回收站中对应文件的路径字符串的指针；否则返回 `false`。

**注意：**  在API不能返回回收站中文件的路径的操作系统中，一旦文件被移动 **pathInTrash* 会被设置为空字符串。在没有回收站的操作系统，此函数总返回 `false`。

此函数引入自： Qt 5.15.

---

### `[override virtual]`bool QFile::open([QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*)

重写函数： [QIODevice::open](https://doc.qt.io/qt-5/qiodevice.html#override-virtualbool-qfileopenqiodeviceopenmode-mode)(QIODevice::OpenMode mode)。

使用 [OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode* 模式打开文件，如果成功，返回 `true` ；否则返回 `false`。

模式 *mode* 必须是 [QIODevice::ReadOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum), [QIODevice::WriteOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum), 或 [QIODevice::ReadWrite](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum)。也可以有附加flags，例如 [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) 和 [QIODevice::Unbuffered](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum)。

**注意：** 在 [WriteOnly](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) 或 [ReadWrite](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) 模式，如果相关文件不存在，此函数会尝试在打开前新建。


**另请参见** [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) and [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### bool QFile::open(FILE **fh*, [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*, [QFileDevice::FileHandleFlags](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) *handleFlags* = DontCloseHandle)

这是一个重载函数。

使用给出的模式 *mode* 打开已有的文件句柄 *fh*。*handleFlags* 可能会被用于指定附加选项。如果成功，返回 `true` ；否则返回 `false`。

例如：

```
#include <stdio.h>

void printError(const char* msg)
{
    QFile file;
    file.open(stderr, QIODevice::WriteOnly);
    file.write(msg, qstrlen(msg));        // 写入 stderr
    file.close();
}
```

当一个 [QFile]() 通过此函数被被打开，[close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 的行为由 [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) flag决定。如果指定了 [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) ，且此函数执行成功，那么 [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 会关闭传入的句柄。否则，[close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 不会关闭文件，只会刷新数据(flush)。

**警告：**

1. 如果 *fh* 并非指向常规文件，例如 `stdin`, `stdout`, 或 `stderr`，你可能不能够使用 [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)()，且[size](#size)() 返回0。详见 [QIODevice::isSequential](https://doc.qt.io/qt-5/qiodevice.html#isSequential)()。
2. 由于使用此函数打开的文件没有指定文件名，你不能通过 [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 读取相关信息。

**Windows平台的注意事项**

当访问文件或其他随机存取设备时，*fh* 必须以二进制模式打开（也就是 `fopen()` 的模式串必须包含'b'）。Qt 会转换行末字节如果您指定 [QIODevice::Text](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) 给 *mode*。顺序读取设备，例如标准输入输出，不受此限制影响。

您需要启用控制台应用支持，才能在控制台使用标准输入输出。要启用，可以在项目文件中加入：

```
CONFIG += console
```



**另请参见** [close](https://doc.qt.io/qt-5/qfiledevice.html#close)().

---

### bool QFile::open(int *fd*, [QIODevice::OpenMode](https://doc.qt.io/qt-5/qiodevice.html#OpenModeFlag-enum) *mode*, [QFileDevice::FileHandleFlags](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) *handleFlags* = DontCloseHandle)

这是一个重载函数。

使用给出的模式 *mode* 打开已有的文件描述符 *fh*。*handleFlags* 可能会被用于指定附加选项。如果成功，返回 `true` ；否则返回 `false`。

当一个 [QFile]() 通过此函数被被打开，[close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 的行为由 [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) flag决定。如果指定了 [AutoCloseHandle](https://doc.qt.io/qt-5/qfiledevice.html#FileHandleFlag-enum) ，且此函数执行成功，那么 [close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 会关闭传入的句柄。否则，[close](https://doc.qt.io/qt-5/qfiledevice.html#close)() 不会关闭文件，只会刷新数据(flush)。

通过此函数打开的文件会被自动设置为 `raw` 模式；这意味着文件I/O函数会很慢。如果您遇到了性能问题，可以尝试其他 `open()` 函数。

**警告：** 

1. 如果 *fd* 不是一个常规文件，例如 0 (`stdin`), 1 (`stdout`), 或 2 (`stderr`)，你可能不能够使用 [seek](https://doc.qt.io/qt-5/qfiledevice.html#seek)()，且[size](#size)() 返回0。详见 [QIODevice::isSequential](https://doc.qt.io/qt-5/qiodevice.html#isSequential)()。

2. 由于使用此函数打开的文件没有指定文件名，你不能通过 [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 读取相关信息。

**另请参见** [close](https://doc.qt.io/qt-5/qfiledevice.html#close)().

---

### `[override virtual]`[QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFile::permissions() const

重写函数： [QFileDevice::permissions](https://doc.qt.io/qt-5/qfiledevice.html#override-virtualqfiledevicepermissions-qfilepermissions-const)() const.

**另请参见** [setPermissions](#override-virtualbool-qfilesetpermissionsqfiledevicepermissions-permissions)().

---

### `[static]`[QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFile::permissions(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

这是一个重载函数。

返回 *fileName* 文件经 OR（位或）后的权限 [QFile::Permission](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) 组合。

---

### bool QFile::remove()

删除文件名 [fileName](#override-virtualqstring-qfilefilename-const)() 的文件。

如果成功，返回 `true` ；否则返回 `false`。

文件会在删除前关闭。

**另请参见** [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[static]`bool QFile::remove(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

这是一个重载函数。

删除文件名 *fileName* 的文件。

如果成功，返回 `true` ；否则返回 `false`。

**另请参见** [remove](#bool-qfileremove)().

---

### bool QFile::rename(const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

把文件 [fileName](#override-virtualqstring-qfilefilename-const)() 重命名为 *newName*。如果成功，返回 `true` ；否则返回 `false`。

注意如果 *newName* 文件名的文件已存在，函数不会覆盖，直接返回 `false` 。

文件在重命名前关闭。

如果直接重命名失败，Qt会尝试拷贝数据到 *newName* 新文件并删除旧文件来实现重命名。如果拷贝或删除失败，Qt会撤回新文件创建，返回原先状态。

**另请参见** [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[static]`bool QFile::rename(const [QString](https://doc.qt.io/qt-5/qstring.html) &*oldName*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*newName*)

这是一个重载函数。

把文件 *oldName* 重命名为 *newName*。如果成功，返回 `true` ；否则返回 `false`。

注意如果 *newName* 文件名的文件已存在，函数不会覆盖，直接返回 `false` 。

**另请参见** [rename](#rename)().

---

### `[override virtual]`bool QFile::resize([qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *sz*)

重写函数： [QFileDevice::resize](https://doc.qt.io/qt-5/qfiledevice.html#override-virtualbool-qfileresizeqint64-sz)(qint64 sz).

---

### `[static]`bool QFile::resize(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *sz*)

这是一个重载函数。

这是文件名 *fileName* 文件的大小为 *sz* 字节。如果修改大小成功返回 `true`，否则返回 `false`。如果 *sz* 比当前文件大小大，后面的数据会填充0；如果 *sz* 比当前文件大小小，会裁剪文件数据。

**警告：** 如果文件不存在，调用会失败。

**另请参见** [resize](#override-virtualbool-qfileresizeqint64-sz)().

---

### void QFile::setFileName(const [QString](https://doc.qt.io/qt-5/qstring.html) &*name*)

设置文件名 *name*。名称可以不包含目录，包含相对目录或绝对目录。

请不要在文件已经打开后调用此函数。

如果文件名不包含路径，或者是相对路径，路径会基于应用程序调用 [open](#override-virtualbool-qfileopenqiodeviceopenmode-mode)() 时的当前路径。

例如：

```
QFile file;
QDir::setCurrent("/tmp");
file.setFileName("readme.txt");
QDir::setCurrent("/home");
file.open(QIODevice::ReadOnly);      // 打开Unix下文件 "/home/readme.txt"
```

注意Qt中目录分隔符统一使用"/".

**另请参见** [fileName](#override-virtualqstring-qfilefilename-const)(), [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html), and [QDir](https://doc.qt.io/qt-5/qdir.html).


---

### `[override virtual]`bool QFile::setPermissions([QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) *permissions*)

重写函数： [QFileDevice::setPermissions](https://doc.qt.io/qt-5/qfiledevice.html#override-virtualbool-qfilesetpermissionsqfiledevicepermissions-permissions)(QFileDevice::Permissions permissions).

为文件设置 *permissions* 权限。如果成功返回 `true` ，如果权限不能修改返回 `false` 。

**警告：** 此函数不会操作修改 ACLs，这会限制函数功能。

**另请参见** [permissions](#override-virtualqfiledevicepermissions-qfilepermissions-const)() and [setFileName](#void-qfilesetfilenameconst-qstring-name)().

---

### `[static]`bool QFile::setPermissions(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QFileDevice::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) *permissions*)

这是一个重载函数。

为文件名 *fileName* 的文件设置 *permissions* 权限。

---

### `[override virtual]`[qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QFile::size() const

重写函数： [QFileDevice::size](https://doc.qt.io/qt-5/qfiledevice.html#size)() const.

---

### `[static]`[QString](https://doc.qt.io/qt-5/qstring.html) QFile::symLinkTarget(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*)

返回符号链接（Unix上的symlink或Windows上快捷方式）*fileName* 指向的文件或目录的绝对路径。如果 *fileName* 不是一个符号链接，返回空字符串。

名称可能并不是一个存在的文件，只是一个字符串路径。[QFile::exists](#bool-qfileexists-const)() 可以用来判断是否存在。

此函数引入自： Qt 4.2.

---

### [QString](https://doc.qt.io/qt-5/qstring.html) QFile::symLinkTarget() const

这是一个重载函数。

返回QFile对象对应的符号链接（Unix上的symlink或Windows上快捷方式）指向的文件或目录的绝对路径。如果 *fileName* 不是一个符号链接，返回空字符串。

名称可能并不是一个存在的文件，只是一个字符串路径。[QFile::exists](#bool-qfileexists-const)() 可以用来判断是否存在。

此函数引入自： Qt 4.2.

**另请参见** [fileName](#override-virtualqstring-qfilefilename-const)() and [setFileName](#void-qfilesetfilenameconst-qstring-name)().