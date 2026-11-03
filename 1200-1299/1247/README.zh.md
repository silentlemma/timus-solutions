# 1247. 没有一段比它的长度加 N 更重

[Timus 1247](https://acm.timus.ru/problem.aspx?space=1&num=1247) · 难度 240 · bitmask, dp, prefix_sums

原题作者 Alexander Mironenko，出自 2003 年 3 月 1 日乌拉尔国立大学个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定正整数 `S, N ≤ 30000` 及 `S` 个整数 `0 ≤ A_i ≤ 100`，并保证 `sum(A_i) = S + N`。判断是否每个非空连续区间均满足 `A_i + … + A_j ≤ (j − i + 1) + N`。时间限制：0.5 秒；内存限制：64 MB。

## 输入

先给出 `S N`，随后 `S` 行，每行一个序列元素。

## 输出

所有区间均满足时输出大写 `YES`，否则输出 `NO`。

## 评测方式

精确比较答案词元。每个新源码有完整目标环境检查、独立数学比较及哈希绑定的自身Accepted；保留简单版本的各自测量。

## 样例

### 样例 1

输入：

```
4 3
2
3
0
2
```

输出：

```
YES
```

### 样例 2

输入：

```
4 5
1
0
5
3
```

输出：

```
NO
```

## 解法

每项减一，定义 `p_0 = 0`、`p_i = sum(A_1 − 1, …, A_i − 1)`。
总和保证给出 `p_S = N`，区间条件为 `p_j − p_(i−1) ≤ N`。

必要性：前缀也是区间，故 `p_i ≤ N`；其后的后缀同样是区间，
故 `N − p_i ≤ N`，得到 `p_i ≥ 0`。充分性：全部前缀均在 `[0, N]` 时，
任何区间之差至多 `N − 0 = N`。因此流式检查 `0 ≤ p_i ≤ N` 即可。
超过 `N` 的前缀本身违规，负前缀使剩余后缀过重，均可立即输出 `NO`。
该等价关系依赖题目的总和保证，不能推广到没有此保证的任意输入。

五份 `prefix_sums` 是首选简单版本：时间 `O(S)`，仅保存当前前缀，算法状态 `O(1)`。
Rust 另保留输入文本缓冲。所有旧 Accepted 源码逐字节保留：通用 Kadane
维护当前位置结尾的最大和 `ending = max(0, ending + A_i − 1)`，
将全局最大值与 `N` 比较；时间也为 `O(S)`，且不需要总和保证。

## 优化解法

保留旧动态规划及五种更简单的流式前缀基础，以后者比较。总和S+N保证条件等价于各p_i=sum(A_1..A_i)-i在[0,N]。C++保持该算法并用4096字节有界读缓冲和直接输出。Python用C实现的迭代器累积原和、减递增位置、再向下整除N+1。N>0时，整数p的p//(N+1)==0恰好等价于0<=p<=N，负数也成立。any寻找首个非零商，无Python逐元素循环或完整序列。O(S)时间、O(1)工作空间。Python基准是当前0.109s/328KB流式版，不是旧1312KB动态规划。

- `1247_prefix_sums_optimized.cpp`: 0.015 s / 64 KB; 基础 `1247_prefix_sums.cpp`: 0.031 s / 104 KB; 相对变化: 时间 -51.6%, 内存 -38.5%.
- `1247_prefix_sums_optimized.py`: 0.078 s / 416 KB; 基础 `1247_prefix_sums.py`: 0.109 s / 328 KB; 相对变化: 时间 -28.4%, 内存 +26.8%.

## 各语言说明

排名快照保存于 2026 年 11 月 2 日和 4 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1247_prefix_sums.cpp`; 覆盖源码 `1247_prefix_sums_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 75/75.

- Go: 首选教学基础 `1247_prefix_sums.go`; 覆盖源码 `1247_prefix_sums.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1247_prefix_sums.java`; 覆盖源码 `1247_prefix_sums.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 首选教学基础 `1247_prefix_sums.py`; 覆盖源码 `1247_prefix_sums_optimized.py`; 时间/内存名次 1/1, 其他作者记录 17/17.

- Rust: 首选教学基础 `1247_prefix_sums.rs`; 覆盖源码 `1247_prefix_sums.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums.cpp](1247_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(S) | AC | 0.031 s | 104 KB | 11308243 |
| [1247_prefix_sums.go](1247_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(S) | AC | 0.046 s | 1316 KB | 11308245 |
| [1247_prefix_sums.java](1247_prefix_sums.java) | Java 1.8 | prefix_sums | O(S) | AC | 0.109 s | 444 KB | 11308247 |
| [1247_prefix_sums.py](1247_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(S) | AC | 0.109 s | 328 KB | 11308241 |
| [1247_prefix_sums.rs](1247_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(S) | AC | 0.031 s | 468 KB | 11308248 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1247_dp.cpp](1247_dp.cpp) | G++ 13.2 x64 | dp | O(S) | AC | 0.031 s | 124 KB | 11283945 |
| [1247_dp.go](1247_dp.go) | Go 1.14 x64 | dp | O(S) | AC | 0.031 s | 1348 KB | 11283948 |
| [1247_dp.java](1247_dp.java) | Java 1.8 | dp | O(S) | AC | 0.109 s | 528 KB | 11283951 |
| [1247_dp.py](1247_dp.py) | Python 3.12 x64 | dp | O(S) | AC | 0.093 s | 1312 KB | 11283950 |
| [1247_dp.rs](1247_dp.rs) | Rust 1.75 x64 | dp | O(S) | AC | 0.062 s | 840 KB | 11283953 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums_optimized.cpp](1247_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.015 s | 64 KB | 11309382 |
| [1247_prefix_sums_optimized.py](1247_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.078 s | 416 KB | 11309921 |
