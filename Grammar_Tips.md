# 语法小贴士

本文件用于总结翻译英文技术文档时，如何尽可能实现信达雅。



## 翻译原则

1. 尽量使用书面语，避免口语化：
   1. 但避免用力过猛，令句子明显诘屈聱牙；
   2. 尽量避免出现任何人称代词。
2. 避免过于复杂的长句，用逗号拆分为多个字句，来回避句式杂糅；
3. 避免直译英语语序，这会导致严重的“翻译腔”，需要考虑把有从句的复合句式调整为中文语句；
4. 避免直译英文词组，这是一种逆向的“chinglish”，如“你得到了它”；
5. 仔细斟酌任何一个/组介词的使用，尤其是需要配对使用，或者影响上下文转换的；
6. 仔细斟酌修饰 and/or 的定语（形容词/从句）和状语（副词/从句），避免不小心扩大修饰范围；
7. 仔细斟酌状语、定语、补语的翻译，避免词性发生变化；
8. 仔细斟酌时态的转换，避免出现时态错误；
9. 避免连续使用重复的修饰性词汇，如形容词、副词、介词。

整体目标是做到 ELI5，让读者可以一目十行地快速浏览，同时精读段落时可以保持视线连续移动而不会出现卡顿，即：

1. 让语句结构复合中文习惯，避免生僻用语，并针对句子之间、段落之间的上下文关系适当调整内容结构；
2. 对于每个句子，需要保证内容翻译的精确度，不会出现任何时态、作用域、5W1H 的歧义。

> ELI5: Explain Like I'm 5 (years old)
>
> 5W1H: Who Where When What Why How



## 语句结构

### 调整语句顺序

在状语和定语同时出现时，英文的语句和中文的语序经常是相反的。此时需要调整语句，以避免出现翻译腔。

原文：

> The right solution for a given application depends on the purpose of the new thread and the thread's lifetime. 

翻译腔：

> - 正确的解决方案，对于给定的程序，依赖于新线程的用途和线程的生命周期。
> - 对于给定程序的正确的解决方案，依赖于新线程的用途和线程的生命周期。

正确翻译：

> 对一个给定的程序，需要根据新线程的用途与线程的生命周期来决定正确的方案。

----

### 拆分长句

调整语句顺序时，若句式过于复杂，也容易写出虽然语序正确，但阅读时格外吃力的句子，即句式杂糅。

此时，应该使用逗号将长句进行拆分为多个子句。

原文：

> - This global thread pool automatically maintains an optimal number of threads based on the number of cores in the CPU.
> - The Qt Concurrent module provides high-level functions that deal with some common parallel computation patterns: map, filter, and reduce.

句式杂糅：

> - 此公共线程池会自动维持基于 CPU 核心数计算的最佳值的线程数。
> - Qt Concurrent 模块提供了数个用于处理一些常见的并行计算模式的高级函数：map、filter 和 reduce。

正确翻译：

> - 此公共线程池会自动维持一定数量的线程，线程数为基于 CPU 核心数计算的最佳值。
> - Qt Concurrent 模块提供了数个高级函数，用于处理一些常见的并行计算模式：map、filter 和 reduce。



## 标点与词汇

### 标点与空格

- 中英混排时，英文单次前后应该带空格；
- 纯英文句子时，分隔符（逗号句号分号）遵循英文语法，符号前不空格，符号后空格；
- 中英语句通过分隔符连接时，使用中文分隔符，无需空格；
- 引号括号根据内容而定，中英混排时一律使用中文标点；
- **加粗**、`代码` 可考虑前后添加空格增加区分度，但与中文分隔符相连时，同理省略空格；
- 分号是用于分隔长句中互相无关的字句，优先级低于句号——因此在使了句号的列表条目末尾，不应使用分号。

----

### 的、地、得

> 的定 地状 得后补

- **的** 用作 **定语**，即形容词与名词间的连接词（常见的并行计算模式）；
- **地** 用作 **状语**，即副词与动词之间的连接词（频繁地创建与销毁线程）；
- **得** 用作 **补语**，即动词或形容词后的补充内容（这段代码执行得很频繁）。

----

### 人称代词

- 第一人称：不应出现。在本项目中仅当原文中便以 Qt 维护者的身份叙述问题时出现，即 **我们**。
- 第二人称：避免出现。利用中文可以一定程度省略主语的特性，可以规避绝大多数第二人称的使用。不得不用时，使用 **您**。
- 第三人称：正常使用 **它**。无性别的第三人称代词，在技术文档中常被用于指代抽象概念和对象。

省略主语，同时删除无法配对使用的的连词：

> 如果您频繁地创建或销毁线程，那么资源开销将会非常大。
>
> 如果<del>您</del>频繁地创建或销毁线程，<del>那么</del>资源开销将会非常大。

----

### 反向 Chinglish

避免平铺直叙的直译英文惯用词组，否则会产生很别扭的自造词/句，和 Chinglish 非常类似。

原文：

> Each Qt application has a global thread pool, which is **accessible through** QThreadPool::globalInstance().

错误翻译：

> 每一个 Qt 程序都会自带一个公共线程池，可以通过调用 QThreadPool::globalInstance() 来**获得它**。

正确翻译：

> 每一个 Qt 程序都会自带一个公共线程池，可以通过调用 QThreadPool::globalInstance() 来**获取**。

----

### 介词

介词用于连接语句的不同部分，是形成语句结构的核心部件。介词对组织起语句的 *从属关系、上下文变化、内容转折* 等起着至关重要的作用。

使用介词时，英文和中文的介词都需要仔细斟酌，否则极易出现错误理解，或者表意不明导致歧义。

原文：

> When the script finishes running

错误翻译：

> > 当脚本运行结束后
>
> 当……时

正确翻译：

> > 在脚本运行结束后
>
> 在……后



## 语句成员角色

### 修饰词的作用域

定语、状语、补语都是用于修饰语句中的其它内容。当语句中出现多个被修饰对象，尤其是在同一个语句位置时，需要仔细区分修饰语的限定范围，避免意外扩大、缩小修饰范围，或导致二义性。

原文：

> - QThread can either *be instantiated* **directly or subclassed.** （后两者为 *be instantiated* 的副词）
> - When the script finishes running, it can send a reply back to the GUI thread **which** will invoke the WorkerScript.onMessage() signal handler.（*which* 用于修饰 *GUI thread*）

错误翻译：

> - 您可以*直接* **实例化或子类化** QThread。（作用域改变，*directly* 和 *be instantiated* 被调换了）
> - 在脚本运行结束后，WorkerScript 将会向 GUI 线程发送回复，会调用 WorkerScript.onMessage() 信号处理函数。（从句的作用对象不明，无法确定是 *WorkerScript* 还是 *GUI 线程*）

正确翻译：

> - 您可以**直接** *实例化* QThread，或*建立* **子类**。（保持正确的作用域，*be instantiated* 拆分到两个字句后，用两个词语分别描述） 
> - 在脚本运行结束后，WorkerScript 将会向 GUI 线程发送回复，**后者**会调用 WorkerScript.onMessage() 信号处理函数。（通过 *后者* 指明从句的作用对象）

----

### 词性变化

定语、状语、补语都是用于修饰其它语句对象，并且放置的前后位置也非常灵活。

不同词性的内容翻译至中文时，通常会通过附加文字来表示词性，很容易出现词性变化，导致理解错误。

原文：

> > To run code in one of a QThreadPool's threads, reimplement QRunnable::run() and instantiate the **subclassed** QRunnable.
>
> 形容词，与 QRunnable 共同形成宾语

错误翻译：

> > 为了将代码放入 QThreadPool 的线程中运行，可以重写 QRunnable::run() 函数并实例化**继承了** QRunnable 的子类。
>
> **继承了 QRunnable** 第一眼看起来是动宾结构的句式，但往后看到 **的子类** 时，又转换为修饰 **子类** 的定语。因此虽然最终含义与原文一致，但在阅读过程中发生了词性变化，同时导致出现理解错误回滚再重新解读，会严重破坏阅读的流畅性。

正确翻译：

> > 为了将代码放入 QThreadPool 的线程中运行，可以重写 QRunnable::run() 函数并实例化**继承自** QRunnable 的子类。
>
> 词性转换为副词，修饰形容词 **QRunnable 的**，但避免了阅读过程中的错误理解

----

### 时态变化

时态在英文中，通过单词结构的直接变换来表达，偶尔会辅以介词（如 `be processed`）。

但在中文中，时态和词性一样，是通过附加文字来描述的，此时很容易粗心大意导致时态发生变化，影响理解内容。

原文：

> > The Qt Concurrent module **provides** high-level functions that deal with some common parallel computation patterns: map, filter, and reduce.
>
> 一般现在时

时态错误：

> > 公共线程池会自动维持**着**一定数量的线程，线程数为基于 CPU 核心数计算的最佳值。
>
> **着**通常用于表示进行时，并且通常还需伴随另一个子句来共同描述一个完整的动作：
>
> - 小明打着电话，说道……（需要配合子句）
> - 小明正在打电话（现在进行时，可独立成句）

正确翻译：

> > 此公共线程池**会自动维持**一定数量的线程，线程数为基于 CPU 核心数计算的最佳值。
>
> 一般现在时
