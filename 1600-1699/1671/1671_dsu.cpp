#include <cstdio>
#include <string>
#include <vector>

std::vector<int> parent;

int find(int v) {
    int root = v;
    while (parent[root] != root) {
        root = parent[root];
    }
    while (parent[v] != root) {
        int next = parent[v];
        parent[v] = root;
        v = next;
    }
    return root;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<int> from(m), to(m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &from[i], &to[i]);
    }
    int q;
    scanf("%d", &q);
    std::vector<int> cuts(q);
    std::vector<bool> cut(m, false);
    for (int& c : cuts) {
        scanf("%d", &c);
        cut[--c] = true;
    }
    parent.resize(n + 1);
    for (int v = 0; v <= n; v++) {
        parent[v] = v;
    }
    int pieces = n;
    auto join = [&](int i) {
        int a = find(from[i]), b = find(to[i]);
        if (a != b) {
            parent[a] = b;
            pieces--;
        }
    };
    // run backwards: start from the web after all cuts and put the threads
    // back one by one, last cut first
    for (int i = 0; i < m; i++) {
        if (!cut[i]) {
            join(i);
        }
    }
    std::vector<int> answers(q);
    for (int k = q - 1; k >= 0; k--) {
        answers[k] = pieces;
        join(cuts[k]);
    }
    std::string out;
    for (int k = 0; k < q; k++) {
        out += std::to_string(answers[k]) + (k + 1 < q ? " " : "\n");
    }
    printf("%s", out.c_str());
}
