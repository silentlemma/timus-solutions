# 1196. 学生写的年份中有多少出现在老师的列表里

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · 难度 53 · binary_search

原题为民间流传的题目，出自 2002 年 3 月 2 日第五届中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

老师有一个已排序的 `N ≤ 15000` 个年份的列表，学生以任意顺序写下 `M ≤ 10⁶` 个
年份；两个列表都可能有重复，年份都不超过 `10⁹`。统计学生列表中有多少条也出现在
老师的列表里。

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
一方的重复，而老师一方的重复不影响结果。`O(M log N)`。要读入一百万个数，快速
读入比查找本身更重要。

注意事项：

- 学生写了两次的年份要计两次；
- 输入多达一百万行，在某些语言中逐行慢速读取可能超时。

答案已在所有测试上与另一份使用哈希集合的独立解答比对。

## 各语言说明

- Python 把老师的年份放进集合；其他语言在排序数组上二分查找。Java 用手写的
  字节读取器读入。
- Python 逐行读取学生的年份。若一次性切分全部输入，内存中会同时存在一百万个小字符串，约 62 MB，
  这样的版本在测试 8 上超出了 64 MB 的限制。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log N) | AC | 0.687 s | 256 KB |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(M log N) | AC | 0.171 s | 5576 KB |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(M log N) | AC | 0.312 s | 616 KB |
| [1196_binary_search.py](1196_binary_search.py) | Python 3.12 x64 | binary_search | O(M log N) | AC | 0.687 s | 1456 KB |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log N) | AC | 0.031 s | 9300 KB |
