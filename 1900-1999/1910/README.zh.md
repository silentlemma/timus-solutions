# 1910. 和最大的连续三项

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

原题作者 Denis Dublennykh，比赛 NEERC 2012, Eastern subregional contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定正数序列，找出和最大的连续三个元素。输出该和以及中间元素从一开始
的下标。保证取得最大和的三元组唯一。时间限制 1 秒，内存限制 64 MB。

## 输入

先给 n，3≤n≤1000，再给 n 个整数 aᵢ，1≤aᵢ≤10⁶。
空格或换行均可作为分隔符。

## 输出

最大和，以及中间元素从一开始的下标。

## 评测方式

两个精确整数，按标记比较。

## 样例

```
6
1 4 4 4 1 1
```

```
12 3
```

## 解法

把第二节到倒数第二节依次当作三节中间的一节：把它和两个邻居相加，记下最大的和
以及它的编号。题目保证最优的三节唯一，所以用严格比较即可。`O(n)`；和不超过
3·10⁶，32 位整数放得下。

注意事项：

- 答案是中间一节的编号，从 1 开始计数；
- n = 3 时只有一组三节。

## 优化解法

`1910_implementation_optimized.java`. Java 保留滑动三元组最大值。只保存前两个值，读入新值后求和，严格变大时更新最优和及从一开始的中间位置。题目保证最大值唯一，因此严格比较足够。和至多 3000000，可用 int。固定字节输入与直接数字输出避免 Scanner、字符串拼接和通用整数格式化，不保存整个序列。时间 O(N)，辅助空间 O(1)。

精确源代码 Java 1.8 Accepted #11327450：0.078 s / 356 KB。2026-11-20 保存的编译器组比较：时间 1/532、内存 2/532。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11303787 为 0.125 s / 380 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1910_implementation_optimized.java`: 0.078 s / 356 KB; 保留教学基础版 `1910_implementation.java`: 0.156 s / 2372 KB.

优化的 C++ 解法不保存各节：它用 `scanf` 逐个读入，只记住当前一节之前的两节，三节
之和只需要这些：128 KB，而不是 192 KB，时间不变。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1910_implementation_optimized.rs`. C 入口直接调用求解函数，返回前刷新 Rust 输出；保留普通入口的原实现。

Accepted #11328940 (Rust 1.75 x64): **0.015 s / 136 KB**. 历史对照: `1910_implementation.rs` (Rust 1.75 x64) — 0.031 s / 236 KB (#11303334).

## 各语言说明

没有特别需要注意的地方。

读取序列时维护三个值的窗口，记录首次达到最大值的位置。通过的提交 11324269 用时 0.140 秒、占用 240 KB；简单版用时 0.062 秒、占用 452 KB。记录的运行时间高于简单版。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327450 |
| [1910_implementation_optimized.py](1910_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) | AC | 0.140 s | 240 KB | 11324269 |
| [1910_implementation_optimized.rs](1910_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 136 KB | 11328940 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
