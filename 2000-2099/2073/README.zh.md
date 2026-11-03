# 2073. 比赛记录汇总表

[Timus 2073](https://acm.timus.ru/problem.aspx?space=1&num=2073) · 难度 242 · implementation

原题作者 Kirill Borozdin（由 Kirill Borozdin 和 Alexey Danilyuk 整理），出自 2015 年乌拉尔地区程序设计团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出 n ≤ 100 场比赛的记录：由 1 到 30 个拉丁字母、数字和空格组成的名称，日期 DD.MM.YY，题目数 p ≤ 13 和提交数 s ≤ 100，然后 s 条提交，每条为题目字母和评测结果。用 `+`、`-`、`|` 画出表格：一行表头，每场比赛一行，包括补齐到 30 个字符的名称、日期（8 个字符）和 13 个标记，对应字母 A … M。若题目至少通过一次，标记为 `o`；提交过但从未通过为 `x`；比赛中有该题但未提交为 `.`；比赛中没有该题则为空格。时间限制 1 秒，内存限制 64 MB。

## 输入

n，然后对每场比赛给出名称行、日期行、“p s”行和 s 行“字母 结果”。结果是 `Accepted`、`Wrong Answer`、`Runtime Error`、`Time Limit Exceeded`、`Memory Limit Exceeded`、`Compilation Error` 之一。

## 输出

按样例格式输出表格，表头前、表头后和每场比赛后各有一条边框线。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入：

```
2
Codeforces Gamma Round 512
29.02.16
5 4
A Accepted
B Accepted
C Accepted
E Accepted
URKOP
17.10.15
12 11
A Accepted
B Wrong Answer
B Time Limit Exceeded
J Accepted
B Accepted
J Time Limit Exceeded
J Accepted
F Accepted
E Runtime Error
H Accepted
E Runtime Error
```

输出：

```
+------------------------------+--------+-------------+
|Contest name                  |Date    |ABCDEFGHIJKLM|
+------------------------------+--------+-------------+
|Codeforces Gamma Round 512    |29.02.16|ooo.o        |
+------------------------------+--------+-------------+
|URKOP                         |17.10.15|oo..xo.o.o.. |
+------------------------------+--------+-------------+
```

## 解法

每场比赛先放 p 个点和 13 − p 个空格。结果为 `Accepted` 的提交把对应标记设为 `o`；其他结果在标记还不是 `o` 时设为 `x`。然后输出各行，名称用空格补齐到 30 个字符。时间复杂度为 O(input)。

名称中可能有空格，所以按行读入，并去掉行尾的空格和回车（名称不会以空格结尾）。标记保留末尾的空格：样例中第二行在边框前以 `.. ` 结尾。

## 优化解法

比赛评分和表格精确布局不变。用有界行缓冲和 ASCII 行缓冲逐场读取输出，不保留全部输入及完整输出串。姓名、日期文本及填充宽度必须原样保持。缓冲长度来自字段上界，数字字段单独解析，不能按文本字段长度截断。

- `2073_implementation_optimized.cpp`: 0.015 s / 112 KB; 基础版 `2073_implementation.cpp`: 0.001 s / 356 KB; 相对基础版的变化: 时间 -0.0%, 内存 -68.5%.
- `2073_implementation_optimized.java`: 0.093 s / 440 KB; 基础版 `2073_implementation.java`: 0.093 s / 2224 KB; 相对基础版的变化: 时间 -0.0%, 内存 -80.2%.
- `2073_implementation_optimized.py`: 0.078 s / 464 KB; 基础版 `2073_implementation.py`: 0.062 s / 1196 KB; 相对基础版的变化: 时间 +25.8%, 内存 -61.2%.
- `2073_implementation_optimized.rs`: 0.015 s / 224 KB; 基础版 `2073_implementation.rs`: 0.015 s / 732 KB; 相对基础版的变化: 时间 -0.0%, 内存 -69.4%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `2073_implementation.cpp`; 覆盖实现 `2073_implementation_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 32/32.

- Go: 优先教学基础版 `2073_implementation.go`; 覆盖实现 `2073_implementation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `2073_implementation.java`; 覆盖实现 `2073_implementation.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `2073_implementation.py`; 覆盖实现 `2073_implementation_optimized.py`; 时间/内存名次 1/2, 其他作者记录 9/9.

- Rust: 优先教学基础版 `2073_implementation.rs`; 覆盖实现 `2073_implementation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.001 s | 356 KB | 11309231 |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB | 11294474 |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.093 s | 2224 KB | 11309232 |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1196 KB | 11309233 |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 732 KB | 11309234 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2073_implementation_optimized.cpp](2073_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(input+output) | AC | 0.015 s | 112 KB | 11308727 |
| [2073_implementation_optimized.java](2073_implementation_optimized.java) | Java 1.8 | implementation | O(input+output) | AC | 0.093 s | 440 KB | 11308732 |
| [2073_implementation_optimized.py](2073_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(input+output) | AC | 0.078 s | 464 KB | 11308735 |
| [2073_implementation_optimized.rs](2073_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(input+output) | AC | 0.015 s | 224 KB | 11308736 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
