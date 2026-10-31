# 1846. GCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · 难度 155 · segment_tree

原题作者 Alexey Samsonov，出自 2010 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个正整数多重集开始时为空。每次操作加入一个数，或删除集合中某个数的一个副本。每次操作后输出整个多重集的最大公约数；空多重集的最大公约数规定为 1。

## 输入

q（1 ≤ q ≤ 10⁵），然后是 q 行 "+ x" 或 "- x"，其中 1 ≤ x ≤ 10⁹。只会删除存在的数。

## 输出

每次操作后的最大公约数，每行一个。

## 样例

### 样例 1

输入：

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

输出：

```
8
2
2
2
6
```

## 解法

最大公约数无法"撤销"，所以删除需要借助数据结构。在按操作编号建立的线段树中，给每次加入分配一个自己的叶子，并为每个值保存一个存放它的叶子的栈。
加入 x 时把 x 写进这次操作的叶子；删除 x 时清空它的栈顶叶子，写入 0，由于 gcd(a, 0) = a，这不会改变任何最大公约数。
每个内部节点保存其子节点的最大公约数，所以根就是多重集的最大公约数，根为 0 表示多重集为空，此时输出 1。
更新一个叶子要重新计算它的祖先；一旦某个节点的值没有变化就可以停止向上，因为更上面的值也不会变。`O(q log q log x)`。

在样例中，叶子保存 8、6、8，所以最大公约数为 2。删除两个 8 会清空两个叶子，只剩下 6。

注意事项：

- 空多重集输出 1 而不是 0；
- 相等的数可能被加入多次并一次删除一个；
- 时限只有半秒，提前停止向上和快速读入都很重要；简单的 Python 版本
  在 PyPy 上运行。

在三十个最多 10⁵ 次操作的随机文件上，答案与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法先读入全部操作，把其中的值排序去重，给每个不同的值一个叶子并记录
它的副本数，而不是每次加入占一个叶子、再用哈希表保存叶子栈。计数为正时叶子存 x，
否则存 0，因此只有某个值出现或消失时树才会改变。每个操作存成一个带符号的 `int`，
即 +x 或 −x，因为 x ≤ 10⁹ 所以放得下；值对应的叶子用二分查找确定。数字从用
`fread` 反复填充的 4 KB 缓冲区中手工解析：{1846_segment_tree_optimized.cpp}。

优化的 Go 解法先读入全部操作，把其中的值排序去重，给每个不同的值一个叶子并记录它
的副本数，而不是每次加入占一个叶子、再用 `map` 保存叶子切片。计数为正时叶子存
x，否则存 0，因此只有某个值出现或消失时树才会改变。每个操作存成一个 `int32`，即
+x 或 −x，因为 x ≤ 10⁹ 所以放得下，树和计数也都是 `int32` 切片；值对应的叶子用二
分查找确定。数字从 `bufio` 读取器中手工解析，而不是把输入切分成单词：
{1846_segment_tree_optimized.go}。

优化的 Java 解法先读入全部操作，从 64 KB 缓冲区中手工解析，而不是用
`StreamTokenizer`。它通过在排好序的副本中二分查找给值编号，并用两个 `int` 数组以
链式栈保存每个值所在的叶子：每个值的栈顶叶子和每个叶子下面的叶子，而不是
`ArrayDeque<Integer>` 的 `HashMap`，因此没有任何数被装箱；每次加入仍然占一个叶
子：{1846_segment_tree_optimized.java}。

优化的 Python 解法一次读入全部输入并按行切分，避免每次操作都调用缓冲输入流。
每个不同的值只有一个叶子和一个副本计数，因此重复副本不会更新树。
树和计数使用整数列表代替 `array("I")`，避免在更新循环中每次访问都转换数组元素。
每个值只在字典中查找一次，答案仍按每 1024 个一批输出。使用 PyPy 3.10；
原先逐行读取的版本在 CPython 下超过了时间限制：
{1846_segment_tree_optimized.py}。

优化的 Rust 解法先读入全部操作并释放输入文本，把值排序去重，给每个不同的值一个叶
子并记录它的副本数，而不是每次加入占一个叶子、再用 `HashMap` 保存 `Vec` 栈。计数
为正时叶子存 x，否则存 0，因此只有某个值出现或消失时树才会改变。每个操作存成一个
`i32`，即 +x 或 −x，因为 x ≤ 10⁹ 所以放得下，树和计数都是 `u32`；答案通过
`BufWriter` 输出，而不是先收集到 `String` 中：{1846_segment_tree_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1846_segment_tree_optimized.cpp`: 时间降低 +61.58%; 内存降低 +75.57%; 基础版本: `1846_segment_tree.cpp`.

- `1846_segment_tree_optimized.go`: 时间降低 -19.23%; 内存降低 +75.57%; 基础版本: `1846_segment_tree.go`.

- `1846_segment_tree_optimized.java`: 时间降低 +46.58%; 内存降低 +50.17%; 基础版本: `1846_segment_tree.java`.

- `1846_segment_tree_optimized.py`: 时间降低 -6.00%; 内存降低 +39.87%; 基础版本: `1846_segment_tree.py`.

- `1846_segment_tree_optimized.rs`: 时间降低 -69.57%; 内存降低 +74.46%; 基础版本: `1846_segment_tree.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.203 s | 8612 KB | 11304079 |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB | 11290662 |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.234 s | 20164 KB | 11305869 |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB | 11290667 |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB | 11290670 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree_optimized.cpp](1846_segment_tree_optimized.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 2104 KB | 11305870 |
| [1846_segment_tree_optimized.go](1846_segment_tree_optimized.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.093 s | 3420 KB | 11305877 |
| [1846_segment_tree_optimized.java](1846_segment_tree_optimized.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.125 s | 10048 KB | 11307314 |
| [1846_segment_tree_optimized.py](1846_segment_tree_optimized.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.265 s | 22284 KB | 11307371 |
| [1846_segment_tree_optimized.rs](1846_segment_tree_optimized.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 3148 KB | 11305885 |
