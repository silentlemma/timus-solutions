#include <algorithm>
#include <iostream>
#include <vector>

struct Point {
    long long x, y;
    int id;
};

std::vector<int> chain_sizes(const std::vector<Point> &p, const std::vector<int> &left,
                             const std::vector<int> &right, const std::vector<int> &order,
                             const std::vector<int> &size, int turn) {
    int n = static_cast<int>(p.size());
    std::vector<int> head(n + 1, n), tail(n + 1, n), count(n + 1);
    std::vector<int> previous(n, n), following(n, n);
    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        int v = *it, a = left[v], b = right[v];
        bool forward = size[a] >= size[b];
        int base = forward ? a : b, small = forward ? b : a;
        auto &back = forward ? previous : following;
        auto &ahead = forward ? following : previous;
        int start = forward ? head[base] : tail[base];
        int end = forward ? tail[base] : head[base];
        int other = forward ? head[small] : tail[small];
        int sign = forward ? turn : -turn, length = count[base];
        // Reuse the larger subtree's chain and insert from its nearer end.
        for (int c = v; c != n;) {
            int next = c == v ? other : ahead[c];
            while (length >= 2) {
                a = back[end];
                long long cross = (p[end].x - p[a].x) * (p[c].y - p[a].y) -
                                  (p[end].y - p[a].y) * (p[c].x - p[a].x);
                if (cross * sign > 0) {
                    break;
                }
                end = a;
                --length;
            }
            if (length) {
                ahead[end] = c;
            } else {
                start = c;
            }
            back[c] = end;
            ahead[c] = n;
            end = c;
            ++length;
            c = next;
        }
        head[v] = forward ? start : end;
        tail[v] = forward ? end : start;
        count[v] = length;
    }
    return count;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<Point> p(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> p[i].x >> p[i].y;
        p[i].id = i;
    }
    std::sort(p.begin(), p.end(), [](const Point &a, const Point &b) { return a.x < b.x; });
    std::vector<int> left(n, n), right(n, n), stack;
    for (int v = 0; v < n; ++v) {
        int last = n;
        while (!stack.empty() && p[stack.back()].y < p[v].y) {
            last = stack.back();
            stack.pop_back();
        }
        left[v] = last;
        if (!stack.empty()) {
            right[stack.back()] = v;
        }
        stack.push_back(v);
    }
    int root = stack.front();
    stack.assign(1, root);
    std::vector<int> order, size(n + 1);
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        order.push_back(v);
        if (left[v] != n) {
            stack.push_back(left[v]);
        }
        if (right[v] != n) {
            stack.push_back(right[v]);
        }
    }
    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        int v = *it;
        size[v] = size[left[v]] + size[right[v]] + 1;
    }
    auto lower = chain_sizes(p, left, right, order, size, 1);
    auto upper = chain_sizes(p, left, right, order, size, -1);
    std::vector<int> answer(n);
    for (int v = 0; v < n; ++v) {
        answer[p[v].id] = std::max(1, lower[v] + upper[v] - 2);
    }
    for (int value : answer) {
        std::cout << value << '\n';
    }
}
