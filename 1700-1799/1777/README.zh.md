# 1777. 阿宁迪利亚瓜人

[Timus 1777](https://acm.timus.ru/problem.aspx?space=1&num=1777) · 难度 128 · simulation

原题作者 Ivan Burmistrov，出自第十五届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

空地上有三堆大小不同的石头。每个人依次找出大小相差最小的两堆，并带来一堆恰好等于这个差的新石堆；所有石堆都留下。提问在找到两堆大小相等的那个人时结束。一共问了多少人？

## 输入

三个不同的大小 x₁、x₂、x₃（1 ≤ xᵢ ≤ 10¹⁸）。

## 输出

被问的人数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
11 5 9
```

输出：

```
3
```

## 解法

按原样模拟：把石堆排序，取相邻之差的最小值，若为 0 则停止，否则加入这么大的一堆。最小差的缩小方式与欧几里得算法中的数相似，所以过程很短：
找到的最长过程来自 10¹⁸ 附近三个相邻的斐波那契数，共问 85 人；在 10,000 个均匀随机生成的合法三元组样本中，平均问 3.7 人，中位数为 3。s 步时为 `O(s² log s)`。

样例中差为 2、4、6：第一个人带来一堆 2，第二个人又看到 9 和 11，再带来一堆 2，第三个人指出两堆 2。

注意事项：

- 找到相等两堆的那个人也要计入；
- 新堆可能与旧堆大小相同，这时下一个人就结束了；
- 大小可达 10¹⁸，需要 64 位整数。
- 随机样本的过程很短并不能确定最坏情况：测试 08 需要问 85 人。

在 90 个随机三元组上（包括斐波那契数的三元组），答案与一个独立的已通过实现一致。

## 优化解法

`1777_simulation_optimized.java`. 保留精确压缩堆模拟。最小两堆 a≤b，正最小差 g≤b−a<b。g<a 时 b−g≥a−g，故新差 min(g,a−g)；否则 g−a≤g，新差 min(g−a,b−g)。仅删除冗余绝对值与最小值运算，更新和人数计数不变。模拟 s 步为 O(s) 时间、O(1) 辅助空间，不宣称步数恒定。

精确源代码 Java 1.8 Accepted #11327759：0.109 s / 404 KB。2026-11-20 保存的编译器组比较：时间 8/77、内存 1/77。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11304426 为 0.14 s / 440 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1777_simulation_optimized.java`: 0.109 s / 404 KB; 保留教学基础版 `1777_simulation.java`: 0.14 s / 1704 KB.

优化的 C++ 解法不保存石堆列表，只记住最小的两堆 a < b 和当前最小差 g。新堆 g 不
超过 b − a，因此小于 b，排序后它的邻居只可能是 a 和 b。旧的差全都保留，所以下一
个最小差是 g、|g − a| 和 b − g 中最小的一个，而最小的两堆变为 g 和 a，或 a 和
g。每一步 `O(1)` 时间，整个过程 `O(1)` 内存，而不是反复对不断增长的向量排序；所
有数值都不超过 10¹⁸，放得进 `long long`：{1777_simulation_optimized.cpp}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1777_simulation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +47.92%; 基础版本: `1777_simulation.cpp`.

`1777_simulation_optimized.rs`. 把所有堆保存在一个有序动态向量中。扫描相邻差，对新最小差二分定位并插入，不再每步重排整个向量。若该大小已存在，直接计入下一位发现相等的人并结束。动态容量不依赖仅凭实验观察到的堆数上限。s 步中扫描与插入移动总计 O(s²)，空间 O(s)。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1777_simulation.rs` 相比：时间 0.046 s → 0.031 s；内存 252 KB → 76 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1777_simulation_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation.cpp](1777_simulation.cpp) | G++ 13.2 x64 | simulation | O(s^2 log s) for s steps | AC | 0.015 s | 192 KB | 11304057 |
| [1777_simulation.go](1777_simulation.go) | Go 1.14 x64 | simulation | O(s^2 log s) for s steps | AC | 0.031 s | 1124 KB | 11289732 |
| [1777_simulation.java](1777_simulation.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.140 s | 1704 KB | 11304058 |
| [1777_simulation.py](1777_simulation.py) | Python 3.12 x64 | simulation | O(s^2 log s) for s steps | AC | 0.093 s | 436 KB | 11289733 |
| [1777_simulation.rs](1777_simulation.rs) | Rust 1.75 x64 | simulation | O(s^2 log s) for s steps | AC | 0.046 s | 252 KB | 11304059 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation_optimized.cpp](1777_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(s) for s steps | AC | 0.015 s | 100 KB | 11304425 |
| [1777_simulation_optimized.java](1777_simulation_optimized.java) | Java 1.8 | simulation | O(s) for s simulation steps; O(1) auxiliary state | AC | 0.109 s | 404 KB | 11327759 |
| [1777_simulation_optimized.rs](1777_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(s²) for s steps | AC | 0.031 s | 76 KB | 11324872 |
