#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

constexpr int ALPHABET_SIZE = 26;
struct Node {
    std::array<int, ALPHABET_SIZE> next{};
    int length = 0, link = 0, diff = 0, series = 0;
    std::uint32_t cache = 0;
};

std::vector<std::uint32_t> solve(const std::string &word) {
    int n = static_cast<int>(word.size());
    std::string text(1, '\0');
    text += word;
    std::vector<Node> nodes;
    nodes.reserve(n + 2);
    nodes.emplace_back();
    nodes.emplace_back();
    nodes[0].length = -1;
    std::vector<std::uint32_t> dp(n + 1);
    dp[0] = 1;
    int last = 1;
    for (int i = 1; i <= n; ++i) {
        int parent = last, c = text[i] - 'a';
        while (text[i - 1 - nodes[parent].length] != text[i])
            parent = nodes[parent].link;
        if (nodes[parent].next[c] == 0) {
            int v = static_cast<int>(nodes.size());
            nodes[parent].next[c] = v;
            nodes.emplace_back();
            nodes[v].length = nodes[parent].length + 2;
            if (nodes[v].length == 1)
                nodes[v].link = 1;
            else {
                int candidate = nodes[parent].link;
                while (text[i - 1 - nodes[candidate].length] != text[i])
                    candidate = nodes[candidate].link;
                nodes[v].link = nodes[candidate].next[c];
            }
            int suffix = nodes[v].link;
            nodes[v].diff = nodes[v].length - nodes[suffix].length;
            nodes[v].series = nodes[v].diff == nodes[suffix].diff ? nodes[suffix].series : suffix;
        }
        last = nodes[parent].next[c];
        std::uint32_t value = 0;
        for (int v = last; nodes[v].length > 0; v = nodes[v].series) {
            int cut = i - nodes[nodes[v].series].length - nodes[v].diff;
            nodes[v].cache = dp[cut];
            int suffix = nodes[v].link;
            if (nodes[v].diff == nodes[suffix].diff)
                nodes[v].cache |= nodes[suffix].cache;
            value |= nodes[v].cache << 1;
        }
        dp[i] = value;
    }
    return dp;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    std::cin >> word;
    auto dp = solve(word);
    for (std::size_t i = 1; i < dp.size(); ++i)
        std::cout << (dp[i] >> 1) << '\n';
}
