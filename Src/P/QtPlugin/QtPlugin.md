Reserved by miRoox until 2020-07-31

# \<QtPlugin\> - 定义插件

[QtPlugin](https://doc.qt.io/qt-5/qmake-variable-reference.html#qtplugin) 头文件定义用于定义插件的宏。

| 属性   | 方法                   |
| -----: | :--------------------- |
| 头文件 | \#include \<QtPlugin\> |



## 宏

|      | 宏名                                                         |
| ---- | ------------------------------------------------------------ |
|      | **[Q_DECLARE_INTERFACE](https://doc.qt.io/qt-5/qtplugin.html#Q_DECLARE_INTERFACE)**(*ClassName*, *Identifier*) |
|      | **[Q_IMPORT_PLUGIN](https://doc.qt.io/qt-5/qtplugin.html#Q_IMPORT_PLUGIN)**(*PluginName*) |
|      | **[Q_PLUGIN_METADATA](https://doc.qt.io/qt-5/qtplugin.html#Q_PLUGIN_METADATA)**(*...*) |



## 详细介绍

**另请参阅** [如何创建 Qt 插件](https://doc.qt.io/qt-5/plugins-howto.html)。

## 宏文档

### Q_DECLARE_INTERFACE(*ClassName*, *Identifier*)

This macro associates the given *Identifier* (a string literal) to the interface class called *ClassName*. The *Identifier* must be unique. For example:

```cpp
#define BrushInterface_iid "org.qt-project.Qt.Examples.PlugAndPaint.BrushInterface/1.0"

Q_DECLARE_INTERFACE(BrushInterface, BrushInterface_iid)
```

This macro is normally used right after the class definition for *ClassName*, in a header file. See the [Plug & Paint](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html) example for details.

If you want to use Q_DECLARE_INTERFACE with interface classes declared in a namespace then you have to make sure the Q_DECLARE_INTERFACE is not inside a namespace though. For example:

```cpp
namespace Foo
{
    struct MyInterface { ... };
}

Q_DECLARE_INTERFACE(Foo::MyInterface, "org.examples.MyInterface")
```

**另请参阅** [Q_INTERFACES](https://doc.qt.io/qt-5/qobject.html#Q_INTERFACES)() and [How to Create Qt Plugins](https://doc.qt.io/qt-5/plugins-howto.html).

### Q_IMPORT_PLUGIN(*PluginName*)

This macro imports the plugin named *PluginName*, which corresponds with the name of the class that declares metadata for the plugin with [Q_PLUGIN_METADATA](https://doc.qt.io/qt-5/qtplugin.html#Q_PLUGIN_METADATA)().

Inserting this macro into your application's source code will allow you to make use of a static plugin.

Example:

```cpp
Q_IMPORT_PLUGIN(qjpeg)
```

Static plugins must also be included by the linker when your application is built. For Qt's predefined plugins, you can use the `QTPLUGIN` to add the required plugins to your build. For example:

```qmake
TEMPLATE      = app
QTPLUGIN     += qjpeg qgif    # image formats
```

**另请参阅** [Static Plugins](https://doc.qt.io/qt-5/plugins-howto.html#static-plugins), [How to Create Qt Plugins](https://doc.qt.io/qt-5/plugins-howto.html), and [Getting Started with qmake](https://doc.qt.io/qt-5/qmake-tutorial.html).

### Q_PLUGIN_METADATA(*...*)

This macro is being used to declare meta data that is part of a plugin that instantiates this object.

The macro needs to declare the IID of the interface implemented through the object, and reference a file containing the meta data for the plugin.

There should be exactly one occurrence of this macro in the source code for a Qt plugin.

Example:

```cpp
class MyInstance : public QObject
{
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QDummyPlugin" FILE "mymetadata.json")
};
```

See the [Plug & Paint](https://doc.qt.io/qt-5/qtwidgets-tools-plugandpaint-app-example.html) example for details.

Note that the class this macro appears on must be default-constructible.

FILE is optional and points to a json file.

The json file must reside in one of the include directories specified by the build-system. moc exits with an error when it could not find the specified file.

This function was introduced in Qt 5.0.

**另请参阅** [Q_DECLARE_INTERFACE](https://doc.qt.io/qt-5/qtplugin.html#Q_DECLARE_INTERFACE)() and [How to Create Qt Plugins](https://doc.qt.io/qt-5/plugins-howto.html).