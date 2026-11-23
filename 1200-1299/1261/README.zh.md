# 1261. 小费

[Timus 1261](https://acm.timus.ru/problem.aspx?space=1&num=1261) · 难度 329 · number_theory

原题作者 Alexander Ipatov，出自 2003 年 10 月 11 日斯维尔德洛夫斯克州中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

钞票面额为 1, 3, 9, 27, … 特里特，客人每种面额恰有一张。账单为 N 特里特
（1 ≤ N ≤ 10⁷）。客人付一笔钱，找零归服务员作小费。只有当小费为正、且本身能用互不相同
的钞票凑出时，服务员才不会生气。求付款额和小费；付款额不能超过 4 294 967 291。任何
合法的一对都可接受；若无解，输出 0。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

付款额和小费。

## 评测方式

合法的组合很多，所以评测程序接受任意一对：付款额减小费必须等于 N，小费为正，付款额
不超过上限，并且两者的三进制表示只含数字 0 和 1。

## 样例

### 样例 1

输入：

```
5
```

输出：

```
9 4
```

## 解法

付款额 P 和小费 T 都是不同的 3 的幂之和，且 P − T = N。把 N 写成数字为 −1、0、1 的平衡
三进制：数字 1 组成 P，数字 −1 组成 T。从低位开始，余数 1 得到数字 1，余数 2 得到数字
−1 并向高位进一。

如果 N 的三进制中没有数字 2，就会得到 T = 0。这时取 P 中缺少的最小的 3 的幂，加到两个
和上：P 中的钞票仍互不相同，T 就是这一张钞票。所以答案总是存在，永远不会输出 0。P 小于
3¹⁶ ≈ 4.3 · 10⁷，远低于上限。`O(log N)`。

注意事项：

- 小费必须为正：N = 1 不能付 1、小费 0，4 3 是一个答案（测试 02）；
- 付款可能需要比 N 更大的钞票：N = 10⁷ 用 14 960 143 付款，小费 4 960 143（测试 03）；
- 付款和小费可以包含同一面额：小费只是一个能凑出的金额，而不是从客人那里拿走的钞票。

1 到 3000 的所有 N 以及最大的两个 N 都用评测程序检查过。

## 优化解法

Go 逐位处理平衡三进制，只保留剩余金额、当前幂、付款和小费。数字一将该钞票加入付款，数字二将它加入小费并向下一位进一。记录最小的未使用钞票，小费为零时可同时加入付款和小费，使小费为正。输入和十进制输出使用固定字节缓冲区，无需通用扫描器或数字格式化器。Go 直接访问标准输入和输出句柄。

已通过评测的基础实现 [1261_number_theory.cpp](1261_number_theory.cpp), [1261_number_theory.java](1261_number_theory.java), [1261_number_theory.py](1261_number_theory.py), [1261_number_theory.rs](1261_number_theory.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

`1261_number_theory_optimized.java`. Java 保留简单版本所述的算法和数据结构。固定字节缓冲区与 FastInput 替代 Scanner 及其正则表达式、区域设置处理。整数记号直接解析；需要字符串时仍进行 UTF-8 解码，十进制记号仍显式转换为数值。仅在需要前瞻时保存一个记号，输出算法不变。这样减少通用解析开销；表中列出算法工作量，输入扫描与字节数成正比，并使用有界输入缓冲区。

与 `1261_number_theory.java` 相比：时间 0.125 s → 0.109 s；内存 1612 KB → 472 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1261_number_theory_optimized.rs`. 保留原有算法及整数类型，直接转换十进制词元，避免通用字符串解析。负数按负值累积，因此最小有符号整数也不会在取绝对值时溢出。输入存储和算法复杂度不变。

Accepted #11328531 (Rust 1.75 x64): **0.015 s / 228 KB**. 历史对照: `1261_number_theory.rs` (Rust 1.75 x64) — 0.046 s / 232 KB (#11284140).

## 各语言说明

以下说明针对基础实现。

- 所有语言都在一个循环中求出平衡三进制的各位。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1261_number_theory.cpp](1261_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log N) | AC | 0.015 s | 128 KB | 11284132 |
| [1261_number_theory.go](1261_number_theory.go) | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 1068 KB | 11284133 |
| [1261_number_theory.java](1261_number_theory.java) | Java 1.8 | number_theory | O(log N) | AC | 0.125 s | 1612 KB | 11284139 |
| [1261_number_theory.py](1261_number_theory.py) | Python 3.12 x64 | number_theory | O(log N) | AC | 0.078 s | 432 KB | 11284137 |
| [1261_number_theory.rs](1261_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log N) | AC | 0.046 s | 232 KB | 11284140 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1261_number_theory_optimized.go](1261_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 308 KB | 11311230 |
| [1261_number_theory_optimized.java](1261_number_theory_optimized.java) | Java 1.8 | number_theory | O(log N) | AC | 0.109 s | 472 KB | 11324798 |
| [1261_number_theory_optimized.rs](1261_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(log N) | AC | 0.015 s | 228 KB | 11328531 |
