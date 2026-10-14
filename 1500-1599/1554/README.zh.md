# 1554. 积性函数

[Timus 1554](https://acm.timus.ru/problem.aspx?space=1&num=1554) · 难度 640 · number_theory

原题出自 2007 年 9 月彼得罗扎沃茨克集训的 Novosibirsk SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定积性函数 F 的前 N 个值（N ≤ 10⁴），其值取模 2007。求它在狄利克雷卷积下的逆 G 的前 N 个
值，其中 (F * G)(n) = Σ F(n/d)·G(d)，d 取遍 n 的约数，要求它在 n = 1 时为 1，其余为 0。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后是 F(1), …, F(N)。

## 输出

在一行中输出 G(1), …, G(N)。

## 样例

### 样例 1

输入:

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

输出:

```
1 2006 2006 0 2006 1 2006 0 0 1 2006 0 2006 1 1 0
```

## 解法

n = 1 时条件为 F(1)·G(1) = 1。n > 1 时得到 F(1)·G(n) = −Σ F(n/d)·G(d)，d 取遍 n 的真约数，
都小于 n。积性的 F 满足 F(1) = 1；解法仍通过模 2007 的逆元除以 F(1)，这不费任何代价。

于是像筛法一样按递增顺序填写 G：一旦 G(d) 已知，就对每个 k ≥ 2 且 d·k ≤ N 的倍数把
F(k)·G(d) 加到它的累加器上；循环到达 n 时，其累加器中已是真约数上的全部和。共
N/1 + N/2 + … ≈ N ln N 步，约 10⁵。结果已按定义直接验证。

注意事项：

- 2007 = 9·223 不是素数，所以 −1 写作 2006，求逆要用扩展欧几里得算法或库函数；
- 处处为 1 的函数的逆是莫比乌斯函数（测试 01），恒等函数的逆是 n·μ(n)（测试 03），刘维尔函
  数的逆是 |μ|（测试 04）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1554_number_theory.cpp](1554_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.015 s | 280 KB |
| [1554_number_theory.go](1554_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 1680 KB |
| [1554_number_theory.java](1554_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 1156 KB |
| [1554_number_theory.py](1554_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.093 s | 2632 KB |
| [1554_number_theory.rs](1554_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 936 KB |
