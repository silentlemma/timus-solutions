# 1184. 把电缆切成 K 段等长电缆时的最大长度

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · 难度 244 · binary_search

原题作者 Vladimir Pinaev 和 Roman Elizarov，出自 2001–2002 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 N 根电缆，切出至少 K 段相同长度的电缆，长度必须为整数厘米，求最大长度。
每段来自同一根电缆，余料不可拼接。`1≤N,K≤10000`；每根长 1 m 至 100 km，
含边界，精确到厘米。时间限制 1 秒，内存 64 MB。

## 输入

首行 N、K；接下来 N 行各一个以米为单位的长度，小数点后恰有两位。

## 输出

输出以米为单位的最大可行长度，小数部分恰有两位。若连正整数厘米长度都不能
得到 K 段，输出 `0.00`。

## 评测方式

比较唯一十进制词，必须保留两位小数。每份新程序在实际目标编译器或解释器下
通过 13 个仓库输入和 39 个独立额外输入。重读全部 156 份额外输出及退出码，
用精确有理数答案校验：合并每根的递减序列 `c/1,c/2,...`，取第 K 大值再向下
取整为厘米；不使用可行性二分。Python 候选还在主机运行 2889 组，小输入独立
枚举每个整数长度。覆盖 1.13 m、零答案、N/K=10000、总长 10¹¹、最大长度、
显式正号，以及先取 64 位最小值再缩窄。2889 是 Python 次数，不是原生次数。
四份发布源码均有各自精确字节的 Accepted。

## 样例

### 样例 1

输入：

```
4 11
8.02
7.43
4.57
5.39
```

输出：

```
2.00
```

## 解法

把每根读成整数厘米 c。既然恰有两位小数，删掉小数点即可精确转换；不要用
二进制浮点数乘 100。范围 `100≤c≤10⁷`。

试取正长度 L，一根可切 `floor(c/L)` 段。`F(L)=Σ floor(c/L)` 不递增，
故 `F(L)≥K` 是单调判定。基础版在零到最长电缆之间二分最大的可行整数 L。
零只是无正答案的哨兵，从不作除数。采用上中位数，即使下界为零，只要需要迭代，
试探值仍为正。

L 可行则更小的正长度都可行；L 不可行则更大都不可行。保留可行下侧、丢弃不可能
部分，最终剩下最大值。输出 `L/100` 与两位余数，必要时补零。时间 `O(N log C)`，
空间 `O(N)`，`C=max(c)≤10⁷`；保留的输入词也应计入。即使每根至少一米，
答案仍可能为零。

## 优化解法

`_optimized` 保留同一精确整数二分，使用更紧的已证明边界和紧凑输入存储。
设 M 为最长长度、S 为总长。最长的一根就能切 K 段长 `floor(M/K)` 的电缆，
故正的 `low=M/K` 可行，零仍作哨兵。任意可行 L 都有 `L≤M`、`K·L≤S`，
所以 `high=min(M,floor(S/K))`，不会丢掉最优解。

low<high 时取 `mid=(low+high+1)/2`，即使 low=0 仍为正。段数累加达到 K
即停止，其余项非负，判定不变。常减少实际工作，最坏仍为 `O(N log C)`。
单根长度与搜索边界适合 32 位；S 可达 `10¹¹`，原生语言必须用 64 位累加，段数
也用宽类型。尤其先在 64 位中取 `min(M,S/K)`，再转 32 位；回归例
`S/K=2³²+100` 会抓到提前截断的错误。

C++、Java 用有限字节缓冲直接读入 32 位数组，跳过长度词的小数点。Java 避免
完整输入字符串、long 数组及区域化格式器。Rust 用有限读取缓冲和 Vec<u32>，
不保留完整输入字符串或逐词替换。CPython 按规定逐行读入 `array('I')`，不保留
全部输入词或装箱 int 列表。I/O 缓冲固定，长度存储线性，五份清晰基础源码逐字节保留。

精确源码 Accepted 内存：C++ 168 对 280 KB（少 40.0%），Java 448 对
6284 KB（少 92.9%），Python 516 对 1580 KB（少 67.3%），Rust 220
对 420 KB（少 47.6%）。C++ 0.031→0.015 s 仅差一个评测计时单位，不凭此
单独准入。Java 0.125→0.093 s，Python 仍 0.078 s，Rust 仍 0.015 s。
四版均凭实测内存而非计时噪声满足条件。

## 各语言说明

五份旧实现保留直接的二分。新 Python 使用 Accepted 的 CPython 3.12，
不代入 PyPy 指标。C++、Java、Rust 已达当前目标；Python 在过滤样本中时间
第二、内存第一，故准入行保留星号，仍可改进。Go 没有符合条件的其他作者提交，
其基础版只获形式覆盖，不证明优势。C++ 两项同时前 15% 或前十名，其他语言族
两项均第一。各项内存收益均与同语言、不变的简单 Accepted 基础版比较。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB | 11283357 |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB | 11283358 |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB | 11283361 |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB | 11283360 |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB | 11283363 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1184_binary_search_optimized.cpp](1184_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.015 s | 168 KB | 11308739 |
| [1184_binary_search_optimized.java](1184_binary_search_optimized.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.093 s | 448 KB | 11308743 |
| [1184_binary_search_optimized.py](1184_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 516 KB | 11308745 |
| [1184_binary_search_optimized.rs](1184_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 220 KB | 11308751 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
