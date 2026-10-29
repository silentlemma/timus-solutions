# 1446. 分院帽

[Timus 1446](https://acm.timus.ru/problem.aspx?space=1&num=1446) · 难度 91 · implementation

原题作者 Stanislav Vasiliev，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 名新生（1 ≤ N ≤ 1000）被分进各学院；按分院仪式的顺序，每名新生先有一行名字
（拉丁字母、空格和连字符，不超过 200 个字符），下一行是学院。按斯莱特林、赫奇帕
奇、格兰芬多、拉文克劳的顺序输出名单：学院名加冒号，然后按仪式顺序每行一个学
生，名单之间空一行。每个学院至少分到一名学生。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后 2N 行：每名学生的名字和学院。

## 输出

四份名单。

## 样例

### 样例 1

输入:

```
7
Ivan Ivanov
Gryffindor
Mac Go Nagolo
Hufflepuff
Zlobeus Zlei
Slytherin
Um Bridge
Slytherin
Tatiana Henrihovna Grotter
Ravenclaw
Garry Potnyj
Gryffindor
Herr Mionag-Ranger
Gryffindor
```

输出:

```
Slytherin:
Zlobeus Zlei
Um Bridge

Hufflepuff:
Mac Go Nagolo

Gryffindor:
Ivan Ivanov
Garry Potnyj
Herr Mionag-Ranger

Ravenclaw:
Tatiana Henrihovna Grotter
```

## 解法

因为名字里有空格，所以按行读入，把每个名字追加到所属学院的名单里；然后按要求的
顺序输出名单。名字只去掉换行符，内部的空格原样保留。共 `O(N)` 行。

注意事项：

- 按单词读入会把名字拆开（测试 01、03、04）；
- 学生的名字可能和学院同名（测试 03）；
- 输出中学院的顺序不是字母顺序。

## 优化解法

优化的 Rust 解法不需要以学院名称为键的映射。它逐行读取输入而不是一次读完，在四个
学院的列表中找到学院，并把每个名字直接追加到对应学院的字节缓冲区：492 KB，而不是
980 KB，时间不变。

优化的 Java 解法按 4 KB 分块读入，按首字母识别学院（四个学院的首字母各不相同），
并把名字以字节形式复制到各学院自己的字节流中，不创建 `String` 对象：0.062 s，而
不是 0.125 s；1180 KB，而不是 2324 KB。优化的 Python 解法以字节读取各行，并把每
个学院的名字收集在一个 `bytearray` 中：812 KB，而不是 1520 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1446_implementation.cpp](1446_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.031 s | 520 KB | 11286303 |
| [1446_implementation.go](1446_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1672 KB | 11286304 |
| [1446_implementation.java](1446_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2324 KB | 11286306 |
| [1446_implementation.py](1446_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 1520 KB | 11286305 |
| [1446_implementation.rs](1446_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 980 KB | 11286307 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1446_implementation_optimized.java](1446_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.062 s | 1180 KB | 11303748 |
| [1446_implementation_optimized.py](1446_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 812 KB | 11303749 |
| [1446_implementation_optimized.rs](1446_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 492 KB | 11303607 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
