
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
||QSqlDatabase(const [QSqlDatabase](QSqlDatabase.md#qsqldatabaseqsqldatabaseconst-qsqldatabase-other) &other)|
||[QSqlDatabase](QSqlDatabase.md#qsqldatabaseqsqldatabase)()|
 |QSqlDatabase &|[operator=](QSqlDatabase.md#qsqldatabase-qsqldatabaseoperatorconst-qsqldatabase-other)(const QSqlDatabase &other)|
||[~QSqlDatabase](QSqlDatabase.md#qsqldatabase-qsqldatabaseoperatorconst-qsqldatabase-other)()|
|void|	[close](QSqlDatabase.md#void-qsqldatabaseclose)()|
|bool|	[commit](QSqlDatabase.md#bool-qsqldatabasecommit)()|
|QString|	[connectOptions](QSqlDatabase.md#qstring-qsqldatabaseconnectoptions-const)() const|
|QString|	[connectionName](QSqlDatabase.md#qstring-qsqldatabaseconnectionname-const)() const|
|QString|	[databaseName](QSqlDatabase.md#qstring-qsqldatabasedatabasename-const)() const|
|QSqlDriver * |[driver()](QSqlDatabase.md#qsqldriver-qsqldatabasedriver-const) const|
|QString|	[driverName()](QSqlDatabase.md#qstring-qsqldatabasedrivername-const) const|
|QSqlQuery|	[exec](QSqlDatabase.md#qsqlquery-qsqldatabaseexecconst-qstring-query--qstring-const)(const QString &query = QString()) const|
|QString|[hostName()](QSqlDatabase.md#qstring-qsqldatabasehostname-const) const|
|bool|	[isOpen](QSqlDatabase.md#bool-qsqldatabaseisopen-const)() const|
|bool	|[isOpenError](QSqlDatabase.md#bool-qsqldatabaseisopenerror-const)() const|
|bool	|[isValid](QSqlDatabase.md#bool-qsqldatabaseisvalid-const)() const|
|QSqlError|[lastError](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)() const|
|QSql::NumericalPrecisionPolicy|[numericalPrecisionPolicy](QSqlDatabase.md#qsqlnumericalprecisionpolicy-qsqldatabasenumericalprecisionpolicy-const)() const|
|bool|	[open](QSqlDatabase.md#bool-qsqldatabaseopen)()|
|bool|[open](QSqlDatabase.md#bool-qsqldatabaseopenconst-qstring-user-const-qstring-password)(const QString &user, const QString &password)|
|QString|	[password](QSqlDatabase.md#qstring-qsqldatabasepassword-const)() const|
|int|	[port](QSqlDatabase.md#int-qsqldatabaseport-const)() const|
|QSqlIndex|	[primaryIndex](QSqlDatabase.md#qsqlindex-qsqldatabaseprimaryindexconst-qstring-tablename-const)(const QString &tablename) const|
|QSqlRecord|[record](QSqlDatabase.md#qsqlrecord-qsqldatabaserecordconst-qstring-tablename-const)(const QString &tablename) const|
|bool	|[rollback](QSqlDatabase.md#bool-qsqldatabaserollback)()|
|void	|[setConnectOptions](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring)(const QString &options = QString())|
|void	|[setDatabaseName](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)(const QString &name)|
|void	|[setHostName](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)(const QString &host)|
|void	|[setNumericalPrecisionPolicy](https://github.com/JackLovel/QtDocumentCN/blob/master/Src/S/QSqlDatabase/QSqlDatabase.md#void-qsqldatabasesetnumericalprecisionpolicyqsqlnumericalprecisionpolicy-precisionpolicy)(QSql::NumericalPrecisionPolicy precisionPolicy)|
|void	|[setPassword](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password)(const QString &password)|
|void	|[setPort](QSqlDatabase.md#void-qsqldatabasesetportint-port)(int port)|
|void	|[setUserName](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)(const QString &name)|
|QStringList	|[tables](QSqlDatabase.md#qstringlist-qsqldatabasetablesqsqltabletype-type--qsqltables-const)(QSql::TableType type = QSql::Tables) const|
|bool|[transaction](https://github.com/JackLovel/QtDocumentCN/blob/master/Src/S/QSqlDatabase/QSqlDatabase.md#bool-qsqldatabasetransaction)()|
|QString|[userName](QSqlDatabase.md#qstring-qsqldatabaseusername-const)() const|

----------
### **静态公共成员**

|  返回值  | 函数名|
|------:|:------|
|QSqlDatabase	|[addDatabase](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection)(const QString &type, const QString &connectionName = QLatin1String(defaultConnection))|
|QSqlDatabase	|[addDatabase](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseqsqldriver-driver-const-qstring-connectionname--qlatin1stringdefaultconnection)(QSqlDriver *driver, const QString &connectionName = QLatin1String(defaultConnection))|
|QSqlDatabase	|[cloneDatabase](QSqlDatabase.md#protected-qsqldatabase-qsqldatabaseclonedatabaseconst-qstring-other-const-qstring-connectionname)(const QSqlDatabase &other, const QString &connectionName)|
|QSqlDatabase	|[cloneDatabase](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseclonedatabaseconst-qstring-other-const-qstring-connectionname)(const QString &other, const QString &connectionName)|
|QStringList|[connectionNames](QSqlDatabase.md#static-qstringlist-qsqldatabaseconnectionnames)()|
|bool	|[contains](QSqlDatabase.md#static-bool-qsqldatabasecontainsconst-qstring-connectionname--qlatin1stringdefaultconnection)(const QString &connectionName = QLatin1String(defaultConnection))|
|QSqlDatabase	|[database](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true)(const QString &connectionName = QLatin1String(defaultConnection), bool open = true)|
|QStringList|[drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)|
|bool	|[isDriverAvailable](QSqlDatabase.md#static-bool-qsqldatabaseisdriveravailableconst-qstring-name)(const QString &name)|
|void	|[registerSqlDriver](QSqlDatabase.md#static-void-qsqldatabaseregistersqldriverconst-qstring-name-qsqldrivercreatorbase-creator)(const QString &name, QSqlDriverCreatorBase *creator)|
|void	|[removeDatabase](QSqlDatabase.md#static-void-qsqldatabaseremovedatabaseconst-qstring-connectionname)(const QString &connectionName)|


### **受保护的成员函数**

|返回值|函数名|
|------:|:------|
||[QSqlDatabase](QSqlDatabase.md#protected-qsqldatabaseqsqldatabaseqsqldriver-driver)(QSqlDriver **driver*)|
||[QSqlDatabase](QSqlDatabase.md#protected-qsqldatabaseqsqldatabaseconst-qstring-type)(const QString &*type*)|


### **详细的介绍**

QSqlDatabase 类提供接口用于数据库的连接 。一个 QSqlDatabase 实例对象表示连接。
这个连接提供  数据库 所需要的 驱动，这个驱动来自于  QSqlDriver。
换而言之，您可以实现自己的数据库驱动，通过继承 QSqlDriver。查看 [如何实现自己的数据库驱动](https://doc.qt.io/qt-5/sql-driver.html#how-to-write-your-own-database-driver) 来获取更多的信息。

通过调用一个静态的 ` addDatabase() `函数，来创建一个连接（即：实例化一个QSqlDatabase类）,并且可以指定驱动或者驱动类型去使用（依赖于数据库的类型 ）和 一个连接的名称。
一个连接是通过它自已的名称，而不是通过数据库的名称去连接的。对于一个数据库您可以有多个连接。`QSqlDatabase` 也支持默认连接，您可以不
传递连接名参数给 `addDatabase()` 来创建 它。随后，这个默认连接假定您 在调用任何静态函数情况下，而不去指定连接名称。
下面的一段代码片段展示了 如何去创建 和打开一个默认连接，去连接 `PostgreSQL `数据库：
```cpp
QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
db.setHostName("acidalia");
db.setDatabaseName("customdb");
db.setUserName("mojito");
db.setPassword("J0a1m8");
bool ok = db.open();
```

当您创建  `QSqlDatabase` 对象后，您就可以通过 `setDatabaseName()`、`setUserName()`、`setPassword()`、`setHostName()`,`setPort()` 以及 `setConnectOptions()`来设置连接的相关的参数。最后，通过调用 `open()`函数来实现数据库的连接。这里，您只有通过调用 `open()` 函数 才能 连接到数据库。

经过上面一系列的操作，最终实现的是默认连接，因为您没有给`addDatabase()`函数 传递 一个叫 连接名 的参数。
最终，您可以调用 `addDatabase()`并且没有传递参数（即：连接名）来实现默认连接：
```CPP
QSqlDatabase db = QSqlDatabase::database();
```
`QSqlDatabase`是一个值类。通过一个 `QSqlDatabase` 实例对数据库连接所做的操作将影响表示相同连接的其他 `QSqlDatabase` 实例。
使用 `cloneDatabase()`  在基于已存在数据库的连接 来 创建 独立的数据库的连接。

警告：强烈建议不要将QSqlDatabase的拷贝作为类成员，因为这将阻止关闭时正确清理实例。
如果需要访问已经存在QSqlDatabase，应该使用database()访问。如果您选择使用作为成员变量的QSqlDatabase，则需要在删除QCoreApplication实例之前删除它，否则可能会导致未定义的行为。

如果您想创建多个数据库连接，可以调用 `addDatabase()`, 并且给一个独一无二的参数(即：连接名称)。使用 带有连接名的`database() ` 函数，来获取该连接。使用 带有连接名的`removeDatabase()` 函数，来删除 一个连接。如果尝试删除由其他`QSqlDatabase`对象引用的连接，`QSqlDatabase`将输出警告。可以使用 [contains()](QSqlDatabase.md#static-bool-qsqldatabasecontainsconst-qstring-connectionname--qlatin1stringdefaultconnection)查看给定的连接名是否在连接列表中。

| |一些实用的方法|
|------:|:------|
|[tables](QSqlDatabase.md#qstringlist-qsqldatabasetablesqsqltabletype-type--qsqltables-const)()|	返回 数据表的列表|
|[primaryIndex](QSqlDatabase.md#qsqlindex-qsqldatabaseprimaryindexconst-qstring-tablename-const)()|	返回数据表的主索引|
|[record](QSqlDatabase.md#qsqlrecord-qsqldatabaserecordconst-qstring-tablename-const)()	|返回数据表字段的元信息|
|[transaction](QSqlDatabase.md#bool-qsqldatabasetransaction)()|开始一个事务|
|[commit](QSqlDatabase.md#bool-qsqldatabasecommit)()|保存并完成一个事务|
|[rollback](QSqlDatabase.md#bool-qsqldatabaserollback)()|取消一个事务|
|hasFeature()|	检查驱动程序是否支持事务|
|[lastError](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)()|	返回有关上一个错误的信息|
|[drivers](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)()|返回可用的数据库驱动名称|
|[isDriverAvailable](QSqlDatabase.md#static-bool-qsqldatabaseisdriveravailableconst-qstring-name)()|检查特定驱动程序是否可用|
|[registerSqlDriver](QSqlDatabase.md#static-void-qsqldatabaseregistersqldriverconst-qstring-name-qsqldrivercreatorbase-creator)()|	注册自定义驱动程序|

**注意：** `QSqlDatabase::exec() ` 方法已经被弃用。请使用 `QSqlQuery::exec() `

**注意：** 使用事务时，必须在创建查询之前启动事务。

### **成员函数文档**
### *[protected]* QSqlDatabase::QSqlDatabase(QSqlDriver *driver)
----------------------------------------------

这是一个重载函数

使用给定驱动程序来创建连接

### *[protected]* QSqlDatabase::QSqlDatabase(const [QString](../QString/QString.md) &*type*)
-----------------------------------------------------

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

请参阅 [SQL Database Drivers](https://doc.qt.io/qt-5/sql-driver.html), [registerSqlDriver()](QSqlDatabase.md#static-void-qsqldatabaseregistersqldriverconst-qstring-name-qsqldrivercreatorbase-creator) 和 [drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)。

### QSqlDatabase::QSqlDatabase(const QSqlDatabase &*other*)
-----------------------------------------
创建一个其它的副本

### QSqlDatabase::QSqlDatabase()
--------------------------------------------
创建一个 无效的 `QSqlDatabase` 空对象。使用 [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection), [removeDatabase()](QSqlDatabase.md#static-void-qsqldatabaseremovedatabaseconst-qstring-connectionname) 和 [database()](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true) 来获得一个有效的 `QSqlDatabase` 对象。

### QSqlDatabase &QSqlDatabase::operator=(const QSqlDatabase &*other*)
----------------------------------------------------
给这个对象赋一个其他其他对象的值

### QSqlDatabase::~QSqlDatabase()
----------------------------------------
销毁这个对象，并且释放所有配置的资源
**注意：** 当最后的连接被销毁，这个折构函数就会暗中的调用 `close()`函数，去删除这个数据库的其他连接。

另请参阅 [close()](QSqlDatabase.md#void-qsqldatabaseclose)。

### *[static]* QSqlDatabase QSqlDatabase::addDatabase(const QString &type, const QString &connectionName = QLatin1String(defaultConnection))
----------------------------

使用驱动程序类型和连接名称，将数据库添加到数据库连接列表中。如果存在相同的连接名，那么这个连接将会被删除。

通过引用连接名，来返回一个新的连接。

如果数据库的类别不存在或者没有被加载，那么 `isValid()`函数将会返回 `false`

如果我们没有指定连接名参数，那么应用程序就会返回默认连接。
如果我们提供了连接名参数，那么可以使用`database(connectionName)` 函数来获取该连接。

**警告：** 如果您指定了 相同的连接名参数，那么就会替换之前的那个相同的连接。如果您多次调用这个函数而不指定 `连接名参数`，则默认连接将被替换。

在使用连接之前，它必须经过初始化。比如：
调用下面一些或者全部 [ setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)、
[setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)、 [setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password) 、
[setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)、
[setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)
和 [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring)，并最终调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)

**注意：** 这个函数是线程安全的

请查看 [database()](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true), [removeDatabase()](QSqlDatabase.md#static-void-qsqldatabaseremovedatabaseconst-qstring-connectionname) 以及 [线程和SQL 单元](https://doc.qt.io/qt-5/threads-modules.html#threads-and-the-sql-module)。

### *[static]* QSqlDatabase QSqlDatabase::addDatabase(QSqlDriver *driver, const QString &connectionName = QLatin1String(defaultConnection))
----------------------------
这个重载函数是非常有用的，当您想创建一个带有[驱动](https://doc.qt.io/qt-5/qsqldriver.html) 连接时，您可以实例化它。有可能您想拥有自己的数据库驱动，或者去实例化 Qt自带的驱动。如果您真的想这样做，我非常建议您把驱动的代码导入到您的应用程序中。例如，您可用自已的  QPSQL 驱动来创建一个 PostgreSQL 连接，像下面这样：
```CPP
PGconn *con = PQconnectdb("host=server user=bart password=simpson dbname=springfield");
QPSQLDriver *drv = new QPSQLDriver(con);
QSqlDatabase db = QSqlDatabase::addDatabase(drv); // 产生成新的默认连接
QSqlQuery query;
query.exec("SELECT NAME, ID FROM STAFF");
```
上面的代码用于设置一个 PostgreSQL 连接和实例化一个 QPSQLDriver 对象。接下来，`addDatabase()` 被调用产生一个已知的连接，以便于它可以使用 `Qt SQL` 相关的类。Qt假定您已经打开了数据库连接，当使用连接句柄（或一组句柄）实例化驱动程序时。

**注意：** 我们假设qtdir是安装Qt的目录。假定您的`PostgreSQL`头文件己经包含在搜索路径中，然后这里才能引用所需要的`PostgreSQL`客户端库和去实例化`QPSQLDriver`对象。

请记住，必须将数据库客户端库到您的程序里。确保客户端库在您的链接器的搜索路径中，并且像下面这样添加到您的 `.pro` 文件里：
```
unix:LIBS += -lpq
win32:LIBS += libpqdll.lib
```
这里介绍了所有驱动支持的方法。只有驱动的构造参数有所不同。列举了一个关于 Qt附带的程序，以及它们的源代码文件，和它们的构造函数参数的列表：


| 驱动|类名|构造器参数|用于导入的文件|
|:------|:------|:------|:------|
|QPSQL|QPSQLDriver|PGconn *connection	|qsql_psql.cpp|
|QMYSQL|	QMYSQLDriver|	MYSQL *connection|	qsql_mysql.cpp|
|QOCI|	QOCIDriver|	OCIEnv *environment, OCISvcCtx *serviceContext|	qsql_oci.cpp|
|QODBC|	QODBCDriver|	SQLHANDLE environment, SQLHANDLE connection|	qsql_odbc.cpp|
|QDB2|	QDB2|	SQLHANDLE environment, SQLHANDLE connection|	qsql_db2.cpp|
|QTDS|	QTDSDriver|	LOGINREC *loginRecord, DBPROCESS *dbProcess, const [QString](../QString/QString.md) &[hostName](QSqlDatabase.md#qstring-qsqldatabasehostname-const)|	qsql_tds.cpp|
|QSQLITE|	QSQLiteDriver|	sqlite *connection|	qsql_sqlite.cpp|
|QIBASE|	QIBaseDriver|	isc_db_handle connection|	qsql_ibase.cpp|

当构造用于为内部查询创建新连接的`QTDSDriver`时，需要主机名（或服务名）。这是为了防止在同时使用多个`QSqlQuery`对象时发生阻塞。

**警告：** 添加一个存在连接名的连接时，这个新添加的连接将会替换另一个。
**警告：** SQL框架拥有驱动程序的所有权。它不能被删除。可以使用[removeDatabase()](QSqlDatabase.md#static-void-qsqldatabaseremovedatabaseconst-qstring-connectionname)，去删除这个连接。
**另请参阅**[drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)

### *[protected]* QSqlDatabase QSqlDatabase::cloneDatabase(const [QString](../QString/QString.md) &*other*, const [QString](../QString/QString.md) &*connectionName*)
-----------------------------------------------------
克隆其他数据库连接并将其存储为`connectionName`。原始数据库中的所有设置，例如[databaseName()](QSqlDatabase.md#qstring-qsqldatabasedatabasename-const)、[hostName()](QSqlDatabase.md#qstring-qsqldatabasehostname-const)等，都会被复制。如果其他数据库无效，则不执行任何操作。返回最新被创建的数据库连接。

**注意：** 这个新的连接不能被打开。您必须调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen),才能使用这个新的连接。

### *[static]* QSqlDatabase QSqlDatabase::cloneDatabase(const [QString](../QString/QString.md) &*other*, const [QString](../QString/QString.md) &*connectionName*)
------------------------------------
这是个重载函数。

克隆其他数据库连接并将其存储为`connectionName`。原始数据库中的所有设置，例如[databaseName()](QSqlDatabase.md#qstring-qsqldatabasedatabasename-const)、[hostName()](QSqlDatabase.md#qstring-qsqldatabasehostname-const)等，都会被复制。如果其他数据库无效，则不执行任何操作。返回最新被创建的数据库连接。

**注意：** 这个新的连接不能被打开。您必须调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen),才能使用这个新的连接。

当我们在另一个线程克隆这个数据库，这个重载是非常有用的。

qt5.13中引入了这个函数。

### void QSqlDatabase::close()
-----------
关闭数据库连接，释放获取的所有资源，并使与数据库一起使用的任何现有QSqlQuery对象无效

这个函数也会影响它的[QSqlDatabase](QSqlDatabase.md)对象副本。

**另请参阅** [removeDatabase()](QSqlDatabase.md#static-void-qsqldatabaseremovedatabaseconst-qstring-connectionname)

### bool QSqlDatabase::commit()
------------------------------

如果驱动支持事务和一个[transaction()](QSqlDatabase.md#bool-qsqldatabasetransaction)已经被启动，那就可以提交一个事务到这个数据库中。如果这个操作成功，就会返回 `true`。否则返回 `false`。

**注意：** 对于一些数据库，如果对数据库使用`SELECT`进行查询操作，将会提交失败并且返回`false`。在执行提交之前，使查询处于非活动状态。

调用 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const) 函数获取错误信息。

**另请参阅**  [QSqlQuery::isActive()](https://doc.qt.io/qt-5/qsqlquery.html#isActive)， [QSqlDriver::hasFeature()](https://doc.qt.io/qt-5/qsqldriver.html#hasFeature)，和 [rollback()](https://doc.qt.io/qt-5/qsqldatabase.html#rollback)。

### [QString](../QString/QString.md) QSqlDatabase::connectOptions() const
--------------------------------
返回用于此连接的连接选项字符串。这个字符串可能是空。

**另请参阅** [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring)

### [QString](../QString/QString.md) QSqlDatabase::connectionName() const
--------------------------
返回连接名，它有可能为空。

**注意：** 这个连接名不是 [数据库名](QSqlDatabase.md#qstring-qsqldatabasedatabasename-const)

`qt4.4` 中引入了这个函数。

**另请参阅** [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection)

### *[static]* [QStringList]([QString](../QStringList/QStringList.md)) QSqlDatabase::connectionNames()
---------------------------------------

返回包含所有连接名称的列表。

**注意：** 这个函数是[线程安全](https://doc.qt.io/qt-5/threads-reentrancy.html)的。

**另请参阅** [contains](QSqlDatabase.md#static-bool-qsqldatabasecontainsconst-qstring-connectionname--qlatin1stringdefaultconnection)()，[database](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true)()， 和 [线程和SQL模块](https://doc.qt.io/qt-5/threads-modules.html#threads-and-the-sql-module)

### *[static]* bool QSqlDatabase::contains(const QString &*connectionName* = QLatin1String(defaultConnection))
------------------------
如果所给的连接名，包含在所给的数据库连接列表里，那么就返回 `true`；否则返回 `false`。

**注意：** 这个函数是 [线程安全的](https://doc.qt.io/qt-5/threads-reentrancy.html)

**另请参阅** [connectionNames()](QSqlDatabase.md#static-qstringlist-qsqldatabaseconnectionnames), [database](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true)() 和 [线程和SQL模块](https://doc.qt.io/qt-5/threads-modules.html#threads-and-the-sql-module)。

### *[static]* QSqlDatabase QSqlDatabase::database(const QString &connectionName = QLatin1String(defaultConnection), bool open = true)
---------------------
返回一个调用 `connectionName` 参数的数据库连接。这个数据库连接使用之前，必须已经通过 [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection) 函数进行添加。如果open为true（默认值），并且数据库连接尚未打开，则现在打开它。如果未指定连接名参数，则使用默认连接。如果连接名不存在数据库列表中，那么将会返回一个非法的连接。

**注意：** 这个函数是 [线程安全的](https://doc.qt.io/qt-5/threads-reentrancy.html)

**另请参阅** [isOpen()](QSqlDatabase.md#bool-qsqldatabaseisopen-const) 和 [线程和SQL模块](https://doc.qt.io/qt-5/threads-modules.html#threads-and-the-sql-module)。

### QString QSqlDatabase::databaseName() const

-----------------------
返回连接的连接数据库名称，当然它也可能是空的。

**注意：** 这个数据库名不是连接名

**另请参阅** [setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)。

### QSqlDriver *QSqlDatabase::driver() const
-----------------------------
返回被使用的数据库连接的所使用的数据库驱动。

**另请参阅** [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection) 和 [drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)

### QString QSqlDatabase::driverName() const
-----------------------------
返回连接的驱动名称

**另请参阅** [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection) 和 [driver()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)

### *[static]* [QStringList](../QStringList/QStringList.md) QSqlDatabase::drivers()
------------------

返回一个可使用的数据库驱动列表
**另请参阅** [registerSqlDriver()](QSqlDatabase.md#static-void-qsqldatabaseregistersqldriverconst-qstring-name-qsqldrivercreatorbase-creator)

### QSqlQuery QSqlDatabase::exec(const QString &*query* = QString()) const
------------------------

在这个数据库里执行 `SQL` 表达式和 返回一个 QSq[https://doc.qt.io/qt-5/qsqlquery.html](https://doc.qt.io/qt-5/qsqlquery.html) 对象。使用 [ lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const) 来获取错误的信息。

如果查询为空，则返回一个空的、无效的查询。并且 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)。

**另请参阅** [QSqlQuery]() 和 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)。

### [QString](../QString/QString.md) QSqlDatabase::hostName() const
-------------------
返回连接的主机名；它有可能为空。

**另请参阅** [setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)

### *[static]* bool QSqlDatabase::isDriverAvailable(const QString &*name*)
----------------

如果调用一个叫 `name` 的驱动，是可以使用的，那么就返回 `true`；反之返回 `false`。

**另请参阅** [drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)。

### bool QSqlDatabase::isOpen() const
-----------------
如果当前数据库连接是打开的，那么就返回 `true`，否则返回 `false`。

### bool QSqlDatabase::isOpenError() const
-------------------------------
如果打开数据库的连接有错误，那么就返回 `true`，否则返回 `false`。可以调用 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const) 函数去获取相关的错误信息。

### bool QSqlDatabase::isValid() const
-------------
如果 [QSqlDatabase()](QSqlDatabase.md) 有一个有效的驱动，那么就返回 `true`。

例子：
```CPP
QSqlDatabase db;
qDebug() << db.isValid();    // 返回 false

db = QSqlDatabase::database("sales");
qDebug() << db.isValid();    // 如果 "sales" 连接存在，就返回 true

QSqlDatabase::removeDatabase("sales");
qDebug() << db.isValid();    // 返回 false
```

### [QSqlError](https://doc.qt.io/qt-5/qsqlerror.html) QSqlDatabase::lastError() const

返回这个数据库出现的最新错误信息。

使用 [QSqlQuery::lastError()](https://doc.qt.io/qt-5/qsqlquery.html#lastError) 函数来获取一个单个查询上的错误。

**另请参阅**  [QSqlError](https://doc.qt.io/qt-5/qsqlerror.html) and [QSqlQuery::lastError()](https://doc.qt.io/qt-5/qsqlquery.html#lastError)。

### [QSql::NumericalPrecisionPolicy](https://doc.qt.io/qt-5/qsql.html#NumericalPrecisionPolicy-enum)QSqlDatabase::numericalPrecisionPolicy() const

返回数据库连接的当前默认精度策略。

qt4.6中引入了这个函数。

**另请参阅** [QSql::NumericalPrecisionPolicy, setNumericalPrecisionPolicy()](https://doc.qt.io/qt-5/qsqldatabase.html#setNumericalPrecisionPolicy)、[QSqlQuery::numericalPrecisionPolicy()](https://doc.qt.io/qt-5/qsqlquery.html#numericalPrecisionPolicy) 和 [QSqlQuery::setNumericalPrecisionPolicy()](https://doc.qt.io/qt-5/qsqlquery.html#setNumericalPrecisionPolicy)。

### bool QSqlDatabase::open()
---------------
使用当前连接值打开数据库连接。如果操作成功就返回 `true`; 反之返回 `false`。可以调用 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)来获取错误的信息。

**另请参阅** [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)、 [setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)、[setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)、[setPassword()](https://doc.qt.io/qt-5/qsqldatabase.html#setPassword)、[setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)、[setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)和 [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring)。

### bool QSqlDatabase::open(const [QString](../QString/QString.md) &*user*, const [QString](../QString/QString.md) &*password*)
-------------------
这是一个重载函数。

使用所给的 `username` 和 `password` 两个参数，打开数据连接，如果成功就返回 `true`; 反之返回 `false`。使用 [lastError()]QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const) 来获取错误的信息。

这个函数不存放所给的 `password` 参数，相反的它会把 `password` 参数直接传给驱动用于打连接，然后销毁这个参数。

**另请参阅** [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const)


### [QString](https://doc.qt.io/qt-5/qstring.html) QSqlDatabase::password() const
------------------
返回连接的密码。如果没有使用[setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password) 函数进行密码的设置 并且 没有调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen) 以及 没有使用密码，那么就返回空的字符串。

**另请参阅** [setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password)

### int QSqlDatabase::port() const
-----------------
返回连接的端口号。如果端口号没有设置，那么这个值就是未定义的。

**另请参阅** [setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)

../QString/QString.md
### [QSqlIndex](../QSqlIndex/QSqlIndex.md) QSqlDatabase::primaryIndex(const [QString](../QString/QString.md) &*tablename*) const
---------------------------

返回所给表格名的索引。如果索引不存在，那么就返回一个空的 [QSqlIndex](https://doc.qt.io/qt-5/qsqlindex.html)

**注意：** 如果表在创建时没有被引用，一些驱动程序（如 `QPSQL` 驱动程序）可能要求您以小写的形式传递表格名。

查看关于 [Qt SQL driver](https://doc.qt.io/qt-5/sql-driver.html) 文档的更多信息。

**另请参阅**  [tables()](QSqlDatabase.md#qstringlist-qsqldatabasetablesqsqltabletype-type--qsqltables-const) 和 [record()](QSqlDatabase.md#qsqlrecord-qsqldatabaserecordconst-qstring-tablename-const)。

### [QSqlRecord](../QSqlRecord/QSqlRecord.md) QSqlDatabase::record(const [QString](../QString/QString.md) &*tablename*) const
-----------------------------------
返回一个[QSqlRecord](https://doc.qt.io/qt-5/qsqlrecord.html)，其中填充了名为tablename的表（或视图）中所有字段的名称。字段在记录中出现的顺序未定义。如果没有这样的表格（或者视图）存在，将会返回一个空的记录。

**注意：** 如果表在创建时没有被引用，一些驱动程序（如 [QPSQL](https://doc.qt.io/qt-5/sql-driver.html#qpsql-case-sensitivity) 驱动程序）可能要求您以小写的形式传递表格名。

查看 [Qt SQL driver](https://doc.qt.io/qt-5/sql-driver.html) 文档的更多信息。

### *[static]* void QSqlDatabase::registerSqlDriver(const [QString](../QString/QString.md) &*name*, [QSqlDriverCreatorBase](../QSqlDriverCreatorBase/QSqlDriverCreatorBase.md) **creator*)
----------------------
这个函数在 `SQL`框架中注册一个名为 `name` 的新 `SQL` 驱动程序。这个是非常有用的，如果您有一个自定义的驱动，并且您并不想把它编译作为一个插件。

例如：
```CPP
QSqlDatabase::registerSqlDriver("MYDRIVER", new QSqlDriverCreator<QSqlDriver>);
QVERIFY(QSqlDatabase::drivers().contains("MYDRIVER"));
QSqlDatabase db = QSqlDatabase::addDatabase("MYDRIVER");
QVERIFY(db.isValid());
```
[QSqlDatabase]()拥有 `creator` 指针的所有权，因此您不能自己删除它。

**另请参阅** [drivers()](QSqlDatabase.md#static-qstringlist-qsqldatabasedrivers)。

### *[static]* void QSqlDatabase::removeDatabase(const [QString](../QString/QString.md) &*connectionName*)
-------------------------------
从数据库列表中，删除一个叫 `connectionName` 数据库连接。

**警告：** 不应在数据库连接上打开查询的情况下调用此函数，否则将发生资源泄漏。

例子：
```CPP
// 错误
QSqlDatabase db = QSqlDatabase::database("sales");
QSqlQuery query("SELECT NAME, DOB FROM EMPLOYEES", db);
QSqlDatabase::removeDatabase("sales"); // 将会输出警告
// “db”现在是一个悬而未决的无效数据库连接，
// “查询”包含无效的结果集
```

正确的做法：
```CPP
{
    QSqlDatabase db = QSqlDatabase::database("sales");
    QSqlQuery query("SELECT NAME, DOB FROM EMPLOYEES", db);
}
// “db”和“query”都被销毁，因为它们超出了范围
QSqlDatabase::removeDatabase("sales"); // 正确的
```

如果要删除默认连接，这个连接可能是通过调用 [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection) 函数而创建的，但未指定连接名称，可以通过对[database()](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true)返回的数据库调用[connectionName()](QSqlDatabase.md#qstring-qsqldatabaseconnectionname-const) 来检索默认连接名称。注意，如果没有创建默认数据库，将返回一个无效的数据库。

**注意：** 这个函数是[线程安全的](https://doc.qt.io/qt-5/threads-reentrancy.html)

**另请查阅** [database()](QSqlDatabase.md#static-qsqldatabase-qsqldatabasedatabaseconst-qstring-connectionname--qlatin1stringdefaultconnection-bool-open--true)，[connectionName()](QSqlDatabase.md#qstring-qsqldatabaseconnectionname-const)，和 [线程和SQL模块](https://doc.qt.io/qt-5/threads-modules.html#threads-and-the-sql-module)。

### bool QSqlDatabase::rollback()
---------------
在数据库里回滚一个事务，如果驱动支持一个事务以及一个 [transaction()](QSqlDatabase.md#bool-qsqldatabasetransaction) 已经被启动。如果操作成功返回 `true`。否则返回 `false`。

**注意：** 对于某些数据库，如果存在使用数据库进行选择的[活动查询](https://doc.qt.io/qt-5/qsqlquery.html#isActive)，则回滚将失败并返回false。确保在执行回滚操作之前，查询是 [非活动](https://doc.qt.io/qt-5/qsqlquery.html#isActive) 的状态。

调用 [lastError()](QSqlDatabase.md#qsqlerror-qsqldatabaselasterror-const) 操作获得错误的相关信息。

**另请查阅**  [QSqlQuery::isActive()](https://doc.qt.io/qt-5/qsqlquery.html#isActive)，[QSqlDriver::hasFeature()](https://doc.qt.io/qt-5/qsqldriver.html#hasFeature) 和 [commit()](QSqlDatabase.md#bool-qsqldatabasecommit)。

### void QSqlDatabase::setConnectOptions(const [QString](../QString/QString.md) &*options* = QString())
----------------------------
设置一组数据库的具体的可选项。它必须在打之这个连接之前执行这个操作，否则是无效的。另一个可能的原因是调用 `QSqlDatabase::setConnectOptions()` 去关闭这个连接，并且调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen) 再次关闭这个连接。

选项字符串的格式是以分号分隔的选项名称，或选项=值对的列表。这个选项依赖于所使用的客户端：

| ODBC |MySQL|PostgreSQL|
|:------|:------|:------|
|SQL_ATTR_ACCESS_MODE|CLIENT_COMPRESS|connect_timeout|
|SQL_ATTR_LOGIN_TIMEOUT|CLIENT_FOUND_ROWS|options|
|SQL_ATTR_CONNECTION_TIMEOUT|CLIENT_IGNORE_SPACE|tty|
|SQL_ATTR_CURRENT_CATALOG|CLIENT_ODBC|requiressl|
|SQL_ATTR_METADATA_ID|CLIENT_NO_SCHEMA|service|
|SQL_ATTR_PACKET_SIZE|CLIENT_INTERACTIVE||
|SQL_ATTR_TRACEFILE|UNIX_SOCKET||
|SQL_ATTR_TRACE|MYSQL_OPT_RECONNECT||
|SQL_ATTR_CONNECTION_POOLING|MYSQL_OPT_CONNECT_TIMEOUT||
|SQL_ATTR_ODBC_VERSION|MYSQL_OPT_READ_TIMEOUT||
| |MYSQL_OPT_WRITE_TIMEOUT||
|   |SSL_KEY||
|   |SSL_CERT||
|    |SSL_CA||
|    |SSL_CAPATH||
|    |SSL_CIPHER||


| DB2 |OCI|TDS|
|:------|:------|:------|
|SQL_ATTR_ACCESS_MODE|OCI_ATTR_PREFETCH_ROWS|无|
|SQL_ATTR_LOGIN_TIMEOUT|OCI_ATTR_PREFETCH_MEMORY||


|[SQLite](https://doc.qt.io/qt-5/qtsql-attribution-sqlite.html#sqlite) |Interbase|
|:------|:------|
|QSQLITE_BUSY_TIMEOUT|ISC_DPB_LC_CTYPE|
|QSQLITE_OPEN_READONLY|ISC_DPB_SQL_ROLE_NAME|
|QSQLITE_OPEN_URI||
|QSQLITE_ENABLE_SHARED_CACHE||
|QSQLITE_ENABLE_REGEXP||

例子：
```CPP
db.setConnectOptions("SSL_KEY=client-key.pem;SSL_CERT=client-cert.pem;SSL_CA=ca-cert.pem;CLIENT_IGNORE_SPACE=1"); // 使用安全套连字进行连接
if (!db.open()) {
    db.setConnectOptions(); // 清除连接的字符串
    // ...
}
// ...
// PostgreSQL 连接
db.setConnectOptions("requiressl=1"); // 确保 PostgreSQL 安全套接字连接
if (!db.open()) {
    db.setConnectOptions(); // 清除可选
    // ...
}
// ...
// ODBC 连接
db.setConnectOptions("SQL_ATTR_ACCESS_MODE=SQL_MODE_READ_ONLY;SQL_ATTR_TRACE=SQL_OPT_TRACE_ON"); // 设置 ODBC 连项
if (!db.open()) {
    db.setConnectOptions(); // 不要尝试去设置这个选项。
    // ...
}
}
```

查阅这个客户端库文档，获得更多关于不同可选项的更多信息。

**另请查阅** [connectOptions()](QSqlDatabase.md#qstring-qsqldatabaseconnectoptions-const)。

### void QSqlDatabase::setDatabaseName(const [QString](../QString/QString.md) &*name*)
-------------------
通过所给的 `name` 参数来设置所连接的数据库名称。必须在[打开](QSqlDatabase.md#bool-qsqldatabaseopen)连接之前设置数据库名称。
或者，可以调用[close()](QSqlDatabase.md#void-qsqldatabaseclose)函数关闭连接，设置数据库名称，然后再次调用[open()](QSqlDatabase.md#bool-qsqldatabaseopen) 。

**注意：** 这个数据库名不是连接名。必须在创建连接对象时将连接名称传递给 [addDatabase()](QSqlDatabase.md#static-qsqldatabase-qsqldatabaseadddatabaseconst-qstring-type-const-qstring-connectionname--qlatin1stringdefaultconnection)。

对于 `QSQLITE` 驱动，如果数据库名指定的名字不存在，然后它将会创建这个文件，除非您设置了 `QSQLITE_OPEN_READONLY`

此外，可以把 `name` 参数设置为 `:memory:`, 可以创建一个临时数据库，该数据库仅在应用程序的生命周期内可用。

对于 `QOCI (Oracle)` 驱动，这个数据库名是 ` TNS Service Name`。

对于 `QODBC` 驱动程序，名称可以是`DSN`，`DSN`文件名（在这种情况下，文件扩展名必须为`.DSN`）或者是一个连接字符串。

例如，`Microsoft Access` 可以使用下面的连接方式来直接打开 `.mdb` 文件，而不是在 `ODBC` 管理工具里创建一个 `DSN` 对象：

```CPP
// ...
QSqlDatabase db = QSqlDatabase::addDatabase("QODBC");
db.setDatabaseName("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};FIL={MS Access};DBQ=myaccessfile.mdb");
if (db.open()) {
    // 成功!
}
// ...
```

这个没有默认的值

**另请查阅** [databaseName()](QSqlDatabase.md#qstring-qsqldatabasedatabasename-const)、[setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)、 [setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password)、 [setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)、 [setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)、[setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring) 和 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)。

### void QSqlDatabase::setHostName(const [QString](../QString/QString.md) &*host*)
----------------------------------------
通过 `host` 参数来设置连接的主机名。为了生效，必须在[打开](QSqlDatabase.md#bool-qsqldatabaseopen)连接之前，设置主机名。或者，可以调用[close()](QSqlDatabase.md#void-qsqldatabaseclose)关闭连接，然后设置主机名，再次调用[open()](QSqlDatabase.md#bool-qsqldatabaseopen)函数。


这个没有默认值。

**另请查阅** [hostName()](QSqlDatabase.md#qstring-qsqldatabasehostname-const)， [setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name), [setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password)，[setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-nam)，[setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)， [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring) 和 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)。

### void QSqlDatabase::setNumericalPrecisionPolicy([QSql::NumericalPrecisionPolicy](../S/QSql.md#enum-qsqlnumericalprecisionpolicy) *precisionPolicy*)
-----------------------------------
设置在此数据库连接上创建的查询使用的默认数值精度策略。

**注意：** 驱动程序不支持以低精度获取数值，将忽略精度策略。您可以使用 [QSqlDriver::hasFeature()](https://doc.qt.io/qt-5/qsqldriver.html#hasFeature)来查找一个驱动是否支持这个功能。

**注意：** 通过 `precisionPolicy` 来设置这个默认的精度策略，将不会响影任何当前的活动查询。

qt4.6中引入了这个函数。

**另请查阅** [QSql::NumericalPrecisionPolicy](../QSql/QSql.md#enum-qsqlnumericalprecisionpolicy)， [numericalPrecisionPolicy()](QSqlDatabase.md#qsqlnumericalprecisionpolicy-qsqldatabasenumericalprecisionpolicy-const)，[QSqlQuery::setNumericalPrecisionPolicy](https://doc.qt.io/qt-5/qsqlquery.html#setNumericalPrecisionPolicy) 和 [QSqlQuery::numericalPrecisionPolicy](https://doc.qt.io/qt-5/qsqlquery.html#numericalPrecisionPolicy).

### void QSqlDatabase::setPassword(const [QString](../QString/QString.md) &*password*)
------------------------
通过 `password` 参数来设置连接的密码。为了生效，必须在[打开](QSqlDatabase.md#bool-qsqldatabaseopen)连接之前来设置密码。或者，您可以调用[close()](QSqlDatabase.md#void-qsqldatabaseclose)关闭连接，然后设置密码，再次调用[open()](QSqlDatabase.md#bool-qsqldatabaseopen)函数。

这个没有默认值。

**警告：** 这个函数以明文的形式把密码存放到qt里。 将密码作为参数来避免这个行为，然后使用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)进行调用。

**另请查阅** [password()](QSqlDatabase.md#qstring-qsqldatabasepassword-const)，[setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)，[setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)，[setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host), [setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port), [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring)和 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)。

### void QSqlDatabase::setPort(int *port*)
----------------
通过`port`参数设置连接的端口号。为了生效，您必须在[打开](QSqlDatabase.md#bool-qsqldatabaseopen)连接之前，进行端口号的设置。或者，您可以调用[close()](QSqlDatabase.md#void-qsqldatabaseclose)关闭连接，然后设置端口号，再次调用[open()](QSqlDatabase.md#bool-qsqldatabaseopen)函数

这个没有默认的值。

**另请查阅** [port()](QSqlDatabase.md#int-qsqldatabaseport-const), [setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)， [setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password), [setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)，[setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name), [setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring) 和 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)。

### void QSqlDatabase::setUserName(const [QString](../QString/QString.md) &*name*)
--------------------
通过 `name` 参数来设置连接的用户名。为了生效，必须在[打开](QSqlDatabase.md#bool-qsqldatabaseopen)连接之前设置用户名。或者，您可以调用 [close()](QSqlDatabase.md#void-qsqldatabaseclose)函数来关闭连接，设置用户，然后再次调用 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)

这个没有默认值。

**另请查阅** [userName()](QSqlDatabase.md#qstring-qsqldatabaseusername-const)，[setDatabaseName()](QSqlDatabase.md#void-qsqldatabasesetdatabasenameconst-qstring-name)，[setPassword()](QSqlDatabase.md#void-qsqldatabasesetpasswordconst-qstring-password)， [setHostName()](QSqlDatabase.md#void-qsqldatabasesethostnameconst-qstring-host)，[setPort()](QSqlDatabase.md#void-qsqldatabasesetportint-port)，[setConnectOptions()](QSqlDatabase.md#void-qsqldatabasesetconnectoptionsconst-qstring-options--qstring) 和 [open()](QSqlDatabase.md#bool-qsqldatabaseopen)。

### [QStringList](../QStringList/QStringList.md) QSqlDatabase::tables([QSql::TableType](https://doc.qt.io/qt-5/qsql.html#TableType-enum) *type* = QSql::Tables) const
--------------------------
返回由 `parameter type` 参数 指定的数据库的表格、系统表和视图的列表。

**另请查阅** [primaryIndex()](QSqlDatabase.md#qsqlindex-qsqldatabaseprimaryindexconst-qstring-tablename-const) 和 [record()](QSqlDatabase.md#qsqlrecord-qsqldatabaserecordconst-qstring-tablename-const)。

### bool QSqlDatabase::transaction()
----------------
如果驱动程序支持事务，则在数据库上开始事务。如果操作成功的话，返回 `true`, 否则返回 `false`。

**另请查阅** [QSqlDriver::hasFeature()](https://doc.qt.io/qt-5/qsqldriver.html#hasFeature)， [commit()](QSqlDatabase.md#bool-qsqldatabasecommit) 和 [rollback()](QSqlDatabase.md#bool-qsqldatabaserollback)。

### [QString](../QString/QString.md) QSqlDatabase::userName() const
--------------
返回连接的用户名; 它也许为空。

**另请查阅** [setUserName()](QSqlDatabase.md#void-qsqldatabasesetusernameconst-qstring-name)。
