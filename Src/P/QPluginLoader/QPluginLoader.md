Reserved by miRoox until 2020-07-31

# QPluginLoader Class

QPluginLoader 在运行时加载插件.

| 属性      | 方法                                            |
| --------- | ---------------------------------------------- |
| 头文件:   | \#include \<QPluginLoader\>                       |
| qmake:    | QT += core                                     |
| 继承: | [QObject](../../O/QObject/QObject.md) |

**注意：** 该类提供的所有函数都是可重入的。



## 属性

| 属性                                                         | 类型                |
| ------------------------------------------------------------ | ------------------- |
| [fileName](QPluginLoader.md#filename--qstring) | QString             |
| [loadHints](QPluginLoader.md#loadhints--qlibraryloadhints) | QLibrary::LoadHints |

## 公共成员函数

|  返回类型            | 函数名             |
| ------------------- | ------------------------------------------------------------ |
|                     | **[QPluginLoader](QPluginLoader.md#qpluginloaderqpluginloaderconst-qstring-filename-qobject-parent--nullptr)**(const QString &*fileName, QObject *parent = nullptr) |
|                     | **[QPluginLoader](QPluginLoader.md#qpluginloaderqpluginloaderqobject-parent--nullptr)**(QObject **parent* = nullptr) |
| virtual             | **[~QPluginLoader](QPluginLoader.md#virtual-qpluginloaderqpluginloader)**() |
| QString             | **[errorString](QPluginLoader.md#qstring-qpluginloadererrorstring-const)**() const |
| QString             | **[fileName](QPluginLoader.md#filename--qstring)**() const |
| QObject *           | **[instance](QPluginLoader.md#qobject-qpluginloaderinstance)**() |
| bool                | **[isLoaded](QPluginLoader.md#bool-qpluginloaderisloaded-const)**() const |
| bool                | **[load](QPluginLoader.md#bool-qpluginloaderload)**() |
| QLibrary::LoadHints | **[loadHints](QPluginLoader.md#loadhints--qlibraryloadhints)**() const |
| QJsonObject         | **[metaData](QPluginLoader.md#qjsonobject-qpluginloadermetadata-const)**() const |
| void                | **[setFileName](QPluginLoader.md#filename--qstring)**(const QString &*fileName*) |
| void                | **[setLoadHints](QPluginLoader.md#loadhints--qlibraryloadhints)**(QLibrary::LoadHints *loadHints*) |
| bool                | **[unload](QPluginLoader.md#bool-qpluginloaderunload)**() |



## 静态公共成员函数

| 返回类型                 | 函数名                                                       |
| ------------------------ | ------------------------------------------------------------ |
| QObjectList              | **[staticInstances](QPluginLoader.md#static-qobjectlist-qpluginloaderstaticinstances)**() |
| QVector\<QStaticPlugin\> | **[staticPlugins](QPluginLoader.md#static-qvectorqstaticplugin-qpluginloaderstaticplugins)**() |



## 相关的非成员函数

| 返回类型 | 函数名                                                       |
| -------- | ------------------------------------------------------------ |
| void     | [qRegisterStaticPluginFunction](QPluginLoader.md#void-qregisterstaticpluginfunctionqstaticplugin-plugin)(QStaticPlugin plugin) |



## 详细介绍

QPluginLoader 提供对 [Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)的访问。Qt 插件存储在共享库（DLL）中，而相比使用 [QLibrary](../../L/QLibrary/QLibrary.md) 访问的共享库，它具有以下优点：

- QPluginLoader 检查插件是否链接到与应用程序相同的 Qt 版本。
- QPluginLoader 提供对根组件对象的直接访问（[instance](QPluginLoader.md#qobject-qpluginloaderinstance)()），而无需手动解析C函数。

QPluginLoader对象的实例在被称为插件的单个共享库文件上运行。它以独立于平台的方式提供对插件中功能的访问。要指定加载的插件，可以在构造函数中传递文件名，或者通过 [setFileName](QPluginLoader.md#filename--qstring)() 进行设置。

最重要的函数有：用来动态加载插件文件的 [load](QPluginLoader.md#bool-qpluginloaderload)()，用来检查加载是否成功的 [isLoaded](QPluginLoader.md#bool-qpluginloaderisloaded-const)() ， 以及用来访问插件根组件的 [instance](QPluginLoader.md#qobject-qpluginloaderinstance)()。如果尚未加载插件，则 [instance](QPluginLoader.md#qobject-qpluginloaderinstance)() 函数会隐式尝试加载该插件。 可以使用 QPluginLoader 的多个实例来访问同一个实际的插件。

加载后，插件将保留在内存中，直到所有 QPluginLoader 实例都已卸载，或者应用程序终止为止。您可以使用 [unload](QPluginLoader.md#bool-qpluginloaderunload)() 来尝试卸载插件，但如果有其它 QPluginLoader 实例正在使用同一个库，那么这一函数调用会失败，而当所有实例都调用了 [unload](QPluginLoader.md#bool-qpluginloaderunload)() 后插件才会真正被卸载。在卸载发生之前，根组件也将被删除。

有关如何使应用程序可通过插件扩展的更多信息，请参见[如何创建 Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)。

请注意，如果您的应用程序与 Qt 静态链接，则无法使用 QPluginLoader。在这种情况下，您还必须静态链接到插件。 如果需要在静态链接的应用程序中加载动态库，则可以使用 [QLibrary](../../L/QLibrary/QLibrary.md)。

**另请参阅** [QLibrary](../../L/QLibrary/QLibrary.md) 和[插件与绘制示例](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html)。

## 属性文档

### fileName : [QString](../../S/QString/QString.md)

该属性记录插件的文件名。

我们建议在文件名中省略文件的后缀，因为 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md) 将自动查找具有适当后缀的文件（请参阅 [QLibrary::isLibrary](../../L/QLibrary/QLibrary.md#static-bool-qlibraryislibraryconst-qstring-filename)()）。

加载插件时，除非文件名具有绝对路径，否则 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md) 会搜索 [QCoreApplication::libraryPaths](../../C/QCoreApplication/QCoreApplication.md#static-qstringlist-qcoreapplicationlibrarypaths)() 指定的所有插件位置。成功加载插件后，fileName() 返回插件的完全限定文件名，如果在构造函数中已指定或传递给 setFileName()，则包括插件的完整路径。

如果文件名不存在，改属性将不会设置，并包含一个空字符串。

默认情况下，该属性包含一个空字符串。

**存取函数**

| 返回类型 | 函数名                                     |
| -------- | ------------------------------------------ |
| QString  | **fileName**() const                       |
| void     | **setFileName**(const QString &*fileName*) |

**另请参阅** [load](QPluginLoader.md#bool-qpluginloaderload)().

### loadHints : [QLibrary::LoadHints](../../L/QLibrary/QLibrary.md#enum-qlibraryloadhintflags-qlibraryloadhints)

为 [load](QPluginLoader.md#bool-qpluginloaderload)() 函数提供一些有关其行为方式的提示。

您可以提供有关如何解析插件中符号的提示。从 Qt 5.7 起，默认设置为 [QLibrary::PreventUnloadHint](../../L/QLibrary/QLibrary.md#enum-qlibraryloadhintflags-qlibraryloadhints)。

有关该属性如何工作的完整说明，请参阅 [QLibrary::loadHints](../../L/QLibrary/QLibrary.md#loadhints--loadhints) 的文档。

该属性在 Qt 4.4 中引入。

**存取函数**

| 返回类型            | 函数名                                            |
| ------------------- | ------------------------------------------------- |
| QLibrary::LoadHints | **loadHints**() const                             |
| void                | **setLoadHints**(QLibrary::LoadHints *loadHints*) |

**另请参阅** [QLibrary::loadHints](../../L/QLibrary/QLibrary.md#loadhints--loadhints)。

## 成员函数文档

### QPluginLoader::QPluginLoader(const [QString](../../S/QString/QString.md) &*fileName*, [QObject](../../O/QObject/QObject.md) **parent* = nullptr)

使用给定的 *parent* 构造一个插件加载器，并加载 *fileName* 指定的插件。

为了可加载，文件的后缀必须是可加载库的有效后缀，具体取决于平台，例如，Unix 上的 `.so`，macOS 和 iOS `.dylib`，以及 Windows 上的 `.dll`。后缀可以通过 [QLibrary::isLibrary](../../L/QLibrary/QLibrary.md#static-bool-qlibraryislibraryconst-qstring-filename)() 验证。

**另请参阅** [setFileName](QPluginLoader.md#filename--qstring)()。

### QPluginLoader::QPluginLoader([QObject](../../O/QObject/QObject.md) **parent* = nullptr)

使用给定的 *parent* 构造一个插件加载器。

### `[virtual]`QPluginLoader::~QPluginLoader()

销毁 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md) 对象。

除非 [unload](QPluginLoader.md#bool-qpluginloaderunload)() 被显式调用，插件会一直留在内存中直到程序结束。

**另请参阅** [isLoaded](QPluginLoader.md#bool-qpluginloaderisloaded-const)() 和 [unload](QPluginLoader.md#bool-qpluginloaderunload)()。

### [QString](../../S/QString/QString.md) QPluginLoader::errorString() const

返回带有最后发生的错误描述文本的字符串。

该函数在 Qt 4.2 中引入。

### [QObject](../../O/QObject/QObject.md) *QPluginLoader::instance()

返回插件的根组件对象。必要时会加载插件。如果无法加载插件或者根组件对象无法实例化时，该函数将返回 `nullptr`。

如果根组件对象已经被销毁了，该函数在调用时会创建一个新的实例。

该函数返回的根组件不会随着 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md) 的销毁而被删除。如果您希望保证根组件会被删除，可以在您不再需要访问核心组件是立即调用 [unload](QPluginLoader.md#bool-qpluginloaderunload)()。当库最终卸载时，对应根组件也会自动删除。

组件对象是一个 [QObject](../../O/QObject/QObject.md)。使用 [qobject_cast](../../O/QObject/QObject.md#template-typename-t-t-qobjectcastqobject-object)() 来访问你想要的接口。

**另请参阅** [load](QPluginLoader.md#bool-qpluginloaderload)()。

### bool QPluginLoader::isLoaded() const

如果已经成功加载插件则返回 `true`，否则返回 `false`。

**另请参阅** [load](QPluginLoader.md#bool-qpluginloaderload)()。

### bool QPluginLoader::load()

加载插件，并在插件成功加载时返回 `true`，否则返回 `false`。由于 [instance](QPluginLoader.md#qobject-qpluginloaderinstance)() 始终在解析任何符号之前调用此函数，因此无需显式调用它。在某些情况下，您可能需要预先加载插件，这时您才要使用该函数。

**另请参阅** [unload](QPluginLoader.md#bool-qpluginloaderunload)()。

### [QJsonObject](../../J/QJsonObject/QJsonObject.md) QPluginLoader::metaData() const

返回该插件的元数据。元数据是在编译插件时使用 [Q_PLUGIN_METADATA](../../P/QtPlugin/QtPlugin.md#Q_PLUGIN_METADATA)() 宏以json格式指定的数据。

无需实际加载插件即可以快速又经济的方式查询元数据。这使得例如可以在其中储存插件的功能，并根据该元数据来决定是否加载插件。

### `[static]`[QObjectList](../../O/QObject/QObject.md#typedef-qobjectlist) QPluginLoader::staticInstances()

返回由插件加载器保存的静态插件实例（根组件）的列表。

**另请参阅** [staticPlugins](QPluginLoader.md#static-qvectorqstaticplugin-qpluginloaderstaticplugins)()。

### `[static]`[QVector](../../V/QVector/QVector.md)\<[QStaticPlugin](../../S/QStaticPlugin/QStaticPlugin.md)\> QPluginLoader::staticPlugins()

返回由插件加载器保存的 QStaticPlugins 列表。 该函数类似于 [staticInstances](QPluginLoader.md#static-qobjectlist-qpluginloaderstaticinstances)()，除了 [QStaticPlugin](../../S/QStaticPlugin/QStaticPlugin.md) 还包含元数据信息。

**另请参阅** [staticInstances](QPluginLoader.md#static-qobjectlist-qpluginloaderstaticinstances)()。

### bool QPluginLoader::unload()

卸载插件，并在插件卸载成功时返回 `true`，否则返回 `false`。

这会在应用程序终止时自动发生，因此您通常不需要调用此函数。

如果存在其它 [QPluginLoader](../../P/QPluginLoader/QPluginLoader.md) 实例正在使用同一个插件，调用会失败，卸载只会发生在所有实例都调用了 unload() 时。

不要试图删除根组件。相反，凭借 unload() ，它会在必要时自动将其删除。

**另请参阅** [instance](QPluginLoader.md#qobject-qpluginloaderinstance)() 和 [load](QPluginLoader.md#bool-qpluginloaderload)()。

## 相关的非成员函数

### void qRegisterStaticPluginFunction([QStaticPlugin](../../S/QStaticPlugin/QStaticPlugin.md) *plugin*)

注册由插件加载器指定的 *plugin*，并由 [Q_IMPORT_PLUGIN](../../P/QtPlugin/QtPlugin.md#Q_IMPORT_PLUGINPluginName)() 使用。

该函数在 Qt 5.0 中引入。