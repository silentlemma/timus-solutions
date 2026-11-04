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

五种直接模拟把每张票计入经过的所有区间，时间为 O(N³)，空间为 O(N)。它们和原有的矩阵前缀解法一起保留。优化后的 Python 每次读入一站的数据。右侧后缀和给出正向区间的贡献，左侧前缀和给出反向区间的贡献。每个向量打包成由 32 位字段组成的整数。移位一个字段后除以 2^32−1 得到后缀和，乘以该进制下由多个 1 组成的数并截断得到前缀和。字段值不超过 1000N²，因此字段之间不会进位。取两个方向上的最大载荷，除以 36 后向上取整。算法时间为 O(N²)，工作空间为 O(N)。与直接模拟相比，运行时间更短，内存占用更高。

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; 基础 `1869_simulation.py`: 0.093 s / 396 KB; 相对变化: 时间 -33.3%, 内存 +18.2%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1869_simulation.cpp`; 覆盖源码 `1869_simulation.cpp`; 时间/内存名次 1/1, 其他作者记录 45/45.

- Go: 首选教学基础 `1869_simulation.go`; 覆盖源码 `1869_simulation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1869_simulation.java`; 覆盖源码 `1869_simulation.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 首选教学基础 `1869_simulation.py`; 覆盖源码 `1869_prefix_sums_optimized.py`; 时间/内存名次 1/1, 其他作者记录 9/9.

- Rust: 首选教学基础 `1869_simulation.rs`; 覆盖源码 `1869_simulation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

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
