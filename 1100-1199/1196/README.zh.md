# 1196. 学生写的年份中有多少出现在老师的列表里

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · 难度 52 · binary_search, hashing

原题为民间流传的题目，出自 2002 年 3 月 2 日第五届中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

老师有一个已排序的 `1 ≤ N ≤ 15000` 个年份的列表，学生以任意顺序写下
`1 ≤ M ≤ 10⁶` 个年份；两个列表都可能有重复，每个年份在 1 到 `10⁹` 之间。统计学生
列表中有多少条也出现在老师的列表里。

时间限制：1.5 秒。内存限制：64 MB。

## 输入

`N` 和老师的年份（每行一个），然后是 `M` 和学生的年份。

## 输出

匹配的条数。

## 样例

### 样例 1

输入：

```
2
1054
1492
4
1492
65536
1492
100
```

输出：

```
2
```

## 解法

老师的列表已经排好序，所以学生的每个年份都用二分查找；每次匹配都计数，包括学生
一方的重复，而老师一方的重复不影响结果。`O(N + M log N)`。要读入一百万个数，快速
读入比查找本身更重要。

注意事项：

- 学生写了两次的年份要计两次；
- 输入约有一百万行，在某些语言中逐行慢速读取可能超时。

答案已在所有测试上与另一份使用哈希集合的独立解答比对。

## 优化解法

优化的 C++ 解法用 `fread` 按 64 KB 分块读入，再手工解析多达一百万个数，而不是每
个数调用一次 `scanf`：0.046 s，而不是 0.687 s，内存几乎不变（260 KB 对 256 KB）。
二分查找不变。

优化的 Go 解法从 4 KB 的带缓冲读取器手工解析日期，而不是用 1 MB 缓冲的按词扫描器，
日期存为 `int32`，并用自己写的二分查找：0.062 s，而不是 0.171 s；996 KB，而不是
5576 KB。优化的 Rust 解法从 64 KB 缓冲区手工解析日期，而不是把整个输入读成字符串，
日期存为 `u32`：320 KB，而不是 9300 KB，时间不变。优化的 Python 解法利用每行恰好
一个日期这一点：直接转换每一行，并用 `map` 而不是 Python 循环统计已知日期：
0.343 s，而不是 0.687 s；1324 KB，而不是 1456 KB。

## 各语言说明

- Python 把老师的年份放进集合；其他语言在排序数组上二分查找。
- Python 逐行读取学生的年份。若一次性切分全部输入，内存中会同时存在一百万个小字符串，约 62 MB，
  这样的版本在测试 8 上超出了 64 MB 的限制。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.687 s | 256 KB | 11283484 |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.171 s | 5576 KB | 11283485 |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(N + M log N) | AC | 0.328 s | 592 KB | 11303453 |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.031 s | 9300 KB | 11283493 |
| [1196_hashing.py](1196_hashing.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.687 s | 1456 KB | 11283490 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1196_binary_search_optimized.cpp](1196_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 260 KB | 11303577 |
| [1196_binary_search_optimized.go](1196_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.062 s | 996 KB | 11303718 |
| [1196_binary_search_optimized.rs](1196_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 320 KB | 11303720 |
| [1196_hashing_optimized.py](1196_hashing_optimized.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.343 s | 1324 KB | 11303721 |
