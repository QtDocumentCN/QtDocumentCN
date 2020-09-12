# QFileInfo 成员函数完整列表

这是 [QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 的成员函数的完整列表，包括继承的函数。

|返回类型|函数名|
|----:|:----|
||[QFileInfo](QFileInfo.md#成员函数文档)(const QFileInfo &fileinfo)|
||[QFileInfo](QFileInfo.md#QFileInfo::QFileInfo(const-QDir-&dir,-const-QString-&file))(const QDir &dir, const QString &file)|
||[QFileInfo](QFileInfo.md#QFileInfo::QFileInfo(const-QFile-&file))(const QFile &file)|
||[QFileInfo](QFileInfo.md#QFileInfo::QFileInfo(const-QString-&file))(const QString &file)|
||[QFileInfo](QFileInfo.md#QFileInfo::QFileInfo())()|
|QFileInfo &|[operator=](QFileInfo.md#QFileInfo-&QFileInfo::operator=(QFileInfo-&&other))(QFileInfo &&other)|
|QFileInfo &|[operator=](QFileInfo.md#QFileInfo-&QFileInfo::operator=(const-QFileInfo-&fileinfo))(const QFileInfo &fileinfo)|
||[~QFileInfo](QFileInfo.md#QFileInfo::~QFileInfo())()|
|QDir|[absoluteDir](QFileInfo.md#QDir-QFileInfo::absoluteDir()-const)() const|
|QString|[absoluteFilePath](QFileInfo.md#QString-QFileInfo::absoluteFilePath()-const)() const|
|QString|[absolutePath](QFileInfo.md#QString-QFileInfo::absolutePath()-const)() const|
|QString|[baseName](QFileInfo.md#QString-QFileInfo::baseName()-const)() const|
|QDateTime|[birthTime](QFileInfo.md#QDateTime-QFileInfo::birthTime()-const)() const|
|QString|[bundleName](QFileInfo.md#QString-QFileInfo::bundleName()-const)() const|
|bool|[caching](QFileInfo.md#bool-QFileInfo::caching()-const)() const|
|QString|[canonicalFilePath](QFileInfo.md#QString-QFileInfo::canonicalFilePath()-const)() const|
|QString|[canonicalPath](QFileInfo.md#QString-QFileInfo::canonicalPath()-const)() const|
|QString|[completeBaseName](QFileInfo.md#QString-QFileInfo::completeBaseName()-const)() const|
|QString|[completeSuffix](QFileInfo.md#QString-QFileInfo::completeSuffix()-const)() const|
|QDir|[dir](QFileInfo.md#QDir-QFileInfo::dir()-const)() const|
|bool|[exists](QFileInfo.md#bool-QFileInfo::exists()-const)() const|
|bool|[exists](QFileInfo.md#bool-QFileInfo::exists(const-QString-&file))(const QString &file)|
|QString|[fileName](QFileInfo.md#QString-QFileInfo::fileName()-const)() const|
|QString|[filePath](QFileInfo.md#QString-QFileInfo::filePath()-const)() const|
|QDateTime|[fileTime](QFileInfo.md#QDateTime-QFileInfo::fileTime(QFile::FileTime-time)-const)(QFile::FileTime time) const|
|QString|[group](QFileInfo.md#QString-QFileInfo::group()-const)() const|
|uint|[groupId](QFileInfo.md#uint-QFileInfo::groupId()-const)() const|
|bool|[isAbsolute](QFileInfo.md#bool-QFileInfo::isAbsolute()-const)() const|
|bool|[isBundle](QFileInfo.md#bool-QFileInfo::isBundle()-const)() const|
|bool|[isDir](QFileInfo.md#bool-QFileInfo::isDir()-const)() const|
|bool|[isExecutable](QFileInfo.md#bool-QFileInfo::isExecutable()-const)() const|
|bool|[isFile](QFileInfo.md#bool-QFileInfo::isFile()-const)() const|
|bool|[isHidden](QFileInfo.md#bool-QFileInfo::isHidden()-const)() const|
|bool|[isJunction](QFileInfo.md#bool-QFileInfo::isJunction()-const)() const|
|bool|[isNativePath](QFileInfo.md#bool-QFileInfo::isNativePath()-const)() const|
|bool|[isReadable](QFileInfo.md#bool-QFileInfo::isReadable()-const)() const|
|bool|[isRelative](QFileInfo.md#bool-QFileInfo::isRelative()-const)() const|
|bool|[isRoot](QFileInfo.md#bool-QFileInfo::isRoot()-const)() const|
|bool|[isShortcut](QFileInfo.md#bool-QFileInfo::isShortcut()-const)() const|
|bool|[isSymLink](QFileInfo.md#bool-QFileInfo::isSymLink()-const)() const|
|bool|[isSymbolicLink](QFileInfo.md#bool-QFileInfo::isSymbolicLink()-const)() const|
|bool|[isWritable](QFileInfo.md#bool-QFileInfo::isWritable()-const)() const|
|QDateTime|[lastModified](QFileInfo.md#QDateTime-QFileInfo::lastModified()-const)() const|
|QDateTime|[lastRead](QFileInfo.md#QDateTime-QFileInfo::lastRead()-const)() const|
|bool|[makeAbsolute](QFileInfo.md#bool-QFileInfo::makeAbsolute())()|
|QDateTime|[metadataChangeTime](QFileInfo.md#QDateTime-QFileInfo::metadataChangeTime()-const)() const|
|QString|[owner](QFileInfo.md#QString-QFileInfo::owner()-const)() const|
|uint|[ownerId](QFileInfo.md#uint-QFileInfo::ownerId()-const)() const|
|QString|[path](QFileInfo.md#QString-QFileInfo::path()-const)() const|
|bool|[permission](QFileInfo.md#bool-QFileInfo::permission(QFile::Permissions-permissions)-const)(QFile::Permissions permissions) const|
|QFile::Permissions|[permissions](QFileInfo.md#QFile::Permissions-QFileInfo::permissions()-const)() const|
|void|[refresh](QFileInfo.md#void-QFileInfo::refresh())() |
|void|[setCaching](QFileInfo.md#void-QFileInfo::setCaching(bool-enable))(bool enable)|
|void|[setFile](QFileInfo.md#void-QFileInfo::setFile(const-QString-&file))(const QString &file)|
|void|[setFile](QFileInfo.md#void-QFileInfo::setFile(const-QFile-&file))(const QFile &file)|
|void|[setFile](QFileInfo.md#void-QFileInfo::setFile(const-QDir-&dir,-const-QString-&file))(const QDir &dir, const QString &file)|
|qint64|[size](QFileInfo.md#qint64-QFileInfo::size()-const)() const|
|QString|[suffix](QFileInfo.md#QString-QFileInfo::suffix()-const)() const|
|void|[swap](QFileInfo.md#void-QFileInfo::swap(QFileInfo-&other))(QFileInfo &other)|
|QString|[symLinkTarget](QFileInfo.md#QString-QFileInfo::symLinkTarget()-const)() const|
|bool|[operator!=](QFileInfo.md#bool-QFileInfo::operator!=(const-QFileInfo-&fileinfo)-const)(const QFileInfo &fileinfo) const|
|bool|[operator==](QFileInfo.md#bool-QFileInfo::operator==(const-QFileInfo-&fileinfo)-const)(const QFileInfo &fileinfo) const|
