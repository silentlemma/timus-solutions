# 2102. 恰好二十个质因子

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · 难度 147 · number_theory

原题作者 Vladimir Leskov，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

判断 n 的质因数分解中指数之和是否恰好为 20，即 n 是否恰好是 20 个（计重数）质数之积。时间限制 2 秒，内存限制 64 MB。

## 输入

n（1 ≤ n ≤ 10¹⁸）。

## 输出

`Yes` 或 `No`。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
No
```

### 样例 2

输入：

```
1048576
```

输出：

```
Yes
```

### 样例 3

输入：

```
10000000000
```

输出：

```
Yes
```

## 解法

用从 2 到 B = 2·10⁶ 的每个 d 去除 n（当 d² ≤ n 时），统计除掉的质因子数。若循环因 d² 超过剩余部分而停止，剩下的是 1 或质数，贡献 0 或 1。否则剩余部分至少为 B² = 4·10¹²，因此已除掉的部分至多 10¹⁸ / B²，小于 2¹⁸，即目前不到 18 个因子；剩余部分没有小于 B 的因子且至多 10¹⁸ < B³，所以至多再贡献两个。总数不可能达到 20，答案为 No。时间复杂度为 O(min(sqrt n, B))。

第三个样例中 10¹⁰ = 2¹⁰ · 5¹⁰ 有 20 个质因子。

## 优化解法

`2102_number_theory_optimized.java`. 保留恰好 20 个质因子的判定。去掉 2、3，再试 6k-1/6k+1；enough 在乘法前用除法检查剩余最小乘积，避免溢出。只差至多两个因子时用平方捷径：只有质数平方恰含两个。Math.sqrt 仅生成候选，须精确 long root*root==n 后才接受；漏掉平方仍走原有轮式回退。至少移除 18 个因子后剩余至多 10^18/2^18，根判素试除小于 1400，回退因子上界 1953125。单个 long 逐字节读取，直接输出固定答案字节。无答案表或概率判素。实际 Java 程序通过 315488 个精确因子用例和 100000 个防溢出乘积界比较。保留教学试除版。

精确源代码 Java 1.8 Accepted #11327435：0.109 s / 468 KB。2026-11-20 保存的编译器组比较：时间 1/78、内存 1/78。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。两项均第一，也满足单独语言目标，无需星号。此前记录的优化运行 #11304532 为 0.14 s / 400 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `2102_number_theory_optimized.java`: 0.109 s / 468 KB; 保留教学基础版 `2102_number_theory.java`: 0.125 s / 1592 KB.

`2102_number_theory_optimized.py`. 仍要求恰好 20 个计重数质因子。去掉 2 和 3 后尝试 6k-1、6k+1 因子。还需两个以上因子时，divisor**remaining>n 可直接否定。只需至多两个时用精确 isqrt：仅当还需两个且平方根是质数时平方数才成功。此时已去掉至少 18 个因子，剩余数至多 10^18/2^18，对其平方根判素的试除因子小于 1400。非平方数继续轮式试除，此阶段因子上界不超过 1953125。固定输入界下空间常数，无浮点误差、概率判素或答案表。本次 Accepted 来自 PyPy 3.10；旧 CPython 指标是另一运行时的独立配对。顶层直接输出后 os._exit(0)。

精确源代码 PyPy 3.10 x64 Accepted #11327440：0.125 s / 928 KB。2026-11-20 保存的编译器组比较：时间 8/28、内存 6/28。低于 1024 KB 严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11304531（Python 3.12 x64）为 0.265 s / 424 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `2102_number_theory_optimized.py`: 0.125 s / 928 KB; 保留教学基础版 `2102_number_theory.py`: 0.453 s / 388 KB.

`2102_number_theory_optimized.cpp`. 保留精确的素因子计数和剩余乘积下界。对正数 n≤10^18，ctz 一次数完所有因子二；再除尽三，只测试 6k±1 的候选。仍需超过两个素因子时，用无符号 128 位乘法累计下界，超过余数即停。乘前下界至多 10^18、除数约至 10^9，临时积可容于 128 位。仅余两个因子时使用原平方界试除。不会给 ctz 传零，判定仍是按重数恰好二十个素因子。

精确源代码 Accepted #11326999：0.015 s / 108 KB。2026-11-20 保存的 G++ 13.2 比较：时间排名 1/113，内存排名 1/113。

### 实测改进

每个保留的优化版本均已获 Accepted。收录依据为时间和内存均列前十或前 15%，两项均列前 30% 且至少一项排名优于同语言基础版，或相对同语言基础版时间或内存至少降低 30%。负的降低比例表示开销增加。星号对应单独的语言排名目标。

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [2102_number_theory.rs](2102_number_theory.rs).

精确源代码 Accepted #11326999：0.015 s / 108 KB；保留的基础版本：0.031 s / 116 KB。比较时间时采用 0.015 s下限。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 116 KB | 11304072 |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB | 11294722 |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.125 s | 1592 KB | 11304073 |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.453 s | 388 KB | 11304074 |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB | 11294726 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory_optimized.java](2102_number_theory_optimized.java) | Java 1.8 | number_theory | Pruned trial division; O(1) storage | AC | 0.109 s | 468 KB | 11327435 |
| [2102_number_theory_optimized.py](2102_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | Pruned trial division; O(1) bounded storage | AC | 0.125 s | 928 KB | 11327440 |
| [2102_number_theory_optimized.cpp](2102_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.015 s | 108 KB | 11326999 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
