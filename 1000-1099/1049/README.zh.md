# 1049. 乘积的约数个数的末位数字

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · 难度 249 · number_theory

原题作者 Stanislav Vasiliev，出自 2000 年 3 月 25 日乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定十个整数 `a1 … a10`，每个都在 1 到 10000 之间。求乘积 `a1 · … · a10` 的正约数个数的末位数字。

时间限制：2 秒。内存限制：64 MB。

## 输入

十个整数，每行一个。

## 输出

一个数字：约数个数的末位。

## 评测方式

精确比较答案词元，空白排版无关。

- `1049_number_theory_optimized.go` (Go 1.14 x64): 14个仓库测试; 14个额外精确源码比较.

- `1049_number_theory_optimized.java` (Java 1.8): 14个仓库测试; 172个额外精确源码比较.

- `1049_number_theory_optimized.py` (PyPy 3.10 x64): 14个仓库测试.

## 样例

### 样例 1

输入：

```
1
2
6
1
3
1
1
1
1
1
```

输出：

```
9
```

### 样例 2

输入：

```
1
1
1
1
1
1
1
1
1
1
```

输出：

```
1
```

## 解法
若 `P = p1^e1 · p2^e2 · … · pk^ek`，`P` 的约数对每个指数独立地在 `0` 到 `ei` 之间选取，所以 `P` 恰有
`(e1 + 1)(e2 + 1)…(ek + 1)` 个约数。

乘积本身可能有 40 位，但根本用不到它：对每个数用试除法分解到其平方根（最多 100 步），把相同素数的指数相加，
再把各个 `(e + 1)` 模 10 相乘。`O(10 · √10000)`。

注意事项：

- 必须先把十个数中的指数加起来，再加 `1`：`2 · 2` 有 3 个约数，而不是 `2 · 2` 个；
- 大于平方根的素因子在试除之后剩下来，也要计入；
- 末位可能是 0（48 = `2^4 · 3` 有 10 个约数）。

## 优化解法

约数公式不变：分解十个数，累加同一素数的指数，把各指数加一后模十相乘。先一次移除二的幂，再试奇因子，最后大于一的余数必为素数。Go用uint8指数及已触及素数表，Java用无符号16位char数组，避免装箱映射。最大指数为10*floor(log2(10000))=130，适合Go uint8，却不适合Java有符号byte。六个不同素数的积已达30030，因此每个输入至多贡献五个。原生索引数组需O(V)初始化和存储，十次试除需O(C sqrt(V))。Python保留小指数字典并用原生位操作；内存与时间的交换另列实测。

- `1049_number_theory_optimized.go`: 0.015 s / 292 KB; 基础 `1049_number_theory.go`: 0.031 s / 1108 KB; 相对变化: 时间 -51.6%, 内存 -73.6%.
- `1049_number_theory_optimized.java`: 0.109 s / 368 KB; 基础 `1049_number_theory.java`: 0.140 s / 3880 KB; 相对变化: 时间 -22.1%, 内存 -90.5%.
- `1049_number_theory_optimized.py`: 0.109 s / 296 KB; 基础 `1049_number_theory.py`: 0.078 s / 456 KB; 相对变化: 时间 +39.7%, 内存 -35.1%.

`1049_number_theory_optimized.rs`. 边读取边分解十个数，以固定字节数组累加质因子指数。每个值不超过 10000，指数总和不超过 130，因此一个字节足够。扫描数组，把指数加一后的值相乘并对十取模。分解耗时 O(10√M)，最后扫描 O(M)，M=10000；存储为 M+1 字节和常数状态。 Rust 通过 C 运行库输入输出，避免完整的解码输入输出 String 和 Rust 格式化。简单且已通过评测的源代码保持不变。

与 `1049_number_theory.rs` 相比：时间 0.015 s → 0.015 s；内存 416 KB → 52 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1049_number_theory_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB | 11278665 |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB | 11278667 |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB | 11278675 |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB | 11278673 |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB | 11278679 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1049_number_theory_optimized.go](1049_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.015 s | 292 KB | 11309757 |
| [1049_number_theory_optimized.java](1049_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.109 s | 368 KB | 11308799 |
| [1049_number_theory_optimized.py](1049_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(C sqrt(V)) time; O(C log V) prime records | AC | 0.109 s | 296 KB | 11309728 |
| [1049_number_theory_optimized.rs](1049_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(10√M+M), M=10000 | AC | 0.015 s | 52 KB | 11325082 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
