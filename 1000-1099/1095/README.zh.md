# 1095. 重排数字得到 7 的倍数

[Timus 1095](https://acm.timus.ru/problem.aspx?space=1&num=1095) · 难度 583 · number_theory

原题作者 Dmitry Filimonenkov，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 个正整数（`1 ≤ N ≤ 10000`，最多 20 位）中的每一个都包含数字 1、2、3 和 4。重排每个数的各位数字，使结果能被 7
整除；若不可能，输出 0。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 个数，每行一个。

## 输出

每个数各位数字组成的一个 7 的倍数，每行一个。

## 评测方式

接受任何满足要求的重排。检查程序验证每个答案恰好由对应数的各位数字组成，不以 0 开头，并且能被 7 整除。

## 样例

### 样例 1

输入：

```
2
1234
531234
```

输出：

```
3241
531342
```

## 题解

从数中取出各一个 1、2、3、4。先按任意顺序写出其余非零数字，再按某种顺序写出这四个关键数字，最后写出所有的 0。
末尾的 0 相当于乘以 10 的幂，不改变能否被 7 整除，而且数不会以 0 开头。若前面部分模 7 余 `r`，则对关键数字的顺序 `p`，
添加末尾的 0 之前，数模 7 等于 `r · 10⁴ + p`；而 1、2、3、4 的 24 种顺序模 7 的余数覆盖了全部七个值（`1234 ≡ 2`，`1243 ≡ 4`，
`1324 ≡ 1`，`2134 ≡ 6`，`2143 ≡ 1`，`3124 ≡ 2`，`3241 ≡ 0`，`4123 ≡ 0`，`1342 ≡ 5`，…）。所以总有一种顺序可行，
答案永远不会是 0。`L` 位数字共 `O(N · L)`。

注意事项：

- 20 位的数可能放不进 64 位整数，所以余数要逐位计算（Python 直接用大整数）；
- 如果前面部分为空，放在前面的 0 可能成为首位，所以所有的 0 都放到末尾；
- 每个关键数字只取出一个，其余的留在前面部分。

检查程序用大整数检查每个答案的数字和整除性。

## 各语言说明

- C++ 用 `std::next_permutation` 列出各种顺序；Go、Java 和 Rust 递归生成；Python 使用 `itertools.permutations`。

## 优化解法

C++ 版本为模 7 的每个余数预先保存数字 1、2、3、4 的一种排列。扫描每个数一次，保留这四个数字、统计零的个数，并计算其余非零数字组成的数的余数。根据该余数查表即可得到所需排列。时间复杂度仍为 O(N·L)，缓冲区大小固定。 评测数据来自提交 11316960。

Python 提交 11317754 耗时 0.125 秒，使用 436 KB。简单版本耗时 0.171 s，使用 2676 KB。

Go 提交 11317765 耗时 0.031 秒，使用 1276 KB。简单版本耗时 0.046 s，使用 4660 KB。

Rust 提交 11317775 耗时 0.015 秒，使用 192 KB。简单版本耗时 0.031 s，使用 936 KB。

Java 提交 11317780 耗时 0.093 秒，使用 1240 KB。简单版本耗时 0.171 s，使用 7408 KB。

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322115 · Go 1.14 x64 №11322116 · Java 1.8 №11322117 · Python 3.12 x64 №11322118 · Rust 1.75 x64 №11322119.

## 题解代码

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1095_number_theory.cpp](1095_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.015 s | 648 KB | 11322115 |
| [1095_number_theory.go](1095_number_theory.go) | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.046 s | 4660 KB | 11322116 |
| [1095_number_theory.java](1095_number_theory.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.171 s | 7408 KB | 11322117 |
| [1095_number_theory.py](1095_number_theory.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.171 s | 2676 KB | 11322118 |
| [1095_number_theory.rs](1095_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.031 s | 936 KB | 11322119 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1095_number_theory_optimized.cpp](1095_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.015 s | 112 KB | 11316960 |
| [1095_number_theory_optimized.py](1095_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.125 s | 436 KB | 11317754 |
| [1095_number_theory_optimized.go](1095_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.031 s | 1276 KB | 11317765 |
| [1095_number_theory_optimized.rs](1095_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.015 s | 192 KB | 11317775 |
| [1095_number_theory_optimized.java](1095_number_theory_optimized.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.093 s | 1240 KB | 11317780 |

\* 带星号的解法尚未达到目标排名，仍可优化。
