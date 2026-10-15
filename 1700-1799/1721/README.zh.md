# 1721. 硬币的两面

[Timus 1721](https://acm.timus.ru/problem.aspx?space=1&num=1721) · 难度 581 · matching

原题作者 Pavel Atnashev，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每道题由两个人准备：一人写题面，另一人准备测试数据，两人的等级恰好相差 2。
每个人要么写题面，要么准备测试，要么两者都会，并且最多参与一道题。求最多能准备多少道题以及每道题由谁准备。

## 输入

n（2 ≤ n ≤ 1000），然后 n 行：不超过 20 个拉丁字母的名字、专长 `statements`、`testdata` 或 `anything`，
以及等级——3 到 1000 的整数。所有名字互不相同。

## 输出

最多的题目数，然后对每道题输出写题面者的名字和准备测试者的名字。任何最优方案都可以。

## 样例

### 样例 1

输入：

```
7
Poll anything 8
Tejat statements 6
Mebsuta testdata 6
Propus testdata 4
Alzir anything 7
Mekbuda anything 3
Dirah testdata 9
```

输出：

```
3
Poll Mebsuta
Tejat Propus
Alzir Dirah
```

## 解法

如果两人的等级恰好相差 2，且其中一人能写题面、另一人能准备测试，就在他们之间连一条边。
一个方案就是一组没有公共人的边，所以问题就是求最大匹配。

这个图是二分图。沿着一条边，⌊rank/2⌋ 恰好变化 1，所以它的奇偶性翻转：⌊rank/2⌋ 为偶数的人构成一侧，为奇数的构成另一侧。
建图与 Hopcroft–Karp 算法共需 `O(n² + E √n)`，当 500 人等级为 3、500 人等级为 5 时 E 可达 250 000。
每一对中选择合法的角色分配；两人两种工作都会时任选。

样例中 Poll (8) 和 Mebsuta (6)、Tejat (6) 和 Propus (4)、Alzir (7) 和 Dirah (9) 组成三道题。
Mekbuda (3) 没有等级为 1 或 5 的人，因此落单。

注意事项：

- 等级必须恰好相差 2，而不是至多相差 2；
- 两个 `statements` 专家或两个 `testdata` 专家不能组成一道题，即使等级相差 2；
- 二分划分让 Hopcroft–Karp 能寻找增广路，无需处理奇环；
- Python 解答用显式栈走增广路，因为一条路径可能经过几百个人。

检查程序将题目数与最优值比较，检查每一对都能准备题目，且没有人参与两次。
在 300 个最多 8 人的随机数据上，数目与穷举所有方案一致；在 60 个 1000 人的随机数据上，与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1721_matching.cpp](1721_matching.cpp) | G++ 13.2 x64 | matching | O(n² + E √n) | AC | 0.015 s | 924 KB |
| [1721_matching.go](1721_matching.go) | Go 1.14 x64 | matching | O(n² + E √n) | AC | 0.031 s | 4476 KB |
| [1721_matching.java](1721_matching.java) | Java 1.8 | matching | O(n² + E √n) | AC | 0.156 s | 6132 KB |
| [1721_matching.py](1721_matching.py) | Python 3.12 x64 | matching | O(n² + E √n) | AC | 0.171 s | 2840 KB |
| [1721_matching.rs](1721_matching.rs) | Rust 1.75 x64 | matching | O(n² + E √n) | AC | 0.031 s | 1800 KB |
