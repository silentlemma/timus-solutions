# 1506. 数字列

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · 难度 134 · implementation

原题作者 Stanislav Vasiliev，出自 2006 年第 31 届 ACM ICPC 叶卡捷琳堡四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 N 个 0 到 999 之间的数（1 ≤ N ≤ 100）排成 K 列（1 ≤ K ≤ N），行数尽可能少。除最
后一列可以较短外，各列高度相同。数先从上到下填满第一列，再填第二列，依此类推。每个
数在 4 个字符宽的字段中右对齐，行末没有多余空格。
保证存在恰好有 K 个非空列的合法表格。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 K，然后是 N 个数。

## 输出

排好的表格。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。 尤其要保留表格对齐以及每个字段前的填充空格。

## 样例

### 样例 1

输入:

```
7 3
1 2 30 40 50 600 700
```

输出:

```
   1  40 700
   2  50
  30 600
```

## 解法

最少的行数是 H = ⌈N / K⌉。任何合法高度 h 都满足 h ≥ H 且 (K − 1)·h < N。
由有解的保证可得 (K − 1)·H < N，因此高度 H 下最后一列非空。
第 c 列放下标从 c·H 到 c·H + H − 1 的数，所以第 r 行由
c = 0, 1, … 时存在的数 c·H + r 组成；它们在第一个用完的列处停止，而这只可能是最后
一列。每个数占 4 个字符输出，然后结束这一行。`O(N)`。

注意事项：

- 数是沿列往下排的，而不是沿行（测试 01）；
- 每个数都占 4 个字符，第一个也是，所以每行都以空格开头（测试 01）；
- 最后一列较短时，下面的行少一个数提前结束，且没有行末空格（测试 06）；
- 有解的保证不可忽略：最后一列至少有一个数（测试 06）；并非所有满足 1 ≤ K ≤ N 的组合都有解；
- K = N 时只有一行，K = 1 时只有一列（测试 03、04）。

## 优化解法

`1506_implementation_optimized.py`. 保留 height=ceil(n/k) 及按列布局。一次解析数值，直接访问 row,row+height,...，每次输出一行四字符宽右对齐字段。去掉全部格式化行的列表及数字字符串切片；仍保留输入整数列表，时间、空间 O(n)。前导填充和换行有意义。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `1506_implementation.py` 相比：时间 0.093 s → 0.125 s；内存 460 KB → 248 KB。

优化的 C++ 解法把数放在栈上 100 个 `int` 的固定数组里，而不是 `std::vector`，因
为 N ≤ 100，所以程序完全不在堆上分配内存：{1506_implementation_optimized.cpp}。

优化的 Java 解法自己补齐每个格子：用 `Integer.toString` 转换数字，并在前面补空格
到 4 个字符，而不是调用 `String.format`，后者每个格子都要新建一个格式化器并解析
格式串。不超过 999 的数最多三位，所以每个格子前面至少有一个空格：
{1506_implementation_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1506_implementation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +48.98%; 基础版本: `1506_implementation.cpp`.

- `1506_implementation_optimized.java`: 时间降低 +14.68%; 内存降低 +56.56%; 基础版本: `1506_implementation.java`.

`1506_implementation_optimized.rs`. 最多 100 个值存入固定 u16 数组，按列和行计算下标，直接输出所需填充空格。无需保存单个数字字符串、拼接的行或完整输出构造器。时间 O(N)，存储由固定数组及数字输出状态限定。 Rust 通过 C 运行库输入输出，避免完整的解码输入输出 String 和 Rust 格式化。简单且已通过评测的源代码保持不变。

与 `1506_implementation.rs` 相比：时间 0.015 s → 0.031 s；内存 252 KB → 52 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1506_implementation_optimized.py`：在该可比样本中，时间名次 279/291，内存名次 2/291。

`1506_implementation_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287283 |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11287284 |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB | 11287286 |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB | 11287285 |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB | 11287287 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation_optimized.cpp](1506_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 100 KB | 11304437 |
| [1506_implementation_optimized.java](1506_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 424 KB | 11304438 |
| [1506_implementation_optimized.rs](1506_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 52 KB | 11325099 |
| [1506_implementation_optimized.py](1506_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(n) space | AC | 0.125 s | 248 KB | 11325476 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
