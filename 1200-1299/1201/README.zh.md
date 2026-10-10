# 1201. 用方括号标出一个日期的月历

[Timus 1201](https://acm.timus.ru/problem.aspx?space=1&num=1201) · 难度 364 · implementation

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
四个，日期数字在两个空格之后右对齐占两个字符。给定日期前后的空格分别换成 `[` 和
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
`7·column + row − first + 1`，只要它落在本月之内。`O(1)`。

注意事项：

- 1900 年不是闰年，2000 年是；
- 一个月可能需要四、五或六列；
- 即使格子为空宽度也固定，所以在最后一周之前结束的行末尾保留空格；这些测试的
  期望输出逐字符比较；
- 括号中的一位数日期保留对齐：`[ 1]`。

月历已在 605 个日期上与另一份独立解答比对，其中包括范围的两端和若干个二月。

## 各语言说明

- 所有语言都按相同的宽度逐格拼出每一行。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1201_implementation.cpp](1201_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 196 KB |
| [1201_implementation.go](1201_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB |
| [1201_implementation.java](1201_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1752 KB |
| [1201_implementation.py](1201_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 560 KB |
| [1201_implementation.rs](1201_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 252 KB |
