# 1206. 数字和可以相加的数对

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · 难度 124 · combinatorics

原题作者 Leonid Volkov，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

设 `S(N)` 为 `N` 的各位数字之和。对 `2 ≤ K ≤ 50`，统计满足
`S(A + B) = S(A) + S(B)` 的无前导零 `K` 位数有序对 `A`、`B` 的个数。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`。

## 输出

数对的个数。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
1980
```

## 解法

加法中的每次进位都会把某一位上的 10 变成下一位上的 1，使数字和减少 9。所以等式
成立当且仅当没有任何进位，也就是每一位上两个数字之和不超过 9。此时各位互相独立。
最高位上两个数字都在 1 到 9 之间，共有 `8 + 7 + … + 1 = 36` 对；其余 `K − 1`
位上数字在 0 到 9 之间，每位有 `10 + 9 + … + 1 = 55` 对。答案是 `36 · 55^(K−1)`，
最多 87 位。用竖式乘法为 `O(K²)`。

注意事项：

- 答案在 `K = 12` 时就超出了 64 位；
- 最高位不能为 0，所以它的对数和其他位不同。

公式已在 `K = 2` 和 `K = 3` 时用枚举全部数对验证，并且每个 `K` 都与另一份独立解答
比对过。

## 各语言说明

- Python 用自带的整数，Go 用 `math/big`，Java 用 `BigInteger`；C++ 和 Rust 把
  十进制数字数组乘以 55 共 `K − 1` 次。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB |
