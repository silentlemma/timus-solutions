# 1864. 在 Den 家聚会

[Timus 1864](https://acm.timus.ru/problem.aspx?space=1&num=1864) · 难度 177 · math

原题为民间流传的题目（由 Daniil Ayzenshteyn 准备），出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个朋友来到 Den 家；第 i 个朋友买了 aᵢ 升果汁，包括 Den 在内的每个人喝得一样多。随后 Den 拿出 100 卢布，支付那些被非购买者喝掉的果汁，在买得比喝得多的朋友之间公平分配。每个朋友向下取整后能得到多少卢布？

## 输入

n（2 ≤ n ≤ 100），然后是 a₁, …, aₙ（0 ≤ aᵢ ≤ 100），总和为正。

## 输出

每个朋友得到的卢布数，向下取整。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
3
10 10 10
```

输出：

```
33 33 33
```

### 样例 2

输入：

```
2
10 0
```

输出：

```
100 0
```

## 解法

总共 S 升时，n + 1 个人每人喝 S/(n + 1)，所以朋友 i 为别人买了 aᵢ − S/(n + 1) 升（若为正），否则为零。钱按这些量的比例分配。全部乘以 n + 1 就都是整数：eᵢ = max(0, aᵢ(n + 1) − S)，朋友 i 得到 ⌊100·eᵢ / Σ e⌋。
总和永远不为 0：朋友们一共买了 S，却只喝了 nS/(n + 1)。`O(n)`；Python 为 `O(n²)`。

在第一个样例中，每人喝了 7.5 升，每个朋友替 Den 付了 2.5 升，所以钱三人平分：向下取整后各 33。

注意事项：

- Den 也喝，所以每份是 S/(n + 1)，而不是 S/n；
- 买得比喝得少的朋友什么也得不到；
- 精确的整数运算避免了向下取整的任何疑问。

在两百次随机聚会上，分配结果与一个独立的已通过实现一致。

## 优化解法

`1864_math_optimized.py`. 保留精确缩放超付 credit[i]=max(0,(N+1)*bought[i]-total) 及 floor(100*credit[i]/sum(credits))。输入 total 为正，截掉负值前 credit 总和等于 total，截断后的分母必为正。整数计算避免舍入误差。公共分母只算一次，时间 O(N)。 基础生成器为每个朋友重算 sum(over)，耗时 O(N²)；现在缓存一次。购买量、超付与拼接输出仍占 O(N) 空间。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `1864_math.py` 相比：时间 0.093 s → 0.14 s；内存 412 KB → 212 KB。

`1864_math_optimized.rs`. 保留精确缩放超付 credit[i]=max(0,(N+1)*bought[i]-total) 及 floor(100*credit[i]/sum(credits))。输入 total 为正，截掉负值前 credit 总和等于 total，截断后的分母必为正。整数计算避免舍入误差。公共分母只算一次，时间 O(N)。 复用一个固定100项 i64 数组，先存购买量后存超付，去掉多个向量及答案字符串。数组显式存储800字节加常数状态；N<=100、购买量<=100 保证乘积安全。 Rust 版本通过 C 运行库读写，不保留解码后的输入 String，也不构造格式化的输出 String。保留简单版本及其 Accepted。

与 `1864_math.rs` 相比：时间 0.031 s → 0.046 s；内存 236 KB → 48 KB。

优化的 C++ 解法计算同样的份额，但把购买量和多出的量存在两个各 100 个数的固定数组
中（因为 `n ≤ 100`，这已足够），而不是堆上的两个向量：
{1864_math_optimized.cpp}。

优化的 Java 解法计算同样的份额，但用 `BufferedReader` 和 `StringTokenizer` 读
数，而不用 `Scanner`，因为 `Scanner` 准备正则表达式要花时间和内存：
{1864_math_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1864_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +45.83%; 基础版本: `1864_math.cpp`.

- `1864_math_optimized.java`: 时间降低 +0.00%; 内存降低 +69.77%; 基础版本: `1864_math.java`.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1864_math_optimized.py`：在该可比样本中，时间名次 18/20，内存名次 1/20。

`1864_math_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math.cpp](1864_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 192 KB | 11304246 |
| [1864_math.go](1864_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1116 KB | 11290890 |
| [1864_math.java](1864_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1720 KB | 11290894 |
| [1864_math.py](1864_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.093 s | 412 KB | 11290893 |
| [1864_math.rs](1864_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11304247 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math_optimized.cpp](1864_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 104 KB | 11307321 |
| [1864_math_optimized.java](1864_math_optimized.java) \* | Java 1.8 | math | O(n) | AC | 0.125 s | 520 KB | 11307325 |
| [1864_math_optimized.py](1864_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.14 s | 212 KB | 11325076 |
| [1864_math_optimized.rs](1864_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 48 KB | 11325116 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
