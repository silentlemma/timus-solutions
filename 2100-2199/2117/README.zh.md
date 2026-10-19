# 2117. 两个平方根之和等于给定的根

[Timus 2117](https://acm.timus.ru/problem.aspx?space=1&num=2117) · 难度 544 · number_theory

原题作者 Pavel Klimov，出自 2019 年大学学术信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对整数 C，统计满足 √A + √B = √C 的非负整数对 A ≤ B 的个数。时间限制 1 秒，内存限制 256 MB。

## 输入

C（0 ≤ C ≤ 10¹⁸）。

## 输出

数对个数。

## 样例

### 样例 1

输入：

```
9
```

输出：

```
2
```

### 样例 2

输入：

```
3
```

输出：

```
1
```

## 解法

记 C = s² q，q 无平方因子。把 √A = √C − √B 平方可知 √(BC) 是整数，进而 A 和 B 为 a² q 和 b² q，且 a + b = s；反之每种这样的拆分都成立。所以答案是满足 a + b = s 的 a ≤ b 的对数，即 ⌊s/2⌋ + 1（C = 0 只有 0, 0 一对）。

剩下的是求 s，即整除 C 的最大平方数的平方根。用不超过 10⁶（10¹⁸ 的立方根）的 d 试除：只要 d² 整除就除掉，然后若还有一个 d 也除掉，每除掉一个 d² 就把 s 乘以 d。剩下的数是 1、质数或两个大于 10⁶ 的质数的乘积，因为三个这样的因子之积会超过 10¹⁸。所以它只有本身是质数的平方时才含平方因子；此时 s 再乘上这个质数。时间复杂度为 O(min(10⁶, √C))。

第一个样例中 9 = 3² · 1，所以 s = 3，数对为 0 + 9 和 1 + 4。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.031 s | 136 KB |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.046 s | 1096 KB |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(min(10⁶, √C)) | AC | 0.140 s | 1604 KB |
| [2117_number_theory.py](2117_number_theory.py) | Python 3.12 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.500 s | 472 KB |
| [2117_number_theory.rs](2117_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.062 s | 232 KB |
