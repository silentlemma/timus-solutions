# 1551. 相扑比赛

[Timus 1551](https://acm.timus.ru/problem.aspx?space=1&num=1551) · 难度 257 · math, sorting

原题作者 Sergey Pupyrev，出自 2007 年 4 月 21 日在叶卡捷琳堡举行的第十一届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一场淘汰赛有 2ᴺ 名相扑选手（1 ≤ N ≤ 10），共 N 轮；每名选手代表一个县。组织者可以选择初始
对阵表。求最大的 K，使得存在某个对阵表，无论比赛结果如何，至少有 K 轮中不会有同县选手相遇。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后 2ᴺ 行，每行是选手名和所属县。
两个字段都由 1–30 个拉丁字母组成。

## 输出

K。

## 评测方式

比较一个整数词元。新Python通过168组分布，对照独立哈希频数：大小写、30字母字段、全异/全同组及最多1024名选手。

## 样例

### 样例 1

输入:

```
3
Homasho Ishikawa
Tamakasuga Tokyo
Futeno Tochigi
Takekaze Tokyo
Kasugao Yamaguchi
Kotoshogiku Ishikawa
Kotomitsuki Tokyo
Miyabiyama Shizuoka
```

输出:

```
1
```

## 解法

第 r 轮把规模为 2^(r−1) 的块两两配对，由于块中任何选手都可能胜出，第 r 轮安全当且仅当每个规
模为 2^r 的块的两半没有共同的县。

取人数最多的县，设有 c 名选手，并让该县选手在对阵其他县时总是获胜。该县选手只有互相对阵时才会
被淘汰，每个不安全的轮次最多将其人数减少一半。因此，从 c 人减少到一人至少需要 ⌈log₂ c⌉ 个
不安全的轮次，所以 K ≤ N − ⌈log₂ c⌉。

这个上界可以达到：对最大的 c 取 k = ⌈log₂ c⌉，把选手按县排序后轮流分进顶部 k 层的 2ᵏ 个块。
每个县至多 2ᵏ 人，所以他们落在不同的块里；每个块内的人都来自不同的县，所以前 N − k 轮都安全。
因此答案为 N − ⌈log₂ c⌉。统计各县人数并取最大值，将 k 从零开始递增，直到 2ᵏ ≥ c，输出 N − k。
穷举对阵表和比赛结果的独立算法在 N ≤ 3 的全部 29 种人数分布及 1200 个随机输入上均与解答一致。
计数需 `O(2ᴺ log 2ᴺ)`。

注意事项：

- 只有一个县时没有安全的轮次（测试 02、04）；
- c = 4 只需两轮不安全，c = 5 需要三轮（测试 06、07）；
- 县名按原样比较，Tokyo 和 tokyo 不同（测试 08）。
- 选手名不影响计数；但两个字段仍须由 1–30 个拉丁字母组成，不能带数字后缀（测试 04–07）。

## 优化解法

答案仍只依赖最大都道府县频数 c：`N−ceil(log2 c)`。紧凑 C++/Java 读取时丢弃选手姓名并立即更新最大频数；C++ 保留有序 map，Java 使用 hash map 及有界字节输入。Python 只保留都道府县字符串，排序后求最长相同段。每个名称恰为一个连续块，块长就是频数。这样省去 Counter 导入、选手姓名词元及独立哈希表项。Python 以 `O(M log M)` 排序（`M=2^N`）换取较少实测内存，不宣称加速。比较完整且区分大小写的字符串，不用可能碰撞的指纹。`bit_length(c−1)` 精确给出向上取整对数。包括直接 Counter 在内的简单版本全部保留。

- `1551_math_optimized.cpp`: 0.015 s / 308 KB; 基础 `1551_math.cpp`: 0.015 s / 544 KB; 相对变化: 时间 -0.0%, 内存 -43.4%.
- `1551_math_optimized.java`: 0.093 s / 568 KB; 基础 `1551_math.java`: 0.156 s / 3280 KB; 相对变化: 时间 -40.4%, 内存 -82.7%.
- `1551_math_sorting.py`: 0.093 s / 464 KB; 基础 `1551_math.py`: 0.062 s / 696 KB; 相对变化: 时间 +50.0%, 内存 -33.3%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1551_math.cpp`; 覆盖源码 `1551_math_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 47/47.

- Go: 首选教学基础 `1551_math.go`; 覆盖源码 `1551_math.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1551_math.java`; 覆盖源码 `1551_math_optimized.java`; 时间/内存名次 1/1, 其他作者记录 4/4.

- Python/PyPy: 首选教学基础 `1551_math.py`; 覆盖源码 `1551_math_sorting.py`; 时间/内存名次 61/4, 其他作者记录 139/139.

- Rust: 首选教学基础 `1551_math.rs`; 覆盖源码 `1551_math.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1551_math.cpp](1551_math.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 544 KB | 11287591 |
| [1551_math.go](1551_math.go) | Go 1.14 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.031 s | 1276 KB | 11287592 |
| [1551_math.java](1551_math.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.156 s | 3280 KB | 11287596 |
| [1551_math.py](1551_math.py) | Python 3.12 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.062 s | 696 KB | 11287594 |
| [1551_math.rs](1551_math.rs) | Rust 1.75 x64 | math | O(M) expected frequency work, M=2^N | AC | 0.046 s | 576 KB | 11287598 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1551_math_optimized.cpp](1551_math_optimized.cpp) | G++ 13.2 x64 | math | O(M log M) | AC | 0.015 s | 308 KB | 11309254 |
| [1551_math_optimized.java](1551_math_optimized.java) | Java 1.8 | math | O(M) expected frequency work, M=2^N | AC | 0.093 s | 568 KB | 11309256 |
| [1551_math_sorting.py](1551_math_sorting.py) \* | Python 3.12 x64 | math, sorting | O(M log M) time; O(M) strings | AC | 0.093 s | 464 KB | 11309558 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
