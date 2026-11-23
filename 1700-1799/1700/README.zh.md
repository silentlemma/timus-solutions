# 1700. 觉醒

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · 难度 482 · implementation

原题作者 Pavel Atnashev，出自 2009 年 4 月 4 日第十三届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每个物体有一组联想词。对若干组物体中的每一组，按字母顺序输出所有物体共有的联想词；若没有，输出 “No solution.”。

## 输入

n（2 ≤ n ≤ 1000）行 “名称: 联想词 联想词 …”，然后是 m（1 ≤ m ≤ 1000）行，每行是至少两个物体名组成的一组。
单词由小写拉丁字母组成，每行不超过 250 个字符。

## 输出

每组一行。

## 样例

### 样例 1

输入：

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

输出：

```
black
black white
No solution.
```

## 解法

以名称为键，把每个物体的联想词存成集合。对一组物体，求各成员集合的交集，排序后输出；若为空则输出 “No solution.”。
每行都很短；每组需要 `O(L²)` 次集合查询。对长为 L 的行，复杂度为 `O((n + m · L) · L log(n + L))`。

注意事项：

- 同一物体的联想词可能重复出现，但只输出一次（测试 02）；
- 一组中同一物体可能出现两次（测试 03）；
- 物体可能完全没有联想词，此时该行在冒号后就结束了。

答案与一个独立的已通过实现一致。

## 优化解法

C++/Go 将关联词映射为共享整数 ID，每对象保存排序去重的 ID 列表。查询复制最短列表，用双索引与其他列表求交，最后只对存活词汇按拼写排序输出；不修改原对象。重复成员和重复关联不影响交集。Python 流式保存 intern 字符串的 frozenset，复制最小集合后求交。三者均流式输出。T 为输入字符数、A 为最多关联数、K 为组大小、W 为词长；ID 求交 O(KA)，拼写排序 O(A log A·W)，哈希为通常期望界。共享不同词汇而非逐对象重复，且不保存完整输入输出。保留简单集合版；Java/Rust 复用符合标准的基础版。

通过评测的 Go 1.14 x64 版本耗时 0.062 秒，基础版为 0.765 秒，内存为 10 348 KB，基础版为 8908 KB。

在先前的比较快照中，基础实现 [1700_implementation.java](1700_implementation.java), [1700_implementation.rs](1700_implementation.rs) 的时间和内存均符合前 15% 或前十名的收录规则。其测量结果保留在简单版本表中。

将各组关联词存入排序数组，用双指针求交集，并逐条输出查询结果。通过的提交 11324225 用时 0.250 秒、占用 8 536 KB；简单版用时 0.437 秒、占用 12376 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1700_hashing_sorting_optimized.rs`. 为关联词分配字典序编号，从最小集合开始求有序整数集合的交集，每个查询对象仅查找一次。A 为关联条目数，Q 为查询对象名总数，W 为参与集合的长度总和，I/O 为输入输出大小。 C 入口直接调用求解函数，返回前刷新 Rust 输出；保留普通入口的原实现。

Accepted #11329024 (Rust 1.75 x64): **0.046 s / 5216 KB**. 历史对照: `1700_implementation.rs` (Rust 1.75 x64) — 0.593 s / 3584 KB (#11289079).

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 7788 KB | 11289069 |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB | 11289071 |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.437 s | 12376 KB | 11289075 |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.390 s | 13524 KB | 11289073 |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.593 s | 3584 KB | 11289079 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1700_hashing_sorting.cpp](1700_hashing_sorting.cpp) | G++ 13.2 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.046 s | 6148 KB | 11315323 |
| [1700_hashing_sorting.go](1700_hashing_sorting.go) | Go 1.14 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.062 s | 10348 KB | 11315329 |
| [1700_implementation_optimized.py](1700_implementation_optimized.py) | Python 3.12 x64 | implementation | O(T + m(KA + A log A·W)) expected | AC | 0.343 s | 8920 KB | 11315330 |
| [1700_sorting.java](1700_sorting.java) | Java 1.8 | sorting | O((n + m · L) · L log(n + L)) | AC | 0.250 s | 8 536 KB | 11324225 |
| [1700_hashing_sorting_optimized.rs](1700_hashing_sorting_optimized.rs) | Rust 1.75 x64 | hashing, sorting | O(A log A + Q log Q + W + I + O) expected time; O(A+I+O) space | AC | 0.046 s | 5216 KB | 11329024 |
