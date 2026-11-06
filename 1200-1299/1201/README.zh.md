# 1201. 用方括号标出一个日期的月历

[Timus 1201](https://acm.timus.ru/problem.aspx?space=1&num=1201) · 难度 365 · implementation

原题作者 Alexander Klepinin，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 1600 年到 2400 年之间的一个日期，打印它所在月份的月历：七行，从星期一到
星期日，每周一列，给定日期用方括号括起来。闰年按格里高利历规则判断。

时间限制：1 秒。内存限制：64 MB。

## 输入

日、月、年。

## 输出

按样例格式输出恰好七行。每行以 `mon` … `sun` 开头；每周占五个字符，最后一周占
四个，但含有括号日期的格子仍占五个。日期数字在两个空格之后右对齐占两个字符。
给定日期前后的空格分别换成 `[` 和
`]`。

## 样例

### 样例 1

输入：

```
16 3 2002
```

输出：

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri   1    8   15   22   29
sat   2    9  [16]  23   30
sun   3   10   17   24   31
```

### 样例 2

输入：

```
1 3 2002
```

输出：

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri [ 1]   8   15   22   29
sat   2    9   16   23   30
sun   3   10   17   24   31
```

## 解法

计算从公元 1 年 1 月 1 日（格里高利历中是星期一）到该月 1 日的天数：`365·(y−1)`
加上闰日 `⌊(y−1)/4⌋ − ⌊(y−1)/100⌋ + ⌊(y−1)/400⌋`，再加上当年此前各月的天数。
对 7 取余就是 1 日所在的行，该月需要 `⌈(first + days)/7⌉` 列。之后每个格子就是
`7·column + row − first + 1`，只要它落在本月之内。每格输出五个字符，最后一列
省去末尾空格，但保留所选日期的右方括号。`O(1)`。

注意事项：

- 1900 年不是闰年，2000 年是；
- 一个月可能需要四、五或六列；
- 即使格子为空宽度也固定，所以在最后一周之前结束的行末尾保留空格；这些测试的
  期望输出在 `rstrip()` 去除整个输出末尾的空白后逐字符比较，而非逐行去除；
- 最后一列中带括号的日期仍占五个字符，包括右方括号 `]`（测试 04 和 08）；
- 括号中的一位数日期保留对齐：`[ 1]`。

月历已在 605 个日期上与另一份独立解答比对，其中包括范围的两端和若干个二月。

## 优化解法

C++ 和 Go 用公历闰年公式计算当月首日的星期，并直接在固定大小的字节缓冲区中生成日历单元。每个单元保留要求的空格和所选日期的括号。C++ 逐行输出。Go 在一个缓冲区生成七行日历，并用固定字节缓冲区读取日期。它直接访问标准句柄并完成部分写入。

已通过评测的基础实现 [1201_implementation.java](1201_implementation.java), [1201_implementation.py](1201_implementation.py), [1201_implementation.rs](1201_implementation.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- 所有语言都按相同的宽度逐格拼出每一行。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1201_implementation.cpp](1201_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 196 KB | 11283545 |
| [1201_implementation.go](1201_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB | 11283546 |
| [1201_implementation.java](1201_implementation.java) \* | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1752 KB | 11283552 |
| [1201_implementation.py](1201_implementation.py) \* | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 560 KB | 11283551 |
| [1201_implementation.rs](1201_implementation.rs) \* | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 252 KB | 11283556 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1201_implementation_optimized.cpp](1201_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 104 KB | 11311038 |
| [1201_implementation_optimized.go](1201_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 284 KB | 11311222 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
