# 1091. 统计有公因数的数集

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · 难度 529 · number_theory

原题作者 Stanislav Vasiliev，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计由 `K` 个不同正整数组成、每个数都不超过 `S`（`2 ≤ K ≤ S ≤ 50`）且最大公因数大于 1 的集合个数。输出这个数；
若它大于 10000，则输出 10000。

时间限制：1 秒。内存限制：64 MB。

## 输入

`K` 和 `S`。

## 输出

集合个数，最多 10000。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
3 10
```

输出：

```
11
```

## 解法

首选教学 Go 版按精确 gcd 计数，无需 Möbius。K>floor(S/2) 时任何除数≥2 都无足够倍数。只算 K≤m≤floor(S/2) 的 C(m,K)，从1用 C(m−1,K)·m/(m−K) 推进。d 从 D=floor(S/K) 降到2，以 C(floor(S/d),K) 减去已知 gcd 为2d、3d… 的数量。每集合只有一个 gcd，类别不交，d≥2 的总和即答案。K=3、S=10 时，精确 gcd 为 3 的集合有 C(3,3)=1 个，gcd 为 2 的有 C(5,3)=10 个，共 11 个。若某组合数达到10000，前 m 个偶数的 K 子集已经给出足够的合法集合，可以返回 10,000。在此之前，递推中小于 10,000 的值乘以 m ≤ 25。每个精确计数至多等于对应组合数，加到小于 10,000 的累计值后小于 20,000。答案上限为 10,000。时间 O(S + D log D)，空间 O(S)。原 Möbius 实现用完整 Pascal 表计算 Σ−μ(d)C(floor(S/d),K)，只截断最终答案。

## 优化解法

Go 快速版保留精确 gcd 递推，直接使用标准句柄，答案缓冲区为六字节。 Rust 快速版用相同精确 gcd 算法、固定32位数组、C 字符输入输出和 C 入口。C++/Java/Python 复用已达标原版。D=floor(S/K)≤25，不存预计算答案表。旧 Go 保留于其他 Accepted 方法，旧 Rust 仍为标准库简单版。星号只涉及语言排名目标。

已通过评测的基础实现 [1091_number_theory.cpp](1091_number_theory.cpp), [1091_number_theory.java](1091_number_theory.java), [1091_number_theory.py](1091_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

`1091_number_theory_optimized.java`. Java 保留简单版本所述的算法和数据结构。固定字节缓冲区与 FastInput 替代 Scanner 及其正则表达式、区域设置处理。整数记号直接解析；需要字符串时仍进行 UTF-8 解码，十进制记号仍显式转换为数值。仅在需要前瞻时保存一个记号，输出算法不变。这样减少通用解析开销；表中列出算法工作量，输入扫描与字节数成正比，并使用有界输入缓冲区。

与 `1091_number_theory.java` 相比：时间 0.109 s → 0.093 s；内存 1640 KB → 492 KB。

## 各语言说明

教学 Go 用普通缓冲输入和两个26元素整数数组。Rust 用两个26元素 u32 数组与无指针 getchar/putchar，答案≤10000 最多五位。原五种程序的精确 Accepted/指标不变，Python 保留实际评测解释器。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB | 11279091 |
| [1091_dp.go](1091_dp.go) | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 912 KB | 11315680 |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB | 11279094 |
| [1091_number_theory.py](1091_number_theory.py) \* | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB | 11279093 |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB | 11279095 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB | 11279092 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1091_dp_optimized.go](1091_dp_optimized.go) \* | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 264 KB | 11315895 |
| [1091_dp.rs](1091_dp.rs) \* | Rust 1.75 x64 | dp | O(S + D log D) | AC | 0.015 s | 60 KB | 11315681 |
| [1091_number_theory_optimized.java](1091_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(S^2) | AC | 0.093 s | 492 KB | 11324824 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
