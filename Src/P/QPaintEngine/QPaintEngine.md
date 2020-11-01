
# QPaintEngine Class

QPaintEngine类为[QPainter](../../P/QPainter/QPainter.md)提供了如何在指定绘图设备上(译者注:一般为QPaintDevice的派生)绘制的一些抽象的方法。

|   属性 | 方法                                                         |
| -----: | :----------------------------------------------------------- |
| 头文件 | `#include <QPaintEngine>`                               |
|  qmake | `QT+=core`                                                   |

## 公共成员类型

| 类型 | 方法                                                         |
| :--: | :----------------------------------------------------------- |
| enum | DirtyFlag { DirtyPen, DirtyBrush, DirtyBrushOrigin, DirtyFont, DirtyBackground, …, AllDirty } |
| flags | DirtyFlags |
| enum | PaintEngineFeature { AlphaBlend, Antialiasing, BlendModes, BrushStroke, ConicalGradientFill, …, AllFeatures } |
| flags	| PaintEngineFeatures |
| enum | PolygonDrawMode { OddEvenMode, WindingMode, ConvexMode, PolylineMode } |
| enum | Type { X11, Windows, MacPrinter, CoreGraphics, QuickDraw, …, Direct2D } |

## 公共成员函数

| 返回类型 | 函数名                                                       |
| -------: | :----------------------------------------------------------- |
|	       |QPaintEngine(QPaintEngine::PaintEngineFeatures caps = PaintEngineFeatures())|
|   virtual |	~QPaintEngine()|
|virtual bool	| begin(QPaintDevice *pdev) = 0 |
|virtual void	|drawEllipse(const QRectF &rect)|
|virtual void	|drawEllipse(const QRect &rect)|
|virtual void	|drawImage(const QRectF &rectangle, const QImage &image, const QRectF &sr, Qt::ImageConversionFlags flags = Qt::AutoColor)|
|virtual void	|drawLines(const QLineF *lines, int lineCount)|
|virtual void	|drawLines(const QLine *lines, int lineCount)|
|virtual void	|drawPath(const QPainterPath &path)|
|virtual void	|drawPixmap(const QRectF &r, const QPixmap &pm, const QRectF &sr) = 0|
|virtual void	|drawPoints(const QPointF *points, int pointCount)|
|virtual void	|drawPoints(const QPoint *points, int pointCount)|
|virtual void	|drawPolygon(const QPointF *points, int pointCount, QPaintEngine::PolygonDrawMode mode)|
|virtual void	|drawPolygon(const QPoint *points, int pointCount, QPaintEngine::PolygonDrawMode mode)|
|virtual void	|drawRects(const QRectF *rects, int rectCount)|
|virtual void	|drawRects(const QRect *rects, int rectCount)|
|virtual void	|drawTextItem(const QPointF &p, const QTextItem &textItem)|
|virtual void	|drawTiledPixmap(const QRectF &rect, const QPixmap &pixmap, const QPointF &p)|
|virtual bool	|end() = 0|
|bool	|hasFeature(QPaintEngine::PaintEngineFeatures feature) const|
|bool	|isActive() const|
|QPaintDevice *|	paintDevice() const|
|QPainter *	|painter() const|
|void	|setActive(bool state)|
|virtual QPaintEngine::Type	|type() const = 0|
|virtual void	|updateState(const QPaintEngineState &state) = 0|

---

## 详细介绍

Qt为不同的painter后端提供了一些预设实现的QPaintEngine

> 译者注：提供一个更加好理解的说法。QPainter的Qt实现一般默认调用的是QPaintEngine的方法。

现在QPaintEngine主要提供的是Qt自带的光栅化引擎(raster engine),Qt在他所有支持的平台上，提供了一个功能完备的光栅化引擎。

在Windows, X11 和 macOS平台上，Qt自带的光栅化引擎都是QWidget这个基础类的默认的绘制方法的提供者，亦或是QImage的绘制方法的提供者。当然有一些特殊的绘制设备的绘制引擎不提供对应的绘制方法，这时候就会调用默认的光栅化引擎。

当然，我们也为OpenGL(可通过QOpenGLWidget访问)跟打印(允许QPainter在QPrinter对象上绘制，用于生成pdf之类的)也提供了对应的QPaintEngine的实现。

> 译者注： QPainter,QPainterEngine，QPaintDevice三个是相辅相成的。
> - QPainter为开发者提供外部接口方法用于绘制
> - QPaintEngine为QPainter提供一些绘制的具体实现
> - QPaintDevice为QPainter提供一个绘图设备，用于显示亦或储存。

如果你想使用QPainter绘制自定义的后端(译者注：这里可以理解为QPaintDevice)。你可以继承QPaintEngine，并实现其所有的虚函数。然后子类化QPaintDevice并且实现它的纯虚成员函数（QPaintDevice::paintEngine()）。

由QPaintDevice创建QPaintEngine，并维护其生命周期。

另请参见QPainter，QPaintDevice::paintEngine()和Paint System

--- 

# 成员类型文档

## enum QPaintEngine::DirtyFlag
## flags QPaintEngine::DirtyFlags

|枚举类型	|枚举值	|描述|
| :---: | :--------- |:---:| 
|QPaintEngine::DirtyPen	|0x0001	|画笔已经标脏，应刷新|
|QPaintEngine::DirtyBrush	|0x0002	|画刷已经标脏，应刷新|
|QPaintEngine::DirtyBrushOrigin	|0x0004	|画刷原始数据已经变化，应刷新|
|QPaintEngine::DirtyFont	|0x0008	|字体发生变化，应刷新|
|QPaintEngine::DirtyBackground	|0x0010	|背景标脏，应刷新|
|QPaintEngine::DirtyBackgroundMode	|0x0020	|背景状态标脏，应刷新|
|QPaintEngine::DirtyTransform	|0x0040	|当前矩阵标脏，应刷新|
|QPaintEngine::DirtyClipRegion	|0x0080	|当前裁剪区域标脏，应刷新|
|QPaintEngine::DirtyClipPath	|0x0100	|裁剪路径标脏，应刷新|
|QPaintEngine::DirtyHints	|0x0200	|当前绘制精度标志变化，应刷新|
|QPaintEngine::DirtyCompositionMode	|0x0400	|绘制组合模式变化，应刷新|
|QPaintEngine::DirtyClipEnabled	|0x0800	|无论是否当前可裁剪，都应刷新|
|QPaintEngine::DirtyOpacity	|0x1000	|当前透明度已经更改，应当使用QPaintEngine::updateState()来进行刷新|
|QPaintEngine::AllDirty	|0xffff	|内部枚举使用变量。|

QPaintEngine使用函数QPaintEngine::updateState()来通知QPainter的延迟刷新。

一个绘制引擎必须更新上面所有的标脏状态（译者注：比如你自定义一个QPaintEngine，就需要处理上面的所有的状态的刷新）

一个标脏枚举使用QFlags<DirtyFlag>类型。 这些类型可以异或使用的。（译者注：比如 QPaintEngine::DirtyPen | QPaintEngine::DirtyBrush   看他们枚举值就看出来了）

---

## enum QPaintEngine::PaintEngineFeature
## flags QPaintEngine::PaintEngineFeatures

|枚举类型	|枚举值	|描述|
| :---: | :--------- |:---:| 
|Constant|	Value|	Description|
|QPaintEngine::AlphaBlend|	0x00000080| 引擎可以使用透明通道|
|QPaintEngine::Antialiasing	|0x00000400	|引擎可以使用抗锯齿来改善渲染图元的外观。|
|QPaintEngine::BlendModes	|0x00008000|	引擎支持混合模式。|
|QPaintEngine::BrushStroke|	0x00000800|	引擎支持画刷描边操作，并不是仅仅是纯色（比如2倍线宽的渐变虚线）|
|QPaintEngine::ConicalGradientFill	|0x00000040	|引擎支持锥形渐变填充。|
|QPaintEngine::ConstantOpacity	|0x00001000|	该引擎支持QPainter :: setOpacity（）提供的功能。|
|QPaintEngine::LinearGradientFill	|0x00000010| 引擎支持线性渐变填充。|
|QPaintEngine::MaskedBrush	|0x00002000|	该引擎能够渲染具有带有Alpha通道或蒙版的纹理的笔刷。|
|QPaintEngine::ObjectBoundingModeGradients	|0x00010000|	该引擎对坐标模式为QGradient :: ObjectBoundingMode的渐变具有本地支持。否则，如果支持QPaintEngine :: PatternTransform，则将对象边界模式渐变转换为具有坐标模式QGradient :: LogicalMode和用于坐标映射的画笔变换的渐变。|
|QPaintEngine::PainterPaths	|0x00000200|	引擎支持路径|
|QPaintEngine::PaintOutsidePaintEvent	|0x20000000| 该引擎能够在绘制事件之外进行绘制。|
|QPaintEngine::PatternBrush	|0x00000008	| 引擎能够使用Qt::BrushStyle中指定的画笔图案渲染画笔。|
|QPaintEngine::PatternTransform	|0x00000002|	该引擎支持转换画笔图案。|
|QPaintEngine::PerspectiveTransform|	0x00004000|	该引擎支持对基元执行透视转换。|
|QPaintEngine::PixmapTransform	|0x00000004	|该引擎可以变换像素图，包括旋转和剪切。|
|QPaintEngine::PorterDuff	|0x00000100	|该引擎支持Porter-Duff操作|
|QPaintEngine::PrimitiveTransform	|0x00000001|	该引擎支持转换绘图图元。|
|QPaintEngine::RadialGradientFill	|0x00000020|	引擎支持径向渐变填充。|
|QPaintEngine::RasterOpModes	|0x00020000	|引擎支持按位栅格操作。|
|QPaintEngine::AllFeatures	|0xffffffff|	以上所有功能。此枚举值通常用作位掩码。|

PaintEngineFeatures类型是QFlags<`PaintEngineFeature`>的typedef 。它存储PaintEngineFeature值的OR组合。(也就是里面的值是可以异或的)

---

## enum QPaintEngine::PolygonDrawMode

|枚举类型	|枚举值	|描述|
| :---: | :--------- |:---:| 
|Constant|	Value|	Description|
|QPaintEngine::OddEvenMode|	0	|多边形应使用OddEven填充规则绘制|
|QPaintEngine::WindingMode|	1	|多边形应使用绕线填充规则绘制。|
|QPaintEngine::ConvexMode|	2|多边形是凸多边形，可以使用可用的专用算法进行绘制。|
|QPaintEngine::PolylineMode	|3	|仅应绘制多边形的轮廓。|

## enum QPaintEngine::Type

|枚举类型	|枚举值	|描述|
| :---: | :--------- |:---:| 
|Constant|	Value|	Description|
|QPaintEngine::X11|	0	 |  |
|QPaintEngine::Windows|	1|  |	 
|QPaintEngine::MacPrinter|	4|	 
|QPaintEngine::CoreGraphics|	3|macOS的Quartz2D（CoreGraphics）|
|QPaintEngine::QuickDraw|	2	|macOS的QuickDraw|
|QPaintEngine::QWindowSystem|	5	|嵌入式Linux的Qt|
|QPaintEngine::PostScript|	6	|（不再支持）|
|QPaintEngine::OpenGL|	7	| |
|QPaintEngine::Picture|	8|	QPicture 格式|
|QPaintEngine::SVG|	9|	可伸缩矢量图形XML格式|
|QPaintEngine::Raster|	10	 | |
|QPaintEngine::Direct3D|	11 |仅Windows，基于Direct3D的引擎|
|QPaintEngine::Pdf	|12|	PDF格式|
|QPaintEngine::OpenVG	|13	 | |
|QPaintEngine::User	|50	| 用戶自定义的最小美剧|
|QPaintEngine::MaxUser	|100	|用戶自定义的最大美剧|
|QPaintEngine::OpenGL2	|14	 | |
|QPaintEngine::PaintBuffer	|15	 | |
|QPaintEngine::Blitter	|16	 | |
|QPaintEngine::Direct2D	|17	|仅Windows，基于Direct2D的引擎|


