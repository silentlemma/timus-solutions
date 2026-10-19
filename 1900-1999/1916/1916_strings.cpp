#include <functional>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

constexpr int MODULUS = 1000000007;

int distinctParts(const std::vector<std::vector<int>> &rules, int width) {
    const std::size_t limit = std::size_t(width - 1);
    std::vector<std::string> prefixes(rules.size());
    std::vector<std::string> suffixes(rules.size());
    std::vector<bool> visited(rules.size(), false);
    std::unordered_set<std::string> parts;
    std::function<void(int)> visit = [&](int vertex) {
        if (visited[vertex]) {
            return;
        }
        if (rules[vertex].empty()) {
            prefixes[vertex] = std::string(1, char(vertex + 1));
            suffixes[vertex] = prefixes[vertex];
        } else {
            std::string prefix;
            std::string suffix;
            for (int child : rules[vertex]) {
                visit(child);
                const std::string span = suffix + prefixes[child];
                for (std::size_t start = 0; start + std::size_t(width) <= span.size(); ++start) {
                    parts.insert(span.substr(start, std::size_t(width)));
                }
                prefix = (prefix + prefixes[child]).substr(0, limit);
                const std::string tail = suffix + suffixes[child];
                suffix = tail.substr(tail.size() > limit ? tail.size() - limit : 0);
            }
            prefixes[vertex] = prefix;
            suffixes[vertex] = suffix;
        }
        visited[vertex] = true;
    };
    for (std::size_t vertex = 0; vertex < rules.size(); ++vertex) {
        visit(int(vertex));
    }
    return int(parts.size() % MODULUS);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, width;
    std::cin >> count >> width;
    std::vector<std::vector<int>> rules(count);
    for (auto &rule : rules) {
        int length;
        std::cin >> length;
        if (length != -1) {
            rule.resize(length);
            for (int &child : rule) {
                std::cin >> child;
                --child;
            }
        }
    }
    std::cout << distinctParts(rules, width) << '\n';
    return 0;
}
