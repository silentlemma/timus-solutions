# 2056. 判断奖学金类别

[Timus 2056](https://acm.timus.ru/problem.aspx?space=1&num=2056) · difficulty 41 · implementation

民间题目，出自 2015 年乌拉尔体育编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

学生参加了 n 门考试，成绩在 3 到 5 之间。确定奖学金：有任何 3 分则为 `None`；否则全是 5 分为 `Named`；否则平均分不低于 4.5 为 `High`；其余情况为 `Common`。时间限制 1 秒，内存限制 64 MB。

## 输入

考试数 n（1 ≤ n ≤ 10），接下来 n 行各一个成绩。

## 输出

一个单词，区分大小写。

## 评测方式

按记号逐个比较输出。

## 样例

```
3
5
5
4
```

```
High
```

```
3
3
3
3
```

```
None
```

第一个示例总分十四，`2·14≥9·3`，平均分超过 4.5；没有三分，但存在四分，所以为 `High`。第二个示例出现三分，最高优先级规则直接给出 `None`。

## 解法

读入成绩，同时记录总和 S 和最小值。然后按顺序应用规则：只要有 3 就是 `None`；全是
5 就是 `Named`；平均分至少 4.5 就是 `High`，用整数检查 2S ≥ 9n；其余情况为
`Common`。`O(n)`。

注意事项：

- 有 3 时平均分再高也没用；
- 全是 5 是 `Named`，不是 `High`；
- 4.5 的门槛包含等号：一个 4 和一个 5 得到 `High`。

## 优化解法

`2056_implementation_optimized.py`. 把每个成绩解析为整数，仅记录是否有 3 及 4 的数量。成绩为 3,4,5 且无 3 时，平均数至少 4.5 等价于 4 的数量乘二不超过 n。保留四个奖学金输出词。免去逐项最小值及总和更新；不同于被排除的字节拼写实验，本版按数值处理加号和前导零。时间 O(n)，输入记号存储 O(I)，保留简单平均数版。 Accepted 行标明实际评测运行时及成对时间/内存。先 flush 输出，再以 os._exit(0) 跳过解释器清理；实测内存收益属于该运行时，不代表渐近加速。

与 `2056_implementation.py` 相比：时间 0.078 s → 0.125 s；内存 472 KB → 228 KB。

优化的 C++ 解法用 `scanf` 读入、用 `puts` 输出，而不是使用 `iostream` 和
`std::string`：116 KB，而不是 420 KB，时间不变。

`2056_parsing_optimized.go`. 使用有界字节缓冲解析十进制成绩，直接读取标准输入并完整写出答案。遇到成绩 3 即可确定 None，无须读取其余成绩。否则保留最小值、总和以及对 4.5 阈值的整数比较。最坏时间 O(n)，额外空间 O(1)，简单版本保持不变。

Accepted #11329388 (Go 1.14 x64): **0.015 s / 260 KB**.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`2056_implementation_optimized.py`：在该可比样本中，时间名次 272/297，内存名次 1/297。

当前准入和星号遵循统一的[排名标准](../../RATING_CRITERIA.md)：前十或前 15%，同编译器的小样本改用规定的参考提交比较。我们的内存低于 1024 KB 时仅比较时间。此前测量描述各自的历史提交。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB | 11293663 |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB | 11293666 |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 420 KB | 11303532 |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB | 11293667 |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB | 11293678 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2056_implementation_optimized.cpp](2056_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 116 KB | 11303966 |
| [2056_implementation_optimized.py](2056_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(I) space | AC | 0.125 s | 228 KB | 11325602 |
| [2056_parsing_optimized.go](2056_parsing_optimized.go) | Go 1.14 x64 | parsing | O(n) time; O(1) auxiliary space | AC | 0.015 s | 260 KB | 11329388 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
