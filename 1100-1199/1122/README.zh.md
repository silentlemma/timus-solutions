# 1122. 把 4 × 4 棋盘变成单一颜色的最少步数

[Timus 1122](https://acm.timus.ru/problem.aspx?space=1&num=1122) · 难度 251 · bitmask

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

## 优化解法

把 16 个操作分成两个各含八个操作的集合。用格雷码顺序枚举每一半，只改变一个操作即可更新 XOR 效果。对左半每种效果，只保存最少操作数。右半效果为 `r`、目标为 `t` 时，在左半查找 `t XOR r`，并分别尝试两种最终颜色。任意操作子集都有唯一的左右划分，即使操作效果线性相关，丢弃更贵的同效果左半表示也不会丢失最优解。这样只枚举两个 `2^8` 列表，而非 `2^16` 个子集。使用哈希表时，期望时间和空间为 `O(2^8)`；哈希表最坏时间可能是记录数的平方。

五种独立实现相对未改动的 Accepted 基础版本均节省至少 30% 内存：C++ 57.0%、Go 31.1%、Java 73.9%、Python 76.1%、Rust 43.5%。时间相同或更低，一个计时刻度的差别不视为可靠加速。在 2026 年 11 月 1 日的快照中，C++、Java、Python 达到排名目标；筛选后的 Go 和 Rust 样本没有其他作者，无法据此证明竞争排名。基础枚举和折半搜索还通过独立状态空间算法交叉验证。

## 各语言说明

五种基础实现枚举全部 `2^16` 个集合，Python 使用 bit_length 和位计数。五种新实现使用哈希表，分别枚举两个八操作集合。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1122_bitmask.cpp](1122_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^16) | AC | 0.015 s | 428 KB | 11279286 |
| [1122_bitmask.go](1122_bitmask.go) | Go 1.14 x64 | bitmask | O(2^16) | AC | 0.031 s | 1608 KB | 11279289 |
| [1122_bitmask.java](1122_bitmask.java) | Java 1.8 | bitmask | O(2^16) | AC | 0.109 s | 1852 KB | 11279292 |
| [1122_bitmask.py](1122_bitmask.py) | Python 3.12 x64 | bitmask | O(2^16) | AC | 0.109 s | 3192 KB | 11279291 |
| [1122_bitmask.rs](1122_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^16) | AC | 0.031 s | 736 KB | 11279293 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1122_bitmask_meet_in_middle.cpp](1122_bitmask_meet_in_middle.cpp) | G++ 13.2 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.015 s | 184 KB | 11308016 |
| [1122_bitmask_meet_in_middle.go](1122_bitmask_meet_in_middle.go) | Go 1.14 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.031 s | 1108 KB | 11308019 |
| [1122_bitmask_meet_in_middle.java](1122_bitmask_meet_in_middle.java) | Java 1.8 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.093 s | 484 KB | 11308020 |
| [1122_bitmask_meet_in_middle.py](1122_bitmask_meet_in_middle.py) | Python 3.12 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.078 s | 764 KB | 11308012 |
| [1122_bitmask_meet_in_middle.rs](1122_bitmask_meet_in_middle.rs) | Rust 1.75 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.015 s | 416 KB | 11308021 |
