# 1456. 绝地之谜 2

[Timus 1456](https://acm.timus.ru/problem.aspx?space=1&num=1456) · 难度 746 · number_theory

原题作者 Ilya Grebnov、Dmitry Kovalioff 与 Nikita Rybak，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 A 和 N（2 ≤ A < N ≤ 10⁹），依次计算余数 Z[1] = A mod N，
Z[i + 1] = Z[i] · A mod N。求使 Z[X] = 1 的最小正整数 X，即满足
A^X ≡ 1 (mod N) 的最小 X；若不存在，输出 0。

时间限制：0.25 秒。内存限制：64 MB。

## 输入

A 和 N。

## 输出

X，或 0。

## 样例

### 样例 1

输入:

```
7 20
```

输出:

```
4
```

余数依次是 7、9、3 和 1。

## 解法

若 A 与 N 有大于 1 的公因数，每个余数都保留这个因数，永远不会变成 1，所以答案是 0。否则
X 是 A 模 N 的乘法阶，由欧拉定理它整除 φ(N)。用试除法（到 √N）分解 N 得到
φ(N)，同样分解 φ(N)，从 x = φ(N) 开始：对 φ(N) 的每个质因数 p，只要 A^(x / p)
模 N 仍为 1，就把 x 除以 p。最后剩下的就是阶，因为幂模 N 等于 1 的指数总是阶的倍数。所有
乘积都小于 10¹⁸，所以 64 位整数加快速幂就足够了。`O(√N + log² N)`。

注意事项：

- A 与 N 有公因数，包括 A 和 N 都是偶数（测试 02、08、11）；
- 阶接近 N 时逐个模拟余数太慢（测试 13）；
- A = N − 1 的阶是 2（测试 04、10）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1456_number_theory.cpp](1456_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 192 KB |
| [1456_number_theory.go](1456_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 1072 KB |
| [1456_number_theory.java](1456_number_theory.java) | Java 1.8 | number_theory | O(sqrt N + log^2 N) | AC | 0.140 s | 1628 KB |
| [1456_number_theory.py](1456_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.078 s | 472 KB |
| [1456_number_theory.rs](1456_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.015 s | 232 KB |
