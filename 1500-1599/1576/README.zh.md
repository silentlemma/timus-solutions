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

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析数字，而不是创建
`Scanner`，这样 JVM 不必加载扫描器及其正则表达式。它把一次通话读成两个数，冒号结
束分钟数，而不是按 `:` 切分 `String`；资费参数按 `int` 读入（足以容纳不超过 1000
的值），之后仍用同样的 `long` 运算：{1576_implementation_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1576_implementation_optimized.java`: 时间降低 -14.68%; 内存降低 +83.24%; 基础版本: `1576_implementation.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1576_implementation.cpp](1576_implementation.cpp).
- [1576_implementation.go](1576_implementation.go).
- [1576_implementation.rs](1576_implementation.rs).

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
| [1576_implementation_optimized.java](1576_implementation_optimized.java) | Java 1.8 | implementation | O(K) | AC | 0.125 s | 376 KB | 11304530 |
