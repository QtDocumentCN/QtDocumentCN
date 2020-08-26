[TOC]



# QJsonParseError Struct

QJsonParseError类用于在JSON解析期间报告错误。

| 属性     | 方法                                  |
| -------- | ------------------------------------- |
| 头文件： | Header:	#include <QJsonParseError> |
| qmake:   | QT += core                            |
| 从：     | Qt5.0                                 |

该结构在5.0被引入。

**注意：** 该结构的所有函数都是[可重入](https://doc.qt.io/qt-5/threads-reentrancy.html).。

## 公共类型

| 类型 | 枚举                                                         |
| ---- | ------------------------------------------------------------ |
| enum | **[ParseError](https://doc.qt.io/qt-5/qjsonparseerror.html#ParseError-enum)** { NoError, UnterminatedObject, MissingNameSeparator, UnterminatedArray, MissingValueSeparator, …, GarbageAtEnd } |

## 公共成员函数

| 类型    | 函数名                                                       |
| ------- | ------------------------------------------------------------ |
| QString | **[errorString](https://doc.qt.io/qt-5/qjsonparseerror.html#errorString)**() const |

## 公共变量

| 类型                        | 变量名 |
| --------------------------- | ------ |
| QJsonParseError::ParseError | error  |
| int                         | offset |

## 详细说明

另外参阅 [JSON Support in Qt](https://doc.qt.io/qt-5/json.html) 和 [JSON Save Game Example](https://doc.qt.io/qt-5/qtcore-serialization-savegame-example.html)。

## 成员类型文档

### enum QJsonParseError::ParseError

该枚举描述了在解析JSON文档期间发生的错误类型。

| 不变量                                 | 值   | 描述                                       |
| -------------------------------------- | ---- | ------------------------------------------ |
| QJsonParseError::NoError               | 0    | 没有发生错误                               |
| QJsonParseError::UnterminatedObject    | 1    | 对象未正确使用大括号                       |
| QJsonParseError::MissingNameSeparator  | 2    | 缺少分隔不同项目的逗号                     |
| QJsonParseError::UnterminatedArray     | 3    | 数组未正确用方括号括起来                   |
| QJsonParseError::MissingValueSeparator | 4    | 缺少将键与对象内的值分隔开的冒号           |
| QJsonParseError::IllegalValue          | 5    | 该值是非法的                               |
| QJsonParseError::TerminationByNumber   | 6    | 输入流在解析数字时结束                     |
| QJsonParseError::IllegalNumber         | 7    | 数字格式不正确                             |
| QJsonParseError::IllegalEscapeSequence | 8    | 输入中发生非法的转义序列                   |
| QJsonParseError::IllegalUTF8String     | 9    | 输入中出现非法的UTF8序列                   |
| QJsonParseError::UnterminatedString    | 10   | 字符串未以引号终止                         |
| QJsonParseError::MissingObject         | 11   | 预期有对象，但找不到                       |
| QJsonParseError::DeepNesting           | 12   | JSON文档的嵌套太深，解析器无法对其进行解析 |
| QJsonParseError::DocumentTooLarge      | 13   | JSON文档太大，解析器无法解析它             |
| QJsonParseError::GarbageAtEnd          | 14   | 解析的文档末尾包含其他垃圾字符             |

## 公有成员函数文档

### [QString](https://doc.qt.io/qt-5/qstring.html) QJsonParseError::errorString() const

返回适合于所报告的JSON解析错误的人类可读消息。

**另请参见**[error](https://doc.qt.io/qt-5/qjsonparseerror.html#error-var)。

## 成员变量文档

### [QJsonParseError::ParseError](https://doc.qt.io/qt-5/qjsonparseerror.html#ParseError-enum) QJsonParseError::error

包含解析错误的类型。如果文档被正确解析，则等于[QJsonParseError :: NoError](https://doc.qt.io/qt-5/qjsonparseerror.html#ParseError-enum)。

**另外参阅** [ParseError](https://doc.qt.io/qt-5/qjsonparseerror.html#ParseError-enum) 和 [errorString](https://doc.qt.io/qt-5/qjsonparseerror.html#errorString)()。

### int QJsonParseError::offset

包含发生解析错误的输入字符串中的偏移量。

**另外参阅** [error](https://doc.qt.io/qt-5/qjsonparseerror.html#error-var) 和 [errorString](https://doc.qt.io/qt-5/qjsonparseerror.html#errorString)()。














