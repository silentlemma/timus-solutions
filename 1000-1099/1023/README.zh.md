# 1023. 选择让后手获胜的每步上限

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · 难度 218 · games, number_theory

原题出自 2000 年 10 月 7 日斯维尔德洛夫斯克州第二届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两名玩家轮流从一堆 `K` 颗纽扣中取走 1 到 `L` 颗；取到最后一颗的人获胜。先手已选定 `K`
（`3 ≤ K ≤ 10^8`），现在后手选择 `L`，要求 `2 ≤ L < K`。求最小的 `L`，使后手无论先手怎样走都能获胜；
若不存在则输出 0。

时间限制：2 秒。内存限制：64 MB。

## 输入

`K`。

## 输出

最小的必胜 `L`，或 0。

## 评测方式

精确比较答案词元，空白排版无关。

- `1023_games_number_theory_optimized.java` (Java 1.8): 14个仓库测试.

- `1023_games_number_theory_optimized.py` (PyPy 3.10 x64): 14个仓库测试; 1003个额外精确源码比较.

## 样例

### 样例 1

输入：

```
8
```

输出：

```
3
```

### 样例 2

输入：

```
35
```

输出：

```
4
```

## 解法

每次可取 `1..L` 枚时，轮到行动者的必败状态恰为 `L + 1` 的倍数，
包括空堆。从正倍数出发，每种合法操作都到达非倍数；从非倍数出发，
取走其除以 `L + 1` 的余数即可留下倍数，此操作合法且不超过当前枚数。
由归纳可证结论。因此后手能保证获胜，当且仅当 `(L + 1)` 整除 `K`。

求最小的约数 `d ≥ 3`，答案为 `L = d − 1`。`d = K` 总合法，所以正确输入
不会得到零。简单版本依次检查整数 `3..sqrt(K)`。如果都不整除，
大于平方根的约数所对应的较小因子只能是 1 或 2；于是只需考虑
整数且不小于 3 的 `K/2`，否则取 `K`。尤其 `K = 4` 应取 `d = 4`，不能取 2。
首个找到的约数最小，故答案正确。时间 `O(sqrt(K))`，辅助空间 `O(1)`。
五份原始 Accepted 基线逐字节保留。

## 优化解法

保留最小合法因子的博弈证明：答案d-1，其中d>=3为K的最小因子。先试3、4、5；其余候选与30互素，轮间隔(4,2,4,2,4,6,2,6)恰遍历其余可能小因子。若到sqrt(K)无因子，偶数仅余K/2，否则K。Python每个循环回边检查四个连续候选，搜索顺序和精确停止条件不变，减少热循环/JIT开销而不导入JIT控制模块。Java保持紧凑奇因子扫描。时间O(sqrt(K))、常量状态；1003个额外检查，包括大素数及上界合数，与独立直接因子枚举一致。

- `1023_games_number_theory_optimized.java`: 0.109 s / 392 KB; 基础 `1023_games_number_theory.java`: 0.109 s / 1576 KB; 相对变化: 时间 -0.0%, 内存 -75.1%.
- `1023_games_number_theory_optimized.py`: 0.140 s / 280 KB; 基础 `1023_games_number_theory.py`: 0.078 s / 400 KB; 相对变化: 时间 +79.5%, 内存 -30.0%.

`1023_games_number_theory_optimized.rs`. 保留最小可用因子的搜索以及偶数的后备处理。用 d<=K/d 作边界，无需计算 d 的平方。只需保存当前因子和输入值，时间 O(√K)，额外空间 O(1)。 Rust 通过 C 运行库输入输出，避免完整的解码输入输出 String 和 Rust 格式化。简单且已通过评测的源代码保持不变。

与 `1023_games_number_theory.rs` 相比：时间 0.015 s → 0.015 s；内存 220 KB → 56 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1023_games_number_theory_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB | 11278278 |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB | 11278279 |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB | 11278281 |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB | 11278280 |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB | 11278282 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory_optimized.java](1023_games_number_theory_optimized.java) | Java 1.8 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.109 s | 392 KB | 11308324 |
| [1023_games_number_theory_optimized.py](1023_games_number_theory_optimized.py) \* | PyPy 3.10 x64 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.140 s | 280 KB | 11309754 |
| [1023_games_number_theory_optimized.rs](1023_games_number_theory_optimized.rs) \* | Rust 1.75 x64 | games, number_theory | O(√K) | AC | 0.015 s | 56 KB | 11325081 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
