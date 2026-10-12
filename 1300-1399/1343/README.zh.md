# 1343. 童话

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · 难度 417 · number_theory

原题作者 Pavel Atnashev，出自 USU Championship 2004。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 12 位数字中的前 k 位（0 ≤ k ≤ 12）。输出任意一个以它们开头、除 1 和自身外没有其他因数的 12 位数。保证
答案存在。

时间限制：1 秒。内存限制：64 MB。

## 输入

第一行是 k，第二行是这 k 位数字。

## 输出

这个 12 位数。

## 检查

检查器接受任何以给定数字开头、且构成的数没有其他因数的 12 位数字串。

## 样例

### 样例 1

输入：

```
5
64631
```

输出：

```
646310554187
```

## 解法

把空余的位填 0，然后逐个加一，直到得到素数。10¹² 附近素数的平均间隔约为 28，而 10¹² 以下没有超过几百的间隔，
所以最多只需尝试几百个数。每个数用以 2、3、5、7、11、13 为底的 Miller–Rabin 检验，这组底在 3 · 10¹² 以下
不会出错。若 12 位全部给出，答案就是这个数本身。若前缀是若干个 0，输出时保留前导零。

注意事项：

- 给定的数字可能以 0 开头，答案必须保留这些 0，例如 `000000000002`（测试 04 和 05）；
- 检验中的平方可达 10²⁴，超过 64 位，所以模 n 乘法需要小心；
- k = 0 时第二行为空（测试 02）。

## 各语言说明

- C++ 和 Rust 用 128 位整数相乘，Go 使用 `bits.Mul64` 和 `bits.Rem64`。Java 把一个因子拆成两个 20 位的部分，
  对于小于 2⁴⁰ 的 n，每个乘积都小于 2⁶⁰。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB |
| [1343_number_theory.java](1343_number_theory.java) | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB |
| [1343_number_theory.py](1343_number_theory.py) | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB |
