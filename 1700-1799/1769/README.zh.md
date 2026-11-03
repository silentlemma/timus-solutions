# 1769. 古老的乌拉尔传说

[Timus 1769](https://acm.timus.ru/problem.aspx?space=1&num=1769) · 难度 206 · strings

原题作者 Daniil Ayzenshteyn，出自 2010 年 4 月 10 日第十四届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个非空的十进制数字串，求其十进制表示不在串中出现的最小正整数。

## 输入

这个串，至多 10⁵ 位。

## 输出

该整数。

## 评测方式

按词元比较输出，多余空白不影响结果。

## 样例

### 样例 1

输入：

```
10123456789
```

输出：

```
11
```

## 解法

n 位的串每种长度至多有 n 个子串，而六位数有 9·10⁵ 个，所以总有某个六位数不出现，答案至多六位。
每个长为 1 到 6、不以 0 开头的子串都是某个数的表示；把它们全部标记，再从 1 开始数到第一个未标记的数，就是答案。`O(6n)`。

样例中 1 到 9 以及 10 都出现了，而 11 没有。

注意事项：

- 以 0 开头的子串不是数的表示，不过 0 后面的数在后一位仍然出现；
- 全是 0 的串缺少 1；
- 依次在串中查找每个数，在答案较大的长串上可能很慢。

在 90 个随机串上，答案与依次查找 1、2、3 等的结果一致；在 20 个长串上与一个独立的已通过实现一致。

## 优化解法

每次只标记一种长度的十进制子串，使用滚动数值编码和紧凑位图。按递增数值寻找第一个缺失数；若该长度全部出现，则增加长度并复用空间。前导零和最小答案按原数值定义处理，不为每个子串分配字符串，也不同时保留全部长度的集合。

- `1769_strings_optimized.cpp`: 0.031 s / 376 KB; 基础版 `1769_strings.cpp`: 0.015 s / 612 KB; 相对基础版的变化: 时间 +106.7%, 内存 -38.6%.
- `1769_strings_optimized.go`: 0.046 s / 1444 KB; 基础版 `1769_strings.go`: 0.031 s / 2740 KB; 相对基础版的变化: 时间 +48.4%, 内存 -47.3%.
- `1769_strings_optimized.java`: 0.140 s / 556 KB; 基础版 `1769_strings.java`: 0.156 s / 2124 KB; 相对基础版的变化: 时间 -10.3%, 内存 -73.8%.
- `1769_strings_optimized.py`: 0.250 s / 1452 KB; 基础版 `1769_strings.py`: 0.312 s / 23740 KB; 相对基础版的变化: 时间 -19.9%, 内存 -93.9%.
- `1769_strings_optimized.rs`: 0.031 s / 468 KB; 基础版 `1769_strings.rs`: 0.031 s / 1472 KB; 相对基础版的变化: 时间 -0.0%, 内存 -68.2%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1769_strings.cpp`; 覆盖实现 `1769_strings.cpp`; 时间/内存名次 1/7, 其他作者记录 72/72.

- Go: 优先教学基础版 `1769_strings.go`; 覆盖实现 `1769_strings.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1769_strings.java`; 覆盖实现 `1769_strings_optimized.java`; 时间/内存名次 2/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1769_strings.py`; 覆盖实现 `1769_strings_optimized.py`; 时间/内存名次 7/1, 其他作者记录 14/14.

- Rust: 优先教学基础版 `1769_strings.rs`; 覆盖实现 `1769_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1769_strings.cpp](1769_strings.cpp) | G++ 13.2 x64 | strings | O(6n) | AC | 0.015 s | 612 KB | 11308926 |
| [1769_strings.go](1769_strings.go) | Go 1.14 x64 | strings | O(6n) | AC | 0.031 s | 2740 KB | 11289655 |
| [1769_strings.java](1769_strings.java) | Java 1.8 | strings | O(6n) | AC | 0.156 s | 2124 KB | 11308927 |
| [1769_strings.py](1769_strings.py) | Python 3.12 x64 | strings | O(6n) | AC | 0.312 s | 23740 KB | 11308928 |
| [1769_strings.rs](1769_strings.rs) | Rust 1.75 x64 | strings | O(6n) | AC | 0.031 s | 1472 KB | 11289658 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1769_strings_optimized.cpp](1769_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(DN+10^D) | AC | 0.031 s | 376 KB | 11308082 |
| [1769_strings_optimized.go](1769_strings_optimized.go) | Go 1.14 x64 | strings | O(DN+10^D) | AC | 0.046 s | 1444 KB | 11308083 |
| [1769_strings_optimized.java](1769_strings_optimized.java) \* | Java 1.8 | strings | O(DN+10^D) | AC | 0.140 s | 556 KB | 11308084 |
| [1769_strings_optimized.py](1769_strings_optimized.py) \* | Python 3.12 x64 | strings | O(DN+10^D) | AC | 0.250 s | 1452 KB | 11308079 |
| [1769_strings_optimized.rs](1769_strings_optimized.rs) | Rust 1.75 x64 | strings | O(DN+10^D) | AC | 0.031 s | 468 KB | 11308085 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
