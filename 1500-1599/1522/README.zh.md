# 1522. 工厂

[Timus 1522](https://acm.timus.ru/problem.aspx?space=1&num=1522) · 难度 1765 · greedy

原题作者 Dmitry Gozman，出自 2007 年 1 月彼得罗扎沃茨克冬季集训的 Dmitry Gozman Contest 1。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N 个玩具（1 ≤ N ≤ 10⁵）依次经过机器 A、B、C，分别耗时 ai、bi、ci（均在 1 到 10⁶ 之
间）；每台机器一次只处理一个玩具，玩具的顺序可以任选，但在所有机器上相同。机器 B 很
快：max bi ≤ min ai 或 max bi ≤ min ci。求完成所有玩具的最短时间和达到它的顺序。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后是每个玩具的 ai、bi、ci。

## 输出

最短完成时间，然后是一个最优的玩具顺序。任何最优顺序都可以。

## 样例

### 样例 1

输入:

```
5
3 1 6
1 1 2
5 2 5
7 1 4
10 2 8
```

输出:

```
33
2 1 3 5 4
```

### 样例 2

输入:

```
1
5 4 7
```

输出:

```
16
1
```

## 解法

当 B 被这样支配时，对耗时为 ai + bi 和 bi + ci 的两台虚拟机器用 Johnson 规则求最优
顺序：先放 ai + bi < bi + ci 的玩具，按 ai + bi 递增，再放其余玩具，按 bi + ci 递减。
在 A、B、C 上模拟求时间：机器在自身空闲且玩具上一道工序已完成时开始处理。`O(N log N)`。

注意事项：

- 这个规则依赖于对 B 的条件；一般的三机问题要难得多；
- B 也可能被 C 而不是 A 支配（测试 04、gen2）；
- 两个合计时间相等的玩具放在哪一组都可以（测试 03、05）；
- 总时间可达 100002000000，超出 32 位（gen3）；
- 最优顺序可能有很多，所以测试使用检查程序（所有测试）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1522_greedy.cpp](1522_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.187 s | 4564 KB |
| [1522_greedy.go](1522_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.062 s | 9752 KB |
| [1522_greedy.java](1522_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.281 s | 10816 KB |
| [1522_greedy.py](1522_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.343 s | 50996 KB |
| [1522_greedy.rs](1522_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.078 s | 11432 KB |
