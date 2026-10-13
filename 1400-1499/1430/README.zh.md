# 1430. 罪与罚

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · 难度 463 · number_theory

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

- x·A 这样的和会超过 32 位（测试 03、06）；
- 若两个价格都大于 N，就什么也不买（测试 12）；
- 答案不唯一，所以测试使用检查器（测试 01）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB |
| [1430_number_theory.java](1430_number_theory.java) | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB |
| [1430_number_theory.py](1430_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB |
