# 1157. 能拼出 N 种长方形、少 K 块时能拼出 M 种的最少瓷砖数

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · 难度 200 · number_theory

原题出自 2001 年 4 月在彼尔姆举行的乌拉尔团体程序设计锦标赛英语轮。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个男孩用他全部的正方形瓷砖拼成长方形。已知 `M`、`N`、`K`（`M, N ≤ 50`，
`K ≤ 9999`），求最小的瓷砖数 `L`，使 `L` 块瓷砖恰好能拼出 `N` 种不同的长方形，
而 `L − K` 块恰好能拼出 `M` 种。若不超过 10000 的这样的 `L` 不存在，输出 `0`。

时间限制：1 秒。内存限制：64 MB。

## 输入

`M`、`N` 和 `K`。

## 输出

最小的 `L`，或者 `0`。

## 样例

### 样例 1

输入：

```
2 3 1
```

输出：

```
16
```

## 解法

`x` 块瓷砖对每种写法 `x = a·b`（`a ≤ b`）拼出一个 `a × b` 的长方形，所以长方形
种数等于 `x` 的约数个数除以二再向上取整（若有平方根，它与自己配对）。对 `d`
从 1 到 10000 做筛法，给 `d` 的每个倍数加一，就能在 `O(10000·log 10000)` 步内
算出 10000 以内所有数的约数个数。然后从 `K + 1` 开始往上试 `L`，第一个满足
`L` 有 `N` 种、`L − K` 有 `M` 种的就是答案。

注意事项：

- `L − K` 至少要有一块瓷砖，所以 `L` 从 `K + 1` 开始；
- 完全平方数的约数个数是奇数，它的正方形只算一次；
- 10000 以内没有数的约数超过 64 个，所以 `N` 或 `M` 大于 32 时答案总是 `0`。

答案已在所有测试上与用试除法直接数长方形的结果比对。

## 各语言说明

- 所有语言使用同样的筛法和搜索。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log L) | AC | 0.015 s | 216 KB |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(L log L) | AC | 0.031 s | 1172 KB |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(L log L) | AC | 0.125 s | 1620 KB |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(L log L) | AC | 0.078 s | 712 KB |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log L) | AC | 0.046 s | 300 KB |
