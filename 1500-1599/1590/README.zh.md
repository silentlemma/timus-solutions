# 1590. 不同子串的数量

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · 难度 186 · strings

原题作者 Alexey Zhevak，出自 2007 年 10 月 27 日在叶卡捷琳堡举行的 ACM ICPC 2007–2008 NEERC 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个非空小写拉丁字母字符串，长度 `N ≤ 5000`。求不同非空连续子串的数量。时间限制：2 秒。内存限制：64 MB。

## 输入

字符串。

## 输出

不同子串的个数。

## 评测方式

按空白分隔的整数答案进行比较。

## 样例

### 样例 1

输入:

```
aaba
```

输出:

```
8
```

## 解法

推荐的简单算法按字典序排序所有后缀。位置 `i` 的后缀有 `N−i` 个非空前缀。
已出现的恰好是与前一个后缀的最长公共前缀所覆盖的长度：具有同一前缀的后缀在排序后连续出现。
因此答案为 `N(N+1)/2` 减去相邻后缀的 LCP 长度之和。首个后缀贡献全部前缀，
每个不同子串恰好计算一次。

五份 `sorting_strings` 实现该直接算法。一次比较可能读 `O(N)` 字符，
最坏时间为 `O(N² log N)`。C++ string_view、Go 切片和 Rust 借用切片仅需
`O(N)` 辅助空间。Java 8 子串和 Python bytes 切片会复制字符，需 `O(N²)` 空间。
Python 对前缀相等性二分搜索 LCP，使用 C 层字节比较，仍满足上述时间界。
五种实现均通过评测。

五份原后缀自动机也全部保留。状态按子串的结束位置集合分组，贡献
`len(v)−len(link(v))` 种不同长度。对非根状态求和即为答案；固定 26 字母时，
时间和空间均为 `O(N)`。克隆复制转移并继承旧后缀链接。

## 优化解法

教学基础算法排序后缀，用子串出现总数减去相邻后缀的最长公共前缀。紧凑 C++ 只排序后缀起点，不复制每个后缀，减少存储，但最坏长字符串比较成本不变。另一些后缀自动机把转移存入扁平边表；克隆状态必须先复制自己的边表再重定向。它们是不同算法，命名和测量比较分别保留。节省内存可能伴随时间增加，反之亦然。

- `1590_strings.java`: 0.093 s / 2412 KB; 基础版 `1590_sorting_strings.java`: 0.187 s / 28464 KB; 相对基础版的变化: 时间 -50.3%, 内存 -91.5%.
- `1590_strings.py`: 0.109 s / 3132 KB; 基础版 `1590_sorting_strings.py`: 0.109 s / 14664 KB; 相对基础版的变化: 时间 -0.0%, 内存 -78.6%.
- `1590_strings.rs`: 0.015 s / 2272 KB; 基础版 `1590_sorting_strings.rs`: 0.046 s / 300 KB; 相对基础版的变化: 时间 -67.4%, 内存 +657.3%.
- `1590_strings_optimized.java`: 0.109 s / 748 KB; 基础版 `1590_sorting_strings.java`: 0.187 s / 28464 KB; 相对基础版的变化: 时间 -41.7%, 内存 -97.4%.
- `1590_strings_optimized.py`: 0.109 s / 1084 KB; 基础版 `1590_sorting_strings.py`: 0.109 s / 14664 KB; 相对基础版的变化: 时间 -0.0%, 内存 -92.6%.
- `1590_strings_optimized.rs`: 0.015 s / 504 KB; 基础版 `1590_sorting_strings.rs`: 0.046 s / 300 KB; 相对基础版的变化: 时间 -67.4%, 内存 +68.0%.
- `1590_sorting_strings_optimized.cpp`: 0.031 s / 152 KB; 基础版 `1590_sorting_strings.cpp`: 0.015 s / 508 KB; 相对基础版的变化: 时间 +106.7%, 内存 -70.1%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1590_sorting_strings.cpp`; 覆盖实现 `1590_sorting_strings_optimized.cpp`; 时间/内存名次 43/1, 其他作者记录 119/119.

- Go: 优先教学基础版 `1590_sorting_strings.go`; 覆盖实现 `1590_sorting_strings.go`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Java: 优先教学基础版 `1590_sorting_strings.java`; 覆盖实现 `1590_strings.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1590_sorting_strings.py`; 覆盖实现 `1590_strings.py`; 时间/内存名次 19/15, 其他作者记录 60/60.

- Rust: 优先教学基础版 `1590_sorting_strings.rs`; 覆盖实现 `1590_sorting_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1590_sorting_strings.cpp](1590_sorting_strings.cpp) | G++ 13.2 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.015 s | 508 KB | 11308193 |
| [1590_sorting_strings.go](1590_sorting_strings.go) | Go 1.14 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.031 s | 1192 KB | 11308194 |
| [1590_sorting_strings.java](1590_sorting_strings.java) | Java 1.8 | sorting, strings | O(N² log N) time, O(N²) space for copied Java 8 suffix strings | AC | 0.187 s | 28464 KB | 11308195 |
| [1590_sorting_strings.py](1590_sorting_strings.py) | Python 3.12 x64 | sorting, strings | O(N² log N) time, O(N²) space for copied suffixes; prefix equality tested by binary search | AC | 0.109 s | 14664 KB | 11308191 |
| [1590_sorting_strings.rs](1590_sorting_strings.rs) | Rust 1.75 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix slices | AC | 0.046 s | 300 KB | 11308196 |
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB | 11287986 |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB | 11287991 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(N) | AC | 0.093 s | 2412 KB | 11287997 |
| [1590_strings.py](1590_strings.py) \* | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 3132 KB | 11287994 |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 2272 KB | 11287999 |
| [1590_strings_optimized.java](1590_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.109 s | 748 KB | 11308188 |
| [1590_strings_optimized.py](1590_strings_optimized.py) \* | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1084 KB | 11308180 |
| [1590_strings_optimized.rs](1590_strings_optimized.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 504 KB | 11308189 |
| [1590_sorting_strings_optimized.cpp](1590_sorting_strings_optimized.cpp) \* | G++ 13.2 x64 | sorting, strings | O(N^2 log N) | AC | 0.031 s | 152 KB | 11309286 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
