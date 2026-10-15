# 1665. 院长的金融金字塔

[Timus 1665](https://acm.timus.ru/problem.aspx?space=1&num=1665) · 难度 438 · number_theory

原题作者 Alex Samsonov，出自 2008 年 1 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

第 1 天晚上桌上有一份申请。之后每天申请数乘以一个整数因子，这个因子是 2 或大于 1 的奇数，每天可以不同。只有在
偶数日、且当天晚上桌上恰好有 N 份申请时才会付钱。对每个 N 判断这是否可能。

## 输入

T（1 ≤ T ≤ 100），然后是 T 个数 N（1 ≤ N ≤ 2²⁵ − 1）。

## 输出

对每个 N 输出 `YES` 或 `NO`。

## 样例

### 样例 1

输入：

```
4
4
7
6
30
```

输出：

```
NO
YES
NO
YES
```

## 解法

第 d 天的申请数是 d − 1 个因子的乘积，而 d 必须是偶数，所以问题是 N 能否写成奇数个因子的乘积，每个因子为 2 或
大于 1 的奇数。设 N = 2ᵃ · r，r 为奇数。只有因子 2 能提供 2，所以恰好有 a 个因子为 2，奇数因子的乘积为 r。

- 若 r = 1，因子恰有 a 个：a 为奇数时 `YES`（N = 1 是第 1 天，不会付钱）。
- 若 a 为偶数且 r > 1，a 个 2 加上 r 本身共 a + 1 个因子，是奇数个：`YES`。
- 若 a 为奇数，r 必须拆成偶数个大于 1 的奇数因子，这当且仅当 r 不是素数时可行（拆成两个，需要时更多）：r 为合数
  时 `YES`，r 为素数时 `NO`。

素性用奇数试除到 √r 来判断，最多约 2900 个除数。`O(T · √N)`。

易错点：

- N = 1 和 a 为偶数的 N = 2ᵃ 都是 `NO`；a 为奇数的 2ᵃ 是 `YES`（测试 02）；
- 奇数次幂的 2 乘以一个素数是 `NO`（样例中的 6，测试 03 中的 2²³ · 3）。

对不超过 3000 的每个 N，答案都与穷举所有因子序列的结果一致，也与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1665_number_theory.cpp](1665_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 128 KB |
| [1665_number_theory.go](1665_number_theory.go) | Go 1.14 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 1084 KB |
| [1665_number_theory.java](1665_number_theory.java) | Java 1.8 | number_theory | O(T sqrt N) | AC | 0.125 s | 448 KB |
| [1665_number_theory.py](1665_number_theory.py) | Python 3.12 x64 | number_theory | O(T sqrt N) | AC | 0.093 s | 412 KB |
| [1665_number_theory.rs](1665_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.031 s | 208 KB |
