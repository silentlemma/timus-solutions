# 1545. 象形文字

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · 难度 50 · implementation

原题作者 Evgeny Krokhalev，出自 2007 年 4 月 21 日在叶卡捷琳堡举行的第十一届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

词典中有 N ≤ 1000 个汉字，每个写作两个小写字母。给定输入的一个字母，输出以它开头的汉字。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，N 个两字母条目，然后是那个字母。

## 输出

符合的条目，每行一个，顺序任意；没有则不输出。

## 样例

### 样例 1

输入:

```
6
na
no
ni
ki
ka
ku
k
```

输出:

```
ka
ki
ku
```

## 解法

把每个条目的首字母与输入的字母比较，按输入顺序输出匹配项。`O(N)`。

注意事项：

- 没有匹配时输出为空（测试 02、05）；
- 出现两次的条目要输出两次（测试 03）；
- 字母必须在首位：出现在第二位不算（测试 05）。

## 优化解法

优化的 C++ 解法把两个字母的条目存放在局部的三字节 C 字符串数组中，而不是
`std::string`，用 `scanf("%2s")` 读入、用 `puts` 输出：120 KB，而不是 392 KB，时
间不变。

每个象形文字都是两个字母。优化的 Java 解法把它们放在由 256 字节块填充的字节数组
中，并从一个字节数组输出答案，不用 `Scanner`，也不用字符串：392 KB，而不是
1804 KB，时间不变。优化的 Rust 解法把每个象形文字存为一对字节，并通过缓冲区很小
的 `BufWriter` 输出：0.015 s，而不是 0.046 s；196 KB，而不是 236 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
