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

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

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

`1685_strings_optimized.rs`. 保留一行编码文本，对输出切片递归回放中间、左、右的平衡遍历。保留首尾空格，只去掉 CR/LF。两个各 20000 字节的固定数组替代 String、动态输出和显式区间栈。每个字符访问一次，时间 O(n)。显式存储为 40000 字节加 O(log(n+1)) 递归帧；题目上界保证数组容量足够。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1685_strings.rs` 相比：时间 0.062 s → 0.046 s；内存 248 KB → 88 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1685_strings_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

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
| [1685_strings_optimized.java](1685_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 668 KB | 11307316 |
| [1685_strings_optimized.rs](1685_strings_optimized.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 88 KB | 11325106 |
