# QText2DEntity Class
class [Qt3DExtras](Qt3DExtras.md#)::QText2DEntity

QText2DEntity 允许在 3D 空间中创建 2D 文本。 [更多的...](QText2DEntity.md#details)

|     |   |
|  ----  | ----  |
| 头文件：    | #include <Qt3DExtras/QText2DEntity>  |
| qmake：  | QT += 3dextras |
| 实例化者：  | [Text2DEntity](Text2DEntity.md#) |
| 继承：  | [Qt3DCore::QEntity](Qt3DCore.md#) |

[所有成员的列表，包括继承的成员](../qt3dextras-qtext2dentity-members.md)

## 特性 
|     |   |
|  ----  | ----  |
| [**颜色：**](QText2DEntity.md#颜色:QColor) | QColor |
| [**字体：**](QText2DEntity.md#字体:QFont)  | QFont |
| [**高度：**](QText2DEntity.md#高度:float)  | float |
| [**文本：**](QText2DEntity.md#文本:QString)  | QString |
| [**宽度：**](QText2DEntity.md#宽度:float)  | float  |

## 公共成员方法
|     |   |
|  ----  | ----  |
| QColor  | [**color()**](QText2DEntity.md#颜色:QColor) const |
| QFont  | [**font()**](QText2DEntity.md#字体:QFont) const |
| float  | [**height()**](QText2DEntity.md#高度:float) const |
| void  | [**setColor**](QText2DEntity.md#颜色:QColor)(const QColor &color) |
| void  | [**setFont**](QText2DEntity.md#字体:QFont)(const QFont &font) |
| void  | [**setHeight**](QText2DEntity.md#高度:float)(float height) |
| void  | [**setText**](QText2DEntity.md#文本:QString)(const QString &text) |
| void  | [**setWidth**](QText2DEntity.md#宽度:float)(float width) |
| QString  | [**text()**](QText2DEntity.md#文本:QString) const |
| float  | [**width()**](QText2DEntity.md#宽度:float) const |

## 信号
|     |   |
|  ----  | ----  |
|void	|[**colorChanged**](QText2DEntity.md#颜色:QColor)(const QColor &color)	|
|void	|[**fontChanged**](QText2DEntity.md#字体:QFont)(const QFont &font)		|
|void	|[**heightChanged**](QText2DEntity.md#高度:float)(float height)		|
|void	|[**textChanged**](QText2DEntity.md#文本:QString)(const QString &text)	|
|void	|[**widthChanged**](QText2DEntity.md#宽度:float)(float width)			|

## 详细说明
QText2DEntity 将文本呈现为 XY 坐标平面中的三角形。 几何体将放置在指定宽度和高度的矩形中。 如果生成的几何图形比指定的宽度宽，则其余部分将显示在新的一行。

通过添加变换组件，可以在场景中定位实体。

QText2DEntity 将根据字形的形状和使用指定颜色的实体材料创建几何体。 

## 成员函数文档
### 颜色:[QColor](../../C/Color.md)
保存在 Qt Quick 场景中显示的文本项的颜色。

**访问功能：**

|     |   |
|  ----  | ----  |
| QColor | **color**() const					|
| void	| **setColor**(const QColor &color)	|

**通知信号：**

|     |   |
| ----  | ----  |
| void	| **colorChanged**(const QColor &color)|


### 字体:[QFont](../../F/Font.md)
保存在 Qt Quick 场景中显示的文本项的字体。

**访问功能：**

|     |   |
| ----  | ----  |
|QFont	|**font**() const|
|void	|**setFont**(const QFont &font)|

**通知信号：**

|     |   |
| ----  | ----  |
|void |**fontChanged**(const QFont &font)|


### 高度:float
返回在 Qt Quick 场景中显示的文本项的高度。

**访问功能：**

|     |   |
| ----  | ----  |
|float	|**height**() const|
|void	|**setHeight**(float height)|


**通知信号：**

|     |   |
| ----  | ----  |
|void |**heightChanged**(float height)|


### 文本:[QString](../../S/QString.md)
保存在 Qt Quick 场景中显示的文本。

**访问功能：**

|     |   |
| ----  | ----  |
|QString |**text**() const|
|void| **setText**(const QString &text)|

**通知信号：**

|     |   |
| ----  | ----  |
|void |**textChanged**(const QString &text)|

###宽度:float
返回在 Qt Quick 场景中显示的文本项的宽度。

**访问功能：**

|     |   |
| ----  | ----  |
|float|**width**() const|
|void |**setWidth**(float width)|

**通知信号：**

|     |   |
| ----  | ----  |
|void 	|**widthChanged**(float width)|
