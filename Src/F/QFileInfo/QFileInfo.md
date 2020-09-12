# QFileInfo 类

QFileInfo 类用于系统无关的文件信息。[更多内容...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)

|属性|方法|
|----:|:----|
|头文件:|`#include <QFileInfo>`|
|qmake:|`QT += core`|

- [列出所有成员函数，包括继承的成员函数](qfileinfo-members.md)
- [废弃的成员函数](qfileinfo-obsolete.md)

**注意** 此类中所有函数均 [可重入](https://doc.qt.io/qt-5/threads-reentrancy.html)

## 公共成员函数

|返回类型|函数名|
|----:|:----|
||[QFileInfo](#QFileInfo::QFileInfo(const-QFileInfo-&fileinfo))(const QFileInfo &fileinfo)|
||[QFileInfo](#QFileInfo::QFileInfo(const-QDir-&dir,-const-QString-&file))(const QDir &dir, const QString &file)|
||[QFileInfo](#QFileInfo::QFileInfo(const-QFile-&file))(const QFile &file)|
||[QFileInfo](#QFileInfo::QFileInfo(const-QString-&file))(const QString &file)|
||[QFileInfo](#QFileInfo::QFileInfo())()|
|QFileInfo &|[operator=](#QFileInfo-&QFileInfo::operator=(QFileInfo-&&other))(QFileInfo &&other)|
|QFileInfo &|[operator=](#QFileInfo-&QFileInfo::operator=(const-QFileInfo-&fileinfo))(const QFileInfo &fileinfo)|
||[~QFileInfo](#QFileInfo::~QFileInfo())()|
|QDir|[absoluteDir](#QDir-QFileInfo::absoluteDir()-const)() const|
|QString|[absoluteFilePath](#QString-QFileInfo::absoluteFilePath()-const)() const|
|QString|[absolutePath](#QString-QFileInfo::absolutePath()-const)() const|
|QString|[baseName](#QString-QFileInfo::baseName()-const)() const|
|QDateTime|[birthTime](#QDateTime-QFileInfo::birthTime()-const)() const|
|QString|[bundleName](#QString-QFileInfo::bundleName()-const)() const|
|bool|[caching](#bool-QFileInfo::caching()-const)() const|
|QString|[canonicalFilePath](#QString-QFileInfo::canonicalFilePath()-const)() const|
|QString|[canonicalPath](#QString-QFileInfo::canonicalPath()-const)() const|
|QString|[completeBaseName](#QString-QFileInfo::completeBaseName()-const)() const|
|QString|[completeSuffix](#QString-QFileInfo::completeSuffix()-const)() const|
|QDir|[dir](#QDir-QFileInfo::dir()-const)() const|
|bool|[exists](#bool-QFileInfo::exists()-const)() const|
|QString|[fileName](#QString-QFileInfo::fileName()-const)() const|
|QString|[filePath](#QString-QFileInfo::filePath()-const)() const|
|QDateTime|[fileTime](#QDateTime-QFileInfo::fileTime(QFile::FileTime-time)-const)(QFile::FileTime time) const|
|QString|[group](#QString-QFileInfo::group()-const)() const|
|uint|[groupId](#uint-QFileInfo::groupId()-const)() const|
|bool|[isAbsolute](#bool-QFileInfo::isAbsolute()-const)() const|
|bool|[isBundle](#bool-QFileInfo::isBundle()-const)() const|
|bool|[isDir](#bool-QFileInfo::isDir()-const)() const|
|bool|[isExecutable](#bool-QFileInfo::isExecutable()-const)() const|
|bool|[isFile](#bool-QFileInfo::isFile()-const)() const|
|bool|[isHidden](#bool-QFileInfo::isHidden()-const)() const|
|bool|[isJunction](#bool-QFileInfo::isJunction()-const)() const|
|bool|[isNativePath](#bool-QFileInfo::isNativePath()-const)() const|
|bool|[isReadable](#bool-QFileInfo::isReadable()-const)() const|
|bool|[isRelative](#bool-QFileInfo::isRelative()-const)() const|
|bool|[isRoot](#bool-QFileInfo::isRoot()-const)() const|
|bool|[isShortcut](#bool-QFileInfo::isShortcut()-const)() const|
|bool|[isSymLink](#bool-QFileInfo::isSymLink()-const)() const|
|bool|[isSymbolicLink](#bool-QFileInfo::isSymbolicLink()-const)() const|
|bool|[isWritable](#bool-QFileInfo::isWritable()-const)() const|
|QDateTime|[lastModified](#QDateTime-QFileInfo::lastModified()-const)() const|
|QDateTime|[lastRead](#QDateTime-QFileInfo::lastRead()-const)() const|
|bool|[makeAbsolute](#bool-QFileInfo::makeAbsolute())()|
|QDateTime|[metadataChangeTime](#QDateTime-QFileInfo::metadataChangeTime()-const)() const|
|QString|[owner](#QString-QFileInfo::owner()-const)() const|
|uint|[ownerId](#uint-QFileInfo::ownerId()-const)() const|
|QString|[path](#QString-QFileInfo::path()-const)() const|
|bool|[permission](#bool-QFileInfo::permission(QFile::Permissions-permissions)-const)(QFile::Permissions permissions) const|
|QFile::Permissions|[permissions](#QFile::Permissions-QFileInfo::permissions()-const)() const|
|void|[refresh](#void-QFileInfo::refresh())() |
|void|[setCaching](#void-QFileInfo::setCaching(bool-enable))(bool enable)|
|void|[setFile](#void-QFileInfo::setFile(const-QString-&file))(const QString &file)|
|void|[setFile](#void-QFileInfo::setFile(const-QFile-&file))(const QFile &file)|
|void|[setFile](#void-QFileInfo::setFile(const-QDir-&dir,-const-QString-&file))(const QDir &dir, const QString &file)|
|qint64|[size](#qint64-QFileInfo::size()-const)() const|
|QString|[suffix](#QString-QFileInfo::suffix()-const)() const|
|void|[swap](#void-QFileInfo::swap(QFileInfo-&other))(QFileInfo &other)|
|QString|[symLinkTarget](#QString-QFileInfo::symLinkTarget()-const)() const|
|bool|[operator!=](#bool-QFileInfo::operator!=(const-QFileInfo-&fileinfo)-const)(const QFileInfo &fileinfo) const|
|bool|[operator==](#bool-QFileInfo::operator==(const-QFileInfo-&fileinfo)-const)(const QFileInfo &fileinfo) const|

## 静态公共成员函数

|返回类型|函数名|
|----:|:----|
|bool|[exists](#[static]bool-QFileInfo::exists(const-QString-&file))(const QString &file)|

## 相关非成员

|返回类型|函数名|
|----:|:----|
|typedef|[QFileInfoList](#QFileInfoList)|

## 详细描述

QFileInfo 可以获取任一文件的名字、路径、访问权限、是否是文件夹及是否是符号链接等信息，也可以获取文件的大小、上次修改时间、上次读取时间，还可以获取 Qt [资源文件](https://doc.qt.io/qt-5/resources.html) 的信息。

QFileInfo 可以表示相对路径也可以表示绝对路径。绝对路径以 “/” （windows 上以驱动符号）开头（例如 "/tmp/quartz"），相对路径以目录名或文件名开头，相对于当前工作目录（例如 "src/fatlib"）。可以用 [isRelative](#isRelative)() 检查一个 QFileInfo 表示的是相对路径还是绝对路径。可以用 [makeAbsolute](#makeAbsolute)() 将相对路径转为绝对路径。

QFileInfo 可以在构造函数中或稍后在 [setFile](#setFile)() 设置文件，可以用 [exists](#exists)() 查看文件是否存在，可以用 [size](#size)() 获取文件大小。

文件类型可以用 [isFile](#isFile)()、[isDir](#isDir)() 和 [isSymLink](#isSymLink)() 获取。[symLinkTarget](#symLinkTarget)() 函数提供了符号链接指向的文件名。

在 Unix 系统（包括 macOS 和 iOS），此类的属性的 getter 函数（例如获取时间或大小）返回的都是目标文件的值，而不是符号链接的（因为Unix透明地处理符号链接）。使用 [QFile](https://doc.qt.io/qt-5/qfile.html) 打开符号链接实际上是打开链接的目标。举例如下：

```cpp
#ifdef Q_OS_UNIX

QFileInfo info1("/home/bob/bin/untabify");
info1.isSymLink();          // returns true
info1.absoluteFilePath();   // returns "/home/bob/bin/untabify"
info1.size();               // returns 56201
info1.symLinkTarget();      // returns "/opt/pretty++/bin/untabify"

QFileInfo info2(info1.symLinkTarget());
info2.isSymLink();          // returns false
info2.absoluteFilePath();   // returns "/opt/pretty++/bin/untabify"
info2.size();               // returns 56201

#endif
```

在Windows上，快捷方式（“.lnk”文件）当前被视为符号链接。 和Unix系统一样，属性的 getter 返回目标文件的大小，而不是`.lnk`文件本身。 此行为已被弃用，并且可能会在Qt的未来版本中删除，此后，.lnk 文件将被视为常规文件。

```cpp
#ifdef Q_OS_WIN

QFileInfo info1("C:\\Documents and Settings\\Bob\\untabify.lnk");
info1.isSymLink();          // returns true
info1.absoluteFilePath();   // returns "C:/Documents and Settings/Bob/untabify.lnk"
info1.size();               // returns 743
info1.symLinkTarget();      // returns "C:/Pretty++/untabify"

QFileInfo info2(info1.symLinkTarget());
info2.isSymLink();          // returns false
info2.absoluteFilePath();   // returns "C:/Pretty++/untabify"
info2.size();               // returns 63942

#endif
```

Elements of the file's name can be extracted with [path](#path)() and [fileName](#fileName)(). The [fileName](#fileName)()'s parts can be extracted with [baseName](#baseName)(), [suffix](#suffix)() or [completeSuffix](#completeSuffix)(). QFileInfo objects to directories created by Qt classes will not have a trailing file separator. If you wish to use trailing separators in your own file info objects, just append one to the file name given to the constructors or [setFile](#setFile)().

涉及文件日期的函数：
[birthTime](#birthTime)()
[lastModified](#lastModified)()
[lastRead](#lastRead)()
[fileTime](#fileTime)()

涉及文件访问权限的函数：
[isReadable](#isReadable)()
[isWritable](#isWritable)()
[isExecutable](#isExecutable)()

涉及文件所有权的函数：
[owner](#owner)()
[ownerId](#ownerId)()
[group](#group)()
[groupId](#groupId)()

同时查验文件权限及所有权：
[permission](#permission)()

**注意** 在NTFS文件系统上，出于性能原因，默认情况下禁用所有权和权限检查。 要启用它，请包含以下行：

```cpp
extern Q_CORE_EXPORT int qt_ntfs_permission_lookup;
```

然后，通过将`qt_ntfs_permission_lookup`递增和递减 1 来打开和关闭权限检查。

```cpp
qt_ntfs_permission_lookup++; // 打开检查
qt_ntfs_permission_lookup--; // 再次关闭
```

### 性能问题

Some of QFileInfo's functions query the file system, but for performance reasons, some functions only operate on the file name itself. For example: To return the absolute path of a relative file name, [absolutePath](#absolutePath)() has to query the file system. The [path](#path)() function, however, can work on the file name directly, and so it is faster.

**注意** To speed up performance, QFileInfo caches information about the file.

Because files can be changed by other users or programs, or even by other parts of the same program, there is a function that refreshes the file information: [refresh](#refresh)(). If you want to switch off a QFileInfo's caching and force it to access the file system every time you request information from it call [setCaching](#setCaching)(false).

**另请参阅** [QDir](https://doc.qt.io/qt-5/qdir.html) and [QFile](https://doc.qt.io/qt-5/qfile.html).

## 成员函数文档

### QFileInfo::QFileInfo(const QFileInfo &fileinfo)

复制一个新的 QFileInfo。

### QFileInfo::QFileInfo(const [QDir](https://doc.qt.io/qt-5/qdir.html) &dir, const [QString](https://doc.qt.io/qt-5/qstring.html) &file)

构造一个新的 QFileInfo，表示指定 dir 目录中的 file 文件信息。

如果 dir 具有相对路径，则 QFileInfo 也将具有相对路径。

如果 file 是绝对路径，则 dir 指定的目录将被忽略。

**另请参阅** [isRelative](#isRelative)()

### QFileInfo::QFileInfo(const [QFile](https://doc.qt.io/qt-5/qfile.html) &file)

构造一个新的 QFileInfo，表示指定的 file 文件信息。

如果文件具有相对路径，则 QFileInfo 也将具有相对路径。

**另请参阅** [isRelative](#isRelative)()

### QFileInfo::QFileInfo(const [QString](https://doc.qt.io/qt-5/qstring.html) &file)

构造一个新的 QFileInfo，表示指定的 file 文件信息。file 可以包含绝对或相对路径。

**另请参阅** [setFile](#setFile)()，[isRelative](#isRelative)()，[QDir::setCurrent](https://doc.qt.io/qt-5/qdir.html#setCurrent)() 和 [QDir::isRelativePath](https://doc.qt.io/qt-5/qdir.html#isRelativePath)()

### QFileInfo::QFileInfo()

构造一个空的 QFileInfo 对象。

注意，空的 QFileInfo 对象不包含文件引用。

**另请参阅** [setFile](#setFile)()

### QFileInfo &QFileInfo::operator=(QFileInfo &&other)

移动构造函数。

该函数在 Qt 5.2 引入

### QFileInfo &QFileInfo::operator=(const QFileInfo &fileinfo)

赋值构造函数。

### QFileInfo::~QFileInfo()

析构函数。

### [QDir](https://doc.qt.io/qt-5/qdir.html) QFileInfo::absoluteDir() const

以 [QDir](https://doc.qt.io/qt-5/qdir.html) 对象的形式返回文件的绝对路径。

**另请参阅** [dir](#dir)()，[filePath](#filePath)()，[fileName](#fileName)() 和 [isRelative](#isRelative)()

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::absoluteFilePath() const

返回包含文件名的绝对路径。

绝对路径名由完整路径和文件名组成。 在Unix上，它将始终以根目录“ /”开头。 在Windows上，它将始终以“ D：/”开头，其中D是驱动器号，但未映射到驱动器号的网络共享除外，在这种情况下，路径将以“ // sharename /”开头。 `QFileInfo` 将大写驱动器号。

Returns an absolute path including the file name.

The absolute path name consists of the full path and the file name. On Unix this will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'. `QFileInfo` will uppercase drive letters. Note that [QDir](https://doc.qt.io/qt-5/qdir.html) does not do this. The code snippet below shows this.

```cpp
    QFileInfo fi("c:/temp/foo"); => fi.absoluteFilePath() => "C:/temp/foo"
```

This function returns the same as [filePath](#filePath)(), unless [isRelative](#isRelative)() is true. In contrast to [canonicalFilePath](#canonicalFilePath)(), symbolic links or redundant "." or ".." elements are not necessarily removed.

**警告** If [filePath](#filePath)() is empty the behavior of this function is undefined.

**另请参阅** [filePath](#filePath)(), [canonicalFilePath](#canonicalFilePath)(), and [isRelative](#isRelative)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::absolutePath() const

Returns a file's path absolute path. This doesn't include the file name.

On Unix the absolute path will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'.

In contrast to [canonicalPath](#canonicalPath)() symbolic links or redundant "." or ".." elements are not necessarily removed.

**警告** If [filePath](#filePath)() is empty the behavior of this function is undefined.

**另请参阅** [absoluteFilePath](#absoluteFilePath)(), [path](#path)(), [canonicalPath](#canonicalPath)(), [fileName](#fileName)(), and [isRelative](#isRelative)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::baseName() const

Returns the base name of the file without the path.

The base name consists of all characters in the file up to (but not including) the first '.' character.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.baseName();  // base = "archive"
```

The base name of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

**另请参阅** [fileName](#fileName)(), [suffix](#suffix)(), [completeSuffix](#completeSuffix)(), and [completeBaseName](#completeBaseName)()

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::birthTime() const

Returns the date and time when the file was created / born.

If the file birth time is not available, this function returns an invalid [QDateTime](https://doc.qt.io/qt-5/qdatetime.html)

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [lastModified](#lastModified)(), [lastRead](#lastRead)(), and [metadataChangeTime](#metadataChangeTime)()

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::bundleName() const

Returns the name of the bundle.

On macOS and iOS this returns the proper localized name for a bundle if the path [isBundle](#isBundle)(). On all other platforms an empty [QString](https://doc.qt.io/qt-5/qstring.html) is returned.

Example:

```cpp
QFileInfo fi("/Applications/Safari.app");
QString bundle = fi.bundleName();                // name = "Safari"
```

This function was introduced in Qt 4.3.

**另请参阅** [isBundle](#isBundle)(), [filePath](#filePath)(), [baseName](#baseName)(), and [suffix](#suffix)().

### bool QFileInfo::caching() const

Returns `true` if caching is enabled; otherwise returns `false`.

**另请参阅** [setCaching](#setCaching)() and [refresh](#refresh)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::canonicalFilePath() const

Returns the canonical path including the file name, i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalFilePath() returns an empty string.

**另请参阅** [filePath](#filePath)(), [absoluteFilePath](#absoluteFilePath)(), and [dir](#dir)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::canonicalPath() const

Returns the file's path canonical path (excluding the file name), i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalPath() returns an empty string.

**另请参阅** [path](#path)() and [absolutePath](#absolutePath)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::completeBaseName() const

Returns the complete base name of the file without the path.

The complete base name consists of all characters in the file up to (but not including) the last '.' character.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.completeBaseName();  // base = "archive.tar"
```

**另请参阅** [fileName](#fileName)(), [suffix](#suffix)(), [completeSuffix](#completeSuffix)(), and [baseName](#baseName)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::completeSuffix() const

Returns the complete suffix (extension) of the file.

The complete suffix consists of all characters in the file after (but not including) the first '.'.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.completeSuffix();  // ext = "tar.gz"
```

**另请参阅** [fileName](#fileName)(), [suffix](#suffix)(), [baseName](#baseName)(), and [completeBaseName](#completeBaseName)().

### [QDir](https://doc.qt.io/qt-5/qdir.html) QFileInfo::dir() const

Returns the path of the object's parent directory as a [QDir](https://doc.qt.io/qt-5/qdir.html) object.

**注意** The [QDir](https://doc.qt.io/qt-5/qdir.html) returned always corresponds to the object's parent directory, even if the `QFileInfo` represents a directory.

For each of the following, dir() returns the [QDir](https://doc.qt.io/qt-5/qdir.html) `"~/examples/191697"`.

```cpp
    QFileInfo fileInfo1("~/examples/191697/.");
    QFileInfo fileInfo2("~/examples/191697/..");
    QFileInfo fileInfo3("~/examples/191697/main.cpp");
```

For each of the following, dir() returns the [QDir](https://doc.qt.io/qt-5/qdir.html) `"."`.

```cpp
    QFileInfo fileInfo4(".");
    QFileInfo fileInfo5("..");
    QFileInfo fileInfo6("main.cpp");
```

**另请参阅** [absolutePath](#absolutePath)(), [filePath](#filePath)(), [fileName](#fileName)(), [isRelative](#isRelative)(), and [absoluteDir](#absoluteDir)().

### bool QFileInfo::exists() const

Returns `true` if the file exists; otherwise returns `false`.

**注意** If the file is a symlink that points to a non-existing file, false is returned.

### `[static]`bool QFileInfo::exists(const [QString](https://doc.qt.io/qt-5/qstring.html) &*file*)

Returns `true` if the *file* exists; otherwise returns `false`.

**注意** If *file* is a symlink that points to a non-existing file, false is returned.

**注意** Using this function is faster than using `QFileInfo(file).exists()` for file system access.

This function was introduced in Qt 5.2.

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::fileName() const

Returns the name of the file, excluding the path.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
QString name = fi.fileName();                // name = "archive.tar.gz"
```

Note that, if this `QFileInfo` object is given a path ending in a slash, the name of the file is considered empty.

**另请参阅** [isRelative](#isRelative)(), [filePath](#filePath)(), [baseName](#baseName)(), and [suffix](#suffix)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::filePath() const

Returns the file name, including the path (which may be absolute or relative).

**另请参阅** [absoluteFilePath](#absoluteFilePath)(), [canonicalFilePath](#canonicalFilePath)(), and [isRelative](#isRelative)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::fileTime([QFile::FileTime](https://doc.qt.io/qt-5/qfiledevice.html#FileTime-enum) *time*) const

Returns the file time specified by time. If the time cannot be determined, an invalid date time is returned.

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [QFile::FileTime](https://doc.qt.io/qt-5/qfiledevice.html#FileTime-enum) and [QDateTime::isValid](https://doc.qt.io/qt-5/qdatetime.html#isValid)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::group() const

Returns the group of the file. On Windows, on systems where files do not have groups, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds).

If the file is a symlink, this function returns the owning group of the target (not the symlink).

**另请参阅** [groupId](#groupId)(), [owner](#owner)(), and [ownerId](#ownerId)().

### [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) QFileInfo::groupId() const

Returns the id of the group the file belongs to.

On Windows and on systems where files do not have groups this function always returns (uint) -2.

If the file is a symlink, this function returns the id of the group owning the target (not the symlink).

**另请参阅** [group](#group)(), [owner](#owner)(), and [ownerId](#ownerId)().

### bool QFileInfo::isAbsolute() const

Returns `true` if the file path name is absolute, otherwise returns false if the path is relative.

**另请参阅** [isRelative](#isRelative)().

### bool QFileInfo::isBundle() const

Returns `true` if this object points to a bundle or to a symbolic link to a bundle on macOS and iOS; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is a bundle (not the symlink).

This function was introduced in Qt 4.3.

**另请参阅** [isDir](#isDir)(), [isSymLink](#isSymLink)(), and [isFile](#isFile)().

### bool QFileInfo::isDir() const

Returns `true` if this object points to a directory or to a symbolic link to a directory; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is a directory (not the symlink).

**另请参阅** [isFile](#isFile)(), [isSymLink](#isSymLink)(), and [isBundle](#isBundle)().

### bool QFileInfo::isExecutable() const

Returns `true` if the file is executable; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is executable (not the symlink).

**另请参阅** [isReadable](#isReadable)(), [isWritable](#isWritable)(), and [permission](#permission)().

### bool QFileInfo::isFile() const

Returns `true` if this object points to a file or to a symbolic link to a file. Returns `false` if the object points to something which isn't a file, such as a directory.

If the file is a symlink, this function returns true if the target is a regular file (not the symlink).

**另请参阅** [isDir](#isDir)(), [isSymLink](#isSymLink)(), and [isBundle](#isBundle)().

### bool QFileInfo::isHidden() const

Returns `true` if this is a `hidden` file; otherwise returns `false`.

**注意** This function returns `true` for the special entries "." and ".." on Unix, even though [QDir::entryList](https://doc.qt.io/qt-5/qdir.html#entryList) threats them as shown. And note that, since this function inspects the file name, on Unix it will inspect the name of the symlink, if this file is a symlink, not the target's name.

On Windows, this function returns `true` if the target file is hidden (not the symlink).

### bool QFileInfo::isJunction() const

Returns `true` if the object points to a junction; otherwise returns `false`.

Junctions only exist on Windows' NTFS file system, and are typically created by the `mklink` command. They can be thought of as symlinks for directories, and can only be created for absolute paths on the local volume.

This function was introduced in Qt 5.15.

### bool QFileInfo::isNativePath() const

Returns `true` if the file path can be used directly with native APIs. Returns `false` if the file is otherwise supported by a virtual file system inside Qt, such as [the Qt Resource System](https://doc.qt.io/qt-5/resources.html).

**注意** Native paths may still require conversion of path separators and character encoding, depending on platform and input requirements of the native API.

This function was introduced in Qt 5.0.

**另请参阅** [QDir::toNativeSeparators](https://doc.qt.io/qt-5/qdir.html#toNativeSeparators)(), [QFile::encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)(), [filePath](#filePath)(), [absoluteFilePath](#absoluteFilePath)(), and [canonicalFilePath](#canonicalFilePath)().

### bool QFileInfo::isReadable() const

Returns `true` if the user can read the file; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is readable (not the symlink).

**注意** If the [NTFS permissions](#ntfs-permissions) check has not been enabled, the result on Windows will merely reflect whether the file exists.

**另请参阅** [isWritable](#isWritable)(), [isExecutable](#isExecutable)(), and [permission](#permission)().

### bool QFileInfo::isRelative() const

Returns `true` if the file path name is relative, otherwise returns false if the path is absolute (e.g. under Unix a path is absolute if it begins with a "/").

**另请参阅** [isAbsolute](#isAbsolute)().

### bool QFileInfo::isRoot() const

Returns `true` if the object points to a directory or to a symbolic link to a directory, and that directory is the root directory; otherwise returns `false`.

### bool QFileInfo::isShortcut() const

Returns `true` if this object points to a shortcut; otherwise returns `false`.

Shortcuts only exist on Windows and are typically `.lnk` files. For instance, true will be returned for shortcuts (`*.lnk` files) on Windows, but false will be returned on Unix (including macOS and iOS).

The shortcut (.lnk) files are treated as regular files. Opening those will open the `.lnk` file itself. In order to open the file a shortcut references to, it must uses [symLinkTarget](#symLinkTarget)() on a shortcut.

**注意** Even if a shortcut (broken shortcut) points to a non existing file, isShortcut() returns true.

**另请参阅** [isFile](#isFile)(), [isDir](#isDir)(), [isSymbolicLink](#isSymbolicLink)(), and [symLinkTarget](#symLinkTarget)().

### bool QFileInfo::isSymLink() const

Returns `true` if this object points to a symbolic link or shortcut; otherwise returns `false`.

Symbolic links exist on Unix (including macOS and iOS) and Windows and are typically created by the `ln -s` or `mklink` commands, respectively. Opening a symbolic link effectively opens the [link's target](#symLinkTarget).

In addition, true will be returned for shortcuts (`*.lnk` files) on Windows. This behavior is deprecated and will likely change in a future version of Qt. Opening those will open the `.lnk` file itself.

Example:

```cpp
QFileInfo info(fileName);
if (info.isSymLink())
    fileName = info.symLinkTarget();
```

**注意** If the symlink points to a non existing file, [exists](#exists)() returns false.

**另请参阅** [isFile](#isFile)(), [isDir](#isDir)(), and [symLinkTarget](#symLinkTarget)().

### bool QFileInfo::isSymbolicLink() const

Returns `true` if this object points to a symbolic link; otherwise returns `false`.

Symbolic links exist on Unix (including macOS and iOS) and Windows (NTFS-symlink) and are typically created by the `ln -s` or `mklink` commands, respectively.

Unix handles symlinks transparently. Opening a symbolic link effectively opens the [link's target](#symLinkTarget).

In contrast to [isSymLink](#isSymLink)(), false will be returned for shortcuts (`*.lnk` files) on Windows. Use [QFileInfo::isShortcut](#isShortcut)() instead.

**注意** If the symlink points to a non existing file, [exists](#exists)() returns false.

**另请参阅** [isFile](#isFile)(), [isDir](#isDir)(), [isShortcut](#isShortcut)(), and [symLinkTarget](#symLinkTarget)().

### bool QFileInfo::isWritable() const

Returns `true` if the user can write to the file; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is writeable (not the symlink).

**注意** If the [NTFS permissions](#ntfs-permissions) check has not been enabled, the result on Windows will merely reflect whether the file is marked as Read Only.

**另请参阅** [isReadable](#isReadable)(), [isExecutable](#isExecutable)(), and [permission](#permission)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::lastModified() const

Returns the date and local time when the file was last modified.

If the file is a symlink, the time of the target file is returned (not the symlink).

**另请参阅** [birthTime](#birthTime)(), [lastRead](#lastRead)(), [metadataChangeTime](#metadataChangeTime)(), and [fileTime](#fileTime)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::lastRead() const

Returns the date and local time when the file was last read (accessed).

On platforms where this information is not available, returns the same as [lastModified](#lastModified)().

If the file is a symlink, the time of the target file is returned (not the symlink).

**另请参阅** [birthTime](#birthTime)(), [lastModified](#lastModified)(), [metadataChangeTime](#metadataChangeTime)(), and [fileTime](#fileTime)().

### bool QFileInfo::makeAbsolute()

Converts the file's path to an absolute path if it is not already in that form. Returns `true` to indicate that the path was converted; otherwise returns `false` to indicate that the path was already absolute.

**另请参阅** [filePath](#filePath)() and [isRelative](#isRelative)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::metadataChangeTime() const

Returns the date and time when the file metadata was changed. A metadata change occurs when the file is created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [lastModified](#lastModified)() and [lastRead](#lastRead)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::owner() const

Returns the owner of the file. On systems where files do not have owners, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds). On Windows, it will return an empty string unless the [NTFS permissions](#ntfs-permissions) check has been enabled.

If the file is a symlink, this function returns the owner of the target (not the symlink).

**另请参阅** [ownerId](#ownerId)(), [group](#group)(), and [groupId](#groupId)().

### [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) QFileInfo::ownerId() const

Returns the id of the owner of the file.

On Windows and on systems where files do not have owners this function returns ((uint) -2).

If the file is a symlink, this function returns the id of the owner of the target (not the symlink).

**另请参阅** [owner](#owner)(), [group](#group)(), and [groupId](#groupId)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::path() const

Returns the file's path. This doesn't include the file name.

Note that, if this `QFileInfo` object is given a path ending in a slash, the name of the file is considered empty and this function will return the entire path.

**另请参阅** [filePath](#filePath)(), [absolutePath](#absolutePath)(), [canonicalPath](#canonicalPath)(), [dir](#dir)(), [fileName](#fileName)(), and [isRelative](#isRelative)().

### bool QFileInfo::permission([QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) permissions) const

Tests for file permissions. The permissions argument can be several flags of type [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) OR-ed together to check for permission combinations.

On systems where files do not have permissions this function always returns `true`.

**注意** The result might be inaccurate on Windows if the [NTFS permissions](#ntfs-permissions) check has not been enabled.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
if (fi.permission(QFile::WriteUser | QFile::ReadGroup))
    qWarning("I can change the file; my group can read the file");
if (fi.permission(QFile::WriteGroup | QFile::WriteOther))
    qWarning("The group or others can change the file");
```

If the file is a symlink, this function checks the permissions of the target (not the symlink).

**另请参阅** [isReadable](#isReadable)(), [isWritable](#isWritable)(), and [isExecutable](#isExecutable)().

### [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFileInfo::permissions() const

Returns the complete OR-ed together combination of [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) for the file.

**注意** The result might be inaccurate on Windows if the [NTFS permissions](#ntfs-permissions) check has not been enabled.

If the file is a symlink, this function returns the permissions of the target (not the symlink).

### void QFileInfo::refresh()

Refreshes the information about the file, i.e. reads in information from the file system the next time a cached property is fetched.

### void QFileInfo::setCaching(bool enable)

If enable is true, enables caching of file information. If enable is false caching is disabled.

When caching is enabled, `QFileInfo` reads the file information from the file system the first time it's needed, but generally not later.

Caching is enabled by default.

**另请参阅** [refresh](#refresh)() and [caching](#caching)().

### void QFileInfo::setFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &file)

Sets the file that the `QFileInfo` provides information about to file.

The file can also include an absolute or relative file path. Absolute paths begin with the directory separator (e.g. "/" under Unix) or a drive specification (under Windows). Relative file names begin with a directory name or a file name and specify a path relative to the current directory.

Example:

```cpp
QString absolute = "/local/bin";
QString relative = "local/bin";
QFileInfo absFile(absolute);
QFileInfo relFile(relative);

QDir::setCurrent(QDir::rootPath());
// absFile and relFile now point to the same file

QDir::setCurrent("/tmp");
// absFile now points to "/local/bin",
// while relFile points to "/tmp/local/bin"
```

**另请参阅** [isFile](#isFile)(), [isRelative](#isRelative)(), [QDir::setCurrent](https://doc.qt.io/qt-5/qdir.html#setCurrent)(), and [QDir::isRelativePath](https://doc.qt.io/qt-5/qdir.html#isRelativePath)().

### void QFileInfo::setFile(const [QFile](https://doc.qt.io/qt-5/qfile.html) &file)

This is an overloaded function.

Sets the file that the `QFileInfo` provides information about to file.

If *file* includes a relative path, the `QFileInfo` will also have a relative path.

**另请参阅** [isRelative](#isRelative)().

### void QFileInfo::setFile(const [QDir](https://doc.qt.io/qt-5/qdir.html) &dir, const [QString](https://doc.qt.io/qt-5/qstring.html) &file)

This is an overloaded function.

Sets the file that the `QFileInfo` provides information about to file in directory dir.

If file includes a relative path, the `QFileInfo` will also have a relative path.

**另请参阅** [isRelative](#isRelative)().

### [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QFileInfo::size() const

Returns the file size in bytes. If the file does not exist or cannot be fetched, 0 is returned.

If the file is a symlink, the size of the target file is returned (not the symlink).

**另请参阅** [exists](#exists)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::suffix() const

Returns the suffix (extension) of the file.

The suffix consists of all characters in the file after (but not including) the last '.'.

Example:

```cpp
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.suffix();  // ext = "gz"
```

The suffix of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

**另请参阅** [fileName](#fileName)(), [completeSuffix](#completeSuffix)(), [baseName](#baseName)(), and [completeBaseName](#completeBaseName)().

### void QFileInfo::swap(QFileInfo &other)

Swaps this file info with other. This function is very fast and never fails.

This function was introduced in Qt 5.0.

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::symLinkTarget() const

Returns the absolute path to the file or directory a symbolic link points to, or an empty string if the object isn't a symbolic link.

This name may not represent an existing file; it is only a string. [QFileInfo::exists](#exists)() returns `true` if the symlink points to an existing file.

This function was introduced in Qt 4.2.

**另请参阅** [exists](#exists)(), [isSymLink](#isSymLink)(), [isDir](#isDir)(), and [isFile](#isFile)().

### bool QFileInfo::operator!=(const QFileInfo &fileinfo) const

Returns `true` if this `QFileInfo` object refers to a different file than the one specified by fileinfo; otherwise returns `false`.

**另请参阅** [operator==](#operator-eq-eq)().

### bool QFileInfo::operator==(const QFileInfo &fileinfo) const

Returns `true` if this `QFileInfo` object refers to a file in the same location as fileinfo; otherwise returns `false`.

Note that the result of comparing two empty `QFileInfo` objects, containing no file references (file paths that do not exist or are empty), is undefined.

**警告** This will not compare two different symbolic links pointing to the same file.

**警告** Long and short file names that refer to the same file on Windows are treated as if they referred to different files.

**另请参阅** [operator!=](#operator-not-eq)()

### QFileInfoList

等同于 [QList](https://doc.qt.io/qt-5/qlist.html)\<`QFileInfo`>
