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

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器要求一个整数。仅当保存参考表示无旋转时接受-1；否则任意 X 属于 [0,N)，把 S 后 X 字节移到前面得到 T 即有效，不要求最小移位。

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

`1423_strings_optimized.py`. 保留 S+S 中精确字节子串搜索。T 位于左偏移 p 时返回右移 (N−p) mod N，否则 −1；周期字符串允许任意有效位移。完整读取并 split 二进制输入，以 bytes.find 搜索，在 os._exit(0) 前输出短答案。保留 O(N) 字节。时间为线性输入输出加运行时子串搜索，无 Python 逐字符循环。此 CPython 记录两项第一，但 1592 KB 仍高于教学版 1372 KB。

精确源码：Python 3.12 x64 Accepted #11327848: 0.062 s / 1592 KB。2026-11-20 保存的编译器组排名，时间然后内存：1/55; 1/55。严格收录采用达到 1024 KB 时要求时间和内存：前十或前 15%，同值共享名次，百分比向上取整。两项第一，无需星号。保留的旧版本有自己的配对指标 #11325463 (Python 3.12 x64): 0.093 s / 1592 KB，不混合测量或运行时。教学源码保持不变。

- `1423_strings_optimized.py`: 0.062 s / 1592 KB; 保留教学基础版 `1423_strings.py`: 0.109 s / 1372 KB.

`1423_strings_optimized.java`. 保留字节 KMP 和右旋转下标。两段定长 N 字节词直接读入最终数组，使用 4096 字节缓冲，不保存完整输入副本或解码 char 数组。int 前缀数组及回绕游标替代虚拟双倍首词扫描中的取模，字节相等支持全部允许值 33…255。时间、空间 O(N)，保留易读字符串版。

精确源代码 Java 1.8 Accepted #11326951：0.109 s / 1920 KB。2026-11-20 保存的当前 Java 比较：时间排名 2/99，内存排名 1/99。内存至少 1024 KB，因此两个严格指标都必须通过；两项均已通过。

- `1423_strings_optimized.java`: 0.109 s / 1920 KB; 保留的教学基础版 `1423_strings.java`: 0.156 s / 5744 KB; 时间变化 -30.1%; 内存变化 -66.6%.

`1423_strings_optimized.rs`. 保留字节 KMP 及右旋索引。前缀长度用 u32，扫描 s 接 s 去末字节的切片链，替代每位置取模而不分配双倍字符串。字节词保留33…255 字符。O(N) 时间空间，直接输出替代 Rust 格式化。

与 `1423_strings.rs` 相比：时间 0.031 s → 0.031 s；内存 3052 KB → 1 804 KB。

优化的 C++ 解法把前缀函数存成打包在 32 位字数组中的 18 位字段，因为每个值都小于
N ≤ 250 000 < 2^18，读取时一次从相邻的两个字中取出字段；每次访问多花几次移位，但
只占约 0.56 MB，而 `int` 值要 1 MB。此外它把 S 扫两遍，而不是构造 S + S，并用
`scanf` 把 S 和 T 读进两个 250 001 字节的静态缓冲区，而不是用 `cin` 读进
`std::string`：{1423_strings_optimized.cpp}。

优化的 Go 解法用 `int32` 而不是 8 字节的 `int` 存前缀函数，因为每个值都小于
N ≤ 250 000，并依据两个字符串的长度都是 N，用 `io.ReadFull` 把 S 和 T 直接读进恰
好 N 字节的数组，而不是读入全部输入再按字段切分：{1423_strings_optimized.go}。

### 实测改进

每个优化版本均已获 Accepted，并满足排名或资源改进准入条件。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1423_strings_optimized.cpp`: 时间降低 -106.67%; 内存降低 +40.82%; 基础版本: `1423_strings.cpp`.

- `1423_strings_optimized.go`: 时间降低 +0.00%; 内存降低 +40.39%; 基础版本: `1423_strings.go`.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1423_strings_optimized.py`：在该可比样本中，时间名次 11/55，内存名次 1/55。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

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
| [1423_strings_optimized.java](1423_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.109 s | 1920 KB | 11326951 |
| [1423_strings_optimized.py](1423_strings_optimized.py) | Python 3.12 x64 | strings | Linear I/O plus runtime substring search; O(N) bytes | AC | 0.062 s | 1592 KB | 11327848 |
| [1423_strings_optimized.rs](1423_strings_optimized.rs) | Rust 1.75 x64 | strings | O(N) time; O(N) space | AC | 0.031 s | 1804 KB | 11325527 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
