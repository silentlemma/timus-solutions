# 1795. 商店里的丈夫们

[Timus 1795](https://acm.timus.ru/problem.aspx?space=1&num=1795) · 难度 253 · simulation

原题作者 Andrew Gein，出自 2010 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

商店有 m 种商品，各有给定的数量；Mark 前面排着 n 个丈夫，每人要买一定数量的某一种商品。在柜台前（花一分钟），够的话丈夫就买下，
商品没有或卖完了就离开。若有但不够，他让下一个人先上前，自己站在第二位给家里打电话；被告知买下剩余的之后，他再次来到柜台：
数量没变就全部买下，什么都没剩就离开，否则再让一个人上前并再次打电话。Mark 到达柜台前要过多少分钟？

## 输入

m（1 ≤ m ≤ 1000）行 "amount of name"，然后 n（1 ≤ n ≤ 1000）行同样格式的丈夫需求，从队首开始。数量在 1 到 1000 之间，
名称最多 20 个小写字母，丈夫可能想买商店不卖的商品。

## 输出

分钟数。

## 评测方式

按词元比较输出，多余空白不影响结果。

## 样例

### 样例 1

输入：

```
3
2 of sweets
4 of milk
1 of sausage
4
2 of milk
3 of sweets
3 of milk
1 of cheese
```

输出：

```
6
```

## 解法

模拟队列。每次到柜台就是一分钟。为每个丈夫记录上次被告知的数量。需要打电话的丈夫被放回队列中下一个人的后面；
如果在 Mark 之前已没有别人，下一个就是 Mark，计数到此结束。他回来时把数量和上次被告知的比较：相同就全部买下，为零就离开，
否则再打一次电话。队列中最多 1000 个丈夫，每次打电话都把打电话的人往后移一位，所以模拟很快。`O(n²)`。

样例中第一个丈夫买走 4 份牛奶中的 2 份。第二个发现只有 2 份糖果，退到第三个人后面；第三个发现只有 2 份牛奶，也退后。
然后两人回来时数量都没变，于是买下，最后一个丈夫找不到奶酪：Mark 之前共 6 次到柜台。

注意事项：

- 回来时数量没变的丈夫会全部买下，即使比他想要的少；
- 排在最后的丈夫需要打电话时会让 Mark 先上前，所以 Mark 在这一分钟之后就到柜台了；
- 每次到柜台都算一分钟，包括以打电话结束的那一次。

在 300 个随机情形上（其中包括只有一种商品、少数要买下全部的人在每次小额购买后都再打电话的情形），答案与一个独立的已通过实现一致。

## 优化解法

仍模拟柜台访问，但只在读入时把商品名映射为整数编号。顾客队列用数组和头下标表示，与下一位交换可原地进行，无需插入删除后移动整个队列。不存在的商品使用零库存项。所有访问及库存更新不变，消除重复字符串查找、队列复制和全输入保存。

- `1795_simulation_optimized.cpp`: 0.031 s / 272 KB; 基础版 `1795_simulation.cpp`: 0.031 s / 552 KB; 相对基础版的变化: 时间 -0.0%, 内存 -50.7%.
- `1795_simulation_optimized.go`: 0.031 s / 1132 KB; 基础版 `1795_simulation.go`: 0.046 s / 6376 KB; 相对基础版的变化: 时间 -32.6%, 内存 -82.2%.
- `1795_simulation_optimized.java`: 0.093 s / 1076 KB; 基础版 `1795_simulation.java`: 0.125 s / 4688 KB; 相对基础版的变化: 时间 -25.6%, 内存 -77.0%.
- `1795_simulation_optimized.py`: 0.078 s / 612 KB; 基础版 `1795_simulation.py`: 0.078 s / 1100 KB; 相对基础版的变化: 时间 -0.0%, 内存 -44.4%.
- `1795_simulation_optimized.rs`: 0.031 s / 508 KB; 基础版 `1795_simulation.rs`: 0.062 s / 632 KB; 相对基础版的变化: 时间 -50.0%, 内存 -19.6%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1795_simulation.cpp`; 覆盖实现 `1795_simulation_optimized.cpp`; 时间/内存名次 47/1, 其他作者记录 53/53.

- Go: 优先教学基础版 `1795_simulation.go`; 覆盖实现 `1795_simulation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1795_simulation.java`; 覆盖实现 `1795_simulation.java`; 时间/内存名次 1/1, 其他作者记录 1/1.

- Python/PyPy: 优先教学基础版 `1795_simulation.py`; 覆盖实现 `1795_simulation.py`; 时间/内存名次 1/1, 其他作者记录 6/6.

- Rust: 优先教学基础版 `1795_simulation.rs`; 覆盖实现 `1795_simulation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1795_simulation.cpp](1795_simulation.cpp) | G++ 13.2 x64 | simulation | O(n^2) | AC | 0.031 s | 552 KB | 11308937 |
| [1795_simulation.go](1795_simulation.go) | Go 1.14 x64 | simulation | O(n^2) | AC | 0.046 s | 6376 KB | 11289883 |
| [1795_simulation.java](1795_simulation.java) | Java 1.8 | simulation | O(n^2) | AC | 0.125 s | 4688 KB | 11308939 |
| [1795_simulation.py](1795_simulation.py) | Python 3.12 x64 | simulation | O(n^2) | AC | 0.078 s | 1100 KB | 11308940 |
| [1795_simulation.rs](1795_simulation.rs) | Rust 1.75 x64 | simulation | O(n^2) | AC | 0.062 s | 632 KB | 11308942 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1795_simulation_optimized.cpp](1795_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 272 KB | 11308816 |
| [1795_simulation_optimized.go](1795_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 1132 KB | 11308817 |
| [1795_simulation_optimized.java](1795_simulation_optimized.java) | Java 1.8 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.093 s | 1076 KB | 11308818 |
| [1795_simulation_optimized.py](1795_simulation_optimized.py) | Python 3.12 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.078 s | 612 KB | 11308814 |
| [1795_simulation_optimized.rs](1795_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N^2+(M+N) log(M+2)) | AC | 0.031 s | 508 KB | 11308820 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
