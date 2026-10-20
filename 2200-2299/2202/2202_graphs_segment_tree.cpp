#include <algorithm>
#include <array>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

constexpr int UNSEEN = -1;

struct SegmentTree {
    int size = 1;
    int absent;
    vector<int> low, high;

    explicit SegmentTree(const vector<int> &mate) : absent(static_cast<int>(mate.size())) {
        while (size < absent) {
            size *= 2;
        }
        low.assign(2 * size, absent);
        high.assign(2 * size, UNSEEN);
        for (int i = 0; i < absent; ++i) {
            low[size + i] = high[size + i] = mate[i];
        }
        for (int i = size - 1; i > 0; --i) {
            pull(i);
        }
    }

    void pull(int node) {
        low[node] = min(low[2 * node], low[2 * node + 1]);
        high[node] = max(high[2 * node], high[2 * node + 1]);
    }

    void erase(int position) {
        int node = size + position;
        low[node] = absent;
        high[node] = UNSEEN;
        while ((node /= 2) > 0) {
            pull(node);
        }
    }

    int crossing(int left, int right) const {
        int first = size + left + 1;
        int last = size + right;
        while (first < last) {
            if (first & 1) {
                if (low[first] < left) {
                    return low[first];
                }
                if (high[first] > right) {
                    return high[first];
                }
                ++first;
            }
            if (last & 1) {
                --last;
                if (low[last] < left) {
                    return low[last];
                }
                if (high[last] > right) {
                    return high[last];
                }
            }
            first /= 2;
            last /= 2;
        }
        return UNSEEN;
    }
};

int region(int x, int y, int width, int height) {
    if (x < 0 || x > width || y < 0 || y > height) {
        return UNSEEN;
    }
    return x > 0 && x < width && y > 0 && y < height ? 1 : 0;
}

int perimeter(int x, int y, int width, int height) {
    if (y == 0) {
        return x;
    }
    if (x == width) {
        return width + y;
    }
    if (y == height) {
        return 2 * width + height - x;
    }
    return 2 * (width + height) - y;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, width, height;
    cin >> n >> width >> height;
    vector<pair<int, int>> events;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        int x, y, u, v;
        cin >> x >> y >> u >> v;
        int first = region(x, y, width, height);
        int second = region(u, v, width, height);
        if (first * second == UNSEEN) {
            cout << "NO\n";
            return 0;
        }
        if (first == 0 && second == 0) {
            events.emplace_back(perimeter(x, y, width, height), count);
            events.emplace_back(perimeter(u, v, width, height), count);
            ++count;
        }
    }
    sort(events.begin(), events.end());
    int endpoints = static_cast<int>(events.size());
    vector<int> left(count, UNSEEN), right(count), owner(endpoints), mate(endpoints);
    for (int position = 0; position < endpoints; ++position) {
        int id = events[position].second;
        owner[position] = id;
        if (left[id] == UNSEEN) {
            left[id] = position;
        } else {
            right[id] = position;
        }
    }
    for (int id = 0; id < count; ++id) {
        mate[left[id]] = right[id];
        mate[right[id]] = left[id];
    }

    SegmentTree tree(mate);
    vector<int> color(count, UNSEEN), queue;
    queue.reserve(count);
    for (int root = 0; root < count; ++root) {
        if (color[root] != UNSEEN) {
            continue;
        }
        queue.clear();
        queue.push_back(root);
        color[root] = 0;
        tree.erase(left[root]);
        tree.erase(right[root]);
        // Find a spanning forest without listing every crossing.
        for (size_t head = 0; head < queue.size(); ++head) {
            int id = queue[head];
            int witness;
            while ((witness = tree.crossing(left[id], right[id])) != UNSEEN) {
                int next = owner[witness];
                color[next] = color[id] ^ 1;
                tree.erase(left[next]);
                tree.erase(right[next]);
                queue.push_back(next);
            }
        }
    }

    // Each side must have a properly nested boundary matching.
    array<vector<int>, 2> stacks;
    for (int position = 0; position < endpoints; ++position) {
        int id = owner[position];
        auto &stack = stacks[color[id]];
        if (position == left[id]) {
            stack.push_back(id);
        } else if (stack.empty() || stack.back() != id) {
            cout << "NO\n";
            return 0;
        } else {
            stack.pop_back();
        }
    }
    cout << "YES\n";
}
