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

处理完一个标签后，只需记住当前位置。三组首字母互不相交：`A, P, O, R` 对应位置 0，
`B, M, S` 对应位置 1，其余合法首字母 `D, G, J, K, T, W` 对应位置 2。
输入保证标签来自表格，因此可用首字母代替完整查表。

初始化 `position = 0`、`steps = 0`。依次求标签位置 `target`，把
`abs(target - position)` 加到 `steps`，再令 `position = target`。
处理恰好 `n` 个标签后输出 `steps`。不能排序或改变顺序。

证明：从位置 `p` 到 `q`，每步只能改变一单位坐标，故至少走 `|q-p|` 步；
直接朝 `q` 走恰好达到此下界。给定顺序固定了所有连续目的地对，也固定了最初的位置 0，
所以各段准确距离之和就是所求总步数。归纳可知，每处理一个标签，当前位置与累计步数都正确。
最后一个标签后没有额外的一段路程。

样例的位置依次为 `0 → 0 → 2 → 0 → 1`，步数为 `0 + 2 + 2 + 1 = 5`。
由于名称长度有界，时间为 `O(n)`。扫描只用 `O(1)` 个计数器；这些程序保存输入标签，
因此总额外空间是 `O(n)`。若逐项读取并处理，可把存储降到 `O(1)`。

注意事项：

- 处理第一个标签前就处于最左侧的位置。
- 两个外侧位置之间需要两步，同一位置之间需要零步。
- 保留重复标签与原顺序；末尾无需返回。
- 注意表中 `Mickey`、`Kuzko`、`Phoebus` 的拼写。首字母表示目的地，
  不是字母表区间，也不是某个小格的编号。

## 各语言说明

五种语言均采用相同的扫描，普通整数足够，答案至多 2000。C++ 使用字符串成员查找，
Go 查找 ASCII 首字母对应的 rune，Rust 查找字节，Java 使用 `indexOf`，Python 使用字符串成员判断。
缓冲输入足以处理 1000 个标签，CPython 无需更换运行时。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 460 KB |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1160 KB |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 596 KB |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 388 KB |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 248 KB |
