# \<QtPlugin\> - 定义插件

QtPlugin 头文件定义用于定义插件的宏。

| 属性   | 方法                   |
| -----: | :--------------------- |
| 头文件 | \#include \<QtPlugin\> |



## 宏

|      | 宏名                                                         |
| ---- | ------------------------------------------------------------ |
|      | **[Q_DECLARE_INTERFACE](QtPlugin.md#q_declare_interfaceclassname-identifier)**(*ClassName*, *Identifier*) |
|      | **[Q_IMPORT_PLUGIN](QtPlugin.md#q_import_pluginpluginname)**(*PluginName*) |
|      | **[Q_PLUGIN_METADATA](QtPlugin.md#q_plugin_metadata)**(*...*) |



## 详细介绍

**另请参阅** [如何创建 Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)。

## 宏文档

### Q_DECLARE_INTERFACE(*ClassName*, *Identifier*)

该宏将给定的 *Identifier*（字符串字面量）与名为 *ClassName* 的接口类关联。*Identifier* 必须是唯一的。例如：

```cpp
#define BrushInterface_iid "org.qt-project.Qt.Examples.PlugAndPaint.BrushInterface/1.0"

Q_DECLARE_INTERFACE(BrushInterface, BrushInterface_iid)
```

通常在头文件中 *ClassName* 的类定义之后立即使用此宏。有关详细信息，请参见[插件与绘制](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html)示例。

如果要对命名空间中的接口类使用 Q_DECLARE_INTERFACE，请务必保证 Q_DECLARE_INTERFACE 不在命名空间中。例如：

```cpp
namespace Foo
{
    struct MyInterface { ... };
}

Q_DECLARE_INTERFACE(Foo::MyInterface, "org.examples.MyInterface")
```

**另请参阅** [Q_INTERFACES](https://doc.qt.io/qt-5/qobject.html#Q_INTERFACES)() 和[如何创建 Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)。

### Q_IMPORT_PLUGIN(*PluginName*)

该宏导入名为 *PluginName* 的插件，该插件与使用 [Q_PLUGIN_METADATA](QtPlugin.md#q_plugin_metadata)() 声明插件元数据的类的名称相对应。This macro imports the plugin named *PluginName*, which corresponds with the name of the class that declares metadata for the plugin with [Q_PLUGIN_METADATA](QtPlugin.md#q_plugin_metadata)().

将该宏插入应用程序的源代码来使您能够使用静态插件。

例如：

```cpp
Q_IMPORT_PLUGIN(qjpeg)
```

构建应用程序时，链接器必须包含静态插件。对于 Qt 预定义的插件，可以使用 `QTPLUGIN` 将插件加入你的构建系统。例如：

```qmake
TEMPLATE      = app
QTPLUGIN     += qjpeg qgif    # image formats
```

**另请参阅** [静态插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md#%E9%9D%99%E6%80%81%E6%8F%92%E4%BB%B6)、[如何创建 Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)以及 [qmake 入门](https://doc.qt.io/qt-5/qmake-tutorial.html)。

### Q_PLUGIN_METADATA(*...*)

该宏用于声明插件元数据，它是实例化此对象的插件的一部分。

该宏需要声明通过该对象实现的接口的 IID，并引用包含该插件的元数据的文件。

对于某一个 Qt 插件，该宏在源代码中应恰好出现一次。

示例：

```cpp
class MyInstance : public QObject
{
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QDummyPlugin" FILE "mymetadata.json")
};
```

有关详细信息，请参见[插件与绘制](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html)示例。

请注意，该宏出现的类必须是可默认构造的。

FILE是可选的，并指向一个 json 文件。

该 json 文件必须存在于构建系统指定的包含目录之一中。当找不到指定文件时，moc 将退出并显示错误。

该宏在 Qt 5.0 中引入。

**另请参阅** [Q_DECLARE_INTERFACE](QtPlugin.md#q_declare_interfaceclassname-identifier)() 和[如何创建 Qt 插件](../../H/How_to_Create_Qt_Plugins/How_to_Create_Qt_Plugins.md)。