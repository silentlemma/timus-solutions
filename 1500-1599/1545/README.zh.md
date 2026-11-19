# 1545. 象形文字

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · 难度 50 · implementation

原题作者 Evgeny Krokhalev，出自 2007 年 4 月 21 日在叶卡捷琳堡举行的第十一届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

词典中有 N ≤ 1000 个汉字，每个写作两个小写字母。给定输入的一个字母，输出以它开头的汉字。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，N 个两字母条目，然后是那个字母。

## 输出

符合的条目，每行一个，顺序任意；没有则不输出。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器将输出分为记号，排序后比较列表并保留出现次数。匹配条目顺序不限，重复项必须保留。

## 样例

### 样例 1

输入:

```
6
na
no
ni
ki
ka
ku
k
```

输出:

```
ka
ki
ku
```

## 解法

把每个条目的首字母与输入的字母比较，按输入顺序输出匹配项。`O(N)`。

注意事项：

- 没有匹配时输出为空（测试 02、05）；
- 出现两次的条目要输出两次（测试 03）；
- 字母必须在首位：出现在第二位不算（测试 05）。

## 优化解法

优化的 C++ 解法把两个字母的条目存放在局部的三字节 C 字符串数组中，而不是
`std::string`，用 `scanf("%2s")` 读入、用 `puts` 输出：120 KB，而不是 392 KB，时
间不变。

每个象形文字都是两个字母。优化的 Java 解法把它们放在由 256 字节块填充的字节数组
中，并从一个字节数组输出答案，不用 `Scanner`，也不用字符串：392 KB，而不是
1804 KB，时间不变。优化的 Rust 解法把每个象形文字存为一对字节，并通过缓冲区很小
的 `BufWriter` 输出：0.015 s，而不是 0.046 s；196 KB，而不是 236 KB。

`1545_implementation_optimized.py`. 保留词典筛选及原有顺序、重复项。分割原始字节，用 startswith 检查单字母前缀，以 bytes 连接匹配项。不保留解码词典或单独的匹配文本列表，但记号列表、切片引用和拼接答案仍需 O(N) 空间，因为每个条目长二。时间 O(N)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1545_implementation.py` 相比：时间 0.062 s → 0.14 s；内存 460 KB → 216 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1545_implementation_optimized.py`：在该可比样本中，时间名次 168/175，内存名次 2/175。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
| [1545_implementation_optimized.py](1545_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N) | AC | 0.14 s | 216 KB | 11324837 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
