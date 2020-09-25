# Qt 中的多线程技术

Qt 提供一系列的类与函数来处理多线程。Qt 开发者们可以使用下面四种方法来实现多线程应用。



## QThread: 低级 API 与可选的事件循环

作为 Qt 进行线程控制的基石，每一个 QThread 实例都代表并控制着一个线程。

您可以直接实例化 QThread，或建立子类。实例化一个 QThread 将附带一个并行事件循环，允许 QObject 槽函数在子线程执行。若子类化一个 QThread，程序可以在事件循环启动前初始化这个新线程；或者在无事件循环下运行并行代码。

**另请参阅**： QThread 类文档 以及示例代码 多线程范例 来了解如何使用 QThread。



## QThreadPool 与 QRunnable: 线程重用

如果频繁地创建与销毁线程，资源开销将会非常大。为了减少这样额外的开销，可以重复使用一些现成的线程来执行新的任务。QThreadPool 就是这样一个保存着可重用的 QThead 的集合。

为了将代码放入 QThreadPool 的线程中运行，可以重写 QRunnable::run() 函数并实例化继承自 QRunnable 的子类。调用 QThreadPool::start() 函数可将 QRunnable 添加到 QThreadPool 的运行队列。一旦出现了一个可用的线程，它将会执行 QRunnable::run() 里的代码。

每一个 Qt 程序都会自带一个公共线程池，可以通过调用 QThreadPool::globalInstance() 来获取。公共线程池会自动维持着一定数量的线程，线程数为基于 CPU 核心数计算的最佳值。不过，您也可以显式创建并管理一个独立的 QThreadPool 。



## Qt Concurrent: 使用高级 API 

Qt Concurrent 模块提供了数个高级函数，用于处理一些常见的并行计算模式：map、filter 和 reduce。不同于使用 QThread 与 QRunnable，这些高级函数不需要使用底层线程原语，比如互斥锁与信号量。取而代之的是返回一个 QFuture 对象，它能够在传入的函数返回值就绪后检索该结果。QFuture 既可以用来查询计算进度，也可以暂停/恢复/取消计算。方便起见，QFutureWatcher 可以让您通过信号槽与 QFuture 进行交互。

Qt Concurrent 的 map、filter 和 reduce 算法会自动将计算过程分配到可用的处理器核心，由此，当下编写的程序在以后部署到更多核心的系统上时会被自动扩展。

此模块还提供了 QtConcurrent::run() 函数，可以将任何函数在另一个线程中运行。不过，QtConcurrent::run() 仅提供 map 、 filter 和 reduce 函数的一部分功能。QFuture 可以用于检索函数返回值，也可以用于查看线程是否处于运行中。然而，调用 QtConcurrent::run() 时只会使用一个线程，并且无法暂停/恢复/取消，也不能查询计算进度。

**另请参阅**： Qt Concurrent 模块文档以获取各个函数的详细信息。



## WorkerScript: QML中的多线程

QML 类型 WorkerScript 可将 JavaScript 代码与 GUI 线程并行运行。

每个 WorkerScript 实例可附加一个 `.js` 脚本。当调用 WorkerScript.sendMessage() 时，脚本将会运行在一个独立的线程中（伴随一个独立的 QML 上下文）。在脚本运行结束后，WorkerScript 将会向 GUI 线程发送回复，后者会调用 WorkerScript.onMessage() 信号处理函数。

使用 WorkerScript，很像使用一个移入子线程工作的 QObject，数据通过信号槽在线程间进行传输。

**另请参阅**：WorkerScript 文档以获得实现脚本的详细信息，以及能够在线程间传输的数据类型列表。



## 选择合适的方法

如上文所述，Qt 提供了开发多线程应用的不同解决方案。对一个给定的程序，需要根据新线程的用途与线程的生命周期来决定正确的方案。下面是一组 Qt 多线程技术的功能对比表，以及对于一些范例较为推荐的解决方案。

### 解决方案对比

| 特性                         | QThread                     | QRunnable 与 QThreadPool | QtConcurrent::run()                                    | Qt Concurrent(Map, Filter, Reduce) | WorkerScript                 |
| ---------------------------- | --------------------------- | ------------------------ | ------------------------------------------------------ | ---------------------------------- | ---------------------------- |
| 语言                         | C++                         | C++                      | C++                                                    | C++                                | QML                          |
| 可以指定线程优先级           | 是                          | 是                       |                                                        |                                    |                              |
| 可以在线程中运行运行事件循环 | 是                          |                          |                                                        |                                    |                              |
| 可以通过信号获取数据更新     | 是（通过 QObject 对象接收） |                          |                                                        |                                    | 是（通过 WorkerScript 接收） |
| 可以使用信号控制线程         | 是（通过 QThread 接收）     |                          |                                                        | 是（通过 QFutureWatcher 接收）     |                              |
| 可以通过QFuture 监视线程     |                             |                          | 部分适用（`译者注：仅可监视返回值，不可监视执行进度`） | 是                                 |                              |
| 内建的暂停/恢复/取消功能     |                             |                          |                                                        | 是                                 |                              |



### 示例用例

| 线程生命周期      | 操作                                                         | 解决方案                                                     |
| :---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 单次调用          | 在另一个线程中运行新的线性函数，可选地在运行期间进行更新进度。 | Qt 提供不同解决方案：<br/>1. 重写 QThread::run() 并将函数放入其中，启动 QThread ，发射信号来更新进度。<br/>2. 重写 QRunnable::run() ，将函数放入其中。将 QRunnable 添加到 QThreadPool 中。修改线程安全的变量以更新进度；<br/>3. 使用 QtConcurrent::run() 运行函数。修改线程安全变量以更新进度。 |
| 单次调用          | 在另一个线程中运行一个现成的函数，并取得它的返回值。         | 使用 QtConcurrent::run() 运行函数。让 QFutureWatcher 在函数返回时发射 finish() 信号，并调用 QFutureWatcher::result() 来获取函数的返回值。 |
| 单次调用          | 对一个容器的所有元素执行一个操作，使用所有可用的 CPU 核心。例如，从一组图片生成缩略图。 | 使用 Qt Concurrent 的 QtConcurrent::filter() 函数选择容器元素，并用 QtConcurrent::map() 函数对每个元素执行操作。要将输出合并为单个结果，可以使用 QtConcurrent:: filteredReduced() 和 QtConcurrent::mappedReduced()。 |
| 单次调用/长期存在 | 在纯 QML 应用中执行耗时计算，并在结果就绪时更新 GUI 。       | 将计算代码放在 `.js` 脚本中，将它附加在 WorkerScript 实例上。调用 WorkerScript.sendMessage() 启动新线程执行计算。脚本也同样调用 sendMessage()，将结果传回 GUI 线程。在 onMessage 中处理结果并且更新 GUI 。 |
| 长期存在          | 对象位于另一个线程中，可以根据请求执行不同的任务和/或接收要使用的新数据。 | 子类化一个 QObject 以创建一个工作类。实例化这个工作类对象与一个 QThread 。将工作类移入新线程。通过队列信号槽的连接，将命令与数据传递给工作类对象。 |
| 长期存在          | 在另一个不需要接收任何信号或事件的线程中，重复执行资源开销大的操作。 | 直接重写 QThread::run() 并创建死循环。启动无事件循环的线程。可以发送信号将数据送回 GUI 线程（`译者注：发送信号不需要依赖事件循环，接收并执行槽函数才需要`)。 |



