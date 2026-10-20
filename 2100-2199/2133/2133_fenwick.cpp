#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

constexpr int QUERY = -1;

struct Operation {
    int index;
    int height;
};

class Fenwick {
  public:
    explicit Fenwick(std::vector<int> counts) : tree(std::move(counts)) {
        for (int index = 1; index < static_cast<int>(tree.size()); ++index) {
            int parent = index + (index & -index);
            if (parent < static_cast<int>(tree.size())) {
                tree[parent] += tree[index];
            }
        }
    }

    void add(int index, int delta) {
        while (index < static_cast<int>(tree.size())) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int prefix(int index) const {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index &= index - 1;
        }
        return result;
    }

    void replace(int old_height, int new_height, int weight) {
        if (old_height != new_height) {
            add(old_height, -weight);
            add(new_height, weight);
        }
    }

  private:
    std::vector<int> tree;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> heights(n);
    std::vector<int> values;
    for (int &height : heights) {
        std::cin >> height;
        values.push_back(height);
    }

    int q;
    std::cin >> q;
    std::vector<Operation> operations(q);
    for (Operation &operation : operations) {
        int type;
        std::cin >> type;
        operation.index = QUERY;
        if (type == 1) {
            std::cin >> operation.index;
            --operation.index;
        }
        std::cin >> operation.height;
        values.push_back(operation.height);
    }

    std::sort(values.begin(), values.end());
    values.erase(std::unique(values.begin(), values.end()), values.end());
    auto rank = [&values](int height) {
        return static_cast<int>(std::lower_bound(values.begin(), values.end(), height) -
                                values.begin()) +
               1;
    };
    for (int &height : heights) {
        height = rank(height);
    }
    for (Operation &operation : operations) {
        operation.height = rank(operation.height);
    }

    std::vector<int> counts(values.size() + 1);
    for (int index = 0; index < n; ++index) {
        ++counts[heights[index]];
        if (index > 0) {
            --counts[std::min(heights[index - 1], heights[index])];
        }
    }
    Fenwick fenwick(std::move(counts));

    // Active buildings minus active adjacent pairs equals the number of runs.
    for (const Operation &operation : operations) {
        int index = operation.index;
        int height = operation.height;
        if (index == QUERY) {
            std::cout << 1 - fenwick.prefix(height - 1) << '\n';
            continue;
        }

        int old_height = heights[index];
        if (old_height == height) {
            continue;
        }
        fenwick.replace(old_height, height, 1);
        if (index > 0) {
            fenwick.replace(std::min(old_height, heights[index - 1]),
                            std::min(height, heights[index - 1]), -1);
        }
        if (index + 1 < n) {
            fenwick.replace(std::min(old_height, heights[index + 1]),
                            std::min(height, heights[index + 1]), -1);
        }
        heights[index] = height;
    }
}
