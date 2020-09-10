# QFileInfo 类

QFileInfo 类用于系统无关的文件信息。[更多内容...](#%E8%AF%A6%E7%BB%86%E6%8F%8F%E8%BF%B0)

|属性|方法|
|----:|:----|
|头文件:|`#include <QFileInfo>`|
|qmake:|`QT += core`|

- [列出所有成员函数，包括继承的成员函数](https://doc.qt.io/qt-5/qfileinfo-members.html)
- [废弃的成员函数](https://doc.qt.io/qt-5/qfileinfo-obsolete.html)

**注意** 此类中所有函数均 [可重入](https://doc.qt.io/qt-5/threads-reentrancy.html)

## 公共成员函数

|返回类型|函数名|
|----:|:----|
||[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#QFileInfo-5)(const QFileInfo &fileinfo)|
||[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#QFileInfo-4)(const QDir &dir, const QString &file)|
||[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#QFileInfo-3)(const QFile &file)|
||[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#QFileInfo-2)(const QString &file)|
||[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#QFileInfo-1)()|
|QFileInfo &|[operator=](https://doc.qt.io/qt-5/qfileinfo.html#operator-eq-1)(QFileInfo &&other)|
|QFileInfo &|[operator=](https://doc.qt.io/qt-5/qfileinfo.html#operator-eq)(const QFileInfo &fileinfo)|
||[~QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html#dtor.QFileInfo)()|
|QDir|[absoluteDir](https://doc.qt.io/qt-5/qfileinfo.html#absoluteDir)() const|
|QString|[absoluteFilePath](https://doc.qt.io/qt-5/qfileinfo.html#absoluteFilePath)() const|
|QString|[absolutePath](https://doc.qt.io/qt-5/qfileinfo.html#absolutePath)() const|
|QString|[baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)() const|
|QDateTime|[birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)() const|
|QString|[bundleName](https://doc.qt.io/qt-5/qfileinfo.html#bundleName)() const|
|bool|[caching](https://doc.qt.io/qt-5/qfileinfo.html#caching)() const|
|QString|[canonicalFilePath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalFilePath)() const|
|QString|[canonicalPath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalPath)() const|
|QString|[completeBaseName](https://doc.qt.io/qt-5/qfileinfo.html#completeBaseName)() const|
|QString|[completeSuffix](https://doc.qt.io/qt-5/qfileinfo.html#completeSuffix)() const|
|QDir|[dir](https://doc.qt.io/qt-5/qfileinfo.html#dir)() const|
|bool|[exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)() const|
|QString|[fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)() const|
|QString|[filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)() const|
|QDateTime|[fileTime](https://doc.qt.io/qt-5/qfileinfo.html#fileTime)(QFile::FileTime time) const|
|QString|[group](https://doc.qt.io/qt-5/qfileinfo.html#group)() const|
|uint|[groupId](https://doc.qt.io/qt-5/qfileinfo.html#groupId)() const|
|bool|[isAbsolute](https://doc.qt.io/qt-5/qfileinfo.html#isAbsolute)() const|
|bool|[isBundle](https://doc.qt.io/qt-5/qfileinfo.html#isBundle)() const|
|bool|[isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)() const|
|bool|[isExecutable](https://doc.qt.io/qt-5/qfileinfo.html#isExecutable)() const|
|bool|[isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)() const|
|bool|[isHidden](https://doc.qt.io/qt-5/qfileinfo.html#isHidden)() const|
|bool|[isJunction](https://doc.qt.io/qt-5/qfileinfo.html#isJunction)() const|
|bool|[isNativePath](https://doc.qt.io/qt-5/qfileinfo.html#isNativePath)() const|
|bool|[isReadable](https://doc.qt.io/qt-5/qfileinfo.html#isReadable)() const|
|bool|[isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)() const|
|bool|[isRoot](https://doc.qt.io/qt-5/qfileinfo.html#isRoot)() const|
|bool|[isShortcut](https://doc.qt.io/qt-5/qfileinfo.html#isShortcut)() const|
|bool|[isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)() const|
|bool|[isSymbolicLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymbolicLink)() const|
|bool|[isWritable](https://doc.qt.io/qt-5/qfileinfo.html#isWritable)() const|
|QDateTime|[lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)() const|
|QDateTime|[lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)() const|
|bool|[makeAbsolute](https://doc.qt.io/qt-5/qfileinfo.html#makeAbsolute)()|
|QDateTime|[metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)() const|
|QString|[owner](https://doc.qt.io/qt-5/qfileinfo.html#owner)() const|
|uint|[ownerId](https://doc.qt.io/qt-5/qfileinfo.html#ownerId)() const|
|QString|[path](https://doc.qt.io/qt-5/qfileinfo.html#path)() const|
|bool|[permission](https://doc.qt.io/qt-5/qfileinfo.html#permission)(QFile::Permissions permissions) const|
|QFile::Permissions|[permissions](https://doc.qt.io/qt-5/qfileinfo.html#permissions)() const|
|void|[refresh](https://doc.qt.io/qt-5/qfileinfo.html#refresh)() |
|void|[setCaching](https://doc.qt.io/qt-5/qfileinfo.html#setCaching)(bool enable)|
|void|[setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile)(const QString &file)|
|void|[setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile-1)(const QFile &file)|
|void|[setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile-2)(const QDir &dir, const QString &file)|
|qint64|[size](https://doc.qt.io/qt-5/qfileinfo.html#size)() const|
|QString|[suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)() const|
|void|[swap](https://doc.qt.io/qt-5/qfileinfo.html#swap)(QFileInfo &other)|
|QString|[symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)() const|
|bool|[operator!=](https://doc.qt.io/qt-5/qfileinfo.html#operator-not-eq)(const QFileInfo &fileinfo) const|
|bool|[operator==](https://doc.qt.io/qt-5/qfileinfo.html#operator-eq-eq)(const QFileInfo &fileinfo) const|

## 静态公共成员函数

|返回类型|函数名|
|----:|:----|
|bool|[exists](https://doc.qt.io/qt-5/qfileinfo.html#exists-1)(const QString &file)|

## 相关非成员

|返回类型|函数名|
|----:|:----|
|typedef|[QFileInfoList](#QFileInfoList)|

## 详细描述

QFileInfo 可以获取任一文件的名字、路径、访问权限、是否是文件夹及是否是符号链接等信息，也可以获取文件的大小、上次修改时间、上次读取时间，还可以获取 Qt [资源文件](https://doc.qt.io/qt-5/resources.html) 的信息。

QFileInfo 可以表示相对路径也可以表示绝对路径。绝对路径以 “/” （windows 上以驱动符号）开头（例如 "/tmp/quartz"），相对路径以目录名或文件名开头，相对于当前工作目录（例如 "src/fatlib"）。可以用 [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)() 检查一个 QFileInfo 表示的是相对路径还是绝对路径。可以用 [makeAbsolute](https://doc.qt.io/qt-5/qfileinfo.html#makeAbsolute)() 将相对路径转为绝对路径。

QFileInfo 可以在构造函数中或稍后在 [setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile)() 设置文件，可以用 [exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)() 查看文件是否存在，可以用 [size](https://doc.qt.io/qt-5/qfileinfo.html#size)() 获取文件大小。

文件类型可以用 [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)()、[isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)() 和 [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)() 获取。[symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)() 函数提供了符号链接指向的文件名。

在 Unix 系统（包括 macOS 和 iOS），此类的属性的 getter 函数（例如获取时间或大小）返回的都是目标文件的值，而不是符号链接的（因为Unix透明地处理符号链接）。使用 [QFile](https://doc.qt.io/qt-5/qfile.html) 打开符号链接实际上是打开链接的目标。举例如下：

```
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

```
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

Elements of the file's name can be extracted with [path](https://doc.qt.io/qt-5/qfileinfo.html#path)() and [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(). The [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)()'s parts can be extracted with [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)(), [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)() or [completeSuffix](https://doc.qt.io/qt-5/qfileinfo.html#completeSuffix)(). QFileInfo objects to directories created by Qt classes will not have a trailing file separator. If you wish to use trailing separators in your own file info objects, just append one to the file name given to the constructors or [setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile)().

The file's dates are returned by [birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)(), [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)(), [lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)() and [fileTime](https://doc.qt.io/qt-5/qfileinfo.html#fileTime)(). Information about the file's access permissions is obtained with [isReadable](https://doc.qt.io/qt-5/qfileinfo.html#isReadable)(), [isWritable](https://doc.qt.io/qt-5/qfileinfo.html#isWritable)() and [isExecutable](https://doc.qt.io/qt-5/qfileinfo.html#isExecutable)(). The file's ownership is available from [owner](https://doc.qt.io/qt-5/qfileinfo.html#owner)(), [ownerId](https://doc.qt.io/qt-5/qfileinfo.html#ownerId)(), [group](https://doc.qt.io/qt-5/qfileinfo.html#group)() and [groupId](https://doc.qt.io/qt-5/qfileinfo.html#groupId)(). You can examine a file's permissions and ownership in a single statement using the [permission](https://doc.qt.io/qt-5/qfileinfo.html#permission)() function.



**注意** On NTFS file systems, ownership and permissions checking is disabled by default for performance reasons. To enable it, include the following line:

```
extern Q_CORE_EXPORT int qt_ntfs_permission_lookup;
```

Permission checking is then turned on and off by incrementing and decrementing `qt_ntfs_permission_lookup` by 1.

```
qt_ntfs_permission_lookup++; // turn checking on
qt_ntfs_permission_lookup--; // turn it off again
```



### 性能问题

Some of QFileInfo's functions query the file system, but for performance reasons, some functions only operate on the file name itself. For example: To return the absolute path of a relative file name, [absolutePath](https://doc.qt.io/qt-5/qfileinfo.html#absolutePath)() has to query the file system. The [path](https://doc.qt.io/qt-5/qfileinfo.html#path)() function, however, can work on the file name directly, and so it is faster.

**注意** To speed up performance, QFileInfo caches information about the file.

Because files can be changed by other users or programs, or even by other parts of the same program, there is a function that refreshes the file information: [refresh](https://doc.qt.io/qt-5/qfileinfo.html#refresh)(). If you want to switch off a QFileInfo's caching and force it to access the file system every time you request information from it call [setCaching](https://doc.qt.io/qt-5/qfileinfo.html#setCaching)(false).

**See also** [QDir](https://doc.qt.io/qt-5/qdir.html) and [QFile](https://doc.qt.io/qt-5/qfile.html).

## 成员函数文档

### QFileInfo::QFileInfo(const QFileInfo &fileinfo)

Constructs a new QFileInfo that is a copy of the given *fileinfo*.

### QFileInfo::QFileInfo(const [QDir](https://doc.qt.io/qt-5/qdir.html) &dir, const [QString](https://doc.qt.io/qt-5/qstring.html) &file)

Constructs a new QFileInfo that gives information about the given *file* in the directory *dir*.

If *dir* has a relative path, the QFileInfo will also have a relative path.

If *file* is an absolute path, then the directory specified by *dir* will be disregarded.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### QFileInfo::QFileInfo(const [QFile](https://doc.qt.io/qt-5/qfile.html) &*file*)

Constructs a new QFileInfo that gives information about file *file*.

If the *file* has a relative path, the QFileInfo will also have a relative path.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### QFileInfo::QFileInfo(const [QString](https://doc.qt.io/qt-5/qstring.html) &*file*)

Constructs a new QFileInfo that gives information about the given file. The *file* can also include an absolute or relative path.

**另请参阅** [setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile)(), [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)(), [QDir::setCurrent](https://doc.qt.io/qt-5/qdir.html#setCurrent)(), and [QDir::isRelativePath](https://doc.qt.io/qt-5/qdir.html#isRelativePath)().

### QFileInfo::QFileInfo()

Constructs an empty QFileInfo object.

Note that an empty QFileInfo object contain no file reference.

**另请参阅** [setFile](https://doc.qt.io/qt-5/qfileinfo.html#setFile)().

### QFileInfo &QFileInfo::operator=(QFileInfo &&*other*)

Move-assigns *other* to this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) instance.

This function was introduced in Qt 5.2.

### QFileInfo &QFileInfo::operator=(const QFileInfo &*fileinfo*)

Makes a copy of the given *fileinfo* and assigns it to this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html).

### QFileInfo::~QFileInfo()

Destroys the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) and frees its resources.

### [QDir](https://doc.qt.io/qt-5/qdir.html) QFileInfo::absoluteDir() const

Returns the file's absolute path as a [QDir](https://doc.qt.io/qt-5/qdir.html) object.

**另请参阅** [dir](https://doc.qt.io/qt-5/qfileinfo.html#dir)(), [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::absoluteFilePath() const

Returns an absolute path including the file name.

The absolute path name consists of the full path and the file name. On Unix this will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'. [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) will uppercase drive letters. Note that [QDir](https://doc.qt.io/qt-5/qdir.html) does not do this. The code snippet below shows this.

```
    QFileInfo fi("c:/temp/foo"); => fi.absoluteFilePath() => "C:/temp/foo"
```

This function returns the same as [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), unless [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)() is true. In contrast to [canonicalFilePath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalFilePath)(), symbolic links or redundant "." or ".." elements are not necessarily removed.

**警告** If [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)() is empty the behavior of this function is undefined.

**另请参阅** [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [canonicalFilePath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalFilePath)(), and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::absolutePath() const

Returns a file's path absolute path. This doesn't include the file name.

On Unix the absolute path will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'.

In contrast to [canonicalPath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalPath)() symbolic links or redundant "." or ".." elements are not necessarily removed.

**警告** If [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)() is empty the behavior of this function is undefined.

**另请参阅** [absoluteFilePath](https://doc.qt.io/qt-5/qfileinfo.html#absoluteFilePath)(), [path](https://doc.qt.io/qt-5/qfileinfo.html#path)(), [canonicalPath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalPath)(), [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::baseName() const

Returns the base name of the file without the path.

The base name consists of all characters in the file up to (but not including) the *first* '.' character.

Example:

```
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.baseName();  // base = "archive"
```

The base name of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

**另请参阅** [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)(), [completeSuffix](https://doc.qt.io/qt-5/qfileinfo.html#completeSuffix)(), and [completeBaseName](https://doc.qt.io/qt-5/qfileinfo.html#completeBaseName)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::birthTime() const

Returns the date and time when the file was created / born.

If the file birth time is not available, this function returns an invalid [QDateTime](https://doc.qt.io/qt-5/qdatetime.html).

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)(), [lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)(), and [metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::bundleName() const

Returns the name of the bundle.

On macOS and iOS this returns the proper localized name for a bundle if the path [isBundle](https://doc.qt.io/qt-5/qfileinfo.html#isBundle)(). On all other platforms an empty [QString](https://doc.qt.io/qt-5/qstring.html) is returned.

Example:

```
QFileInfo fi("/Applications/Safari.app");
QString bundle = fi.bundleName();                // name = "Safari"
```

This function was introduced in Qt 4.3.

**另请参阅** [isBundle](https://doc.qt.io/qt-5/qfileinfo.html#isBundle)(), [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)(), and [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)().

### bool QFileInfo::caching() const

Returns `true` if caching is enabled; otherwise returns `false`.

**另请参阅** [setCaching](https://doc.qt.io/qt-5/qfileinfo.html#setCaching)() and [refresh](https://doc.qt.io/qt-5/qfileinfo.html#refresh)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::canonicalFilePath() const

Returns the canonical path including the file name, i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalFilePath() returns an empty string.

**另请参阅** [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [absoluteFilePath](https://doc.qt.io/qt-5/qfileinfo.html#absoluteFilePath)(), and [dir](https://doc.qt.io/qt-5/qfileinfo.html#dir)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::canonicalPath() const

Returns the file's path canonical path (excluding the file name), i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalPath() returns an empty string.

**另请参阅** [path](https://doc.qt.io/qt-5/qfileinfo.html#path)() and [absolutePath](https://doc.qt.io/qt-5/qfileinfo.html#absolutePath)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::completeBaseName() const

Returns the complete base name of the file without the path.

The complete base name consists of all characters in the file up to (but not including) the *last* '.' character.

Example:

```
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.completeBaseName();  // base = "archive.tar"
```

**另请参阅** [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)(), [completeSuffix](https://doc.qt.io/qt-5/qfileinfo.html#completeSuffix)(), and [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::completeSuffix() const

Returns the complete suffix (extension) of the file.

The complete suffix consists of all characters in the file after (but not including) the first '.'.

Example:

```
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.completeSuffix();  // ext = "tar.gz"
```

**另请参阅** [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)(), [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)(), and [completeBaseName](https://doc.qt.io/qt-5/qfileinfo.html#completeBaseName)().

### [QDir](https://doc.qt.io/qt-5/qdir.html) QFileInfo::dir() const

Returns the path of the object's parent directory as a [QDir](https://doc.qt.io/qt-5/qdir.html) object.

**注意** The [QDir](https://doc.qt.io/qt-5/qdir.html) returned always corresponds to the object's parent directory, even if the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) represents a directory.

For each of the following, dir() returns the [QDir](https://doc.qt.io/qt-5/qdir.html) `"~/examples/191697"`.

```
    QFileInfo fileInfo1("~/examples/191697/.");
    QFileInfo fileInfo2("~/examples/191697/..");
    QFileInfo fileInfo3("~/examples/191697/main.cpp");
```

For each of the following, dir() returns the [QDir](https://doc.qt.io/qt-5/qdir.html) `"."`.

```
    QFileInfo fileInfo4(".");
    QFileInfo fileInfo5("..");
    QFileInfo fileInfo6("main.cpp");
```

**另请参阅** [absolutePath](https://doc.qt.io/qt-5/qfileinfo.html#absolutePath)(), [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)(), and [absoluteDir](https://doc.qt.io/qt-5/qfileinfo.html#absoluteDir)().

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

```
QFileInfo fi("/tmp/archive.tar.gz");
QString name = fi.fileName();                // name = "archive.tar.gz"
```

Note that, if this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) object is given a path ending in a slash, the name of the file is considered empty.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)(), [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)(), and [suffix](https://doc.qt.io/qt-5/qfileinfo.html#suffix)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::filePath() const

Returns the file name, including the path (which may be absolute or relative).

**另请参阅** [absoluteFilePath](https://doc.qt.io/qt-5/qfileinfo.html#absoluteFilePath)(), [canonicalFilePath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalFilePath)(), and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::fileTime([QFile::FileTime](https://doc.qt.io/qt-5/qfiledevice.html#FileTime-enum) *time*) const

Returns the file time specified by *time*. If the time cannot be determined, an invalid date time is returned.

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [QFile::FileTime](https://doc.qt.io/qt-5/qfiledevice.html#FileTime-enum) and [QDateTime::isValid](https://doc.qt.io/qt-5/qdatetime.html#isValid)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::group() const

Returns the group of the file. On Windows, on systems where files do not have groups, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds).

If the file is a symlink, this function returns the owning group of the target (not the symlink).

**另请参阅** [groupId](https://doc.qt.io/qt-5/qfileinfo.html#groupId)(), [owner](https://doc.qt.io/qt-5/qfileinfo.html#owner)(), and [ownerId](https://doc.qt.io/qt-5/qfileinfo.html#ownerId)().

### [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) QFileInfo::groupId() const

Returns the id of the group the file belongs to.

On Windows and on systems where files do not have groups this function always returns (uint) -2.

If the file is a symlink, this function returns the id of the group owning the target (not the symlink).

**另请参阅** [group](https://doc.qt.io/qt-5/qfileinfo.html#group)(), [owner](https://doc.qt.io/qt-5/qfileinfo.html#owner)(), and [ownerId](https://doc.qt.io/qt-5/qfileinfo.html#ownerId)().

### bool QFileInfo::isAbsolute() const

Returns `true` if the file path name is absolute, otherwise returns false if the path is relative.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### bool QFileInfo::isBundle() const

Returns `true` if this object points to a bundle or to a symbolic link to a bundle on macOS and iOS; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is a bundle (not the symlink).

This function was introduced in Qt 4.3.

**另请参阅** [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)(), and [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)().

### bool QFileInfo::isDir() const

Returns `true` if this object points to a directory or to a symbolic link to a directory; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is a directory (not the symlink).

**另请参阅** [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)(), [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)(), and [isBundle](https://doc.qt.io/qt-5/qfileinfo.html#isBundle)().

### bool QFileInfo::isExecutable() const

Returns `true` if the file is executable; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is executable (not the symlink).

**另请参阅** [isReadable](https://doc.qt.io/qt-5/qfileinfo.html#isReadable)(), [isWritable](https://doc.qt.io/qt-5/qfileinfo.html#isWritable)(), and [permission](https://doc.qt.io/qt-5/qfileinfo.html#permission)().

### bool QFileInfo::isFile() const

Returns `true` if this object points to a file or to a symbolic link to a file. Returns `false` if the object points to something which isn't a file, such as a directory.

If the file is a symlink, this function returns true if the target is a regular file (not the symlink).

**另请参阅** [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)(), and [isBundle](https://doc.qt.io/qt-5/qfileinfo.html#isBundle)().

### bool QFileInfo::isHidden() const

Returns `true` if this is a `hidden' file; otherwise returns `false`.

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

**另请参阅** [QDir::toNativeSeparators](https://doc.qt.io/qt-5/qdir.html#toNativeSeparators)(), [QFile::encodeName](https://doc.qt.io/qt-5/qfile.html#encodeName)(), [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [absoluteFilePath](https://doc.qt.io/qt-5/qfileinfo.html#absoluteFilePath)(), and [canonicalFilePath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalFilePath)().

### bool QFileInfo::isReadable() const

Returns `true` if the user can read the file; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is readable (not the symlink).

**注意** If the [NTFS permissions](https://doc.qt.io/qt-5/qfileinfo.html#ntfs-permissions) check has not been enabled, the result on Windows will merely reflect whether the file exists.

**另请参阅** [isWritable](https://doc.qt.io/qt-5/qfileinfo.html#isWritable)(), [isExecutable](https://doc.qt.io/qt-5/qfileinfo.html#isExecutable)(), and [permission](https://doc.qt.io/qt-5/qfileinfo.html#permission)().

### bool QFileInfo::isRelative() const

Returns `true` if the file path name is relative, otherwise returns false if the path is absolute (e.g. under Unix a path is absolute if it begins with a "/").

**另请参阅** [isAbsolute](https://doc.qt.io/qt-5/qfileinfo.html#isAbsolute)().

### bool QFileInfo::isRoot() const

Returns `true` if the object points to a directory or to a symbolic link to a directory, and that directory is the root directory; otherwise returns `false`.

### bool QFileInfo::isShortcut() const

Returns `true` if this object points to a shortcut; otherwise returns `false`.

Shortcuts only exist on Windows and are typically `.lnk` files. For instance, true will be returned for shortcuts (`*.lnk` files) on Windows, but false will be returned on Unix (including macOS and iOS).

The shortcut (.lnk) files are treated as regular files. Opening those will open the `.lnk` file itself. In order to open the file a shortcut references to, it must uses [symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)() on a shortcut.

**注意** Even if a shortcut (broken shortcut) points to a non existing file, isShortcut() returns true.

**另请参阅** [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)(), [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), [isSymbolicLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymbolicLink)(), and [symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)().

### bool QFileInfo::isSymLink() const

Returns `true` if this object points to a symbolic link or shortcut; otherwise returns `false`.

Symbolic links exist on Unix (including macOS and iOS) and Windows and are typically created by the `ln -s` or `mklink` commands, respectively. Opening a symbolic link effectively opens the [link's target](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget).

In addition, true will be returned for shortcuts (`*.lnk` files) on Windows. This behavior is deprecated and will likely change in a future version of Qt. Opening those will open the `.lnk` file itself.

Example:

```
QFileInfo info(fileName);
if (info.isSymLink())
    fileName = info.symLinkTarget();
```

**注意** If the symlink points to a non existing file, [exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)() returns false.

**另请参阅** [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)(), [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), and [symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)().

### bool QFileInfo::isSymbolicLink() const

Returns `true` if this object points to a symbolic link; otherwise returns `false`.

Symbolic links exist on Unix (including macOS and iOS) and Windows (NTFS-symlink) and are typically created by the `ln -s` or `mklink` commands, respectively.

Unix handles symlinks transparently. Opening a symbolic link effectively opens the [link's target](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget).

In contrast to [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)(), false will be returned for shortcuts (`*.lnk` files) on Windows. Use [QFileInfo::isShortcut](https://doc.qt.io/qt-5/qfileinfo.html#isShortcut)() instead.

**注意** If the symlink points to a non existing file, [exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)() returns false.

**另请参阅** [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)(), [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), [isShortcut](https://doc.qt.io/qt-5/qfileinfo.html#isShortcut)(), and [symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)().

### bool QFileInfo::isWritable() const

Returns `true` if the user can write to the file; otherwise returns `false`.

If the file is a symlink, this function returns true if the target is writeable (not the symlink).

**注意** If the [NTFS permissions](https://doc.qt.io/qt-5/qfileinfo.html#ntfs-permissions) check has not been enabled, the result on Windows will merely reflect whether the file is marked as Read Only.

**另请参阅** [isReadable](https://doc.qt.io/qt-5/qfileinfo.html#isReadable)(), [isExecutable](https://doc.qt.io/qt-5/qfileinfo.html#isExecutable)(), and [permission](https://doc.qt.io/qt-5/qfileinfo.html#permission)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::lastModified() const

Returns the date and local time when the file was last modified.

If the file is a symlink, the time of the target file is returned (not the symlink).

**另请参阅** [birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)(), [lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)(), [metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)(), and [fileTime](https://doc.qt.io/qt-5/qfileinfo.html#fileTime)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::lastRead() const

Returns the date and local time when the file was last read (accessed).

On platforms where this information is not available, returns the same as [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)().

If the file is a symlink, the time of the target file is returned (not the symlink).

**另请参阅** [birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)(), [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)(), [metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)(), and [fileTime](https://doc.qt.io/qt-5/qfileinfo.html#fileTime)().

### bool QFileInfo::makeAbsolute()

Converts the file's path to an absolute path if it is not already in that form. Returns `true` to indicate that the path was converted; otherwise returns `false` to indicate that the path was already absolute.

**另请参阅** [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)() and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::metadataChangeTime() const

Returns the date and time when the file metadata was changed. A metadata change occurs when the file is created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).

If the file is a symlink, the time of the target file is returned (not the symlink).

This function was introduced in Qt 5.10.

**另请参阅** [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)() and [lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::owner() const

Returns the owner of the file. On systems where files do not have owners, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds). On Windows, it will return an empty string unless the [NTFS permissions](https://doc.qt.io/qt-5/qfileinfo.html#ntfs-permissions) check has been enabled.

If the file is a symlink, this function returns the owner of the target (not the symlink).

**另请参阅** [ownerId](https://doc.qt.io/qt-5/qfileinfo.html#ownerId)(), [group](https://doc.qt.io/qt-5/qfileinfo.html#group)(), and [groupId](https://doc.qt.io/qt-5/qfileinfo.html#groupId)().

### [uint](https://doc.qt.io/qt-5/qtglobal.html#uint-typedef) QFileInfo::ownerId() const

Returns the id of the owner of the file.

On Windows and on systems where files do not have owners this function returns ((uint) -2).

If the file is a symlink, this function returns the id of the owner of the target (not the symlink).

**另请参阅** [owner](https://doc.qt.io/qt-5/qfileinfo.html#owner)(), [group](https://doc.qt.io/qt-5/qfileinfo.html#group)(), and [groupId](https://doc.qt.io/qt-5/qfileinfo.html#groupId)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::path() const

Returns the file's path. This doesn't include the file name.

Note that, if this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) object is given a path ending in a slash, the name of the file is considered empty and this function will return the entire path.

**另请参阅** [filePath](https://doc.qt.io/qt-5/qfileinfo.html#filePath)(), [absolutePath](https://doc.qt.io/qt-5/qfileinfo.html#absolutePath)(), [canonicalPath](https://doc.qt.io/qt-5/qfileinfo.html#canonicalPath)(), [dir](https://doc.qt.io/qt-5/qfileinfo.html#dir)(), [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), and [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### bool QFileInfo::permission([QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) *permissions*) const

Tests for file permissions. The *permissions* argument can be several flags of type [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) OR-ed together to check for permission combinations.

On systems where files do not have permissions this function always returns `true`.

**注意** The result might be inaccurate on Windows if the [NTFS permissions](https://doc.qt.io/qt-5/qfileinfo.html#ntfs-permissions) check has not been enabled.

Example:

```
QFileInfo fi("/tmp/archive.tar.gz");
if (fi.permission(QFile::WriteUser | QFile::ReadGroup))
    qWarning("I can change the file; my group can read the file");
if (fi.permission(QFile::WriteGroup | QFile::WriteOther))
    qWarning("The group or others can change the file");
```

If the file is a symlink, this function checks the permissions of the target (not the symlink).

**另请参阅** [isReadable](https://doc.qt.io/qt-5/qfileinfo.html#isReadable)(), [isWritable](https://doc.qt.io/qt-5/qfileinfo.html#isWritable)(), and [isExecutable](https://doc.qt.io/qt-5/qfileinfo.html#isExecutable)().

### [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) QFileInfo::permissions() const

Returns the complete OR-ed together combination of [QFile::Permissions](https://doc.qt.io/qt-5/qfiledevice.html#Permission-enum) for the file.

**注意** The result might be inaccurate on Windows if the [NTFS permissions](https://doc.qt.io/qt-5/qfileinfo.html#ntfs-permissions) check has not been enabled.

If the file is a symlink, this function returns the permissions of the target (not the symlink).

### void QFileInfo::refresh()

Refreshes the information about the file, i.e. reads in information from the file system the next time a cached property is fetched.

### void QFileInfo::setCaching(bool *enable*)

If *enable* is true, enables caching of file information. If *enable* is false caching is disabled.

When caching is enabled, [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) reads the file information from the file system the first time it's needed, but generally not later.

Caching is enabled by default.

**另请参阅** [refresh](https://doc.qt.io/qt-5/qfileinfo.html#refresh)() and [caching](https://doc.qt.io/qt-5/qfileinfo.html#caching)().

### void QFileInfo::setFile(const [QString](https://doc.qt.io/qt-5/qstring.html) &*file*)

Sets the file that the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) provides information about to *file*.

The *file* can also include an absolute or relative file path. Absolute paths begin with the directory separator (e.g. "/" under Unix) or a drive specification (under Windows). Relative file names begin with a directory name or a file name and specify a path relative to the current directory.

Example:

```
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

**另请参阅** [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)(), [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)(), [QDir::setCurrent](https://doc.qt.io/qt-5/qdir.html#setCurrent)(), and [QDir::isRelativePath](https://doc.qt.io/qt-5/qdir.html#isRelativePath)().

### void QFileInfo::setFile(const [QFile](https://doc.qt.io/qt-5/qfile.html) &*file*)

This is an overloaded function.

Sets the file that the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) provides information about to *file*.

If *file* includes a relative path, the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) will also have a relative path.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### void QFileInfo::setFile(const [QDir](https://doc.qt.io/qt-5/qdir.html) &*dir*, const [QString](https://doc.qt.io/qt-5/qstring.html) &*file*)

This is an overloaded function.

Sets the file that the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) provides information about to *file* in directory *dir*.

If *file* includes a relative path, the [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) will also have a relative path.

**另请参阅** [isRelative](https://doc.qt.io/qt-5/qfileinfo.html#isRelative)().

### [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QFileInfo::size() const

Returns the file size in bytes. If the file does not exist or cannot be fetched, 0 is returned.

If the file is a symlink, the size of the target file is returned (not the symlink).

**另请参阅** [exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::suffix() const

Returns the suffix (extension) of the file.

The suffix consists of all characters in the file after (but not including) the last '.'.

Example:

```
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.suffix();  // ext = "gz"
```

The suffix of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

**另请参阅** [fileName](https://doc.qt.io/qt-5/qfileinfo.html#fileName)(), [completeSuffix](https://doc.qt.io/qt-5/qfileinfo.html#completeSuffix)(), [baseName](https://doc.qt.io/qt-5/qfileinfo.html#baseName)(), and [completeBaseName](https://doc.qt.io/qt-5/qfileinfo.html#completeBaseName)().

### void QFileInfo::swap(QFileInfo &*other*)

Swaps this file info with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::symLinkTarget() const

Returns the absolute path to the file or directory a symbolic link points to, or an empty string if the object isn't a symbolic link.

This name may not represent an existing file; it is only a string. [QFileInfo::exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)() returns `true` if the symlink points to an existing file.

This function was introduced in Qt 4.2.

**另请参阅** [exists](https://doc.qt.io/qt-5/qfileinfo.html#exists)(), [isSymLink](https://doc.qt.io/qt-5/qfileinfo.html#isSymLink)(), [isDir](https://doc.qt.io/qt-5/qfileinfo.html#isDir)(), and [isFile](https://doc.qt.io/qt-5/qfileinfo.html#isFile)().

### bool QFileInfo::operator!=(const QFileInfo &*fileinfo*) const

Returns `true` if this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) object refers to a different file than the one specified by *fileinfo*; otherwise returns `false`.

**另请参阅** [operator==](https://doc.qt.io/qt-5/qfileinfo.html#operator-eq-eq)().

### bool QFileInfo::operator==(const QFileInfo &fileinfo) const

Returns `true` if this [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) object refers to a file in the same location as *fileinfo*; otherwise returns `false`.

Note that the result of comparing two empty [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) objects, containing no file references (file paths that do not exist or are empty), is undefined.

**警告** This will not compare two different symbolic links pointing to the same file.

**警告** Long and short file names that refer to the same file on Windows are treated as if they referred to different files.

**另请参阅** [operator!=](https://doc.qt.io/qt-5/qfileinfo.html#operator-not-eq)()

## 相关非成员

### QFileInfoList

等同于 [QList](https://doc.qt.io/qt-5/qlist.html)<[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html)>