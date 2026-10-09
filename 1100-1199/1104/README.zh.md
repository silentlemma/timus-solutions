# 1104. 使数能被“基数减一”整除的最小基数

[Timus 1104](https://acm.timus.ru/problem.aspx?space=1&num=1104) · 难度 95 · number_theory

原题作者 Igor Goldberg，出自 2001 年 5 月 Tetrahedron Team Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个数用数字 `0`–`9` 和字母 `A`–`Z`（`A` = 10，…，`Z` = 35）写成，至多 `10^6` 位。求最小的基数
`k`（`2 ≤ k ≤ 36`），使这个字符串在 `k` 进制下是合法的数并且能被 `k − 1` 整除。如果不存在，输出 `No solution.`

时间限制：1 秒。内存限制：64 MB。

## 输入

一行数字。

## 输出

十进制的 `k`，或 `No solution.`

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
A1A
```

输出：

```
22
```

## 解法

因为 `k ≡ 1 (mod k − 1)`，`k` 的任何次幂模 `k − 1` 都余 1，所以 `k` 进制的数与其各位数字之和同余，这和十进制中被 9
整除的判别法是同一个道理。于是只需一次算出数字和 `S` 与最大数字 `m`，再让 `k` 从 `max(m + 1, 2)` 试到 36，输出第一个使
`k − 1` 整除 `S` 的值。对 `L` 位数字为 `O(L)`。

注意事项：

- 基数必须大于每一位数字，所以从 `m + 1` 开始尝试；
- 在 2 进制下任何数都能被 1 整除，所以只由 0 和 1 组成的数答案总是 2，单独的 `0` 也是如此；
- 数字和至多 `35 · 10^6`，32 位整数放得下。

答案经过验证：用 Python 的大整数把整个字符串按每个基数转换，再直接取余数。

## 语言说明

- Python 和 Java 分别用 `int(ch, 36)` 和 `Character.digit` 把每一位按 36 进制数字读入；Rust 用 `to_digit(36)`。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1104_number_theory.cpp](1104_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L) | AC | 0.093 s | 2640 KB |
| [1104_number_theory.go](1104_number_theory.go) | Go 1.14 x64 | number_theory | O(L) | AC | 0.031 s | 6608 KB |
| [1104_number_theory.java](1104_number_theory.java) | Java 1.8 | number_theory | O(L) | AC | 0.109 s | 5448 KB |
| [1104_number_theory.py](1104_number_theory.py) | Python 3.12 x64 | number_theory | O(L) | AC | 0.265 s | 17808 KB |
| [1104_number_theory.rs](1104_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L) | AC | 0.015 s | 7048 KB |
