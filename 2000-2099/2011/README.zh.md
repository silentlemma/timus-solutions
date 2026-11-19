# 2011. 是否至少有六种不同排列

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · 难度 103 · combinatorics

原题作者 Alexey Kungurtsev，出自 2013 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 `n` 个符号，每个属于三种类型之一。用全部符号恰好组成一个长为 `n` 的词，相同符号不可区分。判断能否得到至少六个不同的词。每个给定符号必须恰好使用一次。

## 输入

第一行为 `n`，`1 ≤ n ≤ 100`。第二行为 `n` 个 1 到 3 的整数，表示类型。时间限制 0.5 秒，内存 64 MB。

## 输出

若至少有六个不同词，输出 `Yes`，否则输出 `No`。大小写必须一致，唯一答案按标记比较。

## 评测方式

按记号逐个比较输出。

## 样例

```
6
1 2 2 3 3 3
```

```
Yes
```

三类数量为 1、2、3，共有 `6!/(1!·2!·3!)=60` 个不同词，所以输出 `Yes`。

## 解法

同一种类的碎片彼此相同，所以 k 个碎片（每种分别有 c₁、c₂、c₃ 个）能组成
k!/(c₁!·c₂!·c₃!) 个不同的单词。逐个读入碎片，并对已读部分维护这个数：读到第 k 个
碎片、它的种类现在出现 c 次时，把这个数乘以 k 再除以 c，总能整除。一旦这个数达到
6，答案就是 `Yes`：把剩下的碎片按固定顺序接在后面，单词仍然互不相同。如果始终
达不到 6，答案是 `No`。`O(n)`。

每一步之前这个数不超过 5，所以 5 · 100 在任何整数类型中都放得下；要先乘后除。

注意事项：

- 恰好六个单词就已经是 `Yes`；
- 不要计算完整的阶乘：会溢出。

## 优化解法

`2011_combinatorics_optimized.py`. 保留精确多项式递推 ways=ways*length/count[value]，达到六即停止。按 4096 字节块解析到三个频数，不在提前结束前先建立全部整数列表。追加元素不会减少排列数，未读后缀不能撤销成功。最坏 O(n) 时间，有界记号及块长 B 下 O(B) 空间。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `2011_combinatorics.py` 相比：时间 0.109 s → 0.156 s；内存 516 KB → 264 KB。

`2011_combinatorics_optimized.java`. 保留增量多项式计数 ways=ways*length/count[newType]，达到六立即停止。增加符号不会减少排列数，故 Yes 后可忽略未读后缀。Java 保留原提前停止算法，只替换 Scanner。Rust 去掉完整输入 String 和解析值向量，直接消费符号类型。仅存三计数器，最坏时间 O(n)、辅助空间 O(1)。每次更新前 ways<=5、n<=100，乘积至多 500，普通整数足够，不需阶乘或大整数。保留 >=6 阈值及 Yes/No 大小写。

与 `2011_combinatorics.java` 相比：时间 0.125 s → 0.109 s；内存 1668 KB → 496 KB。

`2011_combinatorics_optimized.rs`. 保留增量多项式计数 ways=ways*length/count[newType]，达到六立即停止。增加符号不会减少排列数，故 Yes 后可忽略未读后缀。Java 保留原提前停止算法，只替换 Scanner。Rust 去掉完整输入 String 和解析值向量，直接消费符号类型。仅存三计数器，最坏时间 O(n)、辅助空间 O(1)。每次更新前 ways<=5、n<=100，乘积至多 500，普通整数足够，不需阶乘或大整数。保留 >=6 阈值及 Yes/No 大小写。

与 `2011_combinatorics.rs` 相比：时间 0.062 s → 0.046 s；内存 232 KB → 64 KB。

优化的 C++ 解法用 `scanf` 边读边统计，而不是使用 `iostream` 和向量，答案一确定就
输出：116 KB，而不是 380 KB，时间不变。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`2011_combinatorics_optimized.java`：在该可比样本中，时间名次 8/127，内存名次 10/127。

`2011_combinatorics_optimized.py`：在该可比样本中，时间名次 47/52，内存名次 1/52。

`2011_combinatorics_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB | 11292493 |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB | 11292495 |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.125 s | 1668 KB | 11303363 |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB | 11292497 |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB | 11292499 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2011_combinatorics_optimized.cpp](2011_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 116 KB | 11303791 |
| [2011_combinatorics_optimized.java](2011_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(n) | AC | 0.109 s | 496 KB | 11324782 |
| [2011_combinatorics_optimized.rs](2011_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 64 KB | 11324869 |
| [2011_combinatorics_optimized.py](2011_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(n) time; O(B) space | AC | 0.156 s | 264 KB | 11325480 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
