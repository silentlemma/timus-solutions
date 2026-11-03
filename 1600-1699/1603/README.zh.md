# 1603. 博学者

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · 难度 255 · implementation

原题作者 Vladimir Yakovlev，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 4 × 4 的表格中填着小写字母。单词可以沿着水平或竖直相邻的格子组成的路径写出，路径可以在任意处直角转弯，
但不能重复经过同一格。对最多 100 个长度为 1 到 16 的单词，判断能否在表中找到。

时间限制：1 秒。内存限制：64 MB。

## 输入

表格的四行，然后是 n 和各个单词。

## 输出

每个单词输出 `word: YES` 或 `word: NO`。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

输出:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## 解法

从每个写着首字母的格子开始深度优先搜索，每步走到一个未用过、写着下一个字母的相邻格子。已用过的格子构成 16 位掩码。
重复的字母会让搜索多次进入同一局面：同样的已用格子集合、同样的最后一格、同样的剩余单词。所以失败的
(掩码, 格子) 对会被记住，不再重复搜索；这样的对至多 16·2¹⁶ 个，实际能到达的少得多。另有一个快速检查，
先排除需要某个字母多于表中数量的单词。

结果已在生成的表格上与独立实现对照，包括单一重复字母配长单词的表格。

注意事项：

- 字母计数可以在搜索前排除单词：十五个 `a` 格子无法提供十六个 `a`，唯一的 `b` 格子也不能同时作为单词的两端（测试 04）；
- 重复字母可能导致重复搜索状态，因此应记住失败的 (掩码, 格子) 对；测试 07 有十四个 `a` 格子以及各一个 `b`、`c` 格子，最长的单词能通过字母计数检查；
- 这样的 NO 可能单由奇偶性导致：把表格按国际象棋盘染色，16 格的路径总是在另一种颜色上结束，
  所以首尾格子同色的单词不可能占满全部 16 格（测试 07）；
- 格子不能用两次，而且只能水平或竖直走（测试 03）。

## 优化解法

搜索仍沿相邻格移动且不重复访问。失败状态按终点及访问掩码记忆；单词位置可由掩码大小确定，不必增加状态维度。字符可选集合和邻接掩码在分支前排除不可能的后续。相同单词复用结果。棋盘固定且小，因此明确计算子集状态上界，不宣称搜索为多项式时间。

- `1603_implementation_optimized.cpp`: 0.015 s / 176 KB; 基础版 `1603_implementation.cpp`: 0.031 s / 452 KB; 相对基础版的变化: 时间 -51.6%, 内存 -61.1%.
- `1603_implementation_optimized.go`: 0.031 s / 988 KB; 基础版 `1603_implementation.go`: 0.031 s / 5708 KB; 相对基础版的变化: 时间 -0.0%, 内存 -82.7%.
- `1603_implementation_optimized.java`: 0.093 s / 620 KB; 基础版 `1603_implementation.java`: 0.109 s / 5228 KB; 相对基础版的变化: 时间 -14.7%, 内存 -88.1%.
- `1603_implementation_optimized.py`: 0.093 s / 1128 KB; 基础版 `1603_implementation.py`: 0.359 s / 21264 KB; 相对基础版的变化: 时间 -74.1%, 内存 -94.7%.
- `1603_implementation_optimized.rs`: 0.031 s / 292 KB; 基础版 `1603_implementation.rs`: 0.062 s / 420 KB; 相对基础版的变化: 时间 -50.0%, 内存 -30.5%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1603_implementation.cpp`; 覆盖实现 `1603_implementation_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 59/59.

- Go: 优先教学基础版 `1603_implementation.go`; 覆盖实现 `1603_implementation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1603_implementation.java`; 覆盖实现 `1603_implementation_optimized.java`; 时间/内存名次 1/2, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1603_implementation.py`; 覆盖实现 `1603_implementation_optimized.py`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Rust: 优先教学基础版 `1603_implementation.rs`; 覆盖实现 `1603_implementation_optimized.rs`; 时间/内存名次 1/1, 其他作者记录 1/1.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB | 11288124 |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB | 11288126 |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB | 11288130 |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB | 11288128 |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB | 11288131 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1603_implementation_optimized.cpp](1603_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(16*2^16) per distinct word | AC | 0.015 s | 176 KB | 11309250 |
| [1603_implementation_optimized.go](1603_implementation_optimized.go) | Go 1.14 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 988 KB | 11309252 |
| [1603_implementation_optimized.java](1603_implementation_optimized.java) \* | Java 1.8 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 620 KB | 11309251 |
| [1603_implementation_optimized.py](1603_implementation_optimized.py) | Python 3.12 x64 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 1128 KB | 11309249 |
| [1603_implementation_optimized.rs](1603_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 292 KB | 11309253 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
