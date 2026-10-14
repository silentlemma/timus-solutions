# 1528. 数列

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · 难度 272 · math

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

f(1) = g(1) = 1，f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1)，
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)²。对至多 5000 组数据
（1 ≤ n ≤ 10000，2 ≤ p ≤ 2·10⁹）输出 f(n) mod p。

时间限制：3 秒。内存限制：64 MB。

## 输入

每行一对 n 和 p，以 0 0 结束。

## 输出

每组数据的 f(n) mod p。

## 样例

### 样例 1

输入:

```
1 2
2 11
0 0
```

输出:

```
1
2
```

## 解法

两个数列都有闭式。若对 i < n 有 g(i) = i，则 g(n) = 1 + (n − 1)n − (n − 1)² = n。于
是 f(n) − f(n − 1) = f(n − 1)·(n − 1)，即 f(n) = n·f(n − 1) = n!。所以每组数据求的是
n! mod p。当 n ≥ p 时 p 本身就是一个因子，答案为 0。否则一路乘到 n 并随时取模；乘积小
于 2·10¹³，在 64 位范围内。所有数据合计至多 5·10⁷ 次乘法，编译型语言很快。Python 中
朴素循环约需 6 秒，所以 Python 解法把每个 100 的倍数的阶乘精确地存为大整数，对其中一
个取模，再乘上至多 99 个因子。

注意事项：

- 公式看起来复杂，其实 g(n) = n、f(n) = n!（所有测试）；
- n ≥ p 时答案直接为 0（测试 02、gen3）；
- p 可达 2·10⁹，乘积需要 64 位（测试 03、gen1）；
- 略大于 n 的质数 p 是很好的检验：由威尔逊定理 (p − 1)! ≡ −1（测试 05）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n) per case | AC | 0.359 s | 17900 KB |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB |
