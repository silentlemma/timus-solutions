# 1011. 占比严格介于两个百分数之间的最小人口

[Timus 1011](https://acm.timus.ru/problem.aspx?space=1&num=1011) · 难度 248 · math, number_theory

原题出自 1997 年乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定两个百分数 `P` 和 `Q`（`0.01 ≤ P, Q ≤ 99.99`，小数点后至多两位，`P < Q`），求最小的正整数 `n`，
使得存在整数 `c` 满足 `P% < c / n < Q%`，两个不等号都是严格的。

时间限制：2 秒。内存限制：64 MB。

## 输入

`P` 和 `Q`，以空格或换行分隔。它们可能写成整数（`13`），也可能带一位或两位小数（`14.1`、`12.50`）。

## 输出

最小的 `n`。

## 评测方式

精确比较答案词元，空白排版无关。

- `1011_number_theory_optimized.cpp` (G++ 13.2 x64): 14个仓库测试; 115个额外精确源码比较.

- `1011_number_theory.go` (Go 1.14 x64): 14个仓库测试; 14个额外精确源码比较.

- `1011_number_theory.java` (Java 1.8): 14个仓库测试; 115个额外精确源码比较.

- `1011_number_theory_optimized.py` (PyPy 3.10 x64): 14个仓库测试.

## 样例

### 样例 1

输入：

```
10 12
```

输出：

```
9
```

### 样例 2

输入：

```
12.5
12.6
```

输出：

```
127
```

## 解法
首先避开浮点数。两个边界小数点后至多两位，因此 `p = 100·P` 和 `q = 100·Q` 都是整数（以百分之一个
百分点为单位），条件变为 `p·n < 10000·c < q·n`。

**枚举 n。** 对给定的 `n`，大于下界的最小 `c` 为 `c = ⌊p·n / 10000⌋ + 1`；当且仅当这个 `c` 仍小于
上界，即 `10000·c < q·n` 时，`n` 可行。依次尝试 `n = 1, 2, ...`。区间宽度至少为 `1/10000`，所以总有
某个 `n ≤ 10000` 可行（最大答案为 5001），枚举瞬间完成。

**Stern–Brocot 树。** 答案就是严格位于 `(p/10000, q/10000)` 内的分数的最小分母。从边界 `0/1` 和 `1/0`
出发沿 Stern–Brocot 树下降：取当前两边界的中位分数 `(a + c)/(b + d)`；若它不大于区间下界，则成为新
的左边界；若不小于区间上界，则成为新的右边界；否则它就是答案。树中第一个落入区间的分数分母最小。

注意事项：

- 把边界读成浮点数：`14.1` 在二进制中无法精确表示，与 `c / n` 在边界处的比较可能出错；
- 两个不等号都是严格的：`P = 12.5` 时 `1/8` 不在区间内；
- `n = 1` 永远不可行，因为 `0 < P` 且 `Q < 100`。

## 优化解法

保留枚举分母及逐步Stern–Brocot教学源码。快速版本保存位于开区间之外的相邻分数a/b、c/d，其中介分数是两者间最简单的分数。若仍在区间外，用精确整数商跳过该侧最长一段；被跳过的分数均已证明不合法，因此第一个区间内的中介分数具有最小分母。百分数解析为整数百分之一，WHOLE=10000，交叉相乘比较，端点相等也排除。商跳跃对应连分数下降，需O(log WHOLE)步和常量数值状态。Go使用可移植有界syscall缓冲，Python用现有文本流及表中明确的PyPy。

- `1011_number_theory_optimized.cpp`: 0.015 s / 104 KB; 基础 `1011_math.cpp`: 0.015 s / 352 KB; 相对变化: 时间 -0.0%, 内存 -70.5%.
- `1011_number_theory.go`: 0.031 s / 312 KB; 基础 `1011_math.go`: 0.015 s / 1088 KB; 相对变化: 时间 +106.7%, 内存 -71.3%.
- `1011_number_theory.java`: 0.125 s / 332 KB; 基础 `1011_math.java`: 0.125 s / 1580 KB; 相对变化: 时间 -0.0%, 内存 -79.0%.
- `1011_number_theory_optimized.py`: 0.156 s / 292 KB; 基础 `1011_number_theory.py`: 0.109 s / 468 KB; 相对变化: 时间 +43.1%, 内存 -37.6%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1011_math.cpp`; 覆盖源码 `1011_number_theory_optimized.cpp`; 时间/内存名次 1/3, 其他作者记录 155/155.

- Go: 首选教学基础 `1011_math.go`; 覆盖源码 `1011_number_theory.go`; 时间/内存名次 2/1, 其他作者记录 1/1.

- Java: 首选教学基础 `1011_math.java`; 覆盖源码 `1011_number_theory.java`; 时间/内存名次 2/1, 其他作者记录 5/5.

- Python/PyPy: 首选教学基础 `1011_number_theory.py`; 覆盖源码 `1011_number_theory_optimized.py`; 时间/内存名次 25/2, 其他作者记录 25/25.

- Rust: 首选教学基础 `1011_math.rs`; 覆盖源码 `1011_math.rs`; 时间/内存名次 1/1, 其他作者记录 1/1.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1011_math.cpp](1011_math.cpp) | G++ 13.2 x64 | math | O(answer) | AC | 0.015 s | 352 KB | 11278050 |
| [1011_math.go](1011_math.go) | Go 1.14 x64 | math | O(answer) | AC | 0.015 s | 1088 KB | 11278054 |
| [1011_math.java](1011_math.java) | Java 1.8 | math | O(answer) | AC | 0.125 s | 1580 KB | 11278060 |
| [1011_number_theory.py](1011_number_theory.py) | Python 3.12 x64 | number_theory | O(answer) tree steps | AC | 0.109 s | 468 KB | 11278057 |
| [1011_math.rs](1011_math.rs) | Rust 1.75 x64 | math | O(answer) | AC | 0.015 s | 228 KB | 11278063 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1011_number_theory.cpp](1011_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(answer) tree steps | AC | 0.015 s | 352 KB | 11278050 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1011_number_theory_optimized.cpp](1011_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.015 s | 104 KB | 11308795 |
| [1011_number_theory.go](1011_number_theory.go) \* | Go 1.14 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.031 s | 312 KB | 11309756 |
| [1011_number_theory.java](1011_number_theory.java) \* | Java 1.8 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.125 s | 332 KB | 11308797 |
| [1011_number_theory_optimized.py](1011_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.156 s | 292 KB | 11309727 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
