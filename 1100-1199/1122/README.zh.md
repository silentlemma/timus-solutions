# 1122. 把 4 × 4 棋盘变成单一颜色的最少步数

[Timus 1122](https://acm.timus.ru/problem.aspx?space=1&num=1122) · 难度 250 · bitmask

原题作者 Leonid Volkov、Oleg Kats 和 Alexander Somov，出自 2001 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`4 × 4` 的棋盘上放着双面棋子，白面（`W`）或黑面（`B`）朝上。一步选择一个格子，并翻转以它为中心的固定 `3 × 3`
模板所标记的棋子；模板可以任意，不必对称，超出棋盘的部分忽略。求使全部 16 枚棋子同色的最少步数，或输出 `Impossible`。

时间限制：1 秒。内存限制：64 MB。

## 输入

四行棋盘，然后三行模板（`1` 表示翻转，`0` 表示不翻）。

## 输出

最少步数，或 `Impossible`。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
WWWW
WBBW
WBWW
WWWW
101
010
101
```

输出：

```
Impossible
```

## 解法

用位掩码表示时，一步就是把棋盘与该格子的固定掩码做异或。异或可交换，同一格走两次会相互抵消，所以任何走法都等价于一个格子集合，每个格子用一次。集合只有
`2^16` 个：用去掉最低格子的集合推出每个集合的总翻转，`flips[s] = flips[s − lowest] ^ move[lowest]`，再取翻转结果等于棋盘（全白）或棋盘全部取反（全黑）的最小集合。`O(2^16)`。

注意事项：

- 两种颜色都是合法目标，所以两个目标都要试；
- 模板以所选格子为中心并在边缘被截断，所以同一模板在边界附近翻转的棋子更少；
- 有些模板永远碰不到某些格子（例如只有一个角的模板永远到不了最后一行和最后一列），这使许多棋盘无解。

答案经过验证：与一个按步对全部 `2^16` 个棋盘状态做广度优先搜索的程序比对，覆盖所有测试和 40 个随机局面。

## 各语言说明

- 各语言都遍历同样的 `2^16` 个集合；最低位和 1 的个数用内置函数求，Python 用 `(s & -s).bit_length()` 和
  `bin(s).count("1")`。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1122_bitmask.cpp](1122_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^16) | AC | 0.015 s | 428 KB |
| [1122_bitmask.go](1122_bitmask.go) | Go 1.14 x64 | bitmask | O(2^16) | AC | 0.031 s | 1608 KB |
| [1122_bitmask.java](1122_bitmask.java) | Java 1.8 | bitmask | O(2^16) | AC | 0.109 s | 1852 KB |
| [1122_bitmask.py](1122_bitmask.py) | Python 3.12 x64 | bitmask | O(2^16) | AC | 0.109 s | 3192 KB |
| [1122_bitmask.rs](1122_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^16) | AC | 0.031 s | 736 KB |
