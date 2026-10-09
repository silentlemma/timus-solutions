# 1094. 光标会回绕的单行显示屏

[Timus 1094](https://acm.timus.ru/problem.aspx?space=1&num=1094) · 难度 462 · simulation

原题作者 Stanislav Vasiliev，出自 2001 年 3 月 USU Open Collegiate Programming Contest（Senior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

显示屏显示一行 80 个字符，开始时全是空格，光标在最左边。按下字符键会把该字符写在光标处（替换原来的字符），并把
光标右移一格；`<` 和 `>` 只移动光标，不写字符。光标一旦越过左边缘或右边缘，就跳到最左边的位置。给定一行最多
10000 次按键，输出最后显示屏上的内容。

时间限制：0.25 秒。内存限制：64 MB。

## 输入

一行按键：字母、数字、`:;-!?.,`、空格、`<` 和 `>`。

## 输出

显示屏的 80 个字符。

## 评测方式

输出必须与期望文本相同；只忽略末尾的空白字符。

## 样例

### 样例 1

输入：

```
>><<<Look for clothes at the <<<<<<<<<<<<<<<second floor. <<<<<<<Fresh pizza and <<<<<<<<<<<<<<<<hamburger at a shop right to <<<<<<<<<<<<<the entrance. Call <<<<<<<<<< 123<-456<-8790 <<<<<<<<<<<<<<<<to order <<<<<<<<<<<<<<<<<computers< and office<<<<<<< chairs.
```

输出：

```
Look for second hamburger at computer and chairs.790                            
```

## 题解

用一个 80 个字符的数组和光标位置模拟。遇到 `<` 和 `>` 移动光标；其他按键写入字符并右移。每次按键后，如果光标
不在 `0 … 79` 内，就把它放回 0。`L` 次按键需要 `O(L)`。

注意事项：

- 越过左边缘也会让光标回到最左边，相当于原地不动：在位置 0 按 `<`，光标仍在 0；
- 写满第 80 个位置后光标回到第一个位置，在最后一个位置按 `>` 也一样；
- 空格是普通的按键，不能跳过，所以要整行读入，只去掉换行符；
- 这一行可能是空的，此时显示屏保持空白。

答案与另一个用字典保存已写格子的模拟程序做了核对。

## 各语言说明

- 五种语言都读取一行，并输出全部 80 个字符，包括末尾的空格。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1094_simulation.cpp](1094_simulation.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.015 s | 376 KB |
| [1094_simulation.go](1094_simulation.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 1092 KB |
| [1094_simulation.java](1094_simulation.java) | Java 1.8 | simulation | O(L) | AC | 0.093 s | 564 KB |
| [1094_simulation.py](1094_simulation.py) | Python 3.12 x64 | simulation | O(L) | AC | 0.078 s | 468 KB |
| [1094_simulation.rs](1094_simulation.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.046 s | 204 KB |
