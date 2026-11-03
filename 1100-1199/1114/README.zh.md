# 1114. 把至多 A 个和 B 个两种颜色的相同小球放进 N 个盒子

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · 难度 194 · combinatorics, math

原题出自保加利亚 IOI 国家队第一次选拔赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一排有 `N` 个盒子（`1 ≤ N ≤ 20`），有 `A` 个相同的红球和 `B` 个相同的蓝球（`0 ≤ A, B ≤ 15`）。每个盒子里可以放任意多个任意颜色的球，盒子可以空着，球也可以不用完。求不同放法的个数。

时间限制：0.6 秒。内存限制：64 MB。

## 输入

一行 `N A B`。

## 输出

放法的个数。

## 评测方式

比较一个精确整数词元。新Python在CPython 3.12和PyPy 3.10各执行全部5120个合法三元组及12个仓库输入；每种环境另以12个独立进程运行仓库输入。预期答案用逐盒分配DP独立核对，并对每种颜色所有允许已用数量求和，覆盖零球及超过有符号64位的最大答案。保留的Java源码另有绑定哈希的组合数与无符号乘积验证，遍历全部5120个三元组。

## 样例

### 样例 1

输入：

```
2 1 1
```

输出：

```
9
```

## 解法

两种颜色独立。把最多 `A` 个红球放入 `N` 个不同盒子，可唯一扩展为
恰好 `A` 个球放入 `N + 1` 个盒子：未用球放入额外盒。反向只需删除额外盒。
隔板法计数为 `C(N + A,N)`，因此答案是
`C(N + A,N) × C(N + B,N)`。

易读 C++、Go、Java、Rust 基线建立 `TOP = 40` 的 Pascal 三角，再查两项，
时间、空间均 `O(TOP²)`；实际需要的索引至多 35。Python 直接调用两次
`math.comb`，不建表。输入界固定时均为相对合法输入规模的 `O(1)`。
五份原 Accepted 源码保留。

所需系数最多为 `C(35,15) = 3247943160 < 2^32`，不代表更大 Pascal 表的
每个单元都只有 32 位。最大答案 `10549134770590785600` 超过有符号 64 位，
但小于 `2^64`。C++、Go、Rust 用无符号 64 位乘积；Java 保留低 64 位，
用 `Long.toUnsignedString` 输出。Python 整数不限机器字长。

## 优化解法

Java 逐步乘除计算组合数：第 i 步后 r=C(N+i,i)，所以下一次除法是精确的。除法前乘积至多35*C(35,15)=113678010600，在有符号 long 内。最终答案可超出有符号64位，但小于2^64；保留低64位并用 Long.toUnsignedString 输出。省去 Pascal 表，清晰基础版全部保留。

Java凭77.4%的内存减少达标；一个计时刻度的耗时差不作为可靠提速证据。

Python优化版保留隔板公式及简短math.comb基础版。从现有标准输入流读取文本，只从sys导入标准流，逐项精确乘除计算两个组合数。第i步后coefficient=C(N+i,i)，所以除以i精确。每个因子至多C(35,15)=3247943160，除法前乘积至多113678010600。最后只将两个完整因子相乘一次，写出精确十进制字符串。Python无界整数保存最大答案10549134770590785600，超过有符号64位。无需Pascal表或math模块。O(A+B)个系数步骤，在题目界限内运算数长度有界。

本源码Accepted 11309624的实际环境为PyPy 3.10 x64，0.125秒、240KB；未改动的CPython 3.12基础版为0.078秒、372KB。内存减少35.5%，时间增加60.3%。仅凭内存收益纳入，排名未达标仍标星。两个测量各属实际提交及其解释器，并未移用指标。

- `1114_combinatorics_math.java`: 0.093 s / 372 KB; 基础 `1114_combinatorics.java`: 0.109 s / 1648 KB; 相对变化: 时间 -14.7%, 内存 -77.4%.
- `1114_combinatorics_optimized.py`: 0.125 s / 240 KB; 基础 `1114_combinatorics.py`: 0.078 s / 372 KB; 相对变化: 时间 +60.3%, 内存 -35.5%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1114_combinatorics.cpp`; 覆盖源码 `1114_combinatorics.cpp`; 时间/内存名次 1/1, 其他作者记录 45/45.

- Go: 首选教学基础 `1114_combinatorics.go`; 覆盖源码 `1114_combinatorics.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1114_combinatorics.java`; 覆盖源码 `1114_combinatorics_math.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 首选教学基础 `1114_combinatorics.py`; 覆盖源码 `1114_combinatorics_optimized.py`; 时间/内存名次 22/1, 其他作者记录 24/24.

- Rust: 首选教学基础 `1114_combinatorics.rs`; 覆盖源码 `1114_combinatorics.rs`; 时间/内存名次 1/1, 其他作者记录 1/1.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 140 KB | 11279222 |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 1060 KB | 11279223 |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O(TOP^2) | AC | 0.109 s | 1648 KB | 11279225 |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) under fixed bounds | AC | 0.078 s | 372 KB | 11279224 |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 232 KB | 11279226 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics_math.java](1114_combinatorics_math.java) | Java 1.8 | combinatorics, math | O(A+B) exact coefficient steps; bounded storage | AC | 0.093 s | 372 KB | 11308284 |
| [1114_combinatorics_optimized.py](1114_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(A+B) exact coefficient steps; bounded storage | AC | 0.125 s | 240 KB | 11309624 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
