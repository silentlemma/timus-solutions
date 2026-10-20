# 2201. 每个 gl 和 hf 都会改变读者运气的聊天服务器

[Timus 2201](https://acm.timus.ru/problem.aspx?space=1&num=2201) · 难度 1875 · parsing, prefix_sums

原题作者 Vadim Barinov，出自 2020 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

游戏服务器处理 N 条聊天命令：加入、退出、在线人数、公共消息、私人消息，以及 admin 专用的两条比较命令。消息由 "gl" 和 "hf" 两种字母对组成，每个在线的读者每读到一个 "gl" 运气乘以 A，每读到一个 "hf" 运气除以 B；作者本人不受影响。输出服务器对每条命令的回复，包括两名玩家运气的比较。时间限制 2.5 秒，内存限制 256 MB。

## 输入

N、M、A 和 B（1 ≤ N ≤ 86400，2 ≤ M ≤ 10，1 ≤ A, B ≤ 10⁹），然后是 N 行日志「[hh:mm:ss] NICK: /command」。

## 输出

服务器对每条命令的回复。

## 样例

### 样例 1

输入：

```
18 4 2 4
[00:00:23] admin: /online
[00:01:02] j0e: /j
[00:01:15] j0e: /s hfhf
[00:01:17] j0e: /q
[00:01:18] admin: /write<j0e> hfhf
[00:03:25] Tea_: /join
[00:04:11] j0e: /join
[00:07:54] Tea_: /j
[00:08:30] admin: /say glgl
[00:08:37] admin: /write<j0e> hfhf
[00:09:00] Tea_: /compare<j0e>
[00:13:41] admin: /c<j0e>-<Tea_>
[00:13:44] j0e: /quit
[00:13:57] admin: /compare<j0e>
[00:27:49] j0e: /j
[00:28:01] j0e: /s hfhf
[00:30:19] admin: /compare<j0e>
[00:30:43] admin: /compare<Tea_>-<j0e>
```

输出：

```
There are 1 players on the server
Successful
j0e: hfhf
Successful
admin (to j0e): hfhf
Successful
Successful
Failed: Tea_ is already on the server
admin: glgl
admin (to j0e): hfhf
Failed: you have no such rights
Tea_ is a lucky guy
Successful
Failed: j0e is not on the server
Successful
j0e: hfhf
j0e is a lucky guy
Their luck is equal
```

## 解法

玩家的运气是 A^g / B^f，其中 g 和 f 是该玩家读到的字母对数，所以只需保存两个计数。公共消息同时到达所有在线玩家，因此计入两个总计，每个玩家保存相对于总计的计数：加入时减去总计，退出时加回总计，公共消息的作者减去自己的字母对。这样对于两个在线玩家，总计相互抵消，运气之差由两个整数 Δg 和 Δf 描述。私人消息只改变收件人的计数。

在接近相等时用对数比较 A^Δg 和 B^Δf 会出错：当 A = 5、B = 34、Δg = 165363、Δf = 75472 时，两个对数只差 9 · 10⁻⁹，而像 10⁻⁶ 这样的容差会把两个不同的运气判为相等。所以相等性要精确判断。把 A 写成 r^s、B 写成 q^t，指数尽可能大。若 A, B > 1 且 A^Δg = B^Δf，则二者都是同一个整数的幂，此时 r = q；所以相等当且仅当 r = q 且 s·Δg = t·Δf，或者对无关的底数有 Δg = Δf = 0；底数为 1 时直接不计。只有在运气不等时才用 Δg·ln A − Δf·ln B 的符号，而双精度能分辨远小于 9 · 10⁻⁹ 的差。

其余部分是仔细的解析：命令的长短名称、回复文本，以及比较命令的检查顺序。

除读取一行外每条命令只需 O(1)，所以整个日志在线性时间内处理完。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2201_parsing_prefix_sums.cpp](2201_parsing_prefix_sums.cpp) | G++ 13.2 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 4176 KB |
| [2201_parsing_prefix_sums.go](2201_parsing_prefix_sums.go) | Go 1.14 x64 | parsing, prefix_sums | O(N) | AC | 0.109 s | 16820 KB |
| [2201_parsing_prefix_sums.java](2201_parsing_prefix_sums.java) | Java 1.8 | parsing, prefix_sums | O(N) | AC | 0.203 s | 10020 KB |
| [2201_parsing_prefix_sums.py](2201_parsing_prefix_sums.py) | Python 3.12 x64 | parsing, prefix_sums | O(N) | AC | 0.328 s | 16696 KB |
| [2201_parsing_prefix_sums.rs](2201_parsing_prefix_sums.rs) | Rust 1.75 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 11700 KB |
