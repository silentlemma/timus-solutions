# 1783. 核军备竞赛

[Timus 1783](https://acm.timus.ru/problem.aspx?space=1&num=1783) · 难度 473 · simulation

原题作者 Pavel Atnashev，出自第十五届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个国家计划在第 i 个月末恰好拥有 aᵢ 枚弹头。其对手从零开始，在第 i 个月初得知计划 aᵢ、…、aᵢ₊ₘ₋₁ 后，
选择最小的整数变化量 xᵢ，使得在接下来 m 个月中每月都把库存改变 xᵢ 时，每个月末都不低于计划。只执行本月的变化；下个月重新选择。输出 x₁、…、xₙ。

## 输入

n 和 m（1 ≤ n ≤ 10000，1 ≤ m ≤ 50），然后是 a₁、…、aₙ₊ₘ₋₁（0 ≤ aᵢ ≤ 10⁵）。

## 输出

x₁、…、xₙ。

## 样例

### 样例 1

输入：

```
4 3
0 0 4 2 1 0
```

输出：

```
2 1 1 -1
```

## 解法

第 i 个月初库存为 s 时，同样变化 x 持续 t 个月后库存为 s + t·x，它必须不小于 aᵢ₊ₜ₋₁。所以 x 是 t = 1…m 时 ⌈(aᵢ₊ₜ₋₁ − s)/t⌉ 的最大值。
然后库存增加 x，下个月重复。负数时也必须向上取整，而许多语言的整数除法会向零取整。`O(n·m)`。

样例中第一道命令要在三个月内达到 4：2。库存为 2 时，后面的计划 0、4、2 需要 ⌈2/2⌉ = 1；然后库存 3 时计划 4、2、1 需要 1；之后库存 4 时计划 2、1、0 允许 −1。

注意事项：

- 计划下降时命令可以为负；
- ⌈−3/2⌉ 等于 −1，而不是 −2 也不是 0，所以除法必须显式向上取整；
- 每次只执行所计划月份中的第一个月。

在 60 个随机情形上（从几个月到 10000 个月，计划为随机、波浪形或稀疏尖峰），答案与一个独立的已通过实现一致。

## 优化解法

仅格式化且已接受的版本：`1783_simulation.java` #11327472, `1783_simulation.cpp` #11327473, `1783_simulation.py` #11327474, `1783_simulation.rs` #11327475。每行表格使用该精确文件自身成对的时间/内存，不将性能变化归因于格式化。

`1783_simulation_optimized.cpp`. 保留最多 50 项未来计划环上带符号向上取整的精确最大值。仅在 delta>best*t 时执行 delta/t 除法；best 为整数时，这与 ceil(delta/t)>best 等价，包括负 delta。非负值用 (delta+t-1)/t，负值向零截断。计划与库存在 0..100000、t<=50，best*t 适合有符号 int。各 16 KiB 输入/输出缓冲，算法仍为 O(nm) 时间、O(m) 计划空间。

精确源代码 G++ 13.2 x64 Accepted #11326998：0.015 s / 104 KB。2026-11-20 保存比较中时间 1/43、内存 1/43，两项均前十，无需星号。低于 1024 KB 时严格收录只看时间。此前优化运行 #11315303：0.031 s / 88 KB；这些是独立运行各自成对的指标，新记录内存更高。保留的 C++ 教学版自身当前 Accepted #11327473 为 0.031 s / 264 KB，算法未变。

C++/Go 保留原有 m 个带符号向上取整的精确最大值，改用至多50整数的环形前瞻窗口。先读 m 项，每次实际调整后以新计划替换过期槽并前移，始终对应当前窗口。遍历以边界检查回绕，不逐项取余。非负 delta 用 (delta+t−1)/t，负数向零截断就是向上取整。计划与库存保持0…100000，32位有符号足够。时间 O(nm)，计划空间从 O(n+m) 降至 O(m)，输入输出有界。保留普通文件；Java、Python、Rust 复用符合标准的基础版。

保留的 Accepted 教学源代码 [1783_simulation.java](1783_simulation.java), [1783_simulation.py](1783_simulation.py), [1783_simulation.rs](1783_simulation.rs) 在保存比较中满足所需指标的严格前十或前 15% 标准。表中为当前精确成对测量，包括仅格式化的版本。算法未变，不增加相同优化副本；星号表示单独语言排名目标。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1783_implementation_parsing_optimized.rs`. 环中仅保存 m 个前瞻值，按月份逻辑顺序扫描两段连续区间，再用下一需求替换最旧值。即使变化为负也保留精确向上取整，直接流式输出订单，存储从完整输入输出降为 O(m)。 按实际答案类型专门化直接输出，避免通用格式分派和临时答案字符串。固定文本采用原生写出，数字输出精确处理所需有符号或无符号值。数学判定及归档简单版本保留。

Accepted #11329204 (Rust 1.75 x64): **0.015 s / 72 KB**. 历史对照: `1783_simulation.rs` (Rust 1.75 x64) — 0.031 s / 828 KB (#11327475).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1783_simulation.cpp](1783_simulation.cpp) | G++ 13.2 x64 | simulation | O(n m) | AC | 0.031 s | 264 KB | 11327473 |
| [1783_simulation.go](1783_simulation.go) | Go 1.14 x64 | simulation | O(n m) | AC | 0.031 s | 1384 KB | 11289783 |
| [1783_simulation.java](1783_simulation.java) | Java 1.8 | simulation | O(n m) | AC | 0.14 s | 2388 KB | 11327472 |
| [1783_simulation.py](1783_simulation.py) | Python 3.12 x64 | simulation | O(n m) | AC | 0.187 s | 2584 KB | 11327474 |
| [1783_simulation.rs](1783_simulation.rs) | Rust 1.75 x64 | simulation | O(n m) | AC | 0.031 s | 828 KB | 11327475 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1783_simulation_optimized.cpp](1783_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n·m) | AC | 0.015 s | 104 KB | 11326998 |
| [1783_simulation_optimized.go](1783_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(n·m) | AC | 0.031 s | 300 KB | 11315305 |
| [1783_implementation_parsing_optimized.rs](1783_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(nm) time; O(m) space + bounded I/O buffers | AC | 0.015 s | 72 KB | 11329204 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
