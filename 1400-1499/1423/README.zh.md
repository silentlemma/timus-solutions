# 1423. 字符串的故事

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · 难度 170 · strings

原题作者 Nikita Rybak、Ilya Grebnov 与 Dmitry Kovalioff，出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

字符串 S 和 T 长度都是 N（1 ≤ N ≤ 250 000），由编码 33 到 255 的字符组成。一次循
环移位把字符串的最后一个字符移到开头。输出一个数 X（0 ≤ X < N），使 X 次移位把 S
变成 T；若不存在，输出 −1；任何满足的 X 都可以。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后 S，然后 T。

## 输出

X 或 −1。

## 样例

### 样例 1

输入:

```
11
abracadabra
racadabraab
```

输出:

```
9
```

样例中 9 次移位把 "abracadabra" 变成 "racadabraab"。

## 解法

向右移 X 次等于向左移 N − X 次，而 S 向左移 k 次的结果恰好是 S + S 中从 k < N 开
始、长度为 N 的子串。所以在 S + S 中查找 T：若出现位置为 k，答案为 (N − k) mod
N；若不出现，答案为 −1。查找用 Knuth–Morris–Pratt 算法和 T 的前缀函数，在去掉最
后一个字符的 S + S 上进行；Python 内置的字节串查找在这里同样是线性的。`O(N)`。

注意事项：

- 周期性的 S 有多个答案，所以测试使用检查器（测试 04）；
- 编码大于 127 的字符必须按原始字节读入；有些读法会解码它们，甚至把编码 160 当
  作空格（测试 05、gen3）；
- 朴素的子串查找在由同一个字母重复组成的字符串上可能是平方复杂度（gen2）。

## 优化解法

优化的 C++ 解法把前缀函数存成打包在 32 位字数组中的 18 位字段，因为每个值都小于
N ≤ 250 000 < 2^18，读取时一次从相邻的两个字中取出字段；每次访问多花几次移位，但
只占约 0.56 MB，而 `int` 值要 1 MB。此外它把 S 扫两遍，而不是构造 S + S，并用
`scanf` 把 S 和 T 读进两个 250 001 字节的静态缓冲区，而不是用 `cin` 读进
`std::string`：{1423_strings_optimized.cpp}。

优化的 Go 解法用 `int32` 而不是 8 字节的 `int` 存前缀函数，因为每个值都小于
N ≤ 250 000，并依据两个字符串的长度都是 N，用 `io.ReadFull` 把 S 和 T 直接读进恰
好 N 字节的数组，而不是读入全部输入再按字段切分：{1423_strings_optimized.go}。

优化的 Java 解法按 64 KB 分块读取原始输入，手工从中切出 S 和 T 作为 `byte` 数组
并按字节比较，而不是用 `BufferedReader` 把各行解码成每个字符占两字节的 `char` 数
组：{1423_strings_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1423_strings_optimized.cpp`: 时间降低 -106.67%; 内存降低 +40.82%; 基础版本: `1423_strings.cpp`.

- `1423_strings_optimized.go`: 时间降低 +0.00%; 内存降低 +40.39%; 基础版本: `1423_strings.go`.

- `1423_strings_optimized.java`: 时间降低 +19.87%; 内存降低 +39.97%; 基础版本: `1423_strings.java`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB | 11286160 |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB | 11286161 |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.156 s | 5744 KB | 11307252 |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB | 11286163 |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB | 11286168 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings_optimized.cpp](1423_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(N) | AC | 0.031 s | 1148 KB | 11307257 |
| [1423_strings_optimized.go](1423_strings_optimized.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 2544 KB | 11307255 |
| [1423_strings_optimized.java](1423_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.125 s | 3448 KB | 11307317 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
