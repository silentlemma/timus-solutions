# 1023. 选择让后手获胜的每步上限

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · 难度 217 · games, number_theory

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两名玩家轮流从一堆 `K` 颗纽扣中取走 1 到 `L` 颗；取到最后一颗的人获胜。先手已选定 `K`
（`3 ≤ K ≤ 10^8`），现在后手选择 `L`，要求 `2 ≤ L < K`。求最小的 `L`，使后手无论先手怎样走都能获胜；
若不存在则输出 0。

时间限制：2 秒。内存限制：64 MB。

## 输入

`K`。

## 输出

最小的必胜 `L`，或 0。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
8
```

输出：

```
3
```

### 样例 2

输入：

```
35
```

输出：

```
4
```

## 题解

**博弈。** 每步可取 1 到 `L` 颗时，轮到者必败的局面恰好是 `L + 1` 的倍数：从这样的一堆出发，任何走法都
留下非倍数；从非倍数出发，取走 `n mod (L + 1)` 颗即可留下倍数。所以后手获胜当且仅当 `L + 1` 整除 `K`。

**选择 L。** 要求最小的 `L ≥ 2` 满足 `L + 1 | K`，即 `K` 的不小于 3 的最小因数 `d`，`L = d - 1`；条件
`L < K` 即 `d ≤ K`。由于 `d = K` 总是可行（`K ≥ 3`），答案永远不是 0。

**快速求 d。** 依次尝试 `d = 3, 4, ...`，直到 `d^2 > K`。若都不整除 `K`，则大于 `sqrt(K)` 的最小因数等于
`K / j`，其中 `j` 是不超过 `sqrt(K)` 的最大因数——而此时不超过 `sqrt(K)` 的因数只剩 1 和 2。于是若 `K` 为
偶数且 `K / 2 ≥ 3`，则 `d = K / 2`，否则 `d = K`。至多 `sqrt(10^8) = 10^4` 步。

注意事项：

- `K = 4`：因数 2 太小，`K / 2 = 2` 也太小，所以 `d = 4`，`L = 3`；
- `K = 2p`（`p` 为质数）：因数 `p` 大于 `sqrt(K)`，不能漏掉；
- 枚举直到 `K` 的所有 `L` 需要 `10^8` 步——C++ 可以，Python 太慢。

## 各语言说明

各语言使用同样的因数搜索。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB |
