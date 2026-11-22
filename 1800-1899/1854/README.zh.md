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

`1854_number_theory_optimized.py`. 保留保证为奇数输入的最大平方因子精确分解。先除尽三，再只测试 6k-1 和 6k+1 因子。每次去掉素数幂后用精确 isqrt 检查，平方余数可立即返回；缩小立方根循环后仅平方余数有贡献。无筛表或预存答案。n<10^18 时 O(n^(1/3)) 次试除和常量算术状态；保留易读的 Python 筛法。

精确源代码 PyPy 3.10 x64 Accepted #11327061：0.125 s / 1068 KB。2026-11-20 保存的当前 Python 语言族编译器比较：时间 2/23、内存 7/23，两项严格前十均通过。内存至少 1024 KB，故必须同时满足时间和内存。单独的两项第一语言目标未满足，保留星号。此前记录的优化 CPython 3.12 #11314964 为 0.203 s / 392 KB。所选 PyPy 记录时间更低、内存更高；这是不同解释器的独立成对测量，并非纯算法加速或混合最小值。保留的简单 CPython 版当前 Accepted #11327562：0.171 s / 1928 KB。无需额外源代码副本或重复提交。

仅格式化后的自身 Accepted：`1854_number_theory.java` #11327560, `1854_number_theory.cpp` #11327561, `1854_number_theory.py` #11327562。保留基础算法及其余源文件。

新 Go、Python、Rust 版仍对不断缩小的余数试除至立方根并提取偶数次幂。若输入或除去因子后的余数为完全平方，可直接返回整个余数作为其最大平方因子。Python 不建立百万项筛表，先除尽三，再仅测试 6k±1，算术状态为常数。试除次数仍为 O(n^(1/3))；去除较小素因子后，合数试除值不可能再整除余数。Python 使用精确 isqrt，Go、Rust 用上界 10⁹ 的整数二分平方根。即使下一次 1000001 的立方检查也能放入有符号 64 位整数，累计平方因子始终整除原始 n。Go 使用标准句柄，Rust 用 C 入口与有界字符输入输出。保留所有旧代码，包括 Python 筛法基础版；C++、Java 的合格基础版继续覆盖快速集合。

保留的 Accepted 基础版 [1854_number_theory.cpp](1854_number_theory.cpp), [1854_number_theory.java](1854_number_theory.java) 在保存比较中满足所需指标的严格前十或前 15% 收录，不增加相同优化副本。表为当前精确成对测量，星号表示单独语言目标。格式化不改算法，不将速度变化归功于格式化。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 112 KB | 11327561 |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB | 11290776 |
| [1854_number_theory.java](1854_number_theory.java) \* | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.125 s | 488 KB | 11327560 |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1928 KB | 11327562 |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB | 11290781 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1854_number_theory_optimized.go](1854_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 280 KB | 11314959 |
| [1854_number_theory_optimized.py](1854_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(n^(1/3)) trial divisions; O(1) arithmetic state | AC | 0.125 s | 1068 KB | 11327061 |
| [1854_number_theory_optimized.rs](1854_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 48 KB | 11314970 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
