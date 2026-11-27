# 1090. 跳得最多的一排新兵：统计逆序对

[Timus 1090](https://acm.timus.ru/problem.aspx?space=1&num=1090) · 难度 366 · fenwick, binary_search

原题作者 Nikita Shamgunov，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `K` 排（`1 ≤ K ≤ 20`），每排 `N` 名新兵（`2 ≤ N ≤ 10000`），按身高从 1（最高）到 `N` 编号；每排是 `1 … N` 的
一个排列。每名新兵对站在他前面、编号比他大的每个人各跳一次。输出总跳跃次数最多的那一排；相同时输出编号最小的。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

`N` 和 `K`，然后 `K` 行，每行 `N` 个数。

## 输出

排的编号。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
3 3
1 2 3
2 1 3
3 2 1
```

输出：

```
3
```

## 题解

一排的总跳跃次数就是排列的逆序对数：满足 `i < j` 且 `a[i] > a[j]` 的位置对。`N = 10000` 时二重循环太慢，所以在
读入这一排时边读边统计。位置 `i` 上的新兵 `x` 前面有 `i` 个人，其中编号比他小的人数是在编号 `1 … N` 上建立的
树状数组中的前缀和；`x` 的跳跃次数就是 `i` 减去这个数。然后把 `x` 加入树中。`O(K · N log N)`。

教学 Python 把之前的值保持有序。bisect 返回插入下标，所以
i-index 个之前的值更大，贡献相应逆序对；list.insert 再移动后缀
保持排序。同一行元素互异。二分 O(log N)，但每次移动 O(N)，
K 行共 O(K N^2) 时间。当前行列表/切片占 O(N) 个工作字；这个
具体实现还保留全部 O(KN) 个解析输入整数，需与工作状态分开计算。

注意事项：

- 最大 N(N-1)/2=49 995 000 放得进有符号 32 位。教学
  C++/Go/Java/Rust 用 64 位总数；优化 C++ 用 int、优化 Go 用
  原生 int，在此界内安全。Python 整数无界。
- 相同时取第一排，所以只有严格更大的总数才替换当前最优；
- 每一排都要清空树状数组。

答案与用归并排序统计逆序对的结果做了核对，`N ≤ 300` 时还与二重循环做了核对。

## 优化解法

C++ 和 Go 版本保留树状数组算法，并用固定大小的缓冲区读取输入。树中的每个计数不超过 N，可用 16 位存储。PyPy 版本以树状数组替代有序列表，前缀查询和插入均需 O(log N)。这三个版本的时间复杂度均为 O(K·N log N)，额外空间均为 O(N)。

当前缓存确认简单 Java 低于 1 MiB，仅按时间名次准入。简单 Rust
未过精确编译器小样本参考所需两项；独立优化 Rust 低于 1 MiB，
按时间参考合格。优化 C++ 用时间名次，Go 用小样本时间参考，
PyPy 需要且通过两项普通名次。使用统一
[排名标准](../../RATING_CRITERIA.md)，保留全部教学源码，
复用合格文件而不复制。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1090_fenwick_implementation_optimized.rs`. 通过有界原生字节缓冲读取词元，短词元内联保存，仅长词元分配额外空间。十进制转换保留有符号边界，不保存完整命令输入。 C 入口直接调用求解函数，返回前刷新 Rust 输出；保留普通入口的原实现。

Accepted #11328959 (Rust 1.75 x64): **0.015 s / 224 KB**. 历史对照: `1090_fenwick.rs` (Rust 1.75 x64) — 0.015 s / 2120 KB (#11279090).

当前 1090_fenwick_implementation_optimized.rs 仅为原有 32 字节
内联记号容量命名。Accepted #11328959（0.树状数组算法、
基础源码和实质注释不变。

## 各语言说明

教学 Python 版本使用有序列表和二分查找，并在 PyPy 3.10 下通过评测。同一源文件在 CPython 3.12 下于测试 9 超时（0.515 秒）。优化 Python 版本使用树状数组，同样在 PyPy 3.10 下通过。表格记录每个已通过提交实际使用的解释器。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB | 11279088 |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB | 11279084 |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB | 11279085 |
| [1090_fenwick.java](1090_fenwick.java) | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB | 11279089 |
| [1090_fenwick.rs](1090_fenwick.rs) | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB | 11279090 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1090_fenwick_optimized.cpp](1090_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 104 KB | 11310324 |
| [1090_fenwick_optimized.go](1090_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.031 s | 816 KB | 11310344 |
| [1090_fenwick.py](1090_fenwick.py) | PyPy 3.10 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 9076 KB | 11310319 |
| [1090_fenwick_implementation_optimized.rs](1090_fenwick_implementation_optimized.rs) | Rust 1.75 x64 | fenwick, implementation | O(K·N log N) | AC | 0.015 s | 232 KB | 11331115 |
