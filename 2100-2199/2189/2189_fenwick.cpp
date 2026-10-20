#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

struct Role {
    std::vector<int> positions;
    std::vector<int> tree;
    std::int64_t score;
    int count = 0;
    int step = 1;

    explicit Role(std::int64_t initial_score) : score(initial_score) {}

    void prepare() {
        std::sort(positions.begin(), positions.end());
        positions.erase(std::unique(positions.begin(), positions.end()), positions.end());
        tree.resize(positions.size() + 1);
        while (step * 2 <= static_cast<int>(positions.size())) {
            step *= 2;
        }
    }

    int prefix(int index) const {
        int result = 0;
        for (; index > 0; index -= index & -index) {
            result += tree[index];
        }
        return result;
    }

    int kth(int order) const {
        int index = 0;
        for (int jump = step; jump > 0; jump /= 2) {
            int next = index + jump;
            if (next < static_cast<int>(tree.size()) && tree[next] < order) {
                index = next;
                order -= tree[next];
            }
        }
        return index + 1;
    }

    void change(int position, int delta, int size) {
        int rank = static_cast<int>(std::lower_bound(positions.begin(), positions.end(), position) -
                                    positions.begin()) +
                   1;
        int before = prefix(rank - 1);
        int left = before == 0 ? 0 : positions[kth(before) - 1];
        int next_order = before + 1 + (delta < 0 ? 1 : 0);
        int right = next_order > count ? size + 1 : positions[kth(next_order) - 1];
        // Splitting a gap removes exactly the intervals crossing this position.
        std::int64_t difference = std::int64_t(position - left) * (right - position);
        score -= delta * difference;
        count += delta;
        for (int index = rank; index < static_cast<int>(tree.size()); index += index & -index) {
            tree[index] += delta;
        }
    }
};

struct Query {
    int position;
    int role;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int size, query_count;
    std::cin >> size >> query_count;
    std::int64_t total = std::int64_t(size) * (size + 1) / 2;
    std::vector<Role> roles;
    roles.reserve(size + query_count);
    std::unordered_map<int, int> ids;
    ids.reserve(size + query_count);

    auto get_role = [&](int value) {
        auto found = ids.find(value);
        if (found != ids.end()) {
            return found->second;
        }
        int id = static_cast<int>(roles.size());
        ids.emplace(value, id);
        roles.emplace_back(total);
        return id;
    };

    std::vector<int> current(size + 1);
    for (int position = 1; position <= size; ++position) {
        int value;
        std::cin >> value;
        int id = get_role(value);
        current[position] = id;
        roles[id].positions.push_back(position);
    }
    std::vector<Query> queries(query_count);
    for (auto &query : queries) {
        int value;
        std::cin >> query.position >> value;
        query.role = get_role(value);
        roles[query.role].positions.push_back(query.position);
    }
    for (auto &role : roles) {
        role.prepare();
    }
    for (int position = 1; position <= size; ++position) {
        roles[current[position]].change(position, 1, size);
    }

    using Entry = std::pair<std::int64_t, int>;
    std::vector<Entry> entries;
    entries.reserve(roles.size());
    for (int id = 0; id < static_cast<int>(roles.size()); ++id) {
        entries.emplace_back(roles[id].score, id);
    }
    std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> minimum(
        std::greater<Entry>(), std::move(entries));

    for (const auto &query : queries) {
        int old = current[query.position];
        if (old != query.role) {
            roles[old].change(query.position, -1, size);
            roles[query.role].change(query.position, 1, size);
            current[query.position] = query.role;
            minimum.emplace(roles[old].score, old);
            minimum.emplace(roles[query.role].score, query.role);
        }
        while (minimum.top().first != roles[minimum.top().second].score) {
            minimum.pop();
        }
        std::cout << minimum.top().first << '\n';
    }
}
