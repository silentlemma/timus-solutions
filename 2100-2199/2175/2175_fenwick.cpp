#include <cstdint>
#include <iostream>
#include <vector>

constexpr int ABSENT = -1;

class PrefixMaximum {
  public:
    explicit PrefixMaximum(const std::vector<std::int64_t> &values)
        : values_(values), tree_(values.size() + 1, ABSENT) {
        const int size = static_cast<int>(values.size());
        for (int node = 1; node <= size; ++node) {
            if (better(node - 1, tree_[node])) {
                tree_[node] = node - 1;
            }
            const int parent = node + (node & -node);
            if (parent <= size && better(tree_[node], tree_[parent])) {
                tree_[parent] = tree_[node];
            }
        }
    }

    int query(int end) const {
        int result = ABSENT;
        for (int node = end; node > 0; node -= node & -node) {
            if (better(tree_[node], result)) {
                result = tree_[node];
            }
        }
        return result;
    }

    void update(int position) {
        const int size = static_cast<int>(values_.size());
        for (int node = position + 1; node <= size; node += node & -node) {
            const int winner = tree_[node];
            // A stored index already sees its increased value, but ancestors may not.
            if (winner != position && !better(position, winner)) {
                break;
            }
            tree_[node] = position;
        }
    }

  private:
    bool better(int candidate, int current) const {
        return current == ABSENT || values_[candidate] > values_[current] ||
               (values_[candidate] == values_[current] && candidate < current);
    }

    const std::vector<std::int64_t> &values_;
    std::vector<int> tree_;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int size;
    std::cin >> size;
    std::vector<std::int64_t> values(size);
    for (std::int64_t &value : values) {
        std::cin >> value;
    }

    std::vector<int> next(size, ABSENT);
    int last = 0;
    int count = 1;
    next[0] = size;
    for (int position = 1; position < size; ++position) {
        if (values[position] > values[last]) {
            next[last] = position;
            next[position] = size;
            last = position;
            ++count;
        }
    }
    PrefixMaximum prefix(values);

    int queries;
    std::cin >> queries;
    while (queries-- > 0) {
        int position;
        std::int64_t increment;
        std::cin >> position >> increment;
        --position;
        if (increment == 0) {
            std::cout << count << '\n';
            continue;
        }
        values[position] += increment;
        if (next[position] == ABSENT) {
            const int previous = prefix.query(position);
            if (values[position] > values[previous]) {
                next[position] = next[previous];
                next[previous] = position;
                ++count;
            }
        }
        if (next[position] != ABSENT) {
            int following = next[position];
            while (following < size && values[following] <= values[position]) {
                const int removed = following;
                following = next[following];
                next[removed] = ABSENT;
                --count;
            }
            next[position] = following;
        }
        prefix.update(position);
        std::cout << count << '\n';
    }
}
