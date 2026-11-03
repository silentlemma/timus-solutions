# 1179. 文本中数最多的进制

[Timus 1179](https://acm.timus.ru/problem.aspx?space=1&num=1179) · 难度 295 · strings

原题作者 Pavel Atnashev，出自 2002 年 2 月 16 日在叶卡捷琳堡举行的第三届乌拉尔国立大学个人程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段至多 1 MB 的文本由数字、大写拉丁字母、空格和换行组成；字母是从 `A = 10`
到 `Z = 35` 的数字。在 `K` 进制中，数是由该进制数字组成的极大连续段。求 2 到
36 之间使文本中数的个数最多的进制 `K`（并列时取最小的），以及这个个数。

时间限制：1 秒。内存限制：64 MB。

## 输入

文本。

## 输出

`K` 和数的个数。

## 评测方式

比较两个整数词元。七份新源码各有 13 个仓库测试和 159 次额外目标环境执行，包含块边界及最大文本。每份 Python 另有 62403 次宿主执行，对照独立正则连续段计数：全部 37 值对/三元组、短文本穷举及随机空白。此计数不是原生语言执行总量。

## 样例

### 样例 1

输入：

```
01234B56789
AZA
```

输出：

```
11 4
```

## 解法

逐个枚举 `k=2..36`。扫描文本，记住前一字符是否为该进制的数字。数字前面是
分隔符时恰好开始一个数，因此每个极大连续段只计一次，也包含从文本首字符开始的段。
只在严格增大时更新最佳进制，平局自然取较小值。时间 `O(35L)`，保存文本需 `O(L)`。

Python 用原生字节操作实现同一扫描：前置分隔符，将字符翻译为零（分隔符）或一
（数字），然后数 `01`。此双字节模式不会自重叠。进制增大时扩充数字表。
空文本或没有数字输出 `2 0`；空格、换行分隔数字，`Z` 在 36 进制才是数字。

## 优化解法

分隔符值为 36，文本前也放一个。相邻值 `(left,right)` 在进制 `k` 开始一个数
当且仅当 `right<k≤left`。若 `right<left`，它对应区间 `max(2,right+1)..left`。
用差分数组累积端点，再对 35 个进制求前缀和。每个数只有一个起始相邻对，故计数正确。
旧原生版本先统计 37×37 相邻对；新 Java/Python 按有界块读取时直接加事件，保留跨块
前一个值。原生相邻对版本时间 `O(L+37²)`，流式版本 `O(L+36)`；后者空间由输入块及
小表决定，不依赖 L。

旧 Python 翻译完整文本，再用固定次数的 C 级字节模式计数：显式考虑字母表大小时
是 `O(37²L)` 而非 `O(L+37²)`，空间 `O(L)`。保留为 Accepted 算法替代项，不作为相对
新教学基础的优化。两份 Java 事件版本相对直接基础都达 30%；新 Java 相对旧 Java
单独只有 29.93% 内存改善，不能向上取整。

- `1179_strings.cpp`: 0.031 s / 116 KB; 基础 `1179_bruteforce_strings.cpp`: 0.171 s / 2836 KB; 相对变化: 时间 -81.9%, 内存 -95.9%.
- `1179_strings.go`: 0.015 s / 3160 KB; 基础 `1179_bruteforce_strings.go`: 0.203 s / 3136 KB; 相对变化: 时间 -92.6%, 内存 +0.8%.
- `1179_strings.java`: 0.125 s / 588 KB; 基础 `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; 相对变化: 时间 -69.2%, 内存 -83.0%.
- `1179_strings_optimized.py`: 0.203 s / 396 KB; 基础 `1179_bruteforce_strings.py`: 0.218 s / 3128 KB; 相对变化: 时间 -6.9%, 内存 -87.3%.
- `1179_strings_optimized.java`: 0.109 s / 412 KB; 基础 `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; 相对变化: 时间 -73.2%, 内存 -88.1%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

- C++: 首选教学基础 `1179_bruteforce_strings.cpp`; 覆盖源码 `1179_strings.cpp`; 时间/内存名次 4/2, 其他作者记录 44/44.

- Go: 首选教学基础 `1179_bruteforce_strings.go`; 覆盖源码 `1179_strings.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1179_bruteforce_strings.java`; 覆盖源码 `1179_strings.java`; 时间/内存名次 2/1, 其他作者记录 4/4.

- Python/PyPy: 首选教学基础 `1179_bruteforce_strings.py`; 覆盖源码 `1179_strings_optimized.py`; 时间/内存名次 1/1, 其他作者记录 5/5.

- Rust: 首选教学基础 `1179_bruteforce_strings.rs`; 覆盖源码 `1179_bruteforce_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1179_bruteforce_strings.cpp](1179_bruteforce_strings.cpp) | G++ 13.2 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.171 s | 2836 KB | 11309345 |
| [1179_bruteforce_strings.go](1179_bruteforce_strings.go) | Go 1.14 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.203 s | 3136 KB | 11309346 |
| [1179_bruteforce_strings.java](1179_bruteforce_strings.java) | Java 1.8 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.406 s | 3464 KB | 11309350 |
| [1179_bruteforce_strings.py](1179_bruteforce_strings.py) | Python 3.12 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.218 s | 3128 KB | 11309344 |
| [1179_bruteforce_strings.rs](1179_bruteforce_strings.rs) | Rust 1.75 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.031 s | 2128 KB | 11309349 |

### 其他 Accepted 实现

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1179_strings.py](1179_strings.py) | Python 3.12 x64 | strings | O(37^2 L) time; O(L) space | AC | 0.640 s | 3100 KB | 11283287 |
| [1179_strings.rs](1179_strings.rs) | Rust 1.75 x64 | strings | O(L+37^2) time | AC | 0.015 s | 2124 KB | 11283294 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1179_strings.cpp](1179_strings.cpp) | G++ 13.2 x64 | strings | O(L+37^2) time | AC | 0.031 s | 116 KB | 11283281 |
| [1179_strings.go](1179_strings.go) | Go 1.14 x64 | strings | O(L+37^2) time | AC | 0.015 s | 3160 KB | 11283283 |
| [1179_strings.java](1179_strings.java) \* | Java 1.8 | strings | O(L+37^2) time | AC | 0.125 s | 588 KB | 11283292 |
| [1179_strings_optimized.py](1179_strings_optimized.py) | Python 3.12 x64 | strings | O(L+36) time; bounded block/table space | AC | 0.203 s | 396 KB | 11309351 |
| [1179_strings_optimized.java](1179_strings_optimized.java) \* | Java 1.8 | strings | O(L+36) time; bounded block/table space | AC | 0.109 s | 412 KB | 11309353 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
