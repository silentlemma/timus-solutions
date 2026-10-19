# 1943. 五张牌的获胜前缀

[Timus 1943](https://acm.timus.ru/problem.aspx?space=1&num=1943) · difficulty 906 · bruteforce, constructive

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

双方初始牌堆各为1..n的排列。每轮同时取两队首；相同则两张都弃掉，
否则较大者获两张并按较小在前、较大在后的顺序放到获胜方队尾。
牌堆空者输，同时空为平局。已知对手初始顺序，选择自己的排列
使之实际获胜，或判断不可能。平局或无限重复不算胜。
时限1秒，内存64 MB。

## 输入

n满足2≤n≤500，随后给对手从顶到底的1..n排列。每方初始每种
牌恰有一张。

## 输出

无解仅输出NO；否则首行YES，第二行任意获胜排列，从顶到底。

## 评测方式

检查器用输出的牌序完整重放整局游戏，接受任何真正获胜的牌序。根据下面的引理，五张及以上的牌时 `NO` 永远不正确。

## 样例

```
4
2 3 4 1
```

```
YES
2 4 1 3
```

## 解法

取对手前m=min(n,5)张牌，枚举其排列，精确模拟每个m张牌游戏。
两队列状态重复即为循环；取第一个获胜排列。n≤5时已经枚举
所有可能自己的牌堆，因此无胜利时NO正确。

关键引理：五张不同点数的牌的任何顺序都有获胜的应对。只有点数的大小关系重要，所以只需考虑 1 到 5，把全部 120² = 14 400 对顺序都模拟一遍即可验证该引理。下面的短脚本完成这一验证，并顺带检查更少的牌：

```python
from collections import deque
from itertools import permutations

def game(a, b):
    a, b = deque(a), deque(b)
    seen, steps = set(), 0
    while a and b:
        state = tuple(a), tuple(b)
        if state in seen:
            return False, steps
        seen.add(state)
        x, y = a.popleft(), b.popleft()
        steps += 1
        if x > y:
            a.extend((y, x))
        elif y > x:
            b.extend((x, y))
    return bool(a), steps

for size in range(2, 6):
    orders = list(permutations(range(1, size + 1)))
    possible, longest = 0, 0
    for opponent in orders:
        results = [game(own, opponent) for own in orders]
        possible += any(won for won, _ in results)
        longest = max(longest, max(steps for _, steps in results))
    print(size, len(orders), possible, longest)
```

| Cards | Opponent orders | Orders with a winning reply | Longest game |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 4 |
| 3 | 6 | 3 | 7 |
| 4 | 24 | 22 | 16 |
| 5 | 120 | 120 | 49 |

总牌数≤10，所以状态有限；重复状态不可能之后获胜。穷举终止，
120种对手顺序各有明确获胜见证。测试含全部6输入及获胜输出，
也含更小牌数的全部13顺序，构成可复现有限证书。五是最小通用
大小，因为四张牌有两种无解顺序。

n>5时，仅重排自己的前五张，其他位置完全复制对手。前n轮未使用
的原始牌总在捕获牌之前，所以两方不能提前空。后n−5个相同的
原始牌对直接消失。第n轮后状态等于五张牌局第5轮后状态，
之后逐轮相同，因此局部胜利变成完整胜利。局部t轮结束，则完整
需要n+t−5≤n+44轮。引理保证n≥5均成功，小规模穷举证明完整性。

时间、空间O(n)，另有最多5!个候选的固定局部搜索。完整局部域
证明每局≤49轮且≤10张活跃牌。这是验证的界，不是程序轮数截断。
该域首胜最多需要68次尝试，代码仍正常枚举直至成功或全部失败。

获牌顺序是小、大；相等两张都消失，同时空为平局。不能将存活
或有限轮数内未输当作获胜。五张不等于五轮。未动牌需放在与
对手相同原始位置，保证在获牌到队首前抵消。对某些有序牌堆的
观察不能代替完整有限引理。

## 各语言说明

C++用next_permutation，Python用itertools.permutations；Go、Java、
Rust实现通常的枢轴、后继及后缀翻转。均保存精确队列状态判环。
Go用队首下标，Java和Rust用双端队列。尾部直接复制，只需标准库，
没有预存答案表。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1943_bruteforce_constructive.cpp](1943_bruteforce_constructive.cpp) | G++ 13.2 x64 | bruteforce, constructive | O(n) | AC | 0.015 s | 520 KB |
| [1943_bruteforce_constructive.go](1943_bruteforce_constructive.go) | Go 1.14 x64 | bruteforce, constructive | O(n) | AC | 0.031 s | 1236 KB |
| [1943_bruteforce_constructive.java](1943_bruteforce_constructive.java) | Java 1.8 | bruteforce, constructive | O(n) | AC | 0.109 s | 848 KB |
| [1943_bruteforce_constructive.py](1943_bruteforce_constructive.py) | Python 3.12 x64 | bruteforce, constructive | O(n) | AC | 0.062 s | 600 KB |
| [1943_bruteforce_constructive.rs](1943_bruteforce_constructive.rs) | Rust 1.75 x64 | bruteforce, constructive | O(n) | AC | 0.046 s | 468 KB |
