#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int WIN = 3, DRAW = 1;

int n;
vector<vector<int>> said, graph;
vector<int> idx, low, comp, stk;
vector<bool> onStack;
int counter = 0, comps = 0;

// Tarjan's strongly connected components
void visit(int v) {
    idx[v] = low[v] = counter++;
    stk.push_back(v);
    onStack[v] = true;
    for (int u : graph[v]) {
        if (idx[u] < 0) {
            visit(u);
            low[v] = min(low[v], low[u]);
        } else if (onStack[u])
            low[v] = min(low[v], idx[u]);
    }
    if (low[v] == idx[v]) {
        int u;
        do {
            u = stk.back();
            stk.pop_back();
            onStack[u] = false;
            comp[u] = comps;
        } while (u != v);
        comps++;
    }
}

// 2-SAT on "captain i tells the truth" (literal 2i) or lies (2i + 1),
// and i scored against j exactly when the literal of statement (i, j) holds
int literal(int i, int j) { return said[i][j] == 1 ? 2 * i : 2 * i + 1; }

int main() {
    scanf("%d", &n);
    said.assign(n, vector<int>(n));
    for (auto &row : said)
        for (int &x : row)
            scanf("%d", &x);
    graph.assign(2 * n, {});
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (said[i][j] >= 0 && said[j][i] >= 0) {
                // somebody scores in every match: a or b, so not a -> b
                int a = literal(i, j), b = literal(j, i);
                graph[a ^ 1].push_back(b);
                graph[b ^ 1].push_back(a);
            }
    idx.assign(2 * n, -1);
    low.assign(2 * n, 0);
    comp.assign(2 * n, -1);
    onStack.assign(2 * n, false);
    for (int v = 0; v < 2 * n; v++)
        if (idx[v] < 0)
            visit(v);
    vector<bool> truthful(n);
    for (int i = 0; i < n; i++) {
        if (comp[2 * i] == comp[2 * i + 1]) {
            puts("Impossible");
            return 0;
        }
        // Tarjan numbers components in reverse topological order
        truthful[i] = comp[2 * i] < comp[2 * i + 1];
    }
    auto scored = [&](int i, int j) { return said[i][j] < 0 || (said[i][j] == 1) == truthful[i]; };
    vector<vector<int>> table(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            bool a = scored(i, j), b = scored(j, i);
            if (a && b)
                table[i][j] = table[j][i] = DRAW;
            else if (a)
                table[i][j] = WIN;
            else
                table[j][i] = WIN;
        }
    for (auto &row : table)
        for (int j = 0; j < n; j++)
            printf("%d%c", row[j], j + 1 < n ? ' ' : '\n');
}
