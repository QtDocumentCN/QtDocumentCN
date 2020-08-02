
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
|QPaintEngine::DirtyBackgroundMode	|0x0020	|The background mode is dirty and needs to be updated.|
|QPaintEngine::DirtyTransform	|0x0040	|The transform is dirty and needs to be updated.|
|QPaintEngine::DirtyClipRegion	|0x0080	|The clip region is dirty and needs to be updated.|
|QPaintEngine::DirtyClipPath	|0x0100	|The clip path is dirty and needs to be updated.|
|QPaintEngine::DirtyHints	|0x0200	|The render hints is dirty and needs to be updated.|
|QPaintEngine::DirtyCompositionMode	|0x0400	|The composition mode is dirty and needs to be updated.|
|QPaintEngine::DirtyClipEnabled	|0x0800	|Whether clipping is enabled or not is dirty and needs to be updated.|
|QPaintEngine::DirtyOpacity	|0x1000	|The constant opacity has changed and needs to be updated as part of the state change in QPaintEngine::updateState().|
|QPaintEngine::AllDirty	|0xffff	|Convenience enum used internally.|
