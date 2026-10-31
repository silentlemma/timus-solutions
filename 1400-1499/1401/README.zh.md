# 1401. 玩家

[Timus 1401](https://acm.timus.ru/problem.aspx?space=1&num=1401) · 难度 159 · constructive

原题作者 Alex Samsonov，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

用由三个格子组成的 L 形骨牌铺满去掉一格的 2ⁿ × 2ⁿ 棋盘，1 ≤ n ≤ 9。输出棋盘：
被去掉的格子为 0，其余每格为覆盖它的骨牌编号，编号从 1 到 (4ⁿ − 1) / 3；若无法
铺满则输出 -1。

时间限制：2 秒。内存限制：64 MB。

## 输入

n，然后是被去掉格子的行 x 和列 y，1 ≤ x, y ≤ 2ⁿ；左上角的格子是 (1, 1)。

## 输出

2ⁿ 行，每行 2ⁿ 个数。任何铺法都被接受。

## 样例

### 样例 1

输入:

```
2
1 1
```

输出:

```
0 1 3 3
1 1 4 3
2 4 4 5
2 2 5 5
```

## 解法

总能铺满，方法是对半分。把棋盘分成四个象限，被去掉的格子位于其中一个。在棋
盘中心周围、属于另外三个象限的三个格子上放一块骨牌。这样每个象限都是恰有一
个格子已被占用的 2ⁿ⁻¹ × 2ⁿ⁻¹ 棋盘，即同一个问题，而 1 × 1 的棋盘无需处理。解
答用栈代替递归保存待处理的正方形及其已占用的格子，并按放置顺序给骨牌编号。
`O(4ⁿ)`。

注意事项：

- 答案永远不会是 -1；
- 512 × 512 的棋盘要输出 262 144 个数，所以输出使用缓冲（生成
  测试）。

测试由检查程序判定：要求只有被去掉的格子为 0，且 1 到 (4ⁿ − 1) / 3 的每个数恰
好出现在构成 2 × 2 方块内 L 形的三个格子上。

## 优化解法

优化的 C++ 解法填写一个 512 × 512 的全局 `int` 数组，而不是 `vector` 的
`vector`，并用递归代替方块栈：每次调用放好一个方块的那块骨牌，再进入它的四个子方
块，递归深度至多 n ≤ 9。子方块按相反顺序访问，因此骨牌编号与用栈时相同。格子用
`printf` 逐个输出，而不是先把整个棋盘作为文本收集到 `string` 中：
{1401_constructive_optimized.cpp}。

优化的 Go 解法用 `int32` 格子代替 64 位的 `int` 存放棋盘，因为骨牌编号至多为
(4⁹ − 1) / 3 = 87 381，这使棋盘内存减半；每个数用 `strconv.AppendInt` 格式化到
同一个反复使用的字节切片中，而不是为每个格子创建一个字符串：
{1401_constructive_optimized.go}。

优化的 Java 解法用递归代替为每个方块往栈里压一个 `Square` 对象：每次调用放好一个
方块的那块骨牌，再进入它的四个子方块，递归深度至多 n ≤ 9；子方块按相反顺序访问，
因此骨牌编号与用栈时相同。输入用 `StreamTokenizer` 而不是 `Scanner` 读取，棋盘通
过 `BufferedWriter` 逐行输出，每行复用同一个 `StringBuilder`，而不是先拼出整个输
出：{1401_constructive_optimized.java}。

优化的 Python 解法把每一行存放在由 4 字节无符号格子组成的 `array("I")` 中，它能
容纳至多 (4⁹ − 1) / 3 = 87 381 的骨牌编号，而不是整数对象的列表。它直接递归进入
子方块，深度至多 n ≤ 9，而不是维护一个元组栈；子方块按相反顺序访问，使骨牌编号保
持不变；棋盘逐行输出，而不是拼接成一个字符串：{1401_constructive_optimized.py}。

优化的 Rust 解法用同样的方法构造棋盘，但把数直接写入 `BufWriter`，而不是先把整个
棋盘格式化成一个约 1.5 MB 的 `String`：{1401_constructive_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1401_constructive_optimized.cpp`: 时间降低 -200.00%; 内存降低 +70.00%; 基础版本: `1401_constructive.cpp`.

- `1401_constructive_optimized.go`: 时间降低 +0.00%; 内存降低 +54.86%; 基础版本: `1401_constructive.go`.

- `1401_constructive_optimized.java`: 时间降低 +38.42%; 内存降低 +57.07%; 基础版本: `1401_constructive.java`.

- `1401_constructive_optimized.py`: 时间降低 +16.80%; 内存降低 +83.59%; 基础版本: `1401_constructive.py`.

- `1401_constructive_optimized.rs`: 时间降低 -48.39%; 内存降低 +72.59%; 基础版本: `1401_constructive.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive.cpp](1401_constructive.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 3760 KB | 11286021 |
| [1401_constructive.go](1401_constructive.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 4732 KB | 11286022 |
| [1401_constructive.java](1401_constructive.java) | Java 1.8 | constructive | O(4^n) | AC | 0.203 s | 13044 KB | 11286024 |
| [1401_constructive.py](1401_constructive.py) | Python 3.12 x64 | constructive | O(4^n) | AC | 0.375 s | 10628 KB | 11286023 |
| [1401_constructive.rs](1401_constructive.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.031 s | 4276 KB | 11286025 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive_optimized.cpp](1401_constructive_optimized.cpp) \* | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.093 s | 1128 KB | 11305930 |
| [1401_constructive_optimized.go](1401_constructive_optimized.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 2136 KB | 11305934 |
| [1401_constructive_optimized.java](1401_constructive_optimized.java) \* | Java 1.8 | constructive | O(4^n) | AC | 0.125 s | 5600 KB | 11305935 |
| [1401_constructive_optimized.py](1401_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(4^n) | AC | 0.312 s | 1744 KB | 11307190 |
| [1401_constructive_optimized.rs](1401_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.046 s | 1172 KB | 11307191 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
