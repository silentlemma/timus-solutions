#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using Integer = std::int64_t;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, q;
    std::cin >> n >> q;
    std::vector<Integer> x(n), y(n), prefix(n + 1), removed(n + 1);
    for (int i = 0; i < n; ++i) {
        std::cin >> x[i] >> y[i];
    }
    auto cross = [&](int a, int b) { return x[a] * y[b] - y[a] * x[b]; };
    for (int i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + cross(i, (i + 1) % n);
    }
    Integer total = prefix[n];
    auto sum = [&](int end) {
        Integer result = 0;
        for (; end > 0; end -= end & -end) {
            result += removed[end];
        }
        return result;
    };
    while (q-- > 0) {
        char type;
        int left, right;
        std::cin >> type >> left >> right;
        --left;
        --right;
        if (left > right) {
            std::swap(left, right);
        }
        Integer part = prefix[right] - prefix[left] + cross(right, left);
        part -= sum(right) - sum(left);
        Integer other = total - part;
        Integer answer = std::max(part, other);
        if (type == 'c') {
            answer = std::min(part, other);
            // Charge the discarded area to the first edge of its original arc.
            int edge = part < other ? left : right;
            for (int i = edge + 1; i <= n; i += i & -i) {
                removed[i] += answer;
            }
            total -= answer;
        }
        std::cout << answer / 2 << (answer % 2 == 0 ? ".0\n" : ".5\n");
    }
}
