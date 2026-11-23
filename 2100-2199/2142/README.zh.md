# 2142. 用双色地支付红色、蓝色和任意法力

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · 难度 127 · greedy

原题作者 Valentin Zuev，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 A 块红色地、B 块蓝色地和 C 块双色地；每块地产生一点法力，双色地可以选择产生红色或蓝色。一个法术需要 X 点红色法力、Y 点蓝色法力，以及另外 Z 点任意颜色的法力。判断这些地是否足够。时间限制 1 秒，内存限制 256 MB。

## 输入

A、B、C，然后是 X、Y、Z，都在 0 到 10⁹ 之间。

## 输出

能支付法术时输出 "It is a kind of magic"，否则输出 "There are no miracles in life"。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入：

```
3 3 1
2 2 1
```

输出：

```
It is a kind of magic
```

### 样例 2

输入：

```
5 6 5
6 5 6
```

输出：

```
There are no miracles in life
```

## 解法

红色地应当先支付红色法力，蓝色地先支付蓝色法力，因为任意颜色的部分用什么地都能付。它们付不起的部分 max(0, X − A) + max(0, Y − B) 必须由双色地来付。此后剩下的每块地，不论种类，都能支付 Z 点任意颜色法力，所以第二个条件是 A + B + C ≥ X + Y + Z。两者合起来是充要条件。和可达 3 · 10⁹，超出 32 位整数。

易错点（测试 02，即第二个样例）：能满足两种颜色的需求还不够。红色需要 6 − 5 = 1 块双色地，但总共 16 块地要付 17 点法力。

## 优化解法

`2142_greedy_optimized.go`. 保留两项充要魔法检查：双色地支付 max(0,X-A)+max(0,Y-B)，总地数还须覆盖 X+Y+Z。补足彩色缺口后，任意剩余地都可支付中立费用。保留两条精确输出语句及全零情况。和可到3·10^9，故 Go 全用 int64，Python 用精确整数。时间、状态 O(1)，字节输入和直接输出替代基础包装。 可移植的 os.Stdin.Read/os.Stdout.Write 与直接整数转换使用各 4096 字节的固定输入输出缓冲区。重复使用输出缓冲区前会处理部分写入。保留原有简单 Accepted 版本。

与 `2142_greedy.go` 相比：时间 0.031 s → 0.031 s；内存 1088 KB → 840 KB。

`2142_greedy_optimized.py`. 保留两项充要魔法检查：双色地支付 max(0,X-A)+max(0,Y-B)，总地数还须覆盖 X+Y+Z。补足彩色缺口后，任意剩余地都可支付中立费用。保留两条精确输出语句及全零情况。和可到3·10^9，故 Go 全用 int64，Python 用精确整数。时间、状态 O(1)，字节输入和直接输出替代基础包装。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `2142_greedy.py` 相比：时间 0.078 s → 0.125 s；内存 416 KB → 208 KB。

优化的 Java 解法直接从 `System.in` 逐字节读入六个数，而不是创建 `Scanner`；对只
做两次比较的程序来说，`Scanner` 的正则表达式和区域设置数据才是主要开销。和可达
3 · 10⁹，所以仍用 `long` 计算：{2142_greedy_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，并满足排名或资源改进准入条件。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `2142_greedy_optimized.java`: 时间降低 +12.80%; 内存降低 +76.67%; 基础版本: `2142_greedy.java`.

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`2142_greedy_optimized.rs`. 保留原有算法及整数类型，直接转换十进制词元，避免通用字符串解析。负数按负值累积，因此最小有符号整数也不会在取绝对值时溢出。输入存储和算法复杂度不变。

Accepted #11328634 (Rust 1.75 x64): **0.015 s / 196 KB**. 历史对照: `2142_greedy.rs` (Rust 1.75 x64) — 0.046 s / 228 KB (#11304056).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`2142_greedy_optimized.go`：在该可比样本中，时间名次 5/12，内存名次 3/12。

`2142_greedy_optimized.py`：在该可比样本中，时间名次 66/79，内存名次 1/79。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB | 11294928 |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB | 11294929 |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.125 s | 1560 KB | 11304055 |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB | 11294930 |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 228 KB | 11304056 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy_optimized.java](2142_greedy_optimized.java) | Java 1.8 | greedy | O(1) | AC | 0.109 s | 364 KB | 11304424 |
| [2142_greedy_optimized.go](2142_greedy_optimized.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 840 KB | 11328343 |
| [2142_greedy_optimized.py](2142_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(1) | AC | 0.125 s | 208 KB | 11324931 |
| [2142_greedy_optimized.rs](2142_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.015 s | 196 KB | 11328634 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
