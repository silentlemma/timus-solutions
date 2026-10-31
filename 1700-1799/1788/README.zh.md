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

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1788_greedy.go](1788_greedy.go).
- [1788_greedy.rs](1788_greedy.rs).

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
