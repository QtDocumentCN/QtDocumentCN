Reserved by miRoox until 2020-07-31

# QPluginLoader Class

QPluginLoader 在运行时加载插件.

| 属性      | 方法                                            |
| --------- | ---------------------------------------------- |
| 头文件:   | \#include \<QPluginLoader\>                       |
| qmake:    | QT += core                                     |
| 继承: | [QObject](https://doc.qt.io/qt-5/qobject.html) |

**注意：** 该类提供的所有函数都是可重入的。



## 属性

| 属性                                                         | 类型                |
| ------------------------------------------------------------ | ------------------- |
| [fileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop) | QString             |
| [loadHints](https://doc.qt.io/qt-5/qpluginloader.html#loadHints-prop) | QLibrary::LoadHints |

## 公共成员函数

|  返回类型            | 函数名             |
| ------------------- | ------------------------------------------------------------ |
|                     | **[QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html#QPluginLoader-1)**(const QString &*fileName, QObject *parent = nullptr) |
|                     | **[QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html#QPluginLoader)**(QObject **parent* = nullptr) |
| virtual             | **[~QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html#dtor.QPluginLoader)**() |
| QString             | **[errorString](https://doc.qt.io/qt-5/qpluginloader.html#errorString)**() const |
| QString             | **[fileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop)**() const |
| QObject *           | **[instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)**() |
| bool                | **[isLoaded](https://doc.qt.io/qt-5/qpluginloader.html#isLoaded)**() const |
| bool                | **[load](https://doc.qt.io/qt-5/qpluginloader.html#load)**() |
| QLibrary::LoadHints | **[loadHints](https://doc.qt.io/qt-5/qpluginloader.html#loadHints-prop)**() const |
| QJsonObject         | **[metaData](https://doc.qt.io/qt-5/qpluginloader.html#metaData)**() const |
| void                | **[setFileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop)**(const QString &*fileName*) |
| void                | **[setLoadHints](https://doc.qt.io/qt-5/qpluginloader.html#loadHints-prop)**(QLibrary::LoadHints *loadHints*) |
| bool                | **[unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)**() |



## 静态公共成员函数

| 返回类型                 | 函数名                                                       |
| ------------------------ | ------------------------------------------------------------ |
| QObjectList              | **[staticInstances](https://doc.qt.io/qt-5/qpluginloader.html#staticInstances)**() |
| QVector\<QStaticPlugin\> | **[staticPlugins](https://doc.qt.io/qt-5/qpluginloader.html#staticPlugins)**() |



## 相关的非成员函数

| 返回类型 | 函数名                                                       |
| -------- | ------------------------------------------------------------ |
| void     | [qRegisterStaticPluginFunction](https://doc.qt.io/qt-5/qpluginloader.html#qRegisterStaticPluginFunction)(QStaticPlugin plugin) |



## 详细介绍

QPluginLoader 提供对 [Qt 插件](https://doc.qt.io/qt-5/plugins-howto.html)的访问。Qt 插件存储在共享库（DLL）中，而相比使用 [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) 访问的共享库，它具有以下优点：

- QPluginLoader 检查插件是否链接到与应用程序相同的 Qt 版本。
- QPluginLoader 提供对根组件对象的直接访问（[instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)()），而无需手动解析C函数。

QPluginLoader对象的实例在被称为插件的单个共享库文件上运行。它以独立于平台的方式提供对插件中功能的访问。要指定加载的插件，可以在构造函数中传递文件名，或者通过 [setFileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop)() 进行设置。

最重要的函数有：用来动态加载插件文件的 [load](https://doc.qt.io/qt-5/qpluginloader.html#load)()，用来检查加载是否成功的 [isLoaded](https://doc.qt.io/qt-5/qpluginloader.html#isLoaded)() ， 以及用来访问插件根组件的 [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)()。如果尚未加载插件，则 [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)() 函数会隐式尝试加载该插件。 可以使用 QPluginLoader 的多个实例来访问同一个实际的插件。

Once loaded, plugins remain in memory until all instances of QPluginLoader has been unloaded, or until the application terminates. You can attempt to unload a plugin using [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)(), but if other instances of QPluginLoader are using the same library, the call will fail, and unloading will only happen when every instance has called [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)(). Right before the unloading happens, the root component will also be deleted.

See [How to Create Qt Plugins](https://doc.qt.io/qt-5/plugins-howto.html) for more information about how to make your application extensible through plugins.

Note that the QPluginLoader cannot be used if your application is statically linked against Qt. In this case, you will also have to link to plugins statically. You can use [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) if you need to load dynamic libraries in a statically linked application.

**See also** [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) and [Plug & Paint Example](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html).

## 属性文档

### fileName : [QString](https://doc.qt.io/qt-5/qstring.html)

This property holds the file name of the plugin

We recommend omitting the file's suffix in the file name, since [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) will automatically look for the file with the appropriate suffix (see [QLibrary::isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)()).

When loading the plugin, [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) searches in all plugin locations specified by [QCoreApplication::libraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#libraryPaths)(), unless the file name has an absolute path. After loading the plugin successfully, fileName() returns the fully-qualified file name of the plugin, including the full path to the plugin if one was given in the constructor or passed to setFileName().

If the file name does not exist, it will not be set. This property will then contain an empty string.

By default, this property contains an empty string.

**Access functions:**

| QString | **fileName**() const                       |
| ------- | ------------------------------------------ |
| void    | **setFileName**(const QString &*fileName*) |

**See also** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)().

### loadHints : [QLibrary::LoadHints](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)

Give the [load](https://doc.qt.io/qt-5/qpluginloader.html#load)() function some hints on how it should behave.

You can give hints on how the symbols in the plugin are resolved. By default since Qt 5.7, [QLibrary::PreventUnloadHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum) is set.

See the documentation of [QLibrary::loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop) for a complete description of how this property works.

This property was introduced in Qt 4.4.

**Access functions:**

| QLibrary::LoadHints | **loadHints**() const                             |
| ------------------- | ------------------------------------------------- |
| void                | **setLoadHints**(QLibrary::LoadHints *loadHints*) |

**See also** [QLibrary::loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop).

## 成员函数文档

### QPluginLoader::QPluginLoader(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a plugin loader with the given *parent* that will load the plugin specified by *fileName*.

To be loadable, the file's suffix must be a valid suffix for a loadable library in accordance with the platform, e.g. `.so` on Unix, - `.dylib` on macOS and iOS, and `.dll` on Windows. The suffix can be verified with [QLibrary::isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)().

**See also** [setFileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop)().

### QPluginLoader::QPluginLoader([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

Constructs a plugin loader with the given *parent*.

### `[virtual]`QPluginLoader::~QPluginLoader()

Destroys the [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) object.

Unless [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)() was called explicitly, the plugin stays in memory until the application terminates.

**See also** [isLoaded](https://doc.qt.io/qt-5/qpluginloader.html#isLoaded)() and [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)().

### [QString](https://doc.qt.io/qt-5/qstring.html) QPluginLoader::errorString() const

Returns a text string with the description of the last error that occurred.

This function was introduced in Qt 4.2.

### [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) *QPluginLoader::instance()

Returns the root component object of the plugin. The plugin is loaded if necessary. The function returns `nullptr` if the plugin could not be loaded or if the root component object could not be instantiated.

If the root component object was destroyed, calling this function creates a new instance.

The root component, returned by this function, is not deleted when the [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) is destroyed. If you want to ensure that the root component is deleted, you should call [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)() as soon you don't need to access the core component anymore. When the library is finally unloaded, the root component will automatically be deleted.

The component object is a [QObject](https://doc.qt.io/qt-5/qobject.html). Use [qobject_cast](https://doc.qt.io/qt-5/qobject.html#qobject_cast)() to access interfaces you are interested in.

**See also** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)().

### bool QPluginLoader::isLoaded() const

Returns `true` if the plugin is loaded; otherwise returns `false`.

**See also** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)().

### bool QPluginLoader::load()

Loads the plugin and returns `true` if the plugin was loaded successfully; otherwise returns `false`. Since [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)() always calls this function before resolving any symbols it is not necessary to call it explicitly. In some situations you might want the plugin loaded in advance, in which case you would use this function.

**See also** [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)().

### [QJsonObject](https://doc.qt.io/qt-5/qjsonobject.html) QPluginLoader::metaData() const

Returns the meta data for this plugin. The meta data is data specified in a json format using the [Q_PLUGIN_METADATA](https://doc.qt.io/qt-5/qtplugin.html#Q_PLUGIN_METADATA)() macro when compiling the plugin.

The meta data can be queried in a fast and inexpensive way without actually loading the plugin. This makes it possible to e.g. store capabilities of the plugin in there, and make the decision whether to load the plugin dependent on this meta data.

### `[static]`[QObjectList](https://doc.qt.io/qt-5/qobject.html#QObjectList-typedef) QPluginLoader::staticInstances()

Returns a list of static plugin instances (root components) held by the plugin loader.

**See also** [staticPlugins](https://doc.qt.io/qt-5/qpluginloader.html#staticPlugins)().

### `[static]`[QVector](https://doc.qt.io/qt-5/qvector.html)<[QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html)> QPluginLoader::staticPlugins()

Returns a list of QStaticPlugins held by the plugin loader. The function is similar to [staticInstances](https://doc.qt.io/qt-5/qpluginloader.html#staticInstances)() with the addition that a [QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html) also contains meta data information.

**See also** [staticInstances](https://doc.qt.io/qt-5/qpluginloader.html#staticInstances)().

### bool QPluginLoader::unload()

Unloads the plugin and returns `true` if the plugin could be unloaded; otherwise returns `false`.

This happens automatically on application termination, so you shouldn't normally need to call this function.

If other instances of [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) are using the same plugin, the call will fail, and unloading will only happen when every instance has called unload().

Don't try to delete the root component. Instead rely on that unload() will automatically delete it when needed.

**See also** [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)() and [load](https://doc.qt.io/qt-5/qpluginloader.html#load)().

## Related Non-Members

### void qRegisterStaticPluginFunction([QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html) *plugin*)

Registers the *plugin* specified with the plugin loader, and is used by [Q_IMPORT_PLUGIN](https://doc.qt.io/qt-5/qtplugin.html#Q_IMPORT_PLUGIN)().

This function was introduced in Qt 5.0.