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

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1049_number_theory.cpp`; 覆盖源码 `1049_number_theory.cpp`; 时间/内存名次 1/1, 其他作者记录 121/121.

- Go: 首选教学基础 `1049_number_theory.go`; 覆盖源码 `1049_number_theory_optimized.go`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Java: 首选教学基础 `1049_number_theory.java`; 覆盖源码 `1049_number_theory_optimized.java`; 时间/内存名次 3/1, 其他作者记录 4/4.

- Python/PyPy: 首选教学基础 `1049_number_theory.py`; 覆盖源码 `1049_number_theory_optimized.py`; 时间/内存名次 44/1, 其他作者记录 54/54.

- Rust: 首选教学基础 `1049_number_theory.rs`; 覆盖源码 `1049_number_theory.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

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

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
