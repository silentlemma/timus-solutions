# 1352. 梅森素数

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · 难度 132 · number_theory

原题作者 Vladimir Yakovlev，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

梅森素数是形如 2^p − 1 的素数。给出 T 个询问，每个询问一个数 N ≤ 38，输出按从小到大顺序第 N 个梅森素数的
指数 p。

时间限制：1 秒。内存限制：64 MB。

## 输入

T，然后是 T 行，每行一个 N。

## 输出

T 行，每行一个指数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

输出：

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## 解法

没有程序能在一秒内找到这些素数：第 38 个指数是 6 972 593，即使检验一个这么大的数也需要巨大的计算量。前 38 个
梅森素数的顺序早已确定，所以解答把它们的指数列表存为常量表，每个询问直接按下标查表。`O(T)`。

注意事项：

- N 从 1 开始计数：第一个梅森素数是 2² − 1 = 3，指数为 2（测试 03）；
- 所有指数都能放进 32 位整数。

前 22 项通过对 10 000 以内所有素数指数运行 Lucas–Lehmer 检验得到验证；其余各项取自公开的列表，并与样例及题面
中提到的数值一致。

## 优化解法

`1352_number_theory_optimized.rs`. 保留题定前 38 个 Mersenne 素数指数的精确表。流式读 Q 个下标，立即经 C 运行时输出整数，不留输入/输出 String 或逐答案 to_string 分配。固定表下 O(Q) 时间、O(1) 辅助空间，不引入新素性算法或额外答案表。

与 `1352_number_theory.rs` 相比：时间 0.001 s → 0.001 s；内存 216 KB → 56 KB。

## 各语言说明

完全未修改的 CPython 源码又运行三次，结果依次为 (0.078 s, 468 KB)、(0.093 s, 400 KB)、(0.046 s, 312 KB)。表格记录最后一次真实 Accepted 的成对指标；重复测量并不代表算法本身加速。在保存的当前解释器可比样本中，该次提交按时间并列第 1/30，按内存第 11/30。内存不超过 1 MiB 时，准入仅看时间排名。清晰的基础实现已经满足条件，因此不添加重复的 optimized Python 源文件。

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1352_number_theory_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB | 11285181 |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB | 11285182 |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB | 11285186 |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.046 s | 312 KB | 11326033 |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB | 11285188 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory_optimized.rs](1352_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(Q) time; O(1) auxiliary space | AC | 0.001 s | 56 KB | 11325503 |


\* Accepted；尚未达到排名目标，该版本仍有优化空间。
