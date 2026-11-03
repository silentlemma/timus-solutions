# 1523. K-逆序

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · 难度 296 · fenwick

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 1 … n 的一个排列 a1, …, an（1 ≤ n ≤ 20000），统计它的 k-逆序（2 ≤ k ≤ 10）：满
足 ai1 > ai2 > … > aik 的下标序列 i1 < i2 < … < ik。输出数目模 10⁹。

时间限制：1 秒。内存限制：64 MB。

## 输入

n 和 k，然后是排列。

## 输出

k-逆序的数目模 10⁹。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入:

```
3 2
3 1 2
```

输出:

```
2
```

### 样例 2

输入:

```
5 3
5 4 3 2 1
```

输出:

```
10
```

## 解法

设 ends[i] 为在位置 i 结束的长度为 L 的递减序列数；L = 1 时处处为 1。在 i 结束的长
度为 L + 1 的序列，是在更早位置 p（ap > ai）结束的长度为 L 的序列后面接上 i。所以每
一层是一次从左到右的扫描，用按值的树状数组：查询大于 ai 的值的和，再在 ai 处加上
ends[i]。把值从大到小编号，“大于”就变成前缀。k − 1 次扫描，共 `O(n·k·log n)`。

注意事项：

- k 可能超过最长递减序列的长度，甚至超过 n，这时答案为 0（测试 04、05、gen3）；
- 数目增长如 C(20000, 10)，所以累加时要取模 10⁹（gen2、gen5）。

## 优化解法

分层逆序 DP 原地使用一个数组。处理位置时先保存旧层值，查询只含更早旧层位置的 Fenwick 树，覆盖数组，再插入保存的旧值。插入新值会混合层次，导致错误。下一层清空复用树。余数和坐标有界，可用紧凑存储；两个余数之和用条件减法代替除法。

- `1523_fenwick_optimized.cpp`: 0.015 s / 192 KB; 基础版 `1523_fenwick.cpp`: 0.031 s / 596 KB; 相对基础版的变化: 时间 -51.6%, 内存 -67.8%.
- `1523_fenwick_optimized.java`: 0.140 s / 624 KB; 基础版 `1523_fenwick.java`: 0.125 s / 3512 KB; 相对基础版的变化: 时间 +12.0%, 内存 -82.2%.
- `1523_fenwick_optimized.py`: 0.859 s / 2000 KB; 基础版 `1523_fenwick.py`: 0.562 s / 5172 KB; 相对基础版的变化: 时间 +52.8%, 内存 -61.3%.
- `1523_fenwick_optimized.rs`: 0.031 s / 472 KB; 基础版 `1523_fenwick.rs`: 0.031 s / 1292 KB; 相对基础版的变化: 时间 -0.0%, 内存 -63.5%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1523_fenwick.cpp`; 覆盖实现 `1523_fenwick_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 95/95.

- Go: 优先教学基础版 `1523_fenwick.go`; 覆盖实现 `1523_fenwick.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1523_fenwick.java`; 覆盖实现 `1523_fenwick_optimized.java`; 时间/内存名次 4/1, 其他作者记录 5/5.

- Python/PyPy: 优先教学基础版 `1523_fenwick.py`; 覆盖实现 `1523_fenwick_optimized.py`; 时间/内存名次 7/1, 其他作者记录 7/7.

- Rust: 优先教学基础版 `1523_fenwick.rs`; 覆盖实现 `1523_fenwick_optimized.rs`; 时间/内存名次 2/1, 其他作者记录 2/2.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB | 11287382 |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB | 11287383 |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB | 11287388 |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB | 11287386 |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB | 11287389 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1523_fenwick_optimized.cpp](1523_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(NK log N) | AC | 0.015 s | 192 KB | 11309407 |
| [1523_fenwick_optimized.java](1523_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(NK log N) | AC | 0.140 s | 624 KB | 11309408 |
| [1523_fenwick_optimized.py](1523_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(NK log N) | AC | 0.859 s | 2000 KB | 11309406 |
| [1523_fenwick_optimized.rs](1523_fenwick_optimized.rs) \* | Rust 1.75 x64 | fenwick | O(NK log N) | AC | 0.031 s | 472 KB | 11309409 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
