# 2091. 把培养方案分得最均匀的两门课

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · 难度 271 · bitmask, bruteforce

原题作者 Dmitry Ivankov，出自 2014 年乌拉尔联邦大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 n × m 的表说明 n 个培养方案各包含 m 门课中的哪些。选两门不同的课 A 和 B；它们把方案分成四组：两门都有、只有 A、只有 B、都没有。使最大的一组尽量小，输出其大小和两门课。任何最优的一对都可接受。时间限制 1 秒，内存限制 64 MB。

## 输入

n 和 m（4 ≤ n, m ≤ 100），然后是 n 行，每行 m 个 0 或 1。

## 输出

最大组的最小可能大小，然后是两门课。

## 评测方式

仓库检查器验证最优值及路线/课程对合法性，不要求字面相同。

- `2091_bitmask.cpp` (G++ 13.2 x64): 13个仓库测试.

- `2091_bitmask.go` (Go 1.14 x64): 13个仓库测试.

- `2091_bitmask.java` (Java 1.8): 13个仓库测试.

- `2091_bitmask.py` (Python 3.12 x64): 13个仓库测试.

- `2091_bitmask.rs` (Rust 1.75 x64): 13个仓库测试.

## 样例

### 样例 1

输入：

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

输出：

```
2
1 3
```

## 解法

课程对少于 5000 个，一对课程的分组只需扫一遍方案，组号为 2·[A] + [B]。枚举所有对的代价是 O(m² n)，五十万步。

样例中课程 1 和 3 给出分组 {4}、{6}、{2, 3} 和 {1, 5}，最大的一组有 2 个方案。

## 优化解法

保留逐课程对、逐项目枚举。快速bitmask源码按课程编码项目。两列计数ca、cb，交集数t时，四组大小为t、ca-t、cb-t、N-ca-cb+t。交集及位计数代替每对扫描N个项目。枚举不同课程对并最小化最大组；ceil(N/4)是通用下界，达到即可有证明地提前退出。重复项目行必须保留为不同位，不能丢失重数。N<=100，原生每课程用两个64位字，Python用大整数。数值状态O(M ceil(N/W))字，Python/Rust另保留O(NM)输入。时间O(NM+M² ceil(N/W))，实际原生至多两字。检查器接受任意达到最优值的课程对。

- `2091_bitmask.cpp`: 0.015 s / 112 KB; 基础 `2091_bruteforce.cpp`: 0.015 s / 228 KB; 相对变化: 时间 -0.0%, 内存 -50.9%.
- `2091_bitmask.go`: 0.015 s / 304 KB; 基础 `2091_bruteforce.go`: 0.031 s / 1200 KB; 相对变化: 时间 -51.6%, 内存 -74.7%.
- `2091_bitmask.java`: 0.125 s / 400 KB; 基础 `2091_bruteforce.java`: 0.125 s / 5664 KB; 相对变化: 时间 -0.0%, 内存 -92.9%.
- `2091_bitmask.py`: 0.078 s / 592 KB; 基础 `2091_bruteforce.py`: 0.125 s / 676 KB; 相对变化: 时间 -37.6%, 内存 -12.4%.
- `2091_bitmask.rs`: 0.015 s / 220 KB; 基础 `2091_bruteforce.rs`: 0.015 s / 464 KB; 相对变化: 时间 -0.0%, 内存 -52.6%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `2091_bruteforce.cpp`; 覆盖源码 `2091_bitmask.cpp`; 时间/内存名次 1/1, 其他作者记录 56/56.

- Go: 首选教学基础 `2091_bruteforce.go`; 覆盖源码 `2091_bitmask.go`; 时间/内存名次 1/1, 其他作者记录 1/1.

- Java: 首选教学基础 `2091_bruteforce.java`; 覆盖源码 `2091_bitmask.java`; 时间/内存名次 2/1, 其他作者记录 3/3.

- Python/PyPy: 首选教学基础 `2091_bruteforce.py`; 覆盖源码 `2091_bitmask.py`; 时间/内存名次 1/1, 其他作者记录 12/12.

- Rust: 首选教学基础 `2091_bruteforce.rs`; 覆盖源码 `2091_bitmask.rs`; 时间/内存名次 1/1, 其他作者记录 1/1.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 228 KB | 11308118 |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB | 11294643 |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.125 s | 5664 KB | 11308125 |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.125 s | 676 KB | 11308827 |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 464 KB | 11308829 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2091_bitmask.cpp](2091_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 112 KB | 11308002 |
| [2091_bitmask.go](2091_bitmask.go) | Go 1.14 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 304 KB | 11309740 |
| [2091_bitmask.java](2091_bitmask.java) \* | Java 1.8 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.125 s | 400 KB | 11308008 |
| [2091_bitmask.py](2091_bitmask.py) | Python 3.12 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.078 s | 592 KB | 11308000 |
| [2091_bitmask.rs](2091_bitmask.rs) | Rust 1.75 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.015 s | 220 KB | 11308009 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
