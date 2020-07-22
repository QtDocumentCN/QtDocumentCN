#  QSql 命名空间

QSql 命名空间 里的 各种名样的标识符，已经被运用在 Qt SQL 各个模块中。[更多](https://doc.qt.io/qt-5/qsql.html#details)


| 属性   | 方法                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | `#include <QSql>`                            |
| qmake  | QT += sql                                                |

## 类型

|||
|------|:------|
|enum	|[Location](https://doc.qt.io/qt-5/qsql.html#Location-enum) { BeforeFirstRow, AfterLastRow }|
|enum	|[NumericalPrecisionPolicy](https://doc.qt.io/qt-5/qsql.html#NumericalPrecisionPolicy-enum) { LowPrecisionInt32, LowPrecisionInt64, LowPrecisionDouble, HighPrecision }|
|flags	|[ParamType](https://doc.qt.io/qt-5/qsql.html#ParamTypeFlag-enum)|
|enum|	[ParamTypeFlag](https://doc.qt.io/qt-5/qsql.html#ParamTypeFlag-enum) { In, Out, InOut, Binary }|
|enum	|[TableType](https://doc.qt.io/qt-5/qsql.html#TableType-enum) { Tables, SystemTables, Views, AllTables }|

## 细节的介绍
查看 [Qt SQL](https://doc.qt.io/qt-5/qtsql-index.html)

## 类型 文档

### enum QSql::Location

此枚举类型描述特殊的sql导航位置：
|  常量  | 值| 介绍|
|------|:------:|:------|
|QSql::BeforeFirstRow | -1 |在第一个记录之前|
|QSql::AfterLastRow	|-2|在最后一个记录之后|
**另请参阅** [QSqlQuery::at()](https://doc.qt.io/qt-5/qsqlquery.html#at)

### enum QSql::NumericalPrecisionPolicy

数据库中的数值可以比它们对应的C++类型更精确。此枚举列出在应用程序中表示此类值的策略。
|  常量  | 值| 介绍|
|------|:------:|:------|
|QSql::LowPrecisionInt32|	0x01|对于32位的整形数值。在浮点数的情况下，小数部分将会被舍去。|
|QSql::LowPrecisionInt64|	0x02|	对于64位的整形数值。在浮点数的情况下，小数部分将会被舍去。|
|QSql::LowPrecisionDouble| 0x04	|强制双精度值。这个默认的规则|
|QSql::HighPrecision|	0	|字符串将会维技精度|

**注意：** 如果特定的驱动发生溢出，这是一个真实行为。像 `Oracle`数据库在这种情形下，就会返回一个错误。

### enum QSql::ParamTypeFlag
### flags QSql::ParamType
这个枚举用于指定绑定参数的类型

|  常量  | 值| 介绍|
|------|:------:|:------|
|QSql::In | 0x00000001 |这个参数被用于向数据库里写入数据|
|QSql::Out | 0x00000002 |这个参数被用于向数据库里获得数据|
|QSql::InOut | In \| Out|这个参数被用于向数据库里写入数据;使用 查询 来向数据库里，重写数据|
|QSql::Binary | 0x00000004|如果您想 显示数据为 原始的二进制数据，那么必须是 OR'd 和其他的标志一 起使用|

类型参数 类型定义为 [QFlags](../QFlags/QFlags.md)<ParamTypeFlag>.  它被存放在 一个 `OR`与  类型参数标志的值 的组合。

### enum QSql::TableType
这个枚举类型描述 SQL 表格的类型。

|  常量  | 值| 介绍|
|------|:------:|:------|
|QSql::Tables | 0x01 |所有表格对用户都是可被查看的|
|QSql::SystemTables | 0x02 |该表格被作为数据库的内部表格|
|QSql::Views | 0x04|所有示图对用户都是可见的|
|QSql::AllTables | 0xff|包含以上所有类型|
