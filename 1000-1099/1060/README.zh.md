# 1060. 使 4 × 4 棋盘同色的最少翻转次数

[Timus 1060](https://acm.timus.ru/problem.aspx?space=1&num=1060) · 难度 378 · bruteforce, bitmask

原题出自 2000–2001 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

4 × 4 的棋盘上放着棋子，朝上的一面为黑（`b`）或白（`w`）。一步操作选择一个格子，翻转该格的棋子以及它上下左右
存在的相邻棋子。求使所有棋子朝上颜色相同（任一颜色）的最少步数；若已经相同输出 `0`；若做不到输出 `Impossible`。

时间限制：2 秒。内存限制：64 MB。

## 输入

四行，每行四个 `b` 或 `w` 字符。

## 输出

最少步数，或 `Impossible`。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
bwbw
wwww
bbwb
bwwb
```

输出：

```
Impossible
```

### 样例 2

输入：

```
bwwb
bbwb
bwwb
bwww
```

输出：

```
4
```

## 题解

把棋盘写成 16 位；在一个格子上操作就是把棋盘与一个固定的、最多五位的掩码异或。异或满足交换律，同一掩码用两次
会抵消，所以操作顺序无关紧要，任何格子都不需要操作两次：一个解就是一个格子集合。

共有 `2^16 = 65536` 个集合。对每个集合，把其中各格的掩码异或到棋盘上，记录结果为全 0 或全 1 的最小集合。
`O(2^16 · 16)`。

65536 个局面中只有 4096 个可解，而且都不超过六步（用于核对测试的、遍历所有局面的广度优先搜索表明了这一点）。

注意事项：

- 全白和全黑都是目标；
- 边上和角上的格子翻转的棋子更少；
- 已经同色的局面需要 0 步。

## 优化解法

Go 对两种目标颜色分别枚举首行的 16 种按压掩码。某行剩余的每个不同色格都强制按压正下方的格子，因此其余行被唯一确定。统计按压位数，只有最后一行之后不再需要按压时才接受该方案。棋盘每行仅占一个字节。Python 把 16 格分成两半，枚举各半按压子集的 XOR 效果，并为每种效果保留最少按压次数。对于每个单色目标和左半效果，查表即可找到所需右半效果。C = 16 时，时间和空间均为 O(2^(C/2))。Go 使用小型固定字节缓冲区并直接访问标准句柄，重试中断调用并完成部分写入。

已通过评测的基础实现 [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp), [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java), [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

以下说明针对基础实现。

- **C++**、**Go**、**Java**、**Rust**：遍历全部 65536 个集合。
- **Python**：逐个格子构造所有集合对应的棋盘，每次把列表加倍（新格子把自己的掩码异或到已有的每个棋盘上），
  从而避免对每个集合的 16 位做 Python 循环。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 124 KB | 11278793 |
| [1060_bruteforce_bitmask.go](1060_bruteforce_bitmask.go) | Go 1.14 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.031 s | 1068 KB | 11278795 |
| [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java) \* | Java 1.8 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 1580 KB | 11278797 |
| [1060_bruteforce_bitmask.py](1060_bruteforce_bitmask.py) | Python 3.12 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 4840 KB | 11278796 |
| [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) | Rust 1.75 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 232 KB | 11278798 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1060_bitmask.go](1060_bitmask.go) \* | Go 1.14 x64 | bitmask | O(H·2^W), H = W = 4 | AC | 0.015 s | 284 KB | 11311214 |
| [1060_bitmask_meet_in_middle.py](1060_bitmask_meet_in_middle.py) | Python 3.12 x64 | bitmask, meet_in_middle | O(2^(C/2)), C = 16 | AC | 0.078 s | 624 KB | 11310331 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
