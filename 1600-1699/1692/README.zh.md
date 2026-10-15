# 1692. 各省的旗帜

[Timus 1692](https://acm.timus.ru/problem.aspx?space=1&num=1692) · 难度 379 · constructive

原题作者 Igor Chevdar，出自 2009 年 2 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

用 n 种颜色设计尽可能多的旗帜，使任意两面旗都有共同的颜色，但没有任何颜色出现在三面或更多旗帜上。

## 输入

n（3 ≤ n ≤ 1000）。

## 输出

旗帜数 k，然后每面旗依次给出颜色数和各颜色。任何合法的设计都可以。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
3
2 1 2
2 1 3
2 2 3
```

## 解法

k(k − 1)/2 对旗帜中的每一对都需要一种共同颜色。至多出现在两面旗上的颜色至多是一对旗的共同颜色，
所以不同的对用不同的颜色，k(k − 1)/2 ≤ n。

这个上界可以达到：给每对旗编号，并为每一对分配一种只涂在这两面旗上的颜色。
于是每面旗有 k − 1 种颜色，任意两面旗共享它们这一对的颜色，且没有颜色出现在两面以上的旗上。
取满足 k(k − 1)/2 ≤ n 的最大 k；多余的颜色不用。输出为 `O(n)`。

注意事项：

- 剩余的颜色不必使用（测试 04）；
- 样例中的设计只是众多答案之一，所以检查器验证旗帜而不是比较文本。

检查器检查数量、范围、每对旗的共同颜色以及“至多两面”的规则；一个独立的已通过实现在所有 n ≤ 300 上的答案都能通过它。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1692_constructive.cpp](1692_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 232 KB |
| [1692_constructive.go](1692_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 1152 KB |
| [1692_constructive.java](1692_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1796 KB |
| [1692_constructive.py](1692_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 464 KB |
| [1692_constructive.rs](1692_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 264 KB |
