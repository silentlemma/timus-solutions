# 1517. 最长公共子串

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · 难度 240 · suffix_structures

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定两个由大写拉丁字母组成的字符串，每个长度为 `N`，`1 ≤ N ≤ 100000`。输出任意最长公共连续子串；没有公共字母时输出空行。时间限制：2 秒。内存限制：64 MB。

## 输入

第一行为整数 `N`，随后两行分别给出两个字符串。

## 输出

输出一个最长公共子串；长度为零时输出空行。

## 评测方式

允许任意最优答案。检查输出是否同时出现在两个字符串中，且长度是否最大；存在并列答案时不必与样例相同。

## 样例

### 样例 1

输入:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

输出:

```
THEGREATALBANIA
```

## 解法

为第一个字符串建立后缀自动机。状态表示结束位置集合相同的子串，
保存最大长度、后缀链接和字符转移。逐字扩展时创建新状态；
若转移目标的长度过大，则通过克隆拆分类，并重定向相关转移。

扫描第二个字符串，维护已读前缀中也出现在第一个字符串内的最长后缀。
缺少转移时沿后缀链接缩短当前匹配，直到可以转移或到达根。
记录最大匹配长度及其结束位置即可恢复答案。每个公共子串都是某个已读前缀的后缀，
因此所求最大值最优。后缀链接降低匹配长度，每读一个字符最多增加一，扫描总成本为线性。

状态与转移数均为 `O(N)`。固定 26 字母下，构建和扫描时间、空间均为 `O(N)`。
简单原生版本保存完整转移行，简单 Python 使用字典。五份易读源码全部原样保留。

## 优化解法

优化版本用平坦数组只存已有转移：每个状态保存链表头，每条边保存字符、目标和下一边索引。
一次查询最多扫描 26 条边。克隆必须复制自己的边链表，避免后续重定向改变原状态。
在 `N ≤ 100000` 下，状态、边索引和长度均可用 32 位整数；
Python 使用紧凑整数数组，字符存入 bytearray。

这样去掉了完整的 26 列转移行及 Python 字典对象，后缀自动机不变量保持不变。
固定字母表下时间仍为 `O(N)`，但查询常数更大；空间仍为 `O(N)`，常数明显减小。
这主要是内存优化。

相对未修改的 Accepted 基础版本，实测内存下降：C++ 82.9%、Go 70.6%、Java 81.1%、Python 82.7%、Rust 81.0%。五种均按内存改善准入。Python 时间从 0.500 秒增至 1.312 秒，内存从 56240 降至 9736 KB；Go 时间也从 0.046 增至 0.078 秒。这是已通过评测的时间与空间权衡，不代表全面加速。排名快照：2026 年 11 月 2 日；星号表示仍未达到排名目标。

## 各语言说明

Python 在 5,760 对字符串上与独立二次复杂度最长公共子串 DP 比较。
还在 100,000 字符、字母表大小为 1、2、26 的字符串上检查了稀疏图结构。
五种实际程序提交前还各自在 Docker 中通过仓库的 13 组测试输入。
这些本地检查补充各自独立的 Accepted 记录。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB | 11287349 |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB | 11287350 |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB | 11287352 |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB | 11287351 |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB | 11287353 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures_optimized.cpp](1517_suffix_structures_optimized.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.062 s | 4968 KB | 11308174 |
| [1517_suffix_structures_optimized.go](1517_suffix_structures_optimized.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.078 s | 7356 KB | 11308176 |
| [1517_suffix_structures_optimized.java](1517_suffix_structures_optimized.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.156 s | 6652 KB | 11308178 |
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) \* | Python 3.12 x64 | suffix_structures | O(N) | AC | 1.312 s | 9736 KB | 11308173 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
