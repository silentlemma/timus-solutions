# 1622. 残局

[Timus 1622](https://acm.timus.ru/problem.aspx?space=1&num=1622) · 难度 3242 · backtracking

原题出自 2008 年冬季彼得罗扎沃茨克集训的 SPbSU ITMO Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

十字形 33 格棋盘上的独立钻石棋（7 × 7 的正方形去掉四个 2 × 2 的角，列为 A–G，行为
1–7）：32 枚棋子占满除中心 D4 以外的所有格子。一步是一枚棋子沿水平或竖直方向跳过相邻
的棋子落到空格上，被跳过的棋子移走。给定一个格子，输出 31 步，使最后唯一的棋子恰好
停在那里；否则输出 `Impossible`。

时间限制：2 秒。内存限制：64 MB。

## 输入

最后一枚棋子的格子。

## 输出

31 步 `from-to`，每行一步，或 `Impossible`。

## 样例

### 样例 1

输入：

```
D4
```

输出：

```
D2-D4
B3-D3
C1-C3
E1-C1
D3-B3
A3-C3
E3-E1
G3-E3
C4-C2
C1-C3
A4-C4
C4-C2
E4-C4
G4-E4
E4-E2
E1-E3
C5-C3
C2-C4
A5-C5
D5-B5
E6-E4
G5-E5
C7-C5
C4-C6
E7-C7
C7-C5
B5-D5
D5-F5
E3-E5
F5-D5
D6-D4
```

### 样例 2

输入：

```
D3
```

输出：

```
Impossible
```

## 解法

哪些格子可行由一个不变量决定。按 (r + c) mod 3 把格子分成三类。一次跳跃涉及一条线上
连续的三个格子，每类各一个，并使每一类的棋子数改变 1，所以三个奇偶性全部翻转。按
(r − c) mod 3 分类同样如此。31 次跳跃之后奇偶性是确定的，于是最后一枚棋子的两个余数都
确定，从而 r 和 c 模 3 也确定：它们必须与中心相同，而中心是可达的。棋盘上只剩下 D4、
D1、D7、A4 和 G4；其他格子都是 `Impossible`。

步骤由深度优先搜索给出：棋盘用 33 位掩码表示，并记住已经证明走不通的局面。搜索 D4 或
D7 只需几分之一秒，直接搜 D1 则慢得多；但初始局面是对称的，A4、D1 和 G4 就是 D7 转过
若干个直角：先搜 D7，再把答案的每一步旋转过去。

易错点：

- 样例中的步骤只是答案之一，由检查器重放验证；
- 紧挨中心的格子（D3）就已经不可能。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1622_backtracking.cpp](1622_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(S) | AC | 0.015 s | 420 KB |
| [1622_backtracking.go](1622_backtracking.go) | Go 1.14 x64 | backtracking | O(S) | AC | 0.031 s | 1244 KB |
| [1622_backtracking.java](1622_backtracking.java) | Java 1.8 | backtracking | O(S) | AC | 0.109 s | 1952 KB |
| [1622_backtracking.py](1622_backtracking.py) | Python 3.12 x64 | backtracking | O(S) | AC | 0.093 s | 804 KB |
| [1622_backtracking.rs](1622_backtracking.rs) | Rust 1.75 x64 | backtracking | O(S) | AC | 0.046 s | 460 KB |
