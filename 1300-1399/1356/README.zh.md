# 1356. 来点简单的

[Timus 1356](https://acm.timus.ru/problem.aspx?space=1&num=1356) · 难度 298 · number_theory

原题作者 Aleksandr Bikbaev，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对 T ≤ 20 个数 N（2 ≤ N ≤ 10⁹）中的每一个，把 N 写成尽可能少的素数之和，并输出这些素数。

时间限制：1 秒。内存限制：64 MB。

## 输入

T，然后是 T 行，每行一个 N。

## 输出

对每个 N 输出一行素数。任何项数最少的和都可以。

## 样例

### 样例 1

输入：

```
7
2
27
85
192
14983
3
7
```

输出：

```
2
23 2 2
2 83
11 181
14983
3
7
```

## 解法

- 若 N 是素数，一个就够。
- 若 N 是偶数，两个就够：哥德巴赫猜想虽未被证明，但已验证到远超 10⁹。依次试 p = 2, 3, 4, …，直到 p 和
  N − p 都是素数。
- 若 N 是奇数，两个素数之和中必有 2，因为两个奇素数之和是偶数。所以恰好当 N − 2 是素数时两个就够。
- 否则需要且只需三个：取不超过 N − 4 的最大素数 p。余下的 N − p 是不小于 4 的偶数，按上面的方法拆成两个素数。

素性用以 2、3、5、7 为底的 Miller–Rabin 检验，它对小于 3.2·10⁹ 的所有数都是准确的。10⁹ 以内素数间隔小于 300，
而在略小于 10⁹ 的 200 000 个偶数上，哥德巴赫分解中最小的素数从未超过 919，所以每个答案只需几百次检验。`O(T · g · log N)`，其中 g 为尝试的候选数。

注意事项：

- 奇数 N 不可能拆成两个奇素数，所以要单独检查含 2 的情况（样例中 `85 = 2 + 83`）；
- 4 = 2 + 2 是唯一用到 2 的偶数拆分（测试 03）；
- 取最大素数后剩下的部分至少为 4，因为 2 不是两个素数之和；
- T 可以为 0（测试 04）。

对 20 000 以内的所有 N 以及 2 000 个 10⁹ 以内的随机 N，检查了答案由素数组成、和正确且项数最少；Miller–Rabin
检验在 203 000 个数上与试除法比较过。测试由检查程序评判，接受任何最短的和。

## 优化解法

Go 和 Rust 沿用适用于 N ≤ 10⁹、底数为 2、3、5、7 的确定性 Miller–Rabin 判定和最少质数项数的搜索。输入按固定大小的字节块读取，每个答案的一、二或三项直接以十进制字符写入固定字节输出缓冲区，不创建临时格式化字符串。Go 直接访问标准句柄并完成部分写入。Rust 通过 C main 启动，通过 C 运行库传输缓冲区。

通过评测的 Rust 1.75 x64 版本耗时 0.031 秒，基础版为 0.015 秒，内存为 60 KB，基础版为 224 KB。

已通过评测的基础实现 [1356_number_theory.cpp](1356_number_theory.cpp), [1356_number_theory.java](1356_number_theory.java), [1356_number_theory.py](1356_number_theory.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- Miller–Rabin 中的乘积小于 10¹⁸，所以各语言用 64 位整数就够了。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1356_number_theory.cpp](1356_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 192 KB | 11285274 |
| [1356_number_theory.go](1356_number_theory.go) | Go 1.14 x64 | number_theory | O(T·g·log N) | AC | 0.031 s | 1100 KB | 11285275 |
| [1356_number_theory.java](1356_number_theory.java) | Java 1.8 | number_theory | O(T·g·log N) | AC | 0.109 s | 516 KB | 11285277 |
| [1356_number_theory.py](1356_number_theory.py) \* | Python 3.12 x64 | number_theory | O(T·g·log N) | AC | 0.109 s | 664 KB | 11285276 |
| [1356_number_theory.rs](1356_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 224 KB | 11285279 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1356_number_theory_optimized.go](1356_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 308 KB | 11311220 |
| [1356_number_theory_optimized.rs](1356_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(T·g·log N) | AC | 0.031 s | 60 KB | 11311225 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
