# 1871. 地震波

[Timus 1871](https://acm.timus.ru/problem.aspx?space=1&num=1871) · 难度 623 · dijkstra

原题作者 Dmitry Ivankov，出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每个 Twitter 用户都有一份关注者列表，关注者能看到该用户的所有推文。关注者可以转推：在消息前加上字符串 "RT @nick: "，其中 nick 是被转发的推文或转推的作者。长度超过 140 个字符的消息根本不会发出。第一个用户发了一条关于地震的推文；谁会得知这件事？

## 输入

n（2 ≤ n ≤ 100），然后是 n 行 "名字 k 关注者₁ … 关注者ₖ"，名字互不相同，由 1 到 30 个拉丁字母组成；最后是推文：一个非空行，至多 140 个字符，ASCII 码在 32 到 127 之间。

## 输出

得知地震的用户数，然后以任意顺序每行输出一个他们的名字。

## 样例

### 样例 1

输入：

```
5
Miyako 1 Sae
Yuno 2 Miyako Sae
Nazuna 1 Nori
Sae 1 Yuno
Nori 1 Nazuna
Hidamari is going to collapse!!!
```

输出：

```
3
Miyako
Sae
Yuno
```

## 解法

发送一条不超过 140 个字符的消息的用户会把它展示给所有关注者。转推用户 u 的消息会多出 6 + |u| 个字符：前缀 "RT @: " 和名字。越短总是越好，所以记录每个用户可能发送的最短消息。这就是从第一个用户出发的最短路，起点值为推文长度，从 u 出发的每条边权为 6 + |u|。在 n ≤ 100 个用户上用 Dijkstra 算法求出它，最短消息超过 140 的用户无法发送它。答案是能够发送消息的用户及其所有关注者：即使关注者自己的转推会太长，关注者也能看到消息。`O(n²)`，C++ 因查询 `map` 而为 `O(n² log n)`。

样例中 Miyako 的推文有 32 个字符。Sae 看到后转推成 44 个字符，Yuno 看到后转推成 53 个字符，又传回 Miyako 和 Sae。Nazuna 和 Nori 始终不知道。

注意事项：

- 转推次数最少并不意味着消息最短：短路径上的长名字可能输给几个短名字；
- 推文可能以空格开头或结尾，空格也计入长度，所以必须整行读取；
- 恰好 140 个字符的消息仍然会发出；
- 不能转推的用户，只要其关注的人发送消息，仍然会得知消息。

在 180 个随机网络上（包括转推次数较少的路径反而给出较长消息的情况），用户集合与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1871_dijkstra.cpp](1871_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(n^2 log n) | AC | 0.015 s | 684 KB |
| [1871_dijkstra.go](1871_dijkstra.go) | Go 1.14 x64 | dijkstra | O(n^2) | AC | 0.031 s | 1556 KB |
| [1871_dijkstra.java](1871_dijkstra.java) | Java 1.8 | dijkstra | O(n^2) | AC | 0.125 s | 1616 KB |
| [1871_dijkstra.py](1871_dijkstra.py) | Python 3.12 x64 | dijkstra | O(n^2) | AC | 0.078 s | 1228 KB |
| [1871_dijkstra.rs](1871_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(n^2) | AC | 0.046 s | 564 KB |
