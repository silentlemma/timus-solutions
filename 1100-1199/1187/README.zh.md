# 1187. 百分比之和为 100 的调查交叉表

[Timus 1187](https://acm.timus.ru/problem.aspx?space=1&num=1187) · 难度 2051 · strings

原题作者 Roman Elizarov，出自 2001–2002 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一份调查至多有 100 个问题，每个问题有 2 到 10 个单字符答案，记录的回答总数至多
10000。对每一对要求的问题，输出一张交叉表：每对答案各有多少人选择，并附上行
合计和列合计；每个数下面还要给出它占行合计和列合计的百分比。百分比是整数，每个
都由精确值向下或向上取整，使一行（或一列）不含合计的百分比之和恰为 100；合计为
零时百分比打印为 `-`。表格版式精确到每个字符。

时间限制：1 秒。内存限制：64 MB。

## 输入

调查名称，问题及其答案，`#`，每人一行答案代码，`#`，要求的表格，`#`。

## 输出

对每张表：标题行、照抄的两个问题、一个空行，以及由 6 个字符宽的单元格组成的
表格；表与表之间用一个空行分隔。

## 评测方式

只要每个百分比都是精确值的向下或向上取整、不含合计的行和列之和为 100%、合计处为
`100%`、零合计处为 `-`，任何取整方式都被接受；其余每个字符都必须完全一致。

## 样例

### 样例 1

输入：

```
New Year Phone Survey for ACM ICPC
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)
#
.@.
HH@
.@.
YFY
HQ*
H@.
YYY
.H@
HFY
HH@
#
Q01 Q02 Health vs greeting style
Q02 BYE Politeness matrix
#
```

输出：

```
New Year Phone Survey for ACM ICPC - Health vs greeting style
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)

       Q02:H Q02:Y Q02:F Q02:Q Q02:@ TOTAL
 Q01:H     2     0     1     1     1     5
         40%    0%   20%   20%   20%  100%
         66%    0%   50%  100%   33%   50%
 Q01:Y     0     1     1     0     0     2
          0%   50%   50%    0%    0%  100%
          0%  100%   50%    0%    0%   20%
 Q01:*     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 Q01:.     1     0     0     0     2     3
         33%    0%    0%    0%   67%  100%
         34%    0%    0%    0%   67%   30%
 Q01:@     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 TOTAL     3     1     2     1     3    10
         30%   10%   20%   10%   30%  100%
        100%  100%  100%  100%  100%  100%

New Year Phone Survey for ACM ICPC - Politeness matrix
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)

       BYE:Y BYE:* BYE:@ BYE:. TOTAL
 Q02:H     0     0     3     0     3
          0%    0%  100%    0%  100%
          0%    0%  100%    0%   30%
 Q02:Y     1     0     0     0     1
        100%    0%    0%    0%  100%
         33%    0%    0%    0%   10%
 Q02:F     2     0     0     0     2
        100%    0%    0%    0%  100%
         67%    0%    0%    0%   20%
 Q02:Q     0     1     0     0     1
          0%  100%    0%    0%  100%
          0%  100%    0%    0%   10%
 Q02:@     0     0     0     3     3
          0%    0%    0%  100%  100%
          0%    0%    0%  100%   30%
 TOTAL     3     1     3     3    10
         30%   10%   30%   30%  100%
        100%  100%  100%  100%  100%
```

## 解法

把各对答案计数填入表中，再把行合计作为多出的一列、列合计作为多出的一行；右下角
就是总人数。

取整方法：取一行（或一列）值 `v`，合计为 `T`。先把每个百分比 `100·v/T` 向下取整。
总和比 100 少某个 `d`，而舍去的小数部分之和恰为 `d`，所以至少有 `d` 个值有小数
部分。把小数部分最大的 `d` 个值各加一。对每一行和每一列（不含合计）都这样做，
包括合计行和合计列本身；合计单元格则为 `100%`（合计为零时为 `-`）。每张表
`O(人数 + 表格大小)`。

其余就是仔细打印：每个单元格右对齐、宽 6，每行的第二、三行以 6 个空格开头，问题
按输入原样照抄。

注意事项：

- 合计不能放进求和为 100 的向量里，否则每个和都会是 200；
- 样例在同一列中把 2/3 向下取整、把 1/3 向上取整，这只是另一种合法选择，所以输出
  会与样例不同，需要检查程序；
- 合计为零的行仍然有按列的百分比，除非列合计也为零，否则都是 0%。

每个输出都在 100 份随机调查上经过检查程序验证，同一检查程序也接受了另一份独立
编写的解答在这些数据上的输出。

## 各语言说明

- 所有语言的取整方式相同：按余数稳定排序，先增加余数最大的，余数相同时先增加
  靠前的单元格，所以五种语言输出的表格完全相同。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1187_strings.cpp](1187_strings.cpp) | G++ 13.2 x64 | strings | O(people + table) per table | AC | 0.015 s | 1008 KB |
| [1187_strings.go](1187_strings.go) | Go 1.14 x64 | strings | O(people + table) per table | AC | 0.031 s | 4656 KB |
| [1187_strings.java](1187_strings.java) | Java 1.8 | strings | O(people + table) per table | AC | 0.265 s | 10196 KB |
| [1187_strings.py](1187_strings.py) | Python 3.12 x64 | strings | O(people + table) per table | AC | 0.125 s | 2564 KB |
| [1187_strings.rs](1187_strings.rs) | Rust 1.75 x64 | strings | O(people + table) per table | AC | 0.031 s | 1296 KB |
