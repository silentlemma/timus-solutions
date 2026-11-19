# 1788. 雨伞的好处

[Timus 1788](https://acm.timus.ru/problem.aspx?space=1&num=1788) · 难度 162 · greedy

原题作者 Sofia Tekhazheva（由 Denis Dublennykh 准备），出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个没带伞的女孩和 m 个带伞的男孩在雨中离开聚会。每个男孩可以用伞送一个女孩。淋湿的女孩会不高兴 gᵢ。没有送任何人的男孩会不高兴 bⱼ·k，
其中 k 是送了女孩的男孩人数。成对的女孩和男孩都不会不高兴。求最小的总不高兴值。

## 输入

n 和 m（1 ≤ n, m ≤ 100），然后是 g₁、…、gₙ，然后是 b₁、…、bₘ，都在 1 到 1000 之间。

## 输出

最小的总不高兴值。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
2 4
1 100
10 8 6 4
```

输出：

```
19
```

## 解法

固定配对数 k。此时最好让 gᵢ 最大的 k 个女孩不被淋湿，并让 bⱼ 最大的 k 个男孩去送人，因为每个落单的人都要付出自己的值（男孩还要乘以 k）。
于是总和等于最小的 n − k 个 gᵢ 之和，加上 k 乘以最小的 m − k 个 bⱼ 之和。把两个列表排序，枚举 0 到 min(n, m) 的每个 k。`O((n + m)²)`。

样例中不配对的代价是 101，两对时剩下的 6 和 4 两个男孩代价为 2·10 = 20。一对时送那位会不高兴 100 的女孩，
剩下值为 1 的女孩和值为 8、6、4 的男孩，代价 1·18，共 19。

注意事项：

- 男孩的代价随 k 增长，所以配对越多并不总是越好；
- 也要尝试 k = 0：此时没有男孩不高兴；
- 中间总和可达 2,550,000（测试 06，k = 49 或 50），即使最终答案为零；
  最优答案的最大可能值为 99,000。两者都能用 32 位整数表示。

在 150 个随机人群上（任意人群、小人群以及敏感的女孩和平静的男孩），答案与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法用 `scanf` 和 `printf` 输入输出，而不是 `iostream`：读至多 202 个
数用不着后者的运行时；排序和求和不变：{1788_greedy_optimized.cpp}。

优化的 Java 解法按 4 KB 分块读入并手工解析数字，而不是用 `Scanner`，后者的正则表
达式机制加载起来既费时间又占内存；排序和求和不变：{1788_greedy_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1788_greedy_optimized.cpp`: 时间降低 +0.00%; 内存降低 +57.43%; 基础版本: `1788_greedy.cpp`.

- `1788_greedy_optimized.java`: 时间降低 +25.60%; 内存降低 +78.62%; 基础版本: `1788_greedy.java`.

`1788_greedy_optimized.rs`. 保留选择最敏感的 k 位女生和男生的贪心策略。排序后维护未配对前缀的和；k 加一时，每个和仅减去一个当前最大剩余值。每个 k 以 O(1) 计算 girls_sum+k*boys_sum，包含 k=0，不再重新求两个切片的和。总时间 O(n log n+m log m)，空间 O(n+m)。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1788_greedy.rs` 相比：时间 0.046 s → 0.046 s；内存 232 KB → 72 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1788_greedy_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy.cpp](1788_greedy.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 404 KB | 11304222 |
| [1788_greedy.go](1788_greedy.go) | Go 1.14 x64 | greedy | O((n + m)^2) | AC | 0.031 s | 1100 KB | 11289825 |
| [1788_greedy.java](1788_greedy.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.125 s | 1852 KB | 11304227 |
| [1788_greedy.py](1788_greedy.py) | Python 3.12 x64 | greedy | O((n + m)^2) | AC | 0.093 s | 448 KB | 11304230 |
| [1788_greedy.rs](1788_greedy.rs) | Rust 1.75 x64 | greedy | O((n + m)^2) | AC | 0.046 s | 232 KB | 11304233 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy_optimized.cpp](1788_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 172 KB | 11307198 |
| [1788_greedy_optimized.java](1788_greedy_optimized.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.093 s | 396 KB | 11307199 |
| [1788_greedy_optimized.rs](1788_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(n log n+m log m) | AC | 0.046 s | 72 KB | 11325110 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
