#include <algorithm>
#include <bitset>
#include <cstdio>
#include <vector>

const int MOST = 500;

int n, counter = 0;
std::vector<int> t, index_, low, group;
std::vector<double> p;
std::vector<bool> onStack;
std::vector<std::vector<int>> deps, groups;
std::vector<int> stack_;

// hypotheses on one cycle of dependencies are all true or all false,
// and Tarjan's method finds those groups, dependencies first
void visit(int v) {
    index_[v] = low[v] = counter++;
    stack_.push_back(v);
    onStack[v] = true;
    for (int w : deps[v]) {
        if (index_[w] < 0) {
            visit(w);
            low[v] = std::min(low[v], low[w]);
        } else if (onStack[w]) {
            low[v] = std::min(low[v], index_[w]);
        }
    }
    if (low[v] == index_[v]) {
        std::vector<int> members;
        while (true) {
            int w = stack_.back();
            stack_.pop_back();
            onStack[w] = false;
            group[w] = groups.size();
            members.push_back(w);
            if (w == v) break;
        }
        groups.push_back(members);
    }
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    t.resize(n);
    p.resize(n);
    deps.resize(n);
    for (int i = 0; i < n; i++) {
        int k;
        scanf("%d %lf %d", &t[i], &p[i], &k);
        deps[i].resize(k);
        for (int &d : deps[i]) {
            scanf("%d", &d);
            d--;
        }
    }
    index_.assign(n, -1);
    low.assign(n, 0);
    group.assign(n, -1);
    onStack.assign(n, false);
    for (int v = 0; v < n; v++) {
        if (index_[v] < 0) visit(v);
    }
    // a group is worth checking only when every group it rests on is fully
    // admissible; inside it, checks stop at the first failure, so the order
    // by t / (1 - p) is the cheapest
    size_t count = groups.size();
    std::vector<double> cost(count), sound(count);
    std::vector<std::bitset<MOST>> reach(count);
    for (size_t g = 0; g < count; g++) {
        std::vector<int> members = groups[g];
        std::sort(members.begin(), members.end(),
                  [](int a, int b) { return t[a] * (1 - p[b]) < t[b] * (1 - p[a]); });
        double still = 1, expected = 0;
        for (int v : members) {
            expected += still * t[v];
            still *= p[v];
        }
        cost[g] = expected;
        sound[g] = still;
        for (int v : members) {
            for (int w : deps[v]) {
                if (group[w] != (int)g) {
                    reach[g] |= reach[group[w]];
                    reach[g][group[w]] = true;
                }
            }
        }
    }
    double answer = 0;
    for (size_t g = 0; g < count; g++) {
        double chance = 1;
        for (size_t h = 0; h < count; h++) {
            if (reach[g][h]) chance *= sound[h];
        }
        answer += chance * cost[g];
    }
    printf("%.3f\n", answer);
}
