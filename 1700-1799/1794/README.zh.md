# 1794. 世界建筑杰作

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · 难度 197 · implementation

原题作者 Vladislav Isenbaev（由 Oleg Dolgorukov 准备），出自 2010 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个学生围成一圈坐着，按顺时针编号为 1 到 n，并按顺时针依次发言。学生 i 希望第 aᵢ 个发言。选择由谁第一个发言，使尽可能多的学生恰好在自己希望的顺序发言。任何最优选择都可以。

## 输入

n（2 ≤ n ≤ 10⁵），然后是 a₁、…、aₙ（1 ≤ aᵢ ≤ n）。

## 输出

第一个发言的学生编号。

## 评测方式

接受满足愿望数最多的任意起始学生，不要求唯一最小编号。

## 样例

### 样例 1

输入：

```
4
4 1 2 3
```

输出：

```
2
```

### 样例 2

输入：

```
3
1 1 1
```

输出：

```
3
```

## 解法

若学生 k 先发言，学生 i 在第 ((i − k) mod n) + 1 个发言。所以只有一个起点能满足学生 i：k = ((i − aᵢ) mod n) + 1。
统计所有学生的这些投票，输出得票最多的起点。`O(n)`。

第一个样例中四个学生都投给起点 2：例如学生 1 想第四个发言，而顺序 2、3、4、1 正好让他排在第四。

注意事项：

- i − aᵢ 可能为负，而在 C++、Go 和 Java 中此时余数也是负的；
- 几个起点可能票数相同，如第二个样例，三个中任何一个都可以。

检查器自己统计票数，接受任何得票最多的起点。在 300 个小班级上它与对所有起点的直接统计一致，在大班级上答案与一个独立的已通过实现一致。

## 优化解法

仍统计每个起始学生的票数。下标差严格位于班级人数的负值与正值之间，一次条件加法即可代替通用取余。缓冲输入不保留全部偏好，计数不超过班级人数，故无符号 32 位足够。实现选择第一个最大值，但题目接受任意最优起始学生。

- `1794_implementation_optimized.cpp`: 0.015 s / 520 KB; 基础版 `1794_implementation.cpp`: 0.078 s / 568 KB; 相对基础版的变化: 时间 -80.8%, 内存 -8.5%.
- `1794_implementation_optimized.py`: 0.187 s / 912 KB; 基础版 `1794_implementation.py`: 0.125 s / 8004 KB; 相对基础版的变化: 时间 +49.6%, 内存 -88.6%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1794_implementation.cpp`; 覆盖实现 `1794_implementation_optimized.cpp`; 时间/内存名次 1/8, 其他作者记录 96/96.

- Go: 优先教学基础版 `1794_implementation.go`; 覆盖实现 `1794_implementation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1794_implementation.java`; 覆盖实现 `1794_implementation.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1794_implementation.py`; 覆盖实现 `1794_implementation_optimized.py`; 时间/内存名次 13/1, 其他作者记录 13/13.

- Rust: 优先教学基础版 `1794_implementation.rs`; 覆盖实现 `1794_implementation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 568 KB | 11308931 |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB | 11289873 |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 792 KB | 11308933 |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.125 s | 8004 KB | 11308935 |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2124 KB | 11308936 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1794_implementation_optimized.cpp](1794_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 520 KB | 11308385 |
| [1794_implementation_optimized.py](1794_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.187 s | 912 KB | 11309462 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
