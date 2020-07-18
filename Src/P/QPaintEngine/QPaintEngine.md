
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

