# QAbstractItemView Class

The QAbstractItemView class provides the basic functionality for item view classes. [更多内容...](QAbstractItemView.md#详细描述)

| 头文件:       | #include <QAbstractItemView>                                 |
| -------------: | :------------------------------------------------------------ |
| qmake:        | QT += widgets                                                |
| 基类:     | [QAbstractScrollArea](../../A/QAbstractScrollArea/QAbstractScrollArea.md) |
| 派生类: | [QColumnView](../../C/QColumnView/QColumnView.md), [QHeaderView](../../H/QHeaderView/QHeaderView.md), [QListView](../../L/QListView/QListView.md), [QTableView](../../T/QTableView/QTableView.md), and [QTreeView](../../T/QTreeView/QTreeView.md) |

- [所有成员列表，包括继承的成员](../../A/QAbstractItemView/QAbstractItemView-members.md)
- [废弃的成员](../../A/QAbstractItemView/QAbstractItemView-obsolete.md)



## 公共成员类型

| enum  | **[DragDropMode](QAbstractItemView.md#enum-qabstractitemviewdragdropmode)** { NoDragDrop, DragOnly, DropOnly, DragDrop, InternalMove } |
| -----: | :------------------------------------------------------------ |
| enum  | **[EditTrigger](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers)** { NoEditTriggers, CurrentChanged, DoubleClicked, SelectedClicked, EditKeyPressed, ..., AllEditTriggers } |
| flags | **[EditTriggers](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers)** |
| enum  | **[ScrollHint](QAbstractItemView.md#enum-qabstractitemviewscrollhint)** { EnsureVisible, PositionAtTop, PositionAtBottom, PositionAtCenter } |
| enum  | **[ScrollMode](QAbstractItemView.md#enum-qabstractitemviewscrollmode)** { ScrollPerItem, ScrollPerPixel } |
| enum  | **[SelectionBehavior](QAbstractItemView.md#enum-qabstractitemviewselectionbehavior)** { SelectItems, SelectRows, SelectColumns } |
| enum  | **[SelectionMode](QAbstractItemView.md#enum-qabstractitemviewselectionmode)** { SingleSelection, ContiguousSelection, ExtendedSelection, MultiSelection, NoSelection } |



## 属性

| **[alternatingRowColors](QAbstractItemView.md#alternatingrowcolors--bool)** : bool | **[horizontalScrollMode](QAbstractItemView.md#horizontalscrollmode--scrollmode)** : ScrollMode |
| :------------------------------------------------------------ | :----------------------------------------------------------- |
| **[autoScroll](QAbstractItemView.md#autoscroll--bool)** : bool | **[iconSize](QAbstractItemView.md#iconsize--qsize)** : QSize |
| **[autoScrollMargin](QAbstractItemView.md#autoscrollmargin--int)** : int | **[selectionBehavior](QAbstractItemView.md#selectionbehavior--selectionbehavior)** : SelectionBehavior |
| **[defaultDropAction](QAbstractItemView.md#defaultdropaction--qtdropaction)** : Qt::DropAction | **[selectionMode](QAbstractItemView.md#selectionmode--selectionmode)** : SelectionMode |
| **[dragDropMode](QAbstractItemView.md#dragdropmode--dragdropmode)** : DragDropMode | **[showDropIndicator](QAbstractItemView.md#showdropindicator--bool)** : bool |
| **[dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool)** : bool | **[tabKeyNavigation](QAbstractItemView.md#tabkeynavigation--bool)** : bool |
| **[dragEnabled](QAbstractItemView.md#dragenabled--bool)** : bool | **[textElideMode](QAbstractItemView.md#textelidemode--qttextelidemode)** : Qt::TextElideMode |
| **[editTriggers](QAbstractItemView.md#edittriggers--edittriggers)** : EditTriggers | **[verticalScrollMode](QAbstractItemView.md#verticalscrollmode--scrollmode)** : ScrollMode |



## 公共成员函数

|                                      | **[QAbstractItemView](QAbstractItemView.md#qabstractitemviewqabstractitemviewqwidget-parent--nullptr)**(QWidget **parent* = nullptr) |
| ------------------------------------: | :------------------------------------------------------------ |
| virtual                              | **[~QAbstractItemView](QAbstractItemView.md#virtualqabstractitemviewqabstractitemview)**() |
| bool                                 | **[alternatingRowColors](QAbstractItemView.md#alternatingrowcolors--bool)**() const |
| int                                  | **[autoScrollMargin](QAbstractItemView.md#autoscrollmargin--int)**() const |
| void                                 | **[closePersistentEditor](QAbstractItemView.md#void-qabstractitemviewclosepersistenteditorconst-qmodelindex-index)**(const QModelIndex &*index*) |
| QModelIndex                          | **[currentIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewcurrentindex-const)**() const |
| Qt::DropAction                       | **[defaultDropAction](QAbstractItemView.md#defaultdropaction--qtdropaction)**() const |
| QAbstractItemView::DragDropMode      | **[dragDropMode](QAbstractItemView.md#dragdropmode--dragdropmode)**() const |
| bool                                 | **[dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool)**() const |
| bool                                 | **[dragEnabled](QAbstractItemView.md#dragenabled--bool)**() const |
| QAbstractItemView::EditTriggers      | **[editTriggers](QAbstractItemView.md#edittriggers--edittriggers)**() const |
| bool                                 | **[hasAutoScroll](QAbstractItemView.md#autoscroll--bool)**() const |
| QAbstractItemView::ScrollMode        | **[horizontalScrollMode](QAbstractItemView.md#horizontalscrollmode--scrollmode)**() const |
| QSize                                | **[iconSize](QAbstractItemView.md#iconsize--qsize)**() const |
| virtual QModelIndex                  | **[indexAt](QAbstractItemView.md#pure-virtualqmodelindex-qabstractitemviewindexatconst-qpoint-point-const)**(const QPoint &*point*) const = 0 |
| QWidget *                            | **[indexWidget](QAbstractItemView.md#qwidget-qabstractitemviewindexwidgetconst-qmodelindex-index-const)**(const QModelIndex &*index*) const |
| bool                                 | **[isPersistentEditorOpen](QAbstractItemView.md#bool-qabstractitemviewispersistenteditoropenconst-qmodelindex-index-const)**(const QModelIndex &*index*) const |
| QAbstractItemDelegate *              | **[itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)**() const |
| QAbstractItemDelegate *              | **[itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateconst-qmodelindex-index-const)**(const QModelIndex &*index*) const |
| QAbstractItemDelegate *              | **[itemDelegateForColumn](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforcolumnint-column-const)**(int *column*) const |
| QAbstractItemDelegate *              | **[itemDelegateForRow](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforrowint-row-const)**(int *row*) const |
| virtual void                         | **[keyboardSearch](QAbstractItemView.md#virtualvoid-qabstractitemviewkeyboardsearchconst-qstring-search)**(const QString &*search*) |
| QAbstractItemModel *                 | **[model](QAbstractItemView.md#qabstractitemmodel-qabstractitemviewmodel-const)**() const |
| void                                 | **[openPersistentEditor](QAbstractItemView.md#void-qabstractitemviewopenpersistenteditorconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void                                 | **[resetHorizontalScrollMode](QAbstractItemView.md#horizontalscrollmode--scrollmode)**() |
| void                                 | **[resetVerticalScrollMode](QAbstractItemView.md#verticalscrollmode--scrollmode)**() |
| QModelIndex                          | **[rootIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewrootindex-const)**() const |
| virtual void                         | **[scrollTo](QAbstractItemView.md#pure-virtualvoid-qabstractitemviewscrolltoconst-qmodelindex-index-qabstractitemviewscrollhint-hint--ensurevisible)**(const QModelIndex &*index*, QAbstractItemView::ScrollHint *hint* = EnsureVisible) = 0 |
| QAbstractItemView::SelectionBehavior | **[selectionBehavior](QAbstractItemView.md#selectionbehavior--selectionbehavior)**() const |
| QAbstractItemView::SelectionMode     | **[selectionMode](QAbstractItemView.md#selectionmode--selectionmode)**() const |
| QItemSelectionModel *                | **[selectionModel](QAbstractItemView.md#qitemselectionmodel-qabstractitemviewselectionmodel-const)**() const |
| void                                 | **[setAlternatingRowColors](QAbstractItemView.md#alternatingrowcolors--bool)**(bool *enable*) |
| void                                 | **[setAutoScroll](QAbstractItemView.md#autoscroll--bool)**(bool *enable*) |
| void                                 | **[setAutoScrollMargin](QAbstractItemView.md#autoscrollmargin--int)**(int *margin*) |
| void                                 | **[setDefaultDropAction](QAbstractItemView.md#defaultdropaction--qtdropaction)**(Qt::DropAction *dropAction*) |
| void                                 | **[setDragDropMode](QAbstractItemView.md#dragdropmode--dragdropmode)**(QAbstractItemView::DragDropMode *behavior*) |
| void                                 | **[setDragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool)**(bool *overwrite*) |
| void                                 | **[setDragEnabled](QAbstractItemView.md#dragenabled--bool)**(bool *enable*) |
| void                                 | **[setDropIndicatorShown](QAbstractItemView.md#showdropindicator--bool)**(bool *enable*) |
| void                                 | **[setEditTriggers](QAbstractItemView.md#edittriggers--edittriggers)**(QAbstractItemView::EditTriggers *triggers*) |
| void                                 | **[setHorizontalScrollMode](QAbstractItemView.md#horizontalscrollmode--scrollmode)**(QAbstractItemView::ScrollMode *mode*) |
| void                                 | **[setIconSize](QAbstractItemView.md#iconsize--qsize)**(const QSize &*size*) |
| void                                 | **[setIndexWidget](QAbstractItemView.md#void-qabstractitemviewsetindexwidgetconst-qmodelindex-index-qwidget-widget)**(const QModelIndex &*index*, QWidget **widget*) |
| void                                 | **[setItemDelegate](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateqabstractitemdelegate-delegate)**(QAbstractItemDelegate **delegate*) |
| void                                 | **[setItemDelegateForColumn](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforcolumnint-column-qabstractitemdelegate-delegate)**(int *column*, QAbstractItemDelegate **delegate*) |
| void                                 | **[setItemDelegateForRow](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforrowint-row-qabstractitemdelegate-delegate)**(int *row*, QAbstractItemDelegate **delegate*) |
| virtual void                         | **[setModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetmodelqabstractitemmodel-model)**(QAbstractItemModel **model*) |
| void                                 | **[setSelectionBehavior](QAbstractItemView.md#selectionbehavior--selectionbehavior)**(QAbstractItemView::SelectionBehavior *behavior*) |
| void                                 | **[setSelectionMode](QAbstractItemView.md#selectionmode--selectionmode)**(QAbstractItemView::SelectionMode *mode*) |
| virtual void                         | **[setSelectionModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetselectionmodelqitemselectionmodel-selectionmodel)**(QItemSelectionModel **selectionModel*) |
| void                                 | **[setTabKeyNavigation](QAbstractItemView.md#tabkeynavigation--bool)**(bool *enable*) |
| void                                 | **[setTextElideMode](QAbstractItemView.md#textelidemode--qttextelidemode)**(Qt::TextElideMode *mode*) |
| void                                 | **[setVerticalScrollMode](QAbstractItemView.md#verticalscrollmode--scrollmode)**(QAbstractItemView::ScrollMode *mode*) |
| bool                                 | **[showDropIndicator](QAbstractItemView.md#showdropindicator--bool)**() const |
| virtual int                          | **[sizeHintForColumn](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforcolumnint-column-const)**(int *column*) const |
| QSize                                | **[sizeHintForIndex](QAbstractItemView.md#qsize-qabstractitemviewsizehintforindexconst-qmodelindex-index-const)**(const QModelIndex &*index*) const |
| virtual int                          | **[sizeHintForRow](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforrowint-row-const)**(int *row*) const |
| bool                                 | **[tabKeyNavigation](QAbstractItemView.md#tabkeynavigation--bool)**() const |
| Qt::TextElideMode                    | **[textElideMode](QAbstractItemView.md#textelidemode--qttextelidemode)**() const |
| QAbstractItemView::ScrollMode        | **[verticalScrollMode](QAbstractItemView.md#verticalscrollmode--scrollmode)**() const |
| virtual QRect                        | **[visualRect](QAbstractItemView.md#pure-virtualqrect-qabstractitemviewvisualrectconst-qmodelindex-index-const)**(const QModelIndex &*index*) const = 0 |



## 重写公共成员函数

| virtual QVariant | **[inputMethodQuery](QAbstractItemView.md#override-virtualqvariant-qabstractitemviewinputmethodqueryqtinputmethodquery-query-const)**(Qt::InputMethodQuery *query*) const override |
| ----------------: | :------------------------------------------------------------ |
|                  |                                                              |



## 公共槽函数

| void         | **[clearSelection](QAbstractItemView.md#slotvoid-qabstractitemviewclearselection)**() |
| ------------: | :------------------------------------------------------------ |
| void         | **[edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)**(const QModelIndex &*index*) |
| virtual void | **[reset](QAbstractItemView.md#virtual-slotvoid-qabstractitemviewreset)**() |
| void         | **[scrollToBottom](QAbstractItemView.md#slotvoid-qabstractitemviewscrolltobottom)**() |
| void         | **[scrollToTop](QAbstractItemView.md#slotvoid-qabstractitemviewscrolltotop)**() |
| virtual void | **[selectAll](QAbstractItemView.md#virtual-slotvoid-qabstractitemviewselectall)**() |
| void         | **[setCurrentIndex](QAbstractItemView.md#slotvoid-qabstractitemviewsetcurrentindexconst-qmodelindex-index)**(const QModelIndex &*index*) |
| virtual void | **[setRootIndex](QAbstractItemView.md#virtual-slotvoid-qabstractitemviewsetrootindexconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void         | **[update](QAbstractItemView.md#slotvoid-qabstractitemviewupdateconst-qmodelindex-index)**(const QModelIndex &*index*) |



## 信号

| void | **[activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)**(const QModelIndex &*index*) |
| ----: | :------------------------------------------------------------ |
| void | **[clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void | **[doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void | **[entered](QAbstractItemView.md#signalvoid-qabstractitemviewenteredconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void | **[iconSizeChanged](QAbstractItemView.md#iconsize--qsize)**(const QSize &*size*) |
| void | **[pressed](QAbstractItemView.md#signalvoid-qabstractitemviewpressedconst-qmodelindex-index)**(const QModelIndex &*index*) |
| void | **[viewportEntered](QAbstractItemView.md#signalvoid-qabstractitemviewviewportentered)**() |



## 保护成员类型

| enum | **[CursorAction](QAbstractItemView.md#enum-qabstractitemviewcursoraction)** { MoveUp, MoveDown, MoveLeft, MoveRight, MoveHome, ..., MovePrevious } |
| ----: | :------------------------------------------------------------ |
| enum | **[DropIndicatorPosition](QAbstractItemView.md#enum-qabstractitemviewdropindicatorposition)** { OnItem, AboveItem, BelowItem, OnViewport } |
| enum | **[State](QAbstractItemView.md#enum-qabstractitemviewstate)** { NoState, DraggingState, DragSelectingState, EditingState, ExpandingState, ..., AnimatingState } |



## 保护成员函数

| QPoint                                      | **[dirtyRegionOffset](QAbstractItemView.md#protectedqpoint-qabstractitemviewdirtyregionoffset-const)**() const |
| -------------------------------------------: | :------------------------------------------------------------ |
| QAbstractItemView::DropIndicatorPosition    | **[dropIndicatorPosition](QAbstractItemView.md#protectedqabstractitemviewdropindicatorposition-qabstractitemviewdropindicatorposition-const)**() const |
| virtual bool                                | **[edit](QAbstractItemView.md#virtual-protectedbool-qabstractitemvieweditconst-qmodelindex-index-qabstractitemviewedittrigger-trigger-qevent-event)**(const QModelIndex &*index*, QAbstractItemView::EditTrigger *trigger*, QEvent **event*) |
| void                                        | **[executeDelayedItemsLayout](QAbstractItemView.md#protectedvoid-qabstractitemviewexecutedelayeditemslayout)**() |
| virtual int                                 | **[horizontalOffset](QAbstractItemView.md#pure-virtual-protectedint-qabstractitemviewhorizontaloffset-const)**() const = 0 |
| virtual bool                                | **[isIndexHidden](QAbstractItemView.md#pure-virtual-protectedbool-qabstractitemviewisindexhiddenconst-qmodelindex-index-const)**(const QModelIndex &*index*) const = 0 |
| virtual QModelIndex                         | **[moveCursor](QAbstractItemView.md#pure-virtual-protectedqmodelindex-qabstractitemviewmovecursorqabstractitemviewcursoraction-cursoraction-qtkeyboardmodifiers-modifiers)**(QAbstractItemView::CursorAction *cursorAction*, Qt::KeyboardModifiers *modifiers*) = 0 |
| void                                        | **[scheduleDelayedItemsLayout](QAbstractItemView.md#protectedvoid-qabstractitemviewscheduledelayeditemslayout)**() |
| void                                        | **[scrollDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewscrolldirtyregionint-dx-int-dy)**(int *dx*, int *dy*) |
| virtual QModelIndexList                     | **[selectedIndexes](QAbstractItemView.md#virtual-protectedqmodelindexlist-qabstractitemviewselectedindexes-const)**() const |
| virtual QItemSelectionModel::SelectionFlags | **[selectionCommand](QAbstractItemView.md#virtual-protectedqitemselectionmodelselectionflags-qabstractitemviewselectioncommandconst-qmodelindex-index-const-qevent-event--nullptr-const)**(const QModelIndex &*index*, const QEvent **event* = nullptr) const |
| void                                        | **[setDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewsetdirtyregionconst-qregion-region)**(const QRegion &*region*) |
| virtual void                                | **[setSelection](QAbstractItemView.md#pure-virtual-protectedvoid-qabstractitemviewsetselectionconst-qrect-rect-qitemselectionmodelselectionflags-flags)**(const QRect &*rect*, QItemSelectionModel::SelectionFlags *flags*) = 0 |
| void                                        | **[setState](QAbstractItemView.md#protectedvoid-qabstractitemviewsetstateqabstractitemviewstate-state)**(QAbstractItemView::State *state*) |
| virtual void                                | **[startDrag](QAbstractItemView.md#virtual-protectedvoid-qabstractitemviewstartdragqtdropactions-supportedactions)**(Qt::DropActions *supportedActions*) |
| QAbstractItemView::State                    | **[state](QAbstractItemView.md#protectedqabstractitemviewstate-qabstractitemviewstate-const)**() const |
| virtual int                                 | **[verticalOffset](QAbstractItemView.md#pure-virtual-protectedint-qabstractitemviewverticaloffset-const)**() const = 0 |
| virtual QStyleOptionViewItem                | **[viewOptions](QAbstractItemView.md#virtual-protectedqstyleoptionviewitem-qabstractitemviewviewoptions-const)**() const |
| virtual QRegion                             | **[visualRegionForSelection](QAbstractItemView.md#pure-virtual-protectedqregion-qabstractitemviewvisualregionforselectionconst-qitemselection-selection-const)**(const QItemSelection &*selection*) const = 0 |



## 重写保护成员函数

| virtual void  | **[dragEnterEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdragentereventqdragenterevent-event)**(QDragEnterEvent **event*) override |
| -------------: | :------------------------------------------------------------ |
| virtual void  | **[dragLeaveEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdragleaveeventqdragleaveevent-event)**(QDragLeaveEvent **event*) override |
| virtual void  | **[dragMoveEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdragmoveeventqdragmoveevent-event)**(QDragMoveEvent **event*) override |
| virtual void  | **[dropEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdropeventqdropevent-event)**(QDropEvent **event*) override |
| virtual bool  | **[event](QAbstractItemView.md#override-virtual-protectedbool-qabstractitemvieweventqevent-event)**(QEvent **event*) override |
| virtual bool  | **[eventFilter](QAbstractItemView.md#override-virtual-protectedbool-qabstractitemvieweventfilterqobject-object-qevent-event)**(QObject **object*, QEvent **event*) override |
| virtual void  | **[focusInEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewfocusineventqfocusevent-event)**(QFocusEvent **event*) override |
| virtual bool  | **[focusNextPrevChild](QAbstractItemView.md#override-virtual-protectedbool-qabstractitemviewfocusnextprevchildbool-next)**(bool *next*) override |
| virtual void  | **[focusOutEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewfocusouteventqfocusevent-event)**(QFocusEvent **event*) override |
| virtual void  | **[inputMethodEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewinputmethodeventqinputmethodevent-event)**(QInputMethodEvent **event*) override |
| virtual void  | **[keyPressEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewkeypresseventqkeyevent-event)**(QKeyEvent **event*) override |
| virtual void  | **[mouseDoubleClickEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewmousedoubleclickeventqmouseevent-event)**(QMouseEvent **event*) override |
| virtual void  | **[mouseMoveEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewmousemoveeventqmouseevent-event)**(QMouseEvent **event*) override |
| virtual void  | **[mousePressEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewmousepresseventqmouseevent-event)**(QMouseEvent **event*) override |
| virtual void  | **[mouseReleaseEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewmousereleaseeventqmouseevent-event)**(QMouseEvent **event*) override |
| virtual void  | **[resizeEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewresizeeventqresizeevent-event)**(QResizeEvent **event*) override |
| virtual void  | **[timerEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewtimereventqtimerevent-event)**(QTimerEvent **event*) override |
| virtual bool  | **[viewportEvent](QAbstractItemView.md#override-virtual-protectedbool-qabstractitemviewviewporteventqevent-event)**(QEvent **event*) override |
| virtual QSize | **[viewportSizeHint](QAbstractItemView.md#override-virtual-protectedqsize-qabstractitemviewviewportsizehint-const)**() const override |



## 保护槽函数

| virtual void | **[closeEditor](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint)**(QWidget **editor*, QAbstractItemDelegate::EndEditHint *hint*) |
| ------------: | :------------------------------------------------------------ |
| virtual void | **[commitData](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcommitdataqwidget-editor)**(QWidget **editor*) |
| virtual void | **[currentChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcurrentchangedconst-qmodelindex-current-const-qmodelindex-previous)**(const QModelIndex &*current*, const QModelIndex &*previous*) |
| virtual void | **[dataChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewdatachangedconst-qmodelindex-topleft-const-qmodelindex-bottomright-const-qvectorint-roles--qvectorint)**(const QModelIndex &*topLeft*, const QModelIndex &*bottomRight*, const QVector<int> &*roles* = QVector<int>()) |
| virtual void | **[editorDestroyed](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemvieweditordestroyedqobject-editor)**(QObject **editor*) |
| virtual void | **[rowsAboutToBeRemoved](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsabouttoberemovedconst-qmodelindex-parent-int-start-int-end)**(const QModelIndex &*parent*, int *start*, int *end*) |
| virtual void | **[rowsInserted](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsinsertedconst-qmodelindex-parent-int-start-int-end)**(const QModelIndex &*parent*, int *start*, int *end*) |
| virtual void | **[selectionChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewselectionchangedconst-qitemselection-selected-const-qitemselection-deselected)**(const QItemSelection &*selected*, const QItemSelection &*deselected*) |
| virtual void | **[updateGeometries](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewupdategeometries)**() |



## 详细描述

QAbstractItemView class is the base class for every standard view that uses a [QAbstractItemModel](../../A/QAbstractItemModel/QAbstractItemModel.md). QAbstractItemView is an abstract class and cannot itself be instantiated. It provides a standard interface for interoperating with models through the signals and slots mechanism, enabling subclasses to be kept up-to-date with changes to their models. This class provides standard support for keyboard and mouse navigation, viewport scrolling, item editing, and selections. The keyboard navigation implements this functionality:

|       Keys        |                        Functionality                         |
| --------------- | ---------------------------------------------------------- |
|    Arrow keys     |           Changes the current item and selects it.           |
|  Ctrl+Arrow keys  |       Changes the current item but does not select it.       |
| Shift+Arrow keys  | Changes the current item and selects it. The previously selected item(s) is not deselected. |
|     Ctrl+Space     |            Toggles selection of the current item.            |
|    Tab/Backtab    |     Changes the current item to the next/previous item.      |
|     Home/End      |          Selects the first/last item in the model.           |
| Page up/Page down | Scrolls the rows shown up/down by the number of visible rows in the view. |
|      Ctrl+A       |               Selects all items in the model.                |

Note that the above table assumes that the [selection mode](QAbstractItemView.md#selectionmode--selectionmode) allows the operations. For instance, you cannot select items if the selection mode is [QAbstractItemView::NoSelection](QAbstractItemView.md#enum-qabstractitemviewselectionmode).

The QAbstractItemView class is one of the [Model/View Classes](../../M/Model_View_Programming/Model_View_Programming.md#模型/视图类) and is part of Qt's [model/view framework](../../M/Model_View_Programming/Model_View_Programming.md).

The view classes that inherit QAbstractItemView only need to implement their own view-specific functionality, such as drawing items, returning the geometry of items, finding items, etc.

QAbstractItemView provides common slots such as [edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)() and [setCurrentIndex](QAbstractItemView.md#slotvoid-qabstractitemviewsetcurrentindexconst-qmodelindex-index)(). Many protected slots are also provided, including [dataChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewdatachangedconst-qmodelindex-topleft-const-qmodelindex-bottomright-const-qvectorint-roles--qvectorint)(), [rowsInserted](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsinsertedconst-qmodelindex-parent-int-start-int-end)(), [rowsAboutToBeRemoved](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsabouttoberemovedconst-qmodelindex-parent-int-start-int-end)(), [selectionChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewselectionchangedconst-qitemselection-selected-const-qitemselection-deselected)(), and [currentChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcurrentchangedconst-qmodelindex-current-const-qmodelindex-previous)().

The root item is returned by [rootIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewrootindex-const)(), and the current item by [currentIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewcurrentindex-const)(). To make sure that an item is visible use [scrollTo](QAbstractItemView.md#pure-virtualvoid-qabstractitemviewscrolltoconst-qmodelindex-index-qabstractitemviewscrollhint-hint--ensurevisible)().

Some of QAbstractItemView's functions are concerned with scrolling, for example [setHorizontalScrollMode](QAbstractItemView.md#horizontalscrollmode--scrollmode)() and [setVerticalScrollMode](QAbstractItemView.md#verticalscrollmode--scrollmode)(). To set the range of the scroll bars, you can, for example, reimplement the view's [resizeEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewresizeeventqresizeevent-event)() function:

```c++
void MyView::resizeEvent(QResizeEvent *event) {
    horizontalScrollBar()->setRange(0, realWidth - width());
    ...
}
```

Note that the range is not updated until the widget is shown.

Several other functions are concerned with selection control; for example [setSelectionMode](QAbstractItemView.md#selectionmode--selectionmode)(), and [setSelectionBehavior](QAbstractItemView.md#selectionbehavior--selectionbehavior)(). This class provides a default selection model to work with ([selectionModel](QAbstractItemView.md#qitemselectionmodel-qabstractitemviewselectionmodel-const)()), but this can be replaced by using [setSelectionModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetselectionmodelqitemselectionmodel-selectionmodel)() with an instance of [QItemSelectionModel](../../I/QItemSelectionModel/QItemSelectionModel.md).

For complete control over the display and editing of items you can specify a delegate with [setItemDelegate](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateqabstractitemdelegate-delegate)().

QAbstractItemView provides a lot of protected functions. Some are concerned with editing, for example, [edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)(), and [commitData](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcommitdataqwidget-editor)(), whilst others are keyboard and mouse event handlers.

**注意：** If you inherit QAbstractItemView and intend to update the contents of the viewport, you should use viewport->[update](QAbstractItemView.md#slotvoid-qabstractitemviewupdateconst-qmodelindex-index)() instead of [update()](../../W/QWidget/QWidget.md#slotvoid-qwidgetupdate) as all painting operations take place on the viewport.

**另请参阅** [View Classes](../../M/Model_View_Programming/Model_View_Programming.md#view-classes), [Model/View Programming](../../M/Model_View_Programming/Model_View_Programming.md), [QAbstractItemModel](../../A/QAbstractItemModel/QAbstractItemModel.md), and [Chart Example](https://doc.qt.io/qt-5/qtwidgets-itemviews-chart-example.html).

## 成员类型文档

### enum QAbstractItemView::CursorAction

This enum describes the different ways to navigate between items,

| Constant                          | Value | Description                                 |
| :--------------------------------- | :----- | :------------------------------------------- |
| `QAbstractItemView::MoveUp`       | `0`   | Move to the item above the current item.    |
| `QAbstractItemView::MoveDown`     | `1`   | Move to the item below the current item.    |
| `QAbstractItemView::MoveLeft`     | `2`   | Move to the item left of the current item.  |
| `QAbstractItemView::MoveRight`    | `3`   | Move to the item right of the current item. |
| `QAbstractItemView::MoveHome`     | `4`   | Move to the top-left corner item.           |
| `QAbstractItemView::MoveEnd`      | `5`   | Move to the bottom-right corner item.       |
| `QAbstractItemView::MovePageUp`   | `6`   | Move one page up above the current item.    |
| `QAbstractItemView::MovePageDown` | `7`   | Move one page down below the current item.  |
| `QAbstractItemView::MoveNext`     | `8`   | Move to the item after the current item.    |
| `QAbstractItemView::MovePrevious` | `9`   | Move to the item before the current item.   |

**另请参阅** [moveCursor](QAbstractItemView.md#pure-virtual-protectedqmodelindex-qabstractitemviewmovecursorqabstractitemviewcursoraction-cursoraction-qtkeyboardmodifiers-modifiers)().

### enum QAbstractItemView::DragDropMode

Describes the various drag and drop events the view can act upon. By default the view does not support dragging or dropping (`NoDragDrop`).

| Constant                          | Value | Description                                                  |
| :--------------------------------- | :----- | :------------------------------------------------------------ |
| `QAbstractItemView::NoDragDrop`   | `0`   | Does not support dragging or dropping.                       |
| `QAbstractItemView::DragOnly`     | `1`   | The view supports dragging of its own items                  |
| `QAbstractItemView::DropOnly`     | `2`   | The view accepts drops                                       |
| `QAbstractItemView::DragDrop`     | `3`   | The view supports both dragging and dropping                 |
| `QAbstractItemView::InternalMove` | `4`   | The view accepts move (**not copy**) operations only from itself. |

Note that the model used needs to provide support for drag and drop operations.

This enum was introduced or modified in Qt 4.2.

**另请参阅** [setDragDropMode](QAbstractItemView.md#dragdropmode--dragdropmode)() and [Using drag and drop with item views](../../M/Model_View_Programming/Model_View_Programming.md#using-drag-and-drop-with-item-views).

### enum QAbstractItemView::DropIndicatorPosition

This enum indicates the position of the drop indicator in relation to the index at the current mouse position:

| Constant                        | Value | Description                                                  |
| :------------------------------- | :----- | :------------------------------------------------------------ |
| `QAbstractItemView::OnItem`     | `0`   | The item will be dropped on the index.                       |
| `QAbstractItemView::AboveItem`  | `1`   | The item will be dropped above the index.                    |
| `QAbstractItemView::BelowItem`  | `2`   | The item will be dropped below the index.                    |
| `QAbstractItemView::OnViewport` | `3`   | The item will be dropped onto a region of the viewport with no items. The way each view handles items dropped onto the viewport depends on the behavior of the underlying model in use. |

### enum QAbstractItemView::EditTrigger flags QAbstractItemView::EditTriggers

This enum describes actions which will initiate item editing.

| Constant                             | Value | Description                                                  |
| :------------------------------------ | :----- | :------------------------------------------------------------ |
| `QAbstractItemView::NoEditTriggers`  | `0`   | No editing possible.                                         |
| `QAbstractItemView::CurrentChanged`  | `1`   | Editing start whenever current item changes.                 |
| `QAbstractItemView::DoubleClicked`   | `2`   | Editing starts when an item is double clicked.               |
| `QAbstractItemView::SelectedClicked` | `4`   | Editing starts when clicking on an already selected item.    |
| `QAbstractItemView::EditKeyPressed`  | `8`   | Editing starts when the platform edit key has been pressed over an item. |
| `QAbstractItemView::AnyKeyPressed`   | `16`  | Editing starts when any key is pressed over an item.         |
| `QAbstractItemView::AllEditTriggers` | `31`  | Editing starts for all above actions.                        |

The EditTriggers type is a typedef for [QFlags](../../F/QFlags/QFlags.md)<EditTrigger>. It stores an OR combination of EditTrigger values.

### enum QAbstractItemView::ScrollHint

| Constant                              | Value | Description                                                |
| :------------------------------------- | :----- | :---------------------------------------------------------- |
| `QAbstractItemView::EnsureVisible`    | `0`   | Scroll to ensure that the item is visible.                 |
| `QAbstractItemView::PositionAtTop`    | `1`   | Scroll to position the item at the top of the viewport.    |
| `QAbstractItemView::PositionAtBottom` | `2`   | Scroll to position the item at the bottom of the viewport. |
| `QAbstractItemView::PositionAtCenter` | `3`   | Scroll to position the item at the center of the viewport. |

### enum QAbstractItemView::ScrollMode

Describes how the scrollbar should behave. When setting the scroll mode to ScrollPerPixel the single step size will adjust automatically unless it was set explicitly using [setSingleStep()](../../A/QAbstractSlider/QAbstractSlider.md#singlestep--int). The automatic adjustment can be restored by setting the single step size to -1.

| Constant                            | Value | Description                                            |
| :----------------------------------- | :----- | :------------------------------------------------------ |
| `QAbstractItemView::ScrollPerItem`  | `0`   | The view will scroll the contents one item at a time.  |
| `QAbstractItemView::ScrollPerPixel` | `1`   | The view will scroll the contents one pixel at a time. |

This enum was introduced or modified in Qt 4.2.

### enum QAbstractItemView::SelectionBehavior

| Constant                           | Value | Description             |
| :---------------------------------- | :----- | :----------------------- |
| `QAbstractItemView::SelectItems`   | `0`   | Selecting single items. |
| `QAbstractItemView::SelectRows`    | `1`   | Selecting only rows.    |
| `QAbstractItemView::SelectColumns` | `2`   | Selecting only columns. |

### enum QAbstractItemView::SelectionMode

This enum indicates how the view responds to user selections:

| Constant                                 | Value | Description                                                  |
| :---------------------------------------- | :----- | :------------------------------------------------------------ |
| `QAbstractItemView::SingleSelection`     | `1`   | When the user selects an item, any already-selected item becomes unselected. It is possible for the user to deselect the selected item by pressing the Ctrl key when clicking the selected item. |
| `QAbstractItemView::ContiguousSelection` | `4`   | When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. |
| `QAbstractItemView::ExtendedSelection`   | `3`   | When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them. |
| `QAbstractItemView::MultiSelection`      | `2`   | When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them. |
| `QAbstractItemView::NoSelection`         | `0`   | Items cannot be selected.                                    |

The most commonly used modes are SingleSelection and ExtendedSelection.

### enum QAbstractItemView::State

Describes the different states the view can be in. This is usually only interesting when reimplementing your own view.

| Constant                                | Value | Description                                     |
| :--------------------------------------- | :----- | :----------------------------------------------- |
| `QAbstractItemView::NoState`            | `0`   | The is the default state.                       |
| `QAbstractItemView::DraggingState`      | `1`   | The user is dragging items.                     |
| `QAbstractItemView::DragSelectingState` | `2`   | The user is selecting items.                    |
| `QAbstractItemView::EditingState`       | `3`   | The user is editing an item in a widget editor. |
| `QAbstractItemView::ExpandingState`     | `4`   | The user is opening a branch of items.          |
| `QAbstractItemView::CollapsingState`    | `5`   | The user is closing a branch of items.          |
| `QAbstractItemView::AnimatingState`     | `6`   | The item view is performing an animation.       |

## 属性文档

### alternatingRowColors : bool

This property holds whether to draw the background using alternating colors

If this property is `true`, the item background will be drawn using [QPalette::Base](../../P/QPalette/QPalette.md#enum-qpalettecolorrole) and [QPalette::AlternateBase](../../P/QPalette/QPalette.md#enum-qpalettecolorrole); otherwise the background will be drawn using the [QPalette::Base](../../P/QPalette/QPalette.md#enum-qpalettecolorrole) color.

By default, this property is `false`.

**存取函数：**

| bool | **alternatingRowColors**() const           |
| ----: | :------------------------------------------ |
| void | **setAlternatingRowColors**(bool *enable*) |

### autoScroll : bool

This property holds whether autoscrolling in drag move events is enabled

If this property is set to true (the default), the [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md) automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge. If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.

This property only works if the viewport accepts drops. Autoscroll is switched off by setting this property to false.

**存取函数：**

| bool | **hasAutoScroll**() const        |
| ----: | :-------------------------------- |
| void | **setAutoScroll**(bool *enable*) |

### autoScrollMargin : int

This property holds the size of the area when auto scrolling is triggered

This property controls the size of the area at the edge of the viewport that triggers autoscrolling. The default value is 16 pixels.

This property was introduced in Qt 4.4.

**存取函数：**

| int  | **autoScrollMargin**() const          |
| ----: | :------------------------------------- |
| void | **setAutoScrollMargin**(int *margin*) |

### defaultDropAction : [Qt::DropAction](../../Q/Qt_Namespace/Qt_Namespace.md#DropAction-enum)

This property holds the drop action that will be used by default in QAbstractItemView::drag()

If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.

This property was introduced in Qt 4.6.

**存取函数：**

| Qt::DropAction | **defaultDropAction**() const                         |
| --------------: | :----------------------------------------------------- |
| void           | **setDefaultDropAction**(Qt::DropAction *dropAction*) |

**另请参阅** [showDropIndicator](QAbstractItemView.md#showdropindicator--bool) and [dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool).

### dragDropMode : [DragDropMode](QAbstractItemView.md#enum-qabstractitemviewdragdropmode)

This property holds the drag and drop event the view will act upon

This property was introduced in Qt 4.2.

**存取函数：**

| QAbstractItemView::DragDropMode | **dragDropMode**() const                                     |
| -------------------------------: | :------------------------------------------------------------ |
| void                            | **setDragDropMode**(QAbstractItemView::DragDropMode *behavior*) |

**另请参阅** [showDropIndicator](QAbstractItemView.md#showdropindicator--bool) and [dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool).

### dragDropOverwriteMode : bool

This property holds the view's drag and drop behavior

If its value is `true`, the selected data will overwrite the existing item data when dropped, while moving the data will clear the item. If its value is `false`, the selected data will be inserted as a new item when the data is dropped. When the data is moved, the item is removed as well.

The default value is `false`, as in the [QListView](../../L/QListView/QListView.md) and [QTreeView](../../T/QTreeView/QTreeView.md) subclasses. In the [QTableView](../../T/QTableView/QTableView.md) subclass, on the other hand, the property has been set to `true`.

注意： This is not intended to prevent overwriting of items. The model's implementation of flags() should do that by not returning [Qt::ItemIsDropEnabled](../../Q/Qt_Namespace/Qt_Namespace.md#ItemFlag-enum).

This property was introduced in Qt 4.2.

**存取函数：**

| bool | **dragDropOverwriteMode**() const              |
| ----: | :---------------------------------------------- |
| void | **setDragDropOverwriteMode**(bool *overwrite*) |

**另请参阅** [dragDropMode](QAbstractItemView.md#dragdropmode--dragdropmode).

### dragEnabled : bool

This property holds whether the view supports dragging of its own items

**存取函数：**

| bool | **dragEnabled**() const           |
| ----: | :--------------------------------- |
| void | **setDragEnabled**(bool *enable*) |

**另请参阅** [showDropIndicator](QAbstractItemView.md#showdropindicator--bool), [DragDropMode](QAbstractItemView.md#enum-qabstractitemviewdragdropmode), [dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool), and [acceptDrops](../../W/QWidget/QWidget.md#acceptdrops--bool).

### editTriggers : [EditTriggers](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers)

This property holds which actions will initiate item editing

This property is a selection of flags defined by [EditTrigger](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers), combined using the OR operator. The view will only initiate the editing of an item if the action performed is set in this property.

**存取函数：**

| QAbstractItemView::EditTriggers | **editTriggers**() const                                     |
| -------------------------------: | :------------------------------------------------------------ |
| void                            | **setEditTriggers**(QAbstractItemView::EditTriggers *triggers*) |

### horizontalScrollMode : [ScrollMode](QAbstractItemView.md#enum-qabstractitemviewscrollmode)

how the view scrolls its contents in the horizontal direction

This property controls how the view scroll its contents horizontally. Scrolling can be done either per pixel or per item. Its default value comes from the style via the [QStyle::SH_ItemView_ScrollMode](../../S/QStyle/QStyle.md#enum-qstylestylehint) style hint.

This property was introduced in Qt 4.2.

**存取函数：**

| QAbstractItemView::ScrollMode | **horizontalScrollMode**() const                             |
| -----------------------------: | :------------------------------------------------------------ |
| void                          | **setHorizontalScrollMode**(QAbstractItemView::ScrollMode *mode*) |
| void                          | **resetHorizontalScrollMode**()                              |

### iconSize : [QSize](../../S/QSize/QSize.md)

This property holds the size of items' icons

Setting this property when the view is visible will cause the items to be laid out again.

**存取函数：**

| QSize | **iconSize**() const                 |
| -----: | :------------------------------------ |
| void  | **setIconSize**(const QSize &*size*) |

**Notifier signal:**

| void | **iconSizeChanged**(const QSize &*size*) |
| ----: | :---------------------------------------- |
|      |                                          |

### selectionBehavior : [SelectionBehavior](QAbstractItemView.md#enum-qabstractitemviewselectionbehavior)

This property holds which selection behavior the view uses

This property holds whether selections are done in terms of single items, rows or columns.

**存取函数：**

| QAbstractItemView::SelectionBehavior | **selectionBehavior**() const                                |
| ------------------------------------: | :------------------------------------------------------------ |
| void                                 | **setSelectionBehavior**(QAbstractItemView::SelectionBehavior *behavior*) |

**另请参阅** [SelectionMode](QAbstractItemView.md#enum-qabstractitemviewselectionmode) and [SelectionBehavior](QAbstractItemView.md#enum-qabstractitemviewselectionbehavior).

### selectionMode : [SelectionMode](QAbstractItemView.md#enum-qabstractitemviewselectionmode)

This property holds which selection mode the view operates in

This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.

**存取函数：**

| QAbstractItemView::SelectionMode | **selectionMode**() const                                    |
| --------------------------------: | :------------------------------------------------------------ |
| void                             | **setSelectionMode**(QAbstractItemView::SelectionMode *mode*) |

**另请参阅** [SelectionMode](QAbstractItemView.md#enum-qabstractitemviewselectionmode) and [SelectionBehavior](QAbstractItemView.md#enum-qabstractitemviewselectionbehavior).

### showDropIndicator : bool

This property holds whether the drop indicator is shown when dragging items and dropping.

**存取函数：**

| bool | **showDropIndicator**() const            |
| ----: | :---------------------------------------- |
| void | **setDropIndicatorShown**(bool *enable*) |

**另请参阅** [dragEnabled](QAbstractItemView.md#dragenabled--bool), [DragDropMode](QAbstractItemView.md#enum-qabstractitemviewdragdropmode), [dragDropOverwriteMode](QAbstractItemView.md#dragdropoverwritemode--bool), and [acceptDrops](../../W/QWidget/QWidget.md#acceptdrops--bool).

### tabKeyNavigation : bool

This property holds whether item navigation with tab and backtab is enabled.

**存取函数：**

| bool | **tabKeyNavigation**() const           |
| ----: | :-------------------------------------- |
| void | **setTabKeyNavigation**(bool *enable*) |

### textElideMode : [Qt::TextElideMode](../../Q/Qt_Namespace/Qt_Namespace.md#TextElideMode-enum)

This property holds the position of the "..." in elided text.

The default value for all item views is [Qt::ElideRight](../../Q/Qt_Namespace/Qt_Namespace.md#TextElideMode-enum).

**存取函数：**

| Qt::TextElideMode | **textElideMode**() const                      |
| -----------------: | :---------------------------------------------- |
| void              | **setTextElideMode**(Qt::TextElideMode *mode*) |

### verticalScrollMode : [ScrollMode](QAbstractItemView.md#enum-qabstractitemviewscrollmode)

how the view scrolls its contents in the vertical direction

This property controls how the view scroll its contents vertically. Scrolling can be done either per pixel or per item. Its default value comes from the style via the [QStyle::SH_ItemView_ScrollMode](../../S/QStyle/QStyle.md#enum-qstylestylehint) style hint.

This property was introduced in Qt 4.2.

**存取函数：**

| QAbstractItemView::ScrollMode | **verticalScrollMode**() const                               |
| -----------------------------: | :------------------------------------------------------------ |
| void                          | **setVerticalScrollMode**(QAbstractItemView::ScrollMode *mode*) |
| void                          | **resetVerticalScrollMode**()                                |

## 成员函数文档

### QAbstractItemView::QAbstractItemView([QWidget](../../W/QWidget/QWidget.md#qwidgetqwidgetqwidget-parent--nullptr-qtwindowflags-f--qtwindowflags) **parent* = nullptr)

Constructs an abstract item view with the given *parent*.

### `[signal]`void QAbstractItemView::activated(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

This signal is emitted when the item specified by *index* is activated by the user. How to activate items depends on the platform; e.g., by single- or double-clicking the item, or by pressing the Return or Enter key when the item is current.

**另请参阅** [clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)(), [doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)(), [entered](QAbstractItemView.md#signalvoid-qabstractitemviewenteredconst-qmodelindex-index)(), and [pressed](QAbstractItemView.md#signalvoid-qabstractitemviewpressedconst-qmodelindex-index)().

### `[slot]`void QAbstractItemView::clearSelection()

Deselects all selected items. The current index will not be changed.

**另请参阅** [setSelection](QAbstractItemView.md#pure-virtual-protectedvoid-qabstractitemviewsetselectionconst-qrect-rect-qitemselectionmodelselectionflags-flags)() and [selectAll](QAbstractItemView.md#virtual-slotvoid-qabstractitemviewselectall)().

### `[signal]`void QAbstractItemView::clicked(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

This signal is emitted when a mouse button is left-clicked. The item the mouse was clicked on is specified by *index*. The signal is only emitted when the index is valid.

**另请参阅** [activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)(), [doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)(), [entered](QAbstractItemView.md#signalvoid-qabstractitemviewenteredconst-qmodelindex-index)(), and [pressed](QAbstractItemView.md#signalvoid-qabstractitemviewpressedconst-qmodelindex-index)().

### `[virtual protected slot]`void QAbstractItemView::closeEditor([QWidget](../../W/QWidget/QWidget.md#qwidgetqwidgetqwidget-parent--nullptr-qtwindowflags-f--qtwindowflags) **editor*, [QAbstractItemDelegate::EndEditHint](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md#enum-qabstractitemdelegateendedithint) *hint*)

Closes the given *editor*, and releases it. The *hint* is used to specify how the view should respond to the end of the editing operation. For example, the hint may indicate that the next item in the view should be opened for editing.

**另请参阅** [edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)() and [commitData](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcommitdataqwidget-editor)().

### `[virtual protected slot]`void QAbstractItemView::commitData([QWidget](../../W/QWidget/QWidget.md#qwidgetqwidgetqwidget-parent--nullptr-qtwindowflags-f--qtwindowflags) **editor*)

Commit the data in the *editor* to the model.

**另请参阅** [closeEditor](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint)().

### `[virtual protected slot]`void QAbstractItemView::currentChanged(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*current*, const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*previous*)

This slot is called when a new item becomes the current item. The previous current item is specified by the *previous* index, and the new item by the *current* index.

If you want to know about changes to items see the [dataChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewdatachangedconst-qmodelindex-topleft-const-qmodelindex-bottomright-const-qvectorint-roles--qvectorint)() signal.

### `[virtual protected slot]`void QAbstractItemView::dataChanged(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*topLeft*, const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*bottomRight*, const [QVector](../../V/QVector/QVector.md)<int> &*roles* = QVector<int>())

This slot is called when items with the given *roles* are changed in the model. The changed items are those from *topLeft* to *bottomRight* inclusive. If just one item is changed *topLeft* == *bottomRight*.

The *roles* which have been changed can either be an empty container (meaning everything has changed), or a non-empty container with the subset of roles which have changed.

**注意：** : [Qt::ToolTipRole](../../Q/Qt_Namespace/Qt_Namespace.md#ItemDataRole-enum) is not honored by dataChanged() in the views provided by Qt.

### `[signal]`void QAbstractItemView::doubleClicked(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

This signal is emitted when a mouse button is double-clicked. The item the mouse was double-clicked on is specified by *index*. The signal is only emitted when the index is valid.

**另请参阅** [clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)() and [activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)().

### `[slot]`void QAbstractItemView::edit(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Starts editing the item corresponding to the given *index* if it is editable.

Note that this function does not change the current index. Since the current index defines the next and previous items to edit, users may find that keyboard navigation does not work as expected. To provide consistent navigation behavior, call [setCurrentIndex](QAbstractItemView.md#slotvoid-qabstractitemviewsetcurrentindexconst-qmodelindex-index)() before this function with the same model index.

**另请参阅** [QModelIndex::flags](../../M/QModelIndex/QModelIndex.md#qtitemflags-qmodelindexflags-const)().

### `[virtual protected slot]`void QAbstractItemView::editorDestroyed([QObject](../../O/QObject/QObject.md#qobjectqobjectqobject-parent--nullptr) **editor*)

This function is called when the given *editor* has been destroyed.

**另请参阅** [closeEditor](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint)().

### `[signal]`void QAbstractItemView::entered(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

This signal is emitted when the mouse cursor enters the item specified by *index*. Mouse tracking needs to be enabled for this feature to work.

**另请参阅** [viewportEntered](QAbstractItemView.md#signalvoid-qabstractitemviewviewportentered)(), [activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)(), [clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)(), [doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)(), and [pressed](QAbstractItemView.md#signalvoid-qabstractitemviewpressedconst-qmodelindex-index)().

### `[signal]`void QAbstractItemView::pressed(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

This signal is emitted when a mouse button is pressed. The item the mouse was pressed on is specified by *index*. The signal is only emitted when the index is valid.

Use the [QGuiApplication::mouseButtons](../../G/QGuiApplication/QGuiApplication.md#staticqtmousebuttons-qguiapplicationmousebuttons)() function to get the state of the mouse buttons.

**另请参阅** [activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)(), [clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)(), [doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)(), and [entered](QAbstractItemView.md#signalvoid-qabstractitemviewenteredconst-qmodelindex-index)().

### `[virtual slot]`void QAbstractItemView::reset()

Reset the internal state of the view.

**警告：** This function will reset open editors, scroll bar positions, selections, etc. Existing changes will not be committed. If you would like to save your changes when resetting the view, you can reimplement this function, commit your changes, and then call the superclass' implementation.

### `[virtual protected slot]`void QAbstractItemView::rowsAboutToBeRemoved(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*parent*, int *start*, int *end*)

This slot is called when rows are about to be removed. The deleted rows are those under the given *parent* from *start* to *end* inclusive.

**另请参阅** [rowsInserted](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsinsertedconst-qmodelindex-parent-int-start-int-end)().

### `[virtual protected slot]`void QAbstractItemView::rowsInserted(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*parent*, int *start*, int *end*)

This slot is called when rows are inserted. The new rows are those under the given *parent* from *start* to *end* inclusive. The base class implementation calls fetchMore() on the model to check for more data.

**另请参阅** [rowsAboutToBeRemoved](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewrowsabouttoberemovedconst-qmodelindex-parent-int-start-int-end)().

### `[slot]`void QAbstractItemView::scrollToBottom()

Scrolls the view to the bottom.

This function was introduced in Qt 4.1.

**另请参阅** [scrollTo](QAbstractItemView.md#pure-virtualvoid-qabstractitemviewscrolltoconst-qmodelindex-index-qabstractitemviewscrollhint-hint--ensurevisible)() and [scrollToTop](QAbstractItemView.md#slotvoid-qabstractitemviewscrolltotop)().

### `[slot]`void QAbstractItemView::scrollToTop()

Scrolls the view to the top.

This function was introduced in Qt 4.1.

**另请参阅** [scrollTo](QAbstractItemView.md#pure-virtualvoid-qabstractitemviewscrolltoconst-qmodelindex-index-qabstractitemviewscrollhint-hint--ensurevisible)() and [scrollToBottom](QAbstractItemView.md#slotvoid-qabstractitemviewscrolltobottom)().

### `[virtual slot]`void QAbstractItemView::selectAll()

Selects all items in the view. This function will use the selection behavior set on the view when selecting.

**另请参阅** [setSelection](QAbstractItemView.md#pure-virtual-protectedvoid-qabstractitemviewsetselectionconst-qrect-rect-qitemselectionmodelselectionflags-flags)(), [selectedIndexes](QAbstractItemView.md#virtual-protectedqmodelindexlist-qabstractitemviewselectedindexes-const)(), and [clearSelection](QAbstractItemView.md#slotvoid-qabstractitemviewclearselection)().

### `[virtual protected slot]`void QAbstractItemView::selectionChanged(const [QItemSelection](../../I/QItemSelection/QItemSelection.md) &*selected*, const [QItemSelection](../../I/QItemSelection/QItemSelection.md) &*deselected*)

This slot is called when the selection is changed. The previous selection (which may be empty), is specified by *deselected*, and the new selection by *selected*.

**另请参阅** [setSelection](QAbstractItemView.md#pure-virtual-protectedvoid-qabstractitemviewsetselectionconst-qrect-rect-qitemselectionmodelselectionflags-flags)().

### `[slot]`void QAbstractItemView::setCurrentIndex(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Sets the current item to be the item at *index*.

Unless the current selection mode is [NoSelection](QAbstractItemView.md#enum-qabstractitemviewselectionmode), the item is also selected. Note that this function also updates the starting position for any new selections the user performs.

To set an item as the current item without selecting it, call

```c++
selectionModel()->setCurrentIndex(index, QItemSelectionModel::NoUpdate);
```

**另请参阅** [currentIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewcurrentindex-const)(), [currentChanged](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcurrentchangedconst-qmodelindex-current-const-qmodelindex-previous)(), and [selectionMode](QAbstractItemView.md#selectionmode--selectionmode).

### `[virtual slot]`void QAbstractItemView::setRootIndex(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Sets the root item to the item at the given *index*.

**另请参阅** [rootIndex](QAbstractItemView.md#qmodelindex-qabstractitemviewrootindex-const)().

### `[slot]`void QAbstractItemView::update(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Updates the area occupied by the given *index*.

This function was introduced in Qt 4.3.

### `[virtual protected slot]`void QAbstractItemView::updateGeometries()

Updates the geometry of the child widgets of the view.

This function was introduced in Qt 4.4.

### `[signal]`void QAbstractItemView::viewportEntered()

This signal is emitted when the mouse cursor enters the viewport. Mouse tracking needs to be enabled for this feature to work.

**另请参阅** [entered](QAbstractItemView.md#signalvoid-qabstractitemviewenteredconst-qmodelindex-index)().

### `[virtual]`QAbstractItemView::~QAbstractItemView()

Destroys the view.

### void QAbstractItemView::closePersistentEditor(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Closes the persistent editor for the item at the given *index*.

**另请参阅** [openPersistentEditor](QAbstractItemView.md#void-qabstractitemviewopenpersistenteditorconst-qmodelindex-index)() and [isPersistentEditorOpen](QAbstractItemView.md#bool-qabstractitemviewispersistenteditoropenconst-qmodelindex-index-const)().

### [QModelIndex](../../M/QModelIndex/QModelIndex.md) QAbstractItemView::currentIndex() const

Returns the model index of the current item.

**另请参阅** [setCurrentIndex](QAbstractItemView.md#slotvoid-qabstractitemviewsetcurrentindexconst-qmodelindex-index)().

### `[protected]`[QPoint](../../P/QPoint/QPoint.md) QAbstractItemView::dirtyRegionOffset() const

Returns the offset of the dirty regions in the view.

If you use [scrollDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewscrolldirtyregionint-dx-int-dy)() and implement a [paintEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareapainteventqpaintevent-event)() in a subclass of [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md), you should translate the area given by the paint event with the offset returned from this function.

**另请参阅** [scrollDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewscrolldirtyregionint-dx-int-dy)() and [setDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewsetdirtyregionconst-qregion-region)().

### `[override virtual protected]`void QAbstractItemView::dragEnterEvent([QDragEnterEvent](../../D/QDragEnterEvent/QDragEnterEvent.md) **event*)

Reimplements: [QAbstractScrollArea::dragEnterEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareadragentereventqdragenterevent-event)(QDragEnterEvent *event).

This function is called with the given *event* when a drag and drop operation enters the widget. If the drag is over a valid dropping place (e.g. over an item that accepts drops), the event is accepted; otherwise it is ignored.

**另请参阅** [dropEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdropeventqdropevent-event)() and [startDrag](QAbstractItemView.md#virtual-protectedvoid-qabstractitemviewstartdragqtdropactions-supportedactions)().

### `[override virtual protected]`void QAbstractItemView::dragLeaveEvent([QDragLeaveEvent](../../D/QDragLeaveEvent/QDragLeaveEvent.md) **event*)

Reimplements: [QAbstractScrollArea::dragLeaveEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareadragleaveeventqdragleaveevent-event)(QDragLeaveEvent *event).

This function is called when the item being dragged leaves the view. The *event* describes the state of the drag and drop operation.

### `[override virtual protected]`void QAbstractItemView::dragMoveEvent([QDragMoveEvent](../../D/QDragMoveEvent/QDragMoveEvent.md) **event*)

Reimplements: [QAbstractScrollArea::dragMoveEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareadragmoveeventqdragmoveevent-event)(QDragMoveEvent *event).

This function is called continuously with the given *event* during a drag and drop operation over the widget. It can cause the view to scroll if, for example, the user drags a selection to view's right or bottom edge. In this case, the event will be accepted; otherwise it will be ignored.

**另请参阅** [dropEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewdropeventqdropevent-event)() and [startDrag](QAbstractItemView.md#virtual-protectedvoid-qabstractitemviewstartdragqtdropactions-supportedactions)().

### `[override virtual protected]`void QAbstractItemView::dropEvent([QDropEvent](../../D/QDropEvent/QDropEvent.md) **event*)

Reimplements: [QAbstractScrollArea::dropEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareadropeventqdropevent-event)(QDropEvent *event).

This function is called with the given *event* when a drop event occurs over the widget. If the model accepts the even position the drop event is accepted; otherwise it is ignored.

**另请参阅** [startDrag](QAbstractItemView.md#virtual-protectedvoid-qabstractitemviewstartdragqtdropactions-supportedactions)().

### `[protected]`[QAbstractItemView::DropIndicatorPosition](QAbstractItemView.md#enum-qabstractitemviewdropindicatorposition) QAbstractItemView::dropIndicatorPosition() const

Returns the position of the drop indicator in relation to the closest item.

This function was introduced in Qt 4.1.

### `[virtual protected]`bool QAbstractItemView::edit(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*, [QAbstractItemView::EditTrigger](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers) *trigger*, [QEvent](../../E/QEvent/QEvent.md) **event*)

Starts editing the item at *index*, creating an editor if necessary, and returns `true` if the view's [State](QAbstractItemView.md#enum-qabstractitemviewstate) is now [EditingState](QAbstractItemView.md#enum-qabstractitemviewstate); otherwise returns `false`.

The action that caused the editing process is described by *trigger*, and the associated event is specified by *event*.

Editing can be forced by specifying the *trigger* to be [QAbstractItemView::AllEditTriggers](QAbstractItemView.md#enum-qabstractitemviewedittriggerflags-qabstractitemviewedittriggers).

**另请参阅** [closeEditor](QAbstractItemView.md#virtual-protected-slotvoid-qabstractitemviewcloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint)().

### `[override virtual protected]`bool QAbstractItemView::event([QEvent](../../E/QEvent/QEvent.md) **event*)

Reimplements: [QAbstractScrollArea::event](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedbool-qabstractscrollareaeventqevent-event)(QEvent *event).

### `[override virtual protected]`bool QAbstractItemView::eventFilter([QObject](../../O/QObject/QObject.md#qobjectqobjectqobject-parent--nullptr) **object*, [QEvent](../../E/QEvent/QEvent.md) **event*)

Reimplements: [QObject::eventFilter](../../O/QObject/QObject.md#virtualbool-qobjecteventfilterqobject-watched-qevent-event)(QObject *watched, QEvent *event).

### `[protected]`void QAbstractItemView::executeDelayedItemsLayout()

Executes the scheduled layouts without waiting for the event processing to begin.

**另请参阅** [scheduleDelayedItemsLayout](QAbstractItemView.md#protectedvoid-qabstractitemviewscheduledelayeditemslayout)().

### `[override virtual protected]`void QAbstractItemView::focusInEvent([QFocusEvent](../../F/QFocusEvent/QFocusEvent.md) **event*)

Reimplements: [QWidget::focusInEvent](../../W/QWidget/QWidget.md#virtual-protectedvoid-qwidgetfocusineventqfocusevent-event)(QFocusEvent *event).

This function is called with the given *event* when the widget obtains the focus. By default, the event is ignored.

**另请参阅** [setFocus](../../W/QWidget/QWidget.md#slotvoid-qwidgetsetfocus)() and [focusOutEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewfocusouteventqfocusevent-event)().

### `[override virtual protected]`bool QAbstractItemView::focusNextPrevChild(bool *next*)

Reimplements: [QWidget::focusNextPrevChild](../../W/QWidget/QWidget.md#virtual-protectedbool-qwidgetfocusnextprevchildbool-next)(bool next).

### `[override virtual protected]`void QAbstractItemView::focusOutEvent([QFocusEvent](../../F/QFocusEvent/QFocusEvent.md) **event*)

Reimplements: [QWidget::focusOutEvent](../../W/QWidget/QWidget.md#virtual-protectedvoid-qwidgetfocusouteventqfocusevent-event)(QFocusEvent *event).

This function is called with the given *event* when the widget loses the focus. By default, the event is ignored.

**另请参阅** [clearFocus](../../W/QWidget/QWidget.md#void-qwidgetclearfocus)() and [focusInEvent](QAbstractItemView.md#override-virtual-protectedvoid-qabstractitemviewfocusineventqfocusevent-event)().

### `[pure virtual protected]`int QAbstractItemView::horizontalOffset() const

Returns the horizontal offset of the view.

In the base class this is a pure virtual function.

**另请参阅** [verticalOffset](QAbstractItemView.md#pure-virtual-protectedint-qabstractitemviewverticaloffset-const)().

### `[pure virtual]`[QModelIndex](../../M/QModelIndex/QModelIndex.md) QAbstractItemView::indexAt(const [QPoint](../../P/QPoint/QPoint.md) &*point*) const

Returns the model index of the item at the viewport coordinates *point*.

In the base class this is a pure virtual function.

**另请参阅** [visualRect](QAbstractItemView.md#pure-virtualqrect-qabstractitemviewvisualrectconst-qmodelindex-index-const)().

### [QWidget](../../W/QWidget/QWidget.md#qwidgetqwidgetqwidget-parent--nullptr-qtwindowflags-f--qtwindowflags) *QAbstractItemView::indexWidget(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns the widget for the item at the given *index*.

This function was introduced in Qt 4.1.

**另请参阅** [setIndexWidget](QAbstractItemView.md#void-qabstractitemviewsetindexwidgetconst-qmodelindex-index-qwidget-widget)().

### `[override virtual protected]`void QAbstractItemView::inputMethodEvent([QInputMethodEvent](../../I/QInputMethodEvent/QInputMethodEvent.md) **event*)

Reimplements: [QWidget::inputMethodEvent](../../W/QWidget/QWidget.md#virtual-protectedvoid-qwidgetinputmethodeventqinputmethodevent-event)(QInputMethodEvent *event).

### `[override virtual]`[QVariant](../../V/QVariant/QVariant.md) QAbstractItemView::inputMethodQuery([Qt::InputMethodQuery](../../Q/Qt_Namespace/Qt_Namespace.md#InputMethodQuery-enum) *query*) const

Reimplements: [QWidget::inputMethodQuery](../../W/QWidget/QWidget.md#virtualqvariant-qwidgetinputmethodqueryqtinputmethodquery-query-const)(Qt::InputMethodQuery query) const.

### `[pure virtual protected]`bool QAbstractItemView::isIndexHidden(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns `true` if the item referred to by the given *index* is hidden in the view, otherwise returns `false`.

Hiding is a view specific feature. For example in [TableView](https://doc.qt.io/qt-5/qml-qtquick-tableview.html) a column can be marked as hidden or a row in the TreeView.

In the base class this is a pure virtual function.

### bool QAbstractItemView::isPersistentEditorOpen(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns whether a persistent editor is open for the item at index *index*.

This function was introduced in Qt 5.10.

**另请参阅** [openPersistentEditor](QAbstractItemView.md#void-qabstractitemviewopenpersistenteditorconst-qmodelindex-index)() and [closePersistentEditor](QAbstractItemView.md#void-qabstractitemviewclosepersistenteditorconst-qmodelindex-index)().

### [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) *QAbstractItemView::itemDelegate() const

Returns the item delegate used by this view and model. This is either one set with [setItemDelegate](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateqabstractitemdelegate-delegate)(), or the default one.

**另请参阅** [setItemDelegate](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateqabstractitemdelegate-delegate)().

### [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) *QAbstractItemView::itemDelegate(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns the item delegate used by this view and model for the given *index*.

### [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) *QAbstractItemView::itemDelegateForColumn(int *column*) const

Returns the item delegate used by this view and model for the given *column*. You can call [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)() to get a pointer to the current delegate for a given index.

This function was introduced in Qt 4.2.

**另请参阅** [setItemDelegateForColumn](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforcolumnint-column-qabstractitemdelegate-delegate)(), [itemDelegateForRow](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforrowint-row-const)(), and [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)().

### [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) *QAbstractItemView::itemDelegateForRow(int *row*) const

Returns the item delegate used by this view and model for the given *row*, or `nullptr` if no delegate has been assigned. You can call [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)() to get a pointer to the current delegate for a given index.

This function was introduced in Qt 4.2.

**另请参阅** [setItemDelegateForRow](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforrowint-row-qabstractitemdelegate-delegate)(), [itemDelegateForColumn](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforcolumnint-column-const)(), and [setItemDelegate](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateqabstractitemdelegate-delegate)().

### `[override virtual protected]`void QAbstractItemView::keyPressEvent([QKeyEvent](../../K/QKeyEvent/QKeyEvent.md) **event*)

Reimplements: [QAbstractScrollArea::keyPressEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareakeypresseventqkeyevent-e)(QKeyEvent *e).

This function is called with the given *event* when a key event is sent to the widget. The default implementation handles basic cursor movement, e.g. Up, Down, Left, Right, Home, PageUp, and PageDown; the [activated](QAbstractItemView.md#signalvoid-qabstractitemviewactivatedconst-qmodelindex-index)() signal is emitted if the current index is valid and the activation key is pressed (e.g. Enter or Return, depending on the platform). This function is where editing is initiated by key press, e.g. if F2 is pressed.

**另请参阅** [edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)(), [moveCursor](QAbstractItemView.md#pure-virtual-protectedqmodelindex-qabstractitemviewmovecursorqabstractitemviewcursoraction-cursoraction-qtkeyboardmodifiers-modifiers)(), [keyboardSearch](QAbstractItemView.md#virtualvoid-qabstractitemviewkeyboardsearchconst-qstring-search)(), and [tabKeyNavigation](QAbstractItemView.md#tabkeynavigation--bool).

### `[virtual]`void QAbstractItemView::keyboardSearch(const [QString](../../S/QString/QString.md) &*search*)

Moves to and selects the item best matching the string *search*. If no item is found nothing happens.

In the default implementation, the search is reset if *search* is empty, or the time interval since the last search has exceeded [QApplication::keyboardInputInterval](../../A/QApplication/QApplication.md#keyboardinputinterval--int)().

### [QAbstractItemModel](../../A/QAbstractItemModel/QAbstractItemModel.md) *QAbstractItemView::model() const

Returns the model that this view is presenting.

**另请参阅** [setModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetmodelqabstractitemmodel-model)().

### `[override virtual protected]`void QAbstractItemView::mouseDoubleClickEvent([QMouseEvent](../../M/QMouseEvent/QMouseEvent.md) **event*)

Reimplements: [QAbstractScrollArea::mouseDoubleClickEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareamousedoubleclickeventqmouseevent-e)(QMouseEvent *e).

This function is called with the given *event* when a mouse button is double clicked inside the widget. If the double-click is on a valid item it emits the [doubleClicked](QAbstractItemView.md#signalvoid-qabstractitemviewdoubleclickedconst-qmodelindex-index)() signal and calls [edit](QAbstractItemView.md#slotvoid-qabstractitemvieweditconst-qmodelindex-index)() on the item.

### `[override virtual protected]`void QAbstractItemView::mouseMoveEvent([QMouseEvent](../../M/QMouseEvent/QMouseEvent.md) **event*)

Reimplements: [QAbstractScrollArea::mouseMoveEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareamousemoveeventqmouseevent-e)(QMouseEvent *e).

This function is called with the given *event* when a mouse move event is sent to the widget. If a selection is in progress and new items are moved over the selection is extended; if a drag is in progress it is continued.

### `[override virtual protected]`void QAbstractItemView::mousePressEvent([QMouseEvent](../../M/QMouseEvent/QMouseEvent.md) **event*)

Reimplements: [QAbstractScrollArea::mousePressEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareamousepresseventqmouseevent-e)(QMouseEvent *e).

This function is called with the given *event* when a mouse button is pressed while the cursor is inside the widget. If a valid item is pressed on it is made into the current item. This function emits the [pressed](QAbstractItemView.md#signalvoid-qabstractitemviewpressedconst-qmodelindex-index)() signal.

### `[override virtual protected]`void QAbstractItemView::mouseReleaseEvent([QMouseEvent](../../M/QMouseEvent/QMouseEvent.md) **event*)

Reimplements: [QAbstractScrollArea::mouseReleaseEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollareamousereleaseeventqmouseevent-e)(QMouseEvent *e).

This function is called with the given *event* when a mouse button is released, after a mouse press event on the widget. If a user presses the mouse inside your widget and then drags the mouse to another location before releasing the mouse button, your widget receives the release event. The function will emit the [clicked](QAbstractItemView.md#signalvoid-qabstractitemviewclickedconst-qmodelindex-index)() signal if an item was being pressed.

### `[pure virtual protected]`[QModelIndex](../../M/QModelIndex/QModelIndex.md) QAbstractItemView::moveCursor([QAbstractItemView::CursorAction](QAbstractItemView.md#enum-qabstractitemviewcursoraction) *cursorAction*, [Qt::KeyboardModifiers](../../Q/Qt_Namespace/Qt_Namespace.md#KeyboardModifier-enum) *modifiers*)

Returns a [QModelIndex](../../M/QModelIndex/QModelIndex.md) object pointing to the next object in the view, based on the given *cursorAction* and keyboard modifiers specified by *modifiers*.

In the base class this is a pure virtual function.

### void QAbstractItemView::openPersistentEditor(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*)

Opens a persistent editor on the item at the given *index*. If no editor exists, the delegate will create a new editor.

**另请参阅** [closePersistentEditor](QAbstractItemView.md#void-qabstractitemviewclosepersistenteditorconst-qmodelindex-index)() and [isPersistentEditorOpen](QAbstractItemView.md#bool-qabstractitemviewispersistenteditoropenconst-qmodelindex-index-const)().

### `[override virtual protected]`void QAbstractItemView::resizeEvent([QResizeEvent](../../R/QResizeEvent/QResizeEvent.md) **event*)

Reimplements: [QAbstractScrollArea::resizeEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#override-virtual-protectedvoid-qabstractscrollarearesizeeventqresizeevent-event)(QResizeEvent *event).

This function is called with the given *event* when a resize event is sent to the widget.

**另请参阅** [QWidget::resizeEvent](../../W/QWidget/QWidget.md#virtual-protectedvoid-qwidgetresizeeventqresizeevent-event)().

### [QModelIndex](../../M/QModelIndex/QModelIndex.md) QAbstractItemView::rootIndex() const

Returns the model index of the model's root item. The root item is the parent item to the view's toplevel items. The root can be invalid.

**另请参阅** [setRootIndex](QAbstractItemView.md#virtual-slotvoid-qabstractitemviewsetrootindexconst-qmodelindex-index)().

### `[protected]`void QAbstractItemView::scheduleDelayedItemsLayout()

Schedules a layout of the items in the view to be executed when the event processing starts.

Even if scheduleDelayedItemsLayout() is called multiple times before events are processed, the view will only do the layout once.

**另请参阅** [executeDelayedItemsLayout](QAbstractItemView.md#protectedvoid-qabstractitemviewexecutedelayeditemslayout)().

### `[protected]`void QAbstractItemView::scrollDirtyRegion(int *dx*, int *dy*)

Prepares the view for scrolling by (*dx*,*dy*) pixels by moving the dirty regions in the opposite direction. You only need to call this function if you are implementing a scrolling viewport in your view subclass.

If you implement [scrollContentsBy](../../A/QAbstractScrollArea/QAbstractScrollArea.md#virtual-protectedvoid-qabstractscrollareascrollcontentsbyint-dx-int-dy)() in a subclass of [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md), call this function before you call [QWidget::scroll](../../W/QWidget/QWidget.md#void-qwidgetscrollint-dx-int-dy)() on the viewport. Alternatively, just call [update](QAbstractItemView.md#slotvoid-qabstractitemviewupdateconst-qmodelindex-index)().

**另请参阅** [scrollContentsBy](../../A/QAbstractScrollArea/QAbstractScrollArea.md#virtual-protectedvoid-qabstractscrollareascrollcontentsbyint-dx-int-dy)(), [dirtyRegionOffset](QAbstractItemView.md#protectedqpoint-qabstractitemviewdirtyregionoffset-const)(), and [setDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewsetdirtyregionconst-qregion-region)().

### `[pure virtual]`void QAbstractItemView::scrollTo(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*, [QAbstractItemView::ScrollHint](QAbstractItemView.md#enum-qabstractitemviewscrollhint) *hint* = EnsureVisible)

Scrolls the view if necessary to ensure that the item at *index* is visible. The view will try to position the item according to the given *hint*.

In the base class this is a pure virtual function.

### `[virtual protected]`[QModelIndexList](../../M/QModelIndex/QModelIndex.md#typedef-qmodelindexlist) QAbstractItemView::selectedIndexes() const

This convenience function returns a list of all selected and non-hidden item indexes in the view. The list contains no duplicates, and is not sorted.

**另请参阅** [QItemSelectionModel::selectedIndexes](../../I/QItemSelectionModel/QItemSelectionModel.md#qmodelindexlist-qitemselectionmodelselectedindexes-const)().

### `[virtual protected]`[QItemSelectionModel::SelectionFlags](../../I/QItemSelectionModel/QItemSelectionModel.md#enum-qitemselectionmodelselectionflagflags-qitemselectionmodelselectionflags) QAbstractItemView::selectionCommand(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*, const [QEvent](../../E/QEvent/QEvent.md) **event* = nullptr) const

Returns the SelectionFlags to be used when updating a selection with to include the *index* specified. The *event* is a user input event, such as a mouse or keyboard event.

Reimplement this function to define your own selection behavior.

**另请参阅** [setSelection](QAbstractItemView.md#pure-virtual-protectedvoid-qabstractitemviewsetselectionconst-qrect-rect-qitemselectionmodelselectionflags-flags)().

### [QItemSelectionModel](../../I/QItemSelectionModel/QItemSelectionModel.md) *QAbstractItemView::selectionModel() const

Returns the current selection model.

**另请参阅** [setSelectionModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetselectionmodelqitemselectionmodel-selectionmodel)() and [selectedIndexes](QAbstractItemView.md#virtual-protectedqmodelindexlist-qabstractitemviewselectedindexes-const)().

### `[protected]`void QAbstractItemView::setDirtyRegion(const [QRegion](../../R/QRegion/QRegion.md) &*region*)

Marks the given *region* as dirty and schedules it to be updated. You only need to call this function if you are implementing your own view subclass.

This function was introduced in Qt 4.1.

**另请参阅** [scrollDirtyRegion](QAbstractItemView.md#protectedvoid-qabstractitemviewscrolldirtyregionint-dx-int-dy)() and [dirtyRegionOffset](QAbstractItemView.md#protectedqpoint-qabstractitemviewdirtyregionoffset-const)().

### void QAbstractItemView::setIndexWidget(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*, [QWidget](../../W/QWidget/QWidget.md#qwidgetqwidgetqwidget-parent--nullptr-qtwindowflags-f--qtwindowflags) **widget*)

Sets the given *widget* on the item at the given *index*, passing the ownership of the widget to the viewport.

If *index* is invalid (e.g., if you pass the root index), this function will do nothing.

The given *widget*'s [autoFillBackground](../../W/QWidget/QWidget.md) property must be set to true, otherwise the widget's background will be transparent, showing both the model data and the item at the given *index*.

If index widget A is replaced with index widget B, index widget A will be deleted. For example, in the code snippet below, the [QLineEdit](../../L/QLineEdit/QLineEdit.md) object will be deleted.

```c++
setIndexWidget(index, new QLineEdit);
...
setIndexWidget(index, new QTextEdit);
```

This function should only be used to display static content within the visible area corresponding to an item of data. If you want to display custom dynamic content or implement a custom editor widget, subclass [QStyledItemDelegate](../../S/QStyledItemDelegate/QStyledItemDelegate.md) instead.

This function was introduced in Qt 4.1.

**另请参阅** [indexWidget](QAbstractItemView.md#qwidget-qabstractitemviewindexwidgetconst-qmodelindex-index-const)() and [Delegate Classes](../../M/Model_View_Programming/Model_View_Programming.md#delegate-classes).

### void QAbstractItemView::setItemDelegate([QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) **delegate*)

Sets the item delegate for this view and its model to *delegate*. This is useful if you want complete control over the editing and display of items.

Any existing delegate will be removed, but not deleted. [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md) does not take ownership of *delegate*.

**警告：** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the [closeEditor()](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md#signalvoid-qabstractitemdelegatecloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint--nohint) signal, and attempt to access, modify or close an editor that has already been closed.

**另请参阅** [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)().

### void QAbstractItemView::setItemDelegateForColumn(int *column*, [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) **delegate*)

Sets the given item *delegate* used by this view and model for the given *column*. All items on *column* will be drawn and managed by *delegate* instead of using the default delegate (i.e., [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)()).

Any existing column delegate for *column* will be removed, but not deleted. [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md) does not take ownership of *delegate*.

**注意：** If a delegate has been assigned to both a row and a column, the row delegate will take precedence and manage the intersecting cell index.

**警告：** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the [closeEditor()](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md#signalvoid-qabstractitemdelegatecloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint--nohint) signal, and attempt to access, modify or close an editor that has already been closed.

This function was introduced in Qt 4.2.

**另请参阅** [itemDelegateForColumn](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforcolumnint-column-const)(), [setItemDelegateForRow](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforrowint-row-qabstractitemdelegate-delegate)(), and [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)().

### void QAbstractItemView::setItemDelegateForRow(int *row*, [QAbstractItemDelegate](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md) **delegate*)

Sets the given item *delegate* used by this view and model for the given *row*. All items on *row* will be drawn and managed by *delegate* instead of using the default delegate (i.e., [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)()).

Any existing row delegate for *row* will be removed, but not deleted. [QAbstractItemView](../../A/QAbstractItemView/QAbstractItemView.md) does not take ownership of *delegate*.

**注意：** If a delegate has been assigned to both a row and a column, the row delegate (i.e., this delegate) will take precedence and manage the intersecting cell index.

**警告：** You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the [closeEditor()](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md#signalvoid-qabstractitemdelegatecloseeditorqwidget-editor-qabstractitemdelegateendedithint-hint--nohint) signal, and attempt to access, modify or close an editor that has already been closed.

This function was introduced in Qt 4.2.

**另请参阅** [itemDelegateForRow](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegateforrowint-row-const)(), [setItemDelegateForColumn](QAbstractItemView.md#void-qabstractitemviewsetitemdelegateforcolumnint-column-qabstractitemdelegate-delegate)(), and [itemDelegate](QAbstractItemView.md#qabstractitemdelegate-qabstractitemviewitemdelegate-const)().

### `[virtual]`void QAbstractItemView::setModel([QAbstractItemModel](../../A/QAbstractItemModel/QAbstractItemModel.md) **model*)

Sets the *model* for the view to present.

This function will create and set a new selection model, replacing any model that was previously set with [setSelectionModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetselectionmodelqitemselectionmodel-selectionmodel)(). However, the old selection model will not be deleted as it may be shared between several views. We recommend that you delete the old selection model if it is no longer required. This is done with the following code:

```c++
QItemSelectionModel *m = view->selectionModel();
view->setModel(new model);
delete m;
```

If both the old model and the old selection model do not have parents, or if their parents are long-lived objects, it may be preferable to call their [deleteLater](../../O/QObject/QObject.md#slotvoid-qobjectdeletelater)() functions to explicitly delete them.

The view *does not* take ownership of the model unless it is the model's parent object because the model may be shared between many different views.

**另请参阅** [model](QAbstractItemView.md#qabstractitemmodel-qabstractitemviewmodel-const)(), [selectionModel](QAbstractItemView.md#qitemselectionmodel-qabstractitemviewselectionmodel-const)(), and [setSelectionModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetselectionmodelqitemselectionmodel-selectionmodel)().

### `[pure virtual protected]`void QAbstractItemView::setSelection(const [QRect](../../R/QRect/QRect.md) &*rect*, [QItemSelectionModel::SelectionFlags](../../I/QItemSelectionModel/QItemSelectionModel.md#enum-qitemselectionmodelselectionflagflags-qitemselectionmodelselectionflags) *flags*)

Applies the selection *flags* to the items in or touched by the rectangle, *rect*.

When implementing your own itemview setSelection should call [selectionModel](QAbstractItemView.md#qitemselectionmodel-qabstractitemviewselectionmodel-const)()->select(selection, flags) where selection is either an empty [QModelIndex](../../M/QModelIndex/QModelIndex.md) or a [QItemSelection](../../I/QItemSelection/QItemSelection.md) that contains all items that are contained in *rect*.

**另请参阅** [selectionCommand](QAbstractItemView.md#virtual-protectedqitemselectionmodelselectionflags-qabstractitemviewselectioncommandconst-qmodelindex-index-const-qevent-event--nullptr-const)() and [selectedIndexes](QAbstractItemView.md#virtual-protectedqmodelindexlist-qabstractitemviewselectedindexes-const)().

### `[virtual]`void QAbstractItemView::setSelectionModel([QItemSelectionModel](../../I/QItemSelectionModel/QItemSelectionModel.md) **selectionModel*)

Sets the current selection model to the given *selectionModel*.

Note that, if you call [setModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetmodelqabstractitemmodel-model)() after this function, the given *selectionModel* will be replaced by one created by the view.

**注意：** It is up to the application to delete the old selection model if it is no longer needed; i.e., if it is not being used by other views. This will happen automatically when its parent object is deleted. However, if it does not have a parent, or if the parent is a long-lived object, it may be preferable to call its [deleteLater](../../O/QObject/QObject.md#slotvoid-qobjectdeletelater)() function to explicitly delete it.

**另请参阅** [selectionModel](QAbstractItemView.md#qitemselectionmodel-qabstractitemviewselectionmodel-const)(), [setModel](QAbstractItemView.md#virtualvoid-qabstractitemviewsetmodelqabstractitemmodel-model)(), and [clearSelection](QAbstractItemView.md#slotvoid-qabstractitemviewclearselection)().

### `[protected]`void QAbstractItemView::setState([QAbstractItemView::State](QAbstractItemView.md#enum-qabstractitemviewstate) *state*)

Sets the item view's state to the given *state*.

**另请参阅** [state](QAbstractItemView.md#protectedqabstractitemviewstate-qabstractitemviewstate-const)().

### `[virtual]`int QAbstractItemView::sizeHintForColumn(int *column*) const

Returns the width size hint for the specified *column* or -1 if there is no model.

This function is used in views with a horizontal header to find the size hint for a header section based on the contents of the given *column*.

**另请参阅** [sizeHintForRow](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforrowint-row-const)().

### [QSize](../../S/QSize/QSize.md) QAbstractItemView::sizeHintForIndex(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns the size hint for the item with the specified *index* or an invalid size for invalid indexes.

**另请参阅** [sizeHintForRow](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforrowint-row-const)() and [sizeHintForColumn](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforcolumnint-column-const)().

### `[virtual]`int QAbstractItemView::sizeHintForRow(int *row*) const

Returns the height size hint for the specified *row* or -1 if there is no model.

The returned height is calculated using the size hints of the given *row*'s items, i.e. the returned value is the maximum height among the items. Note that to control the height of a row, you must reimplement the [QAbstractItemDelegate::sizeHint](../../A/QAbstractItemDelegate/QAbstractItemDelegate.md#pure-virtualqsize-qabstractitemdelegatesizehintconst-qstyleoptionviewitem-option-const-qmodelindex-index-const)() function.

This function is used in views with a vertical header to find the size hint for a header section based on the contents of the given *row*.

**另请参阅** [sizeHintForColumn](QAbstractItemView.md#virtualint-qabstractitemviewsizehintforcolumnint-column-const)().

### `[virtual protected]`void QAbstractItemView::startDrag([Qt::DropActions](../../Q/Qt_Namespace/Qt_Namespace.md#DropAction-enum) *supportedActions*)

Starts a drag by calling drag->exec() using the given *supportedActions*.

### `[protected]`[QAbstractItemView::State](QAbstractItemView.md#enum-qabstractitemviewstate) QAbstractItemView::state() const

Returns the item view's state.

**另请参阅** [setState](QAbstractItemView.md#protectedvoid-qabstractitemviewsetstateqabstractitemviewstate-state)().

### `[override virtual protected]`void QAbstractItemView::timerEvent([QTimerEvent](../../T/QTimerEvent/QTimerEvent.md) **event*)

Reimplements: [QObject::timerEvent](../../O/QObject/QObject.md#virtual-protectedvoid-qobjecttimereventqtimerevent-event)(QTimerEvent *event).

This function is called with the given *event* when a timer event is sent to the widget.

**另请参阅** [QObject::timerEvent](../../O/QObject/QObject.md#virtual-protectedvoid-qobjecttimereventqtimerevent-event)().

### `[pure virtual protected]`int QAbstractItemView::verticalOffset() const

Returns the vertical offset of the view.

In the base class this is a pure virtual function.

**另请参阅** [horizontalOffset](QAbstractItemView.md#pure-virtual-protectedint-qabstractitemviewhorizontaloffset-const)().

### `[virtual protected]`[QStyleOptionViewItem](../../S/QStyleOptionViewItem/QStyleOptionViewItem.md) QAbstractItemView::viewOptions() const

Returns a [QStyleOptionViewItem](../../S/QStyleOptionViewItem/QStyleOptionViewItem.md) structure populated with the view's palette, font, state, alignments etc.

### `[override virtual protected]`bool QAbstractItemView::viewportEvent([QEvent](../../E/QEvent/QEvent.md) **event*)

Reimplements: [QAbstractScrollArea::viewportEvent](../../A/QAbstractScrollArea/QAbstractScrollArea.md#virtual-protectedbool-qabstractscrollareaviewporteventqevent-event)(QEvent *event).

This function is used to handle tool tips, and What's This? mode, if the given *event* is a [QEvent::ToolTip](../../E/QEvent/QEvent.md#enum-qeventtype),or a [QEvent::WhatsThis](../../E/QEvent/QEvent.md#enum-qeventtype). It passes all other events on to its base class viewportEvent() handler.

Returns `true` if *event* has been recognized and processed; otherwise, returns `false`.

### `[override virtual protected]`[QSize](../../S/QSize/QSize.md) QAbstractItemView::viewportSizeHint() const

Reimplements: [QAbstractScrollArea::viewportSizeHint](../../A/QAbstractScrollArea/QAbstractScrollArea.md#virtual-protectedqsize-qabstractscrollareaviewportsizehint-const)() const.

This function was introduced in Qt 5.2.

### `[pure virtual]`[QRect](../../R/QRect/QRect.md) QAbstractItemView::visualRect(const [QModelIndex](../../M/QModelIndex/QModelIndex.md) &*index*) const

Returns the rectangle on the viewport occupied by the item at *index*.

If your item is displayed in several areas then visualRect should return the primary area that contains index and not the complete area that index might encompasses, touch or cause drawing.

In the base class this is a pure virtual function.

**另请参阅** [indexAt](QAbstractItemView.md#pure-virtualqmodelindex-qabstractitemviewindexatconst-qpoint-point-const)() and [visualRegionForSelection](QAbstractItemView.md#pure-virtual-protectedqregion-qabstractitemviewvisualregionforselectionconst-qitemselection-selection-const)().

### `[pure virtual protected]`[QRegion](../../R/QRegion/QRegion.md) QAbstractItemView::visualRegionForSelection(const [QItemSelection](../../I/QItemSelection/QItemSelection.md) &*selection*) const

Returns the region from the viewport of the items in the given *selection*.

In the base class this is a pure virtual function.

**另请参阅** [visualRect](QAbstractItemView.md#pure-virtualqrect-qabstractitemviewvisualrectconst-qmodelindex-index-const)() and [selectedIndexes](QAbstractItemView.md#virtual-protectedqmodelindexlist-qabstractitemviewselectedindexes-const)().