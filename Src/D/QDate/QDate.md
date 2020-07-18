[TOC]

# QDate Class


| 属性   | 方法               |
| ------ | ------------------ |
| 头文件 | #include `<QDate>` |
| qmake  | QT += core         |

**注意：** 该类提供的所有函数都是可重入的。



## 公共成员类型

| 类型 | 名称                                                                          |
| ---- | ----------------------------------------------------------------------------- |
| enum | [MonthNameType](#enum-qdatemonthnametype){ DateFormat, StandaloneFormat } |



## 公共成员函数

| 类型      | 函数名                                                       |
| --------- | ------------------------------------------------------------ |
|           | **[QDate](#qdateqdateint-y-int-m-int-d)**(int *y*, int *m*, int *d*) |
|           | **[QDate](#qdateqdate)**()                                   |
| QDate     | **[addDays](#qdate-qdateadddaysqint64-ndays-const)**(qint64 *ndays*) const |
| QDate     | **[addMonths](#qdate-qdateaddmonthsint-nmonths-qcalendar-cal-const)**(int *nmonths*, QCalendar *cal*) const |
| QDate     | **[addMonths](#qdate-qdateaddmonthsint-nmonths-const)**(int *nmonths*) const |
| QDate     | **[addYears](#qdate-qdateaddyearsint-nyears-qcalendar-cal-const)**(int *nyears*, QCalendar *cal*) const |
| QDate     | **[addYears](#qdate-qdateaddyearsint-nyears-const)**(int *nyears*) const |
| int       | **[day](#int-qdatedayqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[day](#int-qdateday-const)**() const                       |
| int       | **[dayOfWeek](#int-qdatedayofweekqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[dayOfWeek](#int-qdatedayofweek-const)**() const           |
| int       | **[dayOfYear](#int-qdatedayofyearqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[dayOfYear](#int-qdatedayofyear-const)**() const           |
| int       | **[daysInMonth](#int-qdatedaysinmonthqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[daysInMonth](#int-qdatedaysinmonth-const)**() const       |
| int       | **[daysInYear](#int-qdatedaysinyearqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[daysInYear](#int-qdatedaysinyear-const)**() const         |
| qint64    | **[daysTo](#qint64-qdatedaystoconst-qdate-d-const)**(const QDate &*d*) const |
| QDateTime | **[endOfDay](#qdatetime-qdateendofdayqttimespec-spec--qtlocaltime-int-offsetseconds--0-const)**(Qt::TimeSpec *spec* = Qt::LocalTime, int *offsetSeconds* = 0) const |
| QDateTime | **[endOfDay](#qdatetime-qdateendofdayconst-qtimezone-zone-const)**(const QTimeZone &*zone*) const |
| void      | **[getDate](#void-qdategetdateint-year-int-month-int-day-const)**(int *\*year*, int *\*month*, int *\*day*) const |
| bool      | **[isNull](#bool-qdateisnull-const)**() const                |
| bool      | **[isValid](#bool-qdateisvalid-const)**() const              |
| int       | **[month](#int-qdatemonthqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[month](#int-qdatemonth-const)**() const                   |
| bool      | **[setDate](#bool-qdatesetdateint-year-int-month-int-day)**(int *year*, int *month*, int *day*) |
| bool      | **[setDate](#bool-qdatesetdateint-year-int-month-int-day-qcalendar-cal)**(int *year*, int *month*, int *day*, QCalendar *cal*) |
| QDateTime | **[startOfDay](#qdatetime-qdateendofdayqttimespec-spec--qtlocaltime-int-offsetseconds--0-const)**(Qt::TimeSpec *spec* = Qt::LocalTime, int *offsetSeconds* = 0) const |
| QDateTime | **[startOfDay](#qdatetime-qdatestartofdayconst-qtimezone-zone-const)**(const QTimeZone &*zone*) const |
| qint64    | **[toJulianDay](#qint64-qdatetojulianday-const)**() const    |
| QString   | **[toString](#qstring-qdatetostringqtdateformat-format--qttextdate-const)**(Qt::DateFormat *format* = Qt::TextDate) const |
| QString   | **[toString](#qstring-qdatetostringconst-qstring-format-const)**(const QString &*format*) const |
| QString   | **[toString](#qstring-qdatetostringconst-qstring-format-qcalendar-cal-const)**(const QString &*format*, QCalendar *cal*) const |
| QString   | **[toString](#qstring-qdatetostringqstringview-format-const)**(QStringView *format*) const |
| QString   | **[toString](#qstring-qdatetostringqstringview-format-qcalendar-cal-const)**(QStringView *format*, QCalendar *cal*) const |
| int       | **[weekNumber](#int-qdateweeknumberint-yearnumber--nullptr-const)**(int **yearNumber* = nullptr) const |
| int       | **[year](#int-qdateyearqcalendar-cal-const)**(QCalendar *cal*) const |
| int       | **[year](#int-qdateyear-const)**() const                     |
| bool      | **[operator!=](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |
| bool      | **[operator<](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |
| bool      | **[operator<=](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |
| bool      | **[operator==](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |
| bool      | **[operator>](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |
| bool      | **[operator>=](#bool-qdateoperatorconst-qdate-d-const)**(const QDate &*d*) const |



## 静态公共成员

| 类型  | 函数名                                                       |
| ----- | ------------------------------------------------------------ |
| QDate | **[currentDate](#static-qdate-qdatecurrentdate)**()          |
| QDate | **[fromJulianDay](#staticqdate-qdatefromjuliandayqint64-jd)**(qint64 *jd*) |
| QDate | **[fromString](#staticqdate-qdatefromstringconst-qstring-string-qtdateformat-format--qttextdate)**(const QString &*string*, Qt::DateFormat *format* = Qt::TextDate) |
| QDate | **[fromString](#staticqdate-qdatefromstringconst-qstring-string-const-qstring-format)**(const QString &*string*, const QString &*format*) |
| QDate | **[fromString](#staticqdate-qdatefromstringconst-qstring-string-const-qstring-format-qcalendarcal)**(const QString &*string*, const QString &*format*, QCalendar *cal*) |
| bool  | **[isLeapYear](#staticbool-qdateisleapyearint-year)**(int *year*) |
| bool  | **[isValid](#staticbool-qdateisvalidint-year-int-month-int-day)**(int *year*, int *month*, int *day*) |



## 相关非成员函数

| 类型          | 函数名                                                       |
| ------------- | ------------------------------------------------------------ |
| QDataStream & | **[operator<<](#../QDataStream/QDataStream.md#qdatastream-operatorqdatastream-out-const-qdate-date)**(QDataStream &*out*, const QDate &*date*) |
| QDataStream & | **[operator>>](#../QDataStream/QDataStream.md#qdatastream-operatorqdatastream-in-qdate-date)**(QDataStream &*in*, QDate &*date*) |



## 详细描述

无论系统的日历和地域设置如何，一个`QDate`对象代表特定的一天。它可以告诉你某一天的年、月、日，其对应于着格里高利历或者你提供的`QCalendar`。

一个`QDate`对象一般提供显式给定的年月日创建。注意`QDate`将1~99的年数保持，不做任何偏移。静态函数currentDate()会创建一个从系统时间读取的`QDate`对象。显式的日期设定也可以使用 setDate()。fromString() 函数返回一个由日期字符串和日期格式确定的日期。

year(), month(), day() 函数可以访问年月日。另外，还有 dayOfWeek() , dayOfYear() 返回一周或一年中的天数。文字形式的信息可以通过`toString()`获得。天数和月数可以由`QLocale`类映射成文字。

QDate提供比较两个对象的全套操作，小于意味着日期靠前。

你可以通过addDays()给日期增减几天，同样的还有 addMonths() , addYears() 增减几个月、几年。daysTo() 函数返回两个日期相距的天数。

daysInMonth() 和 daysInYear() 函数返回一个月、一年里有几天。isLeapYear() 用于判断闰年。

### 特别注意

- 年数没有0
  第0年的日期是非法的。公元后是正年份，公元前是负年份。`QDate(1, 1, 1)`的前一天是`QDate(-1, 12, 31)`。

- 合法的日期范围
  日期内部存储为儒略日天号，每天对应一个连续的整数，公元前4714年11月24日是格里高利历第0天（儒略历的公元前4713年1月1日）。除了可以准确有效地表示绝对日期，此类也可以用来做不同日历系统的转换。儒略历天数可以通过 QDate::toJulianDay() 和 QDate::fromJulianDay() 读写。
  由于技术原因，储存的儒略历天号在-784350574879~784354017364之间，大概是公元前2亿年到公元后2亿年之间。

另参考：[QTime](https://doc.qt.io/qt-5/qtime.html) , [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) , [QCalendar](../../C/QCalendar/QCalendar.md) , [QDateTime::YearRange](https://doc.qt.io/qt-5/qdatetime.html#YearRange-enum) , [QDateEdit](https://doc.qt.io/qt-5/qdateedit.html) , [QDateTimeEdit](https://doc.qt.io/qt-5/qdatetimeedit.html) , and [QCalendarWidget](https://doc.qt.io/qt-5/qcalendarwidget.html)。



## 成员类型文档

### enum QDate::MonthNameType

此枚举描述字符串中月份名称的表示类型

| 常量                      | 数值 | 描述                                                               |
| ------------------------- | ---- | ------------------------------------------------------------------ |
| `QDate::DateFormat`       | `0`  | 用于日期到字符串格式化。                                           |
| `QDate::StandaloneFormat` | `1`  | 用于枚举月份和一周七天。通常单独的名字用首字母大写的单数形式书写。 |

此枚举在Qt 4.5中引入或修改。



## 成员函数文档

### [QString](../../S/QString/QString.md) QDate::toString([QStringView](../../S/QStringView/QStringView.md) *format*) const

### [QString](../../S/QString/QString.md) QDate::toString([QStringView](../../S/QStringView/QStringView.md) *format*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

### [QString](../../S/QString/QString.md) QDate::toString(const [QString](../../S/QString/QString.md) &*format*) const

### [QString](../../S/QString/QString.md) QDate::toString(const [QString](../../S/QString/QString.md) &*format*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回字符串形式的日期。 参数*format*控制输出的格式。如果传入参数*cal*, 它决定了使用的日历系统，默认是格里高利历。

日期格式的表示如下：

| 占位符 |                                                                     输出格式                                                                     |
| :----: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
|   d    |                                                             无占位0的日期 (1 to 31)                                                              |
|   dd   |                                                             有占位0的日期 (01 to 31)                                                             |
|  ddd   |    简写的一周七天名称(例如 'Mon' to 'Sun')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()     |
|  dddd  | 长版的一周七天名称 (例如 'Monday' to 'Sunday')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)() |
|   M    |                                                             无占位0的月份 (1 to 12)                                                              |
|   MM   |                                                             有占位0的月份 (01 to 12)                                                             |
|  MMM   |      缩写的月份名称 (例如 'Jan' to 'Dec')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()      |
|  MMMM  | 长版的月份名称 (例如 'January' to 'December')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()  |
|   yy   |                                                              两位数年份 (00 to 99)                                                               |
|  yyyy  |                                                   四位数年份。 如果是负数，加上符号是五个字符                                                    |

单引号包裹的内容将会一字不差地放进输出到字符串中 (不带外面的单引号), 尽管包含上述格式占位符。连续两个单引号('')会被转义成一个单引号输出。所有其他字符不会被转义，将原封不动输出。

没有分隔符的多个占位符(例如 "ddMM")受支持，但要慎用。因为结果的可读性不好，易引起多义(例如“dM”的输出"212"就分不清2.12还是21,2)

假设今天是1969年7月20日，下面是一些格式字符串的例子

|       格式        |       结果        |
| :---------------: | :---------------: |
|    dd.MM.yyyy     |    20.07.1969     |
|   ddd MMMM d yy   |  Sun July 20 69   |
| 'The day is' dddd | The day is Sunday |

如果日期非法，返回空字符串。

**注意：** 如果需要本地化的月份日期表达, 请使用 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)().[toString](#qstring-qdatetostringconst-qstring-format-const)(), 因为 QDate 将在 Qt 6使用英文表达 (C语言风格) 。

**另参考：** [fromString](#staticqdate-qdatefromstringconst-qstring-string-const-qstring-format)() , [QDateTime::toString](https://doc.qt.io/qt-5/qdatetime.html#toString)() , [QTime::toString](https://doc.qt.io/qt-5/qtime.html#toString)(), and [QLocale::toString](https://doc.qt.io/qt-5/qlocale.html#toString)()。

----

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QDate::endOfDay([Qt::TimeSpec](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) *spec* = Qt::LocalTime, int *offsetSeconds* = 0) const

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QDate::endOfDay(const [QTimeZone](../../T/QTimeZone/QTimeZone.md) &*zone*) const

返回这一天的最后一刻的时间。通常来说，是午夜前1ms：然而，如果时区转换让这一天跨过午夜（如夏令时），返回的是真实的最后一刻时间。这种情况只可能在使用时区参数 [QTimeZone](../../T/QTimeZone/QTimeZone.md) *zone*或者本地时间参数 [Qt::LocalTime](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) *spec*时发生。

参数 *offsetSeconds* 会被忽略，除非参数 *spec* 为 [Qt::OffsetFromUTC](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum)，其表示出了时区信息。如果UTC和那个时区间没有过渡，一天的结束是 [QTime](https://doc.qt.io/qt-5/qtime.html)(23, 59, 59, 999)。

在罕见的日期被整体跳过（只在从东向西跨越国际日期变更线时），返回可能是非法的。将 [Qt::TimeZone](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) 作为 *spec* 参数传递 (而不是一个 [QTimeZone](../../T/QTimeZone/QTimeZone.md)) 也会造成非法结果，如果那一时刻超过了 [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) 的表示范围。

函数在 Qt 5.14 中引入。

**另参考：** [startOfDay](#qdatetime-qdateendofdayqttimespec-spec--qtlocaltime-int-offsetseconds--0-const)()。

----

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QDate::startOfDay([Qt::TimeSpec](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) *spec* = Qt::LocalTime, int *offsetSeconds* = 0) const

### [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) QDate::startOfDay(const [QTimeZone](../../T/QTimeZone/QTimeZone.md) &*zone*) const

返回一天的开始时刻。通常来说应该是午夜那一时刻：然而，如果时区转换让这一天跨过午夜（如夏令时），返回的是真实的最早的一刻时间。这种情况只可能在使用时区参数 [QTimeZone](../../T/QTimeZone/QTimeZone.md) *zone*或者本地时间参数 [Qt::LocalTime](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) *spec*时发生。

参数 *offsetSeconds* 会被忽略，除非参数 *spec* 为 [Qt::OffsetFromUTC](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum)，其表示出了时区信息。如果UTC和那个时区间没有过渡，一天的结束是 [QTime](https://doc.qt.io/qt-5/qtime.html)(0, 0)。

在罕见的日期被整体跳过（只在从东向西跨越国际日期变更线时），返回可能是非法的。

将 [Qt::TimeZone](https://doc.qt.io/qt-5/qt.html#TimeSpec-enum) 作为 *spec* 参数传递 (而不是一个 [QTimeZone](../../T/QTimeZone/QTimeZone.md)) 也会造成非法结果，如果那一时刻超过了 [QDateTime](https://doc.qt.io/qt-5/qdatetime.html) 的表示范围。

函数在 Qt 5.14 中引入。

**另参考：** [endOfDay](#qdatetime-qdateendofdayqttimespec-spec--qtlocaltime-int-offsetseconds--0-const)()。

----

### QDate::QDate(int *y*, int *m*, int *d*)

从年月日构造对象，使用格里高利历。如果日期非法，对象不会修改，且 [isValid](#bool-qdateisvalid-const)() 返回`false`。

**警告：** 1~99年就对应于它本身，不会偏移。第0年是非法的。

**另参考：** [isValid](#bool-qdateisvalid-const)() and [QCalendar::dateFromParts](../../C/QCalendar/QCalendar.md#dateFromParts)()。



### QDate::QDate()

构造一个空的日期，也是不可用的。

**另参考：** [isNull](#bool-qdateisnull-const)() and [isValid](#bool-qdateisvalid-const)()。

----

### QDate QDate::addDays([qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *ndays*) const

返回一个 *ndays* 天之后的新日期对象(负数意味着往前减日期)。

当当前日期或新日期是非法日期时，返回非法日期。

**另参考：** [addMonths](#qdate-qdateaddmonthsint-nmonths-const)() , [addYears](#qdate-qdateaddyearsint-nyears-const)(), and [daysTo](#qint64-qdatedaystoconst-qdate-d-const)()。

----

### QDate QDate::addMonths(int *nmonths*) const

### QDate QDate::addMonths(int *nmonths*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回一个 *nmonths*月之后的新日期对象(负数意味着往前减日期)。

如果传入 *cal* 参数，会使用日历系统使用，否则使用格里高利历。

**注意：** 如果新的日期超出年、月的合理范围，函数讲返回那个月中最接近的日期。

**另参考：** [addDays](#qdate-qdateadddaysqint64-ndays-const)() and [addYears](#qdate-qdateaddyearsint-nyears-const)()。

----

### QDate QDate::addYears(int *nyears*) const

### QDate QDate::addYears(int *nyears*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回一个 *nyears* 年之后的新日期对象(负数意味着往前减日期)。

如果传入 *cal* 参数，会使用日历系统使用，否则使用格里高利历。

**注意：** 如果新的日期超出年、月的合理范围，函数讲返回那个月中最接近的日期。

**另参考：** [addDays](#qdate-qdateadddaysqint64-ndays-const)() and [addMonths](#qdate-qdateaddmonthsint-nmonths-const)()。

----

### `[static]` QDate QDate::currentDate()

返回系统时钟所示的今天的日期对象。

**另参考：** [QTime::currentTime](https://doc.qt.io/qt-5/qtime.html#currentTime)() and [QDateTime::currentDateTime](https://doc.qt.io/qt-5/qdatetime.html#currentDateTime)()。

----

### int QDate::day() const

### int QDate::day([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回日期是当前月份的第几天。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历。非法日期则返回0。

一些日历系统中，返回值可能大于7。

**另参考：** [year](#int-qdateyear-const)() , [month](#int-qdatemonth-const)() , and [dayOfWeek](#int-qdatedayofweek-const)()。

----

### int QDate::dayOfWeek() const

### int QDate::dayOfWeek([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回日期是当前周的第几天（1=周一，7=周日）。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历。非法日期则返回0。

一些日历系统中，返回值可能大于7。

**另参考：** [day](#int-qdateday-const)() , [dayOfYear](#int-qdatedayofyear-const)() , and [Qt::DayOfWeek](https://doc.qt.io/qt-5/qt.html#DayOfWeek-enum)。

----

### int QDate::dayOfYear() const

### int QDate::dayOfYear([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回日期是当年的第几天（第一天返回1）。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历。非法日期则返回0。

**另参考：** [day](#int-qdateday-const)() and [dayOfWeek](#int-qdatedayofweek-const)()。

----

### int QDate::daysInMonth() const

### int QDate::daysInMonth([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回日期对应的月份中总天数。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历 (返回值是 28~31)。非法日期则返回0。

**另参考：** [day](#int-qdateday-const)() and [daysInYear](#int-qdatedaysinyear-const)()。

----

### int QDate::daysInYear() const

### int QDate::daysInYear([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回日期对应的一年中的总天数。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历 (返回值是 365 或 366)。非法日期则返回0。

**另参考：** [day](#int-qdateday-const)() and [daysInMonth](#int-qdatedaysinmonth-const)()。

----

### [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QDate::daysTo(const QDate &*d*) const

返回两个日期相差的天数 (*d* 日期靠前则返回为负)。

如果比较的二者中有非法日期，返回0。

示例:

```
QDate d1(1995, 5, 17);  // May 17, 1995
QDate d2(1995, 5, 20);  // May 20, 1995
d1.daysTo(d2);          // returns 3
d2.daysTo(d1);          // returns -3
```

**另参考：** [addDays](#qdate-qdateadddaysqint64-ndays-const)()。

----

### `[static]`QDate QDate::fromJulianDay([qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) *jd*)

将jd表示的儒略日解析为日期并返回。

**另参考：** [toJulianDay](#qint64-qdatetojulianday-const)()。

----

### `[static]`QDate QDate::fromString(const [QString](../../S/QString/QString.md) &*string*, [Qt::DateFormat](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) *format* = Qt::TextDate)

返回  *string* 表示的  QDate 对象，非法字符串不会被解析。

注意 [Qt::TextDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum): 建议使用英文的简写月份名称(例如 "Jan")。尽管本地化的月份名在Qt5在也可以使用，但这依赖于用户的地域设置。

**注意：** 对于本地化日期的支持，包括以下日期格式—— [Qt::SystemLocaleDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) , [Qt::SystemLocaleShortDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) , [Qt::SystemLocaleLongDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) , [Qt::LocaleDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), [Qt::DefaultLocaleShortDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 和[Qt::DefaultLocaleLongDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) , 将会在Qt6中移除。使用 [QLocale::toDate](https://doc.qt.io/qt-5/qlocale.html#toDate)() 来代替。

**另参考：** [toString](#qstring-qdatetostringconst-qstring-format-const)() 和 [QLocale::toDate](https://doc.qt.io/qt-5/qlocale.html#toDate)()。

----

### `[static]`QDate QDate::fromString(const [QString](../../S/QString/QString.md) &*string*, const [QString](../../S/QString/QString.md) &*format*)

### `[static]`QDate QDate::fromString(const [QString](../../S/QString/QString.md) &*string*, const [QString](../../S/QString/QString.md) &*format*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*)

返回  *string* 表示的  QDate 对象，非法字符串不会被解析。

如果传入 *cal* 参数，会使用此日历系统，否则使用格里高利历。下面的格式描述针对于格里高利历，其它日历可能不同。

日期格式的表示如下：

| 占位符 |                                                                     输出格式                                                                     |
| :----: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
|   d    |                                                             无占位0的日期 (1 to 31)                                                              |
|   dd   |                                                             有占位0的日期 (01 to 31)                                                             |
|  ddd   |    简写的一周七天名称(例如 'Mon' to 'Sun')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()     |
|  dddd  | 长版的一周七天名称 (例如 'Monday' to 'Sunday')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)() |
|   M    |                                                             无占位0的月份 (1 to 12)                                                              |
|   MM   |                                                             有占位0的月份 (01 to 12)                                                             |
|  MMM   |      缩写的月份名称 (例如 'Jan' to 'Dec')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()      |
|  MMMM  | 长版的月份名称 (例如 'January' to 'December')。使用系统地域设置来格式化, 也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()  |
|   yy   |                                                              两位数年份 (00 to 99)                                                               |
|  yyyy  |                                                   四位数年份。 如果是负数，加上符号是五个字符                                                    |

**注意：** 不行此函数的其他版, 日期和月份名必须使用用户本地语言。只有用户语言是英语时，英文名称才适用。

所有其他字符将会被舍弃，单引号('')包裹的内容，无论是否包含格式占位符也会被舍弃。例如：

```
QDate date = QDate::fromString("1MM12car2003", "d'MM'MMcaryyyy");
// date is 1 December 2003
```

如果字符串不符合格式，一个将返回一个非法的 QDate。不需要前面补0的格式是贪婪的，这意味着他们会读取两位数，尽管数字大小超出日期合法范围，并且会占据给后续格式读取的数字位置。例如，下面的日期可以表示1月30日，但M格式会捕获两位数字，导致日期返回非法：

```
QDate date = QDate::fromString("130", "Md"); // invalid
```

年月日中，没有出现在格式中的，将会使用如下默认值：

| 字段  | 默认值 |
| :---: | :----: |
| Year  |  1900  |
| Month |   1    |
|  Day  |   1    |

下面是默认值的示例：

```
QDate::fromString("1.30", "M.d");           // January 30 1900
QDate::fromString("20000110", "yyyyMMdd");  // January 10, 2000
QDate::fromString("20000110", "yyyyMd");    // January 10, 2000
```

**注意：** 如果使用本地化的日期月份名称, 请使用 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)().toDate() , 因为 QDate 将在 Qt 6 中仅接受英文表达 (C语言风格) 。

**另参考：** [toString](#qstring-qdatetostringconst-qstring-format-const)() , [QDateTime::fromString](https://doc.qt.io/qt-5/qdatetime.html#fromString)() , [QTime::fromString](https://doc.qt.io/qt-5/qtime.html#fromString)() , and [QLocale::toDate](https://doc.qt.io/qt-5/qlocale.html#toDate)()。

----

### void QDate::getDate(int *\*year*, int *\*month*, int *\*day*) const

读取日期，储存到 *\*year*, *\*month*, and *\*day*。指针可以是空指针。

如果日期非法，返回的是0。

**注意：**在 Qt 5.7 之前, 这个函数不是常函数。

此函数在 Qt 4.5 中引入。

**另参考：** [year](#int-qdateyear-const)() , [month](#int-qdatemonth-const)() , [day](#int-qdateday-const)() , [isValid](#bool-qdateisvalid-const)() , and [QCalendar::partsFromDate](../../C/QCalendar/QCalendar.md#partsFromDate)()。

----

### `[static]`bool QDate::isLeapYear(int *year*)

判断是否是格里高利历的闰年，是则返回true。

**另参考：** [QCalendar::isLeapYear](../../C/QCalendar/QCalendar.md#isLeapYear)()。

----

### bool QDate::isNull() const

判断日期是否为空，日期为空则返回true。 空日期是非法的。

**注意：** 行为与 [isValid](#bool-qdateisvalid-const)() 等价。

**另参考：** [isValid](#bool-qdateisvalid-const)()。

----

### bool QDate::isValid() const

判断日期是否合法，合法返回true。

**另参考：** [isNull](#bool-qdateisnull-const)() and [QCalendar::isDateValid](../../C/QCalendar/QCalendar.md#isDateValid)()。

----

### `[static]`bool QDate::isValid(int *year*, int *month*, int *day*)

是上述方法的重载。

判断日期（以格里高利历解析）是否合法，合法返回true。

例如：

```
QDate::isValid(2002, 5, 17);  // true
QDate::isValid(2002, 2, 30);  // false (2月没有20日)
QDate::isValid(2004, 2, 29);  // true (是闰年)
QDate::isValid(2000, 2, 29);  // true (是闰年)
QDate::isValid(2006, 2, 29);  // false (不是闰年)
QDate::isValid(2100, 2, 29);  // false (不是闰年)
QDate::isValid(1202, 6, 6);   // true (即使这一年在格里高利历之前)
```

**另参考：** [isNull](#bool-qdateisnull-const)() , [setDate](#setDate)() , and [QCalendar::isDateValid](../../C/QCalendar/QCalendar.md#isDateValid)()。

----

### int QDate::month() const

### int QDate::month([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回月份编号，第一个月返回1。

如果传入 *cal* 参数，会使用日历系统使用，否则使用格里高利历。

对于格里高利历，1月就是咱中文说的阳历一月。

对于非法日期返回0。注意有一些日历中，月份可能多于12个。

**另参考：** [year](#int-qdateyear-const)() and [day](#int-qdateday-const)()。

----

### bool QDate::setDate(int *year*, int *month*, int *day*)

设置对应的日期，使用的是格里高利历。 如果设置的日期合法，将返回true，否则日期标记为非法并返回false。

此函数在 Qt 4.2 中引入。

**另参考：** [isValid](#bool-qdateisvalid-const)() and [QCalendar::dateFromParts](../../C/QCalendar/QCalendar.md#dateFromParts)()。

----

### bool QDate::setDate(int *year*, int *month*, int *day*, [QCalendar](../../C/QCalendar/QCalendar.md) *cal*)

设置对应的日期，使用的是cal对应的日历。如果设置的日期合法，将返回true，否则日期标记为非法并返回false。

函数在 Qt 5.14 中引入。

**另参考：** [isValid](#bool-qdateisvalid-const)() and [QCalendar::dateFromParts](../../C/QCalendar/QCalendar.md#dateFromParts)()。

----

### [qint64](https://doc.qt.io/qt-5/qtglobal.html#qint64-typedef) QDate::toJulianDay() const

将日期转换为儒略日。

**另参考：** [fromJulianDay](#staticqdate-qdatefromjuliandayqint64-jd)()。

----

### [QString](../../S/QString/QString.md) QDate::toString([Qt::DateFormat](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) *format* = Qt::TextDate) const

这是一个重载函数，返回日期的字符串。 *format* 参数决定字符串格式。

如果 *format* 是 [Qt::TextDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), 日期使用默认格式。日期月份将使用系统地域设置，也就是 [QLocale::system](https://doc.qt.io/qt-5/qlocale.html#system)()。一个例子是 "Sat May 20 1995"。

如果 *format* 是 [Qt::ISODate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), 字符串按照 ISO 8601 格式展开, 格式形如 yyyy-MM-dd。例如2002-01-05

*format* 中的 [Qt::SystemLocaleDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), [Qt::SystemLocaleShortDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 和[Qt::SystemLocaleLongDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 将在 Qt 6 中删除。这些应当由 [QLocale::system().toString(date, QLocale::ShortFormat)](https://doc.qt.io/qt-5/qlocale.html#toString) 或 [QLocale::system().toString(date, QLocale::LongFormat)](https://doc.qt.io/qt-5/qlocale.html#toString)替代。

*format* 中的 [Qt::LocaleDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), [Qt::DefaultLocaleShortDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 和[Qt::DefaultLocaleLongDate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 将在 Qt 6 中删除。这些应当由  [QLocale().toString(date, QLocale::ShortFormat)](https://doc.qt.io/qt-5/qlocale.html#toString) 或 [QLocale().toString(date, QLocale::LongFormat)](https://doc.qt.io/qt-5/qlocale.html#toString) 替代。

如果 *format* 是 [Qt::RFC2822Date](https://doc.qt.io/qt-5/qt.html#DateFormat-enum), 字符串会转换成 [RFC 2822](http://www.rfc-editor.org/rfc/rfc2822.txt) 兼容的格式。示例其一是 "20 May 1995"。

如果日期非法，返回空字符串。

**警告：**  [Qt::ISODate](https://doc.qt.io/qt-5/qt.html#DateFormat-enum) 格式只在0~9999年可用。

**另参考：** [fromString](#staticqdate-qdatefromstringconst-qstring-string-const-qstring-format)() and [QLocale::toString](https://doc.qt.io/qt-5/qlocale.html#toString)()。

----

### int QDate::weekNumber(int **yearNumber* = nullptr) const

返回 ISO 8601 周序号 (1 到 53)。对于非法日期返回0。

如果 *yearNumber* 不是`nullptr`(默认参数), 年号返回值存于`*yearNumber`。

根据 ISO 8601, 格里高利历中，跨年的周属于天数更多的那年。 由于 ISO 8601 规定一周始于周一，周三在哪一年这周就属于哪一年。 大多数年有52周，但也有53周的年份。

**注意：** *\*yearNumber* 不总是与 [year](#int-qdateyear-const)() 相等。例如, 2000.1.1是1999年第52周, 2002.12.31是2003年第1周。

**另参考：** [isValid](#bool-qdateisvalid-const)()。

----

### int QDate::year() const

### int QDate::year([QCalendar](../../C/QCalendar/QCalendar.md) *cal*) const

返回整数型的年份。

如果传入参数 *cal* , 它决定了使用的日历系统，默认是格里高利历。

如果日期不合法，返回0。在一些日历系统中，比第一年早的年份非法。

如果使用包含第0年的日历系统，在返回0时通过 [isValid](#bool-qdateisvalid-const)() 判断是否合法。这些日历正常的使用负年份，-1年的下一年是0年，再下一年是1年。

一些日历中，没有0年份但是有负数年份。例如格里高利历，公元前x年就是年份-x。

**另参考：** [month](#int-qdatemonth-const)() , [day](#int-qdateday-const)() , [QCalendar::hasYearZero](../../C/QCalendar/QCalendar.md#hasYearZero)() , and [QCalendar::isProleptic](../../C/QCalendar/QCalendar.md#isProleptic)()。

### bool QDate::operator!=(const QDate &*d*) const

### bool QDate::operator<(const QDate &*d*) const

### bool QDate::operator<=(const QDate &*d*) const

### bool QDate::operator==(const QDate &*d*) const

### bool QDate::operator>(const QDate &*d*) const

### bool QDate::operator>=(const QDate &*d*) const

对于日期A和B，大于意味着日期靠后，小于意味着日期靠前，相等就是同一天。



## 相关非成员函数

### [QDataStream](../QDataStream/QDataStream.md) &operator<<([QDataStream](../QDataStream/QDataStream.md) &*out*, const QDate &*date*)

向数据流写入日期

**另参考：** [Serializing Qt Data Types](https://doc.qt.io/qt-5/datastreamformat.html)。

### [QDataStream](../QDataStream/QDataStream.md) &operator>>([QDataStream](../QDataStream/QDataStream.md) &*in*, QDate &*date*)

从数据流读出日期

**另参考：** [Serializing Qt Data Types](https://doc.qt.io/qt-5/datastreamformat.html)。