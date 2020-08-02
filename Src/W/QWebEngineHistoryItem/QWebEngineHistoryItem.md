[TOC]



# QWebEngineHistoryItem Class

QWebEngineHistoryItem类表示Web引擎页面历史记录中的一项。

| 属性    | 方法                              |
| ------- | --------------------------------- |
| 头文件: | \#include <QWebEngineHistoryItem> |
| qmake:  | QT += webenginewidgets            |
| 引入:   | Qt 5.4                            |

## 公有成员函数

| 类型                    | 函数                                                         |
| ----------------------- | ------------------------------------------------------------ |
|                         | [QWebEngineHistoryItem](qwebenginehistoryitem.html#QWebEngineHistoryItem)(const QWebEngineHistoryItem &*other*) |
|                         | [~QWebEngineHistoryItem](qwebenginehistoryitem.html#dtor.QWebEngineHistoryItem)() |
| QUrl                    | [iconUrl](qwebenginehistoryitem.html#iconUrl)() const        |
| bool                    | [isValid](qwebenginehistoryitem.html#isValid)() const        |
| QDateTime               | [lastVisited](qwebenginehistoryitem.html#lastVisited)() const |
| QUrl                    | [originalUrl](qwebenginehistoryitem.html#originalUrl)() const |
| void                    | [swap](qwebenginehistoryitem.html#swap)(QWebEngineHistoryItem &*other*) |
| QString                 | [title](qwebenginehistoryitem.html#title)() const            |
| QUrl                    | [url](qwebenginehistoryitem.html#url)() const                |
| QWebEngineHistoryItem & | [operator=](qwebenginehistoryitem.html#operator-eq)(const QWebEngineHistoryItem &*other*) |



## 详细描述

QWebEngineHistoryItem类表示Web引擎页面历史记录中的一项。

每个Web引擎历史记录项都代表一个网页历史记录堆栈中的一个条目，其中包含有关该页面，其位置以及上次访问时间的信息。

另请参见[QWebEngineHistory](qwebenginehistory.html) and [QWebEnginePage::history](qwebenginepage.html#history)()。

## 成员函数文档

### QWebEngineHistoryItem::QWebEngineHistoryItem(const [QWebEngineHistoryItem](qwebenginehistoryitem.html#QWebEngineHistoryItem) &*other*)

从其他构造一个历史项。 新项目和其他项目将共享其数据，并且修改该项目或其他项目将修改两个实例。

### QWebEngineHistoryItem::~QWebEngineHistoryItem()

销毁历史记录项。

### [QUrl](../../U/QUrl.md) QWebEngineHistoryItem::iconUrl() const

返回与历史记录项关联的图标的URL。

See also [url](qwebenginehistoryitem.html#url)(), [originalUrl](qwebenginehistoryitem.html#originalUrl)(), and [title](qwebenginehistoryitem.html#title)()。

### bool QWebEngineHistoryItem::isValid() const

返回这是否是有效的历史记录项。

### [QDateTime](../../D/QDateTime.md) QWebEngineHistoryItem::lastVisited() const

返回上次访问与该项目关联的页面的日期和时间。

See also [title](qwebenginehistoryitem.html#title)() and [url](qwebenginehistoryitem.html#url)()。

### [QUrl](../../U/QUrl.md) QWebEngineHistoryItem::originalUrl() const

返回与历史记录项关联的原始URL。

See also [url](qwebenginehistoryitem.html#url)().

###  void QWebEngineHistoryItem::swap([QWebEngineHistoryItem](qwebenginehistoryitem.html#QWebEngineHistoryItem) &*other*)

将历史项与其他项交换。

### [Q](../qtcore/qstring.html)String QWebEngineHistoryItem::title() const

返回与历史记录项关联的页面的标题。

See also [url](qwebenginehistoryitem.html#url)() and [lastVisited](qwebenginehistoryitem.html#lastVisited)().

###  [QUrl](../../U/QUrl.md) QWebEngineHistoryItem::url() const

返回与历史记录项关联的URL。

See also [originalUrl](qwebenginehistoryitem.html#originalUrl)(), [title](qwebenginehistoryitem.html#title)(), and [lastVisited](qwebenginehistoryitem.html#lastVisited)().

###  QWebEngineHistoryItem &QWebEngineHistoryItem::operator=(const [QWebEngineHistoryItem](qwebenginehistoryitem.html#QWebEngineHistoryItem) &*other*)

为此分配另一个历史记录项。 该项目和其他项目将共享其数据，并且修改该项目或其他项目将修改两个实例。



















