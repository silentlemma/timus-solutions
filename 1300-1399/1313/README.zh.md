# 1313. 关于体育

[Timus 1313](https://acm.timus.ru/problem.aspx?space=1&num=1313) · 难度 34 · implementation

原题创意来自 Stanislav Vasiliev，由 Stanislav Vasiliev 和 Alexander Klepinin 准备，出自 2004 年 3 月 11–16 日在叶卡捷琳堡举行的第八届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一幅 N × N 的图像（N ≤ 100），按对角线输出它的像素：从左上角开始，一条对角线接一条对角线，每条从
左下端到右上端。顺序见样例。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后是 N 行，每行 N 个不超过 100 的正整数。

## 输出

按对角线顺序排列的 N² 个数，输出在一行中。

## 样例

### 样例 1

输入：

```
4
1 3 6 10
2 5 9 13
4 8 12 15
7 11 14 16
```

输出：

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
```

## 解法

第 s 条对角线由行号与列号之和为 s 的格子组成，s 从 0 到 2N − 2。从最低的格子往上走，就是让行号 i 从
min(s, N − 1) 递减到 max(0, s − N + 1)，列号为 s − i。`O(N²)`。

注意事项：

- 右下半部分的对角线较短，并且到不了第 0 行，所以下界是 max(0, s − N + 1)（测试 04）；
- N = 1 时只有一个像素（测试 02）。

## 优化解法

优化的 Java 解法用手工解析代替 `StringTokenizer`，把图像存放在一个扁平的 `byte`
数组中，因为每个数都不超过 100，并把数字逐位写入 1 KB 的输出缓冲区：392 KB，而不
是 1176 KB，时间不变。沿对角线的遍历不变。

优化的 Python 解法把最多为 100 的颜色值放在 `bytearray` 中，每种颜色的文本只生成
一次，并以字节构造答案：484 KB，而不是 1892 KB，时间不变。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1313_implementation_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328649 (Go 1.14 x64): **0.001 s / 1248 KB**. 历史对照: `1313_implementation.go` (Go 1.14 x64) — 0.046 s / 1352 KB (#11303290).

`1313_implementation_optimized.rs`. 保留原有算法及整数类型，直接转换十进制词元，避免通用字符串解析。负数按负值累积，因此最小有符号整数也不会在取绝对值时溢出。输入存储和算法复杂度不变。

Accepted #11328537 (Rust 1.75 x64): **0.015 s / 580 KB**. 历史对照: `1313_implementation.rs` (Rust 1.75 x64) — 0.031 s / 588 KB (#11284910).

## 各语言说明

- 除 C++ 以及优化的 Java 和 Python 解法外，数字都按文本原样搬运：从来不需要把它
  们当作整数。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1313_implementation.cpp](1313_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284904 |
| [1313_implementation.go](1313_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 1352 KB | 11303290 |
| [1313_implementation.java](1313_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.078 s | 1176 KB | 11284908 |
| [1313_implementation.py](1313_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 1892 KB | 11284907 |
| [1313_implementation.rs](1313_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 588 KB | 11284910 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1313_implementation_optimized.java](1313_implementation_optimized.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 392 KB | 11303592 |
| [1313_implementation_optimized.py](1313_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.062 s | 484 KB | 11303739 |
| [1313_implementation_optimized.go](1313_implementation_optimized.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1248 KB | 11328649 |
| [1313_implementation_optimized.rs](1313_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.015 s | 580 KB | 11328537 |
