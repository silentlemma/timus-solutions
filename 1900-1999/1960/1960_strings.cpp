#include <array>
#include <iostream>
#include <string>
#include <vector>

constexpr int ALPHABET_SIZE = 26;
constexpr int EMPTY_ROOT = 1;
constexpr int ROOT_COUNT = 2;

struct Node {
    int length = 0, link = 0;
    std::array<int, ALPHABET_SIZE> next{};
};

std::vector<int> distinctCounts(const std::string &text) {
    std::vector<Node> nodes(text.size() + ROOT_COUNT);
    nodes[0].length = -1;
    int nodeCount = ROOT_COUNT, last = EMPTY_ROOT;
    std::vector<int> answer;
    answer.reserve(text.size());
    for (int position = 0; position < static_cast<int>(text.size()); ++position) {
        const char letter = text[position];
        const int code = letter - 'a';
        int parent = last;
        while (true) {
            const int left = position - nodes[parent].length - 1;
            if (left >= 0 && text[left] == letter)
                break;
            parent = nodes[parent].link;
        }
        int node = nodes[parent].next[code];
        if (node == 0) {
            node = nodeCount++;
            nodes[node].length = nodes[parent].length + 2;
            nodes[parent].next[code] = node;
            if (nodes[node].length == 1)
                nodes[node].link = EMPTY_ROOT;
            else {
                int candidate = nodes[parent].link;
                while (true) {
                    const int left = position - nodes[candidate].length - 1;
                    if (left >= 0 && text[left] == letter)
                        break;
                    candidate = nodes[candidate].link;
                }
                nodes[node].link = nodes[candidate].next[code];
            }
        }
        last = node;
        answer.push_back(nodeCount - ROOT_COUNT);
    }
    return answer;
}

void printCounts(const std::vector<int> &values) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i != 0)
            std::cout << ' ';
        std::cout << values[i];
    }
    std::cout << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string text;
    if (!(std::cin >> text))
        return 0;
    printCounts(distinctCounts(text));
}
