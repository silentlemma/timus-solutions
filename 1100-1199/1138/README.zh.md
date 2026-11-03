# 1138. 每次加薪都是整数百分比的最长工作序列

[Timus 1138](https://acm.timus.ru/problem.aspx?space=1&num=1138) · 难度 204 · dp

原题出自 2001 年 10 月 17–18 日在雷宾斯克举行的俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一位程序员的第一份工资恰好是 `s`，之后每份工资都是正整数，并比前一份
高出整数个百分点，最后一份不超过 `n`，`1 ≤ n, s ≤ 10000`。求最多可能有
多少份工作（包括第一份）。

时间限制：1 秒。内存限制：64 MB。

## 输入

`n` 和 `s`。

## 输出

最多的工作数。

## 评测方式

比较一个整数词元。保留的原生新增程序各有 380 次额外执行：320 个小规模精确路径枚举和 60 个边界回归。修订的教学 Python 保存了 7730 次与字面工资 DAG 预言机比较、7260 次后继集合比较、12 个仓库测试及 169 个额外 PyPy 目标测试，含最大 n。不同检查的计数不可混作原生语言总数。

## 样例

### 样例 1

输入：

```
10 2
```

输出：

```
5
```

## 解法

令 `jobs[a]` 为从 `s` 开始、以工资 `a` 结束的最多工作数。转到 `b>a` 合法当且仅当
`100(b−a)` 能被 `a` 整除。四种原生语言的教学版逐个尝试更大的整数工资，更新
`jobs[b]=max(jobs[b],jobs[a]+1)`，初始只有 `jobs[s]=1`。工资严格递增，升序就是
拓扑序；归纳可知每条最长路径都被考虑。时间 `O(n²)`，空间 `O(n)`。

已接受的教学 Python 直接枚举正整数百分比：对每个可达 `a`，尝试
`p≤floor(100(n−a)/a)`，仅当 `a*p % 100 == 0` 时转到 `a+a*p/100`。
每个合法后继恰好对应一个百分比，因此 DP 证明不变，不需要 gcd 推导。
至多 `O(P n log n)` 次检查，`P=100`，空间 `O(n)`；这不是平方级工资对枚举。
该版本由 PyPy 3.10 接受。早期 Python 工资对版本超时，不发布。

`s>n` 输出零，否则计入第一份工作。加薪必须为正，跳过不可达工资。乘积不超过
一百万，工作数不超过 10000，原生 32 位整数足够。

## 优化解法

设 `P=100`、`g=gcd(a,P)`。因为 `a/g` 与 `P/g` 互质，`a | P(b−a)` 等价于
`(a/g) | (b−a)`，所以合法后继恰为 `a+a/g,a+2a/g,…`。只生成合法工资，
不再遍历所有工资或百分比；拓扑 DP 的正确性不变。每个 `a` 至多 `Pn/a` 次更新，
加上 gcd，总时间 `O(P n log n+n log P)`，空间 `O(n)`。额外 Java 版预计算
100 个余数的 `gcd(r,100)`，并用 StreamTokenizer 代替 Scanner。

五份旧 gcd 程序全部保留。它们与直接教学枚举不同，保留原 `dp` 名称；额外
Java `_optimized` 仍是 gcd 算法。以下与各语言真正首选基础版比较。Python 比较
包含 PyPy/CPython 的变化；内存节省不代表时间和内存排名都达标。

- `1138_dp.cpp`: 0.015 s / 224 KB; 基础 `1138_bruteforce_dp.cpp`: 0.125 s / 208 KB; 相对变化: 时间 -88.0%, 内存 +7.7%.
- `1138_dp.go`: 0.031 s / 1144 KB; 基础 `1138_bruteforce_dp.go`: 0.546 s / 1140 KB; 相对变化: 时间 -94.3%, 内存 +0.4%.
- `1138_dp.java`: 0.125 s / 1680 KB; 基础 `1138_bruteforce_dp.java`: 0.296 s / 460 KB; 相对变化: 时间 -57.8%, 内存 +265.2%.
- `1138_dp.py`: 0.093 s / 508 KB; 基础 `1138_bruteforce_dp.py`: 0.140 s / 1988 KB; 相对变化: 时间 -33.6%, 内存 -74.4%.
- `1138_dp.rs`: 0.015 s / 256 KB; 基础 `1138_bruteforce_dp.rs`: 0.234 s / 236 KB; 相对变化: 时间 -93.6%, 内存 +8.5%.
- `1138_dp_optimized.java`: 0.093 s / 448 KB; 基础 `1138_bruteforce_dp.java`: 0.296 s / 460 KB; 相对变化: 时间 -68.6%, 内存 -2.6%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

- C++: 首选教学基础 `1138_bruteforce_dp.cpp`; 覆盖源码 `1138_dp.cpp`; 时间/内存名次 1/2, 其他作者记录 64/64.

- Go: 首选教学基础 `1138_bruteforce_dp.go`; 覆盖源码 `1138_dp.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1138_bruteforce_dp.java`; 覆盖源码 `1138_dp_optimized.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 首选教学基础 `1138_bruteforce_dp.py`; 覆盖源码 `1138_dp.py`; 时间/内存名次 2/3, 其他作者记录 10/10.

- Rust: 首选教学基础 `1138_bruteforce_dp.rs`; 覆盖源码 `1138_dp.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1138_bruteforce_dp.cpp](1138_bruteforce_dp.cpp) | G++ 13.2 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.125 s | 208 KB | 11308262 |
| [1138_bruteforce_dp.go](1138_bruteforce_dp.go) | Go 1.14 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.546 s | 1140 KB | 11308263 |
| [1138_bruteforce_dp.java](1138_bruteforce_dp.java) | Java 1.8 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.296 s | 460 KB | 11308265 |
| [1138_bruteforce_dp.py](1138_bruteforce_dp.py) | PyPy 3.10 x64 | bruteforce, dp | O(P n log n) time; O(n) space, P=100 | AC | 0.140 s | 1988 KB | 11309354 |
| [1138_bruteforce_dp.rs](1138_bruteforce_dp.rs) | Rust 1.75 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.234 s | 236 KB | 11308269 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1138_dp.cpp](1138_dp.cpp) | G++ 13.2 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 224 KB | 11279425 |
| [1138_dp.go](1138_dp.go) | Go 1.14 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.031 s | 1144 KB | 11279426 |
| [1138_dp.java](1138_dp.java) \* | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.125 s | 1680 KB | 11279429 |
| [1138_dp.py](1138_dp.py) \* | Python 3.12 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 508 KB | 11279428 |
| [1138_dp.rs](1138_dp.rs) | Rust 1.75 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 256 KB | 11279431 |
| [1138_dp_optimized.java](1138_dp_optimized.java) | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 448 KB | 11308275 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
