# 1057. 区间内 K 个不同的 B 的幂之和

[Timus 1057](https://acm.timus.ru/problem.aspx?space=1&num=1057) · 难度 717 · combinatorics

原题出自雷宾斯克国立航空学院。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计区间 `[X, Y]`（`1 ≤ X ≤ Y ≤ 2^31 − 1`）内恰好是 `K` 个不同的 `B` 的整数次幂之和的整数个数（`1 ≤ K ≤ 20`，
`2 ≤ B ≤ 10`）。

时间限制：1 秒。内存限制：64 MB。

## 输入

`X` 和 `Y`，然后是 `K`，再然后是 `B`。

## 输出

个数。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
15 20
2
2
```

输出：

```
3
```

### 样例 2

输入：

```
1 100
1
10
```

输出：

```
3
```

## 题解

`B` 的不同负次幂之和小于 1，所以整数和只用非负指数。这样的数恰好是 `B` 进制下各位都是 0 或 1、且有 `K` 个 1
的数。用函数 `f(n)` 统计 `[0, n]` 内这样的数；答案为 `f(Y) − f(X − 1)`。

计算 `f(n)` 时，把 `n` 写成 `B` 进制（最多 31 位）：

1. 若某位大于 1，那么任何在这一位之上与 `n` 相同的 0/1 串，无论后面是什么都小于 `n`，所以可以把这一位及其后
   所有位都换成 1，而不改变计数；
2. 现在所有位都是 0 或 1：从高位往下走，记录已取的 1 的个数；在某个为 1 的位上若改选 0，则较低的 `i` 位可以
   任意，贡献 `C(i, K − ones)` 个数；选 1 则继续；
3. 最后，若 `n` 本身恰有 `K` 个 1，也计入。

借助一张小的二项式系数表，复杂度 `O(log_B Y)`。

注意事项：

- `B` 进制的各位必须是 0 或 1；出现 2 或更大的数字就不是*不同*幂之和了；
- `X = 1` 时 `f(X − 1)` 即 `f(0) = 0`；
- `B = 10` 时 `2^31` 以下只有 10 个位置，所以 `K > 10` 时答案为 0。

## 各语言说明

- **C++**、**Go**、**Java**、**Rust**：到 32 的杨辉三角。**Python**：`math.comb`，当 `k > n` 时返回 0。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1057_combinatorics.cpp](1057_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(log Y) | AC | 0.001 s | 204 KB |
| [1057_combinatorics.go](1057_combinatorics.go) | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.015 s | 1080 KB |
| [1057_combinatorics.java](1057_combinatorics.java) | Java 1.8 | combinatorics | O(log Y) | AC | 0.125 s | 1656 KB |
| [1057_combinatorics.py](1057_combinatorics.py) | Python 3.12 x64 | combinatorics | O(log Y) | AC | 0.078 s | 512 KB |
| [1057_combinatorics.rs](1057_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(log Y) | AC | 0.046 s | 252 KB |
