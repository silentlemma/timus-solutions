# 1385. 有趣的数

[Timus 1385](https://acm.timus.ru/problem.aspx?space=1&num=1385) · 难度 247 · math

原题作者 Alexander Ipatov，出自 2005 年 8 月彼得罗扎沃茨克夏季集训。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个没有前导零的 2N 位数，如果它既能被前 N 位组成的数整除，又能被后 N 位
组成的数整除，就称为有趣的数。求 2N 位有趣数的个数，1 ≤ N ≤ 10 000。

时间限制：1 秒。内存限制：64 MB。

## 输入

数 N。

## 输出

个数。

## 评测方式

比较一个整数词元。五份新增源码各有13个仓库测试、67次额外目标执行，含 N=1,2,3,4,4300,4301,9999,10000。仅 Python 另对 N=1..10000 全部执行。小规模计数在 N≤3 用原始整除定义核对，N=4 显式枚举倍数。不可称作每种语言各执行10000次。

## 样例

### 样例 1

输入:

```
1
```

输出:

```
14
```

这十四个数是 11、12、15、22、24、33、36、44、48、55、66、77、88 和 99。

## 解法

写作 `A*M+B`，其中 `M=10^N`、`M/10≤A<M`、`0≤B<M`。后半段允许前导零，
但作为除数必须非零。A 整除整体意味着 `B=k*A`，`1≤k≤9`。再由
`k*A | A*M+B` 得 `k | M`。每个合法 k 对应 `A=M/10..M/k−1`，共
`M/k−M/10` 种；不同 k 的方案不相交，直接相加。

教学 Go、Java、Python 用标准大整数直接算 M，枚举 k=1..9 并精确除法。存储
`O(N)` 个十进制位，算术和十进制转换的保守界为 `O(N²)`。Python 关闭默认整数
十进制转换位数限制，否则合法大 N 会失败。结果不能装入普通固定宽度整数。
旧公式源码全部保留；C++、Rust 标准库没有对应的大整数类型，采用已证明的闭式。

## 优化解法

在 k=1..9 中，能整除 `10^N` 的数只能含质因子2和5。N=1 时是1,2,5，
贡献9+4+1=14；N=2 时是1,2,4,5，贡献90+40+15+10=155。N≥3 时集合固定为
1,2,4,5,8。提出 `10^(N−3)`，得到
`(1000−100)+(500−100)+(250−100)+(200−100)+(125−100)=1575`。
输出 `1575` 再接 N−3 个零即可。这些常量由整除计数推导，不是特定输入答案表。
答案有 N+1 位，输出时间 `O(N)`。旧公式构造完整答案串，空间 `O(N)`；新 C++/Java
按有界块输出零，相对 N 只需 `O(1)` 辅助空间。

旧 Python 公式相对直接大整数教学版节省35.5%内存，时间同为0.078秒。新 Java
比大整数基础慢但更省内存，两方面均记录。未达排名目标不影响真实内存改善的准入，
对应公式源码加星号。

- `1385_math.py`: 0.078 s / 392 KB; 基础 `1385_math_number_theory.py`: 0.078 s / 608 KB; 相对变化: 时间 -0.0%, 内存 -35.5%.
- `1385_math_optimized.cpp`: 0.015 s / 120 KB; 基础 `1385_math.cpp`: 0.015 s / 372 KB; 相对变化: 时间 -0.0%, 内存 -67.7%.
- `1385_math_optimized.java`: 0.093 s / 432 KB; 基础 `1385_math_number_theory.java`: 0.078 s / 1388 KB; 相对变化: 时间 +19.2%, 内存 -68.9%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

- C++: 首选教学基础 `1385_math.cpp`; 覆盖源码 `1385_math_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 39/39.

- Go: 首选教学基础 `1385_math_number_theory.go`; 覆盖源码 `1385_math_number_theory.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1385_math_number_theory.java`; 覆盖源码 `1385_math_optimized.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 首选教学基础 `1385_math_number_theory.py`; 覆盖源码 `1385_math.py`; 时间/内存名次 2/7, 其他作者记录 20/20.

- Rust: 首选教学基础 `1385_math.rs`; 覆盖源码 `1385_math.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1385_math.cpp](1385_math.cpp) | G++ 13.2 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 372 KB | 11285827 |
| [1385_math_number_theory.go](1385_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.031 s | 1428 KB | 11308776 |
| [1385_math_number_theory.java](1385_math_number_theory.java) | Java 1.8 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 1388 KB | 11308767 |
| [1385_math_number_theory.py](1385_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 608 KB | 11308764 |
| [1385_math.rs](1385_math.rs) | Rust 1.75 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 224 KB | 11285843 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1385_math.go](1385_math.go) | Go 1.14 x64 | math | O(N) output time; O(N) string space | AC | 0.031 s | 1116 KB | 11285831 |
| [1385_math.java](1385_math.java) | Java 1.8 | math | O(N) output time; O(N) string space | AC | 0.109 s | 1648 KB | 11285839 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1385_math.py](1385_math.py) \* | Python 3.12 x64 | math | O(N) output time; O(N) string space | AC | 0.078 s | 392 KB | 11285836 |
| [1385_math_optimized.cpp](1385_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) output time; O(1) auxiliary space | AC | 0.015 s | 120 KB | 11308752 |
| [1385_math_optimized.java](1385_math_optimized.java) | Java 1.8 | math | O(N) output time; O(1) auxiliary space | AC | 0.093 s | 432 KB | 11308759 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
