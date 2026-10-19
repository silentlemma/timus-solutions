# 2115. 至多交换一次使队列有序

[Timus 2115](https://acm.timus.ru/problem.aspx?space=1&num=2115) · 难度 228 · sorting

原题作者 Ivan Smirnov，出自 2019 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 名学生站成一排，身高为 aᵢ。若队列按升序或降序排列就合格。判断它是否已经合格，能否通过交换两名学生使其合格（以及交换哪两名），或者都不行。任何能修正的交换都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

n ≤ 10⁵，然后是身高，至多 10⁹。

## 输出

`Nothing to do here`；或 `Yes` 和两个位置；或 `No hope`。

## 评测方式

检查器比较结论，对 `Yes` 交换输出的两名学生后检查顺序。

## 样例

### 样例 1

输入：

```
3
150 160 170
```

输出：

```
Nothing to do here
```

### 样例 2

输入：

```
4
140 160 150 170
```

输出：

```
Yes
2 3
```

## 解法

把身高排序；目标是排好的队列或其反转。一次交换只改变两个位置，所以只有当队列与目标恰好在两个位置 i、j 不同时才可能变成目标，而且恰好在 aᵢ 与 aⱼ 互为对方目标值时成功。两个目标都试一遍，排序耗时 O(n log n)。

第二个样例中 140 160 150 170 与升序在位置 2 和 3 不同，交换它们就有序了（交换 1 和 4 则得到降序）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2115_sorting.cpp](2115_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.109 s | 2556 KB |
| [2115_sorting.go](2115_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.140 s | 5696 KB |
| [2115_sorting.java](2115_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3676 KB |
| [2115_sorting.py](2115_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.140 s | 15740 KB |
| [2115_sorting.rs](2115_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.046 s | 3524 KB |
