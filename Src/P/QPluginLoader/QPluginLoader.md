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

加载后，插件将保留在内存中，直到所有 QPluginLoader 实例都已卸载，或者应用程序终止为止。您可以使用 [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)() 来尝试卸载插件，但如果有其它 QPluginLoader 实例正在使用同一个库，那么这一函数调用会失败，而当所有实例都调用了 [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)() 后插件才会真正被卸载。在卸载发生之前，根组件也将被删除。

有关如何使应用程序可通过插件扩展的更多信息，请参见[如何创建 Qt 插件](https://doc.qt.io/qt-5/plugins-howto.html)。

请注意，如果您的应用程序与 Qt 静态链接，则无法使用 QPluginLoader。在这种情况下，您还必须静态链接到插件。 如果需要在静态链接的应用程序中加载动态库，则可以使用 [QLibrary](https://doc.qt.io/qt-5/qlibrary.html)。

**另请参阅** [QLibrary](https://doc.qt.io/qt-5/qlibrary.html) 和[插件与绘制示例](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html)。

## 属性文档

### fileName : [QString](https://doc.qt.io/qt-5/qstring.html)

该属性记录插件的文件名。

我们建议在文件名中省略文件的后缀，因为 [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) 将自动查找具有适当后缀的文件（请参阅 [QLibrary::isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)()）。

加载插件时，除非文件名具有绝对路径，否则 [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) 会搜索 [QCoreApplication::libraryPaths](https://doc.qt.io/qt-5/qcoreapplication.html#libraryPaths)() 指定的所有插件位置。成功加载插件后，fileName() 返回插件的完全限定文件名，如果在构造函数中已指定或传递给 setFileName()，则包括插件的完整路径。

如果文件名不存在，改属性将不会设置，并包含一个空字符串。

默认情况下，该属性包含一个空字符串。

**存取函数**

| 返回类型 | 函数名                                     |
| -------- | ------------------------------------------ |
| QString  | **fileName**() const                       |
| void     | **setFileName**(const QString &*fileName*) |

**另请参阅** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)().

### loadHints : [QLibrary::LoadHints](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)

为 [load](https://doc.qt.io/qt-5/qpluginloader.html#load)() 函数提供一些有关其行为方式的提示。

您可以提供有关如何解析插件中符号的提示。从 Qt 5.7 起，默认设置为 [QLibrary::PreventUnloadHint](https://doc.qt.io/qt-5/qlibrary.html#LoadHint-enum)。

有关该属性如何工作的完整说明，请参阅 [QLibrary::loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop) 的文档。

该属性在 Qt 4.4 中引入。

**存取函数**

| 返回类型            | 函数名                                            |
| ------------------- | ------------------------------------------------- |
| QLibrary::LoadHints | **loadHints**() const                             |
| void                | **setLoadHints**(QLibrary::LoadHints *loadHints*) |

**另请参阅** [QLibrary::loadHints](https://doc.qt.io/qt-5/qlibrary.html#loadHints-prop)。

## 成员函数文档

### QPluginLoader::QPluginLoader(const [QString](https://doc.qt.io/qt-5/qstring.html) &*fileName*, [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

使用给定的 *parent* 构造一个插件加载器，并加载 *fileName* 指定的插件。

为了可加载，文件的后缀必须是可加载库的有效后缀，具体取决于平台，例如，Unix 上的 `.so`，macOS 和 iOS `.dylib`，以及 Windows 上的 `.dll`。后缀可以通过 [QLibrary::isLibrary](https://doc.qt.io/qt-5/qlibrary.html#isLibrary)() 验证。

**另请参阅** [setFileName](https://doc.qt.io/qt-5/qpluginloader.html#fileName-prop)()。

### QPluginLoader::QPluginLoader([QObject](https://doc.qt.io/qt-5/qobject.html#QObject) **parent* = nullptr)

使用给定的 *parent* 构造一个插件加载器。

### `[virtual]`QPluginLoader::~QPluginLoader()

销毁 [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) 对象。

除非 [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)() 被显式调用，插件会一直留在内存中直到程序结束。

**另请参阅** [isLoaded](https://doc.qt.io/qt-5/qpluginloader.html#isLoaded)() 和 [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)()。

### [QString](https://doc.qt.io/qt-5/qstring.html) QPluginLoader::errorString() const

返回带有最后发生的错误描述文本的字符串。

该函数在 Qt 4.2 中引入。

### [QObject](https://doc.qt.io/qt-5/qobject.html#QObject) *QPluginLoader::instance()

返回插件的根组件对象。必要时会加载插件。如果无法加载插件或者根组件对象无法实例化时，该函数将返回 `nullptr`。

如果根组件对象已经被销毁了，该函数在调用时会创建一个新的实例。

该函数返回的根组件不会随着 [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) 的销毁而被删除。如果您希望保证根组件会被删除，可以在您不再需要访问核心组件是立即调用 [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)()。当库最终卸载时，对应根组件也会自动删除。

组件对象是一个 [QObject](https://doc.qt.io/qt-5/qobject.html)。使用 [qobject_cast](https://doc.qt.io/qt-5/qobject.html#qobject_cast)() 来访问你想要的接口。

**另请参阅** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)()。

### bool QPluginLoader::isLoaded() const

如果已经成功加载插件则返回 `true`，否则返回 `false`。

**另请参阅** [load](https://doc.qt.io/qt-5/qpluginloader.html#load)()。

### bool QPluginLoader::load()

加载插件，并在插件成功加载时返回 `true`，否则返回 `false`。由于 [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)() 始终在解析任何符号之前调用此函数，因此无需显式调用它。在某些情况下，您可能需要预先加载插件，这时您才要使用该函数。

**另请参阅** [unload](https://doc.qt.io/qt-5/qpluginloader.html#unload)()。

### [QJsonObject](https://doc.qt.io/qt-5/qjsonobject.html) QPluginLoader::metaData() const

返回该插件的元数据。元数据是在编译插件时使用 [Q_PLUGIN_METADATA](https://doc.qt.io/qt-5/qtplugin.html#Q_PLUGIN_METADATA)() 宏以json格式指定的数据。

无需实际加载插件即可以快速又经济的方式查询元数据。这使得例如可以在其中储存插件的功能，并根据该元数据来决定是否加载插件。

### `[static]`[QObjectList](https://doc.qt.io/qt-5/qobject.html#QObjectList-typedef) QPluginLoader::staticInstances()

返回由插件加载器保存的静态插件实例（根组件）的列表。

**另请参阅** [staticPlugins](https://doc.qt.io/qt-5/qpluginloader.html#staticPlugins)()。

### `[static]`[QVector](https://doc.qt.io/qt-5/qvector.html)\<[QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html)\> QPluginLoader::staticPlugins()

返回由插件加载器保存的 QStaticPlugins 列表。 该函数类似于 [staticInstances](https://doc.qt.io/qt-5/qpluginloader.html#staticInstances)()，除了 [QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html) 还包含元数据信息。

**另请参阅** [staticInstances](https://doc.qt.io/qt-5/qpluginloader.html#staticInstances)()。

### bool QPluginLoader::unload()

卸载插件，并在插件卸载成功时返回 `true`，否则返回 `false`。

这会在应用程序终止时自动发生，因此您通常不需要调用此函数。

如果存在其它 [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html) 实例正在使用同一个插件，调用会失败，卸载只会发生在所有实例都调用了 unload() 时。

不要试图删除根组件。相反，凭借 unload() ，它会在必要时自动将其删除。

**另请参阅** [instance](https://doc.qt.io/qt-5/qpluginloader.html#instance)() 和 [load](https://doc.qt.io/qt-5/qpluginloader.html#load)()。

## 相关的非成员函数

### void qRegisterStaticPluginFunction([QStaticPlugin](https://doc.qt.io/qt-5/qstaticplugin.html) *plugin*)

注册由插件加载器指定的 *plugin*，并由 [Q_IMPORT_PLUGIN](https://doc.qt.io/qt-5/qtplugin.html#Q_IMPORT_PLUGIN)() 使用。

该函数在 Qt 5.0 中引入。