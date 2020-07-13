
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
