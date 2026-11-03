# 1748. 最复杂的数

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · 难度 268 · number_theory

原题作者 Petr Lezhankin，出自 2009 年 8 月彼得罗扎沃茨克夏季集训的乌法国立航空技术大学专场。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个数的复杂度是它的约数个数。对每个给定的 n，求 1 到 n 中最复杂的数（有多个时取最小的）及其复杂度。

## 输入

t（1 ≤ t ≤ 100），然后是 t 个数 n（1 ≤ n ≤ 10¹⁸）。

## 输出

对每个 n 输出该数及其约数个数。

## 评测方式

按词元比较输出，多余空白不影响结果。

## 样例

### 样例 1

输入：

```
5
1
10
100
1000
10000
```

输出：

```
1 1
6 4
60 12
840 32
7560 64
```

## 解法

p₁^a₁ · p₂^a₂ · … 的约数个数为 (a₁ + 1)(a₂ + 1)…，只取决于指数。把最大的指数放在最小的素数上，得到具有这些指数的最小的数，
所以答案总是形如 2^a · 3^b · 5^c · …，在连续素数上满足 a ≥ b ≥ c ≥ …。10¹⁸ 以内这样的数只有几万个，
所需素数到 53 为止，因为 2 · 3 · … · 53 已超过 10¹⁸。

通过对指数的搜索把它们全部列出、排序，再从小到大扫描并记录当前最优：只有约数严格更多时才替换最优，
这样相同时保留较小者。每个询问就是二分查找不超过 n 的最后一个数。列表中有 K = 32 749 个数，复杂度 `O(K log K + t log K)`。

当 n = 100 时答案是 60 = 2² · 3 · 5，有 3 · 2 · 2 = 12 个约数。

注意事项：

- 在接近 10¹⁸ 时相乘可能溢出 64 位，应在相乘前用除法检查边界；
- 相同时较小的数胜出：2 和 3 都有两个约数。

在 100 个不超过 20 000 的随机询问上，答案与约数个数筛法一致；在 30 个不超过 10¹⁸ 以及纪录保持者附近的随机测试上，
与一个独立的已通过实现一致。

## 优化解法

只在最大查询界限内枚举非递增素数指数。按数值维护非支配前沿，约数数目严格递增。若前驱的约数不少，新候选无用；否则删除随后约数不更多的记录。所有可能最优答案均保留，平局保留较小数。查询二分紧凑前沿，不保存并排序全部候选及独立前缀最佳数组。

C 是生成的指数候选数，R 是最大前沿大小，T 是询问数；插入可能移动 R 项。

- `1748_number_theory_optimized.cpp`: 0.015 s / 168 KB; 基础版 `1748_number_theory.cpp`: 0.015 s / 1904 KB; 相对基础版的变化: 时间 -0.0%, 内存 -91.2%.
- `1748_number_theory_optimized.go`: 0.031 s / 1136 KB; 基础版 `1748_number_theory.go`: 0.031 s / 5404 KB; 相对基础版的变化: 时间 -0.0%, 内存 -79.0%.
- `1748_number_theory_optimized.java`: 0.109 s / 488 KB; 基础版 `1748_number_theory.java`: 0.187 s / 8084 KB; 相对基础版的变化: 时间 -41.7%, 内存 -94.0%.
- `1748_number_theory_optimized.py`: 0.093 s / 536 KB; 基础版 `1748_number_theory.py`: 0.187 s / 6476 KB; 相对基础版的变化: 时间 -50.3%, 内存 -91.7%.
- `1748_number_theory_optimized.rs`: 0.031 s / 224 KB; 基础版 `1748_number_theory.rs`: 0.031 s / 1368 KB; 相对基础版的变化: 时间 -0.0%, 内存 -83.6%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1748_number_theory.cpp`; 覆盖实现 `1748_number_theory_optimized.cpp`; 时间/内存名次 1/2, 其他作者记录 71/71.

- Go: 优先教学基础版 `1748_number_theory.go`; 覆盖实现 `1748_number_theory.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1748_number_theory.java`; 覆盖实现 `1748_number_theory_optimized.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1748_number_theory.py`; 覆盖实现 `1748_number_theory_optimized.py`; 时间/内存名次 1/1, 其他作者记录 8/8.

- Rust: 优先教学基础版 `1748_number_theory.rs`; 覆盖实现 `1748_number_theory.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1904 KB | 11308921 |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB | 11289533 |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB | 11289536 |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.187 s | 6476 KB | 11308922 |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB | 11289537 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1748_number_theory_optimized.cpp](1748_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(CR+T log R) | AC | 0.015 s | 168 KB | 11309275 |
| [1748_number_theory_optimized.go](1748_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 1136 KB | 11309278 |
| [1748_number_theory_optimized.java](1748_number_theory_optimized.java) | Java 1.8 | number_theory | O(CR+T log R) | AC | 0.109 s | 488 KB | 11309276 |
| [1748_number_theory_optimized.py](1748_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(CR+T log R) | AC | 0.093 s | 536 KB | 11309274 |
| [1748_number_theory_optimized.rs](1748_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 224 KB | 11309279 |
