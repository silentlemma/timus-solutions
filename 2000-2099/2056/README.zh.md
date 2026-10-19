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

扫描成绩，维护总和 `S`、最小值 `q`，初始分别为零和五。处理每个前缀后，它们恰好是前缀总和与最小值，因为新成绩加入总和，并与原最小值比较。处理完 `n` 项后，`q=3` 当且仅当存在三分，此时先输出 `None`，不考虑平均值。

否则 `q=5` 当且仅当成绩全部为五，因为五是合法最大值，此时输出 `Named`。若两项都不满足，则只有四分和五分，且至少有一个四分。由于 `n>0`，条件 `S/n≥4.5` 等价于精确整数比较 `2S≥9n`；成立输出 `High`，否则输出 `Common`。这些判断按规定顺序覆盖全部情况且互斥，因此算法正确。

即使平均分很高，三分也优先取消奖学金。全五分必须是 `Named` 而非 `High`。阈值包含相等，四分与五分组合应为 `High`。不要先用整数除法截断平均值。仅有一次考试时，三、四、五分分别对应 `None`、`Common`、`Named`，注意大小写。

## 各语言说明

一次扫描 `O(n)` 时间，工作状态 `O(1)`；Python 和 Rust 另保存 `O(n)` 输入文本或令牌，其他版本用缓冲流读取。算术全部精确：`S≤50`、`2S≤100`、`9n≤90`。五个版本使用相同三个统计量；Python 为 CPython 3.12，无需浮点除法。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 452 KB |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB |
