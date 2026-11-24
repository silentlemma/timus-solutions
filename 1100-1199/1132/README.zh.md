# 1132. 求 a 模素数 n 的全部平方根，最多 100000 组询问

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · 难度 545 · number_theory

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

C++ 教学版按素数对查询排序，每组建立一张平方表。对奇素数 p，两根为 x 和 p − x，枚举 1 到 floor(p/2) 即可找到较小的根。相邻平方之差为 2x − 1，因此每个余数只需一次加法和至多一次减去 p。表中为零表示对应的非零余数无根。p = 2 时两根相同，只输出一次 1。原查询下标用于恢复输出顺序。时间 O(K log K + Σp)，对输入中不同的素数求和。空间 O(K + P)，其中 P 是输入的最大素数。

## 优化解法

新 C++/Go/Rust 保留 Tonelli–Shanks，但 p≡3 mod4 直接算 a^((p+1)/4) 并验平方，省去独立 Euler 测试。p≡5 mod8 试 a^((p+3)/8)，必要时乘缓存的 2^((p−1)/4) 再验证。其余 p−1=q2^s，q奇数；一次 b=a^((q−1)/2) 得 r=ab、t=rb，保持 r²=at。若 t 阶为2^s则无根，否则标准修正逐次降阶；二次幂用反复平方。每模数一个 uint16 缓存原始 c=z^q，不能缓存循环修改值。乘积<32767²，uint32足够。固定缓冲流式输入输出，Rust用C字符I/O，不保留全部查询/答案。每问 O(log²P)，特类 O(log P)；各需要素数额外一次非剩余搜索，Z_p 候选耗 O((Z_p+1)log p)。设 K 为查询数，Z = Σ(Z_p+1) 对这些素数求和，含初始化的总时间为 O(P + K log² P + Z log P)。空间 O(P)，P=32768，加固定缓冲。保留简单版，Java/Python复用达标基础版。

通过评测的 Rust 1.75 x64 版本耗时 0.062 秒，基础版为 0.015 秒，内存为 108 KB，基础版为 4068 KB。

已通过评测的基础实现 [1132_number_theory.java](1132_number_theory.java), [1132_number_theory.py](1132_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

原文件缓存每个素数的二次非剩余。优化的 C++、Go 和 Rust 缓存对应分支的初始幂或修正值。p≡3 mod4 时直接计算平方根。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB | 11279382 |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB | 11279383 |
| [1132_number_theory.java](1132_number_theory.java) \* | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB | 11279386 |
| [1132_number_theory.py](1132_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB | 11279385 |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB | 11279388 |
| [1132_math.cpp](1132_math.cpp) | G++ 13.2 x64 | math | O(K log K + Σp) | AC | 0.171 s | 6056 KB | 11315928 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1132_number_theory_optimized.cpp](1132_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.031 s | 140 KB | 11315759 |
| [1132_number_theory_optimized.go](1132_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.015 s | 992 KB | 11315760 |
| [1132_number_theory_optimized.rs](1132_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.062 s | 108 KB | 11315763 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
