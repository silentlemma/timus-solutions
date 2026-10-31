# 1612. 电车论坛

[Timus 1612](https://acm.timus.ru/problem.aspx?space=1&num=1612) · 难度 152 · strings

原题作者 Alexander Ipatov，由 Denis Musin 准备，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

论坛上一条不超过 10000 个字符的消息由小写拉丁字母、空格、换行和标点 `. , - : ! ?` 组成。若其中单词 `tram`
出现得比 `trolleybus` 多，作者是电车司机；反之是无轨电车司机；否则是公交车司机。单词是由字母组成的连续片段。
这条消息是谁写的？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

消息。

## 输出

`Tram driver`、`Trolleybus driver` 或 `Bus driver`。

## 样例

### 样例 1

输入:

```
of course, tram is the best transport
in the world!
```

输出:

```
Tram driver
```

### 样例 2

输入:

```
yes, yekaterinburg trams are the
best trams in the world, but
i like my trolleybus too.
```

输出:

```
Trolleybus driver
```

### 样例 3

输入:

```
read forum.tr.ru every day!
you can learn much about tram 
drivers and trolleybus drivers.
```

输出:

```
Bus driver
```

## 解法

在每个非字母字符处把消息切成单词，分别统计等于 `tram` 和 `trolleybus` 的单词个数并比较：`O(n)`。
答案已在生成的消息上与独立实现对比过。

注意事项：

- 只有完整的单词才算：`trams`、`tramway` 或 `forum.tr.ru` 中的 `tr` 都不是单词 `tram`（样例 2 和 3）；
- 标点也分隔单词，所以 `tram-tram` 中有两个 tram，`tram,trolleybus` 中各有一个（测试 06 和 07）；
- 两个数相等（包括都为零）时是公交车司机。

## 优化解法

优化的 C++ 解法把单词收集在一个固定的 11 字节 `char` 数组中，而不是
`std::string`：只有不超过 10 个字母（`trolleybus` 的长度）的单词才可能匹配，所以
第 10 个之后的字母只计数、不保存。它用范围比较判断字母，而不是 `islower`：
{1612_strings_optimized.cpp}。

优化的 Java 解法从 4 KB 缓冲区中读取字节，而不是把整条消息收集到 `StringBuilder`
里再用正则表达式切分。对当前单词，它只记录长度以及它是否仍是 `tram` 和
`trolleybus` 的前缀，因此从不保存任何单词：{1612_strings_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1612_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +56.41%; 基础版本: `1612_strings.cpp`.

- `1612_strings_optimized.java`: 时间降低 +14.68%; 内存降低 +51.90%; 基础版本: `1612_strings.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1612_strings.go](1612_strings.go).
- [1612_strings.rs](1612_strings.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1612_strings.cpp](1612_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 156 KB | 11288250 |
| [1612_strings.go](1612_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1124 KB | 11288251 |
| [1612_strings.java](1612_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 840 KB | 11288255 |
| [1612_strings.py](1612_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 444 KB | 11288253 |
| [1612_strings.rs](1612_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 232 KB | 11288257 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1612_strings_optimized.cpp](1612_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 68 KB | 11305846 |
| [1612_strings_optimized.java](1612_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 404 KB | 11305849 |
