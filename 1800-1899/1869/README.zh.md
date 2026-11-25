# 1869. 新年巡游

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · 难度 239 · prefix_sums, simulation

原题作者 Denis Dublennykh，出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一列火车从符拉迪沃斯托克（1 号站）开往莫斯科（n 号站），依次停靠 1, …, n 号站，然后沿原路返回。有 aᵢⱼ 人买了从 i 站到 j 站的票：i < j 时乘去程列车，i > j 时乘返程列车。每节车厢有 36 个座位。列车需要多少节车厢才能让每个人都有座位？

## 输入

n（2 ≤ n ≤ 100），然后是 n × n 矩阵 aᵢⱼ（0 ≤ aᵢⱼ ≤ 1000，aᵢᵢ = 0）。

## 输出

最少的车厢数。

## 评测方式

精确比较答案词元。每个新源码有完整目标环境检查、独立数学比较及哈希绑定的自身Accepted；保留简单版本的各自测量。

## 样例

### 样例 1

输入：

```
3
0 180 180
0 0 180
360 0 0
```

输出：

```
10
```

## 解法

列车必须容纳任一方向、任一区段上同时在车上的最多人数。对每个方向，在编号较小的站加上 aᵢⱼ，在编号较大的站减去它。按站号递增对这些变化求前缀和，就是每个区段的载客量。答案是最大载客量除以 36 向上取整。`O(n²)`。

样例中去程两个区段都有 360 人（1 站到 3 站的 180 人，加上 1 站到 2 站或 2 站到 3 站的 180 人），返程全程有 360 人：10 节车厢。

注意事项：

- 两个方向是不同的行程，载客量不能相加；
- 除法向上取整：37 人需要两节车厢；
- 完全没有票时答案为 0。

在 150 个随机矩阵上，答案与一个独立的已通过实现一致。

## 优化解法

`1869_prefix_sums_optimized.go`. 读矩阵时分别累计两个方向的上下车差分，再求两数组前缀和，取最大载客量向上除以 36。Go 保留原 O(n²) 差分算法，以固定缓冲整数输入替换格式扫描，并去掉未用哨兵格。Rust 相比保留的 O(n³) 直接模拟降为 O(n²)；另有原前缀和源文件仍保留，故新实现名为 prefix_sums_optimized。两版都流式消费矩阵，不保存矩阵或输入全文，以 O(n) 有符号 64 位数组存载量。n<=100、元素<=1000 时总量安全；零需求输出零。

与 `1869_prefix_sums.go` 相比：时间 0.031 s → 0.015 s；内存 1244 KB → 816 KB。

`1869_prefix_sums_optimized.rs`. 读矩阵时分别累计两个方向的上下车差分，再求两数组前缀和，取最大载客量向上除以 36。Go 保留原 O(n²) 差分算法，以固定缓冲整数输入替换格式扫描，并去掉未用哨兵格。Rust 相比保留的 O(n³) 直接模拟降为 O(n²)；另有原前缀和源文件仍保留，故新实现名为 prefix_sums_optimized。两版都流式消费矩阵，不保存矩阵或输入全文，以 O(n) 有符号 64 位数组存载量。n<=100、元素<=1000 时总量安全；零需求输出零。

与 `1869_simulation.rs` 相比：时间 0.046 s → 0.015 s；内存 320 KB → 64 KB。

五种直接模拟把每张票计入经过的所有区间，时间为 O(N³)，空间为 O(N)。它们和原有的矩阵前缀解法一起保留。优化后的 Python 每次读入一站的数据。右侧后缀和给出正向区间的贡献，左侧前缀和给出反向区间的贡献。每个向量打包成由 32 位字段组成的整数。移位一个字段后除以 2^32−1 得到后缀和，乘以该进制下由多个 1 组成的数并截断得到前缀和。字段值不超过 1000N²，因此字段之间不会进位。取两个方向上的最大载荷，除以 36 后向上取整。算法时间为 O(N²)，工作空间为 O(N)。与直接模拟相比，运行时间更短，内存占用更高。

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; 基础 `1869_simulation.py`: 0.093 s / 396 KB; 相对变化: 时间 -33.3%, 内存 +18.2%.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1869_prefix_sums_optimized.go`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

`1869_prefix_sums_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1869_simulation.cpp](1869_simulation.cpp) | G++ 13.2 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 108 KB | 11308691 |
| [1869_simulation.go](1869_simulation.go) | Go 1.14 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 1228 KB | 11308696 |
| [1869_simulation.java](1869_simulation.java) | Java 1.8 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 388 KB | 11308693 |
| [1869_simulation.py](1869_simulation.py) | Python 3.12 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 396 KB | 11308701 |
| [1869_simulation.rs](1869_simulation.rs) | Rust 1.75 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.046 s | 320 KB | 11308699 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 180 KB | 11309204 |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB | 11290934 |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.093 s | 444 KB | 11309206 |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.078 s | 1324 KB | 11309207 |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 336 KB | 11309208 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums_optimized.py](1869_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N^2) time, O(N) working space | AC | 0.062 s | 468 KB | 11310099 |
| [1869_prefix_sums_optimized.go](1869_prefix_sums_optimized.go) \* | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 816 KB | 11328315 |
| [1869_prefix_sums_optimized.rs](1869_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 64 KB | 11325130 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
