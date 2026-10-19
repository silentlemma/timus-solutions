#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Node {
    int first = 0;
    int next = 0;
    int leaves = 0;
    int normal = 0;
    int supplied = 0;
    unsigned char label = 0;
};

int minimum_clicks(const std::vector<std::string> &words) {
    size_t capacity = 1;
    for (const auto &word : words)
        capacity += word.size();
    std::vector<Node> nodes(1);
    nodes.reserve(capacity);
    for (const auto &word : words) {
        int node = 0;
        for (unsigned char letter : word) {
            int child = nodes[node].first;
            while (child && nodes[child].label != letter)
                child = nodes[child].next;
            if (!child) {
                child = static_cast<int>(nodes.size());
                Node added;
                added.next = nodes[node].first;
                added.label = letter;
                nodes.push_back(added);
                nodes[node].first = child;
            }
            node = child;
        }
    }
    for (int node = static_cast<int>(nodes.size()) - 1; node >= 0; --node) {
        int child = nodes[node].first;
        if (!child) {
            nodes[node].leaves = 1;
            continue;
        }
        int total = 0, best_normal = 0, best_supplied = 0;
        while (child) {
            const int count = nodes[child].leaves;
            nodes[node].leaves += count;
            total += nodes[child].normal + count;
            const int saving = nodes[child].normal - nodes[child].supplied;
            best_normal = std::max(best_normal, saving);
            best_supplied = std::max(best_supplied, count + saving);
            child = nodes[child].next;
        }
        nodes[node].normal = total - best_normal;
        nodes[node].supplied = total - best_supplied;
    }
    return nodes[0].normal;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<std::string> words(count);
    for (auto &word : words)
        std::cin >> word;
    std::cout << minimum_clicks(words) << '\n';
}
