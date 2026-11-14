# 1554. 积性函数

[Timus 1554](https://acm.timus.ru/problem.aspx?space=1&num=1554) · 难度 639 · number_theory

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
O(N log N) 步，约 10⁵。结果已按定义直接验证。

注意事项：

- 2007 = 9·223 不是素数，所以 −1 写作 2006，求逆要用扩展欧几里得算法或库函数；
- 处处为 1 的函数的逆是莫比乌斯函数（测试 01），恒等函数的逆是 n·μ(n)（测试 03），刘维尔函
  数的逆是 |μ|（测试 04）。

## 优化解法

每次更新都对 2007 取模，因此数组中只保存 0 到 2006 的数，16 位就足够。取模前用更宽的整数类型进行乘法。系数为零时对后续倍数没有贡献，可以跳过这些更新。

Go 提交 11317288 耗时 0.031 秒，使用 968 KB；基础版耗时 0.031 秒，使用 1676 KB。

Rust 提交 11317290 耗时 0.015 秒，使用 240 KB；基础版耗时 0.015 秒，使用 940 KB。

Java 提交 11317291 耗时 0.109 秒，使用 528 KB；基础版耗时 0.109 秒，使用 1152 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11321745 · Go 1.14 x64 №11322093 · Java 1.8 №11322412 · Python 3.12 x64 №11321746 · Rust 1.75 x64 №11322455.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1554_number_theory.cpp](1554_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.015 s | 264 KB | 11321745 |
| [1554_number_theory.go](1554_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 1676 KB | 11322093 |
| [1554_number_theory.java](1554_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 1152 KB | 11322412 |
| [1554_number_theory.py](1554_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.109 s | 2636 KB | 11321746 |
| [1554_number_theory.rs](1554_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 940 KB | 11322455 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1554_number_theory_optimized.go](1554_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 968 KB | 11317288 |
| [1554_number_theory_optimized.rs](1554_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 240 KB | 11317290 |
| [1554_number_theory_optimized.java](1554_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 528 KB | 11317291 |

\* Go 仍有提升排名的空间。 Rust 仍有提升排名的空间。 Java 仍有提升排名的空间。
