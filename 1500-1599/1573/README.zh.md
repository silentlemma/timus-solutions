# 1573. 炼金术

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · 难度 108 · math

原题作者 Alexander Ipatov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Sandro 有三袋各不相同的试剂：B 个蓝色、R 个红色、Y 个黄色（各 1 … 100 个）。一种药水需要配方中每种颜色的试剂
各一个，颜色互不相同。求能配出药水的试剂组合数。

时间限制：1 秒。内存限制：64 MB。

## 输入

B、R 和 Y，然后是正整数 K 以及配方中 K 种互不相同的颜色（Blue、Red 或 Yellow）。

## 输出

方法数。

## 样例

### 样例 1

输入:

```
2 3 5
3
Red
Yellow
Blue
```

输出:

```
30
```

## 解法

配方中的每种颜色从自己的袋子里取一个试剂，各次选择互相独立，所以答案是配方中提到的各袋大小的乘积，至多为
100³ = 10⁶。`O(K)`。

注意事项：

- 输入中袋子的顺序是蓝、红、黄，而样例的配方先列出红色；
- 只计配方中出现的颜色（测试 02、03）。

## 优化解法

优化的 C++ 解法用 `scanf` 代替 `iostream` 读入，并按颜色的首字母选择袋子（Blue、
Red 和 Yellow 的首字母各不相同），而不是在以字符串为键的 `std::map` 中查找名称。
颜色读入 7 字节的缓冲区，足以容纳最长的名称 Yellow；乘积用 `int` 保存，因为它不
超过 10⁶：{1573_math_optimized.cpp}。

优化的 Java 解法直接从 `System.in` 逐位解析数字，而不是创建 `Scanner`；并按颜色
的首字母选择袋子、跳过单词的其余部分（Blue、Red 和 Yellow 的首字母各不相同），而
不是在存放装箱 `Long` 值的 `HashMap` 中查找名称。乘积用 `int` 保存，因为它不超过
10⁶：{1573_math_optimized.java}。

优化的 Rust 解法把三个袋子的大小放在三个变量中，用对颜色名称的 `match` 选出其中
一个，而不是构建 `HashMap`：{1573_math_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1573_math_optimized.cpp`: 时间降低 +0.00%; 内存降低 +69.23%; 基础版本: `1573_math.cpp`.

- `1573_math_optimized.java`: 时间降低 +12.80%; 内存降低 +79.85%; 基础版本: `1573_math.java`.

- `1573_math_optimized.rs`: 时间降低 -206.67%; 内存降低 +45.10%; 基础版本: `1573_math.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1573_math.go](1573_math.go).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) | Java 1.8 | math | O(K) | AC | 0.109 s | 328 KB | 11304267 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
