# 1729. 死人的宝箱

[Timus 1729](https://acm.timus.ru/problem.aspx?space=1&num=1729) · 难度 630 · geometry

原题作者 Fedor Fominykh（由 Denis Dublennykh 准备），出自 2009 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Jack 站在半径为 r、被丛林覆盖的圆形岛屿中心，只有到了岸边才能看到海。他的小船停在岸边某处，
从距离小船最近岸点不超过 a 度的岸点上才能看到它。求在最坏情况下能看到小船的路线的最短长度。

## 输入

r 和 a（1 ≤ r ≤ 1000，0.001 ≤ a ≤ 45），小数点后至多三位。

## 输出

最佳路线在最坏情况下的距离，小数点后至少六位。

## 样例

### 样例 1

输入：

```
1.000 30.000
```

输出：

```
6.0000000
```

## 解法

走到岸边需要 r。此后 Jack 到过的每个岸点能让他看到以该点为中心、宽 2a 度的弧，最坏情况下小船只在最后一个点才看到。
两个岸点之间最短的走法是弦；相邻点最多相隔 2a，而从第一个点到最后一个点绕岛扫过的角度至少为 360 − 2a，弧才能绕岛一圈闭合。

所以路线是 r 加上若干条弦，它们的角度之和为 360 − 2a，每个不超过 2a。角为 θ 的弦长 2r·sin(θ/2)，增长慢于 θ，
因此在总和固定时各段越不均匀总长越小：k − 1 条完整的 2a 弦（k = ⌊180/a⌋），再加一条余下 360 − 2ka 度的短弦，
当 2a 整除 360 时短弦为空。`O(1)`。

样例中 a = 30：六个点相隔 60°，五条长为 r 的弦，答案为 1 + 5 = 6。

注意事项：

- 用浮点数计算 ⌊180/a⌋ 可能少 1；各解答以千分之一度为单位精确读入 a。不过这种误差恰好给出相同的长度，
  因为少掉的完整弦会以一条 2a 的短弦补回来；
- a = 0.001 时路线有 179 999 条弦，所以总和用乘法计算，而不是逐条循环。

在 300 个随机数据上，答案与一个独立的已通过实现在全部七位输出数字上一致。

## 优化解法

C++ 版本使用 C 标准库进行输入和输出。输入角度最多有三位小数，乘以 1000 后取整即可恢复以千分之一度为单位的整数，再做除法和取余。弦长公式仍只需常数时间和空间。评测数据来自提交 11316978。

先把角度换算成千分之一度的整数，再计算完整弦的数量和余角。 Rust 1.75 x64（提交 11318489）的运行时间从 0.046 秒变为 0.031 秒，内存从 260 KB 变为 256 KB。

先把角度换算成千分之一度的整数，再计算完整弦的数量和余角。 Python 3.12 x64（提交 11318496）的运行时间从 0.109 秒变为 0.078 秒，内存从 464 KB 变为 520 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322451 · Rust 1.75 x64 №11321953 · Go 1.14 x64 №11322452 · Java 1.8 №11322453 · Python 3.12 x64 №11322454.

先把角度换算成千分之一度的整数，再计算完整弦的数量和余角。 Java 1.8（提交 11322411）的运行时间从 0.14 秒变为 0.125 秒，内存从 1800 KB 变为 392 KB。

Go 用弦长公式计算距离，然后从小缓冲区输出固定精度的结果。 Go 1.14 x64（提交 11322864）的运行时间从 0.031 秒变为 0.031 秒，内存从 1088 KB 变为 304 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1729_geometry_parsing_optimized.rs`. 用精确千分单位替代浮点输入转换，保留弦长公式及七位小数 C 输出。

Accepted #11328988 (Rust 1.75 x64): **0.015 s / 84 KB**. 历史对照: `1729_geometry_optimized.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11318489).

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1729_geometry_parsing_optimized.java`. 把有界小数输入按精确千分单位解析，保留弦长公式，直接输出七位小数，避免通用浮点输入输出转换。 把有界输入缓冲和解析方法直接放入 Main，去掉一个辅助类加载和分配。完整公式、输出精度及定点格式器保持不变。 独立程序完整写出答案后，先刷新两个输出流，再调用 Runtime.halt(0)。

Accepted #11329243 (Java 1.8): **0.078 s / 476 KB**. 历史对照: `1729_geometry_optimized.java` (Java 1.8) — 0.125 s / 392 KB (#11322411).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1729_geometry.cpp](1729_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB | 11322451 |
| [1729_geometry.go](1729_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11322452 |
| [1729_geometry.java](1729_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1800 KB | 11322453 |
| [1729_geometry.py](1729_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 464 KB | 11322454 |
| [1729_geometry.rs](1729_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB | 11321953 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1729_geometry_optimized.cpp](1729_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 136 KB | 11316978 |
| [1729_geometry_optimized.rs](1729_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB | 11318489 |
| [1729_geometry_optimized.py](1729_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 520 KB | 11318496 |
| [1729_geometry_optimized.java](1729_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 392 KB | 11322411 |
| [1729_geometry_optimized.go](1729_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 304 KB | 11322864 |
| [1729_geometry_parsing_optimized.rs](1729_geometry_parsing_optimized.rs) | Rust 1.75 x64 | geometry, parsing | O(1) | AC | 0.015 s | 84 KB | 11328988 |
| [1729_geometry_parsing_optimized.java](1729_geometry_parsing_optimized.java) | Java 1.8 | geometry, parsing | O(1) | AC | 0.078 s | 476 KB | 11329243 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
