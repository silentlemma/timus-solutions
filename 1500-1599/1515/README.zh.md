# 1515. 财政改革

[Timus 1515](https://acm.timus.ru/problem.aspx?space=1&num=1515) · 难度 215 · greedy

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 种面值（1 ≤ N ≤ 100）的钞票各有一张，按递增顺序给出，每种在 1 到 10⁶ 之间。求不能
由其中某些钞票相加得到的最小正整数；单独一张钞票也算一种和。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是按递增顺序的 N 个面值。

## 输出

任何一组钞票都凑不出的最小数。

## 样例

### 样例 1

输入:

```
5
1 2 4 9 100
```

输出:

```
8
```

## 解法

按递增顺序处理面值，维护 reach：1 到 reach 的每个数都能凑出的最大数。如果下一个面
值 d 不超过 reach + 1，那么 reach + d 以内的每个数也都能凑出：不超过 reach 的照旧，
更大的用 d 加上一个不超过 reach 的和。如果 d > reach + 1，reach + 1 就凑不出：已处
理的面值总和只有 reach，而其他每个面值本身就大于 reach + 1。答案是 reach + 1。
`O(N)`。

注意事项：

- 没有面值为 1 的钞票时答案是 1（测试 03、06）；
- 答案可以比所有面值都大，最大为全部面值之和加一（测试 04、05、gen2）；
- 第一个空缺出现时就可以停止，后面的面值都填不上它：有 1 和 3 时凑不出 2（测试
  07）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1515_greedy.cpp](1515_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 196 KB |
| [1515_greedy.go](1515_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1096 KB |
| [1515_greedy.java](1515_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.109 s | 500 KB |
| [1515_greedy.py](1515_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.078 s | 428 KB |
| [1515_greedy.rs](1515_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 228 KB |
