# 2023. 三个位置之间的步数

[Timus 2023](https://acm.timus.ru/problem.aspx?space=1&num=2023) · 难度 40 · implementation

原题作者 Alex Samsonov，出自 NEERC 2014 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三个目的地在直线上依次位于相邻的 0、1、2 号位置。每个收件标签属于唯一的位置，完整对应表如下：

| 位置 | 收件标签 |
| --- | --- |
| 0 | Alice, Ariel, Aurora, Phil, Peter, Olaf, Phoebus, Ralph, Robin |
| 1 | Bambi, Belle, Bolt, Mulan, Mowgli, Mickey, Silver, Simba, Stitch |
| 2 | Dumbo, Genie, Jiminy, Kuzko, Kida, Kenai, Tarzan, Tiana, Winnie |

从位置 0 开始，按照给定顺序处理 `n` 个标签。走到相邻位置需要一步，在正确位置处理标签不需要步数。
求总步数。最后一个标签处理完就结束，不要求返回位置 0。标签可以重复。
限制为 `1 ≤ n ≤ 1000`、1 秒、64 MB。

## 输入

第一行是 `n`，随后 `n` 行各含表中的一个标签，拼写及大小写与表完全相同。行的顺序就是处理顺序。
标签只含字母，长度不超过七。

## 输出

输出一个整数，表示总步数，范围为 0 到 `2n`，包含端点。

## 评测方式

按记号逐个比较输出。

## 样例

```
4
Aurora
Tiana
Ariel
Mulan
```

```
5
```

## 解法

对每个标签在表中查出它的位置并走过去：从位置 p 走到位置 q 需要 |p − q| 步。从位置
0 开始，把这些距离相加。`O(n)`。

在样例中，位置依次为 0 → 0 → 2 → 0 → 1，步数为 0 + 2 + 2 + 1 = 5。

注意事项：

- 处理第一个标签之前站在位置 0；
- 处理完最后一个标签后不需要返回。

## 优化解法

优化解法（C++、Java）逐字节读取输入，不保存任何名字。标签中唯一的大写字母就是首
字母，而首字母能区分位置：A、P、O、R 表示位置 0，B、M、S 表示位置 1，其余都表示
位置 2。数字 `n` 中没有大写字母，所以输入中的每个大写字母都开始下一个标签。C++
为 100 KB，而不是 400 KB，时间不变。Java 为 0.078 s，而不是 0.140 s；344 KB，而
不是 1964 KB。

优化的 Rust 解法和 C++、Java 解法一样逐字节扫描输入中的大写字母，而不是读入名字
再查表：232 KB，而不是 424 KB，时间不变。

## 各语言说明

没有特别需要注意的地方。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 400 KB | 11303356 |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1156 KB | 11303357 |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1964 KB | 11303358 |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 400 KB | 11303359 |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 424 KB | 11303360 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [2023_implementation_optimized.cpp](2023_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303660 |
| [2023_implementation_optimized.java](2023_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 344 KB | 11303663 |
| [2023_implementation_optimized.rs](2023_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 232 KB | 11303793 |
