#include <cstdio>
#include <vector>

int n, q;
std::vector<int> head, nxt, to, askHead, askNext, askVertex, askDist, answer;
std::vector<int> depth, path, stack;

// walk the tree from root in preorder: when a vertex is reached, path holds
// its ancestors by depth, so a query at it with d <= depth is answered at
// once; returns the deepest vertex
int walk(int root) {
    int deepest = root;
    depth.assign(n + 1, -1);
    depth[root] = 0;
    stack.assign(1, root);
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        path[depth[v]] = v;
        if (depth[v] > depth[deepest]) deepest = v;
        for (int i = askHead[v]; i >= 0; i = askNext[i]) {
            if (answer[i] == 0 && askDist[i] <= depth[v]) answer[i] = path[depth[v] - askDist[i]];
        }
        for (int e = head[v]; e >= 0; e = nxt[e]) {
            if (depth[to[e]] < 0) {
                depth[to[e]] = depth[v] + 1;
                stack.push_back(to[e]);
            }
        }
    }
    return deepest;
}

int main() {
    if (scanf("%d %d", &n, &q) != 2) return 0;
    head.assign(n + 1, -1);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        to.push_back(b);
        nxt.push_back(head[a]);
        head[a] = (int)to.size() - 1;
        to.push_back(a);
        nxt.push_back(head[b]);
        head[b] = (int)to.size() - 1;
    }
    askHead.assign(n + 1, -1);
    askNext.resize(q);
    askVertex.resize(q);
    askDist.resize(q);
    answer.assign(q, 0);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &askVertex[i], &askDist[i]);
        askNext[i] = askHead[askVertex[i]];
        askHead[askVertex[i]] = i;
    }
    path.resize(n + 1);
    // at least one diameter end is farthest from any vertex; the walk from
    // vertex 1 finds one end, and the walk from there finds the other
    int a = walk(1);
    int b = walk(a);
    walk(b);
    for (int i = 0; i < q; i++) printf("%d\n", answer[i]);
    return 0;
}
