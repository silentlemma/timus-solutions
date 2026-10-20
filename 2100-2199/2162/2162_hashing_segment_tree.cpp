#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

constexpr int64_t LABEL_BASE = 1000000001;

struct EdgeHash {
    static constexpr uint64_t INCREMENT = 0x9e3779b97f4a7c15;
    static constexpr uint64_t FIRST_MULTIPLIER = 0xbf58476d1ce4e5b9;
    static constexpr uint64_t SECOND_MULTIPLIER = 0x94d049bb133111eb;
    static constexpr int FIRST_SHIFT = 30;
    static constexpr int SECOND_SHIFT = 27;
    static constexpr int FINAL_SHIFT = 31;

    size_t operator()(uint64_t value) const {
        static const uint64_t salt = chrono::steady_clock::now().time_since_epoch().count();
        value += salt + INCREMENT;
        value = (value ^ (value >> FIRST_SHIFT)) * FIRST_MULTIPLIER;
        value = (value ^ (value >> SECOND_SHIFT)) * SECOND_MULTIPLIER;
        return value ^ (value >> FINAL_SHIFT);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int size;
    cin >> size;
    vector<int> values(size);
    for (int &value : values) {
        cin >> value;
    }

    vector<int> good_until(size, size);
    for (int offset = 0; offset < 2; ++offset) {
        unordered_map<int64_t, int, EdgeHash> next_edge;
        next_edge.reserve(size);
        int limit = size;
        for (int position = size - 2 - offset; position >= 0; position -= 2) {
            int first = values[position];
            int second = values[position + 1];
            if (first == 0 || second == 0 || first == second) {
                limit = position;
            } else {
                int64_t key = min(first, second) * LABEL_BASE + max(first, second);
                auto found = next_edge.find(key);
                if (found != next_edge.end()) {
                    limit = min(limit, found->second);
                }
                next_edge[key] = position;
            }
            // The first forbidden pair is excluded from a valid edge block.
            good_until[position] = limit;
        }
    }

    int leaf_count = 1;
    while (leaf_count < size) {
        leaf_count *= 2;
    }
    vector<int> tree(2 * leaf_count, 0);
    copy(values.begin(), values.end(), tree.begin() + leaf_count);
    for (int node = leaf_count - 1; node > 0; --node) {
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int answer = 0;
    for (int start = 0; start + 1 < size; ++start) {
        int vertices = values[start];
        int edges = values[start + 1];
        if (vertices == 0 || edges > (size - start - 2) / 2) {
            continue;
        }
        if (edges == 0) {
            ++answer;
            continue;
        }
        int end = start + 2 + 2 * edges;
        if (end > good_until[start + 2]) {
            continue;
        }

        int left = leaf_count + start + 2;
        int right = leaf_count + end;
        int maximum = 0;
        while (left < right) {
            if (left % 2 == 1) {
                maximum = max(maximum, tree[left++]);
            }
            if (right % 2 == 1) {
                maximum = max(maximum, tree[--right]);
            }
            left /= 2;
            right /= 2;
        }
        if (maximum <= vertices) {
            ++answer;
        }
    }
    cout << answer << '\n';
}
