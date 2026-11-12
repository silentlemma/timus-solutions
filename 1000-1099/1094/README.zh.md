# 1094. 光标会回绕的单行显示屏

[Timus 1094](https://acm.timus.ru/problem.aspx?space=1&num=1094) · 难度 466 · simulation

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

## 优化解法

新的 C++、Go、Rust 流式读取按键，只保存 80 个显示格和光标，不保留整行。零位置左移仍为零；最后一格右移或写入后回零。空格是普通写入。首个行尾或 EOF 后停止，输出全部 80 格，包括尾部空格。时间 O(L)、额外存储 O(80)，Go 输入缓冲有界。C++/Rust 使用 C runtime 字符输入输出，Rust 用 C 入口；Go 使用标准句柄。保留简单文件；Java/Python 复用符合标准的基础版。

已通过评测的基础实现 [1094_simulation.java](1094_simulation.java), [1094_simulation.py](1094_simulation.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- 五种语言都读取一行，并输出全部 80 个字符，包括末尾的空格。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1094_simulation.cpp](1094_simulation.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.015 s | 376 KB | 11279111 |
| [1094_simulation.go](1094_simulation.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 1092 KB | 11279112 |
| [1094_simulation.java](1094_simulation.java) | Java 1.8 | simulation | O(L) | AC | 0.093 s | 564 KB | 11279114 |
| [1094_simulation.py](1094_simulation.py) \* | Python 3.12 x64 | simulation | O(L) | AC | 0.078 s | 468 KB | 11279113 |
| [1094_simulation.rs](1094_simulation.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.046 s | 204 KB | 11279115 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1094_simulation_optimized.cpp](1094_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.001 s | 76 KB | 11315263 |
| [1094_simulation_optimized.go](1094_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 276 KB | 11315265 |
| [1094_simulation_optimized.rs](1094_simulation_optimized.rs) \* | Rust 1.75 x64 | simulation | O(L) | AC | 0.031 s | 52 KB | 11315266 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
