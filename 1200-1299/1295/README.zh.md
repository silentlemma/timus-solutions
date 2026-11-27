# 1295. 胡思乱想

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · 难度 151 · number_theory

原题作者 Den Raskovalov，出自 2004 年 3 月 13 日第九届中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

当 1 ≤ n ≤ 300 000 时，十进制数 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ 末尾有几个零？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

一个整数 n，`1 ≤ n ≤ 300000`。

## 输出

末尾零的个数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
8
```

输出：

```
0
```

### 样例 2

输入：

```
7
```

输出：

```
2
```

## 解法

n 最大时这个和超过 180 000 位，但末尾零的个数受其中 2 的幂次限制。设 S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ。

- n = 1：S = 10，一个零。
- n 为偶数：1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4)，而 2ⁿ、4ⁿ 是 4 的倍数，所以 S 能被 2 整除但不能被 4
  整除。
- n 为奇数且 n ≥ 3：3ⁿ ≡ 3 (mod 8)，所以 1ⁿ + 3ⁿ ≡ 4 (mod 8)，而 2ⁿ 和 4ⁿ 是 8 的倍数；S 能被
  4 整除但不能被 8 整除。

因此 S 末尾不会有三个零，一切由 S mod 100 决定：为 0 时两个零，末位为 0 时一个零，否则没有。
四个幂模 100 的值用快速幂求出。`O(log n)`。

实际上答案只取决于 n mod 20：n 被 4 整除时为 0，n 模 4 余 3 或模 20 余 5 时为 2，其余为 1。
解法直接计算，而不依赖这张表。

注意事项：

- n 模 4 余 1 时通常只有一个零，但 n = 5、25、… 有两个（测试 05 和 06）；
- 完整的和可以用高精度构造，但完全没有必要：只有最后两位重要。

对 3000 以内的每个 n，结果都与高精度精确和比较过。

## 优化解法

`1295_math.java`. 闭式同余公式替代模幂：n 被 4 整除时尾零为零；n mod 4=3 或 n mod 20=5 时两个；否则一个。模 5 判是否有零，奇数情形模 25 展开判第二个，模 8 排除第三个，n=1 单独为 10。未嵌入答案表。算术及存储 O(1)，另需读取十进制输入。不同算法命名 math，保留模幂替代版及教学版。实际公式对全部 n=1..300000 与独立模幂比较。

Java 1.8 精确源码 #11327403 为 `0.078 s / 340 KB`，2026 年 11 月
20 日保存的时间和内存排名均为 2/67。内存低于 1024 KB 时只要求时间，
故公式版达标。不同的模幂版本 #11305839 为 `0.109 s / 324 KB`；时间
排名 12/67 未进前十或向上取整为 11 的前 15%，因此保留星号，
并无另一套语言第一名要求。

- `1295_math.java`: 0.078 s / 340 KB; 保留教学版 `1295_number_theory.java` (Java 1.8): 0.125 s / 1600 KB.

未改动的 Python 文件选用 CPython 3.12 #11327024
`0.062 s / 660 KB`，时间排名 1/57、内存排名 30/57，按时间达标。
基础 #11284644 为 `0.093 s / 464 KB`，所选运行更快但内存更多。
同文件此前记录的 PyPy 3.10 #11325070 为 `0.125 s / 200 KB`，
更慢但内存更低。不混合不同运行/编译器的配对数据；后文省内存说明
指历史 PyPy 配对。直接复用文件，无需副本或额外语言准入目标。

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析 `n`，而不是创建
`Scanner`，这样 JVM 不必加载扫描器及其正则表达式；模 100 的幂运算不变：
{1295_number_theory_optimized.java}。

### 实测改进

以下是单独的配对测量，并不表示全部改善 30%，也不是另一套准入规则。Go
#11328536 相对基础 #11284638 时间仍为 `0.031 s`，内存从 1080 降至
936 KB，仅减少 13.3%。它凭稀疏时间比较达标，并非节省 30%。负的减少
比例表示开销增加；保留教学源码及不同的旧实现。

- `1295_number_theory_optimized.java`: 时间降低 +12.80%; 内存降低 +79.75%; 基础版本: `1295_number_theory.java`.

`1295_number_theory_optimized.py`. 保留模 100 判断末尾零数的论证，直接计算 1+pow(2,n,100)+pow(3,n,100)+pow(4,n,100)，不用四个底数的生成器。模幂不构造巨大整数。已证明至多两个末尾零，因此余零对应二，可被十整除对应一，否则零。时间 O(log n) 次有界模运算，状态 O(1)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1295_number_theory.py` 相比：时间 0.093 s → 0.125 s；内存 464 KB → 200 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1295_number_theory_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328536 (Go 1.14 x64): **0.031 s / 936 KB**. 历史对照: `1295_number_theory.go` (Go 1.14 x64) — 0.031 s / 1080 KB (#11284638).

## 各语言说明

全部语言采用统一[排名标准](../../RATING_CRITERIA.md)：所需指标普通前十或前
15%，同编译器有 1–10 个有效对手时以参考比较替代排名。内存小于 1024 KB
时只要求时间。排除快于 `0.015 s` 的对手，只给自己的时间设置该比较下限。
同值共享排名，百分比截点向上取整。不设日期/ID 门槛、单独第一名要求
或仅凭改善 30% 准入。算法、注释及 Accepted 配对表格均不变。

11 月 18 日旧 PyPy 排名（时间 37/57、内存 1/57）为历史记录。绑定源码的
冻结审计接纳 C++、公式 Java、所选 CPython、优化 Go 和简单 Rust。Go
三个对手的时间上限为 `0.062 s`，基础 Go 超出其 1076.40 KB 内存上限。
Rust 通过唯一对手的 `0.062 s` 时间上限。简单 Go、Java、Python 虽未通过
所需比较，仍保留用于教学。

当前 Go 仅按严格检查要求将转换位宽 64 提取为 `numericBits`。#11328536
及上述比较对应此前的精确字节。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
| [1295_math.java](1295_math.java) | Java 1.8 | math | O(1) arithmetic/storage + decimal input | AC | 0.078 s | 340 KB | 11327403 |
| [1295_number_theory_optimized.py](1295_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.062 s | 660 KB | 11327024 |
| [1295_number_theory_optimized.go](1295_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 932 KB | 11331007 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
