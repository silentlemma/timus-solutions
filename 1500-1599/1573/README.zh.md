# 1573. 炼金术

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · 难度 108 · math

原题作者 Alexander Ipatov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Sandro 有三袋各不相同的试剂：B 个蓝色、R 个红色、Y 个黄色（各 1 … 100 个）。一种药水需要配方中每种颜色的试剂
各一个，颜色互不相同。求能配出药水的试剂组合数。

时间限制：1 秒。内存限制：64 MB。

## 输入

B、R 和 Y，然后是正整数 K 以及配方中 K 种互不相同的颜色（Blue、Red 或 Yellow）。

## 输出

方法数。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入:

```
2 3 5
3
Red
Yellow
Blue
```

输出:

```
30
```

## 解法

配方中的每种颜色从自己的袋子里取一个试剂，各次选择互相独立，所以答案是配方中提到的各袋大小的乘积，至多为
100³ = 10⁶。`O(K)`。

注意事项：

- 输入中袋子的顺序是蓝、红、黄，而样例的配方先列出红色；
- 只计配方中出现的颜色（测试 02、03）。

## 优化解法

`1573_math_optimized.java`. 保留所需不同颜色袋中独立选择数的乘积。首字母 B/R/Y 唯一标识保证的 Blue/Red/Yellow，跳过剩余字符而不创建配方字符串。1024 字节输入缓冲及原始数值输出降低开销。至多三个不超过 100 的因子适合 int；K 种配方颜色需 O(K) 工作及固定辅助空间。计数证明和简单源代码不变。

精确源代码 Java 1.8 Accepted #11327456：0.093 s / 344 KB。2026-11-20 保存的编译器组比较：时间 12/82、内存 2/82。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。单独语言目标要求两项第一，故保留星号。此前记录的优化运行 #11304267 为 0.109 s / 328 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1573_math_optimized.java`: 0.093 s / 344 KB; 保留教学基础版 `1573_math.java`: 0.125 s / 1628 KB.

优化的 C++ 解法用 `scanf` 代替 `iostream` 读入，并按颜色的首字母选择袋子（Blue、
Red 和 Yellow 的首字母各不相同），而不是在以字符串为键的 `std::map` 中查找名称。
颜色读入 7 字节的缓冲区，足以容纳最长的名称 Yellow；乘积用 `int` 保存，因为它不
超过 10⁶：{1573_math_optimized.cpp}。

优化的 Rust 解法把三个袋子的大小放在三个变量中，用对颜色名称的 `match` 选出其中
一个，而不是构建 `HashMap`：{1573_math_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1573_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +69.23%; 基础版本: `1573_math.cpp`.

- `1573_math_optimized.rs`: 时间降低 -206.67%; 内存降低 +45.10%; 基础版本: `1573_math.rs`.

`1573_math_optimized.py`. 保留对配方不同颜色的可选数量相乘。把 ASCII 字节名 Blue、Red、Yellow 直接映射到整数数量，避免解码输入和文本键。O(K) 次乘法、O(K) 记号存储，K<=3 且乘积至多 10^6。改变的是表示及运行开销，不是组合计数规则。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1573_math.py` 相比：时间 0.078 s → 0.109 s；内存 452 KB → 232 KB。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1573_math_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328571 (Go 1.14 x64): **0.015 s / 948 KB**. 历史对照: `1573_math.go` (Go 1.14 x64) — 0.015 s / 1084 KB (#11287815).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1573_math_optimized.py`：在该可比样本中，时间名次 34/51，内存名次 1/51。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) | Java 1.8 | math | O(K) time; O(1) auxiliary space | AC | 0.093 s | 344 KB | 11327456 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
| [1573_math_optimized.py](1573_math_optimized.py) \* | PyPy 3.10 x64 | math | O(K) | AC | 0.109 s | 232 KB | 11324919 |
| [1573_math_optimized.go](1573_math_optimized.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 948 KB | 11328571 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
