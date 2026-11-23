# 2167. 把一个数变成质数的最小异或密钥

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · 难度 503 · bitmask, number_theory

原题作者 Vadim Barinov，出自 2022 年乌拉尔团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 T 个小于 2²⁰ 的数 a 中的每一个，求使 a XOR k 为质数的最小非负密钥 k。时间限制 2 秒，内存限制 256 MB。

## 输入

T（1 ≤ T ≤ 10⁵），然后是这些数（0 ≤ a ≤ 1 048 575）。

## 输出

每个数的最小密钥。

## 样例

### 样例 1

输入：

```
3
5
6
1
```

输出：

```
0
1
2
```

## 解法

对固定的 a，密钥 k = a XOR p 与质数 p 一一对应，所以问题是找出使 a XOR p 最小的质数 p。小于 2²⁰ 的密钥已经能得到所有小于 2²⁰ 的质数（包括 2），而更大的质数需要至少 2²⁰ 的密钥，所以只需考虑小于 2²⁰ 的质数。

p 与 a 在越高的位上相同，异或值就越小。用筛法求出小于 2²⁰ 的质数，并对每个 j 建一张表，记录是否存在以给定 j 位前缀开头的质数；每张表都是下一张表中相邻两项的 OR。查询时从高位开始确定 p 的各位：若某个质数具有保留 a 当前位后的更长前缀，就保留这一位，否则取另一位。准备 O(2²⁰ log log 2²⁰) 之后，每个数只需 20 步。

样例中 5 是质数，6 XOR 1 = 7，1 XOR 2 = 3。

C++ 教学版先筛出 U = 2²⁰ 以下的素数。对每个输入 a 按从小到大的顺序尝试密钥，直到 a XOR k 首次为素数，此时 k 就是最小密钥。取密钥 a XOR 2 可得到素数 2，因此必有小于 U 的可行密钥。穷举核对全部 U 个输入后，得到的最大答案为 95。筛法用时 O(U log log U)，空间 O(U)，该输入范围内每次查询至多查表 96 次。

## 优化解法

C++ 把同一素数前缀树按堆编号逐节点压成一位。U=2²⁰ 时 2U 位占 262144 字节；叶位就是筛：初始化奇数候选与二，清除一和奇合数。奇偶掩码不是素数或答案表。内部位取两子节点 OR。查询从根一开始，优先选择含素数且与输入位相同的子节点，令当前最高未决异或位为零。若该分支为空，只能走另一边。叶编号减 U 得到素数 p，输出输入值与 p 的异或。定长输入输出代替增长答案串。时间 O(U log log U+T log U)、空间 O(U) 位。保留简单版，其余四种语言复用达标基础版。

已通过评测的基础实现 [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go), [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java), [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py), [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`2167_bitmask_number_theory_optimized.py`. 依据每个 16 数值块中八个奇数素数位置，预计算块内 XOR 答案，单独处理素数 2。仅当当前块没有素数时，才搜索高 16 位的字典树。筛及查表数据均在运行时生成，20 位范围的全部查询已独立验证。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11328685 (Python 3.12 x64): **0.312 s / 13876 KB**. 历史对照: `2167_bitmask_number_theory.py` (Python 3.12 x64) — 0.64 s / 16760 KB (#11328350).

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`2167_number_theory_optimized.rs`. 运行时构建奇素数位筛，按递增 XOR 密钥搜索首个素数。XOR 置换有限域，故必有解；不使用预计算搜索上界，全部 20 位查询均独立验证。

Accepted #11328991 (Rust 1.75 x64): **0.031 s / 128 KB**. 历史对照: `2167_bitmask_number_theory.rs` (Rust 1.75 x64) — 0.046 s / 4172 KB (#11328351).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.093 s | 2268 KB | 11328348 |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.031 s | 3080 KB | 11295059 |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.171 s | 4856 KB | 11328349 |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.64 s | 16760 KB | 11328350 |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) | Rust 1.75 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.046 s | 4172 KB | 11328351 |
| [2167_number_theory.cpp](2167_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(U log log U + 96 T) | AC | 0.109 s | 1136 KB | 11315938 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory_optimized.cpp](2167_bitmask_number_theory_optimized.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(U log log U + T log U) | AC | 0.031 s | 336 KB | 11315846 |
| [2167_bitmask_number_theory_optimized.py](2167_bitmask_number_theory_optimized.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.312 s | 13876 KB | 11328685 |
| [2167_number_theory_optimized.rs](2167_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L + sum(K_i)) time; O(L) bits, L=2^20 | AC | 0.031 s | 128 KB | 11328991 |
