# 1723. 桑德罗之书

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · 难度 62 · strings

原题作者 Ivan Burmistrov（由 Olga Soboleva 准备），出自 2009 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定单词的每个子串都是一个咒语，其威力是它在单词中出现的次数（重叠的也计入）。输出一个威力最大的咒语。

## 输入

一个非空单词，由不超过 50 个小写拉丁字母组成。

## 输出

任意一个威力最大的咒语。

## 样例

### 样例 1

输入：

```
tebidohtebidoh
```

输出：

```
tebidoh
```

## 解法

咒语的每次出现都以其首字母的一次出现开头，而不同的出现开头位置不同。
所以没有咒语比它的首字母单独构成的咒语更强，出现最多的字母就是威力最大的咒语。`O(n)`。

样例中每个字母都出现两次，所以 `t` 与 `tebidoh` 一样强。

注意事项：

- 出现可以重叠：`aba` 在 `abababa` 中出现三次，而 `a` 出现四次；
- 任何威力最大的咒语都可以，所以测试使用检查程序。

检查程序计算答案的出现次数（含重叠），并与期望答案比较。在 300 个随机单词上，出现最多的字母与穷举所有子串的结果一致。

## 优化解法

优化的 C++ 解法一边用 `getchar` 读取一边统计字母，不保存字符串：84 KB，而不是
352 KB。

优化的 Java 解法直接从 `System.in` 逐字节读取字母，而不是用 `Scanner` 读入整个单
词，并以一个字节输出答案：348 KB，而不是 1556 KB，时间不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 352 KB | 11303504 |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB | 11289348 |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1556 KB | 11303505 |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB | 11289349 |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB | 11289353 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1723_strings_optimized.cpp](1723_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 84 KB | 11303635 |
| [1723_strings_optimized.java](1723_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.140 s | 348 KB | 11303774 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
