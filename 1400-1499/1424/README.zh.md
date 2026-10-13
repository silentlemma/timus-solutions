# 1424. 小巴

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · 难度 697 · greedy

原题作者 Dmitry Kovalioff、Ilya Grebnov 与 Nikita Rybak（创意来自 Sergey Sofronov），出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一辆有 M 个座位（M ≤ 1000）的小巴从 1 号站开到 N 号站（N ≤ 100 000），只跑一
趟。K 个人（K ≤ 50 000）想乘车，第 i 人从 S[i] 站到 F[i] 站，不论远近都付 P。司
机可以拒绝任何人。输出最大利润以及应搭载的人的编号，顺序任意；任何最优方案都可
以。

时间限制：1 秒。内存限制：64 MB。

## 输入

N、M、K 和 P，然后 K 行 S F。

## 输出

利润，然后是要搭载的人。

## 样例

### 样例 1

输入:

```
6 2 6 9
1 4
2 6
1 5
2 3
4 6
3 6
```

输出:

```
36
1 5 6 4
```

## 解法

每位乘客付钱相同，所以要在车上同时不超过 M 人的前提下尽量多载人；在某站空出的座
位可以在同一站被占用。按顺序经过各站。在每一站，行程在此结束的人下车，在此等候
的人全部上车，只要车上多于 M 人，就拒绝去得最远的那位，当作从未搭载。

拒绝最远的乘客是安全的：在某站之后车上的人中，任何最优方案都至少要放弃超出的那
么多人；把被保留的长行程换成被拒绝的短行程，绝不会让后面的站更拥挤，因为短行程
先结束。按终点站排序的大顶堆找出最远的乘客，按终点站统计的已搭载人数维护车上人
数。`O(N + K log K)`。

注意事项：

- 行程是半开区间：在某站下车的人把座位让给在该站上车的人（测试 05）；
- 没有人时答案是 0 和一个空列表（测试 02）；
- 多人可能想走完全相同的行程（测试 04、gen3）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.093 s | 4752 KB |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12376 KB |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.187 s | 13932 KB |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.218 s | 30352 KB |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.031 s | 10376 KB |
