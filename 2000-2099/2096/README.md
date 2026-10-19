# 2096. Questions about plans derived from earlier plans

[Timus 2096](https://acm.timus.ru/problem.aspx?space=1&num=2096) · difficulty 2627 · dfs, trees

Original problem by Egor Shchelkonogov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Plan 0 gives an activity for each of n days. Plan i (i = 1 … m) first
asks questions "what is on day x in plan f" for earlier plans f, then
copies an earlier plan pᵢ and applies changes, each setting the days d,
d + p, …, d + (k − 1)p to a new activity (later changes win). Answer all
questions. The limits are 2 seconds and 64 MB.

## Input

n and m (up to 10⁵), the n activities of plan 0, then for each plan its
questions and its base plan with the changes; at most 10⁵ questions and
10⁵ changes in total, and the changes touch at most 5·10⁶ days in total.

## Output

For each plan, one line with the answers to its questions.

## Examples

### Example 1

Input:

```
3 2
1 2 3
1
0 3
0 2
1 2 2 4
2 2 1 5
3
1 1
1 2
1 3
0 0
```

Output:

```
3
4 5 5
```

## Solution

Every plan is its base plan plus its own changes, so the plans form a
tree rooted at plan 0, and every question is about a fixed plan. All of
them are answered offline in one walk over the tree with a single array
of activities: entering a plan applies its changes, saving the old
values of the days it overwrites, answers the questions about this plan,
visits the children, and on leaving restores the saved values in
reverse order. Each changed day is written and restored once, so the
work is O(n + m + Σ k + q). The walk uses an explicit stack, because the
tree can be a path of 10⁵ plans.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2096_dfs_trees.cpp](2096_dfs_trees.cpp) | G++ 13.2 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.078 s | 24856 KB |
| [2096_dfs_trees.go](2096_dfs_trees.go) | Go 1.14 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.093 s | 28888 KB |
| [2096_dfs_trees.java](2096_dfs_trees.java) | Java 1.8 | dfs, trees | O(n + m + sum k + q) | AC | 0.156 s | 30380 KB |
| [2096_dfs_trees.py](2096_dfs_trees.py) | Python 3.12 x64 | dfs, trees | O(n + m + sum k + q) | AC | 1.312 s | 36924 KB |
| [2096_dfs_trees.rs](2096_dfs_trees.rs) | Rust 1.75 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.078 s | 25888 KB |
