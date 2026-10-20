#include <algorithm>
#include <cstdint>
#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m, a, b;
    std::cin >> n >> m >> a >> b;
    std::int64_t row_total = 0, column_total = 0;
    std::int64_t selected_row = 0, selected_column = 0;
    for (int i = 1; i <= n; ++i) {
        std::int64_t value;
        std::cin >> value;
        row_total += value;
        if (i == a) {
            selected_row = value;
        }
    }
    for (int j = 1; j <= m; ++j) {
        std::int64_t value;
        std::cin >> value;
        column_total += value;
        if (j == b) {
            selected_column = value;
        }
    }

    if (row_total != column_total) {
        std::cout << 0 << '\n';
        return 0;
    }
    const auto lower = std::max<std::int64_t>(0, selected_row + selected_column - row_total);
    const auto upper = std::min(selected_row, selected_column);
    std::cout << upper - lower + 1 << '\n';
}
