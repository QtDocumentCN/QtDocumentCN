Reserved by kongdehui until 2022-07-31.

# QOpenGLShaderProgram 类

QOpenGLShaderProgram类允许链接和使用OpenGL着色器程序。 [More...](https://doc.qt.io/qt-6/qopenglshaderprogram.html#details)

| 头文件: | #include <QOpenGLShaderProgram>                              |
| ------- | ------------------------------------------------------------ |
| CMake:  | find_package(Qt6 REQUIRED COMPONENTS OpenGL) target_link_libraries(mytarget PRIVATE Qt6::OpenGL) |
| qmake:  | QT += opengl                                                 |
| 自从:   | Qt 5.0                                                       |
| 继承:   | [QObject](https://doc.qt.io/qt-6/qobject.html)               |

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qopenglshaderprogram-members.html)

## 公共职能

|                        | **[QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html#QOpenGLShaderProgram)**(QObject **parent* = nullptr) |
| ---------------------- | ------------------------------------------------------------ |
| virtual                | **[~QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html#dtor.QOpenGLShaderProgram)**() |
| bool                   | **[addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode)**(QOpenGLShader::ShaderType *type*, const char **source*) |
| bool                   | **[addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode-1)**(QOpenGLShader::ShaderType *type*, const QByteArray &*source*) |
| bool                   | **[addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode-2)**(QOpenGLShader::ShaderType *type*, const QString &*source*) |
| bool                   | **[addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)**(QOpenGLShader::ShaderType *type*, const QString &*fileName*) |
| bool                   | **[addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)**(QOpenGLShader **shader*) |
| bool                   | **[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)**(QOpenGLShader::ShaderType *type*, const char **source*) |
| bool                   | **[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode-1)**(QOpenGLShader::ShaderType *type*, const QByteArray &*source*) |
| bool                   | **[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode-2)**(QOpenGLShader::ShaderType *type*, const QString &*source*) |
| bool                   | **[addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)**(QOpenGLShader::ShaderType *type*, const QString &*fileName*) |
| int                    | **[attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)**(const char **name*) const |
| int                    | **[attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation-1)**(const QByteArray &*name*) const |
| int                    | **[attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation-2)**(const QString &*name*) const |
| bool                   | **[bind](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bind)**() |
| void                   | **[bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation)**(const char **name*, int *location*) |
| void                   | **[bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation-1)**(const QByteArray &*name*, int *location*) |
| void                   | **[bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation-2)**(const QString &*name*, int *location*) |
| bool                   | **[create](https://doc.qt.io/qt-6/qopenglshaderprogram.html#create)**() |
| QList<float>           | **[defaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultInnerTessellationLevels)**() const |
| QList<float>           | **[defaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultOuterTessellationLevels)**() const |
| void                   | **[disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)**(int *location*) |
| void                   | **[disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray-1)**(const char **name*) |
| void                   | **[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)**(int *location*) |
| void                   | **[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray-1)**(const char **name*) |
| bool                   | **[isLinked](https://doc.qt.io/qt-6/qopenglshaderprogram.html#isLinked)**() const |
| virtual bool           | **[link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)**() |
| QString                | **[log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)**() const |
| int                    | **[maxGeometryOutputVertices](https://doc.qt.io/qt-6/qopenglshaderprogram.html#maxGeometryOutputVertices)**() const |
| int                    | **[patchVertexCount](https://doc.qt.io/qt-6/qopenglshaderprogram.html#patchVertexCount)**() const |
| GLuint                 | **[programId](https://doc.qt.io/qt-6/qopenglshaderprogram.html#programId)**() const |
| void                   | **[release](https://doc.qt.io/qt-6/qopenglshaderprogram.html#release)**() |
| void                   | **[removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)**() |
| void                   | **[removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)**(QOpenGLShader **shader*) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)**(int *location*, const GLfloat **values*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-1)**(int *location*, const QVector2D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-2)**(int *location*, const QVector3D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-3)**(int *location*, const QVector4D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-4)**(int *location*, GLenum *type*, const void **values*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-5)**(const char **name*, const GLfloat **values*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-6)**(const char **name*, const QVector2D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-7)**(const char **name*, const QVector3D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-8)**(const char **name*, const QVector4D **values*, int *stride* = 0) |
| void                   | **[setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray-9)**(const char **name*, GLenum *type*, const void **values*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer)**(int *location*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer-1)**(const char **name*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* = 0) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)**(int *location*, GLfloat *value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-1)**(int *location*, GLfloat *x*, GLfloat *y*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-2)**(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-3)**(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-4)**(int *location*, const QVector2D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-5)**(int *location*, const QVector3D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-6)**(int *location*, const QVector4D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-7)**(int *location*, const QColor &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-8)**(int *location*, const GLfloat **values*, int *columns*, int *rows*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-9)**(const char **name*, GLfloat *value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-10)**(const char **name*, GLfloat *x*, GLfloat *y*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-11)**(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-12)**(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-13)**(const char **name*, const QVector2D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-14)**(const char **name*, const QVector3D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-15)**(const char **name*, const QVector4D &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-16)**(const char **name*, const QColor &*value*) |
| void                   | **[setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue-17)**(const char **name*, const GLfloat **values*, int *columns*, int *rows*) |
| void                   | **[setDefaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultInnerTessellationLevels)**(const QList<float> &*levels*) |
| void                   | **[setDefaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultOuterTessellationLevels)**(const QList<float> &*levels*) |
| void                   | **[setPatchVertexCount](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setPatchVertexCount)**(int *count*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)**(int *location*, GLfloat *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-1)**(int *location*, GLint *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-36)**(const char **name*, const QColor &*color*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-37)**(const char **name*, const QPoint &*point*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-38)**(const char **name*, const QPointF &*point*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-39)**(const char **name*, const QSize &*size*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-40)**(const char **name*, const QSizeF &*size*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-41)**(const char **name*, const QMatrix2x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-42)**(const char **name*, const QMatrix2x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-43)**(const char **name*, const QMatrix2x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-44)**(const char **name*, const QMatrix3x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-45)**(const char **name*, const QMatrix3x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-46)**(const char **name*, const QMatrix3x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-47)**(const char **name*, const QMatrix4x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-48)**(const char **name*, const QMatrix4x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-49)**(const char **name*, const QMatrix4x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-50)**(const char **name*, const GLfloat [2][2] *value* = 2) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-51)**(const char **name*, const GLfloat [3][3] *value* = 3) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-52)**(const char **name*, const GLfloat [4][4] *value* = 4) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-53)**(const char **name*, const QTransform &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-2)**(int *location*, GLuint *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-3)**(int *location*, GLfloat *x*, GLfloat *y*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-4)**(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-5)**(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-6)**(int *location*, const QVector2D &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-7)**(int *location*, const QVector3D &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-8)**(int *location*, const QVector4D &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-9)**(int *location*, const QColor &*color*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-10)**(int *location*, const QPoint &*point*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-11)**(int *location*, const QPointF &*point*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-12)**(int *location*, const QSize &*size*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-13)**(int *location*, const QSizeF &*size*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-14)**(int *location*, const QMatrix2x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-15)**(int *location*, const QMatrix2x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-16)**(int *location*, const QMatrix2x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-17)**(int *location*, const QMatrix3x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-18)**(int *location*, const QMatrix3x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-19)**(int *location*, const QMatrix3x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-20)**(int *location*, const QMatrix4x2 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-21)**(int *location*, const QMatrix4x3 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-22)**(int *location*, const QMatrix4x4 &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-23)**(int *location*, const GLfloat [2][2] *value* = 2) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-24)**(int *location*, const GLfloat [3][3] *value* = 3) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-25)**(int *location*, const GLfloat [4][4] *value* = 4) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-26)**(int *location*, const QTransform &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-27)**(const char **name*, GLfloat *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-28)**(const char **name*, GLint *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-29)**(const char **name*, GLuint *value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-30)**(const char **name*, GLfloat *x*, GLfloat *y*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-31)**(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-32)**(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-33)**(const char **name*, const QVector2D &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-34)**(const char **name*, const QVector3D &*value*) |
| void                   | **[setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue-35)**(const char **name*, const QVector4D &*value*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray)**(int *location*, const GLfloat **values*, int *count*, int *tupleSize*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-1)**(int *location*, const GLint **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-2)**(int *location*, const GLuint **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-3)**(int *location*, const QVector2D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-4)**(int *location*, const QVector3D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-5)**(int *location*, const QVector4D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-6)**(int *location*, const QMatrix2x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-7)**(int *location*, const QMatrix2x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-8)**(int *location*, const QMatrix2x4 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-9)**(int *location*, const QMatrix3x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-10)**(int *location*, const QMatrix3x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-11)**(int *location*, const QMatrix3x4 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-12)**(int *location*, const QMatrix4x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-13)**(int *location*, const QMatrix4x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-14)**(int *location*, const QMatrix4x4 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-15)**(const char **name*, const GLfloat **values*, int *count*, int *tupleSize*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-16)**(const char **name*, const GLint **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-17)**(const char **name*, const GLuint **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-18)**(const char **name*, const QVector2D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-19)**(const char **name*, const QVector3D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-20)**(const char **name*, const QVector4D **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-21)**(const char **name*, const QMatrix2x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-22)**(const char **name*, const QMatrix2x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-23)**(const char **name*, const QMatrix2x4 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-24)**(const char **name*, const QMatrix3x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-25)**(const char **name*, const QMatrix3x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-26)**(const char **name*, const QMatrix3x4 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-27)**(const char **name*, const QMatrix4x2 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-28)**(const char **name*, const QMatrix4x3 **values*, int *count*) |
| void                   | **[setUniformValueArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray-29)**(const char **name*, const QMatrix4x4 **values*, int *count*) |
| QList<QOpenGLShader *> | **[shaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#shaders)**() const |
| int                    | **[uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation)**(const char **name*) const |
| int                    | **[uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation-1)**(const QByteArray &*name*) const |
| int                    | **[uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation-2)**(const QString &*name*) const |

## 静态公共成员

| bool | **[hasOpenGLShaderPrograms](https://doc.qt.io/qt-6/qopenglshaderprogram.html#hasOpenGLShaderPrograms)**(QOpenGLContext **context* = nullptr) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

## 详细介绍

### 介绍

此类支持以OpenGL着色语言（GLSL）和OpenGL/ES着色语言（OpenGL/ES）编写的着色器程序。

[QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 和QOpenGLShaderProgram 使程序员免于编译和链接顶点和片段着色器的细节。

下面的示例使用提供的源代码创建一个顶点着色器程序。一旦编译和链接，着色器程序通过[QOpenGLShaderProgram::bind](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bind)()在当前 [QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html) 中被激活：

```
QOpenGLShader shader(QOpenGLShader::Vertex);
shader.compileSourceCode(code);

QOpenGLShaderProgram program(context);
program.addShader(&shader);
program.link();

program.bind();
```

### 编写便携式着色器

由于对标准顶点属性和统一变量的支持程度不同，着色器程序可能难以在OpenGL实现中重用。特别是，GLSL/ES缺少桌面OpenGL系统中存在的所有标准变量：gl_Vertex, gl_Normal, gl_Color等。桌面OpenGL缺少变量限定符highp,mediump,lowp。

QOpenGLShaderProgram 类通过在桌面OpenGL上为所有着色器程序添加以下行前缀，使编写可移植着色器的过程更容易:

```
#define highp
#define mediump
#define lowp
```

这使得在桌面系统上运行大多数 GLSL/ES 着色器程序成为可能。程序员应该限制自己只使用GLSL/ES中存在的功能，并避免只在桌面上工作的标准变量名。

### 简单着色器示例

```
program.addShaderFromSourceCode(QOpenGLShader::Vertex,
    "attribute highp vec4 vertex;\n"
    "uniform highp mat4 matrix;\n"
    "void main(void)\n"
    "{\n"
    "   gl_Position = matrix * vertex;\n"
    "}");
program.addShaderFromSourceCode(QOpenGLShader::Fragment,
    "uniform mediump vec4 color;\n"
    "void main(void)\n"
    "{\n"
    "   gl_FragColor = color;\n"
    "}");
program.link();
program.bind();

int vertexLocation = program.attributeLocation("vertex");
int matrixLocation = program.uniformLocation("matrix");
int colorLocation = program.uniformLocation("color");
```

激活上述着色器程序后，我们可以绘制一个绿色三角形，如下所示:

```
static GLfloat const triangleVertices[] = {
    60.0f,  10.0f,  0.0f,
    110.0f, 110.0f, 0.0f,
    10.0f,  110.0f, 0.0f
};

QColor color(0, 255, 0, 255);

QMatrix4x4 pmvMatrix;
pmvMatrix.ortho(rect());

program.enableAttributeArray(vertexLocation);
program.setAttributeArray(vertexLocation, triangleVertices, 3);
program.setUniformValue(matrixLocation, pmvMatrix);
program.setUniformValue(colorLocation, color);

glDrawArrays(GL_TRIANGLES, 0, 3);

program.disableAttributeArray(vertexLocation);
```

### 二进制着色器和程序

可以使用来自[QOpenGLShader::shaderId](https://doc.qt.io/qt-6/qopenglshader.html#shaderId)() glShaderBinary() 的返回值指定二进制着色器。然后可以使用 [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 将包含二进制文件的[QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html)  实例添加到着色器程序中，并使用 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)()以通常的方式链接。



可以使用 [programId](https://doc.qt.io/qt-6/qopenglshaderprogram.html#programId)() glProgramBinaryOES()的返回值指定二进制程序。然后应用程序应该调用 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 它会注意到程序已经被指定和链接，允许对着色器程序执行其他操作。着色器程序的id可以使用 [create](https://doc.qt.io/qt-6/qopenglshaderprogram.html#create)() 函数显示创建。

#### 缓存程序二进制

从Qt5.9开始，内置了对在磁盘上缓存程序二进制文件的支持。要启用此功能，请切换到使用 [addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode)() 和 [addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)()。 使用 OpenGL ES 3.x 上下文或支持 `GL_ARB_get_program_binary`, 这将透明地缓存  [QSt和ardPaths::GenericCacheLocation](https://doc.qt.io/qt-6/qst和ardpaths.html#St和ardLocation-enum) 或 [QSt和ardPaths::CacheLocation](https://doc.qt.io/qt-6/qst和ardpaths.html#St和ardLocation-enum)下的程序二进制文件。当支持不可用时，调用可缓存的函数变体等同于正常的变体。

**注意:** 一些驱动程序没有任何可用的二进制格式，即使它们宣传扩展或提供OpenGL ES 3.0。在这种情况下，程序二进制支持将被禁用。

**另请参见** [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html).

## 成员函数文档

### QOpenGLShaderProgram::QOpenGLShaderProgram([QObject](https://doc.qt.io/qt-6/qobject.html#QObject) **parent* = nullptr)

构造一个新的着色器程序并将其附加到parent。在调用 [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 之前，该程序无效。

着色器程序将与当前的 [QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html)相关联。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)()。

### `[virtual]`QOpenGLShaderProgram::~QOpenGLShaderProgram()

删除此着色器程序。

### `[since 5.9]`bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const char **source*)

将指定类型和源的着色器注册到此程序。与 [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)(),不同，此函数不执行编译。编译推迟到 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 并且可能根本不会发生, 因为[link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 可能会使用来自Qt的着色器磁盘缓存的程序二进制文件。这通常会导致性能显著提供高。

如果着色器已注册或在非缓存情况下成功编译，则返回true；如果有错误，则为false。可以通过[log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()检索编译错误信息。

当磁盘缓存被禁用时，例如通过 [Qt::AA_DisableShaderDiskCache](https://doc.qt.io/qt-6/qt.html#ApplicationAttribute-enum) ，或者OpenGL上下文不支持上下文二进制文件，调用该函数相当于[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)() 。

这个函数是在Qt 5.9中引入的。

**另请参见** [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)() 和 [addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)()。

### `[since 5.9]`bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) &*source*)

这是一个重载的函数。

将指定类型和源的着色器注册到此程序。与 [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)(),不同，此函数不执行编译。编译推迟到 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 并且可能根本不会发生, 因为[link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 可能会使用来自Qt的着色器磁盘缓存的程序二进制文件。这通常会导致性能显著提供高。

如果着色器已注册或在非缓存情况下成功编译，则返回true；如果有错误，则为false。可以通过[log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()检索编译错误信息。

当磁盘缓存被禁用时，例如通过 [Qt::AA_DisableShaderDiskCache](https://doc.qt.io/qt-6/qt.html#ApplicationAttribute-enum) ，或者OpenGL上下文不支持上下文二进制文件，调用该函数相当于[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)()。

这个函数是在Qt 5.9中引入的。

**另请参见** [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)() 和 [addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)()。

### `[since 5.9]`bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/qt-6/qstring.html) &*source*)

这是一个重载的函数。

将指定类型和源的着色器注册到此程序。与 [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)(),不同，此函数不执行编译。编译推迟到 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 并且可能根本不会发生, 因为[link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 可能会使用来自Qt的着色器磁盘缓存的程序二进制文件。这通常会导致性能显著提供高。

如果着色器已注册或在非缓存情况下成功编译，则返回true；如果有错误，则为false。可以通过[log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()检索编译错误信息。

当磁盘缓存被禁用时，例如通过 [Qt::AA_DisableShaderDiskCache](https://doc.qt.io/qt-6/qt.html#ApplicationAttribute-enum) ，或者OpenGL上下文不支持上下文二进制文件，调用该函数相当于[addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)()。

这个函数是在Qt 5.9中引入的。

**另请参见** [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)() 和 [addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)()。

### `[since 5.9]`bool QOpenGLShaderProgram::addCacheableShaderFromSourceFile([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/qt-6/qstring.html) &*fileName*)

将指定类型和文件名的着色器注册到此程序。与 [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)()不同， 此函数不执行编译。编译推迟到 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 并且可能根本不会发生, 因为[link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 可能会使用来自Qt的着色器磁盘缓存的程序二进制文件。这通常会导致性能显著提供高。

如果着色器已注册或在非缓存情况下成功编译，则返回true；如果有错误，则为false。可以通过[log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()检索编译错误信息。

当磁盘缓存被禁用时，例如通过 [Qt::AA_DisableShaderDiskCache](https://doc.qt.io/qt-6/qt.html#ApplicationAttribute-enum) ，或者OpenGL上下文不支持上下文二进制文件，调用该函数相当于 [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)()。

这个函数是在Qt 5.9中引入的。

**另请参见** [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)() 和[addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode)()。

### bool QOpenGLShaderProgram::addShader([QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) **shader*)

将已编译的着色器添加到此着色器程序。如果可以添加着色器，则返回true，否则返回false。

着色器对象的所有权仍属于调用者。当这个 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例被删除时，它不会被删除。这允许调用者将相同的着色器添加到多个着色器程序。

**另请参见** [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)(), [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)(), [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)(), [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 和 [removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)()。

### bool QOpenGLShaderProgram::addShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const char **source*)

将源代码编译为指定类型的着色器并将其添加到此着色器程序中。true如果编译成功则返回，否则返回false。编译错误和警告将通过 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)() 提供。

此函数旨在成为快速将顶点和片段着色器添加到着色器程序的快捷方式，而无需先创建 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 的实例。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)(), [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)(), [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)(), [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)(), 和[removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)()。

### bool QOpenGLShaderProgram::addShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) &*source*)

这是一个重载的方法。

将源代码编译为指定类型的着色器并将其添加到此着色器程序中。true如果编译成功则返回，否则返回false。编译错误和警告将通过 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)() 提供。

此函数旨在成为快速将顶点和片段着色器添加到着色器程序的快捷方式，而无需先创建 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 的实例。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)(), [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)(), [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)(), [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)(), 和 [removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)()。

### bool QOpenGLShaderProgram::addShaderFromSourceCode([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/qt-6/qstring.html) &*source*)

这是一个重载的方法。

将源代码编译为指定类型的着色器并将其添加到此着色器程序中。true如果编译成功则返回，否则返回false。编译错误和警告将通过 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)() 提供。

此函数旨在成为快速将顶点和片段着色器添加到着色器程序的快捷方式，而无需先创建 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 的实例。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)(), [addShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile)(), [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)(), [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)(), 和[removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)()。

### bool QOpenGLShaderProgram::addShaderFromSourceFile([QOpenGLShader::ShaderType](https://doc.qt.io/qt-6/qopenglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/qt-6/qstring.html) &*fileName*)

将fileName的内容编译为指定类型的着色器，并将其添加到此着色器程序中。true如果编译成功则返回，否则返回false。编译错误和警告将通过 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)() 提供。

此函数旨在成为快速将顶点和片段着色器添加到着色器程序的快捷方式，而无需先创建 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 的实例。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 和 [addShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode)()。

### int QOpenGLShaderProgram::attributeLocation(const char **name*) const

返回此着色器程序的参数列表中属性名称的位置。如果name不是此着色器程序的有效属性，则返回-1。

**另请参见** [uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation)() 和 [bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation)()。

### int QOpenGLShaderProgram::attributeLocation(const [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) &*name*) const

这是一个重载方法。

返回此着色器程序的参数列表中属性名称的位置。如果name不是此着色器程序的有效属性，则返回-1。

**另请参见** [uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation)() 和 [bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation)()。

### int QOpenGLShaderProgram::attributeLocation(const [QString](https://doc.qt.io/qt-6/qstring.html) &*name*) const

这是一个重载方法。

返回此着色器程序的参数列表中属性名称的位置。如果name不是此着色器程序的有效属性，则返回-1。

**另请参见** [uniformLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation)() 和 [bindAttributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation)()。

### bool QOpenGLShaderProgram::bind()

将此着色器程序绑定到活动的 [QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html) 并使其成为当前着色器程序。任何先前绑定的着色器程序都会被释放。这相当于调用 `glUseProgram()` 在 [programId](https://doc.qt.io/qt-6/qopenglshaderprogram.html#programId)()上。如果程序绑定成功，则返回true，否在返回false。如果shader程序还没有被链接，或者需要重新链接，这个函数会调用 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)()。

**另请参见** [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 和 [release](https://doc.qt.io/qt-6/qopenglshaderprogram.html#release)()。

### void QOpenGLShaderProgram::bindAttributeLocation(const char **name*, int *location*)

将属性名称绑定到指定位置。该函数可以在程序链接之前或之后调用。链接程序时未明确绑定的任何属性都将自动分配位置。

在程序链接后调用此函数时，需要重新链接程序才能使更改生效。

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。

### void QOpenGLShaderProgram::bindAttributeLocation(const [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) &*name*, int *location*)

这是一个重载方法。

将属性名称绑定到指定位置。该函数可以在程序链接之前或之后调用。链接程序时未明确绑定的任何属性都将自动分配位置。

在程序链接后调用此函数时，需要重新链接程序才能使更改生效。

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。

### void QOpenGLShaderProgram::bindAttributeLocation(const [QString](https://doc.qt.io/qt-6/qstring.html) &*name*, int *location*)

这是一个重载方法。

将属性名称绑定到指定位置。该函数可以在程序链接之前或之后调用。链接程序时未明确绑定的任何属性都将自动分配位置。

在程序链接后调用此函数时，需要重新链接程序才能使更改生效。

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。

### `[since 5.3]`bool QOpenGLShaderProgram::create()

请求立即创建着色器程序的id。成功则返回true，否则返回false。

该函数主要用于将 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 与直接在着色器程序id上操作的其它OpenGL函数相结合, 例如 `GL_OES_get_program_binary`。

正常使用shader程序时，会按需创建shader程序的id。

这个函数是在 Qt 5.3中引入的。

**另请参见** [programId](https://doc.qt.io/qt-6/qopenglshaderprogram.html#programId)()。

### [QList](https://doc.qt.io/qt-6/qlist.html)<float> QOpenGLShaderProgram::defaultInnerTessellationLevels() const

如果曲面细分控制着色器不输出它们，则返回要由曲面细分图元生成器使用的默认内部曲面细分级别。有关OpenGL和Tessellation着色器的更多详细信息，请参阅 [OpenGL Tessellation Shaders](http://www.opengl.org/wiki/Tessellation_Shader)。

返回描述内部细分级别的浮点 [QList](https://doc.qt.io/qt-6/qlist.html) . 向量将始终具有两个元素，但并非所有元素都对每种镶嵌模式都有意义。

**注意：** 这将返回全局OpenGL状态值。它不是特定于这个[QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。

**注意：** 此函数仅在 OpenGL >= 4.0 中受支持，并且在 OpenGL ES 3.2中不会返回有效结果。

**另请参见** [setDefaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultInnerTessellationLevels)() 和 [defaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultOuterTessellationLevels)()。

### [QList](https://doc.qt.io/qt-6/qlist.html)<float> QOpenGLShaderProgram::defaultOuterTessellationLevels() const

在曲面细分控制着色器不输出它们的情况下，返回由曲面细分图元生成器使用的默认外部曲面细分级别。有关OpenGL和Tessellation着色器的更多详细信息，请参阅 [OpenGL Tessellation Shaders](http://www.opengl.org/wiki/Tessellation_Shader)。

返回描述外部细分级别的浮点 [QList](https://doc.qt.io/qt-6/qlist.html) . 向量将始终具有四个元素，但并非所有元素都对每种镶嵌模式都有意义。

**注意：** 这将返回全局OpenGL状态值。它不是特定于这个[QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。

**注意：** 此函数仅在 OpenGL >= 4.0 中受支持，并且在 OpenGL ES 3.2中不会返回有效结果。

**另请参见** [setDefaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultOuterTessellationLevels)() 和 [defaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultInnerTessellationLevels)()。

### void QOpenGLShaderProgram::disableAttributeArray(int *location*)

在该着色器程序中的位置禁用顶点数组，该位置由先前调用 [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)()启用。

**另请参见** [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)(), [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), 和 [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::disableAttributeArray(const char **name*)

这是一个重载方法。

禁用此着色器程序中名为name的顶点数组，该顶点数组由先前调用 [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)()启用。

**另请参见** [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)(), [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), 和 [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::enableAttributeArray(int *location*)

在此着色器程序中启用位于位置的顶点数组，以便着色器程序使用由 [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)() 在位置上设置的值。

**另请参见** [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)(), [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)(), [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), 和 [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::enableAttributeArray(const char **name*)

这是一个重载方法。

在此着色器程序中启用名为name的顶点数组，以便着色器程序使用由 [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)() 对name设置的值。

**另请参见** [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)(), [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)(), [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), 和 [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### `[static]`bool QOpenGLShaderProgram::hasOpenGLShaderPrograms([QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html) **context* = nullptr)

返回true 表示此系统支持以OpenGL着色语言 (GLSL)编写的着色器程序；否则为假。

上下文用于解析GLSL扩展。 如果 *context* 是`nullptr`, 则使用[QOpenGLContext::currentContext](https://doc.qt.io/qt-6/qopenglcontext.html#currentContext)() 。

### bool QOpenGLShaderProgram::isLinked() const

如果此着色器程序已链接，返回true；否则返回false。

**另请参见** [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)()。

### `[virtual]`bool QOpenGLShaderProgram::link()

使用 [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)()将添加到此程序的着色器链接在一起。如果链接成功则返回true，否则返回false。如果链接失败，可以使用 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()检索错误消息。

子类可以覆盖此函数以初始化属性和统一变量以用于特定着色器程序。

如果着色器程序已经链接，再次调用此函数将强制它重新连接。

当通过 [addCacheableShaderFromSourceCode](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceCode)() 或 [addCacheableShaderFromSourceFile](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addCacheableShaderFromSourceFile)()将着色器添加到该程序时，程序二进制文件是受支持的，并且缓存的二进制文件在磁盘上可用，实际编译和链接将被跳过。相反，link() 将通过 glProgramBinary()使用二进制blob初始化程序。如果程序没有缓存版本或者它是使用不同的驱动程序版本生成的，着色器将从源代码编译，程序将正常链接。这允许无缝升级图形驱动程序，而不必担心可能不兼容的二进制格式。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 和 [log](https://doc.qt.io/qt-6/qopenglshaderprogram.html#log)()。

### [QString](https://doc.qt.io/qt-6/qstring.html) QOpenGLShaderProgram::log() const

返回最后一个 [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)() 或 [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 期间发生的错误和警告，并带有明确指定的源代码。

**另请参见** [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)()。

### int QOpenGLShaderProgram::maxGeometryOutputVertices() const

返回几何着色器可以输出多少顶点的硬件限制。

### int QOpenGLShaderProgram::patchVertexCount() const

返回渲染时要使用的每个补丁的顶点数。

**注意：** 这将返回全局OpenGL状态值。它不是特定于这个 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。

**另请参见** [setPatchVertexCount](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setPatchVertexCount)()。

### GLuint QOpenGLShaderProgram::programId() const

返回与此着色器程序关联的OpenGL标识符。

**另请参见** [QOpenGLShader::shaderId](https://doc.qt.io/qt-6/qopenglshader.html#shaderId)()。

### void QOpenGLShaderProgram::release()

从当前 [QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html) 释放活动着色器程序。这相当于调用 `glUseProgram(0)`.

**另请参见** [bind](https://doc.qt.io/qt-6/qopenglshaderprogram.html#bind)()。

### void QOpenGLShaderProgram::removeAllShaders()

删除之前添加到此程序的所有着色器。如果着色器的 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 对象是在外部构建的，它们将不会被删除。由 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 内部构造的 [QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) 对象将被删除。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 和 [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)()。

### void QOpenGLShaderProgram::removeShader([QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) **shader*)

从此着色器程序中删除着色器。对象未被删除。

着色器程序必须在当前 [QOpenGLContext](https://doc.qt.io/qt-6/qopenglcontext.html)中有效。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)(), [link](https://doc.qt.io/qt-6/qopenglshaderprogram.html#link)(), 和 [removeAllShaders](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders)()。

### void QOpenGLShaderProgram::setAttributeArray(int *location*, const GLfloat **values*, int *tupleSize*, int *stride* = 0)

在此着色器程序中的 *location* 处设置属性的顶点值数组。 *tupleSize* 表示每个顶点的组件数(1, 2, 3, or 4),  *stride* 表示顶点之间的字节数。默认的 *stride*值为零表示顶点密集地打包在values中。

当在 *location*上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)()时，该数组将变为活动状态。否则将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*location*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(int *location*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) **values*, int *stride* = 0)

在此着色器程序中的 *location* 上设置属性的二维顶点值数组。 *stride* 表示顶点之间的字节数。默认的 *stride* 值为零表示顶点密集地打包在 *values* 中。

当在 *location* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*location*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(int *location*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) **values*, int *stride* = 0)

在此着色器程序中的 *location* 上设置属性的三维顶点值数组。 *stride* 表示顶点之间的字节数。默认的 *stride* 值为零表示顶点密集地打包在 *values* 中。

当在 *location* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*location*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(int *location*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) **values*, int *stride* = 0)

在此着色器程序中的 *location* 上设置属性的四维顶点值数组。 *stride* 表示顶点之间的字节数。默认的 *stride* 值为零表示顶点密集地打包在 *values* 中。

当在 *location* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*location*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(int *location*, GLenum *type*, const void **values*, int *tupleSize*, int *stride* = 0)

在此程序的 *location* 设置属性的顶点值数组.  *stride* 表示顶点之间的字节数。默认的*stride* 值为0表示顶点密集地打包在*values*中。

*type* 表示*values* 数组中元素的类型，, 通常是 `GL_FLOAT`, `GL_UNSIGNED_BYTE` 等.  *tupleSize* 表示每个顶点的组件数: 1, 2, 3, 或 4.

当在 *location* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*location*设置指定的值。

[setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer)() 函数可用于将属性数据设置为顶点缓冲区内的偏移量。

**注意：** 将启用标准化。如果不需要，请直接通过 [QOpenGLFunctions](https://doc.qt.io/qt-6/qopenglfunctions.html)  掉用glVertexAttribPointer。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)(), 和 [setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer)()。

### void QOpenGLShaderProgram::setAttributeArray(const char **name*, const GLfloat **values*, int *tupleSize*, int *stride* = 0)

这是一个重载方法。

在此着色器程序中设置名为 *name*的属性的顶点值数组 。 *tupleSize* 表示每个顶点的组件数 (1, 2, 3, 或 4),  *stride* 表示顶点之间的字节数。 默认的 *stride* 值为0表示顶点密集地打包在*values*中。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 为*name*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(const char **name*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) **values*, int *stride* = 0)

这是一个重载方法。

在此程序中设置名为*name*的属性的二维顶点值数组。  *stride* 表示顶点之间的字节数。默认的*stride* 值为0表示顶点密集地打包在*values*中。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 为*name*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(const char **name*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) **values*, int *stride* = 0)

这是一个重载方法。

在此程序中设置名为*name*的属性的三维顶点值数组。  *stride* 表示顶点之间的字节数。默认的*stride* 值为0表示顶点密集地打包在*values*中。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 为*name*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(const char **name*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) **values*, int *stride* = 0)

这是一个重载方法。

在此程序中设置名为*name*的属性的四维顶点值数组。  *stride* 表示顶点之间的字节数。默认的*stride* 值为0表示顶点密集地打包在*values*中。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 为*name*设置指定的值。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), 和 [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeArray(const char **name*, GLenum *type*, const void **values*, int *tupleSize*, int *stride* = 0)

这是一个重载方法。

在此着色器程序中设置名为 *name* 的属性的顶点值数组.  *stride* 表示顶点之间的字节数。默认的*stride* 值为0表示顶点密集地打包在*values*中。

*type* 表示*values* 数组中元素的类型，, 通常是 `GL_FLOAT`, `GL_UNSIGNED_BYTE` 等.  *tupleSize* 表示每个顶点的组件数: 1, 2, 3, 或 4。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时. 该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*name*设置指定的值。

[setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer)() 函数可用于将属性数据设置为顶点缓冲区内的偏移量。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)(), [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)(), [enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)(), [disableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray)(), 和 [setAttributeBuffer](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer)()。

### void QOpenGLShaderProgram::setAttributeBuffer(int *location*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* = 0)

在此着色器程序中的 *location* 处设置属性的顶点值数组。从当前绑定的顶点缓冲区中的特定 *offset* 开始。 *stride* 表示顶点之间的字节数。默认的 *stride* 为0表示顶点密集地打包在值数组中。

 *type* 表示顶点值数组中元素的类型，通常是 `GL_FLOAT`, `GL_UNSIGNED_BYTE`, 等。  *tupleSize* 表示每个顶点的组件数: 1、2、3、或 4。

当在 *location* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时，该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*name*设置指定的值。

**注意：** 将启用标准化。如果不需要，请直接通过  [QOpenGLFunctions](https://doc.qt.io/qt-6/qopenglfunctions.html) 调用glVertexAttribPointer 。

**另请参见** [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeBuffer(const char **name*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* = 0)

这是一个重载方法。

在此着色器程序中设置名为*name* 的属性的顶点值数组。从当前绑定的顶点缓冲区中的特定 *offset* 开始。 *stride* 表示顶点之间的字节数。默认的 *stride* 为0表示顶点密集地打包在值数组中。

 *type* 表示顶点值数组中元素的类型，通常是 `GL_FLOAT`, `GL_UNSIGNED_BYTE`, 等。  *tupleSize* 表示每个顶点的组件数: 1、2、3、或 4。

当在 *name* 上调用[enableAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray)() 时，该数组将变为活动状态。否则，将使用 [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)() 给*name*设置指定的值。

**另请参见** [setAttributeArray](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, GLfloat *value*)

将当前上下文中的 *location* 的属性设置为 *value* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*)

将当前上下文中的 *location* 的属性设置为 2D 向量(*x*, *y*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

将当前上下文中的 *location* 的属性设置为 3D 向量 (*x*, *y*, *z*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

将当前上下文中的 *location* 的属性设置为 4D 向量 (*x*, *y*, *z*, *w*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) &*value*)

Sets the attribute at *location* in the current context to *value*.

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) &*value*)

将当前上下文中的 *location* 的属性设置为 *value* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) &*value*)

将当前上下文中的 *location* 的属性设置为 *value* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, const [QColor](https://doc.qt.io/qt-6/qcolor.html) &*value*)

将当前上下文中的 *location* 的属性设置为 *value* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(int *location*, const GLfloat **values*, int *columns*, int *rows*)

将当前上下文中*location*的属性设置为 *values* 的内容，其中包含 *columns* 元素，每个元素由 *rows* 元素组成。行值应为1、2、3或4。此函数通常用于设置矩阵值和列向量。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, GLfloat *value*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, GLfloat *x*, GLfloat *y*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为2D 向量 (*x*, *y*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为3D 向量 (*x*, *y*, *z*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为4D 向量 (*x*, *y*, *z*, *w*)。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, const [QColor](https://doc.qt.io/qt-6/qcolor.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setAttributeValue(const char **name*, const GLfloat **values*, int *columns*, int *rows*)

这是一个重载方法。

将当前上下文中名为 *name* 的属性设置为 *values* 的内容，其中包含 *columns* 元素，每个元素由 *rows* 元素组成。行值应为1、2、3或4。此函数通常用于设置矩阵值和列向量。

**另请参见** [setUniformValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue)()。

### void QOpenGLShaderProgram::setDefaultInnerTessellationLevels(const [QList](https://doc.qt.io/qt-6/qlist.html)<float> &*levels*)

设置在曲面细分控制着色器未将其输出到 *levels* 时由曲面细分图元生成器使用的默认外部曲面细分级别。有关 OpenG 和 Tessellation 着色器的更多详细信息，请参阅 [OpenGL Tessellation Shaders](http://www.opengl.org/wiki/Tessellation_Shader).

 *levels* 参数应该是一个由2个浮点数组成的 [QList](https://doc.qt.io/qt-6/qlist.html) 。并非所有值对所有细分模式都有意义。如果您指定的向量少于2个元素，则其余元素将被赋予默认值 1。

**注意：**  这会修改全局OpenGL状态，并且不特定于此 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。您应该在需要时在您的渲染函数中调用它，因为 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 不会为您应用它。这纯粹是一个遍历功能。

**注意：** 此功能仅适用于 OpenGL >= 4.0，不支持 OpenGL ES 3.2.

**另请参见** [defaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultInnerTessellationLevels)() 和 [setDefaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultOuterTessellationLevels)()。

### void QOpenGLShaderProgram::setDefaultOuterTessellationLevels(const [QList](https://doc.qt.io/qt-6/qlist.html)<float> &*levels*)

设置在曲面细分控制着色器未将其输出到 *levels* 时由曲面细分图元生成器使用的默认外部曲面细分级别。有关 OpenG 和 Tessellation 着色器的更多详细信息，请参阅 [OpenGL Tessellation Shaders](http://www.opengl.org/wiki/Tessellation_Shader).

 *levels* 参数应该是一个由4个浮点数组成的 [QList](https://doc.qt.io/qt-6/qlist.html) 。并非所有值对所有细分模式都有意义。如果您指定的向量少于4个元素，则其余元素将被赋予默认值 1。

**注意：**  这会修改全局OpenGL状态，并且不特定于此 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。您应该在需要时在您的渲染函数中调用它，因为 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 不会为您应用它。这纯粹是一个遍历功能。

**注意：** 此功能仅适用于 OpenGL >= 4.0，不支持 OpenGL ES 3.2.

**另请参见** [defaultOuterTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#defaultOuterTessellationLevels)() 和 [setDefaultInnerTessellationLevels](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setDefaultInnerTessellationLevels)()。

### void QOpenGLShaderProgram::setPatchVertexCount(int *count*)

使用此函数向 OpenGL指定要 *count* 的补丁中的定点数。补丁是自定义的OpenGL原语，其解释完全由曲面细分着色器阶段定义。 因此，仅在使用包含曲面细分阶段着色器的 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 时调用此函数才有意义。 使用 OpenGL 曲面细分时，唯一可以使用 `glDraw*()` 函数渲染的图元是 `GL_PATCHES`.

这相当于调用 glPatchParameteri(GL_PATCH_VERTICES, count).

**注意：** 这会修改全局OpenGL状态，并且不特定于此 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 实例。您应该在需要时在您的渲染函数中调用它，因为 [QOpenGLShaderProgram](https://doc.qt.io/qt-6/qopenglshaderprogram.html) 不会为您应用它。这纯粹是一个遍历功能。

**另请参见** [patchVertexCount](https://doc.qt.io/qt-6/qopenglshaderprogram.html#patchVertexCount)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLfloat *value*)

将当前上下文中 *location* 的统一变量设置为 *value*.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLint *value*)

将当前上下文中 *location* 的统一变量设置为 *value*.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QColor](https://doc.qt.io/qt-6/qcolor.html) &*color*)

这是一个重载方法。

将当前上下文中名为*name* 关联的统一变量设置为  *color* 的红色、绿色、蓝色和alpha分量。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QPoint](https://doc.qt.io/qt-6/qpoint.html) &*point*)

这是一个重载方法。

将当前上下文中名为*name* 关联的统一变量设置为 *point* 的x和y坐标。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QPointF](https://doc.qt.io/qt-6/qpointf.html) &*point*)

这是一个重载方法。

将当前上下文中名为*name* 关联的统一变量设置为 *point* 的x和y坐标。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QSize](https://doc.qt.io/qt-6/qsize.html) &*size*)

这是一个重载方法。

将当前上下文中名为*name* 关联的统一变量设置为 给定size的宽度和高度.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QSizeF](https://doc.qt.io/qt-6/qsizef.html) &*size*)

这是一个重载方法。

将当前上下文中名为*name* 关联的统一变量设置为 给定size的宽度和高度.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix2x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x2-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 2x2 矩阵 *value*.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix2x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x3-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 2x3 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat2*3的GLSL类型。相反，它将统一视为vec3的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix2x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x4-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 2x4 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat2*4的GLSL类型。相反，它将统一视为vec4的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix3x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x2-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 3x2 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat4*3的GLSL类型。相反，它将统一视为vec4的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix3x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x3-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 3x3 矩阵 *value*.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix3x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x4-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 3x4 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat4*3的GLSL类型。相反，它将统一视为vec4的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix4x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x2-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 4x2 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat4*2的GLSL类型。相反，它将统一视为vec2的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix4x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x3-typedef) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 4x3 矩阵 *value*.

**注意：** 此函数不知道非平方矩阵支持，即现代OpenGL版本中存在的类似mat4*3的GLSL类型。相反，它将统一视为vec3的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QMatrix4x4](https://doc.qt.io/qt-6/qmatrix4x4.html) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 4x4 矩阵 *value*.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const GLfloat [2][2] *value* = 2)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 2x2 矩阵 *value*. 矩阵元素必须以列优先顺序指定

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const GLfloat [3][3] *value* = 3)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 3x3 矩阵 *value*. 矩阵元素必须以列优先顺序指定

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const GLfloat [4][4] *value* = 4)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为 4x4 矩阵 *value*. 矩阵元素必须以列优先顺序指定.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QTransform](https://doc.qt.io/qt-6/qtransform.html) &*value*)

这是一个重载方法。

将当前上下文中名为*name* 的统一变量设置为指定  [QTransform](https://doc.qt.io/qt-6/qtransform.html) 值的 3x3 变换矩阵 *value* 。

要将 [QTransform](https://doc.qt.io/qt-6/qtransform.html) value 设置为着色器中的 4x4 矩阵，请使用 `setUniformValue(name, QMatrix4x4(value))`.

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLuint *value*)

将当前上下文中 *location* 的 uniform 变量设置为  *value*. 设置采样器值时应使用此功能。

**注意：** 此函数不知道现在OpenGL 版本中对 unsigned int 的支持，因此将 *value*  视为 GLint 并调用 glUniform1i.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*)

将当前上下文中 *location* 的 uniform 变量设置为 2D 向量 (*x*, *y*).

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

将当前上下文中 *location* 的 uniform 变量设置为 3D 向量 (*x*, *y*, *z*).

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

将当前上下文中 *location* 的 uniform 变量设置为 4D 向量 (*x*, *y*, *z*, *w*).

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) &*value*)

将当前上下文中 *location* 的 uniform 变量设置为*value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) &*value*)

将当前上下文中 *location* 的 uniform 变量设置为*value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) &*value*)

将当前上下文中 *location* 的 uniform 变量设置为*value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QColor](https://doc.qt.io/qt-6/qcolor.html) &*color*)

将当前上下文中的 *location* 的 uniform 变量设置为 *color*的红色、绿色、蓝色和alpha分量。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QPoint](https://doc.qt.io/qt-6/qpoint.html) &*point*)

将当前上下文中 *location* 的 uniform 变量设置为 *point*  的x和y坐标。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QPointF](https://doc.qt.io/qt-6/qpointf.html) &*point*)

将当前上下文中 *location* 的 uniform 变量设置为 *point*  的x和y坐标。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QSize](https://doc.qt.io/qt-6/qsize.html) &*size*)

将当前上下文中 *location* 的 uniform 变量设置为给定size的宽度和高度 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QSizeF](https://doc.qt.io/qt-6/qsizef.html) &*size*)

将当前上下文中 *location* 的 uniform 变量设置为给定size的宽度和高度 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x2-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为2*2矩阵 *value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x3-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为2*3矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat2x3 。相反，它将统一视为vec3的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x4-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为2*4矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat2x4 。相反，它将统一视为vec4的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x2-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为3*2矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat3x2 。相反，它将统一视为vec2的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x3-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为3*3矩阵 *value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x4-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为3*4矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat3x4 。相反，它将统一视为vec4的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x2-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为4*2矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat4x2 。相反，它将统一视为vec2的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x3-typedef) &*value*)

将当前上下文中 *location* 的统一变量设置为4*3矩阵 *value* 。

**注意：** 此函数不知道非方阵支持，即现代OpenGL版本中存在的GLSL类型，如 mat4x3。相反，它将统一视为vec3的数组。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x4](https://doc.qt.io/qt-6/qmatrix4x4.html) &*value*)

将当前上下文中 *location* 的统一变量设置为4*4矩阵 *value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const GLfloat [2][2] *value* = 2)

这是一个重载方法。

将当前上下文中 *location* 的统一变量设置为2*2矩阵 *value*. 矩阵元素必须以列优先顺序指定。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const GLfloat [3][3] *value* = 3)

这是一个重载方法。

将当前上下文中 *location* 的统一变量设置为3*3矩阵 *value*. 矩阵元素必须以列优先顺序指定。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const GLfloat [4][4] *value* = 4)

这是一个重载方法。

将当前上下文中 *location* 的统一变量设置为4*4矩阵 *value*. 矩阵元素必须以列优先顺序指定。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(int *location*, const [QTransform](https://doc.qt.io/qt-6/qtransform.html) &*value*)

将当前上下文中 *location* 的统一变量设置为指定为 [QTransform](https://doc.qt.io/qt-6/qtransform.html) 值的3*3变换矩阵值。

要将 [QTransform](https://doc.qt.io/qt-6/qtransform.html) 值设置为着色器中的 4x4 矩阵, 请使用 `setUniformValue(location, QMatrix4x4(value))`.

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLfloat *value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为 *value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLint *value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为 *value* 。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLuint *value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为 *value* 。设置采样器值时应使用此功能。

**注意：** 此函数不知道现代 OpenGL版本中对 unsigned int的支持，因此将 *values* 视为 GLint 并调用 glUniform1iv.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLfloat *x*, GLfloat *y*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为2D向量 (*x*, *y*,)。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为3D向量 (*x*, *y*, *z*,)。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为4D向量 (*x*, *y*, *z*, *w*)。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为*values*。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为*values*。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValue(const char **name*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) &*value*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量设置为*values*。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const GLfloat **values*, int *count*, int *tupleSize*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 元素。每个元素都有*tupleSize* 数组。 *tupleSize* 必须为 1, 2, 3, 或 4。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const GLint **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const GLuint **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 元素。设置采样器值数组时应使用此

**注意：** 此函数不知道现代 OpenGL版本中对 unsigned int的支持，因此将 *values* 视为 GLint 并调用 glUniform1iv.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 2D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 3D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 4D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x2-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 2*2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x3-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 2*3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x4-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 2*4 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x2-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 3*2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x3-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 3*3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x4-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 3*4 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x2-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 4*2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x3-typedef) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 4*3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x4](https://doc.qt.io/qt-6/qmatrix4x4.html) **values*, int *count*)

将当前上下文中名为 *location* 的统一变量数组设置为*values*的 *count* 4*4矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const GLfloat **values*, int *count*, int *tupleSize*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count*元素。每个元素都有*tupleSize* 组件。 *tupleSize*  必须为 1, 2, 3, 或 4.

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const GLint **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count*元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const GLuint **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count*元素。设置采样器值数组时应使用此重载。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QVector2D](https://doc.qt.io/qt-6/qvector2d.html) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count* 2D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QVector3D](https://doc.qt.io/qt-6/qvector3d.html) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count* 3D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QVector4D](https://doc.qt.io/qt-6/qvector4d.html) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的 *count* 4D向量元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix2x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x2-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 2x2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix2x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x3-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 2x3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix2x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix2x4-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 2x4 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix3x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x2-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 3x2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix3x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x3-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 3x3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix3x4](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix3x4-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 3x4 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix4x2](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x2-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 4x2 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix4x3](https://doc.qt.io/qt-6/qgenericmatrix.html#QMatrix4x3-typedef) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 4x3 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### void QOpenGLShaderProgram::setUniformValueArray(const char **name*, const [QMatrix4x4](https://doc.qt.io/qt-6/qmatrix4x4.html) **values*, int *count*)

这是一个重载方法。

将当前上下文中名为 *name* 的统一变量数组设置为*values*的*count* 4x4 矩阵元素。

**另请参见** [setAttributeValue](https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue)()。

### [QList](https://doc.qt.io/qt-6/qlist.html)<[QOpenGLShader](https://doc.qt.io/qt-6/qopenglshader.html) *> QOpenGLShaderProgram::shaders() const

返回已使用 [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)()添加到此着色器程序的所有着色器的列表。

**另请参见** [addShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader)() 和 [removeShader](https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader)()。

### int QOpenGLShaderProgram::uniformLocation(const char **name*) const

返回此着色器程序的参数列表中统一变量名称的位置。如果*name*不是此着色器程序的有效统一变量，则返回-1.

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。

### int QOpenGLShaderProgram::uniformLocation(const [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) &*name*) const

这是一个重载方法。

返回此着色器程序的参数列表中统一变量名称的位置。如果*name*不是此着色器程序的有效统一变量，则返回-1.

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。

### int QOpenGLShaderProgram::uniformLocation(const [QString](https://doc.qt.io/qt-6/qstring.html) &*name*) const

这是一个重载方法。

返回此着色器程序的参数列表中统一变量名称的位置。如果*name*不是此着色器程序的有效统一变量，则返回-1.

**另请参见** [attributeLocation](https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation)()。