
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
