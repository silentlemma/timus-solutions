# 1737. 助记符与回文 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · 难度 254 · strings

原题作者 Alexander Ipatov，出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

按字母序列出由字母 a、b、c 组成、长度为 n、且不含长度至少为 2 的回文子串的所有单词。若它们总长度超过 100 000 个字母，输出 `TOO LONG`。

## 输入

n（1 ≤ n ≤ 20 000）。

## 输出

每行一个单词，或者 `TOO LONG`。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入：

```
2
```

输出：

```
ab
ac
ba
bc
ca
cb
```

## 解法

长度至少为 2 的回文中间必有长度为 2 或 3 的回文，所以只需相邻字母不同、相隔一个的字母也不同。
于是任意连续三个字母都是 a、b、c 的某种排列，每个字母都重复三位之前的字母：单词是 a、b、c 六种排列之一的重复。
因此 n = 1 时有三个单词，更大的 n 都有六个；当 6n > 100 000，即从 n = 16 667 起，答案是 `TOO LONG`。`O(n)`。

注意事项：

- n = 1 时六种排列只给出三个不同的单词；
- 限制针对总长度，而不是单词个数。

对 n 不超过 9，列表与逐一检查所有由 a、b、c 组成的单词的结果一致。

## 优化解法

长度至少为二时，前两个不同字母唯一确定合法周期串。按字母序枚举字母对，即可直接按字典序输出六个串，无需集合、去重或排序。单字母情况单独输出三个串。构造前先判断输出是否过长，之后分块输出，不保留全部串及拼接结果。

- `1737_strings_optimized.cpp`: 0.031 s / 112 KB; 基础版 `1737_strings.cpp`: 0.031 s / 232 KB; 相对基础版的变化: 时间 -0.0%, 内存 -51.7%.
- `1737_strings_optimized.go`: 0.015 s / 964 KB; 基础版 `1737_strings.go`: 0.031 s / 1448 KB; 相对基础版的变化: 时间 -51.6%, 内存 -33.4%.
- `1737_strings_optimized.java`: 0.093 s / 388 KB; 基础版 `1737_strings.java`: 0.109 s / 3016 KB; 相对基础版的变化: 时间 -14.7%, 内存 -87.1%.
- `1737_strings_optimized.py`: 0.093 s / 444 KB; 基础版 `1737_strings.py`: 0.109 s / 980 KB; 相对基础版的变化: 时间 -14.7%, 内存 -54.7%.
- `1737_strings_optimized.rs`: 0.015 s / 196 KB; 基础版 `1737_strings.rs`: 0.015 s / 328 KB; 相对基础版的变化: 时间 -0.0%, 内存 -40.2%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1737_strings.cpp`; 覆盖实现 `1737_strings_optimized.cpp`; 时间/内存名次 42/1, 其他作者记录 48/48.

- Go: 优先教学基础版 `1737_strings.go`; 覆盖实现 `1737_strings.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1737_strings.java`; 覆盖实现 `1737_strings_optimized.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1737_strings.py`; 覆盖实现 `1737_strings_optimized.py`; 时间/内存名次 5/7, 其他作者记录 15/15.

- Rust: 优先教学基础版 `1737_strings.rs`; 覆盖实现 `1737_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 232 KB | 11308913 |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB | 11289457 |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 3016 KB | 11308916 |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 980 KB | 11308917 |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB | 11289460 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1737_strings_optimized.cpp](1737_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(output size) | AC | 0.031 s | 112 KB | 11308823 |
| [1737_strings_optimized.go](1737_strings_optimized.go) | Go 1.14 x64 | strings | O(output size) | AC | 0.015 s | 964 KB | 11308824 |
| [1737_strings_optimized.java](1737_strings_optimized.java) | Java 1.8 | strings | O(output size) | AC | 0.093 s | 388 KB | 11308825 |
| [1737_strings_optimized.py](1737_strings_optimized.py) \* | Python 3.12 x64 | strings | O(output size) | AC | 0.093 s | 444 KB | 11308821 |
| [1737_strings_optimized.rs](1737_strings_optimized.rs) | Rust 1.75 x64 | strings | O(output size) | AC | 0.015 s | 196 KB | 11308826 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
