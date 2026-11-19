# 1929. 包含指定成员且余下可分组的三人队

[Timus 1929](https://acm.timus.ru/problem.aspx?space=1&num=1929) · difficulty 385 · combinatorics

Original problem from Ural Regional School Programming Contest 2012 | by Olga Soboleva (prepared by Kirill Devyatkin).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 人中有 m 名特殊成员。每队恰好三人，且至少有一名特殊成员。
统计包含 1 号成员、并使其余所有人仍能划分为合法三人队的无序队伍。
无论余下有多少种分组方式，每个选定队伍只计一次。限制：1 秒，64 MB。

## 输入

第一行 n,m：6≤n≤999，n 能被 3 整除，1≤m≤n。
第二行给出 m 个互不相同的特殊成员编号，范围 1..n，次序任意。
1 号可能是特殊成员，也可能不是。

## 输出

一个整数，包含 1 号的可行队伍数。

## 评测方式

精确比较一个整数记号。

## 样例

```
6 4
2 3 4 6
```

```
10
```

## 解法

若 1 号特殊，令 h=1，否则 h=0。其余伙伴中有 S=m−h 名特殊成员，
U=n−m−(1−h) 名普通成员。枚举两名伙伴中特殊人数 r=0,1,2。
所选队伍移除 h+r 名特殊成员，必须满足 h+r≥1。
余下有 t=n/3−1 个队，能分组当且仅当 m−h−r≥t。

必要性：每个剩余队伍需要不同的特殊成员。充分性：先为每队指定
一名不同的特殊成员，恰有 2t 人待安排到 2t 个空位中，任意填入即可。
多余的特殊成员同样能填补空位，除此没有限制。

每个合法 r 的贡献为 C(S,r)·C(U,2−r)。不能选出的数量记作零；
C(a,0)=1、C(a,1)=a、C(a,2)=a(a−1)/2。三个情况互不重叠，
每个无序伙伴对恰好出现一次，因此求和就是答案。

读取编号耗时 O(m)，计数计算 O(1)。C++、Go、Java 流式读取，
辅助空间 O(1)；Python 和 Rust 缓冲输入，占 O(m)。

所选队伍自身也必须有特殊成员。正确移除 1 号所属类别，不要计算
伙伴次序或角色安排。剩余每队要求至少一名而非恰好一名特殊成员。
m<n/3 时答案为零；m=n/3 时每队恰好一名，公式自动涵盖。
C(0,0)=1。找到 1 号后仍应读取剩余编号。

## 优化解法

`1929_combinatorics_optimized.java`. Java 保留简单版本所述的算法和数据结构。固定字节缓冲区与 FastInput 替代 Scanner 及其正则表达式、区域设置处理。整数记号直接解析；需要字符串时仍进行 UTF-8 解码，十进制记号仍显式转换为数值。仅在需要前瞻时保存一个记号，输出算法不变。这样减少通用解析开销；表中列出算法工作量，输入扫描与字节数成正比，并使用有界输入缓冲区。

与 `1929_combinatorics.java` 相比：时间 0.125 s → 0.093 s；内存 2 368 KB → 492 KB。

Go 和 Rust 读取特殊成员编号，直到找到一号成员或读完列表，只保留这一归属标记。随后直接累加搭档中有零、一或两名特殊成员的可行数量。选出的三人组必须包含特殊成员，并为每个剩余队伍留下一名。无需保存编号集合或三人组列表。Go 使用固定字节缓冲区并直接访问标准句柄，重试中断调用并完成部分写入。

已通过评测的基础实现 [1929_combinatorics.cpp](1929_combinatorics.cpp), [1929_combinatorics.java](1929_combinatorics.java), [1929_combinatorics.py](1929_combinatorics.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。保留教学算法。复查的基础代码行使用其自身新精确源代码 Accepted 的指标与 ID；这些检查不算优化。

`1929_combinatorics_optimized.java`：在该可比样本中，时间名次 2/25，内存名次 3/25。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1929_combinatorics.cpp](1929_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(m) | AC | 0.015 s | 392 KB | 11291652 |
| [1929_combinatorics.go](1929_combinatorics.go) | Go 1.14 x64 | combinatorics | O(m) | AC | 0.031 s | 1100 KB | 11291659 |
| [1929_combinatorics.java](1929_combinatorics.java) \* | Java 1.8 | combinatorics | O(m) | AC | 0.125 s | 2368 KB | 11325555 |
| [1929_combinatorics.py](1929_combinatorics.py) \* | Python 3.12 x64 | combinatorics | O(m) | AC | 0.078 s | 492 KB | 11291667 |
| [1929_combinatorics.rs](1929_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(m) | AC | 0.046 s | 240 KB | 11291675 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1929_combinatorics_optimized.go](1929_combinatorics_optimized.go) \* | Go 1.14 x64 | combinatorics | O(m) | AC | 0.015 s | 284 KB | 11311216 |
| [1929_combinatorics_optimized.rs](1929_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(m) | AC | 0.015 s | 216 KB | 11310802 |
| [1929_combinatorics_optimized.java](1929_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(m) | AC | 0.093 s | 492 KB | 11324810 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
