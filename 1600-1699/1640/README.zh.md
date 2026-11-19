# 1640. 寒冰之环

[Timus 1640](https://acm.timus.ru/problem.aspx?space=1&num=1640) · 难度 178 · geometry

原题作者 Dmitry Ivankov（由 Alexander Ipatov 准备），出自 2008 年 10 月的乌拉尔国立大学中学生竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

恶魔站在 n 个格点上。Sandro 可以传送到任何没有恶魔的点，并以该点为圆心施放半径不超过 10000 的
寒冰之环。冰环必须杀死至少一个恶魔（落在圆周上的），而所有活着的恶魔都必须在环内。输出圆心和半径。

## 输入

n（1 ≤ n ≤ 100），然后是恶魔的坐标，均为绝对值不超过 1000 的整数，以 Sandro 当前位置为原点。所有
恶魔位置互不相同，也没有恶魔站在 Sandro 所在的点。

## 输出

圆心和半径，精度 10⁻⁹。任何合法答案都被接受。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器要求恰好三个有限数 x,y,r，满足 0<=r<=10000+1e-6。圆心与每个恶魔距离至少 1e-6，所有恶魔距圆心至多 r+1e-6，且至少一个距离与 r 相差不超过 1e-6。这是仓库检查的容差；题目另要求 1e-9 精度。

## 样例

### 样例 1

输入：

```
7
1 1
1 5
3 6
5 3
8 0
9 5
5 9
```

输出：

```
5 4 5
```

### 样例 2

输入：

```
2
0 2
2 0
```

输出：

```
1 1 1.41421356237309
```

## 解法

根本不用传送。Sandro 所在的点没有恶魔，以它为圆心、经过最远恶魔的圆会杀死那个恶魔并围住其余所有
恶魔。其半径不超过 1000 · √2，远小于 10000。`O(n)`。

易错点：

- 圆心不能落在恶魔所在的点，所以最小覆盖圆的圆心并不总能用；而起始点总是可以；
- 合法答案很多，所以检查器接受任何符合规则的圆。

## 优化解法

优化的 Java 解法输出同样的圆，但按 4 KB 字节块手工读取数，而不用 `Scanner`，因为
`Scanner` 准备正则表达式要花时间和内存：{1640_geometry_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1640_geometry_optimized.java`: 时间降低 +33.57%; 内存降低 +54.92%; 基础版本: `1640_geometry.java`.

`1640_geometry_optimized.rs`. 仍以题目保证没有恶魔的原点为圆心。逐对读取整数坐标，用 i64 精确维护 max(x*x+y*y)，最后只开一次平方根，不再对每点调用 hypot。坐标绝对值不超过 1000，平方和安全有界。半径输出十位小数。时间 O(n)，额外状态 O(1)，无需保存所有浮点输入的向量。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1640_geometry.rs` 相比：时间 0.062 s → 0.031 s；内存 268 KB → 96 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1640_geometry_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry.cpp](1640_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 148 KB | 11288466 |
| [1640_geometry.go](1640_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.015 s | 1112 KB | 11288467 |
| [1640_geometry.java](1640_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 2032 KB | 11288469 |
| [1640_geometry.py](1640_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB | 11288468 |
| [1640_geometry.rs](1640_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 268 KB | 11304017 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry_optimized.java](1640_geometry_optimized.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 916 KB | 11307283 |
| [1640_geometry_optimized.rs](1640_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 96 KB | 11325103 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
