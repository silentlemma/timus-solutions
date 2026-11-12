#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using Money = long long;

struct Block {
    int size = 0;
    Money sum = 0, added = 0;
};

class Salaries {
    int width;
    std::vector<Money> values;
    std::vector<Block> blocks;

  public:
    explicit Salaries(int count)
        : width(static_cast<int>(std::ceil(std::sqrt(count)))), values(count),
          blocks((count + width - 1) / width) {}

    void put(int index, Money salary) {
        values[index] = salary;
        Block &block = blocks[index / width];
        block.sum += salary;
        ++block.size;
    }

    Money get(int index) const { return values[index] + blocks[index / width].added; }

    Money sum(int left, int right) const {
        Money total = 0;
        while (left < right) {
            int id = left / width;
            const Block &block = blocks[id];
            int stop = std::min(right, id * width + block.size);
            if (stop - left == block.size) {
                total += block.sum;
            } else {
                total += (stop - left) * block.added;
                for (int i = left; i < stop; ++i) {
                    total += values[i];
                }
            }
            left = stop;
        }
        return total;
    }

    void add(int left, int right, Money amount) {
        while (left < right) {
            int id = left / width;
            Block &block = blocks[id];
            int stop = std::min(right, id * width + block.size);
            block.sum += (stop - left) * amount;
            if (stop - left == block.size) {
                block.added += amount;
            } else {
                for (int i = left; i < stop; ++i) {
                    values[i] += amount;
                }
            }
            left = stop;
        }
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int employees, updates;
    std::cin >> employees >> updates;
    std::vector<int> parent(employees), size(employees, 1), first(employees), next(employees, 1);
    std::vector<Money> initial(employees);
    std::cin >> initial[0];
    for (int employee = 1; employee < employees; ++employee) {
        std::cin >> parent[employee] >> initial[employee];
    }
    for (int employee = employees - 1; employee > 0; --employee) {
        size[parent[employee]] += size[employee];
    }
    // Reserve one contiguous range for each child of a department.
    for (int employee = 1; employee < employees; ++employee) {
        int boss = parent[employee];
        first[employee] = next[boss];
        next[boss] += size[employee];
        next[employee] = first[employee] + 1;
    }

    Salaries salaries(employees);
    for (int employee = 0; employee < employees; ++employee) {
        salaries.put(first[employee], initial[employee]);
    }
    for (int i = 0; i < updates; ++i) {
        std::string kind;
        int employee;
        Money threshold, amount;
        std::cin >> kind >> employee >> threshold >> amount;
        int count = kind == "employee" ? 1 : size[employee];
        int left = first[employee], right = left + count;
        if (salaries.sum(left, right) < threshold * count) {
            salaries.add(left, right, amount);
        }
    }
    for (int employee = 0; employee < employees; ++employee) {
        std::cout << salaries.get(first[employee]) << '\n';
    }
}
