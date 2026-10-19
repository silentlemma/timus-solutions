#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int kOrientationCount = 4;
using Groups = std::array<std::vector<int>, 2>;

Groups fixedDirections(const std::vector<int> &values, int firstDirection, int secondDirection) {
    int size = static_cast<int>(values.size());
    std::array<int, 2> direction{firstDirection, secondDirection};
    std::array<int, 2> other{secondDirection == 1 ? 0 : size + 1,
                             firstDirection == 1 ? 0 : size + 1};
    std::array<std::vector<std::uint8_t>, 2> parent{std::vector<std::uint8_t>(size),
                                                    std::vector<std::uint8_t>(size)};
    int previous = values[0];
    for (int index = 1; index < size; ++index) {
        int value = values[index];
        std::array<int, 2> next{-1, -1};
        for (int owner = 0; owner < 2; ++owner) {
            if (other[owner] >= 0 && direction[owner] * (value - previous) > 0) {
                next[owner] = other[owner];
                parent[owner][index] = static_cast<std::uint8_t>(owner);
            }
            if (other[1 - owner] >= 0 && direction[owner] * (value - other[1 - owner]) > 0) {
                if (next[owner] < 0 || direction[1 - owner] * (previous - next[owner]) < 0) {
                    next[owner] = previous;
                    parent[owner][index] = static_cast<std::uint8_t>(1 - owner);
                }
            }
        }
        if (next[0] < 0 && next[1] < 0)
            return {};
        other = next;
        previous = value;
    }
    int owner = other[0] >= 0 ? 0 : 1;
    std::vector<int> assignment(size);
    std::array<int, 2> counts{};
    for (int index = size - 1; index >= 0; --index) {
        assignment[index] = owner;
        ++counts[owner];
        owner = parent[owner][index];
    }
    if (counts[0] == 0)
        assignment.back() = 0;
    if (counts[1] == 0)
        assignment.back() = 1;
    Groups groups;
    for (int index = 0; index < size; ++index)
        groups[assignment[index]].push_back(values[index]);
    return groups;
}

Groups partition(const std::vector<int> &values) {
    constexpr std::array<std::array<int, 2>, kOrientationCount> directions{
        {{{1, 1}}, {{-1, -1}}, {{1, -1}}, {{-1, 1}}}};
    for (const auto &direction : directions) {
        auto groups = fixedDirections(values, direction[0], direction[1]);
        if (!groups[0].empty())
            return groups;
    }
    return {};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<int> values(size);
    for (int &value : values)
        std::cin >> value;
    auto groups = partition(values);
    if (groups[0].empty()) {
        std::cout << "Fail\n";
    } else {
        std::cout << groups[0].size() << ' ' << groups[1].size() << '\n';
        for (const auto &group : groups) {
            for (int value : group)
                std::cout << value << ' ';
            std::cout << '\n';
        }
    }
}
