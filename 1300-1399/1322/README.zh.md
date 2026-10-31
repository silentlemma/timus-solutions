# 1322. 间谍

[Timus 1322](https://acm.timus.ru/problem.aspx?space=1&num=1322) · 难度 179 · strings

原题创意来自 Alexander Klepinin，由 Alexander Klepinin 和 Stanislav Vasiliev 准备，出自 2004 年 3 月 11–16 日在叶卡捷琳堡举行的第八届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

加密器取一段最多 100 000 个字符的文本，写出它的所有循环移位并排序，然后输出排好序的表格的最后一列，以及
原文所在行的编号 K。给定 K 和最后一列，还原文本。字符为字母和下划线，顺序是 A 到 Z，然后 `_`，然后 a 到 z。

时间限制：0.25 秒。内存限制：64 MB。

## 输入

第一行是 K，第二行是最后一列。

## 输出

原文。

## 样例

### 样例 1

输入：

```
3
rdarcaaaabb
```

输出：

```
abracadabra
```

## 解法

这是 Burrows–Wheeler 变换的逆变换。以字符 c 结尾的各行，把 c 从末尾移到开头后，就变成以 c 开头的各行，而且
相对顺序不变。以 c 开头的行按 c 之后的内容排序，以 c 结尾的行也恰好按同样的方式排序。所以以 c 结尾的第 j
行，就是以 c 开头的第 j 行移位一次的结果。

把最后一列的位置按字符稳定排序，结果记为 order。于是第 order[j] 行以排好序的列中第 j 个字符结尾，也就是第
j 行开头的字符，而第 order[j] 行是第 j 行左移一位，即晚一个字符开始的那个移位。从第 K 行出发沿 order 走 n
步，依次经过从文本第二个、第三个……字符开始的移位，而每个移位的最后一个字符正是它起点前面的那个字符，所以
文本按顺序得出。题目给出的字符顺序就是 ASCII 顺序，因此对 128 个编码做计数排序即可在 `O(n)` 时间内完成稳定排序。
Python 则使用内置的稳定比较排序，最坏时间复杂度为 `O(n log n)`。所有实现的额外空间均为 `O(n)`。

注意事项：

- 周期性文本会有若干相同的行，K 可能指向其中任意一行，结果都是同一个文本（测试 04）；
- 大写字母在下划线之前，小写字母在它之后（测试 05）；
- 排序必须稳定，否则相同的字符会被打乱；
- 时间限制是 0.25 秒，因此应使用缓冲输入输出。

在 400 个长度不超过 12 的随机文本和周期性文本上检验过解码器，这些文本用直接对移位排序的方式加密。

## 优化解法

优化的 C++ 解法在 `order` 的每个元素中同时打包该行结尾的字符：低 7 位存字符编码
（小于 128），高位存行号（小于 100 000 < 2^17），所以一个元素放得进 32 位。这样
沿行跳转时只读一个数组而不是两个，每个字符立即用 `putchar` 输出，而不是先把文本
拼成字符串。最后一列用 `scanf` 读入 100 001 字节的静态缓冲区，而不是用
`iostream` 和 `std::string`：{1322_strings_optimized.cpp}。

优化的 Java 解法在 `order` 的每个元素中同时打包该行结尾的字符：低 7 位存字符编码
（小于 128），高位存行号（小于 100 000 < 2^17），所以一个元素放得进 `int`。这样
沿行跳转时只读一个数组而不是两个，每个字符直接写入 `BufferedOutputStream`，而不
是存进 `char` 数组再变成 `String`。最后一列按 4 KB 分块逐字节读入 100 000 个元素
的 `byte` 数组，而不是把各行收集到 `StringBuilder` 再复制到 `char` 数组：
{1322_strings_optimized.java}。

优化的 Python 解法用按 128 个编码的计数排序代替内置的 `sorted`，并把 `order` 存
在 32 位元素的 `array("I")` 中，而不是 Python 整数的列表。每个元素还打包了该行结
尾的字符：低 7 位存字符编码（小于 128），高位存行号（小于 100 000 < 2^17），所以
一个元素放得进 32 位。文本在 `bytearray` 中构建，而不是单字符字符串的列表。计数
排序是 Python 循环，比 `sorted` 慢，所以收益主要在内存：
{1322_strings_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1322_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +43.24%; 基础版本: `1322_strings.cpp`.

- `1322_strings_optimized.java`: 时间降低 +0.00%; 内存降低 +70.69%; 基础版本: `1322_strings.java`.

- `1322_strings_optimized.py`: 时间降低 -39.74%; 内存降低 +84.08%; 基础版本: `1322_strings.py`.

## 各语言说明

- Python 用内置的稳定排序对位置排序；其他语言使用计数排序。
- Python 和 Rust 在解析前读入全部输入；Java 先收集各行再分词，C++ 和 Go 则从缓冲输入中读取词元。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings.cpp](1322_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1036 KB | 11284953 |
| [1322_strings.go](1322_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2624 KB | 11284954 |
| [1322_strings.java](1322_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 3152 KB | 11284956 |
| [1322_strings.py](1322_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.078 s | 6308 KB | 11284955 |
| [1322_strings.rs](1322_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 1108 KB | 11284957 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings_optimized.cpp](1322_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.001 s | 588 KB | 11307290 |
| [1322_strings_optimized.java](1322_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.093 s | 924 KB | 11307302 |
| [1322_strings_optimized.py](1322_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 1004 KB | 11307297 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
