# 1680. 第一个未出线名次

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · 难度 224 · strings

原题作者 Dmitry Ivankov，由 Alexander Ipatov 准备，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

半决赛向总决赛输送 q 支队伍，每所大学至多一支：凡是排在本校另一支队伍之后的队伍都会从排名表中划掉。
输出划掉之后位于第 q + 1 名的队伍。

## 输入

年份、n（n ≤ 201）和 q（3 ≤ q ≤ 12），然后按名次给出 n 支队伍。
队伍写作大学名、一个空格、'#' 和 1 到 8 的编号；只有一支队伍的大学可以不写编号。
名称由拉丁字母、空格、'.'、'-' 和 '&' 组成，长度不超过 36，两所大学的名称不会只在大小写上不同。答案一定存在。

## 输出

该队伍在排名表中的写法。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入：

```
1999 10 6
St Petersburg SU #1
Belarusian SU #1
Moscow SU #4
Southern Ural SU
Moscow SU #1
Novosibirsk SU #1
St Petersburg SU #3
Belarusian SU #3
St Petersburg IFMO #1
Ural SU #3
```

输出：

```
Ural SU #3
```

## 解法

沿排名表往下走，维护已有队伍进入名单的大学集合。队伍所属的大学是最后一个 '#' 之前的文本去掉末尾空格，
没有 '#' 时就是整行。既然两所大学的名称不会只在大小写上不同，就用小写来比较。
所属大学已在集合中的队伍跳过；否则若集合里已有 q 所大学，这支队伍就是答案，若没有，则把它的大学加入集合。
名称长度为 L 时 `O(n · L)`。

注意事项：

- 同一所大学可能以不同的大小写出现（“Ural SU” 和 “URAL SU”，测试 02），所以比较时忽略大小写；
- 名称要整体比较：“Ural SU” 和 “Ural SU State” 是不同的大学（测试 03）；
- 按输入原样输出队伍，包括编号。

答案与一个独立的已通过实现一致。

## 优化解法

仍选择每所大学的第一支队伍，大学名比较忽略大小写，输出保留原队名拼写。达到输出配额后不再保存新大学键。流式处理规定的记录，避免保存全部输入行和额外副本。选用的 PyPy 实现保留 Unicode 处理，不因节省空间而改变大小写规则或输出编码。

- `1680_strings_optimized.cpp`: 0.001 s / 100 KB; 基础版 `1680_strings.cpp`: 0.001 s / 400 KB; 相对基础版的变化: 时间 -0.0%, 内存 -75.0%.
- `1680_strings_optimized.py`: 0.125 s / 244 KB; 基础版 `1680_strings.py`: 0.078 s / 364 KB; 相对基础版的变化: 时间 +60.3%, 内存 -33.0%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1680_strings.cpp`; 覆盖实现 `1680_strings_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 47/47.

- Go: 优先教学基础版 `1680_strings.go`; 覆盖实现 `1680_strings.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1680_strings.java`; 覆盖实现 `1680_strings.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1680_strings.py`; 覆盖实现 `1680_strings_optimized.py`; 时间/内存名次 11/1, 其他作者记录 12/12.

- Rust: 优先教学基础版 `1680_strings.rs`; 覆盖实现 `1680_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.001 s | 400 KB | 11308838 |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB | 11288810 |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB | 11288813 |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 364 KB | 11308839 |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB | 11288816 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1680_strings_optimized.cpp](1680_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(input size) | AC | 0.001 s | 100 KB | 11308250 |
| [1680_strings_optimized.py](1680_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(input size) | AC | 0.125 s | 244 KB | 11309387 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
