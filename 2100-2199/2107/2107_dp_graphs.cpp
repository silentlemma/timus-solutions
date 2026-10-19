#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n >> k;
    std::vector<int> next(n), indegree(n);
    for (int &value : next) {
        std::cin >> value;
        --value;
        if (value >= 0 && ++indegree[value] > 1) {
            std::cout << "No\n";
            return 0;
        }
    }

    std::vector<bool> seen(n);
    std::vector<std::vector<std::vector<int>>> paths(n + 1);
    for (int start = 0; start < n; ++start) {
        if (indegree[start] != 0) {
            continue;
        }
        std::vector<int> path;
        for (int vertex = start; vertex >= 0; vertex = next[vertex]) {
            seen[vertex] = true;
            path.push_back(vertex);
        }
        paths[path.size()].push_back(path);
    }
    for (int start = 0; start < n; ++start) {
        if (seen[start]) {
            continue;
        }
        int length = 0;
        for (int vertex = start; !seen[vertex]; vertex = next[vertex]) {
            seen[vertex] = true;
            ++length;
        }
        if (k % length != 0) {
            std::cout << "No\n";
            return 0;
        }
    }

    std::vector<int> lengths, radix, multiplier;
    int states = 1;
    for (int length = 1; length <= n; ++length) {
        if (!paths[length].empty()) {
            lengths.push_back(length);
            radix.push_back(static_cast<int>(paths[length].size()) + 1);
            multiplier.push_back(states);
            states *= radix.back();
        }
    }
    const int types = static_cast<int>(lengths.size());
    std::vector<std::vector<int>> digits(states, std::vector<int>(types));
    std::vector<int> groups;
    for (int state = 1; state < states; ++state) {
        int total = 0;
        for (int type = 0; type < types; ++type) {
            digits[state][type] = state / multiplier[type] % radix[type];
            total += digits[state][type] * lengths[type];
        }
        if (k % total == 0) {
            groups.push_back(state);
        }
    }

    // Each digit counts paths of one length, so equivalent paths share a state.
    std::vector<int> choice(states, -1);
    choice[0] = 0;
    for (int state = 1; state < states; ++state) {
        int anchor = types - 1;
        while (digits[state][anchor] == 0) {
            --anchor;
        }
        for (int group : groups) {
            if (group > state) {
                break;
            }
            if (digits[group][anchor] == 0 || choice[state - group] < 0) {
                continue;
            }
            bool contained = true;
            for (int type = 0; type < types; ++type) {
                if (digits[group][type] > digits[state][type]) {
                    contained = false;
                    break;
                }
            }
            if (contained) {
                choice[state] = group;
                break;
            }
        }
    }
    if (choice.back() < 0) {
        std::cout << "No\n";
        return 0;
    }

    for (int state = states - 1; state > 0;) {
        const int group = choice[state];
        std::vector<std::vector<int>> cycle;
        for (int type = 0; type < types; ++type) {
            for (int count = 0; count < digits[group][type]; ++count) {
                auto &bucket = paths[lengths[type]];
                cycle.push_back(bucket.back());
                bucket.pop_back();
            }
        }
        for (std::size_t index = 0; index < cycle.size(); ++index) {
            next[cycle[index].back()] = cycle[(index + 1) % cycle.size()].front();
        }
        state -= group;
    }
    std::cout << "Yes\n";
    for (int vertex = 0; vertex < n; ++vertex) {
        if (vertex > 0) {
            std::cout << ' ';
        }
        std::cout << next[vertex] + 1;
    }
    std::cout << '\n';
}
