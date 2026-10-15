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

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1684_strings.cpp](1684_strings.cpp) | G++ 13.2 x64 | strings | O(m + n) | AC | 0.031 s | 6108 KB |
| [1684_strings.go](1684_strings.go) | Go 1.14 x64 | strings | O(m + n) | AC | 0.031 s | 7368 KB |
| [1684_strings.java](1684_strings.java) | Java 1.8 | strings | O(m + n) | AC | 0.140 s | 8584 KB |
| [1684_strings.py](1684_strings.py) | Python 3.12 x64 | strings | O(m + n) | AC | 0.265 s | 7024 KB |
| [1684_strings.rs](1684_strings.rs) | Rust 1.75 x64 | strings | O(m + n) | AC | 0.062 s | 5168 KB |
