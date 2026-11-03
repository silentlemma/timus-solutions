# 2144. 把密封盒子排成一个有序队列

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · 难度 221 · sorting

原题作者 Ivan Smirnov，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 个盒子，每个盒子里是一排固定的手办尺寸，不能重新排列也不能倒过来。判断能否把盒子按某种顺序摆放，使所有尺寸合起来构成一个不降序列。时间限制 0.5 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 100），然后对每个盒子给出 kᵢ（1 ≤ kᵢ ≤ 100）及其尺寸（1 ≤ aᵢⱼ ≤ 10⁴）。

## 输出

YES 或 NO。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入：

```
3
2 1 2
3 7 7 7
1 5
```

输出：

```
YES
```

### 样例 2

输入：

```
2
2 1 3
1 2
```

输出：

```
NO
```

## 解法

每个盒子内部必须不降。此后只有它的第一个尺寸 f 和最后一个尺寸 l 有关系，合法顺序要求每个盒子的 l 不超过下一个盒子的 f。

在任何合法顺序中，第一个尺寸都不降，因为 f ≤ l ≤ 下一个盒子的 f。在第一个尺寸同为 f 的盒子中，除最后一个外都有 l ≤ f，即 l = f。因此只要存在合法顺序，按 (f, l) 排序就能得到一个，只需检查这个顺序中的相邻盒子。工作量 O(Σ kᵢ + n log n)。

第一个样例中盒子 (1, 2)、(5, 5) 和 (7, 7) 按此顺序正好衔接；第二个样例中 (1, 3) 和 (2, 2) 重叠。

## 优化解法

流式读取每个箱子的内容，发现内部逆序立即拒绝。合法箱只需保留两个端点。把有界端点打包为整数，普通数值排序即得到所需区间字典序；解包后沿用简单证明的相邻区间检查。Java 用基本类型键代替对象数组和比较器，Python 不保存全输入及临时端点元组。

- `2144_sorting_optimized.java`: 0.109 s / 2064 KB; 基础版 `2144_sorting.java`: 0.187 s / 6916 KB; 相对基础版的变化: 时间 -41.7%, 内存 -70.2%.
- `2144_sorting_optimized.py`: 0.078 s / 420 KB; 基础版 `2144_sorting.py`: 0.093 s / 1040 KB; 相对基础版的变化: 时间 -16.1%, 内存 -59.6%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `2144_sorting.cpp`; 覆盖实现 `2144_sorting.cpp`; 时间/内存名次 1/6, 其他作者记录 100/100.

- Go: 优先教学基础版 `2144_sorting.go`; 覆盖实现 `2144_sorting.go`; 时间/内存名次 1/1, 其他作者记录 1/1.

- Java: 优先教学基础版 `2144_sorting.java`; 覆盖实现 `2144_sorting_optimized.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `2144_sorting.py`; 覆盖实现 `2144_sorting_optimized.py`; 时间/内存名次 7/2, 其他作者记录 66/66.

- Rust: 优先教学基础版 `2144_sorting.rs`; 覆盖实现 `2144_sorting.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 168 KB | 11309245 |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB | 11294957 |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6916 KB | 11309246 |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.093 s | 1040 KB | 11309247 |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 320 KB | 11309248 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2144_sorting_optimized.java](2144_sorting_optimized.java) | Java 1.8 | sorting | O(total sizes+N log N) | AC | 0.109 s | 2064 KB | 11308445 |
| [2144_sorting_optimized.py](2144_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(total sizes+N log N) | AC | 0.078 s | 420 KB | 11308442 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
