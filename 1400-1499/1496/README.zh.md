# 1496. 刷屏者

[Timus 1496](https://acm.timus.ru/problem.aspx?space=1&num=1496) · 难度 49 · implementation

原题作者 Sergey Pupyrev，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

比赛最后 10 分钟收到 N 次提交（0 ≤ N ≤ 100），每次来自一个由至多 30 个小写字母和数
字组成名字的队伍。按任意顺序输出所有提交超过一次的队伍。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 个队名。

## 输出

提交多于一次的队伍，每行一个。

## 样例

### 样例 1

输入:

```
11
naucoder
iceman
abikbaev
abikbaev
petr
abikbaev
abikbaev
x
abikbaev
acrush
x
```

输出:

```
x
abikbaev
```

## 解法

用字典统计每支队伍的提交次数，输出次数大于一的队伍，每支一次。保持首次出现的顺序
不是必需的，但能让输出稳定。C++ 为 `O(N log N)`，其余平均为 `O(N)`。

注意事项：

- 提交了很多次的队伍也只输出一次（测试 01）；
- 队名是文本，所以 "0" 和 "00" 是不同的队伍（测试 04）；
- 没有重复的队伍时输出为空（测试 02、03、05）。

## 优化解法

优化解法（C++、Java）不保存首次出现的顺序：一读到某队的第二次提交，该队就加入答
案。C++ 立即输出该队；Java 把它追加到 `StringBuilder` 中，最后一次性输出整个答
案。输出顺序与简单解法不同，题目允许这样做。

优化的 C++ 解法用 `scanf` 把名字读入 31 字节的缓冲区，而不是用 `iostream`：
184 KB，而不是 412 KB，时间不变。优化的 Java 解法按 256 字节分块读入，并手工切出
每个最多 30 个字符的队名，而不是使用 `Scanner`：0.093 s，而不是 0.156 s；
428 KB，而不是 3944 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1496_implementation.cpp](1496_implementation.cpp) | G++ 13.2 x64 | implementation | O(N log N) | AC | 0.015 s | 412 KB | 11287227 |
| [1496_implementation.go](1496_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1116 KB | 11287228 |
| [1496_implementation.java](1496_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.156 s | 3944 KB | 11287230 |
| [1496_implementation.py](1496_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 336 KB | 11287229 |
| [1496_implementation.rs](1496_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 412 KB | 11287231 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1496_implementation_optimized.cpp](1496_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N log N) | AC | 0.015 s | 184 KB | 11303613 |
| [1496_implementation_optimized.java](1496_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 428 KB | 11303755 |
