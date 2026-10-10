# 1197. 一个孤立的马能攻击多少格

[Timus 1197](https://acm.timus.ru/problem.aspx?space=1&num=1197) · 难度 28 · implementation

原题为民间流传的题目，出自 2002 年 3 月 2 日第五届中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

棋盘上只有一个马。对给出的 `N ≤ 64` 个格子中的每一个，求马在那里能攻击到棋盘
上的多少个格子。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后是 `N` 个用国际象棋记法表示的格子：字母 `a` 到 `h` 表示列，数字 `1`
到 `8` 表示行。

## 输出

对每个格子，在单独一行输出被攻击的格子数。

## 样例

### 样例 1

输入：

```
3
a1
d4
g6
```

输出：

```
2
8
6
```

## 解法

马有八种可能的跳法：朝一个方向走两格，再横向走一格。把八种都试一遍，统计落在
棋盘内的个数。`O(N)`。

注意事项：

- 在边上或角上只有一部分跳法留在棋盘内，所以每一跳的两个坐标都要检查；
- 字母是列、数字是行，不过棋盘是对称的，弄反了也不影响答案。

答案已在全部 64 个格子上与另一份独立解答比对。

## 各语言说明

- 所有语言都把八种跳法放在表里循环处理。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1197_implementation.cpp](1197_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.001 s | 396 KB |
| [1197_implementation.go](1197_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1072 KB |
| [1197_implementation.java](1197_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1576 KB |
| [1197_implementation.py](1197_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.046 s | 328 KB |
| [1197_implementation.rs](1197_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 216 KB |
