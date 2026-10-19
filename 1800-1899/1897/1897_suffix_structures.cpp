#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

constexpr int BYTE_VALUES = 256;
constexpr int LETTERS = 26;
constexpr int PREFIX_KEY_BITS = 60;
constexpr int NODES_PER_CHARACTER = 4;

struct Node {
    int depth, first, next, parent, terminal, representative;
    bool parity, winning;
};

class GameIndex {
    string text, combined;
    int n, size, alphabet_size, prefix_bits, prefix_pairs;
    vector<int> order, rank, compact, logs;
    vector<vector<int>> table;
    vector<Node> nodes;
    vector<int> roots, counts;
    bool empty_winning;

    void build_suffix_array() {
        order.resize(size);
        rank.resize(size);
        vector<int> count(max(size, BYTE_VALUES)), shifted(size), following(size);
        for (int i = 0; i < size; ++i) ++count[rank[i] = combined[i]];
        for (int i = 1; i < BYTE_VALUES; ++i) count[i] += count[i - 1];
        for (int i = size - 1; i >= 0; --i) order[--count[rank[i]]] = i;
        int classes = BYTE_VALUES;
        for (int distance = 1;; distance *= 2) {
            int used = 0;
            for (int i = max(0, size - distance); i < size; ++i) shifted[used++] = i;
            for (int i : order) {
                if (i >= distance) shifted[used++] = i - distance;
            }
            fill(count.begin(), count.begin() + classes, 0);
            for (int i : shifted) ++count[rank[i]];
            for (int i = 1; i < classes; ++i) count[i] += count[i - 1];
            for (int i = size - 1; i >= 0; --i) order[--count[rank[shifted[i]]]] = shifted[i];
            classes = 1;
            following[order[0]] = 0;
            for (int i = 1; i < size; ++i) {
                int a = order[i - 1], b = order[i];
                int second_a = a + distance < size ? rank[a + distance] : -1;
                int second_b = b + distance < size ? rank[b + distance] : -1;
                if (rank[a] != rank[b] || second_a != second_b) ++classes;
                following[b] = classes - 1;
            }
            rank.swap(following);
            if (classes == size) break;
        }
        vector<int> lcp(size);
        for (int position = 0, height = 0; position < size; ++position) {
            int place = rank[position];
            if (place == 0) {
                height = 0;
                continue;
            }
            int other = order[place - 1];
            while (position + height < size && other + height < size
                   && combined[position + height] == combined[other + height]) ++height;
            lcp[place] = height;
            if (height) --height;
        }
        table.push_back(move(lcp));
        for (int span = 1; 2 * span <= size; span *= 2) {
            const auto& previous = table.back();
            vector<int> row(size - 2 * span + 1);
            for (int i = 0; i < static_cast<int>(row.size()); ++i) {
                row[i] = min(previous[i], previous[i + span]);
            }
            table.push_back(move(row));
        }
        logs.resize(size + 1);
        for (int i = 2; i <= size; ++i) logs[i] = logs[i / 2] + 1;
    }

    int lce(int a, int b) const {
        if (a == b) return size - a;
        int left = rank[a], right = rank[b];
        if (left > right) swap(left, right);
        int level = logs[right - left];
        return min(table[level][left + 1], table[level][right - (1 << level) + 1]);
    }

    int radius(int center, int parity) const { return min(center, n - center - parity); }

    int common(int a, int b, int parity) const {
        int cap = min(radius(a, parity), radius(b, parity));
        if (cap == 0) return 0;
        return min({cap, lce(2 * n + 1 - a, 2 * n + 1 - b), lce(a + parity, b + parity)});
    }

    int compare(int a, int b, int parity) const {
        int shared = common(a, b, parity);
        int cap = min(radius(a, parity), radius(b, parity));
        if (shared == cap) {
            int ra = radius(a, parity), rb = radius(b, parity);
            return (ra > rb) - (ra < rb);
        }
        char left_a = text[a - shared - 1], left_b = text[b - shared - 1];
        if (left_a != left_b) return left_a < left_b ? -1 : 1;
        return text[a + shared + parity] < text[b + shared + parity] ? -1 : 1;
    }

    int new_node(int depth, int parity, int center = -1) {
        int node = static_cast<int>(nodes.size());
        nodes.push_back({depth, -1, -1, -1, center, -1, parity != 0, false});
        return node;
    }

    void attach(int parent, int child) {
        nodes[child].parent = parent;
        nodes[child].next = nodes[parent].first;
        nodes[parent].first = child;
    }

    int build_centers(vector<int> centers, int parity) {
        int root = new_node(0, parity);
        vector<uint64_t> keys(n);
        for (int center : centers) {
            uint64_t key = 0;
            int cap = radius(center, parity);
            for (int offset = 0; offset < prefix_pairs; ++offset) {
                key <<= prefix_bits;
                if (offset < cap) {
                    key += compact[text[center - offset - 1]] * alphabet_size;
                    key += compact[text[center + offset + parity]] + 1;
                }
            }
            keys[center] = key;
        }
        sort(centers.begin(), centers.end(), [&](int a, int b) { return keys[a] < keys[b]; });
        for (int begin = 0; begin < static_cast<int>(centers.size());) {
            int end = begin + 1;
            while (end < static_cast<int>(centers.size())
                   && keys[centers[end]] == keys[centers[begin]]) {
                ++end;
            }
            sort(centers.begin() + begin, centers.begin() + end,
                 [&](int a, int b) { return compare(a, b, parity) < 0; });
            begin = end;
        }
        vector<int> stack{root};
        int previous_center = -1;
        for (int center : centers) {
            int shared = previous_center < 0 ? 0 : common(previous_center, center, parity);
            int last = -1;
            while (nodes[stack.back()].depth > shared) {
                int popped = stack.back();
                stack.pop_back();
                if (last != -1) attach(popped, last);
                last = popped;
            }
            if (nodes[stack.back()].depth < shared) {
                int node = new_node(shared, parity);
                attach(node, last);
                stack.push_back(node);
            } else if (last != -1) {
                attach(stack.back(), last);
            }
            int cap = radius(center, parity);
            if (cap > nodes[stack.back()].depth) {
                stack.push_back(new_node(cap, parity, center));
            } else {
                auto& node = nodes[stack.back()];
                int old = node.terminal;
                if (old < 0 || rank[center - cap] < rank[old - cap]) node.terminal = center;
            }
            previous_center = center;
        }
        while (stack.size() > 1) {
            int child = stack.back();
            stack.pop_back();
            attach(stack.back(), child);
        }
        return root;
    }

public:
    int64_t total = 0;

    explicit GameIndex(string source) : text(move(source)), n(static_cast<int>(text.size())) {
        combined = text + '#';
        combined.append(text.rbegin(), text.rend());
        size = static_cast<int>(combined.size());
        compact.assign(BYTE_VALUES, -1);
        alphabet_size = 0;
        for (char letter = 'a'; letter <= 'z'; ++letter) {
            if (text.find(letter) != string::npos) compact[letter] = alphabet_size++;
        }
        prefix_bits = 0;
        for (int value = alphabet_size * alphabet_size; value; value >>= 1) ++prefix_bits;
        prefix_pairs = alphabet_size > 1 ? PREFIX_KEY_BITS / prefix_bits : 1;
        build_suffix_array();
        nodes.reserve(NODES_PER_CHARACTER * n + LETTERS + 1);
        vector<int> even(n - 1);
        iota(even.begin(), even.end(), 1);
        roots.push_back(build_centers(move(even), 0));
        vector<vector<int>> groups(LETTERS);
        for (int c = 0; c < n; ++c) groups[text[c] - 'a'].push_back(c);
        for (auto& centers : groups) {
            if (!centers.empty()) roots.push_back(build_centers(move(centers), 1));
        }
        vector<int> traversal, stack = roots;
        while (!stack.empty()) {
            int node = stack.back();
            stack.pop_back();
            traversal.push_back(node);
            for (int child = nodes[node].first; child != -1; child = nodes[child].next) {
                stack.push_back(child);
            }
        }
        for (auto it = traversal.rbegin(); it != traversal.rend(); ++it) {
            auto& node = nodes[*it];
            int best = node.terminal;
            for (int child = node.first; child != -1; child = nodes[child].next) {
                const auto& next = nodes[child];
                bool immediate = next.winning ^ ((next.depth - node.depth - 1) & 1);
                if (!immediate) node.winning = true;
                int center = next.representative;
                if (best < 0 || rank[center - node.depth] < rank[best - node.depth]) best = center;
            }
            node.representative = best;
        }
        counts.assign(n + 2, 0);
        for (const auto& node : nodes) {
            if (node.parent == -1) {
                if (node.parity && node.winning) {
                    ++counts[node.representative];
                    --counts[node.representative + 2];
                }
                continue;
            }
            int low = nodes[node.parent].depth + 1, high = node.depth;
            int wanted = (node.representative - ((high + 1 - node.winning) & 1)) & 1;
            int left = node.representative - high, right = node.representative - low;
            if ((left & 1) != wanted) ++left;
            if ((right & 1) != wanted) --right;
            if (left <= right) {
                ++counts[left];
                --counts[right + 2];
            }
        }
        for (int i = 2; i < n; ++i) counts[i] += counts[i - 2];
        empty_winning = nodes[roots[0]].winning;
        total = empty_winning;
        for (int i = 0; i < n; ++i) total += counts[i];
    }

    string kth(int64_t k) const {
        if (k > total) return "no solution";
        if (empty_winning) {
            if (k == 1) return "-";
            --k;
        }
        int start = -1;
        for (int position : order) {
            if (position >= n) continue;
            if (k > counts[position]) k -= counts[position];
            else {
                start = position;
                break;
            }
        }
        vector<int> lengths;
        for (const auto& node : nodes) {
            if (node.parent == -1) {
                if (node.parity && node.winning && node.representative == start) {
                    lengths.push_back(1);
                }
            } else {
                int radius = node.representative - start;
                if (nodes[node.parent].depth < radius && radius <= node.depth
                    && (node.winning ^ ((node.depth - radius) & 1))) {
                    lengths.push_back(2 * radius + node.parity);
                }
            }
        }
        sort(lengths.begin(), lengths.end());
        return text.substr(start, lengths[k - 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string text;
    int64_t k;
    cin >> text >> k;
    cout << GameIndex(text).kth(k) << '\n';
}
