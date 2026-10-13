# 1439. 与那个人的对决

[Timus 1439](https://acm.timus.ru/problem.aspx?space=1&num=1439) · 难度 428 · binary_search

原题作者 Alexander Klepinin 和 Stanislav Vasiliev，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

魔法部的房间编号为 1, 2, …, N（1 ≤ N ≤ 10⁹），编号始终连续：一个房间被摧毁时，
所有编号更大的房间编号都减一。按顺序给出 M ≤ 10⁵ 个事件，每个是 "D x"（当前编号
为 x 的房间被摧毁）或 "L x"（哈利看着当前编号为 x 的门）。最多摧毁 10⁴ 个房间。
对每个 "L" 事件，输出该房间最初的编号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 M 个事件。

## 输出

最初的编号，每行一个。

## 样例

### 样例 1

输入:

```
20 7
L 5
D 5
L 4
L 5
D 5
L 4
L 5
```

输出:

```
5
4
6
4
7
```

## 解法

把被摧毁房间的原编号存入有序数组 g。当前编号为 x 的房间，原编号为 x + k，其中 k
是在它下面被摧毁的房间数。沿数组往上走，房间 g[j] 在它下面当且仅当
g[j] ≤ x + j，即 g[j] − j ≤ x；由于 g 中的编号互不相同，g[j] − j 不减，所以在它
下面的房间构成一个前缀，其长度 k 用二分查找求出。

对 "L" 输出 x + k。对 "D"，新的原编号 x + k 恰好放在数组的位置 k：之前的都更小，
之后的都更大，所以插入后数组仍然有序。设摧毁了 D 个房间，复杂度
`O(M log D + D²)`，每次插入最多移动 10⁴ 个数。

注意事项：

- 反复摧毁同一个门牌号，每次都会藏起一个新房间（测试 03、07、gen3）；
- 编号可达十亿，无法为每个房间开数组（测试 05、gen1）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1439_binary_search.cpp](1439_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D^2) | AC | 0.156 s | 424 KB |
| [1439_binary_search.go](1439_binary_search.go) | Go 1.14 x64 | binary_search | O(M log D + D^2) | AC | 0.171 s | 5708 KB |
| [1439_binary_search.java](1439_binary_search.java) | Java 1.8 | binary_search | O(M log D + D^2) | AC | 0.171 s | 10132 KB |
| [1439_binary_search.py](1439_binary_search.py) | Python 3.12 x64 | binary_search | O(M log D + D^2) | AC | 0.421 s | 21004 KB |
| [1439_binary_search.rs](1439_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log D + D^2) | AC | 0.031 s | 4664 KB |
