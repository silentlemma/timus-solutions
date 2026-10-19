# 1854. 与帕提亚的谈判

[Timus 1854](https://acm.timus.ru/problem.aspx?space=1&num=1854) · 难度 424 · number_theory

原题作者 Grigoriy Nazarov，出自 2011 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Team.GOV Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

哈德良皇帝要献祭一群 n 只公羊（n 为奇数），平均分给若干位神。士麦那的塞翁希望神的数目是奇数，并且有奇数个正约数。求满足条件的最大神的数目。

## 输入

一个奇数 n（1 ≤ n ≤ 10¹⁸ − 1）。

## 输出

最大的满足条件的神的数目。

## 样例

### 样例 1

输入：

```
45
```

输出：

```
9
```

## 解法

一个数有奇数个约数，当且仅当它是完全平方数：约数按 k 与 m/k 配对，只有平方数有一个与自身配对的约数。奇数 n 的约数都是奇数，所以答案是整除 n 的最大平方数，即对 n 的质因数分解中每个 p^e 取 p^(2⌊e/2⌋) 的乘积。

在 p³ ≤ n 时除去奇质数 p，n 随之变小。剩下的数没有不超过其立方根的质因子，所以它是 1、一个质数、两个质数之积或一个质数的平方，只有最后一种情况会贡献平方因子：用精确的整数平方根检查。
试除最多 10⁶ 步，Python 版本只试筛出的质数。`O(n^(1/3))`。

在样例中 45 = 3²·5，所以答案是 9。

注意事项：

- 较大质因子的平方，例如 (10⁹ − 63)²，会在试除之后留下，仍然必须识别出来；
- 接近 10¹⁸ 的数的浮点平方根可能差一，要用整数检查修正。

在一百个小数上答案与直接搜索一致，在大质数、两个大质数之积、大质数的平方以及许多小质数之积上与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 128 KB |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB |
| [1854_number_theory.java](1854_number_theory.java) | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.093 s | 488 KB |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1968 KB |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB |
