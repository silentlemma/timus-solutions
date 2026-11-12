# 1430. 罪与罚

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · 难度 461 · number_theory

原题作者 Nikita Rybak、Ilya Grebnov 与 Dmitry Kovalioff，出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

商品单价为 A 或 B，每种可以买任意多件，可花的钱为 N（1 ≤ A, B, N ≤ 2·10⁹）。求
x 和 y，使 x·A + y·B ≤ N 且尽量大；任何最优的一对都可以。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

A、B 和 N。

## 输出

x 和 y。

## 样例

### 样例 1

输入:

```
8 5 22
```

输出:

```
2 1
```

## 解法

设 A ≥ B（否则交换两者，最后再把答案换回来）。若 x ≥ B，则可以把 B 件单价 A 的
商品换成 A 件单价 B 的商品，总价不变，所以存在 x < B 的最优答案；又由 x·A ≤ N
得 x ≤ N / A。于是 x 从 0 取到 min(N / A, B − 1)，对每个 x，剩下的钱买
y = (N − x·A) / B 件单价 B 的商品。因为 A ≥ B，要么 B ≤ √N，要么 N / A < √N，所以
x 至多约 44 722 个值；一旦恰好花完 N，循环立即停止。`O(√N)`。

注意事项：

- x·A 这样的乘积可用 32 位有符号整数表示（测试 03、06）；
- 若两个价格都大于 N，就什么也不买（测试 12）；
- 答案不唯一，所以测试使用检查器（测试 02）。

## 优化解法

新的 C++、Go、Rust 保留有界购买枚举。令 A≥B、g=gcd(A,B)，B/g 件 A 价商品可等价替换为 A/g 件 B 价商品，因此只需 0≤x≤min(floor(N/A),B/g−1)。未花金额 r=(N−xA) mod B 从 N mod B 开始，每步减 A mod B，负时加 B，循环内无除法。保存最小余数，最后一次恢复 y。所有花费均为 g 的倍数，N mod g 是余数下界，可据此提前结束。最坏枚举仍 O(√N)，另加欧几里得算法；改进算术常数。Go 有界句柄输入输出及 Rust C runtime 也减少运行时存储。保留简单源码；Java/Python 复用已符合标准的基础版。

已通过评测的基础实现 [1430_number_theory.java](1430_number_theory.java), [1430_number_theory.py](1430_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB | 11286201 |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB | 11286202 |
| [1430_number_theory.java](1430_number_theory.java) \* | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB | 11286204 |
| [1430_number_theory.py](1430_number_theory.py) \* | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB | 11286203 |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB | 11286205 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1430_number_theory_optimized.cpp](1430_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.015 s | 108 KB | 11315180 |
| [1430_number_theory_optimized.go](1430_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.031 s | 292 KB | 11315184 |
| [1430_number_theory_optimized.rs](1430_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(sqrt N + log min(A,B)) | AC | 0.046 s | 56 KB | 11315187 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
