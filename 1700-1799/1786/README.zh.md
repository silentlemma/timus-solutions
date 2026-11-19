# 1786. 桑德罗传记

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · 难度 110 · strings

原题作者 Olga Soboleva，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段由拉丁字母组成的文本需要修改，使其中出现单词 "Sandro"。把一个字母换成同样大小写的另一个字母需要 5 枚金币，改变一个字母的大小写也需要 5 枚。求最小花费。

## 输入

文本，长度为 6 到 200 个字母。

## 输出

最少的金币数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
MyNameIsAlexander
```

输出：

```
20
```

## 解法

枚举名字六个字母的所有放置位置。一个字母大小写不对要 5，字母本身不对再加 5，所以两方面都不对的字母要 10。在每个位置把六个代价相加，取最小的和。扫描本身需要 `O(n)` 时间，但 Python 在每个位置复制后缀 `text[start:]`，因此该实现的时间复杂度为 `O(n^2)`。所有实现计入输入字符串后的空间复杂度均为 `O(n)`；输入长度最多只有 200。

样例中最佳位置是 "xander"：x 需要换字母并改成大写，花 10，e → r 和 r → o 各花 5，共 20。

注意事项：

- 字母不对且大小写也不对时，两笔费用都要付；
- 测试 03 的 `sANDRO` 中，六个字母的大小写全部错误，因此花费为 30；
- 名字可以从第一个字母开始，也可以在最后一个字母结束。

在 2,000 个随机短文本、592 个定向用例、全部 8 个已有测试和 64 个生成用例上，Python 的答案与基于合法操作图的独立参考程序一致。

## 优化解法

`1786_strings_optimized.py`. 保留把 ASCII 字母及大小写改为 Sandro 六字母的费用。每目标位置建 256 字节转换表，把整段文本变为六条对齐费用流，再逐列加六项。去掉简单版每窗 text[start:] 的后缀复制（二次复制字符量）及逐字符 Python 调用。固定六字符目标下时间 O(L)，费用流空间 O(L)，并非常量。本版没有强制解释器退出。自身 Accepted 按排名收录，即使无实测 30% 改进。

与 `1786_strings.py` 相比：时间 0.109 s → 0.078 s；内存 408 KB → 400 KB。

优化的 C++ 解法用 `scanf` 把文本读入 201 字节的缓冲区（足够容纳 200 个字母和结尾
的零），而不是使用 `std::cin` 和 `std::string`；由于文本只含拉丁字母，它通过与
`'Z'` 比较来判断大小写，通过加上 `'a' − 'A'` 转成小写，而不是调用 `isupper` 和
`tolower`：{1786_strings_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐字符读取文本，而不是创建 `Scanner`；由于文
本只含拉丁字母，它通过与 `'Z'` 比较来判断大小写，通过加上 `'a' − 'A'` 转成小写，
而不是调用 `Character.isUpperCase` 和 `Character.toLowerCase`：
{1786_strings_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，并满足排名或资源改进准入条件。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1786_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +68.42%; 基础版本: `1786_strings.cpp`.

- `1786_strings_optimized.java`: 时间降低 +28.44%; 内存降低 +75.13%; 基础版本: `1786_strings.java`.

`1786_strings_optimized.rs`. 用环形存储只保留最近六个字母。对每个完整窗口，独立累加改大小写和忽略大小写后改字母以匹配 Sandro 的成本。每位置六次比较，时间 O(N)，额外空间 O(1)，无需保存文本或分配切片。 Rust 通过 C 运行库输入输出，避免完整的解码输入输出 String 和 Rust 格式化。简单且已通过评测的源代码保持不变。

与 `1786_strings.rs` 相比：时间 0.031 s → 0.062 s；内存 216 KB → 64 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1786_strings_optimized.py`：在该可比样本中，时间名次 2/32，内存名次 7/32。

`1786_strings_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 380 KB | 11304047 |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB | 11289804 |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1576 KB | 11304048 |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.109 s | 408 KB | 11304049 |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB | 11289809 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings_optimized.cpp](1786_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 120 KB | 11304276 |
| [1786_strings_optimized.java](1786_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.078 s | 392 KB | 11304277 |
| [1786_strings_optimized.rs](1786_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(N) | AC | 0.062 s | 64 KB | 11325109 |
| [1786_strings_optimized.py](1786_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L) time; O(L) space | AC | 0.078 s | 400 KB | 11325470 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
