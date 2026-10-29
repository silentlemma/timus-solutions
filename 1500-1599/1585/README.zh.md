# 1585. 企鹅

[Timus 1585](https://acm.timus.ru/problem.aspx?space=1&num=1585) · 难度 38 · implementation

原题作者 Vladimir Yakovlev，出自 2007 年 10 月 27 日在叶卡捷琳堡举行的 ACM ICPC 2007–2008 NEERC 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

笔记本里记了 N ≤ 1000 只企鹅，每只记为“Emperor Penguin”“Little Penguin”或“Macaroni Penguin”。输出出现次数最多的种类；
它是唯一的。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后每行一个种类。

## 输出

出现最多的种类。

## 样例

### 样例 1

输入:

```
7
Emperor Penguin
Macaroni Penguin
Little Penguin
Emperor Penguin
Macaroni Penguin
Macaroni Penguin
Little Penguin
```

输出:

```
Macaroni Penguin
```

## 解法

按第一个单词统计记录，输出次数最多的种类，后面加上“Penguin”。`O(N)`。

注意事项：

- 每条记录中间有空格，所以要么按整行读，要么按两个单词读；
- 某个种类可能根本不出现（测试 03）。

## 优化解法

三种企鹅以不同的大写字母 E、L、M 开头，而单词“Penguin”和数字 `N` 都不含这些字
母，因此只需在整个输入中统计这几个字母，选出最大的计数。优化的 C++ 解法完全不读
取单词，用 `getchar` 统计字母，并用 `puts` 而不是 `iostream` 输出答案：88 KB，而
不是 388 KB，时间不变。优化的 Java 解法在读取 256 字节块时统计这些字母：
0.109 s，而不是 0.171 s；328 KB，而不是 4576 KB。

优化的 Python 解法用 `bytes.count` 在原始字节中统计完整名称：348 KB，而不是
512 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB | 11287935 |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB | 11287937 |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB | 11287943 |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB | 11287941 |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB | 11287944 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1585_implementation_optimized.cpp](1585_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 88 KB | 11303626 |
| [1585_implementation_optimized.java](1585_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 328 KB | 11303761 |
| [1585_implementation_optimized.py](1585_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 348 KB | 11303762 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
