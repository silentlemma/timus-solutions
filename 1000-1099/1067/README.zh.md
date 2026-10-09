# 1067. 由完整路径重建的文件夹树

[Timus 1067](https://acm.timus.ru/problem.aspx?space=1&num=1067) · 难度 363 · trees, sorting

原题出自 2000–2001 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 `N` 条不同的文件夹路径（`1 ≤ N ≤ 500`），每条不超过 80 个字符，文件夹名之间用反斜杠分隔。名字由 1 到 8
个字符组成：大写字母、数字和特殊字符 ``!#$%&'()-@^_`{}~``。输出文件夹树：每个文件夹占一行，每深一层多缩进
一个空格，每个文件夹的子文件夹紧跟在它后面，每一层的文件夹按字典序排列。

时间限制：2 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 行路径。

## 输出

文件夹树，每行一个文件夹。

## 评测方式

输出必须与期望文本相同；只忽略末尾的空白字符。行首的空格是答案的一部分。

## 样例

### 样例 1

输入：

```
7
WINNT\SYSTEM32\CONFIG
GAMES
WINNT\DRIVERS
HOME
WIN\SOFT
GAMES\DRIVERS
WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86
```

输出：

```
GAMES
 DRIVERS
HOME
WIN
 SOFT
WINNT
 DRIVERS
 SYSTEM32
  CERTSRV
   CERTCO~1
    X86
  CONFIG
```

## 题解

把每条路径放进文件夹树：从根出发沿路径中的名字往下走，缺少的文件夹就新建。然后深度优先遍历，按子文件夹的排序
顺序访问，输出每个文件夹，前面加上与深度相同数量的空格。如果每个文件夹用有序映射保存子文件夹，顺序就自然
得到。`O(L log N)`，`L` 为路径总长度。

注意事项：

- 把完整路径当作字符串排序是不够的：反斜杠位于编码表中间，在大写字母和数字之后，但在 `^`、`_`、`` ` ``、`{`、
  `}` 和 `~` 之前，所以 `A!` 会排在 `A` 和 `A\X` 之间；名字必须逐层比较；
- 路径中间的文件夹可能从未单独列出，不同父文件夹下的同名文件夹是不同的文件夹；
- 路径中没有空格，所以可以按空白分隔的记号读取，这样也顺便忽略了回车符。

答案用另一种方法做了核对：把所有路径的所有前缀当作名字元组排序，这样每个文件夹正好排在它的整棵子树之前。

## 各语言说明

- C++、Java 和 Rust 用有序映射（`std::map`、`TreeMap`、`BTreeMap`）保存子文件夹；Go 和 Python 用哈希表，
  输出时再对键排序。
- 各语言都按字符编码比较名字，对这些字符来说正是题目要求的顺序。
- Java 用正则表达式 `\\`（一个转义的反斜杠）拆分路径。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1067_trees_sorting.cpp](1067_trees_sorting.cpp) | G++ 13.2 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 3472 KB |
| [1067_trees_sorting.go](1067_trees_sorting.go) | Go 1.14 x64 | trees, sorting | O(L log N) | AC | 0.015 s | 8376 KB |
| [1067_trees_sorting.java](1067_trees_sorting.java) | Java 1.8 | trees, sorting | O(L log N) | AC | 0.093 s | 7380 KB |
| [1067_trees_sorting.py](1067_trees_sorting.py) | Python 3.12 x64 | trees, sorting | O(L log N) | AC | 0.078 s | 6692 KB |
| [1067_trees_sorting.rs](1067_trees_sorting.rs) | Rust 1.75 x64 | trees, sorting | O(L log N) | AC | 0.031 s | 12116 KB |
