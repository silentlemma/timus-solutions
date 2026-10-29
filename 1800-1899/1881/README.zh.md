# 1881. 冗长的题面

[Timus 1881](https://acm.timus.ru/problem.aspx?space=1&num=1881) · 难度 62 · simulation

原题作者 Fedor Fominykh，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每页有 h 行，每行 w 个字符。同一行的单词之间用一个空格分隔，放不进当前行的单词另起一行；单词从不拆分。n 个单词的文本占多少页？

## 输入

h、w 和 n（1 ≤ h, w ≤ 100，1 ≤ n ≤ 10 000），然后是 n 个单词，每行一个，长度都不超过 w；总长度不超过 10 000。
单词非空，且仅由大写或小写英文字母以及标点符号 `.,!?` 组成。

## 输出

页数。

## 样例

### 样例 1

输入：

```
3 5 6
To
be
or
not
to
be
```

输出：

```
2
```

## 解法

贪心地填充各行。记录当前行已用的字符数；单词如果不是行首，需要它的长度加一个空格。放不下就用它开始新的一行。把计数初值设为 −1，行首单词就不需要空格。答案是行数除以 h 向上取整。`O(n)`。

样例中各行为 "To be"、"or"、"not" 和 "to be"："or not" 和 "not to" 都多了一个字符。四行在每页三行的纸上占两页。

注意事项：

- 连同空格恰好填满行剩余部分的单词仍然放得下；
- 空格只放在单词之间，从不放在行首；
- 页数向上取整。

在 100 个随机文本上，页数与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法从不保存单词：它用 `getchar` 逐个字符读取每个单词，只记下长度，而
分行只需要长度。内存为 128 KB，而不是 404 KB，时间不变。

优化的 Java 解法按 1 KB 分块读入，只逐字节测量每个单词的长度，而不是把各行拼起来
再切成字符串：408 KB，而不是 1336 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB | 11291031 |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB | 11291032 |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB | 11291035 |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB | 11291034 |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB | 11291036 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1881_simulation_optimized.cpp](1881_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 128 KB | 11303646 |
| [1881_simulation_optimized.java](1881_simulation_optimized.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 408 KB | 11303783 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
