# QMainWindow 类

QMainWindow 类用于创建主程序窗口。 [More...](https://doc.qt.io/qt-5/qmainwindow.html#details)

|属性|方法|
|----:|:----|
|头文件:|`#include <QMainWindow>`|
|qmake:|`QT += widgets`|
|继承:|[QWidget](https://doc.qt.io/qt-5/qwidget.html)|

- [列出所有成员函数, 包括继承的成员函数](https://doc.qt.io/qt-5/qmainwindow-members.html)

## 公共成员类型

|类型|方法|
|----:|:----|
|enum|[DockOption](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) { AnimatedDocks, AllowNestedDocks, AllowTabbedDocks, ForceTabbedDocks, VerticalTabs, GroupedDragging }|
|flags| [DockOptions](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum)|

## 属性

|属性名|类型|
|----:|:----|
|[animated](https://doc.qt.io/qt-5/qmainwindow.html#animated-prop)|bool|
|[dockNestingEnabled](https://doc.qt.io/qt-5/qmainwindow.html#dockNestingEnabled-prop)|bool|
|[dockOptions](https://doc.qt.io/qt-5/qmainwindow.html#dockOptions-prop)|DockOptions|
|[documentMode](https://doc.qt.io/qt-5/qmainwindow.html#documentMode-prop)|bool|
|[iconSize](https://doc.qt.io/qt-5/qmainwindow.html#iconSize-prop)|QSize|
|[tabShape](https://doc.qt.io/qt-5/qmainwindow.html#tabShape-prop)|QTabWidget::TabShape|
|[toolButtonStyle](https://doc.qt.io/qt-5/qmainwindow.html#toolButtonStyle-prop)|Qt::ToolButtonStyle|
|[unifiedTitleAndToolBarOnMac](https://doc.qt.io/qt-5/qmainwindow.html#unifiedTitleAndToolBarOnMac-prop)|bool|

## 公共成员函数

|返回类型|函数名|
|----:|:----|
||[QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html#QMainWindow) (QWidget \*parent = nullptr, Qt::WindowFlags flags = Qt::WindowFlags())|
|virtual|[~QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html#dtor.QMainWindow) ()|
|void|[addDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#addDockWidget) (Qt::DockWidgetArea area, QDockWidget \*dockwidget)|
|void|[addDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#addDockWidget-1) (Qt::DockWidgetArea area, QDockWidget \*dockwidget, Qt::Orientation orientation)|
|void|[addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar) (Qt::ToolBarArea area, QToolBar \*toolbar)|
|void|[addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar-1) (QToolBar \*toolbar)|
|QToolBar \*|[addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar-2) (const QString &title)|
|void|[addToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#addToolBarBreak) (Qt::ToolBarArea area = Qt::TopToolBarArea)|
|QWidget \*|[centralWidget](https://doc.qt.io/qt-5/qmainwindow.html#centralWidget) () const|
|Qt::DockWidgetArea|[corner](https://doc.qt.io/qt-5/qmainwindow.html#corner) (Qt::Corner corner) const|
|virtual QMenu \*|[createPopupMenu](https://doc.qt.io/qt-5/qmainwindow.html#createPopupMenu) ()|
|QMainWindow::DockOptions|[dockOptions](https://doc.qt.io/qt-5/qmainwindow.html#dockOptions-prop) () const|
|Qt::DockWidgetArea|[dockWidgetArea](https://doc.qt.io/qt-5/qmainwindow.html#dockWidgetArea) (QDockWidget \*dockwidget) const|
|bool|[documentMode](https://doc.qt.io/qt-5/qmainwindow.html#documentMode-prop) () const|
|QSize|[iconSize](https://doc.qt.io/qt-5/qmainwindow.html#iconSize-prop) () const|
|void|[insertToolBar](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBar) (QToolBar \*before, QToolBar \*toolbar)|
|void|[insertToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBarBreak) (QToolBar \*before)|
|bool|[isAnimated](https://doc.qt.io/qt-5/qmainwindow.html#animated-prop) () const|
|bool|[isDockNestingEnabled](https://doc.qt.io/qt-5/qmainwindow.html#dockNestingEnabled-prop) () const|
|QMenuBar \*|[menuBar](https://doc.qt.io/qt-5/qmainwindow.html#menuBar) () const|
|QWidget \*|[menuWidget](https://doc.qt.io/qt-5/qmainwindow.html#menuWidget) () const|
|void|[removeDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#removeDockWidget) (QDockWidget \*dockwidget)|
|void|[removeToolBar](https://doc.qt.io/qt-5/qmainwindow.html#removeToolBar) (QToolBar \*toolbar)|
|void|[removeToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#removeToolBarBreak) (QToolBar \*before)|
|void|[resizeDocks](https://doc.qt.io/qt-5/qmainwindow.html#resizeDocks) (const QList\<QDockWidget \*> &docks, const QList\<int> &sizes, Qt::Orientation orientation)|
|bool|[restoreDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#restoreDockWidget) (QDockWidget \*dockwidget)|
|bool|[restoreState](https://doc.qt.io/qt-5/qmainwindow.html#restoreState) (const QByteArray &state, int version = 0)|
|QByteArray|[saveState](https://doc.qt.io/qt-5/qmainwindow.html#saveState) (int version = 0) const|
|void|[setCentralWidget](https://doc.qt.io/qt-5/qmainwindow.html#setCentralWidget) (QWidget \*widget)|
|void|[setCorner](https://doc.qt.io/qt-5/qmainwindow.html#setCorner) (Qt::Corner corner, Qt::DockWidgetArea area)|
|void|[setDockOptions](https://doc.qt.io/qt-5/qmainwindow.html#dockOptions-prop) (QMainWindow::DockOptions options)|
|void|[setDocumentMode](https://doc.qt.io/qt-5/qmainwindow.html#documentMode-prop) (bool enabled)|
|void|[setIconSize](https://doc.qt.io/qt-5/qmainwindow.html#iconSize-prop) (const QSize &iconSize)|
|void|[setMenuBar](https://doc.qt.io/qt-5/qmainwindow.html#setMenuBar) (QMenuBar \*menuBar)|
|void|[setMenuWidget](https://doc.qt.io/qt-5/qmainwindow.html#setMenuWidget) (QWidget \*menuBar)|
|void|[setStatusBar](https://doc.qt.io/qt-5/qmainwindow.html#setStatusBar) (QStatusBar \*statusbar)|
|void|[setTabPosition](https://doc.qt.io/qt-5/qmainwindow.html#setTabPosition) (Qt::DockWidgetAreas areas, QTabWidget::TabPosition tabPosition)|
|void|[setTabShape](https://doc.qt.io/qt-5/qmainwindow.html#tabShape-prop) (QTabWidget::TabShape tabShape)|
|void|[setToolButtonStyle](https://doc.qt.io/qt-5/qmainwindow.html#toolButtonStyle-prop) (Qt::ToolButtonStyle toolButtonStyle)|
|void|[splitDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#splitDockWidget) (QDockWidget \*first, QDockWidget \*second, Qt::Orientation orientation)|
|QStatusBar \*|[statusBar](https://doc.qt.io/qt-5/qmainwindow.html#statusBar) () const|
|QTabWidget::TabPosition|[tabPosition](https://doc.qt.io/qt-5/qmainwindow.html#tabPosition) (Qt::DockWidgetArea area) const|
|QTabWidget::TabShape|[tabShape](https://doc.qt.io/qt-5/qmainwindow.html#tabShape-prop) () const|
|QList\<QDockWidget \*>|[tabifiedDockWidgets](https://doc.qt.io/qt-5/qmainwindow.html#tabifiedDockWidgets) (QDockWidget \*dockwidget) const|
|void|[tabifyDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#tabifyDockWidget) (QDockWidget \*first, QDockWidget \*second)|
|QWidget \*|[takeCentralWidget](https://doc.qt.io/qt-5/qmainwindow.html#takeCentralWidget) ()|
|Qt::ToolBarArea|[toolBarArea](https://doc.qt.io/qt-5/qmainwindow.html#toolBarArea) (QToolBar \*toolbar) const|
|bool|[toolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#toolBarBreak) (QToolBar \*toolbar) const|
|Qt::ToolButtonStyle|[toolButtonStyle](https://doc.qt.io/qt-5/qmainwindow.html#toolButtonStyle-prop) () const|
|bool|[unifiedTitleAndToolBarOnMac](https://doc.qt.io/qt-5/qmainwindow.html#unifiedTitleAndToolBarOnMac-prop) () const|

## 公共槽

|返回类型|函数名|
|----:|:----|
|void|[setAnimated](https://doc.qt.io/qt-5/qmainwindow.html#animated-prop) (bool enabled)|
|void|[setDockNestingEnabled](https://doc.qt.io/qt-5/qmainwindow.html#dockNestingEnabled-prop) (bool enabled)|
|void|[setUnifiedTitleAndToolBarOnMac](https://doc.qt.io/qt-5/qmainwindow.html#unifiedTitleAndToolBarOnMac-prop) (bool set)|

## 信号

|返回类型|函数名|
|----:|:----|
|void|[iconSizeChanged](https://doc.qt.io/qt-5/qmainwindow.html#iconSizeChanged) (const QSize &iconSize)|
|void|[tabifiedDockWidgetActivated](https://doc.qt.io/qt-5/qmainwindow.html#tabifiedDockWidgetActivated) (QDockWidget \*dockWidget)|
|void|[toolButtonStyleChanged](https://doc.qt.io/qt-5/qmainwindow.html#toolButtonStyleChanged) (Qt::ToolButtonStyle toolButtonStyle)|

## 保护成员函数

|返回类型|函数名|
|----:|:----|
|virtual void|[contextMenuEvent](https://doc.qt.io/qt-5/qmainwindow.html#contextMenuEvent) (QContextMenuEvent \*event) override|
|virtual bool|[event](https://doc.qt.io/qt-5/qmainwindow.html#event) (QEvent \*event) override|

## 详细描述

### Qt 主窗口框架

主窗口提供了一套创建应用程序用户界面的框架。 Qt 用`QMainWindow`和 [相关类](https://doc.qt.io/qt-5/widget-classes.html#main-window-and-related-classes) 来管理主窗口。`QMainWindow`已经定义了一个布局，可以往里添加一些 [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) 和 [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html)，也可以添加一个 [QMenuBar](https://doc.qt.io/qt-5/qmenubar.html) 和一个 [QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html)。这个布局有一个中央区域，可以放任意部件。如下图所示：

![main window layout](mainwindowlayout.png)

**注意** 主窗口必须设置中央部件。

### 创建主窗口组件

中央部件通常是标准 Qt 部件，如 [QTextEdit](https://doc.qt.io/qt-5/qtextedit.html) 或  [QGraphicsView](https://doc.qt.io/qt-5/qgraphicsview.html)，也可自定义部件。用`setCentralWidget()`来设置中央部件。

主窗口可以是单文档界面或多文档界面。 Qt 中设置 [QMdiArea](https://doc.qt.io/qt-5/qmdiarea.html) 为中央部件即创建了多文档界面。

下面举例说明主窗口可以添加的部件。

#### 创建菜单

Qt 用 [QMenu](https://doc.qt.io/qt-5/qmenu.html) 类实现菜单，主窗口将其放在 [QMenuBar](https://doc.qt.io/qt-5/qmenubar.html)。可以添加 [QAction](https://doc.qt.io/qt-5/qaction.html) 到`QMenu`，一个`QAction`代表菜单中的一个条目。

用`menuBar()`可以得到主窗口的菜单栏，用 [QMenuBar::addMenu](https://doc.qt.io/qt-5/qmenubar.html#addMenu()) 添加菜单。

QMainWindow 默认有一个菜单栏，可以用`setMenuBar()`自定义一个新的菜单栏。如果不想用 [QMenuBar](https://doc.qt.io/qt-5/qmenubar.html) ，也可以用`setMenuWidget()`来定制菜单栏。

创建菜单代码示例：

```c++
    void MainWindow::createMenus()
    {
        fileMenu = menuBar()->addMenu(tr("&File"));
        fileMenu->addAction(newAct);
        fileMenu->addAction(openAct);
        fileMenu->addAction(saveAct);
    }
```

`createPopupMenu()`可以创建弹出式菜单，它会在主窗口收到 context menu 事件时弹出。 停靠部件和菜单栏默认实现了右键菜单，可以重写`createPopupMenu()`创建自定义菜单。

#### 创建工具栏

Qt 用 [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) 类实现工具栏，可以用`addToolBar()`添加工具栏到主窗口。

可以设置 [Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum) 来控制工具栏的初始位置。可以用`addToolBarBreak()`或`insertToolBarBreak()`分割工具栏所在的区域，前者可使接下来添加的工具栏换至新的一行，后者添加了一个工具栏分隔符。用 [QToolBar::setAllowedAreas](https://doc.qt.io/qt-5/qtoolbar.html#allowedAreas-prop) 加 [QToolBar::setMovable](https://doc.qt.io/qt-5/qtoolbar.html#movable-prop) 可以限制用户放工具栏的位置。

工具栏图标的尺寸可以用`iconSize()`获取，它是平台相关的。可以用`setIconSize()`设置固定尺寸。用`setToolButtonStyle()`可以修改工具栏图标外观。

创建工具栏代码示例：

```c++
    void MainWindow::createToolBars()
    {
        fileToolBar = addToolBar(tr("File"));
        fileToolBar->addAction(newAct);
    }
```

#### 创建停靠部件

Qt 用 [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 类实现停靠部件。停靠部件即可以停靠在主窗口的窗口，可以用`addDockWidget()`添加停靠部件到主窗口。

可以设置 [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) 来控制停靠部件的位置，有上、下、左、右四种。`setCorner()`可以让一个角落属于某个相邻的区域。默认情况下，一个区域只有一个停靠部件，用`setDockNestingEnabled()`可以使其能上下或者左右排列多个停靠部件。

两个停靠部件也可以堆叠在一起，然后使用 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 来选择应显示哪个部件。

创建并添加停靠部件到主窗口的代码示例：

```c++
    QDockWidget *dockWidget = new QDockWidget(tr("Dock Widget"), this);
    dockWidget->setAllowedAreas(Qt::LeftDockWidgetArea | Qt::RightDockWidgetArea);
    dockWidget->setWidget(dockWidgetContents);
    addDockWidget(Qt::LeftDockWidgetArea, dockWidget);
```

#### 状态栏

用`setStatusBar()`可以设置状态栏，调用`statusBar()`会返回主窗口的状态栏。查看 [QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html) 获取更多内容。

### 存储状态

QMainWindow 用`saveState()`保存布局，用`restoreState()`恢复布局。包括工具栏和停靠部件的位置和相对主窗口的尺寸。

**另请参阅** [QMenuBar](https://doc.qt.io/qt-5/qmenubar.html)，[QToolBar](https://doc.qt.io/qt-5/qtoolbar.html)，[QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html), [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html)，[Application Example](https://doc.qt.io/qt-5/qtwidgets-mainwindows-application-example.html)，[Dock Widgets Example](https://doc.qt.io/qt-5/qtwidgets-mainwindows-dockwidgets-example.html)，[MDI Example](https://doc.qt.io/qt-5/qtwidgets-mainwindows-mdi-example.html)，[SDI Example](https://doc.qt.io/qt-5/qtwidgets-mainwindows-sdi-example.html) 和 [Menus Example](https://doc.qt.io/qt-5/qtwidgets-mainwindows-menus-example.html)。

## 成员变量文档

### enum QMainWindow::DockOption flags QMainWindow::DockOptions

该枚举包含指定 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 停靠行为的标志。

|函数|值|描述|
|:----:|:----:|------|
|`QMainWindow::AnimatedDocks`|`0x01`|同 [animated](https://doc.qt.io/qt-5/qmainwindow.html#animated-prop) 属性|
|`QMainWindow::AllowNestedDocks`|`0x02`|同 [dockNestingEnabled](https://doc.qt.io/qt-5/qmainwindow.html#dockNestingEnabled-prop) 属性|
|`QMainWindow::AllowTabbedDocks`|`0x04`|允许形成下方有 tabBar 的重合部件|
|`QMainWindow::ForceTabbedDocks`|`0x08`|每个停靠区域都只包含一个选项卡式停靠部件。换句话说，停靠区域里不能上下或左右排列停靠部件。如果设置了此选项，则 AllowNestedDocks 不起作用。|
|`QMainWindow::VerticalTabs`|`0x10`|设置 tabBar 在竖直左方位置（默认在下方），包含了 AllowTabbedDocks。另请参阅 [setTabPosition](https://doc.qt.io/qt-5/qmainwindow.html#setTabPosition) ()|
|`QMainWindow::GroupedDragging`|`0x20`| 拖动停靠部件的标题栏时，将拖动所有和它在一起的停靠部件。包含了 AllowTabbedDocks 。在某些停靠部件有区域限制时会有问题。（该枚举值在 Qt 5.6 添加）|

这些选项只是控制停靠部件将如何放入 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html)，不会重新排列停靠部件。所以要先给停靠部件设置这些选项，再添加到主窗口。AnimatedDocks 和 VerticalTabs 选项例外，它们可以随后设置。

此枚举值在 Qt 4.3 引入和修改

DockOptions 是 [QFlags](https://doc.qt.io/qt-5/qflags.html)\<DockOption> 的 typedef。它存储 DockOption 值的 OR 组合。

## 属性文档

### animated : bool

此属性表示是否对操作停靠部件和工具栏进行动画处理

当停靠部件或工具栏在主窗口拖动时，主窗口会显示它们将停靠在什么位置。设置此属性使 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 在平滑动画中移动其内容。清除此属性会使它们啪地进入新位置。

默认情况，此属性是生效的。如果主窗口调整尺寸或重绘太慢，可能会无效。

设置此属性与使用 [setDockOptions](https://doc.qt.io/qt-5/qmainwindow.html#dockOptions-prop) () 设置 [AnimatedDocks](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) 选项相同。

该属性在 Qt 4.2 引入

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|bool|isAnimated() const|
|void|setAnimated(bool enabled)|

### dockNestingEnabled : bool

此属性表示停靠部件是否可以嵌套。

如果此属性为`false`，停靠区域只能是水平的或垂直的一行。如果此属性为`true`，停靠区域所占的区域可以沿任意方向拆分以包含更多的停靠部件。

> 译者注：如果设为 true，两个 dock 可以上面一块，下面一块，显示在一个区域里，如果设为 false，则两个 dock 只能变成选项卡式占用一个区域。

只有在包含大量停靠部件的应用程序中，才需要停靠嵌套。它给用户更大的自由来组织主窗口。但是，当停靠部件拖过主窗口时，停靠嵌套会导致更加复杂和不太直观的行为。

设置此属性与使用 [setDockOptions](https://doc.qt.io/qt-5/qmainwindow.html#dockOptions-prop) () 设置 [AllowNestedDocks](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) 选项相同。

该属性在 Qt 4.2 引入

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|bool|isDockNestingEnabled() const|
|void|setDockNestingEnabled(bool enabled)|

### dockOptions : [DockOptions](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum)

此属性表示 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 的停靠行为

默认值是 [AnimatedDocks](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) | [AllowTabbedDocks](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum)

该属性在 Qt 4.3 引入

**存取函数：**

|返回类型|函数名|
|:----:|:----:|
|QMainWindow::DockOptions|dockOptions() const|
|void|setDockOptions(QMainWindow::DockOptions options)|

### documentMode : bool

此属性决定选项卡式停靠部件的选项卡栏是否为文档模式。

默认为 false

该属性在 Qt 4.5 引入

**存取函数：**

|返回类型|函数名|
|:----:|:----:|
|bool|documentMode() const|
|void|setDocumentMode(bool enabled)|

**另请参阅** [QTabBar::documentMode](https://doc.qt.io/qt-5/qtabbar.html#documentMode-prop)

### iconSize : [QSize](https://doc.qt.io/qt-5/qsize.html)

主窗口工具栏图标的尺寸。

默认是 GUI 样式的默认工具栏图标大小。请注意，使用的图标必须至少具有此大小，因为图标只会缩小。

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|QSize|iconSize() const|
|void|setIconSize(const QSize &iconSize)|

### tabShape : [QTabWidget::TabShape](https://doc.qt.io/qt-5/qtabwidget.html#TabShape-enum)

此属性表示选项卡式停靠部件的选项卡形状。

默认是 [QTabWidget::Rounded](https://doc.qt.io/qt-5/qtabwidget.html#TabShape-enum)

该属性在 Qt 4.5 引入

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|QTabWidget::TabShape|tabShape() const|
|void|setTabShape(QTabWidget::TabShape tabShape)|

**另请参阅** [setTabPosition](https://doc.qt.io/qt-5/qmainwindow.html#setTabPosition) ()

### toolButtonStyle : [Qt::ToolButtonStyle](https://doc.qt.io/qt-5/qt.html#ToolButtonStyle-enum)

主窗口的工具栏按钮样式。

若要使工具按钮的样式遵循系统设置，请将此属性设置为 [Qt::ToolButtonFollowStyle](https://doc.qt.io/qt-5/qt.html#ToolButtonStyle-enum)。在 Unix 上，将使用桌面环境变量中的用户设置。在其他平台上，[Qt::ToolButtonFollowStyle](https://doc.qt.io/qt-5/qt.html#ToolButtonStyle-enum) 意思是仅显示图标。

默认是 [Qt::ToolButtonIconOnly](https://doc.qt.io/qt-5/qt.html#ToolButtonStyle-enum)

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|Qt::ToolButtonStyle|toolButtonStyle() const|
|void|setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)|

### unifiedTitleAndToolBarOnMac : bool

此属性表示窗口是否使用 macOS 上的统一标题和工具栏外观

请注意，与 Qt 4 相比，Qt 5 实现有几个限制：

- 不支持在包含 OpenGL 内容的窗口中使用。这包括 QGLWidget 和 [QOpenGLWidget](https://doc.qt.io/qt-5/qopenglwidget.html)。
- 使用可停靠或可移动工具栏可能会导致绘制错误，不建议使用。

该属性在 Qt 5.2 引入

**存取函数：**
|返回类型|函数名|
|:----:|:----:|
|bool|unifiedTitleAndToolBarOnMac() const|
|void|setUnifiedTitleAndToolBarOnMac(bool set)|

## 成员函数文档

### QMainWindow::QMainWindow([QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*parent = nullptr, [Qt::WindowFlags](https://doc.qt.io/qt-5/qt.html#WindowType-enum) flags = Qt::WindowFlags())

主窗口构造函数，指定 *parent* 和 *flags*

主窗口设置了 [Qt::Window](https://doc.qt.io/qt-5/qt.html#WindowType-enum) 标志，因此它总作为顶层窗口被创建。

### `[signal]`void QMainWindow::iconSizeChanged(const [QSize](https://doc.qt.io/qt-5/qsize.html) &iconSize)

当窗口图标被改变时，将发出此信号。新图标的尺寸为 *iconSize*。

您可以将此信号连接到其他组件，以帮助保持应用程序的一致外观。

**另请参阅** [setIconSize](https://doc.qt.io/qt-5/qmainwindow.html#iconSize-prop) ().

### `[signal]`void QMainWindow::tabifiedDockWidgetActivated([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockWidget)

当通过选择选项卡激活停靠部件时，将发出此信号。 *dockWidget* 表示激活的停靠部件。

该函数在 Qt 5.8 引入

**另请参阅** [tabifyDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#tabifyDockWidget)() and [tabifiedDockWidgets](https://doc.qt.io/qt-5/qmainwindow.html#tabifiedDockWidgets)()

### `[signal]`void QMainWindow::toolButtonStyleChanged([Qt::ToolButtonStyle](https://doc.qt.io/qt-5/qt.html#ToolButtonStyle-enum) toolButtonStyle)

当窗口的工具栏按钮样式更改时，将发出此信号。*toolButtonStyle* 表示新样式。

您可以将此信号连接到其他组件，以帮助保持应用程序的一致外观。

**另请参阅** [setToolButtonStyle](https://doc.qt.io/qt-5/qmainwindow.html#toolButtonStyle-prop) ()

### `[virtual]`QMainWindow::~QMainWindow()

销毁主窗口

### void QMainWindow::addDockWidget([Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) area, [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget)

添加指定 *dockwidget* 到指定 *area*.

### void QMainWindow::addDockWidget([Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) area, [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget, [Qt::Orientation](https://doc.qt.io/qt-5/qt.html#Orientation-enum) orientation)

将 *dockwidget* 添加到指定的 *area*，方向由 *orientation* 指定。

### void QMainWindow::addToolBar([Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum) area, [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*toolbar)

在主窗口中将 *toolbar* 添加到指定的 *area*。*toolbar* 放置在当前工具栏块（比如分隔符）的后面。如果主窗口已管理 *toolbar*，则只会将工具栏移动到 *area*。

**另请参阅** [insertToolBar](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBar) ()，[addToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#addToolBarBreak) () 和 [insertToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBarBreak) ()

### void QMainWindow::addToolBar([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*toolbar)

这是一个重载函数。

相当于调用 addToolBar([Qt::TopToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum), *toolbar*)

### [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*QMainWindow::addToolBar(const [QString](https://doc.qt.io/qt-5/qstring.html) &title)

这是一个重载函数。

创建 [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) 的一个对象，设置它的窗口标题为 *title* 并将它添加到上方的工具栏区域。

**另请参阅** [setWindowTitle](https://doc.qt.io/qt-5/qwidget.html#windowTitle-prop) ()

### void QMainWindow::addToolBarBreak([Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum) area = Qt::TopToolBarArea)

添加一个工具栏 break。这时，新添加的工具条将不再紧跟前一个工具条，而是另起一行。

### [QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*QMainWindow::centralWidget() const

返回主窗口的中央部件。如果尚未设置中央部件，则此函数返回零。

**另请参阅** [setCentralWidget](https://doc.qt.io/qt-5/qmainwindow.html#setCentralWidget) ()

### `[override virtual protected]`void QMainWindow::contextMenuEvent([QContextMenuEvent](https://doc.qt.io/qt-5/qcontextmenuevent.html) \*event)

重写：[QWidget::contextMenuEvent](https://doc.qt.io/qt-5/qwidget.html#contextMenuEvent) (QContextMenuEvent *event)

### [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) QMainWindow::corner([Qt::Corner](https://doc.qt.io/qt-5/qt.html#Corner-enum) corner) const

返回占用指定 *corner* 的停靠部件区域。

**另请参阅** [setCorner](https://doc.qt.io/qt-5/qmainwindow.html#setCorner) ()

### `[virtual]`[QMenu](https://doc.qt.io/qt-5/qmenu.html) \*QMainWindow::createPopupMenu()

返回一个弹出式菜单，其中包含主窗口中存在的工具栏和停靠部件的可选中条目。如果没有工具栏和停靠小部件，则此函数将返回`nullptr`。

默认情况下，当用户激活上下文菜单时，主窗口会调用此函数，通常通过右键单击工具栏或停靠部件。

如果要创建自定义弹出式菜单，请重新实现此功能并返回新创建的弹出式菜单。弹出式菜单的所有权将传输到调用方。

**另请参阅** [addDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#addDockWidget) ()，[addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar) () 和 [menuBar](https://doc.qt.io/qt-5/qmainwindow.html#menuBar) ()

### [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) QMainWindow::dockWidgetArea([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget) const

返回 *dockwidget* 的 [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum)。如果 *dockwidget* 没有被加入主窗口，此函数返回`Qt::NoDockWidgetArea`

**另请参阅** [addDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#addDockWidget) ()，[splitDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#splitDockWidget) () 和 [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum)

### `[override virtual protected]`bool QMainWindow::event([QEvent](https://doc.qt.io/qt-5/qevent.html) \*event)

重写：[QWidget::event](https://doc.qt.io/qt-5/qwidget.html#event) (QEvent \*event)

### void QMainWindow::insertToolBar([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*before, [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*toolbar)

将 *toolbar* 插入到 *before* 工具栏占用的区域之前。例如，在正常的从左到右布局操作中，*toolbar* 将显示在水平工具栏区域中 *before* 工具栏的左侧。

**另请参阅** [insertToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBarBreak) ()，[addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar) () 和 [addToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#addToolBarBreak) ()

### void QMainWindow::insertToolBarBreak([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*before)

在 *before* 工具栏左侧插入一个工具栏 break。

### [QMenuBar](https://doc.qt.io/qt-5/qmenubar.html) \*QMainWindow::menuBar() const

返回主窗口的菜单栏。如果菜单栏不存在，则此函数将创建并返回一个空菜单栏。

如果希望 Mac 应用程序中的所有窗口共享一个菜单栏，请不要使用此函数来创建它，因为此处创建的菜单栏将把 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 作为它的父对象。必须创建一个没有父对象的菜单栏，然后可以在所有 Mac 窗口之间共享该菜单栏。这样创建：

```c++
QMenuBar *menuBar = new QMenuBar(nullptr);
```

**另请参阅** [setMenuBar](https://doc.qt.io/qt-5/qmainwindow.html#setMenuBar) ()

### [QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*QMainWindow::menuWidget() const

返回主窗口的菜单栏。如果尚未构造菜单栏，返回 null。

该函数在 Qt 4.2 引入

**另请参阅** [setMenuWidget](https://doc.qt.io/qt-5/qmainwindow.html#setMenuWidget) ()

### void QMainWindow::removeDockWidget([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget)

从主窗口布局中移除 *dockwidget* 并将其隐藏。注意，*dockwidget* 没有被 *delete*。

### void QMainWindow::removeToolBar([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*toolbar)

从主窗口布局中移除 *toolbar* 并将其隐藏。注意，*toolbar* 没有被 *delete*。

### void QMainWindow::removeToolBarBreak([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*before)

删除 *before* 工具栏之前的一个工具栏 break。

### void QMainWindow::resizeDocks(const [QList](https://doc.qt.io/qt-5/qlist.html)\<[QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*> &docks, const [QList](https://doc.qt.io/qt-5/qlist.html)\<int> &sizes, [Qt::Orientation](https://doc.qt.io/qt-5/qt.html#Orientation-enum) orientation)

将 *docks* 列表中的停靠部件调整为 *sizes* 列表中的相应尺寸（以像素为单位）。如果 *orientation* 为 [Qt::Horizontal](https://doc.qt.io/qt-5/qt.html#Orientation-enum)，则调整宽度，否则调整高度。尺寸会调整，以遵守设置的最大尺寸和最小尺寸，并且 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 本身不会调整大小。任何多余或缺少的空间将根据尺寸的相对权重分布在部件之间。

示例：

```c++
    resizeDocks({blueWidget, yellowWidget}, {20 , 40}, Qt::Horizontal);
```

如果蓝色和黄色部件嵌套在同一级别上，它们将被调整大小，使黄色部件是蓝色部件的两倍大

如果某些部件在选项卡中分组，则每个组只应指定一个部件。不在列表中的部件可能会改变以遵守约束。

该函数在 Qt 5.6 引入

### bool QMainWindow::restoreDockWidget([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget)

如果在调用 [restoreState](https://doc.qt.io/qt-5/qmainwindow.html#restoreState) () 后创建 *dockwidget* 的状态，则恢复状态。如果状态已恢复，则返回`true`；否则返回`false`。

**另请参阅** [restoreState](https://doc.qt.io/qt-5/qmainwindow.html#restoreState) () 和 [saveState](https://doc.qt.io/qt-5/qmainwindow.html#saveState) ()

### bool QMainWindow::restoreState(const [QByteArray](https://doc.qt.io/qt-5/qbytearray.html) &state, int version = 0)

还原主窗口工具栏和停靠部件的 *state*。也恢复 corner 的设置。*version* 编号与存储在 *state* 中的号码进行比较。如果它们不匹配，主窗口的状态保持不变，并且函数将返回`false`；否则，状态将恢复，函数返回 `true`。

若要恢复用 [QSettings](https://doc.qt.io/qt-5/qsettings.html) 保存的窗口 geometry，可以这么写：

```c++
void MainWindow::readSettings()
{
    QSettings settings("MyCompany", "MyApp");
    restoreGeometry(settings.value("myWidget/geometry").toByteArray());
    restoreState(settings.value("myWidget/windowState").toByteArray());
}
```

**另请参阅** [saveState](https://doc.qt.io/qt-5/qmainwindow.html#saveState) ()，[QWidget::saveGeometry](https://doc.qt.io/qt-5/qwidget.html#saveGeometry) ()，[QWidget::restoreGeometry](https://doc.qt.io/qt-5/qwidget.html#restoreGeometry) () 和 [restoreDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#restoreDockWidget) ()

### [QByteArray](https://doc.qt.io/qt-5/qbytearray.html) QMainWindow::saveState(int version = 0) const

保存主窗口工具栏和停靠部件的当前状态。这包括用 [setCorner](https://doc.qt.io/qt-5/qmainwindow.html#setCorner) () 设置的角落区域。*version* 作为数据的一部分存储。

[objectName](https://doc.qt.io/qt-5/qobject.html#objectName-prop) 属性用于标识每个 [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) 和 [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html)。您应该确保此属性对于添加到 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 的每个 [QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) 和 [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 是唯一的。

要还原保存的状态，请传递返回值和 *version* 给 [restoreState](https://doc.qt.io/qt-5/qmainwindow.html#restoreState) ()。

若要在窗口关闭时保存 geometry，可以这样实现关闭事件：

```c++
void MyMainWindow::closeEvent(QCloseEvent *event)
{
    QSettings settings("MyCompany", "MyApp");
    settings.setValue("geometry", saveGeometry());
    settings.setValue("windowState", saveState());
    QMainWindow::closeEvent(event);
}
```

**另请参阅** [restoreState](https://doc.qt.io/qt-5/qmainwindow.html#restoreState) ()， [QWidget::saveGeometry](https://doc.qt.io/qt-5/qwidget.html#saveGeometry) () 和 [QWidget::restoreGeometry](https://doc.qt.io/qt-5/qwidget.html#restoreGeometry) ()

### void QMainWindow::setCentralWidget([QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*widget)

将主窗口的中央部件设置为 *widget*。

注意： [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 拥有 *widget* 指针的所有权，会在适当的时间将其删除。

**另请参阅** [centralWidget](https://doc.qt.io/qt-5/qmainwindow.html#centralWidget) ()

### void QMainWindow::setCorner([Qt::Corner](https://doc.qt.io/qt-5/qt.html#Corner-enum) corner, [Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) area)

用停靠部件 *area* 占据指定的 *corner*。

**另请参阅** [corner](https://doc.qt.io/qt-5/qmainwindow.html#corner) ()

### void QMainWindow::setMenuBar([QMenuBar](https://doc.qt.io/qt-5/qmenubar.html) \*menuBar)

将主窗口的菜单栏设置为 *menuBar*。

注意： [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 拥有 *menuBar* 指针的所有权，会在适当的时间将其删除。

**另请参阅** [menuBar](https://doc.qt.io/qt-5/qmainwindow.html#menuBar) ()

### void QMainWindow::setMenuWidget([QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*menuBar)

将主窗口的菜单栏设置为 *menuBar*。

[QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 拥有 *menuBar* 指针的所有权，会在适当的时间将其删除。

该函数在 Qt 4.2 引入

**另请参阅** [menuWidget](https://doc.qt.io/qt-5/qmainwindow.html#menuWidget) ()

### void QMainWindow::setStatusBar([QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html) \*statusbar)

将主窗口的状态栏设置为 *statusbar*。

将状态栏设置为`nullptr`会将其从主窗口中删除。请注意，[QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html)  拥有 *statusbar* 指针的所有权，会在适当的时间将其删除。

**另请参阅** [statusBar](https://doc.qt.io/qt-5/qmainwindow.html#statusBar) ()

### void QMainWindow::setTabPosition([Qt::DockWidgetAreas](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) areas, [QTabWidget::TabPosition](https://doc.qt.io/qt-5/qtabwidget.html#TabPosition-enum) tabPosition)

将停靠部件 *areas* 的选项卡位置设置为指定的 *tabPosition*。默认情况下，所有停靠区域在底部显示其选项卡。

**注意** [VerticalTabs](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) 会覆盖此方法设置的选项卡位置

该函数在 Qt 4.5 引入

**另请参阅** [tabPosition](https://doc.qt.io/qt-5/qmainwindow.html#tabPosition) () 和 [setTabShape](https://doc.qt.io/qt-5/qmainwindow.html#tabShape-prop) ()

### void QMainWindow::splitDockWidget([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*first, [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*second, [Qt::Orientation](https://doc.qt.io/qt-5/qt.html#Orientation-enum) orientation)

分割停靠部件 *first* 为两个停靠部件，第一个部件指针传给 *first*，第二个部件指针传给 *second*。

*orientation* 指定了空间的划分。[Qt::Horizontal](https://doc.qt.io/qt-5/qt.html#Orientation-enum) 左右分割；[Qt::Vertical](https://doc.qt.io/qt-5/qt.html#Orientation-enum) 上下分割。

*注意*：如果 *first* 位于选项卡式停靠区域中，则 *second* 将添加为新选项卡，这是因为单个选项卡只能包含一个停靠部件。

*注意*：[Qt::LayoutDirection](https://doc.qt.io/qt-5/qt.html#LayoutDirection-enum) 会影响两个分割区域的停靠部件顺序。启用从右到左布局方向时，将反转停靠部件的位置。

**另请参阅** [tabifyDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#tabifyDockWidget)(), [addDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#addDockWidget) () 和 [removeDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#removeDockWidget) ()

### [QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html) \*QMainWindow::statusBar() const

返回主窗口的状态栏。如果状态栏不存在，则此函数将创建并返回一个空状态栏。

**另请参阅** [setStatusBar](https://doc.qt.io/qt-5/qmainwindow.html#setStatusBar) ()

### [QTabWidget::TabPosition](https://doc.qt.io/qt-5/qtabwidget.html#TabPosition-enum) QMainWindow::tabPosition([Qt::DockWidgetArea](https://doc.qt.io/qt-5/qt.html#DockWidgetArea-enum) area) const

返回停靠区域 *area* 的位置。

**注意** 如果设置了 [VerticalTabs](https://doc.qt.io/qt-5/qmainwindow.html#DockOption-enum) ，会覆盖此函数的返回值。

该函数在 Qt 4.5 引入

**另请参阅** [setTabPosition](https://doc.qt.io/qt-5/qmainwindow.html#setTabPosition) () 和 [tabShape](https://doc.qt.io/qt-5/qmainwindow.html#tabShape-prop) ()

### [QList](https://doc.qt.io/qt-5/qlist.html)\<[QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*> QMainWindow::tabifiedDockWidgets([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*dockwidget) const

返回 *dockwidget* 内堆叠着的停靠部件。

该函数在 Qt 4.5 引入

**另请参阅** [tabifyDockWidget](https://doc.qt.io/qt-5/qmainwindow.html#tabifyDockWidget) ()

### void QMainWindow::tabifyDockWidget([QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*first, [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) \*second)

将 *second* 停靠部件移动到 *first* 停靠部件旁形成一个选项卡式停靠区域。

**另请参阅** [tabifiedDockWidgets](https://doc.qt.io/qt-5/qmainwindow.html#tabifiedDockWidgets) ()

### [QWidget](https://doc.qt.io/qt-5/qwidget.html#QWidget) \*QMainWindow::takeCentralWidget()

从主窗口中移除中央部件。

返回中央部件的指针。

该函数在 Qt 5.2 引入

### [Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum) QMainWindow::toolBarArea([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) \*toolbar) const

返回 *toolbar* 的 [Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum)。 如果主窗口没有添加 *toolbar* ，返回 `Qt::NoToolBarArea`。

**另请参阅** [addToolBar](https://doc.qt.io/qt-5/qmainwindow.html#addToolBar) ()， [addToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#addToolBarBreak) () 和 [Qt::ToolBarArea](https://doc.qt.io/qt-5/qt.html#ToolBarArea-enum)

### bool QMainWindow::toolBarBreak([QToolBar](https://doc.qt.io/qt-5/qtoolbar.html) **toolbar*) const

返回 *toolbar* 之前是否有工具栏 break。

**另请参阅** [addToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#addToolBarBreak) () 和 [insertToolBarBreak](https://doc.qt.io/qt-5/qmainwindow.html#insertToolBarBreak) ()