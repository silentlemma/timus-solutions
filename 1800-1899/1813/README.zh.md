# 1813. 随机播放器

[Timus 1813](https://acm.timus.ru/problem.aspx?space=1&num=1813) · 难度 1570 · number_theory

原题出自 Tavrida NU Akai Contest，2010 年 8 月彼得罗扎沃茨克夏季集训。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

序列 x₀ = 0，xᵢ = (a·xᵢ₋₁ + b) mod m 必须在前 m 项中把 0 到 m − 1 的每个数恰好经过一次，并回到 0。对所有满足条件的 (a, b)（0 ≤ a, b < m），求 a 的平均值并向下取整。

## 输入

至多 100 行，每行一个 m（1 < m < 10⁹）。

## 输出

对每个 m 输出向下取整的平均值。

## 样例

### 样例 1

输入：

```
2
36
100
123
```

输出：

```
1
13
41
1
```

## 解法

序列必须是长度为 m 的单个循环，即线性同余发生器的满周期。由 Hull–Dobell 定理，这恰好在以下条件成立时发生：b 与 m 互质，a − 1 能被 m 的每个素因子整除，
并且当 m 能被 4 整除时 a − 1 也能被 4 整除。所以令 c 为 m 的不同素因子之积（当 4 | m 时再乘 2），好的 a 就是 1、1 + c、1 + 2c、… 中小于 m 的，
共 m/c 个（c 整除 m）。好的 b 的个数与 a 无关，所以对所有组合的平均值就是这个等差数列的平均值 (m − c + 2)/2。对 m 试除到 √m 进行分解，每个值 `O(√m)`。

对于 m = 36 = 2²·3²，c = 2·3·2 = 12，a 为 1、13 或 25，平均值为 13。对于 m = 123 = 3·41，c = 123，只有 a = 1 可行。

注意事项：

- 4 的倍数需要额外的因子 2：m = 4 时 a = 3 不行；
- 对组合的平均等于对 a 的平均，仅仅因为每个好的 a 拥有相同数量的好的 b；
- a = 0 永远不行，因为此时序列一直重复 b。

对 2 到 60 的所有 m，答案与对全部 (a, b) 的完整模拟一致；在随机值、小素数之积、大素数及其平方上，与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1813_number_theory.cpp](1813_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(m)) per value | AC | 0.015 s | 128 KB |
| [1813_number_theory.go](1813_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 1104 KB |
| [1813_number_theory.java](1813_number_theory.java) | Java 1.8 | number_theory | O(sqrt(m)) per value | AC | 0.078 s | 528 KB |
| [1813_number_theory.py](1813_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(m)) per value | AC | 0.093 s | 704 KB |
| [1813_number_theory.rs](1813_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 232 KB |
