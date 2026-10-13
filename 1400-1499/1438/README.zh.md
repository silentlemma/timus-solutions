# 1438. Time Limit Exceeded

[Timus 1438](https://acm.timus.ru/problem.aspx?space=1&num=1438) · 难度 2917 · simulation

原题作者 Alexander Klepinin，出自 2006 年 2 月 25 日第七届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

执行一个用小型语言写成、不超过 2000 行的程序。每行是一个标签、一条命令，或标签
后接一条命令。命令有 `end`、`print x`、赋值 `v = x`、`v = x op y`（op 为
`+ - * / % or and xor` 之一）、`v = not x`、`goto label`，以及带六种常见比较的
`if x cmp y goto label`；x 和 y 是变量或数字。标签和关键字不区分大小写，变量名
区分。数值是 32 位整数，不会溢出。

输出程序打印的内容。若执行一千万条命令后程序仍在运行，就停止它，并加上一行
"Program terminated. Variables state:"，之后按名字顺序为每个已赋值的变量输出
"名字: 值"。

时间限制：1.5 秒。内存限制：64 MB。

## 输入

程序；除标签与其冒号之间外，任何位置都可以有任意多个空格。

## 输出

打印的数值；若程序被停止，再输出报告。

## 样例

### 样例 1

输入:

```
X = 5
      Y = 1
loop: Y = Y * X
      X = X - 1
      if X >= 1 goto LOOP
      Print Y
      y = Y - 5
      Print y
      end
```

输出:

```
120
115
```

### 样例 2

输入:

```
value = 15
        value = not value
        value = value or 4
        print value
        value = 0
loop:   
        value = value - 1
        Value = value % 6
        ValueA = value % -6
        goto loop
```

输出:

```
-12
Program terminated. Variables state:
Value: 3
ValueA: 3
value: -2499999
```

## 解法

先编译，再运行。把每行拆成单词；以 ":" 结尾的第一个单词是标签，指向下一条命令的
编号，因此只有标签的行，或连续几行这样的行，都指向其后的命令。每个变量和每个数字
都在同一张值表里占一个槽位，于是每条命令变成一个小记录：种类、槽位号、运算代码和
跳转目标。执行就是带计数器、对这些记录的简单循环；运行期间不按名字查找任何东西。

命令按形状区分：第二个单词是 "=" 就是赋值，再按长度分出复制、`not` 或二元运算。
除法向零取整，余数取 `(a mod b + |b|) mod |b|`，永不为负：第二个样例要求负值的
`% 6` 与 `% -6` 都得 3。恰好执行了一千万条命令且最后一条不是 `end` 时输出报告，
即使这条命令就在最后一行。设程序长度为 L、步数上限 K = 10⁷，复杂度 `O(L + K)`。

注意事项：

- 单独一行的标签或连续两行这样的标签（测试 03），以及与关键字同名的标签（测试
  11）；
- 名字以关键字开头的变量，例如 `ifi`（测试 10）；
- 被跳过的赋值不会让变量进入报告（测试 04）；
- 第一千万条命令是 `end` 时正常结束，是其他命令时则不是（测试 12、13、17）；
- 名字按字符编码排序，所以大写字母在前（测试 16）。

## 各语言说明

- Python 在 PyPy 下运行：最长的循环 CPython 约需 1.6 秒，PyPy 约 0.4 秒。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1438_simulation.cpp](1438_simulation.cpp) | G++ 13.2 x64 | simulation | O(L + K) | AC | 0.281 s | 1864 KB |
| [1438_simulation.go](1438_simulation.go) | Go 1.14 x64 | simulation | O(L + K) | AC | 0.125 s | 4840 KB |
| [1438_simulation.java](1438_simulation.java) | Java 1.8 | simulation | O(L + K) | AC | 0.421 s | 7320 KB |
| [1438_simulation.py](1438_simulation.py) | PyPy 3.10 x64 | simulation | O(L + K) | AC | 0.843 s | 8448 KB |
| [1438_simulation.rs](1438_simulation.rs) | Rust 1.75 x64 | simulation | O(L + K) | AC | 0.140 s | 2096 KB |
