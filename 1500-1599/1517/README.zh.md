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

`1517_suffix_structures_optimized.py`. 保留后缀自动机，为至多 2N+1 个状态各分配一行 26 个有符号 32 位转移下标；长度与后缀链接也用紧凑整数数组。克隆先复制转移行再重定向链接。无需边链表扫描和 Python 字典，但每状态预留全部 26 格。扫描第二串时沿后缀链接回退，输出任一最长公共子串。长度 N、M 下时间 O(26N+M)，状态 O(26N) 加两条输入串；保留字典教学版。

精确源代码 PyPy 3.10 Accepted #11326700：0.234 s / 25000 KB。2026-11-20 保存的当前编译器比较：时间排名 1/32，内存排名 9/32。两项必需指标均通过严格前十或前 15%（百分比界限向上取整）。星号表示 Python 单独的双指标第一名目标。

此前记录的优化提交 #11308173（Python 3.12 x64）为 1.312 s / 9736 KB。当前 PyPy 3.10 记录时间更低、内存更高。这是不同评测运行的成对测量，比较包含解释器选择及运行波动。

- `1517_suffix_structures_optimized.py`: 0.234 s / 25000 KB; 保留教学基础版 `1517_suffix_structures.py` (Python 3.12 x64): 0.5 s / 56240 KB.

优化 C++、Go、Java、Rust 保留稀疏转移数组：每状态一个表头，每边保存字符、目标及下一边下标。查找最多扫 26 条边；克隆在重定向前复制自己的边表。N<=100000 下索引和长度为 32 位。固定字母表下这四版工作、空间 O(N)，内存常数更小。表保留此前 Accepted 及 2026 年 11 月 2 日比较；Go 为 0.078 s，对比基础 0.046 s，体现时间/空间权衡。

相对表中基础版的实测内存下降：C++ 82.9%, Go 70.6%, Java 81.1%, Python 55.5%, Rust 81.0%.

## 各语言说明

当前 Python 程序在 CPython 3.12、PyPy 3.10 各通过 58 个本地输入后获得自身 Accepted。上文说明密集转移表示，表记录接受的 PyPy 运行。

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
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) | PyPy 3.10 x64 | suffix_structures | O(26N+M) time; O(26N+M) space | AC | 0.234 s | 25000 KB | 11326700 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |
