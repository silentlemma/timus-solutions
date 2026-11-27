# 1157. 能拼出 N 种长方形、少 K 块时能拼出 M 种的最少瓷砖数

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · 难度 200 · number_theory

原题出自 2001 年 4 月在彼尔姆举行的乌拉尔团体程序设计锦标赛英语轮。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个男孩用他全部的正方形瓷砖拼成长方形。已知 `M`、`N`、`K`（`1 ≤ M, N ≤ 50`，
`1 ≤ K ≤ 9999`），求最小的瓷砖数 `L`，使 `L` 块瓷砖恰好能拼出 `N` 种不同的长方形，
而 `L − K` 块恰好能拼出 `M` 种。若不超过 10000 的这样的 `L` 不存在，输出 `0`。

时间限制：1 秒。内存限制：64 MB。

## 输入

整数 M、N、K 满足 1<=M,N<=50、1<=K<=9999。

## 输出

最小的 `L`，或者 `0`。

## 评测方式

按 tests.json 逐词元比较唯一整数答案，忽略空白；参考为简单
C++ 筛法。

独立分解 `1..10000` 的每个瓷砖数，通过素因子指数计算约数个数，
构造形状数参考表，其最大值为 32。实际 Python 候选程序通过 125 个查询，
包括样例、无解形状数和 `K = 9999`，以独立表中的首个匹配作为预期答案。
五份实际候选各自在 Docker 中通过仓库的 13 个输入。
这些检查并非穷举所有输入三元组。随后五份候选均取得各自的 Accepted。

## 样例

### 样例 1

输入：

```
2 3 1
```

输出：

```
16
```

## 解法

用 `x` 块瓷砖能拼出的每种长方形，对应无序约数对 `a × b = x`、`a ≤ b`；
旋转不算新形状。设 `d[x]` 为约数个数，将每个约数与其商配对，得到
`shapes[x] = (d[x] + 1) // 2`；完全平方数的中间约数与自身配对。

简单筛法对每个约数 `1..B` 的所有倍数增加 `d[x]`，其中 `B = 10000`。
每个约数恰好计入一次。按递增顺序枚举 `L = K + 1..B`，检查两种瓷砖数量
是否分别具有要求的形状数。首个匹配最小，无匹配则输出 `0`。
从 `K + 1` 开始保证 `L − K ≥ 1`，由此同时证明计数及答案选择的正确性。
时间 `O(B log B)`，辅助空间 `O(B)`。五份原始 Accepted 源码逐字节保留；
Python 另建形状数列表，原生语言基线则按需从约数表计算形状数。

## 优化解法

直接统计无序约数对。对每个较短边 `a = 1..floor(sqrt(B))`，
递增 `a², a² + a, …, B` 的计数。这恰好枚举 `a × b`、`b ≥ a`。
每个长方形有唯一的较短边，故只访问一次；正方形同样只访问一次。
使用原来的递增搜索即可得到同一答案。

每个计数仅需一字节：对于任意 `x ≤ B`，较短边最多有
`floor(sqrt(x)) ≤ 100` 个，连 Java 有符号 `byte` 也不会溢出。
表占 `10001` 字节，不含对象头、输入输出和运行时。时间仍为 `O(B log B)`，
空间仍为 `O(B)`，但增量操作更少且存储更紧凑。Java 还将 `Scanner` 换成
`StreamTokenizer`；Rust 直接解析三个数，不收集数值向量。
这是同一约数对筛法的不同实现，因此使用 `_optimized` 后缀。

本节约数对筛法适用于优化 C++、Java、Python、Rust。优化 Go
保留基础版完整约数筛，用 int 计数，再从约数数目计算形状数；
改变的是 token 读取与复用输出缓冲，并非字节表或约数对枚举。
两种筛法都需 O(B log B) 时间、O(B) 字或字节；完整输入读取器
另存 I 字节输入。

相对同语言原基线，C++ 内存 216 → 120 KB（减少 44.4%），Python
712 → 428 KB（39.9%），Java 1620 → 420 KB（74.1%）。C++、Python
记录时间不变；Java 还从 0.125 降至 0.078 秒（37.6%）。Rust 记录时间改善：
0.046 → 0.015 秒（67.4%）；内存只减少 25.3%，300 → 224 KB。
这些测量属于此前 Accepted 修订。

先前 Go 约数对实验（0.015 s / 1076 KB）未按该源码发布。
目前确有独立优化 Go 文件：完整约数筛加快速输入输出，取得
Accepted #11328509，0.031 s / 1040 KB。基础版仍保留。仅一个
计时刻度差不能证明稳定加速。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1157_number_theory_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328509 (Go 1.14 x64): **0.031 s / 1040 KB**. 历史对照: `1157_number_theory.go` (Go 1.14 x64) — 0.031 s / 1172 KB (#11281331).

当前优化 Go 修订把限制注释放回常量旁，并命名 strconv 原有
64 位宽度。表格及 Accepted #11328509（0.算法
及所有简单版本保留。

## 各语言说明

当前准入遵循统一[排名标准](../../RATING_CRITERIA.md)，不再要求
旧的第一名或改善 30%。源码绑定缓存确认：低于 1 MiB 时，两个
C++、两个 Python、两个 Rust 及优化 Java 均通过时间标准。Rust
明确回退至全部编译器，有一个合格 Rust 1.58 对手；并非空样本
或精确版本的小样本比较。此前优化 Go 的 Accepted 通过两项小
样本标准，对手为两个 Go 1.14 提交。Java/Go 基础版虽未达相应
指标仍作为教学版本保留。当前各行无星号，结论属于缓存证据。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 216 KB | 11281313 |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.031 s | 1172 KB | 11281331 |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.125 s | 1620 KB | 11281380 |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 712 KB | 11281359 |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.046 s | 300 KB | 11281448 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1157_number_theory_optimized.cpp](1157_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 120 KB | 11308304 |
| [1157_number_theory_optimized.java](1157_number_theory_optimized.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.078 s | 420 KB | 11308317 |
| [1157_number_theory_optimized.py](1157_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 428 KB | 11308301 |
| [1157_number_theory_optimized.rs](1157_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.015 s | 224 KB | 11308320 |
| [1157_number_theory_optimized.go](1157_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.015 s | 1024 KB | 11331013 |
