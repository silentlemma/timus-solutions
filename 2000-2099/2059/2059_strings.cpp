#include <iostream>
#include <string>
#include <vector>

constexpr int MAX_WORD_LENGTH = 200000;
constexpr int MAX_NODES = 2 * MAX_WORD_LENGTH + 2;
constexpr std::size_t OUTPUT_BATCH = 65536;

struct Tree {
    std::vector<int> length, link, first, next, label, count_a, count_b;
    int x = 0, y = 0, z = 0;
    Tree()
        : length(MAX_NODES), link(MAX_NODES), first(MAX_NODES), next(MAX_NODES), label(MAX_NODES),
          count_a(MAX_NODES), count_b(MAX_NODES) {
        length[0] = -1;
    }
    void solve(const std::string &a, const std::string &b) {
        x = y = z = 0;
        if (a.size() == 1 && b.size() == 1) {
            if (a == b)
                y = 1;
            else
                x = z = 1;
            return;
        }
        first[0] = first[1] = 0;
        count_a[0] = count_a[1] = count_b[0] = count_b[1] = 0;
        int nodes = 2;
        for (int pass = 0; pass < 2; ++pass) {
            const std::string &word = pass == 0 ? a : b;
            std::vector<int> &counts = pass == 0 ? count_a : count_b;
            int last = 1;
            for (int end = 0; end < static_cast<int>(word.size()); ++end) {
                int letter = static_cast<unsigned char>(word[end]), node = last;
                while (end - length[node] - 1 < 0 ||
                       static_cast<unsigned char>(word[end - length[node] - 1]) != letter)
                    node = link[node];
                int found = first[node];
                while (found != 0 && label[found] != letter)
                    found = next[found];
                if (found == 0) {
                    found = nodes++;
                    int size = length[node] + 2, suffix = 1;
                    if (size != 1) {
                        int candidate = link[node];
                        while (end - length[candidate] - 1 < 0 ||
                               static_cast<unsigned char>(word[end - length[candidate] - 1]) !=
                                   letter)
                            candidate = link[candidate];
                        suffix = first[candidate];
                        while (label[suffix] != letter)
                            suffix = next[suffix];
                    }
                    length[found] = size;
                    link[found] = suffix;
                    first[found] = 0;
                    next[found] = first[node];
                    label[found] = letter;
                    first[node] = found;
                    count_a[found] = count_b[found] = 0;
                }
                last = found;
                ++counts[found];
            }
        }
        for (int node = nodes - 1; node >= 2; --node) {
            int ca = count_a[node], cb = count_b[node], suffix = link[node];
            count_a[suffix] += ca;
            count_b[suffix] += cb;
            if (ca > cb)
                ++x;
            else if (ca == cb)
                ++y;
            else
                ++z;
        }
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string line;
    std::getline(std::cin, line);
    int tests = std::stoi(line);
    Tree tree;
    std::string output;
    for (int index = 1; index <= tests; ++index) {
        std::string a, b;
        std::getline(std::cin, a);
        std::getline(std::cin, b);
        if (!a.empty() && a.back() == '\r')
            a.pop_back();
        if (!b.empty() && b.back() == '\r')
            b.pop_back();
        tree.solve(a, b);
        output += "Case #" + std::to_string(index) + ": " + std::to_string(tree.x) + " " +
                  std::to_string(tree.y) + " " + std::to_string(tree.z) + "\n";
        if (output.size() >= OUTPUT_BATCH) {
            std::cout << output;
            output.clear();
        }
    }
    std::cout << output;
}
