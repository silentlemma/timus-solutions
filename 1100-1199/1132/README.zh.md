# 1132. 求 a 模素数 n 的全部平方根，最多 100000 组询问

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · 难度 548 · number_theory

原题作者：Mikhail Medvedev。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对最多 `K ≤ 100000` 组询问 `a, n`，其中 `n ≤ 32767` 为素数，
`1 ≤ a ≤ 32767` 且不被 `n` 整除，按递增顺序输出 `1` 到 `n − 1` 中满足
`x² ≡ a (mod n)` 的所有 `x`；若不存在，输出 `No root`。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K`，然后 `K` 行，每行是 `a` 和 `n`。

## 输出

每组询问一行：用空格分隔的根，或者 `No root`。

## 样例

### 样例 1

输入：

```
5
4 17
3 7
2 7
14 31
10007 20011
```

输出：

```
2 15
No root
3 4
13 18
5382 14629
```

## 解法

先把 `a` 对 `n` 取模。`n = 2` 时唯一的根是 `1`。对奇素数，用欧拉判别法判断
根是否存在：二次剩余的 `a^((n−1)/2)` 等于 `1`，否则等于 `n − 1`。若存在根
`r`，另一个根是 `n − r`；因为 `n` 是奇数且 `a` 不为零，两者不同。

根本身由 Tonelli–Shanks 算法求出。写成 `n − 1 = q·2^s`，`q` 为奇数，并取
任意一个非剩余 `z`。从 `r = a^((q+1)/2)`、`t = a^q`、`c = z^q` 开始；此时
始终有 `r² = a·t`。当 `t ≠ 1` 时，找出满足 `t^(2^i) = 1` 的最小 `i`，令
`b = c^(2^(s−i−1))`，并更新 `r ← r·b`、`t ← t·b²`、`c ← b²`、`s ← i`。每一步
都会降低 `t` 的阶，所以最多 `s` 步后 `t = 1` 且 `r² = a`。每个素数的最小
非剩余只求一次并保存。当 `n ≡ 3 (mod 4)` 时循环完全不执行，
`r = a^((n+1)/4)`。每组询问 `O(log² n)`。

注意事项：

- `a` 可能大于 `n`，所以要先取模；
- `n = 2` 只有一个根 `1`，欧拉判别法不适用；
- 两个根按从小到大输出；
- 询问多达 100000 组，输入输出都要缓冲。

答案已在所有测试上与每个出现过的素数的全部平方表比对。

## 各语言说明

- 所有语言使用同样的 Tonelli–Shanks 算法，并为每个素数缓存非剩余。
- Go 用一个小的逐字节读取器读入 200000 个数，比 `fmt.Fscan` 更快。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB |
| [1132_number_theory.java](1132_number_theory.java) | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB |
| [1132_number_theory.py](1132_number_theory.py) | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB |
