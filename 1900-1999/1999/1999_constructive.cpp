#include <array>
#include <iostream>
#include <vector>

constexpr int BASE = 10;

struct Machine {
    std::vector<int> terminal;
    std::vector<std::array<int, BASE>> rows;
};

Machine construct(const std::vector<std::array<int, BASE>> &old, const std::vector<int> &flags,
                  int offset) {
    int n = static_cast<int>(old.size()), stride = n + 1;
    std::vector<int> identifiers(2 * n * stride, -1), keys{2 * n};
    identifiers[keys[0]] = 0;
    Machine result;
    for (std::size_t head = 0; head < keys.size(); ++head) {
        int key = keys[head], pair = key / 2, normal = pair / stride, previous = pair % stride;
        result.terminal.push_back(key & 1);
        std::array<int, BASE> row{};
        for (int digit = 0; digit < BASE; ++digit) {
            int nextNormal = old[normal][digit];
            int nextPrevious =
                digit > 0 ? old[normal][digit - 1] : (previous == n ? n : old[previous][BASE - 1]);
            int accepted = 0;
            if (digit >= offset)
                accepted = flags[old[normal][digit - offset]];
            else if (previous != n)
                accepted = flags[old[previous][digit + BASE - offset]];
            int target = 2 * (nextNormal * stride + nextPrevious) + accepted;
            if (identifiers[target] < 0) {
                identifiers[target] = static_cast<int>(keys.size());
                keys.push_back(target);
            }
            row[digit] = identifiers[target];
        }
        result.rows.push_back(row);
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int offset, n;
    std::cin >> offset >> n;
    std::vector<int> flags(n);
    for (int &flag : flags)
        std::cin >> flag;
    std::vector<std::array<int, BASE>> old(n);
    for (auto &row : old)
        for (int &target : row) {
            std::cin >> target;
            --target;
        }
    Machine result = construct(old, flags, offset);
    std::cout << "Success\n" << result.rows.size() << '\n';
    for (std::size_t i = 0; i < result.terminal.size(); ++i)
        std::cout << (i ? " " : "") << result.terminal[i];
    std::cout << '\n';
    for (auto row : result.rows) {
        for (int digit = 0; digit < BASE; ++digit)
            std::cout << (digit ? " " : "") << row[digit] + 1;
        std::cout << '\n';
    }
}
