# 1684. 杰克的最后一个词

[Timus 1684](https://acm.timus.ru/problem.aspx?space=1&num=1684) · 难度 266 · strings

原题作者 Dmitry Ivankov，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个词和第二个词。把第二个词切成若干段，每段都是第一个词的非空前缀，或者报告无法做到。

## 输入

两个词，每行一个，非空，由小写拉丁字母组成，长度不超过 75000。

## 输出

若存在切分，输出 No，下一行输出用空格分隔的各段；否则输出 Yes。任何正确的切分都可以。

## 评测方式

检查片段拼接为原文本且每段是模式前缀，接受任意合法分解，并核验无解回答。

## 样例

### 样例 1

输入：

```
abracadabra
abrabracada
```

输出：

```
No
abr abracad a
```

### 样例 2

输入：

```
abracadabra
arbadacarba
```

输出：

```
Yes
```

## 解法

设 z[p] 为从第二个词的位置 p 开始、与第一个词前缀相同的最长长度：
对 word + "#" + last 求 Z 函数即可在线性时间内得到全部。从切点 p 出发，
下一段可以在 p + 1, …, p + z[p] 中任意位置结束，因为更短的前缀也都匹配。
所以可达的切点总是一整段 0, …, reach：让 p 从 0 开始、在 p ≤ reach 时前进，
并把 reach 扩展到 p + z[p]。每个新覆盖的切点 q 记住覆盖它的 p，从末尾沿这些链接回溯就得到各段。

如果扫描在第二个词结束之前停止，答案为 Yes。两词长度为 m 和 n 时为 `O(m + n)`。

注意事项：

- 每次取最长前缀可能失败：对 aab 和 aaab，贪心取 aa 后剩下 ab，而 a + aab 可行（测试 06）；
- 答案的词是反着的：No 表示存在切分；
- 输出行最多有 75000 段，最好一次性拼好。

检查器把结论与一个独立的已通过实现比较，并验证各段都是前缀且拼起来正好是该词。

## 优化解法

新算法用前缀函数匹配及从后向前的最长末段贪心，替代基础版的 Z 函数和正向可达切分。字典对取前缀封闭：把最后一段向左延长，只会截短更早的合法前缀，因此可安全取最长末段。记录每个文本终点的匹配长度，逆向恢复切点并输出原串片段。紧凑链接及长度数组代替合并 Z 缓冲与输出副本。

- `1684_greedy_strings.cpp`: 0.015 s / 836 KB; 基础版 `1684_strings.cpp`: 0.015 s / 6084 KB; 相对基础版的变化: 时间 -0.0%, 内存 -86.3%.
- `1684_greedy_strings.go`: 0.015 s / 2068 KB; 基础版 `1684_strings.go`: 0.031 s / 7368 KB; 相对基础版的变化: 时间 -51.6%, 内存 -71.9%.
- `1684_greedy_strings.java`: 0.109 s / 1248 KB; 基础版 `1684_strings.java`: 0.140 s / 8584 KB; 相对基础版的变化: 时间 -22.1%, 内存 -85.5%.
- `1684_greedy_strings.py`: 0.156 s / 1692 KB; 基础版 `1684_strings.py`: 0.250 s / 7360 KB; 相对基础版的变化: 时间 -37.6%, 内存 -77.0%.
- `1684_greedy_strings.rs`: 0.015 s / 1288 KB; 基础版 `1684_strings.rs`: 0.031 s / 4176 KB; 相对基础版的变化: 时间 -51.6%, 内存 -69.2%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1684_strings.cpp`; 覆盖实现 `1684_greedy_strings.cpp`; 时间/内存名次 1/1, 其他作者记录 67/67.

- Go: 优先教学基础版 `1684_strings.go`; 覆盖实现 `1684_strings.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1684_strings.java`; 覆盖实现 `1684_greedy_strings.java`; 时间/内存名次 1/1, 其他作者记录 6/6.

- Python/PyPy: 优先教学基础版 `1684_strings.py`; 覆盖实现 `1684_greedy_strings.py`; 时间/内存名次 6/1, 其他作者记录 30/30.

- Rust: 优先教学基础版 `1684_strings.rs`; 覆盖实现 `1684_strings.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.015 s | 6084 KB | 11308841 |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB | 11288854 |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB | 11288857 |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.250 s | 7360 KB | 11309202 |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.031 s | 4176 KB | 11309203 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1684_greedy_strings.cpp](1684_greedy_strings.cpp) | G++ 13.2 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 836 KB | 11309270 |
| [1684_greedy_strings.go](1684_greedy_strings.go) | Go 1.14 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 2068 KB | 11309272 |
| [1684_greedy_strings.java](1684_greedy_strings.java) | Java 1.8 | greedy, strings | O(pattern length + text length) | AC | 0.109 s | 1248 KB | 11309271 |
| [1684_greedy_strings.py](1684_greedy_strings.py) \* | Python 3.12 x64 | greedy, strings | O(pattern length + text length) | AC | 0.156 s | 1692 KB | 11309268 |
| [1684_greedy_strings.rs](1684_greedy_strings.rs) | Rust 1.75 x64 | greedy, strings | O(pattern length + text length) | AC | 0.015 s | 1288 KB | 11309273 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
