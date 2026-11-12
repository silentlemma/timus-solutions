# 2046. 固定课程表中的整词换行

[Timus 2046](https://acm.timus.ru/problem.aspx?space=1&num=2046) · difficulty 507 · implementation

原题作者 Oleg Dolgorukov，出自 2015 年乌拉尔体育编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

绘制四行课次、三列星期的表格，星期列依次为 Tuesday、Thursday、Saturday。单元格内容宽度为十。保留名称单词及顺序，同一行单词间一个空格；若下一个单词连同分隔空格能放下，就留在本行，否则换行，不拆词。内容靠上、靠左，每行右侧补空格至十字符，不足的单元格行为空格。每个表格行的高度等于其最高单元格，整行为空时高度为一。交点用 `+`，横边用 `-`，竖边用 `|`，没有额外标题。

## 输入

给出 `1≤n≤12` 门课程，每门占两行：名称，以及星期和课次编号。名称含一至五个单词，单词间恰一个空格，无首尾空格；每个单词含一至十个大小写拉丁字母。名称两两不同。星期为 `Tuesday`、`Thursday` 或 `Saturday`，课次为 `1..4`；没有两门课占同一个位置。时间限制 1 秒，内存限制 64 MB。

## 输出

只输出表格，精确检查内部空格、换行及边界位置，末尾保留换行。横边为 `+----------+----------+----------+`，每行 34 个字符。设四个内容行高度之和为 `H`，总行数为 `H+5`，至多 25。

## 评测方式

输出逐字符精确比较，只有最后的换行可以不同。

## 样例

```
9
Physics
Thursday 3
Maths
Tuesday 1
Chemistry
Thursday 1
Physical education
Saturday 2
Astronomy
Saturday 4
Urban geography
Tuesday 4
History
Saturday 1
Modeling
Thursday 2
Biology
Thursday 4
```

```
+----------+----------+----------+
|Maths     |Chemistry |History   |
+----------+----------+----------+
|          |Modeling  |Physical  |
|          |          |education |
+----------+----------+----------+
|          |Physics   |          |
+----------+----------+----------+
|Urban     |Biology   |Astronomy |
|geography |          |          |
+----------+----------+----------+
```

第一行三个名称都只占一行。第二行的 `Physical education` 放不进十列，需要 `Physical` 和 `education` 两行，因此整个课次行变成两行，星期二空单元格和 `Modeling` 的第二行补空格。`Urban geography` 同理使最后一个课次行占两行。课程仍位于指定星期和课次。

## 解法

单独换行每个名称。维护当前行：空行直接放下一个词；否则若加上空格及下一个词后总长不超过十，就追加；超出则结束当前行，用该词开始新行。按课次减一、固定星期索引保存至网格。

每处理完一个词，所有已结束行都包含从其起点能放下的最长连续单词前缀，当前行按原顺序包含其余已处理词。追加能放下的词保持此性质；若放不下，则旧词加新词必超过宽度，开始新行恰好符合题意。每个单词自身不超过十，故不会丢词、拆词或溢出。

每个课次取三格高度和一的最大值，输出对应行数。在层 `r`，每格输出其第 `r` 行或空串，再右补至十字符。这保留独立换行，得到靠上靠左对齐，且完整空行仍占一行。表格前一条横边、每个课次后一条横边，正好五条。输入位置唯一，课程不会覆盖。

令 `L` 为名称总长度，`C=3`、`W=10`，`H≤20` 为内容高度之和。包含输出缓冲的时间和空间为 `O(L+WCH)`；流式版本所需输出存储更少。本题 `L≤648`，完整输出至多 875 字节。

## 优化解法

C++、Go 保持贪心换行，但直接写入定长字符格：四节、三天、至多五行、宽十，仅 600 个填空格字符。每行高度从一开始，随换行增加；每个词只复制一次到最终位置。复用 35 字节输出行及边框。单词与填充空格共用格数组。整行读取课程名，保留大小写、空行和所有右侧空格。输入 L 字节、输出 B 字节时，时间 O(L+B)。表格和行缓冲区大小固定。C++ 逐名读取、逐行输出。Go 通过标准句柄将输入读入 1024 字节缓冲区，收集至多 875 字节结果后写出。Java、Python 和 Rust 复用达标基础版。

已通过评测的基础实现 [2046_implementation.java](2046_implementation.java), [2046_implementation.py](2046_implementation.py), [2046_implementation.rs](2046_implementation.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

原 Go 用 scanner，新 C++/Go 整行读名称并填入定长补空格字符格。换行计入词间空格，保留 Tuesday/Thursday/Saturday 顺序、空行、大小写及右侧填充。Java 用类型列表和小 builder，Rust 用自有字符串，Python 在 CPython3.12 下用独立列表。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2046_implementation.cpp](2046_implementation.cpp) | G++ 13.2 x64 | implementation | O(L+WCH) | AC | 0.015 s | 436 KB | 11293468 |
| [2046_implementation.go](2046_implementation.go) | Go 1.14 x64 | implementation | O(L+WCH) | AC | 0.031 s | 1112 KB | 11293471 |
| [2046_implementation.java](2046_implementation.java) | Java 1.8 | implementation | O(L+WCH) | AC | 0.093 s | 580 KB | 11293476 |
| [2046_implementation.py](2046_implementation.py) \* | Python 3.12 x64 | implementation | O(L+WCH) | AC | 0.078 s | 536 KB | 11293472 |
| [2046_implementation.rs](2046_implementation.rs) \* | Rust 1.75 x64 | implementation | O(L+WCH) | AC | 0.015 s | 232 KB | 11293480 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [2046_implementation_optimized.cpp](2046_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(L+B) | AC | 0.015 s | 112 KB | 11315447 |
| [2046_implementation_optimized.go](2046_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(L+B) | AC | 0.015 s | 276 KB | 11315843 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
