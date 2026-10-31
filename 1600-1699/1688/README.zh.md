# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · 难度 134 · implementation

原题作者 Alexander Ipatov，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三名队员点的东西一样，每次都由其中一人买单。另一名队员在别人替其支付的钱（每张账单的三分之一）超过 n 时即可退出。
按顺序给出账单，判断在第几次聚餐之后会发生这件事。

## 输入

n 和 m（1 ≤ n ≤ 2 · 10⁹；0 ≤ m ≤ 3000），然后是 m 张账单，均为 1 到 2 · 10⁶ 之间的整数。

## 输出

对第一次满足条件的聚餐 x 输出 “Free after x times.”，若始终不满足则输出 “Team.GOV!”。

## 样例

### 样例 1

输入：

```
1666 5
2000
1024
900
1156
1200
```

输出：

```
Free after 4 times.
```

### 样例 2

输入：

```
3000 5
2000
1024
900
1156
1200
```

输出：

```
Team.GOV!
```

## 解法

维护账单的累计和。份额 total / 3 超过 n 当且仅当 total > 3n，这样就不用处理分数；
在第一次满足该条件时停下。`O(m)`。

注意事项：

- 3n 可达 6 · 10⁹，累计和也一样：要用 64 位整数（测试 06）；
- 份额恰好等于 n 还不够，比较是严格的（测试 04 和 06）。

答案与一个独立的已通过实现一致。

## 优化解法

优化的 Java 解法从一个 4 KB 的缓冲区逐字节解析数字，缓冲区读完后再从 `System.in`
重新填充，而不是先把全部输入复制到 `StringBuilder`，再为分词复制成另一个字符串。
即使答案已经确定，它也会读完全部 m 张账单；总额和 3n 都可能达到 6 · 10⁹，所以都
用 `long` 保存：{1688_implementation_optimized.java}。

优化的 Python 解法通过遍历 `sys.stdin.buffer` 的生成器逐行取出词元，而不是读入全
部输入再转换成最多 3002 个整数的列表；累计总额的方式与简单解法相同：
{1688_implementation_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1688_implementation_optimized.java`: 时间降低 -60.26%; 内存降低 +62.20%; 基础版本: `1688_implementation.java`.

- `1688_implementation_optimized.py`: 时间降低 +0.00%; 内存降低 +44.67%; 基础版本: `1688_implementation.py`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1688_implementation.cpp](1688_implementation.cpp).
- [1688_implementation.go](1688_implementation.go).
- [1688_implementation.rs](1688_implementation.rs).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 128 KB | 11304065 |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB | 11288883 |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB | 11288886 |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB | 11288885 |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 232 KB | 11304066 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation_optimized.java](1688_implementation_optimized.java) | Java 1.8 | implementation | O(m) | AC | 0.125 s | 384 KB | 11304439 |
| [1688_implementation_optimized.py](1688_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 436 KB | 11304440 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
