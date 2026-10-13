# 1449. 信贷业务 2

[Timus 1449](https://acm.timus.ru/problem.aspx?space=1&num=1449) · 难度 1464 · matching

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 家企业（2 ≤ N ≤ 100）向 N 家银行贷款；A[i, j] 是企业 i 从银行 j 获得的贷款
（0 ≤ A[i, j] ≤ 10⁶）。为企业选择非负整数贿赂 BR[i]，为银行选择 BC[j]，使每笔
贷款满足 A[i, j] ≤ BR[i] + BC[j]，且全部贿赂之和尽量小。输出任意一种最优方案。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N × N 的贷款矩阵。

## 输出

第一行为 BR，第二行为 BC。

## 样例

### 样例 1

输入:

```
4
5 8 4 3
3 6 2 1
4 6 4 1
4 3 5 4
```

输出:

```
2 0 1 2
3 6 3 2
```

## 解法

这是指派问题的线性规划对偶。对任意排列 σ，贿赂要覆盖贷款 A[i, σ(i)]，所以总和
至少是最重完美匹配的权值；匈牙利算法给出的势恰好达到这个权值。在代价 −A 上运行
它：结束时 u[i] + v[j] ≤ −A[i, j]，并在找到的匹配上取等号，所以 BR = −u 和
BC = −v 覆盖所有贷款，总和等于最重匹配的权值，并且势都是整数。

势可能为负，但给所有 BR 加上 t、所有 BC 减去 t，既不改变总和，也不改变任何
BR[i] + BC[j]。平移到最小的 BR 为 0。此时没有 BC 为负：若 BC[j] 为负，则所有
BR[i] ≥ A[i, j] − BC[j] 都为正，包括那个为 0 的。`O(N³)`。

注意事项：

- 全零矩阵也要给出答案，即全零（测试 02）；
- 只有一家银行放贷时，只由这家银行支付即可（测试 07）；
- 势并不是贿赂：平移前要先将势取相反数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1449_matching.cpp](1449_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.015 s | 284 KB |
| [1449_matching.go](1449_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.031 s | 1368 KB |
| [1449_matching.java](1449_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.093 s | 780 KB |
| [1449_matching.py](1449_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.171 s | 1520 KB |
| [1449_matching.rs](1449_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.031 s | 424 KB |
