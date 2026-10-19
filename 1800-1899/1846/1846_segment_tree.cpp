#include <cstdio>
#include <numeric>
#include <unordered_map>
#include <vector>

int main() {
    int q;
    if (scanf("%d", &q) != 1) return 0;
    int size = 1;
    while (size < q) size *= 2;
    // every addition gets its own leaf; an empty leaf holds 0, which does
    // not change a gcd
    std::vector<int> tree(2 * size, 0);
    std::unordered_map<int, std::vector<int>> leaves;  // value -> leaves
    for (int k = 0; k < q; k++) {
        char sign;
        int x;
        scanf(" %c %d", &sign, &x);
        int v, value;
        if (sign == '+') {
            leaves[x].push_back(k);
            v = k + size;
            value = x;
        } else {
            v = leaves[x].back() + size;
            leaves[x].pop_back();
            value = 0;
        }
        tree[v] = value;
        // once a node keeps its value, so do all above it
        for (v /= 2; v > 0; v /= 2) {
            int g = std::gcd(tree[2 * v], tree[2 * v + 1]);
            if (tree[v] == g) break;
            tree[v] = g;
        }
        printf("%d\n", tree[1] ? tree[1] : 1);
    }
    return 0;
}
