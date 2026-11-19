# 1607. 出租车

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · 难度 46 · implementation

原题作者 Denis Musin，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Petya 和出租车司机讨价还价。Petya 从 a 开始，每次加价 b；司机从 c 开始，每次降价 d；两人轮流开价，Petya 先说。
谁都不会报出越过对方的价格：司机宁可接受 Petya 的报价也不会要价更低，Petya 宁可接受司机的价格也不会出价更高。
Petya 要付多少钱？所有数都在 1 到 10000 之间。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

a、b、c 和 d。

## 输出

车费。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入:

```
150 50 1000 100
```

输出:

```
450
```

## 解法

把讨价过程模拟一遍。若 a 已不低于 c，司机直接接受。否则 Petya 加价 b，若达到司机的价格，Petya 就接受司机的价格；
接着司机降价 d，若达到 Petya 的报价，司机就接受这个报价。每轮差距至少缩小 2，所以最多约 5000 轮：`O(max(1, c - a))`。
结果已在 800 个随机输入上与独立实现对照。

注意事项：

- 将要越过对方价格的一方按对方的价格让步，所以答案总是真正报出过的价格（测试 04 和 05）；
- Petya 可能一开始就高于司机的价格，此时不必还价，Petya 付 a（测试 02）。

## 优化解法

优化的 Java 解法直接从 `System.in` 逐字节解析数字，而不是使用 `Scanner`：
316 KB，而不是 1600 KB，时间不变。

`1607_math.py`. 用闭式公式替代逐轮讨价还价。a>=c 时返回 a；否则 q=(c-a-1)//(b+d) 是双方仍未达成一致的完整轮数，下一次报价或回应以 min(a+(q+1)*b,c-q*d) 成交。b,d 为正保证可除。此版本命名为 math，模拟源文件单独保留。有界整数时间和空间 O(1)。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1607_implementation.py` 相比：时间 0.093 s → 0.156 s；内存 416 KB → 200 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1607_math.py`：在该可比样本中，时间名次 97/97，内存名次 1/97。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 132 KB | 11288177 |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 1112 KB | 11288180 |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.140 s | 1600 KB | 11288188 |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(max(1, c - a)) | AC | 0.093 s | 416 KB | 11288185 |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(max(1, c - a)) | AC | 0.031 s | 224 KB | 11288189 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1607_implementation_optimized.java](1607_implementation_optimized.java) \* | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.125 s | 316 KB | 11303763 |
| [1607_math.py](1607_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.156 s | 200 KB | 11324835 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
