# QFileInfo 废弃的成员函数

[QFileInfo](https://doc.qt.io/qt-5/qfileinfo.html) 类的以下成员函数已废弃。提供它们是为了使旧的源代码正常工作。 我们强烈建议不要在新代码中使用它们。

## 公共成员函数

|返回类型|函数名|
|:----|:----|
|`(obsolete)`QDateTime|[created](https://doc.qt.io/qt-5/qfileinfo-obsolete.html#created)() const|
|`(obsolete)`QString|[readLink](https://doc.qt.io/qt-5/qfileinfo-obsolete.html#readLink)() const|

## 成员函数文档

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QFileInfo::created() const

此函数已废弃。 提供它是为了使旧的源代码正常工作。 我们强烈建议不要在新代码中使用它

返回文件创建的日期和时间，元数据上次更新或修改的时间（依次选三者中任一可用的）

不推荐使用此函数。 请使用 [birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)() 函数获取创建文件的时间，使用 [metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)() 获取其元数据上次更新时间，使用 [lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)() 获取上次修改时间

如果文件是符号链接，则返回目标文件的时间（非符号链接的）

**另请参阅** [birthTime](https://doc.qt.io/qt-5/qfileinfo.html#birthTime)(),[metadataChangeTime](https://doc.qt.io/qt-5/qfileinfo.html#metadataChangeTime)()，[lastModified](https://doc.qt.io/qt-5/qfileinfo.html#lastModified)() 和 [lastRead](https://doc.qt.io/qt-5/qfileinfo.html#lastRead)()

### [QString](https://doc.qt.io/qt-5/qstring.html) QFileInfo::readLink() const

此函数已废弃。提供它是为了使旧的源代码正常工作。 我们强烈建议不要在新代码中使用它

使用 [symLinkTarget](https://doc.qt.io/qt-5/qfileinfo.html#symLinkTarget)() 替代
