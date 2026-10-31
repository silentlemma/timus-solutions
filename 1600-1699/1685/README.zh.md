# 1685. 拼写

[Timus 1685](https://acm.timus.ru/problem.aspx?space=1&num=1685) · 难度 184 · strings

原题作者 Eugene Krokhalev，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

文本按如下方式加密：先写出它的中间字符（n 个字符中的第 (1 + n) div 2 个），
然后加密它左边的部分，再加密右边的部分。给出加密后的行，还原原文。

## 输入

一行，至多 20000 个字符：拉丁字母、空格和标点。

## 输出

原文。

## 样例

### 样例 1

输入：

```
kyaVs alisse uop.
```

输出：

```
Vasya likes soup.
```

### 样例 2

输入：

```
gtorhoprahy
```

输出：

```
orthography
```

## 解法

加密按固定顺序访问文本的位置：区间的中点，然后左区间，然后右区间。
这个顺序只取决于 n，所以重放这个顺序，把密文的第 i 个字符放到第 i 个被访问的位置。
对从 0 开始编号的区间 lo..hi，中点是 (lo + hi) div 2。用显式栈代替递归，尽管递归深度只有约 log n。`O(n)`。

注意事项：

- 行首或行尾可能有空格，它们也是文本的字符：只能去掉换行符；
- 文本中可能有连续的多个空格（测试 05）。

答案与一个独立的已通过实现一致，并能把加密器的输出还原为随机文本。

## 优化解法

优化的 C++ 解法用 `fgets` 把这一行读进 20003 字节的静态缓冲区（足够放下 20000 个
字符、回车、换行和结尾的零），并填写一个 20000 字节的静态输出数组，用 `fwrite`
输出，而不是用 `std::string` 和 `iostream`。它在半开区间上用普通递归重放顺序，而
不是用存放二元组的向量，因为 20000 个字符时深度最多约 15 层：
{1685_strings_optimized.cpp}。

优化的 Java 解法在半开区间上用普通递归重放顺序（20000 个字符时深度最多约
15 层），而不是用为每个字符分配两个 `int[]` 区间的 `ArrayDeque`：
{1685_strings_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1685_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +71.13%; 基础版本: `1685_strings.cpp`.

- `1685_strings_optimized.java`: 时间降低 +14.68%; 内存降低 +60.05%; 基础版本: `1685_strings.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1685_strings.go](1685_strings.go).
- [1685_strings.rs](1685_strings.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings.cpp](1685_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 388 KB | 11288861 |
| [1685_strings.go](1685_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1228 KB | 11288862 |
| [1685_strings.java](1685_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1672 KB | 11288864 |
| [1685_strings.py](1685_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 536 KB | 11288863 |
| [1685_strings.rs](1685_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.062 s | 248 KB | 11288865 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings_optimized.cpp](1685_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 112 KB | 11307312 |
| [1685_strings_optimized.java](1685_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.093 s | 668 KB | 11307316 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
