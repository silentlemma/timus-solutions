# 1212. 海战棋中再放一艘船的位置

[Timus 1212](https://acm.timus.ru/problem.aspx?space=1&num=1212) · 难度 493 · geometry

原题作者 Anton Botov 和 Anatoly Uglov，出自 2002 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

海战棋盘有 `N` 行 `M` 列，都不超过 30000，上面已经放了最多 30 艘长 1 到 4 格的
船。船与船不能接触，连角也不行。统计再横向或纵向放一艘 `K` 格船的方法数。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`、`M` 和船数 `L`；然后每艘船给出其左上格的列号和行号、长度以及 `V` 或 `H`；
最后是 `K`。

## 输出

新船可放位置的数量。

## 样例

### 样例 1

输入：

```
4 4 2
1 2 2 V
3 1 2 H
2
```

输出：

```
4
```

## 解法

每艘已放的船都禁止它周围的矩形，即四周各扩一格。先统计横向的位置。在每个禁止
矩形的上边以及下边的下一行处把行切分成若干带；同一带内每一行碰到的矩形都相同，
所以带内各行的位置数相同。对带中的一行，按顺序取出被禁止的列区间，对它们之间的
每段空白加上 `max(0, 长度 − K + 1)`，再乘以带的高度。纵向的位置就是把棋盘转过来
再数一遍。单格船两个方向是同一种放法，所以只数一次。带最多 61 条，
`O(L² log L)`。

注意事项：

- 船的第一个数是列，第二个数是行；
- 单格船不能数两次；
- 禁止矩形会伸出棋盘边缘，切分带时要裁掉；
- 答案可达约 `1.8·10⁹`，超出 32 位整数。

答案已在 450 个随机小棋盘上与逐格的暴力解法比对，并在所有测试上与另一份独立
解答比对。

## 各语言说明

- 所有语言都给禁止矩形使用具名字段，两个方向共用同一个计数函数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1212_geometry.cpp](1212_geometry.cpp) | G++ 13.2 x64 | geometry | O(L² log L) | AC | 0.031 s | 432 KB |
| [1212_geometry.go](1212_geometry.go) | Go 1.14 x64 | geometry | O(L² log L) | AC | 0.031 s | 1144 KB |
| [1212_geometry.java](1212_geometry.java) | Java 1.8 | geometry | O(L² log L) | AC | 0.140 s | 1940 KB |
| [1212_geometry.py](1212_geometry.py) | Python 3.12 x64 | geometry | O(L² log L) | AC | 0.078 s | 684 KB |
| [1212_geometry.rs](1212_geometry.rs) | Rust 1.75 x64 | geometry | O(L² log L) | AC | 0.046 s | 232 KB |
