#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>

constexpr int MAX_VALUE = 1000000;

class SegmentTree {
    int size = 1;
    std::vector<int> maximum;

    int first(int node, int left, int right, int query_left, int query_right) const {
        if (right < query_left || query_right < left || maximum[node] < query_left) {
            return 0;
        }
        if (left == right) {
            return left;
        }
        int middle = (left + right) / 2;
        int answer = first(node * 2, left, middle, query_left, query_right);
        if (answer != 0) {
            return answer;
        }
        return first(node * 2 + 1, middle + 1, right, query_left, query_right);
    }

  public:
    explicit SegmentTree(const std::vector<int> &previous) {
        int count = static_cast<int>(previous.size()) - 1;
        while (size < count) {
            size *= 2;
        }
        maximum.resize(size * 2);
        for (int position = 1; position <= count; ++position) {
            maximum[size + position - 1] = previous[position];
        }
        for (int node = size - 1; node > 0; --node) {
            maximum[node] = std::max(maximum[node * 2], maximum[node * 2 + 1]);
        }
    }

    void update(int position, int value) {
        int node = size + position - 1;
        maximum[node] = value;
        while (node > 1) {
            node /= 2;
            int value = std::max(maximum[node * 2], maximum[node * 2 + 1]);
            if (maximum[node] == value) {
                break;
            }
            maximum[node] = value;
        }
    }

    int find(int left, int right) const { return first(1, 1, size, left, right); }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count, query_count;
    std::cin >> count >> query_count;
    std::vector<int> smallest(MAX_VALUE + 1);
    for (int prime = 2; prime <= MAX_VALUE; ++prime) {
        if (smallest[prime] != 0) {
            continue;
        }
        smallest[prime] = prime;
        if (prime > MAX_VALUE / prime) {
            continue;
        }
        for (int multiple = prime * prime; multiple <= MAX_VALUE; multiple += prime) {
            if (smallest[multiple] == 0) {
                smallest[multiple] = prime;
            }
        }
    }
    auto factors = [&](int value) {
        std::vector<int> result;
        while (value > 1) {
            int prime = smallest[value];
            result.push_back(prime);
            do {
                value /= prime;
            } while (value % prime == 0);
        }
        return result;
    };

    std::vector<int> values(count + 1), previous(count + 1);
    std::vector<std::set<int>> positions(MAX_VALUE + 1);
    for (int position = 1; position <= count; ++position) {
        std::cin >> values[position];
        for (int prime : factors(values[position])) {
            auto &occurrences = positions[prime];
            if (!occurrences.empty()) {
                previous[position] = std::max(previous[position], *occurrences.rbegin());
            }
            occurrences.insert(occurrences.end(), position);
        }
    }
    SegmentTree tree(previous);
    for (int query = 0; query < query_count; ++query) {
        int type, left, right;
        std::cin >> type >> left >> right;
        if (type == 1) {
            int second = tree.find(left, right);
            if (second == 0) {
                std::cout << -1 << '\n';
            } else {
                std::cout << previous[second] << ' ' << second << '\n';
            }
            continue;
        }
        int position = left;
        if (values[position] == right) {
            continue;
        }
        auto old_factors = factors(values[position]);
        auto new_factors = factors(right);
        std::vector<int> affected{position};
        // Only consecutive occurrences of a prime can change their predecessor.
        for (int prime : old_factors) {
            if (std::binary_search(new_factors.begin(), new_factors.end(), prime)) {
                continue;
            }
            auto &occurrences = positions[prime];
            auto current = occurrences.find(position);
            auto successor = std::next(current);
            if (successor != occurrences.end()) {
                affected.push_back(*successor);
            }
            occurrences.erase(current);
        }
        for (int prime : new_factors) {
            if (std::binary_search(old_factors.begin(), old_factors.end(), prime)) {
                continue;
            }
            auto &occurrences = positions[prime];
            auto successor = occurrences.lower_bound(position);
            if (successor != occurrences.end()) {
                affected.push_back(*successor);
            }
            occurrences.insert(successor, position);
        }
        values[position] = right;
        std::sort(affected.begin(), affected.end());
        affected.erase(std::unique(affected.begin(), affected.end()), affected.end());
        for (int changed : affected) {
            int best = 0;
            for (int prime : factors(values[changed])) {
                auto &occurrences = positions[prime];
                auto current = occurrences.lower_bound(changed);
                if (current != occurrences.begin()) {
                    best = std::max(best, *std::prev(current));
                }
            }
            previous[changed] = best;
            tree.update(changed, best);
        }
    }
}
