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

与 `1352_number_theory.rs` 相比：时间 0.031 s → 0.001 s；内存 216 KB → 56 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1352_parsing_optimized.go`. 在 256 字节补充缓冲上直接进行类型化转换，并完整写出紧凑输出。负整数直接以负值累积，覆盖有符号最小值，无需反射式输入或通用输出分派。 词元转换及数值输出按实际类型专门化，移除未使用的通用分支，保留算法和注释。 在当前输入块内转换完整数字段，仅在词元或块边界提交局部游标。负值累积支持有符号最小值，去掉逐位符号分支或读取调用，保留 EOF 和可选符号。

Accepted #11329135 (Go 1.14 x64): **0.015 s / 796 KB**. 历史对照: `1352_number_theory.go` (Go 1.14 x64) — 0.031 s / 1084 KB (#11285182).


`1352_number_theory_parsing_optimized.java`. 保留相同的 38 个梅森素数指数及 OEIS 引用。查询解析和答案格式化使用可复用的 1 KiB 字节缓冲，避免 StreamTokenizer、字符解码和临时十进制字符串。Runtime.halt(0) 前写完剩余字节。查询流不受缓冲大小限制，简单版本保持不变。

此精确源码有独立 Accepted，并满足统一的[排名标准](../../RATING_CRITERIA.md)。下述时间与内存来自同一次提交，重复测量可能因评测计时而不同。保留已有简单版本和不同的优化版本。

Accepted #11329348 (Java 1.8): **0.046 s / 480 KB**.

## 各语言说明

完全未修改的 CPython 源码又运行三次，结果依次为 (0.078 s, 468 KB)、(0.093 s, 400 KB)、(0.046 s, 312 KB)。表格记录最后一次真实 Accepted 的成对指标；重复测量并不代表算法本身加速。在保存的当前解释器可比样本中，该次提交按时间并列第 1/30，按内存第 11/30。内存严格小于 1 MiB（1024 KB） 时，准入仅看时间排名。清晰的基础实现已经满足条件，因此不添加重复的 optimized Python 源文件。

适用统一的[标准](../../RATING_CRITERIA.md)，没有单独第一名目标或改善
30% 准入。只有严格小于 1024 KB 才不比较内存；恰好 1024 KB 时两项均须
比较。排除快于 0.015 s 的对手，仅我们自己的时间取下限。Rust 在同语言
旧编译器回退中有三个合格对手，基础/优化时间名次 4/4、1/4 均通过，
并非空样本自动准入。

38 项常量表空间 O(1)。简单 C++/Go 流式查询/输出，仅有界 O(1) 存储。
简单 Java 保存 O(T) 输出；Python 保留拆分输入及拼接输出，Rust 保留
输入/输出 String，空间 O(I+T)，I 为输入字节。查询核心 O(T)，完整字节
解析 O(I+T)。优化 Rust/Go/Java 用固定缓冲流式处理，额外空间 O(1)。

`1352_parsing_optimized.go` 仅将检查要求的常量命名，数值、算法及注释未变。

`1352_number_theory_parsing_optimized.java` 仅将检查要求的常量命名，数值、算法及注释未变。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 116 KB | 11329301 |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1080 KB | 11329303 |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.125 s | 428 KB | 11329302 |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.046 s | 312 KB | 11326033 |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.031 s | 216 KB | 11329304 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory_optimized.rs](1352_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(Q) time; O(1) auxiliary space | AC | 0.001 s | 56 KB | 11325503 |
| [1352_parsing_optimized.go](1352_parsing_optimized.go) | Go 1.14 x64 | parsing | O(T) | AC | 0.015 s | 792 KB | 11331002 |
| [1352_number_theory_parsing_optimized.java](1352_number_theory_parsing_optimized.java) | Java 1.8 | number_theory, parsing | O(T) time; O(1) auxiliary space | AC | 0.062 s | 496 KB | 11331042 |

**当前测量。** 解法表记录所保留精确源码的最新 Accepted 结果。此前的性能比较描述历史提交；当前准入遵循统一的[排名标准](../../RATING_CRITERIA.md)。
