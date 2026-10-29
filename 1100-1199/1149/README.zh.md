# 1149. 写出嵌套的正弦表达式

[Timus 1149](https://acm.timus.ru/problem.aspx?space=1&num=1149) · 难度 61 · strings

原题作者 Vladimir Gladkov，出自 2001 年 4 月在彼尔姆举行的乌拉尔团体程序设计锦标赛热身赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

令 `Aₙ = sin(1−sin(2+sin(3−…sin(n)…)))`，其中符号减、加交替，并令
`S_N = (…((A₁+N)A₂+N−1)A₃+…+2)A_N+1`。对 `1 ≤ N ≤ 200`，按样例的格式原样输出
`S_N` 的文本，不含空格。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

表达式 `S_N`。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
((sin(1)+3)sin(1-sin(2))+2)sin(1-sin(2+sin(3)))+1
```

## 解法

只要求输出文本，不需要计算。`Aₙ` 是 `sin(1`，然后对每个后续的 `k` 写出符号
（奇数后面是减号，偶数后面是加号）和 `sin(k`，最后是 `n` 个右括号。`S_N` 以
`N − 1` 个左括号开头；然后对 `i` 从 1 到 `N` 依次写出 `Aᵢ`、加号、数
`N − i + 1`，除最后一部分外每部分后面跟一个右括号。输出约有 `4·N²` 个
字符，`N = 200` 时为 16.5 万，用一个字符串拼成。`O(N²)`。

注意事项：

- `k` 后面的符号取决于 `k` 本身，而不是正弦的嵌套深度；
- 最后一部分 `A_N+1` 后面没有右括号；
- `N = 1` 时答案就是 `sin(1)+1`；
- 任何地方都没有空格。

答案已在所有测试上与另一种构造方式比对：从内向外包裹表达式 `(S)Aᵢ+…`，
`Aᵢ` 用递归构造。

## 优化解法

优化的 C++ 解法用 `scanf`、`printf` 和 `putchar` 代替 `iostream`，逐段输出
表达式，而不是先拼成 `std::string`，因此很长的答案从不整个放在内存里：128 KB，
而不是 768 KB。

优化的 Java 解法把表达式直接写进 4 KB 的字节缓冲区，而不是拼接字符串，并逐字节解
析这个数，而不是使用 `Scanner`：0.046 s，而不是 0.125 s；372 KB，而不是 4356 KB。
优化的 Python 解法边构造边输出，每个正弦式都在前一个的开头部分上继续延伸：384 KB，
而不是 780 KB，时间不变。

## 各语言说明

- 简单的 Python 解法拼接片段列表；其他简单解法使用字符串或构建器。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1149_strings.cpp](1149_strings.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 768 KB | 11280016 |
| [1149_strings.go](1149_strings.go) | Go 1.14 x64 | strings | O(N²) | AC | 0.015 s | 2976 KB | 11280150 |
| [1149_strings.java](1149_strings.java) | Java 1.8 | strings | O(N²) | AC | 0.125 s | 4356 KB | 11280213 |
| [1149_strings.py](1149_strings.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.046 s | 780 KB | 11280177 |
| [1149_strings.rs](1149_strings.rs) | Rust 1.75 x64 | strings | O(N²) | AC | 0.015 s | 636 KB | 11280243 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1149_strings_optimized.cpp](1149_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 128 KB | 11303572 |
| [1149_strings_optimized.java](1149_strings_optimized.java) | Java 1.8 | strings | O(N²) | AC | 0.046 s | 372 KB | 11303716 |
| [1149_strings_optimized.py](1149_strings_optimized.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.062 s | 384 KB | 11303717 |
