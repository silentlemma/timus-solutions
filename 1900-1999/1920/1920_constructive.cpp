#include <iostream>
#include <utility>
#include <vector>

void insertEar(std::vector<int> &successor, int first, int second, int outerFirst,
               int outerSecond) {
    if (successor[first] != second) {
        std::swap(first, second);
        std::swap(outerFirst, outerSecond);
    }
    successor[first] = outerFirst;
    successor[outerFirst] = outerSecond;
    successor[outerSecond] = second;
}

std::vector<int> constructCycle(int size, int length) {
    if (length % 2 || length > size * size - size % 2) {
        return {};
    }
    std::vector<int> successor(size * size, -1);
    std::vector<int> initial = {0, 1, size + 1, size};
    for (int index = 0; index < static_cast<int>(initial.size()); ++index) {
        successor[initial[index]] = initial[(index + 1) % initial.size()];
    }
    int used = static_cast<int>(initial.size());
    int width = size - size % 2;
    for (int column = 2; column < width && used < length; ++column) {
        insertEar(successor, column - 1, size + column - 1, column, size + column);
        used += 2;
    }
    for (int row = 2; row < size && used < length; ++row) {
        for (int column = 0; column < width && used < length; column += 2) {
            int upper = (row - 1) * size + column;
            int lower = row * size + column;
            insertEar(successor, upper, upper + 1, lower, lower + 1);
            used += 2;
        }
    }
    if (size % 2) {
        for (int row = 0; row < size - 1 && used < length; row += 2) {
            int left = row * size + width - 1;
            insertEar(successor, left, left + size, left + 1, left + size + 1);
            used += 2;
        }
    }
    std::vector<int> result;
    int current = 0;
    for (int index = 0; index < length; ++index) {
        result.push_back(current);
        current = successor[current];
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, length;
    std::cin >> size >> length;
    auto cycle = constructCycle(size, length);
    if (cycle.empty()) {
        std::cout << "Unsuitable device\n";
    } else {
        std::cout << "Overwhelming power of magic\n";
        for (int vertex : cycle) {
            std::cout << vertex / size + 1 << ' ' << vertex % size + 1 << '\n';
        }
    }
    return 0;
}
