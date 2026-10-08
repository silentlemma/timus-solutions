#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

const int END_OF_INPUT = -1;

// Disjoint sets of prefix positions; parity[x] is the parity of the number of
// ones between x and its parent.
struct Dsu {
    std::vector<int> parent, parity, rank;

    int add() {
        parent.push_back(parent.size());
        parity.push_back(0);
        rank.push_back(0);
        return parent.size() - 1;
    }

    std::pair<int, int> find(int x) {
        if (parent[x] == x)
            return {x, 0};
        auto [root, p] = find(parent[x]);
        parent[x] = root;
        parity[x] ^= p;
        return {root, parity[x]};
    }

    // Records that x and y differ by parity w; false on a contradiction.
    bool unite(int x, int y, int w) {
        auto [rx, px] = find(x);
        auto [ry, py] = find(y);
        if (rx == ry)
            return (px ^ py) == w;
        if (rank[rx] < rank[ry])
            std::swap(rx, ry);
        parent[ry] = rx;
        parity[ry] = px ^ py ^ w;
        if (rank[rx] == rank[ry])
            rank[rx]++;
        return true;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int length, q;
    while (std::cin >> length && length != END_OF_INPUT) {
        std::cin >> q;
        Dsu d;
        std::unordered_map<int, int> ids;
        auto id = [&](int pos) {
            auto it = ids.find(pos);
            if (it != ids.end())
                return it->second;
            return ids[pos] = d.add();
        };
        int answer = q;
        for (int i = 0; i < q; i++) {
            int l, r;
            std::string word;
            std::cin >> l >> r >> word;
            // ones in [l, r] = prefix(r) - prefix(l - 1)
            if (answer == q && !d.unite(id(l - 1), id(r), word == "odd"))
                answer = i;
        }
        std::cout << answer << '\n';
    }
    return 0;
}
