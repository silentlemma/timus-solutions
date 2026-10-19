#include <iostream>
#include <stdexcept>
#include <vector>

constexpr int small_odd_limit = 5;
constexpr int first_odd_prime = 3;
constexpr int column = 2;

std::vector<std::vector<int>> construct(int n) {
    std::vector<std::vector<int>> grid(n, std::vector<int>(n));
    int value = 0;
    auto visit = [&](int row, int col) { grid[row][col] = ++value; };
    if (n % 2 && n < small_odd_limit) {
        for (int row = 0; row < n; ++row)
            for (int step = 0; step < n; ++step)
                visit(row, row % 2 ? n - 1 - step : step);
        return grid;
    }
    const int limit = n * n;
    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false;
    for (int p = 2; p * p <= limit; ++p)
        if (prime[p])
            for (int multiple = p * p; multiple <= limit; multiple += p)
                prime[multiple] = false;
    std::vector<int> following(limit + 1), widths(n);
    int largest = 0;
    for (int p = limit; p >= 0; --p) {
        following[p] = largest;
        if (prime[p])
            largest = p;
    }
    if (n % 2 == 0) {
        visit(0, 1);
        visit(0, 0);
        visit(1, 0);
        for (int row = 1; row < n - 2; row += 2) {
            const int width = (following[value] - value - 2) / 2;
            widths[row] = width;
            for (int col = 1; col <= width; ++col)
                visit(row, col);
            visit(row + 1, width);
            for (int col = width - 1; col >= 0; --col)
                visit(row + 1, col);
            visit(row + 2, 0);
        }
        for (int col = 1; col < n; ++col)
            visit(n - 1, col);
        for (int row = n - 2; row > 1; row -= 2) {
            const int width = widths[row - 1];
            for (int col = n - 1; col > width; --col)
                visit(row, col);
            for (int col = width + 1; col < n; ++col)
                visit(row - 1, col);
        }
        for (int col = n - 1; col > 1; --col)
            visit(0, col);
        return grid;
    }
    const int right_width = n - column - 1;
    int initial = -1;
    for (int candidate = 0; candidate <= right_width; ++candidate) {
        if (candidate == right_width - 1)
            continue;
        const int first = first_odd_prime + 2 * candidate;
        int current = first + 2 * n;
        if (!prime[first] || !prime[current])
            continue;
        bool valid = true;
        for (int row = n - 1; row > column + 1; row -= 2) {
            const int next_prime = following[current];
            const int width = (next_prime - current - 2) / 2;
            if (width < 0 || width >= right_width) {
                valid = false;
                break;
            }
            widths[row] = width;
            current = next_prime;
        }
        if (valid) {
            initial = candidate;
            break;
        }
    }
    if (initial < 0)
        throw std::logic_error("No admissible prime prefix");
    visit(1, 1);
    visit(1, column);
    for (int col = column + 1; col <= column + initial; ++col)
        visit(1, col);
    for (int col = column + initial; col >= column; --col)
        visit(0, col);
    visit(0, 1);
    visit(0, 0);
    visit(1, 0);
    visit(2, 0);
    visit(2, 1);
    for (int row = column + 1; row < n; row += 2) {
        visit(row, 1);
        visit(row, 0);
        visit(row + 1, 0);
        visit(row + 1, 1);
    }
    visit(n - 1, column);
    for (int row = n - 1; row > column + 1; row -= 2) {
        const int width = widths[row];
        for (int col = column + 1; col <= column + width; ++col)
            visit(row, col);
        visit(row - 1, column + width);
        for (int col = column + width - 1; col >= column; --col)
            visit(row - 1, col);
        visit(row - 2, column);
    }
    const int left = column + initial + 1;
    if (left == n) {
        for (int col = column + 1; col < n; ++col)
            visit(2, col);
    } else {
        for (int col = column + 1; col <= left; ++col)
            visit(2, col);
        visit(1, left);
        for (int col = left; col < n; ++col)
            visit(0, col);
        for (int col = n - 1; col > left; --col)
            visit(1, col);
        for (int col = left + 1; col < n; ++col)
            visit(2, col);
    }
    for (int row = column + 1; row < n; row += 2) {
        const int width = widths[row + 1];
        for (int col = n - 1; col > column + width; --col)
            visit(row, col);
        for (int col = column + width + 1; col < n; ++col)
            visit(row + 1, col);
    }
    return grid;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    for (const auto &row : construct(n)) {
        for (int col = 0; col < n; ++col)
            std::cout << (col ? " " : "") << row[col];
        std::cout << '\n';
    }
}
