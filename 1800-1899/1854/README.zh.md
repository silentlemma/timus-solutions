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

## 优化解法

新 Go、Python、Rust 版仍对不断缩小的余数试除至立方根并提取偶数次幂。若输入或除去因子后的余数为完全平方，可直接返回整个余数作为其最大平方因子。Python 不再建立百万项筛表，而逐个尝试奇数，使代码更短、辅助空间为常数。试除次数仍为 O(n^(1/3))；去除较小素因子后，合数试除值不可能再整除余数。Python 使用精确 isqrt，Go、Rust 用上界 10⁹ 的整数二分平方根。即使下一次 1000001 的立方检查也能放入有符号 64 位整数，累计平方因子始终整除原始 n。Go 使用标准句柄，Rust 用 C 入口与有界字符输入输出。保留所有旧代码，包括 Python 筛法基础版；C++、Java 的合格基础版继续覆盖快速集合。

通过评测的 Python 3.12 x64 版本耗时 0.203 秒，基础版为 0.171 秒，内存为 392 KB，基础版为 1968 KB。

已通过评测的基础实现 [1854_number_theory.cpp](1854_number_theory.cpp), [1854_number_theory.java](1854_number_theory.java) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 128 KB | 11290772 |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB | 11290776 |
| [1854_number_theory.java](1854_number_theory.java) | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.093 s | 488 KB | 11290779 |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1968 KB | 11290778 |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB | 11290781 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1854_number_theory_optimized.go](1854_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 280 KB | 11314959 |
| [1854_number_theory_optimized.py](1854_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.203 s | 392 KB | 11314964 |
| [1854_number_theory_optimized.rs](1854_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 48 KB | 11314970 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
