[TOC]



# QWebEngineHistory class

QWebEngineHistory类表示Web引擎页面的历史记录。

| 属性      | 方法                          |
| --------- | ----------------------------- |
| 头文件    | \#include <QWebEngineHistory> |
| qmake参数 | QT + = webenginewidgets       |

该类在Qt 5.4中引入。

## 公有成员函数

| 类型                         | 方法                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| void                         | **[back](https://doc.qt.io/qt-5/qwebenginehistory.html#back)**() |
| QWebEngineHistoryItem        | **[backItem](https://doc.qt.io/qt-5/qwebenginehistory.html#backItem)**() const |
| QList<QWebEngineHistoryItem> | **[backItems](https://doc.qt.io/qt-5/qwebenginehistory.html#backItems)**(int *maxItems*) const |
| bool                         | **[canGoBack](https://doc.qt.io/qt-5/qwebenginehistory.html#canGoBack)**() const |
| bool                         | **[canGoForward](https://doc.qt.io/qt-5/qwebenginehistory.html#canGoForward)**() const |
| void                         | **[clear](https://doc.qt.io/qt-5/qwebenginehistory.html#clear)**() |
| int                          | **[count](https://doc.qt.io/qt-5/qwebenginehistory.html#count)**() const |
| QWebEngineHistoryItem        | **[currentItem](https://doc.qt.io/qt-5/qwebenginehistory.html#currentItem)**() const |
| int                          | **[currentItemIndex](https://doc.qt.io/qt-5/qwebenginehistory.html#currentItemIndex)**() const |
| void                         | **[forward](https://doc.qt.io/qt-5/qwebenginehistory.html#forward)**() |
| QWebEngineHistoryItem        | **[forwardItem](https://doc.qt.io/qt-5/qwebenginehistory.html#forwardItem)**() const |
| QList<QWebEngineHistoryItem> | **[forwardItems](https://doc.qt.io/qt-5/qwebenginehistory.html#forwardItems)**(int *maxItems*) const |
| void                         | **[goToItem](https://doc.qt.io/qt-5/qwebenginehistory.html#goToItem)**(const QWebEngineHistoryItem &*item*) |
| QWebEngineHistoryItem        | **[itemAt](https://doc.qt.io/qt-5/qwebenginehistory.html#itemAt)**(int *i*) const |
| QList<QWebEngineHistoryItem> | **[items](https://doc.qt.io/qt-5/qwebenginehistory.html#items)**() const |

## 相关非成员函数

| 类型          | 方法                                                         |
| ------------- | ------------------------------------------------------------ |
| QDataStream & | **[operator<<](https://doc.qt.io/qt-5/qwebenginehistory.html#operator-lt-lt)**(QDataStream &*stream*, const QWebEngineHistory &*history*) |
| QDataStream & | **[operator>>](https://doc.qt.io/qt-5/qwebenginehistory.html#operator-gt-gt)**(QDataStream &*stream*, QWebEngineHistory &*history*) |

## 详细描述



## 成员函数文档

每个Web引擎页面都包含访问过的页面的历史记录，可以由[QWebEnginePage::history](https://doc.qt.io/qt-5/qwebenginepage.html#history)()得到。

历史记录使用当前项目的概念，通过使用[back](https://doc.qt.io/qt-5/qwebenginehistory.html#back)() 和 [forward](https://doc.qt.io/qt-5/qwebenginehistory.html#forward)()函数来回导航，将访问的页面划分为可以访问的页面。 当前项目可以通过调用 [currentItem](https://doc.qt.io/qt-5/qwebenginehistory.html#currentItem)()获得，并且历史记录中的任意项目都可以通过将其传递给[goToItem](https://doc.qt.io/qt-5/qwebenginehistory.html#goToItem)()使其成为当前项目。

可以通过调用[backItems](https://doc.qt.io/qt-5/qwebenginehistory.html#backItems)()函数获得描述可以返回的页面的项目列表。类似的，可以使用[forwardItems](https://doc.qt.io/qt-5/qwebenginehistory.html#forwardItems)()函数获得描述当前页面之前页面的项目。 项目的总列表是通过 [items](https://doc.qt.io/qt-5/qwebenginehistory.html#items)()函数获得的。

与容器一样，可以使用函数来检查列表中的历史记录。可以使用[itemAt](https://doc.qt.io/qt-5/qwebenginehistory.html#itemAt)()获得历史记录中的任意项目，通过 [count](https://doc.qt.io/qt-5/qwebenginehistory.html#count)()给出项目的总数，并可以使用 [clear](https://doc.qt.io/qt-5/qwebenginehistory.html#clear)() 函数清除历史记录。

可以使用>>运算符将QWebEngineHistory的状态保存到[QDataStream](../../D/QDataStream/QDataStream.md) 中，并使用<<操作符进行加载。

**另外参见** [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) and [QWebEnginePage](../../W/QWebEnginePage.md)。

## 成员函数文档

### void QWebEngineHistory::back()

将当前项目设置为历史记录中的前一个项目，然后转到相应页面； 也就是说，返回一个历史项目。

**See also** [forward](https://doc.qt.io/qt-5/qwebenginehistory.html#forward)() and [goToItem](https://doc.qt.io/qt-5/qwebenginehistory.html#goToItem)().

### [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) QWebEngineHistory::backItem() const

返回历史记录中当前项目之前的项目。

### [QList](../../L/QList/QList.md)<[QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md)> QWebEngineHistory::backItems(int *maxItems*) const

返回向后历史记录列表中的项目列表。 最多返回*maxItems*条目。

**See also** [forwardItems](https://doc.qt.io/qt-5/qwebenginehistory.html#forwardItems)()。

### bool QWebEngineHistory::canGoBack() const

如果历史记录中当前项目之前有一个项目，则返回**true**， 否则返回**false**。

**See also** [canGoForward](https://doc.qt.io/qt-5/qwebenginehistory.html#canGoForward)()。

### bool QWebEngineHistory::canGoForward() const

如果我们有一个项目可以前进，则返回**true**，否则返回**false**。

**See also** [canGoBack](https://doc.qt.io/qt-5/qwebenginehistory.html#canGoBack)()。

### void QWebEngineHistory::clear()

清除历史记录。

**See also** [count](https://doc.qt.io/qt-5/qwebenginehistory.html#count)() and [items](https://doc.qt.io/qt-5/qwebenginehistory.html#items)()。

### int QWebEngineHistory::count() const

返回历史记录中的项目总数。

### [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) QWebEngineHistory::currentItem() const

返回历史记录中的当前项目。

### int QWebEngineHistory::currentItemIndex() const

返回历史记录中当前项目的索引。

### void QWebEngineHistory::forward()

将当前项目设置为历史记录中的下一个项目，然后转到相应页面； 即，前进一个历史项目。

**See also** [back](https://doc.qt.io/qt-5/qwebenginehistory.html#back)() and [goToItem](https://doc.qt.io/qt-5/qwebenginehistory.html#goToItem)()。

### [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) QWebEngineHistory::forwardItem() const

返回历史记录中当前项目之后的项目。

### [QList](../../L/QList/QList.md)<[QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md)> QWebEngineHistory::forwardItems(int *maxItems*) const

返回转发历史记录列表中的项目列表。 最多返回*maxItems*条目。

**See also** [backItems](https://doc.qt.io/qt-5/qwebenginehistory.html#backItems)().

### void QWebEngineHistory::goToItem(const [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) &*item*)

将当前项目设置为历史记录中的指定项目，然后转到页面。

**See also** [back](https://doc.qt.io/qt-5/qwebenginehistory.html#back)() and [forward](https://doc.qt.io/qt-5/qwebenginehistory.html#forward)()。

### [QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md) QWebEngineHistory::itemAt(int *i*) const

返回历史记录中索引i处的项目。

### [QList](../../L/QList/QList.md)<[QWebEngineHistoryItem](../../W/QWebEngineHistoryItem/QWebEngineHistoryItem.md)> QWebEngineHistory::items() const

返回历史记录中当前所有项目的列表。

**See also** [count](https://doc.qt.io/qt-5/qwebenginehistory.html#count)() and [clear](https://doc.qt.io/qt-5/qwebenginehistory.html#clear)()。

## 相关非成员函数

### [QDataStream](../../D/QDataStream/QDataStream.md) &operator<<([QDataStream](../../D/QDataStream/QDataStream.md) &*stream*, const QWebEngineHistory &*history*)

将Web引擎历史记录历史记录保存到流中。

### [QDataStream](../../D/QDataStream/QDataStream.md) &operator>>([QDataStream](../../D/QDataStream/QDataStream.md) &*stream*, QWebEngineHistory &*history*)

将Web引擎历史记录从流加载到历史记录中。