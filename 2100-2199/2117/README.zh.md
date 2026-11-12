# 2117. 两个平方根之和等于给定的根

[Timus 2117](https://acm.timus.ru/problem.aspx?space=1&num=2117) · 难度 544 · number_theory

原题作者 Pavel Klimov，出自 2019 年大学学术信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对整数 C，统计满足 √A + √B = √C 的非负整数对 A ≤ B 的个数。时间限制 1 秒，内存限制 256 MB。

## 输入

C（0 ≤ C ≤ 10¹⁸）。

## 输出

数对个数。

## 样例

### 样例 1

输入：

```
9
```

输出：

```
2
```

### 样例 2

输入：

```
3
```

输出：

```
1
```

## 解法

记 C = s² q，q 无平方因子。把 √A = √C − √B 平方可知 √(BC) 是整数，进而 A 和 B 为 a² q 和 b² q，且 a + b = s；反之每种这样的拆分都成立。所以答案是满足 a + b = s 的 a ≤ b 的对数，即 ⌊s/2⌋ + 1（C = 0 只有 0, 0 一对）。

剩下的是求 s，即整除 C 的最大平方数的平方根。用不超过 10⁶（10¹⁸ 的立方根）的 d 试除：只要 d² 整除就除掉，然后若还有一个 d 也除掉，每除掉一个 d² 就把 s 乘以 d。剩下的数是 1、质数或两个大于 10⁶ 的质数的乘积，因为三个这样的因子之积会超过 10¹⁸。所以它只有本身是质数的平方时才含平方因子；此时 s 再乘上这个质数。时间复杂度为 O(min(10⁶, √C))。

第一个样例中 9 = 3² · 1，所以 s = 3，数对为 0 + 9 和 1 + 4。

## 优化解法

新 C++/Go 保留 C=s²q（q 无平方因子）及答案 floor(s/2)+1。C>0 时，将 √A = √C − √B 平方得到 2√(BC) = B + C − A。右侧的平方被四整除，所以右侧为偶数，BC 是平方。B>0 时，B 与 C 的素因子指数奇偶性相同，故 B=b²q、A=(s−b)²q。因此只需考虑 s 的整数拆分，包括 A=0。

完全平方数（含零）直接取 s=sqrt(C)。否则移除2、3的成对因子和剩余奇数次因子，再只试6k±1。当 d³ 超过不断缩小的余数 R 时停止：剩余素因子均≥d，计重数最多两个，只有 R 本身为平方才再贡献平方因子。浮点平方根估计经精确整数乘法校正，C≤10^18及首个失败立方均适合 uint64。相较逐整数到固定10^6，轮式枚举减少除法，自适应边界常更早结束。最坏 O(C^(1/3)) 时间、O(1) 额外空间。Go 通过标准句柄读入 64 字节缓冲。答案至多 500,000,001，九位数字加换行符只需十字节。保留所有简单版，Java/Python/Rust 复用达标原版。

已通过评测的基础实现 [2117_number_theory.java](2117_number_theory.java), [2117_number_theory.py](2117_number_theory.py), [2117_number_theory.rs](2117_number_theory.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.031 s | 136 KB | 11294802 |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.046 s | 1096 KB | 11294803 |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(min(10⁶, √C)) | AC | 0.140 s | 1604 KB | 11294808 |
| [2117_number_theory.py](2117_number_theory.py) \* | Python 3.12 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.500 s | 472 KB | 11294805 |
| [2117_number_theory.rs](2117_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.062 s | 232 KB | 11294811 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2117_number_theory_optimized.cpp](2117_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(C^(1/3)) | AC | 0.015 s | 112 KB | 11315748 |
| [2117_number_theory_optimized.go](2117_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(C^(1/3)) | AC | 0.046 s | 276 KB | 11315923 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
