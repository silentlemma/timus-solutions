#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int rows, columns;
    if (!(std::cin >> rows >> columns)) {
        return 0;
    }

    const int stride = columns + 1;
    std::vector<std::int64_t> row_prefix(rows * stride);
    std::vector<std::int64_t> diagonal_prefix((rows + 1) * stride);
    std::int64_t total = 0;
    for (int row = 0; row < rows; ++row) {
        for (int column = 0; column < columns; ++column) {
            std::int64_t value;
            std::cin >> value;
            row_prefix[row * stride + column + 1] = row_prefix[row * stride + column] + value;
            diagonal_prefix[(row + 1) * stride + column] =
                diagonal_prefix[row * stride + column + 1] + value;
            total += value;
        }
    }

    int queries;
    std::cin >> queries;
    const int maximum_distance = rows + columns - 2;
    while (queries-- > 0) {
        int wind;
        std::cin >> wind;
        if (wind >= maximum_distance) {
            std::cout << total << " 1 1\n";
            continue;
        }

        std::vector<std::int64_t> below(columns);
        std::int64_t best = -1;
        int best_row = rows;
        int best_column = columns;
        for (int row = rows - 1; row >= 0; --row) {
            const int last_row = std::min(rows - 1, row + wind + 1);
            for (int column = 0; column < columns; ++column) {
                const int right = std::min(columns, column + wind + 1);
                std::int64_t sum = below[column] + row_prefix[row * stride + right] -
                                   row_prefix[row * stride + column];

                // Moving up adds one row and removes the farthest anti-diagonal.
                const int diagonal = row + column + wind + 1;
                const int first_row = std::max(row + 1, diagonal - columns + 1);
                if (first_row <= last_row) {
                    sum -= diagonal_prefix[(last_row + 1) * stride + diagonal - last_row] -
                           diagonal_prefix[first_row * stride + diagonal - first_row + 1];
                }
                below[column] = sum;
                if (sum > best || (sum == best &&
                                   (row < best_row || (row == best_row && column < best_column)))) {
                    best = sum;
                    best_row = row;
                    best_column = column;
                }
            }
        }
        std::cout << best << ' ' << best_row + 1 << ' ' << best_column + 1 << '\n';
    }
}
