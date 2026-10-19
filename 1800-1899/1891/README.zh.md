# 1891. Ocean 语言

[Timus 1891](https://acm.timus.ru/problem.aspx?space=1&num=1891) · 难度 711 · parsing

原题作者 Alex Samsonov，出自 NEERC 2011 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

对一系列变量声明进行类型检查。可用的类型为 `int`、`real` 和
`string`。每个声明用一次函数调用的返回值初始化新变量。声明类型可以
是上述三者之一，也可以是 `auto`，表示采用函数的返回类型。

函数可以重名。调用根据函数名和有序的参数类型列表选择函数，参数数量
也必须相同。实参只能是此前各行已声明的变量。类型必须完全一致，没有
隐式转换。函数名和变量名属于不同的命名空间，因此可以相同。

找出第一个错误的声明。同一行中按以下优先级检查错误：

- `Double declaration`：变量名已经声明；
- `Unknown variable`：至少一个实参尚未声明；
- `No such function`：不存在名字及参数类型均匹配的函数；
- `Invalid initialization`：显式声明的类型与返回类型不同。

如果整个程序正确，按声明顺序列出所有 `auto` 变量推断出的类型。
时间限制为 1 秒，内存限制为 64 MB。

## 输入

首先是函数头数量 f，1 ≤ f ≤ 100。随后 f 行的格式为
`name(type, ..., type) : type`，参数列表可以为空。不存在两个名字和
有序参数类型列表都相同的函数头。

接着是声明数量 n，1 ≤ n ≤ 100。随后 n 行的格式为
`type variable = name(argument, ..., argument)`，其中 `type` 也可以是
`auto`，实参为变量名。每个函数头或调用至多有 10 个参数。

名字由 1 到 20 个字母组成。变量名仅含小写英文字母；函数名还可以含有
大写英文字母，并且区分大小写。`int`、`real`、`string` 和 `auto`
不能作为名字。空格格式与样例一致；语法保证正确，只需检查上述语义错误。

## 输出

出现错误时输出 `Error on line k: message`，其中 k 是从 1 开始的声明
行号，message 必须是上述错误信息之一。此时不输出任何推断类型，即使
此前的声明正确。

否则对每个 `auto` 变量按声明顺序输出 `name : type`。如果没有 `auto`
声明，则输出为空。

## 评测方式

输出按记号逐一比较。

## 样例

### 样例 1

输入：

```
2
ReadInt() : int
IntToReal(int) : real
3
auto a = ReadInt()
auto b = IntToReal(a)
int c = ReadInt()
```

输出：

```
a : int
b : real
```

### 样例 2

输入：

```
1
ReadInt() : int
2
int x = ReadInt()
int x = ReadInt()
```

输出：

```
Error on line 2: Double declaration
```

### 样例 3

输入：

```
3
ReadInt() : int
ReadReal() : real
SumRealInt(real, int) : real
4
auto x = ReadInt()
auto y = ReadReal()
real z = SumRealInt(y, x)
real q = SumRealInt(x, y)
```

输出：

```
Error on line 4: No such function
```

## 解法

解析函数头，建立从函数签名到返回类型的映射。签名由函数名和有序的
形参类型列表组成，空列表表示无参数函数。另用一个映射保存已声明变量
的名字和类型。标点符号只用于分隔字段，不会出现在名字内部。

按顺序处理声明。首先检查新变量名是否已存在，再查询每个实参。只要
有实参未声明，就在函数匹配之前报告 `Unknown variable`。根据实参类型
构造签名，在函数表中查找。若找到，则比较返回类型和显式声明类型；
如果声明为 `auto`，就采用返回类型。

只有所有检查都成功后才加入新变量。对于 `auto`，还把名字和推断类型
加入输出列表。整个程序检查成功后才打印该列表；如果后面出现错误，
则只输出错误信息。

每行开始前，变量表恰好保存此前所有正确声明确定的类型，因此实参查询
只会使用允许的变量。签名查询精确实现重载匹配规则，返回类型比较检查
初始化是否合法。按要求的顺序执行这些步骤，即可得到最早错误行中
优先级最高的错误。

设 L 为输入总长度。使用哈希表时，解析、构造签名和查找的期望时间
为 `O(L)`，空间为 `O(L)`。

第一个样例中，`a` 的类型为 `int`，`b` 的类型为 `real`，显式声明的
`c` 不输出。第二个样例在第 2 个声明中重复声明了 `x`。第三个样例中，
`SumRealInt(y, x)` 匹配 `(real, int)`，但第 4 行的 `(int, real)`
不匹配。虽然此前已推断 `x` 和 `y` 的类型，但程序有错误，不能输出它们。

注意事项：

- 参数顺序和函数名的大小写都必须保留；
- 未知实参的错误优先于函数不存在；
- 先检查重复声明，再检查右侧表达式；
- 新变量在完成声明前不能引用自身；
- `auto` 会变成具体类型，不会出现在调用签名中；
- 不要把 `int` 隐式转换为 `real`；
- 无参数函数以及正确程序的空输出都是合法情况。

在 237 个测试上，答案与按规则单独编写的解释器一致，测试涵盖合法程序和全部四种错误。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1891_parsing.cpp](1891_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 516 KB |
| [1891_parsing.go](1891_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1180 KB |
| [1891_parsing.java](1891_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.109 s | 1288 KB |
| [1891_parsing.py](1891_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 644 KB |
| [1891_parsing.rs](1891_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.062 s | 492 KB |
