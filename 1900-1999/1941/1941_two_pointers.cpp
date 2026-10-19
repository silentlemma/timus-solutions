#include <iostream>
#include <sstream>
#include <string>
#include <vector>

constexpr int LOWEST_SYMBOL = 33;
constexpr int SYMBOL_COUNT = 90;
constexpr int ALPHABET_SIZE = SYMBOL_COUNT * SYMBOL_COUNT * SYMBOL_COUNT;

int encode(const std::string &token) {
    return ((token[0] - LOWEST_SYMBOL) * SYMBOL_COUNT + token[1] - LOWEST_SYMBOL) * SYMBOL_COUNT +
           token[2] - LOWEST_SYMBOL;
}

class WindowCounter {
    std::vector<int> deficit;
    std::vector<int> ring;
    int missing;
    int position = 0;
    int used = 0;

  public:
    explicit WindowCounter(const std::vector<int> &pattern)
        : deficit(ALPHABET_SIZE), ring(pattern.size()), missing(static_cast<int>(pattern.size())) {
        for (int code : pattern)
            ++deficit[code];
    }

    bool push(int code) {
        if (used == static_cast<int>(ring.size())) {
            const int old = ring[position];
            if (deficit[old] >= 0)
                ++missing;
            ++deficit[old];
        } else {
            ++used;
        }
        if (deficit[code] > 0)
            --missing;
        --deficit[code];
        ring[position] = code;
        if (++position == static_cast<int>(ring.size()))
            position = 0;
        return missing == 0;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string line, token;
    std::getline(std::cin, line);
    std::istringstream input(line);
    std::vector<int> pattern;
    while (input >> token)
        pattern.push_back(encode(token));
    WindowCounter counter(pattern);
    int answer = 0;
    while (std::cin >> token)
        answer += counter.push(encode(token));
    std::cout << answer << '\n';
    return 0;
}
