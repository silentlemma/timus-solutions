# 1747. 巡视领地

[Timus 1747](https://acm.timus.ru/problem.aspx?space=1&num=1747) · 难度 1366 · combinatorics

原题作者 Artyom Ripatti，出自 2009 年 8 月彼得罗扎沃茨克夏季集训的乌法国立航空技术大学专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个城市两两之间都有一条道路。国王从首都出发，必须恰好访问每个城市两次，然后回到首都。求可能路线数对 p 取模的结果。

## 输入

n 和 p（3 ≤ n ≤ 10⁵，1 ≤ p ≤ 10⁹ + 7）。

## 输出

路线数对 p 取模。

## 样例

### 样例 1

输入：

```
3 123
```

输出：

```
2
```

### 样例 2

输入：

```
4 123
```

输出：

```
30
```

## 解法

首都在开头和结尾各访问一次，所以中间的路线是一个单词：其余 m = n − 1 个城市各出现两次，且没有城市紧跟着自己，
因为道路连接的是两个不同的城市。对相邻成对的情况做容斥，得到这种单词的个数

a(m) = Σ (−1)^k C(m, k) (2m − k)! / 2^(m − k)，

但 p 不一定是质数，模 p 下不一定能做除法。同样的数满足

a(m) = m(2m − 1)·a(m − 1) + m(m − 1)·a(m − 2)，a(0) = 1，a(1) = 0，

它只需要乘法，所以对任意 p 都能在 `O(n)` 步内得到答案。

当 n = 4 时其余城市有三个，单词共 30 个，例如 `ABCABC` 和 `ABACBC`。

注意事项：

- p 可以是 1、偶数或任意合数，因此不能用模逆元；
- m(2m − 1) 可达 2·10¹⁰，所以在下一次乘法前先对 p 取模，以保持在 64 位以内。

对所有不超过 59 的 m 以及 m = 100、250、500、1000、1500，递推式与容斥求和用精确整数算出的结果相同。
在 68 个测试上，答案也与一个独立的已通过实现（它把 p 分解为素数幂）一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1747_combinatorics.cpp](1747_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 384 KB |
| [1747_combinatorics.go](1747_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.031 s | 1080 KB |
| [1747_combinatorics.java](1747_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 1592 KB |
| [1747_combinatorics.py](1747_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.140 s | 376 KB |
| [1747_combinatorics.rs](1747_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 244 KB |
