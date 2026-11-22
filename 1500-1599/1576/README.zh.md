# 1576. 电话资费

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · 难度 147 · implementation

原题为民间流传的题目，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三种资费：基本资费，月租 N1，每分钟 C1；组合资费，月租 N2 含 T 分钟，超出 T 的每分钟 C2；不限量资费，月租
N3。不超过 6 秒的通话免费，更长的通话按整分钟向上取整。给定至多 1000 次通话（格式 mm:ss），输出每种资费下的
月账单。

时间限制：1 秒。内存限制：64 MB。

## 输入

N1 和 C1，然后是 N2、T 和 C2，然后是 N3，它们都是 1 到 1000 之间的整数，再是
K（1 ≤ K ≤ 1000）和 K 次通话时长，格式为 mm:ss，其中 0 ≤ mm, ss ≤ 59。

## 输出

按样例格式输出三行。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

输出:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### 样例 2

输入:

```
10 2
100 1 1
1000
1
03:00
```

输出:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## 解法

把计费分钟数加起来：s 秒的通话在 s ≤ 6 时不计，否则计 ⌈s / 60⌉ 分钟。总共 M 分钟时，三种账单分别为
N1 + C1·M、N2 + C2·max(0, M − T) 和 N3，都小于 7·10⁷。`O(K)`。

注意事项：

- 恰好 6 秒的通话免费，7 秒的通话算一整分钟，恰好一分钟的通话算一分钟（测试 03）；
- 组合资费在分钟数不超过 T 时不额外收费，所以超出部分不会是负数；
- 标签按相同宽度对齐：`Basic:` 后五个空格，`Combined:` 后两个，`Unlimited:` 后一个。

## 优化解法

`1576_implementation_optimized.java`. Java 将 mm:ss 通话直接读成两个整数，不拆分字符串。至多六秒的通话免费，否则计费分钟为 mm+(ss>0)，仅保存总和。三种资费公式不变并使用 int：至多 1000 次通话、每次至多 60 计费分钟、资费参数至多 1000，使最大费用不超过 60001000。重复使用的各 1024 字节输入输出缓冲区直接输出原有标签、空格与数字，避免 StringBuilder 拼接。时间 O(K)，辅助空间 O(1)。全部 3600 个分秒组合均与按秒向上取整比较。

精确源代码 Java 1.8 Accepted #11327448：0.078 s / 356 KB。2026-11-20 保存的编译器组比较：时间 1/54、内存 1/54。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。两项均第一，也满足单独语言目标，无需星号。此前记录的优化运行 #11304530 为 0.125 s / 376 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1576_implementation_optimized.java`: 0.078 s / 356 KB; 保留教学基础版 `1576_implementation.java`: 0.109 s / 2244 KB.

`1576_implementation_optimized.rs`. 保留至多六秒免费及每个收费电话向上取整分钟。直接流式读取 k 个 mm:ss，整数读取器消费两字段间冒号，不再搜索和切分文本。仅累计收费分钟，保留三套餐公式、标签和对齐空格。O(k) 时间、O(1) 辅助空间，不改变计费规则。

与 `1576_implementation.rs` 相比：时间 0.015 s → 0.015 s；内存 232 KB → 52 KB。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1576_implementation_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB | 11287847 |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB | 11287851 |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB | 11287858 |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB | 11287853 |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB | 11287860 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation_optimized.java](1576_implementation_optimized.java) | Java 1.8 | implementation | O(K) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327448 |
| [1576_implementation_optimized.rs](1576_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(k) time; O(1) space | AC | 0.015 s | 52 KB | 11325528 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
