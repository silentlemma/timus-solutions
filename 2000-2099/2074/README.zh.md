# 2074. 按主题路径对题目分组

[Timus 2074](https://acm.timus.ru/problem.aspx?space=1&num=2074) · 难度 976 · implementation, sorting

原题作者 Mikhail Rubinchik。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

主题分类器是一棵以列表形式写出的树：每个标题是形如 `2.2.1.` 的编号加上主题名，其后可有一行或多行列出该主题的题号。对每个出现过的题目，输出它所属的主题，主题用从根到它的路径上的名称以点连接来描述。主题集合完全相同的题目输出在同一行。时间限制 2 秒，内存限制 256 MB。

## 输入

分类器，格式同样例。主题不超过 20 个，不同题号不超过 20 个，范围 1000 到 9999。主题名由 1 到 20 个小写字母和单个空格组成。编号按深度优先顺序给出，所以含 k 个数的标题是最近一个含 k − 1 个数的标题的子主题。

## 输出

每行形如“题号 : 主题”：组内题号按升序以 ", " 分隔，然后是 " : "，再是按字典序以 ", " 分隔的主题描述。各行本身按字典序排列。

## 样例

### 样例 1

输入：

```
1. graphs
1022
1065
2. geometry
1020
2.1. idea
1130
2.2. technique
1111 1065
1265
2.2.1. convex hull
1271
3. dynamic programming
1244
```

输出：

```
1020 : geometry
1022 : graphs
1065 : geometry.technique, graphs
1111, 1265 : geometry.technique
1130 : geometry.idea
1244 : dynamic programming
1271 : geometry.technique.convex hull
```

## 解法

逐行读入。第一个词以点结尾的行是标题；点的个数就是深度，所以把名称栈截到 depth − 1 项再压入新名称。当前主题的描述就是用点连接的栈。其他行是题号，每个题号的集合加入当前描述。题目只属于列出它的主题，不属于其祖先：样例中 1065 只在 graphs 和 geometry.technique 中。

然后把每个题目排好序的集合连接成键，键相同的题目归为一组，每组输出一行：排好序的题号和键。各行按普通字符串排序，其中空格在点之前，点在字母之前。主题和题目都不超过 20 个，工作量极小。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2074_implementation_sorting.cpp](2074_implementation_sorting.cpp) | G++ 13.2 x64 | implementation, sorting | O(1) | AC | 0.031 s | 808 KB |
| [2074_implementation_sorting.go](2074_implementation_sorting.go) | Go 1.14 x64 | implementation, sorting | O(1) | AC | 0.046 s | 1368 KB |
| [2074_implementation_sorting.java](2074_implementation_sorting.java) | Java 1.8 | implementation, sorting | O(1) | AC | 0.171 s | 4960 KB |
| [2074_implementation_sorting.py](2074_implementation_sorting.py) | Python 3.12 x64 | implementation, sorting | O(1) | AC | 0.109 s | 792 KB |
| [2074_implementation_sorting.rs](2074_implementation_sorting.rs) | Rust 1.75 x64 | implementation, sorting | O(1) | AC | 0.062 s | 796 KB |
