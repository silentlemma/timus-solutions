# 1756. 一个半挖土工

[Timus 1756](https://acm.timus.ru/problem.aspx?space=1&num=1756) · 难度 179 · math

原题作者 Magaz Asanov，出自 2010 年 3 月 13 日第十一届乌拉尔国立大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

m 个挖土工每天都干活，恰好 d₁ 天挖完一条沟。安排 d₂ 天里每天有几个人干活，使同样的沟恰好 d₂ 天挖完，并且雇用的人数最少。允许某些天没有人干活。

## 输入

m、d₁ 和 d₂（1 ≤ m, d₁, d₂ ≤ 10000）。

## 输出

d₂ 个数：每天干活的人数。任何最优安排都可以。

## 样例

### 样例 1

输入：

```
3 1 2
```

输出：

```
1 2
```

## 解法

这条沟需要 W = m·d₁ 人·天。要雇的人数就是最忙那天的人数，而 d₂ 天每天至多 k 人最多完成 k·d₂ 人·天，所以至少需要 ⌈W / d₂⌉ 人。
这么多也足够：设 W = q·d₂ + r，在 d₂ − r 天安排 q 人，其余 r 天安排 q + 1 人。`O(d₂)`。

样例中 W = 3，分 2 天：一天 1 人，一天 2 人，所以雇两个人，而不是一个半。

注意事项：

- m·d₁ 可达 10⁸，32 位能装下，但值得留意；
- W < d₂ 时有些天没人干活；
- 每天的人数之和必须恰好等于 W，而不是不少于 W。

在小规模、随机和接近上限的输入上，这些安排都通过了检查总和与最忙一天的检查器；一个独立的已通过实现输出的是同样的每日人数，只是顺序不同。

## 优化解法

优化的 Java 解法手工读取三个数，而不是用 `Scanner`，只把两种可能的每日人数各格式
化一次，并通过 `BufferedOutputStream` 写出它们的字节，而不是在 `StringBuilder`
中拼出多达 10000 个数的整行：{1756_math_optimized.java}。

优化的 Python 解法只把两种可能的每日人数各格式化一次，并通过重复这两个字符串拼出
整行，而不是建立多达 10000 个整数的列表再逐个转换成字符串：
{1756_math_optimized.py}。

优化的 Rust 解法只把两种可能的每日人数各格式化一次，并直接写入 `BufWriter`，而不
是生成多达 10000 个字符串再拼接成另一个：{1756_math_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1756_math_optimized.java`: 时间降低 -36.80%; 内存降低 +77.43%; 基础版本: `1756_math.java`.

- `1756_math_optimized.py`: 时间降低 +37.60%; 内存降低 +59.93%; 基础版本: `1756_math.py`.

- `1756_math_optimized.rs`: 时间降低 +51.61%; 内存降低 +68.39%; 基础版本: `1756_math.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1756_math.cpp](1756_math.cpp).
- [1756_math.go](1756_math.go).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math.cpp](1756_math.cpp) | G++ 13.2 x64 | math | O(d2) | AC | 0.015 s | 124 KB | 11304258 |
| [1756_math.go](1756_math.go) | Go 1.14 x64 | math | O(d2) | AC | 0.031 s | 1060 KB | 11289576 |
| [1756_math.java](1756_math.java) | Java 1.8 | math | O(d2) | AC | 0.125 s | 2020 KB | 11304259 |
| [1756_math.py](1756_math.py) | Python 3.12 x64 | math | O(d2) | AC | 0.125 s | 1148 KB | 11289577 |
| [1756_math.rs](1756_math.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.031 s | 620 KB | 11304260 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math_optimized.java](1756_math_optimized.java) \* | Java 1.8 | math | O(d2) | AC | 0.171 s | 456 KB | 11307303 |
| [1756_math_optimized.py](1756_math_optimized.py) | Python 3.12 x64 | math | O(d2) | AC | 0.078 s | 460 KB | 11307291 |
| [1756_math_optimized.rs](1756_math_optimized.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.015 s | 196 KB | 11307300 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
