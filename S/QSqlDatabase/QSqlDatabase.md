
# **QSqlDatabase 类**
QSqlDatabase 类 用于处理数据库的连接

| 属性   | 方法                                                         |
| ------ | ------------------------------------------------------------ |
| 头文件 | `#include <QSqlDatabase>`                            |
| qmake  | QT += sql                                                |

[列出所有的成员，包括继承成员](https://doc.qt.io/qt-5/qsqldatabase-members.html)

----------

### **公共类型**

|  返回值  | 函数名|
|------:|:------|
||QSqlDatabase(const QSqlDatabase &other)|
||QSqlDatabase()|
 |QSqlDatabase &|operator=(const QSqlDatabase &other)|
||~QSqlDatabase()|
|void|	close()|
|bool|	commit()|
|QString|	connectOptions() const|
|QString|	connectionName() const|
|QString|	databaseName() const|
|QSqlDriver * |driver() const|
|QString|	driverName() const|
|QSqlQuery|	exec(const QString &query = QString()) const|
|QString|hostName() const|
|bool|	isOpen() const|
|bool	|isOpenError() const|
|bool	|isValid() const|
|QSqlError|lastError() const|
|QSql::NumericalPrecisionPolicy|	numericalPrecisionPolicy() const|
|bool|	open()|
|bool|open(const QString &user, const QString &password)|
|QString|	password() const|
|int|	port() const|
|QSqlIndex|	primaryIndex(const QString &tablename) const|
|QSqlRecord|	record(const QString &tablename) const|
|bool	|rollback()|
|void	|setConnectOptions(const QString &options = QString())|
|void	|setDatabaseName(const QString &name)|
|void	|setHostName(const QString &host)|
|void	|setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy precisionPolicy)|
|void	|setPassword(const QString &password)|
|void	|setPort(int port)|
|void	|setUserName(const QString &name)|
|QStringList	|tables(QSql::TableType type = QSql::Tables) const|
|bool|	transaction()|
|QString|	userName() const|

----------
 ### **静态公共成员**
 |  返回值  | 函数名|
 |------:|:------|
 |QSqlDatabase	|addDatabase(const QString &type, const QString &connectionName = QLatin1String(defaultConnection))|
 |QSqlDatabase	|addDatabase(QSqlDriver *driver, const QString &connectionName = QLatin1String(defaultConnection))|
 |QSqlDatabase	|cloneDatabase(const QSqlDatabase &other, const QString &connectionName)|
 |QSqlDatabase	|cloneDatabase(const QString &other, const QString &connectionName)|
 |QStringList|	connectionNames()|
 |bool	|contains(const QString &connectionName = QLatin1String(defaultConnection))|
 |QSqlDatabase	|database(const QString &connectionName = QLatin1String(defaultConnection), bool open = true)|
 |QStringList|	drivers()|
 |bool	|isDriverAvailable(const QString &name)|
 |void	|registerSqlDriver(const QString &name, QSqlDriverCreatorBase *creator)|
 |void	|removeDatabase(const QString &connectionName)|

 ----------
  ### **受保护的成员函数**
  |  返回值  | 函数名|
  |------:|:------|
  |	|QSqlDatabase(QSqlDriver *driver)|
  |	|QSqlDatabase(const QString &type)|

  -----------
  ### **详细的介绍**

QSqlDatabase 类提供接口用于数据库的连接 。一个 QSqlDatabase 实例对象表示连接。
这个连接提供  数据库 所需要的 驱动，这个驱动来自于  QSqlDriver。
换而言之，你可以实现自己的数据库驱动，通过继承 QSqlDriver。查看 [如何实现自己的数据库驱动](https://doc.qt.io/qt-5/sql-driver.html#how-to-write-your-own-database-driver) 来获取更多的信息。

通过调用一个静态的 ` addDatabase() `函数，来创建一个连接（即：实例化一个QSqlDatabase类）,并且可以指定驱动或者驱动类型去使用（依赖于数据库的类型 ）和 一个连接的名称。
一个连接是通过它自已的名称，而不是通过数据库的名称去连接的。对于一个数据库你可以有多个连接。`QSqlDatabase` 也支持默认连接，你可以不
传递连接名参数给 `addDatabase()` 来创建 它。随后，这个默认连接假定你 在调用任何静态函数情况下，而不去指定连接名称。
下面的一段代码片段展示了 如何去创建 和打开一个默认连接，去连接 `PostgreSQL `数据库：
```cpp
QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
db.setHostName("acidalia");
db.setDatabaseName("customdb");
db.setUserName("mojito");
db.setPassword("J0a1m8");
bool ok = db.open();
```

当你创建  `QSqlDatabase` 对象后，你就可以通过 `setDatabaseName()`、`setUserName()`、`setPassword()`、`setHostName()`,`setPort()` 以及 `setConnectOptions()`来设置连接的相关的参数。最后，通过调用 `open()`函数来实现数据库的连接。这里，你只有通过调用 `open()` 函数 才能 连接到数据库。

经过上面一系列的操作，最终实现的是默认连接，因为你没有给`addDatabase()`函数 传递 一个叫 连接名 的参数。
最终，你可以调用 `addDatabase()`并且没有传递参数（即：连接名）来实现默认连接：
```CPP
QSqlDatabase db = QSqlDatabase::database();
```
`QSqlDatabase`是一个值类。通过一个 `QSqlDatabase` 实例对数据库连接所做的操作将影响表示相同连接的其他 `QSqlDatabase` 实例。
使用 `cloneDatabase()`  在基于已存在数据库的连接 来 创建 独立的数据库的连接。

警告：强烈建议不要将QSqlDatabase的拷贝作为类成员，因为这将阻止关闭时正确清理实例。
如果需要访问已经存在QSqlDatabase，应该使用database()访问。如果你选择使用作为成员变量的QSqlDatabase，则需要在删除QCoreApplication实例之前删除它，否则可能会导致未定义的行为。

如果你想创建多个数据库连接，可以调用 `addDatabase()`, 并且给一个独一无二的参数(即：连接名称)。使用 带有连接名的`database() ` 函数，来获取该连接。使用 带有连接名的`removeDatabase()` 函数，来删除 一个连接。如果尝试删除由其他`QSqlDatabase`对象引用的连接，`QSqlDatabase`将输出警告。可以使用`contains()`查看给定的连接名是否在连接列表中。

| |一些实用的方法|
|------:|:------|
|tables()|	返回 数据表的列表|
|primaryIndex()|	返回数据表的主索引|
|record()	|返回数据表字段的元信息|
|transaction()|开始一个事务|
|commit()|保存并完成一个事务|
|rollback()|取消一个事务|
|hasFeature()|	检查驱动程序是否支持事务|
|lastError()|	返回有关上一个错误的信息|
|drivers()|返回可用的数据库驱动名称|
|isDriverAvailable()|检查特定驱动程序是否可用|
|registerSqlDriver()|	注册自定义驱动程序|

**注意：** `QSqlDatabase::exec() ` 方法已经被弃用。请使用 `QSqlQuery::exec() `

**注意：** 使用事务时，必须在创建查询之前启动事务。

### **成员函数文档**
### QSqlDatabase::QSqlDatabase(QSqlDriver *driver)  `[受保护] `   

这是一个重载函数

使用给定驱动程序来创建连接

### QSqlDatabase::QSqlDatabase(const QString &type)  `[受保护] `   

这是一个重载函数

通过引用所给的数据库驱动类型来创建一个连接。如果不给定 数据库驱动类型 ，那么这个数据库连接将会没有什么作用。

当前可用的驱动类型：

| 驱动类别|介绍|
|------:|:------|
|QDB2|	IBM DB2|
|QIBASE|	Borland InterBase 驱动|
|QMYSQL|	MySQL 驱动|
|QOCI	|Oracle 调用的接口驱动|
|QODBC|	ODBC 驱动 (包含 Microsoft SQL Server)|
|QPSQL|	PostgreSQL 驱动|
|QSQLITE|	SQLite 第三版本 或者 以上|
|QSQLITE2|	SQLite 第二版本|
|QTDS|	Sybase Adaptive Server|

其他第三方驱动程序，包括自己自定义的驱动程序，都可以动态加载。

请参阅 [SQL Database Drivers](https://doc.qt.io/qt-5/sql-driver.html), [registerSqlDriver()](https://doc.qt.io/qt-5/qsqldatabase.html#registerSqlDriver) 和 [drivers()](https://doc.qt.io/qt-5/qsqldatabase.html#drivers)。

### QSqlDatabase::QSqlDatabase(const QSqlDatabase &other)   
创建一个其它的副本

### QSqlDatabase::QSqlDatabase()
创建一个 无效的 `QSqlDatabase` 空对象。使用 [addDatabase()](https://doc.qt.io/qt-5/qsqldatabase.html#addDatabase), [removeDatabase()](https://doc.qt.io/qt-5/qsqldatabase.html#removeDatabase) 和 [database()](https://doc.qt.io/qt-5/qsqldatabase.html#database) 来获得一个有效的 `QSqlDatabase` 对象。

### QSqlDatabase &QSqlDatabase::operator=(const QSqlDatabase &other)
给这个对象赋一个其他其他对象的值

### QSqlDatabase::~QSqlDatabase()
销毁这个对象，并且释放所有配置的资源
**注意：**  当最后的连接被销毁，这个折构函数就会暗中的调用 `close()`函数，去删除这个数据库的其他连接。

查阅 [close()](https://doc.qt.io/qt-5/qsqldatabase.html#close)。
