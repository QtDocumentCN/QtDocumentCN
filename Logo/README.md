# Logo 设计

方形图标：
![Logo_green](Logo_green.drawio.svg)
![Logo](Logo.drawio.svg)
![Logo_green_no_question](Logo_green_no_question.drawio.svg)
![Logo_no_question](Logo_no_question.drawio.svg)

圆形图标：
![Logo_green_round](Logo_green_round.drawio.svg)


## 设计思路

基于 [Qt 官方图标](www.qt.io)，添加 `中文文档` 字样。

图标全程使用 `svg` 资源，以便在所有分辨率下都得到较好的显示效果。

使用 [Draw.io](www.draw.io) 编辑生成最终图像。

### 方形图标

参考 chm 和 Qt4 Aassistant 的图标风格，在右下角添加问号标识。

填充文字时，带问号版缩放高度至 `16pt`，无问号版缩放高度至 `20pt`。绿色字体因为边缘不明显，带问号版略微放大高度至 `17pt`。

### 圆形图标

设置 70x70pt 的圆，在适当位置放置 `Qt` 官方图标和 `中文文档` 字样，官方图标大小不变，文本缩放高度至 `19pt`。

添加 70x70pt 的外接矩形，采用相同尺寸。



## 资源来源

### Qt图标

原始图标来自 [Qt 官方网站](www.qt.io) 内嵌 `svg` 代码。

![Qt](Qt.svg)

----

### 问号字样

<img src="Question.svg" width="81" height="108.6">

问号图像使用 [FontAwesome](http://www.fontawesome.com.cn/) 字体中的 [Question 符号](http://www.fontawesome.com.cn/icons/question/)，并修改颜色为 Qt 配色，添加白色描边：

```html
<path ... fill="#41cd52" stroke-width="30" stroke="white"/>
```

----

### 中文文档字样

![中文文档_green](Text_green.svg)
![中文文档](Text.svg)

使用 [Noto Sans CJK SC Bold](https://www.google.com/get/noto/help/cjk/) 字体，即 [思源黑体](https://github.com/adobe-fonts/source-han-sans) 的粗体效果。

基于 [text-to-svg](https://github.com/shrhdk/text-to-svg) 模块，使用 `Node.js`  将文本的字形转换为 `svg` 图像：

```javascript
// 导入 text-to-svg 模块
const TextToSVG = require('text-to-svg');

// 加载字体，创建对象
const textToSVG = TextToSVG.loadSync('字体路径/NotoSansCJKsc-Bold.otf');

// 主题色填充，无描边
const attributes = {fill: '#41cd52'};

// 使用 72 磅渲染
const options = {x: 0, y: 0, fontSize: 72, anchor: 'top', attributes: attributes};

// 渲染文本，生成 svg
var fs = require("fs");
fs.writeFile("Text_green.svg", textToSVG.getSVG('中文文档', options), () => {});
```


