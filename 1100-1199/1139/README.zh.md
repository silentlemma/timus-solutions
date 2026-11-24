# 1139. 沿对角线飞越街道网格时经过的街区数

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · 难度 78 · number_theory

原题出自 2001 年 10 月 17–18 日在雷宾斯克举行的俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 条大道和 `M` 条街道（`1 < N, M < 32000`）把城市分成正方形街区。直升机
从西南角沿直线飞到东北角。求它飞越的街区数；街区是其正方形的开内部，
所以只碰到角不算。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `M`。

## 输出

街区数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
4 3
```

输出：

```
4
```

### 样例 2

输入：

```
3 3
```

输出：

```
2
```

## 解法

街区构成 `a × b` 的网格，`a = N − 1`，`b = M − 1`，飞行路线是它的对角线。
它先进入第一个街区，每穿过一条网格线就进入一个新街区。它穿过 `a − 1`
条内部竖线和 `b − 1` 条内部横线，但在网格的内部角点处会同时穿过各一条，
只进入一个新街区。对角线经过点 `(k·a/g, k·b/g)`，所以恰好遇到 `g − 1` 个
内部角点，其中 `g = gcd(a, b)`。总数为
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`。`O(log min(a, b))`。

注意事项：

- 输入给的是线的条数而不是街区数，各减一；
- 在正方形网格中，对角线经过沿途所有角点，只穿过 `a` 个街区；
- 只有一行或一列时，飞行会经过其中每个街区。

答案已对所有 `N, M ≤ 40` 以及所有测试，与按列精确取整统计对角线下街区数的
结果比对。

## 优化解法

`1139_number_theory_optimized.py`. 保留网格穿越公式 a+b-gcd(a,b)，a=N-1、b=M-1。用迭代欧几里得余数循环求 gcd，保留角点修正。O(log min(N,M)) 次有界整数步骤，额外状态 O(1)，不是新的几何算法。 内联 gcd 循环而不导入 math.gcd，直接解析两个字节记号。实测收益为评测内存更低，并不声称 Python 循环快于原生库。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1139_number_theory.py` 相比：时间 0.078 s → 0.125 s；内存 400 KB → 220 KB。

`1139_number_theory_optimized.rs`. 保留网格穿越公式 a+b-gcd(a,b)，a=N-1、b=M-1。用迭代欧几里得余数循环求 gcd，保留角点修正。O(log min(N,M)) 次有界整数步骤，额外状态 O(1)，不是新的几何算法。 迭代循环替代递归 gcd，直接数字输入输出去掉保留的输入 String。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1139_number_theory.rs` 相比：时间 0.015 s → 0.031 s；内存 248 KB → 56 KB。

优化的 Java 解法用 `System.in.read` 逐字节读取两个数，而不用 `Scanner`，并用循环
而不是递归计算最大公约数。公式相同；内存为 360 KB，而不是 1592 KB，时间
不变。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1139_number_theory_optimized.py`：在该可比样本中，时间名次 47/57，内存名次 1/57。

`1139_number_theory_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB | 11279432 |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB | 11279433 |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB | 11279436 |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB | 11279435 |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB | 11279438 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1139_number_theory_optimized.java](1139_number_theory_optimized.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.093 s | 360 KB | 11303570 |
| [1139_number_theory_optimized.py](1139_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log min(N,M)) | AC | 0.125 s | 220 KB | 11324847 |
| [1139_number_theory_optimized.rs](1139_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(log min(N,M)) | AC | 0.031 s | 56 KB | 11324856 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
