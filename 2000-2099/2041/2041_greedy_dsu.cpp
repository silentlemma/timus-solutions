#include <algorithm>
#include <iostream>
#include <numeric>
#include <tuple>
#include <utility>
#include <vector>

struct Doll {
    int inner, outer, id;
};

struct Predecessor {
    std::vector<int> parent, best;
    std::vector<unsigned char> rank;
    explicit Predecessor(int n) : parent(n + 1), best(n + 1), rank(n + 1) {
        std::iota(parent.begin(), parent.end(), 0);
        std::iota(best.begin(), best.end(), 0);
    }
    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    void erase(int x) {
        int a = find(x), b = find(x - 1);
        if (rank[a] < rank[b])
            std::swap(a, b);
        parent[b] = a;
        best[a] = std::min(best[a], best[b]);
        if (rank[a] == rank[b])
            ++rank[a];
    }
};

std::vector<int> solve(std::vector<Doll> items) {
    const int n = static_cast<int>(items.size());
    int limit = 0;
    for (const auto &item : items)
        limit = std::max(limit, item.outer);
    ++limit;
    std::sort(items.begin(), items.end(), [](const Doll &a, const Doll &b) {
        return std::tie(a.inner, a.outer, a.id) < std::tie(b.inner, b.outer, b.id);
    });
    Predecessor available(n);
    std::vector<int> answer;
    answer.reserve(n);
    for (int step = 0; step < n; ++step) {
        int cut = static_cast<int>(
            std::lower_bound(items.begin(), items.end(), limit,
                             [](const Doll &item, int value) { return item.inner < value; }) -
            items.begin());
        int position = available.best[available.find(cut)];
        if (position == 0)
            return {};
        const auto &item = items[position - 1];
        answer.push_back(item.id);
        limit = item.outer;
        available.erase(position);
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<Doll> items(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> items[i].inner >> items[i].outer;
        items[i].id = i + 1;
    }
    auto answer = solve(std::move(items));
    if (answer.empty())
        std::cout << "No\n";
    else {
        std::cout << "Yes\n";
        for (int i = 0; i < n; ++i)
            std::cout << (i ? " " : "") << answer[i];
        std::cout << '\n';
    }
}
