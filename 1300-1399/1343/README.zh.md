# 1343. 童话

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · 难度 417 · number_theory

原题作者 Pavel Atnashev，出自 USU Championship 2004。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 12 位数字中的前 k 位（0 ≤ k ≤ 12）。输出任意一个以它们开头、除 1 和自身外没有其他因数的 12 位数。保证
答案存在。

时间限制：1 秒。内存限制：64 MB。

## 输入

第一行是 k，第二行是这 k 位数字。

## 输出

这个 12 位数。

## 检查

检查器接受任何以给定数字开头、且构成的数没有其他因数的 12 位数字串。

## 样例

### 样例 1

输入：

```
5
64631
```

输出：

```
646310554187
```

## 解法

首选教学版为 C++ 试除。用零补全前缀，单独处理 2，再枚举奇数候选。一个数为素数当且仅当不被整数平方根以内的任何数整除。先检查 2、3，其余素数必为 6q−1 或 6q+1，循环检查这些对。N<10¹²，乘积可用 64 位。G 个候选的时间 O(G·sqrt(N))，辅助空间 O(1)，无需模幂或素数表。答案保证使搜索在离开给定前缀前成功。始终输出十二位并保留前导零。给全十二位时直接输出保证有效的值，包括 000000000001。基础试除只保留 C++；更高级的 Accepted 实现另列。

## 优化解法

`1343_number_theory_optimized.java`. 保留已有六基 Miller-Rabin 和20位拆分模乘，是原有优化 Java 算法的精简输入输出实现。跨分隔符直接读恰好 k 个前缀数字，数值补到12位，仅 k<12 时连续搜索；存在性保证完整12位前缀已是合法答案。直接输出前导零和数值，省去 Scanner、StringBuilder、String.format。测试值低于10^12<2^40，拆分中间值安全容于 long。设低于 P 的候选 G 个，耗时 O(G log P) 次有界字模步骤，空间 O(1)。不虚构简单 Java 版本，保留已有优化文件；新精确 Accepted 依据自身前十/前15% 排名纳入。

与 `1343_number_theory.java` 相比：时间 0.125 s → 0.093 s；内存 1752 KB → 500 KB。

Miller–Rabin 使用六个底数 2,3,5,7,11,13。检查小素因子后写 N−1=2ˢd，d 为奇数。每个底数计算 x=aᵈ mod N；若 x 为 1、N−1，或接下来 s−1 次模平方之一为 N−1，则该底数通过，否则候选为合数。[Jaeschke 六底数界](https://doi.org/10.1090/S0025-5718-1993-1192971-8) 为 3474749660383，覆盖本题全部值，因此确定无误。G 个候选需 O(G log N) 次机器字操作。新 Go、Rust 使用有界输入输出；Go 用 bits.Mul64/bits.Rem64，Rust 用 u128。Java、Python 复用合格原文件。C++ 快速覆盖共享“简单版本”的[试除文件](1343_bruteforce.cpp)，其精确 Accepted 符合收录规则，不复制 optimized 文件；这不宣称试除渐进复杂度优于 Miller–Rabin。原 C++/Go/Rust Miller–Rabin 保留在其他 Accepted 实现中。

已通过评测的基础实现 [1343_number_theory.java](1343_number_theory.java), [1343_number_theory.py](1343_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1343_number_theory_optimized.java`：在该可比样本中，时间名次 1/37，内存名次 2/37。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1343_bruteforce.cpp](1343_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(G sqrt N) | AC | 0.015 s | 112 KB | 11314926 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB | 11285094 |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB | 11285096 |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB | 11285099 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1343_number_theory_optimized.go](1343_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(G log N) | AC | 0.015 s | 312 KB | 11314932 |
| [1343_number_theory.java](1343_number_theory.java) \* | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB | 11285098 |
| [1343_number_theory.py](1343_number_theory.py) \* | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB | 11285097 |
| [1343_number_theory_optimized.rs](1343_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(G log N) | AC | 0.046 s | 56 KB | 11314929 |
| [1343_number_theory_optimized.java](1343_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(G·log P) | AC | 0.093 s | 500 KB | 11325016 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
