#include <cstdio>
#include <functional>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

// every piece that can ever appear is a maximal run of rings above some
// content; such runs nest, and the children of a run are the runs above its
// smallest content
struct Chain {
    vector<int> rings, low, grundy;
    vector<vector<int>> children;

    int build(int left, int right) {
        int node = low.size(), m = rings[left];
        for (int i = left; i <= right; i++)
            m = min(m, rings[i]);
        low.push_back(m);
        children.emplace_back();
        grundy.push_back(0);
        for (int i = left; i <= right; i++)
            if (rings[i] > m) {
                int j = i;
                while (j + 1 <= right && rings[j + 1] > m)
                    j++;
                int child = build(i, j);
                children[node].push_back(child);
                i = j;
            }
        return node;
    }

    // {x: xor of the pieces left by removing rings up to x} in node
    map<int, int> afterMoves(int node) {
        map<int, int> result;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        int x = 0;
        for (int c : children[node]) {
            heap.push({low[c], c});
            x ^= grundy[c];
        }
        result[low[node]] = x;
        while (!heap.empty()) {
            int content = heap.top().first;
            while (!heap.empty() && heap.top().first == content) {
                int c = heap.top().second;
                heap.pop();
                x ^= grundy[c];
                for (int d : children[c]) {
                    x ^= grundy[d];
                    heap.push({low[d], d});
                }
            }
            result[content] = x;
        }
        return result;
    }

    int analyse() {
        build(0, rings.size() - 1);
        // children are built after their parents, so go backwards
        for (int node = low.size() - 1; node >= 0; node--) {
            set<int> options;
            for (auto &kv : afterMoves(node))
                options.insert(kv.second);
            int g = 0;
            while (options.count(g))
                g++;
            grundy[node] = g;
        }
        return grundy[0];
    }
};

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    vector<Chain> chains(k);
    vector<int> g(k);
    int total = 0;
    for (int i = 0; i < k; i++) {
        int length;
        if (scanf("%d", &length) != 1)
            return 0;
        chains[i].rings.resize(length);
        for (int &r : chains[i].rings)
            if (scanf("%d", &r) != 1)
                return 0;
        g[i] = chains[i].analyse();
        total ^= g[i];
    }
    if (total == 0) {
        printf("S\n");
        return 0;
    }
    // a winning move leaves the chain with the xor of all other chains
    for (int i = 0; i < k; i++) {
        map<int, int> after = chains[i].afterMoves(0);
        for (size_t j = 0; j < chains[i].rings.size(); j++)
            if (after[chains[i].rings[j]] == (total ^ g[i])) {
                printf("G\n%d %d\n", i + 1, (int)j + 1);
                return 0;
            }
    }
}
