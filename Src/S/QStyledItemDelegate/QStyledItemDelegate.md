[toc]
# QStyledItemDelegate

`QStyledItemDelegate ` 类为模型(model)中的数据项提供显示和编辑功能。

| 属性     | 方法                            |
| -------- | ------------------------------- |
| 头文件:  | \#include <QStyledItemDelegate> |
| qmake:   | QT += widgets                   |
| 引入版本 | Qt 4.2                          |
| 继承的类 | [QAbstractItemDelegate]()       |

这个类是在Qt 4.2中引入的

## 公有成员函数





## 重载实现的公有函数





## 保护成员函数





## 重载实现的保护函数





## 详细描述

当在Qt项视图中显示来自模型的数据时，各个项都是由委托绘制的，例如 `QTableView` 。当编辑一个项目时，它提供一个编辑器部件，它被放置在项目视图的顶部。`QStyledItemDelegate` 是所有Qt项视图的默认委托，在创建时安装在项目上面。

`QStyledItemDelegate` 类是模型/视图类之一，是Qt的模型/视图框架的一部分。委托允许项目显示和编辑独立于模型和视图进行开发。

对模型中每一项数据分配一个 `ItemDataRole `;每个项可以存储一个`QVariant` 角色。`QStyledItemDelegate` 实现了用户期望的常见数据类型显示和编辑，包括布尔值(`booleans`)、整数(`integers`)和字符串(`strings`)。

它们在模型中的角色不同，数据的绘制方式将有所不同。下表描述了角色和委托人可以为每个角色提供的数据处理类型。要确保模型为每个角色返回适当的数据，来确定视图中每一项的外观。

| 角色                    | 接受类型                                |
| ----------------------- | --------------------------------------- |
| Qt::BackgroundRole      | QBrush                                  |
| Qt::BackgroundColorRole | QColor (已弃用，使用Qt::BackgroundRole) |
| Qt::CheckStateRole      | Qt::CheckState                          |
| Qt::DecorationRole      | QIcon, QPixmap, QImage and QColor       |
| Qt::DisplayRole         | QString和字符串形式表示的类型           |
| Qt::EditRole            | [QItemEditorFactory]() 查看详情         |
| Qt::FontRole            | QFont                                   |
| Qt::SizeHintRole        | QSize                                   |
| Qt::TextAlignmentRole   | Qt::Alignment                           |
| Qt::ForegroundRole      | QBrush                                  |
| Qt::TextColorRole       | QColor (已弃用，使用Qt::BackgroundRole) |

使用 `QItemEditorFactory` 创建编辑器; `QItemEditorFactory`提供的默认静态实例安装在所有项目委托上。您可以使用`setItemEditorFactory()` 设置自定义工厂，或者使用 `QItemEditorFactory::setDefaultFactory()` 设置新的默认工厂。被编辑的是存储在带有 `EditRole` 的项目模型中的数据。有关项目编辑器工厂的更高级介绍，请参见[QItemEditorFactory]()类。[Color Editor Factory]()示例展示了如何使用工厂创建自定义编辑器。

### 子类化QStyledItemDelegate

如果委托不支持绘制您需要的数据类型，或者您想定制项目的绘制，您需要子类化 `QStyledItemDelegate`，并重新实现 `paint()` 和 `sizeHint()` 。` paint()` 函数是为每个项单独调用，使用 `sizeHint()`，您可以为每个项指定提示.

在重新实现 `paint()` 时，通常会处理自己想要绘制的数据类型，并对其他类型使用超类实现。

复选框指示器的绘制是由当前的样式来执行的。样式还指定了不同数据角色的大小和绘制数据的边界矩形。项目本身的边界矩形也由样式计算。因此，当绘制已经支持的数据类型时，最好询问这些边框的样式。最好向样式询问这些边界矩形。[QStyle]()类对此有更详细的描述。

如果你想改变任何一个由样式计算出的边界矩形或复选框指示器，你可以子类QStyle。但是请注意，重新实现` sizeHint() ` 会影响项的大小。

自定义委托可以在不使用编辑器项工厂的情况下提供编辑器。在这种情况下，必须重新实现以下虚函数:

createEditor() 返回用于更改模型数据的小组件，并可重新实现以定制编辑行为。
setEditorData()为小组件提供了用于操作的数据。
updateEditorGeometry() 确保根据项目视图正确显示编辑器。
setModelData()将更新的数据返回给模型。
[Star Delegate]()示例通过重新实现这些方法来创建编辑器。

### QStyledItemDelegate与QItemDelegate



## 成员函数文档



## 未完成部分

关键词文件跳转