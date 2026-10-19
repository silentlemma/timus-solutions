# 1934. 最短路线中的最低风险

[Timus 1934](https://acm.timus.ru/problem.aspx?space=1&num=1934) · difficulty 359 · shortest_paths, probability

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在简单无向图中寻找从s到t的路线。边的整数百分数p表示该边独立
发生故障的概率p/100。首先最小化经过的顶点数，包括起点和终点；
然后最小化途中至少发生一次故障的概率。也允许风险与最优值相差
不超过10⁻⁶的最短路线。限制为1秒、64MB。

## 输入

先给出n,m，2≤n≤100000，1≤m≤100000；再给出不同的s,t，编号
在1..n。随后m行各有a,b,p，1≤a,b≤n、a≠b、0≤p≤99。
每个无序顶点对至多一条边。所要求的输出描述一条存在的s到t路线。

## 输出

第一行输出k及所选路线的故障概率，概率用0到1之间的数表示，
绝对误差至多10⁻⁶。第二行按路线顺序输出k个顶点编号。k必须
最小；所选路线的真实风险最多比该长度的最低风险高10⁻⁶。
任意满足要求的路线均可。

## 评测方式

检查器确认路线存在且顶点数最少，并且其失败概率与输出的概率都与最优值相差不超过 10⁻⁶。任何这样的路线都被接受。

## 样例

```
4 4
1 3
1 2 50
2 3 50
1 4 10
4 3 10
```

```
3 0.19
1 4 3
```

## 解法

令q=1−p/100为一条边上的成功概率。整条路线成功概率为q的
乘积，风险为1减去该乘积。由于q>0，可定义可加代价c=−log(q)。
最小化代价之和就等价于最大化成功概率的乘积。

从s执行普通FIFO广度优先搜索。每个顶点保存距离、该距离下
最小对数代价和对应前驱。处理u→v时，尚未发现的v获得距离
distance[u]+1；仅当distance[v]=distance[u]+1时尝试更新代价。
同层边和回边不能引入更长路线。FIFO保证一个顶点出队前，
前一层的所有顶点都已处理。按层归纳，所有最短前驱均已提供
候选方案，因此出队时保存的代价最优。可以在t出队时停止，
但不能在首次发现t时停止。

从t沿前驱回溯并反转即可得到路线。总代价为C时，风险计算为
−expm1(−C)。log1p和expm1提高接近零时的精度，对数也避免了
长路线直接乘法的下溢。双精度和小数点后十二位足以满足10⁻⁶
容差。边代价表仅有100项。

时间O(n+m)，空间O(n+m)，包括邻接表、BFS状态、路线和输入
输出缓冲。无需优先队列，也无需递归。

s,t在边记录之前。顶点数优先于概率：更长的零风险路线不能
代替更短的危险路线。不能直接相加百分数；应乘成功概率或加
负对数。首次发现t时尚未得到全部候选。不同合法路线不应按
字节比较。零风险边和最终四舍五入为1的风险都是合法情况。

## 各语言说明

以零起始编号将边编码为100·相邻顶点+p，最大9,999,999，可用
32位整数。C++、Go和Rust使用编码边的动态数组。Java使用
原生head/next/edge数组和缓冲整数读取器。Python在BFS前释放
输入记号迭代器，并以有类型数组保存距离、前驱和代价。所有
实现均迭代恢复路径并缓冲输出。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1934_shortest_paths.cpp](1934_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 7288 KB |
| [1934_shortest_paths.go](1934_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 15636 KB |
| [1934_shortest_paths.java](1934_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 9180 KB |
| [1934_shortest_paths.py](1934_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.406 s | 33792 KB |
| [1934_shortest_paths.rs](1934_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 14136 KB |
