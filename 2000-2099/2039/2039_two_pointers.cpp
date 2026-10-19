#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int last_zero(const std::string &line, int from, int to) {
    while (to > from) {
        --to;
        if (line[to] == '0')
            return to;
    }
    return -1;
}

long long solve(const std::vector<std::string> &grid, int k) {
    const int n = static_cast<int>(grid.size());
    const int m = static_cast<int>(grid[0].size());
    if (k > std::min(n, m))
        return 0;
    std::vector<std::string> columns(m, std::string(n, '0'));
    for (int r = 0; r < n; ++r)
        for (int c = 0; c < m; ++c)
            columns[c][r] = grid[r][c];
    long long answer = 0;
    for (int diagonal = 1 - n; diagonal < m; ++diagonal) {
        const int r0 = std::max(0, -diagonal), c0 = std::max(0, diagonal);
        int start = 0, pivot_r = -1, pivot_c = -1, black_r = 0, black_c = 0;
        for (int at = 0; at < std::min(n - r0, m - c0); ++at) {
            const int r = r0 + at, c = c0 + at;
            while (true) {
                const int rs = r0 + start, cs = c0 + start;
                int last = last_zero(grid[r], cs, c);
                bool valid = last < 0 || pivot_r < 0 ||
                             grid[r].compare(cs, c - cs, grid[pivot_r], cs, c - cs) == 0;
                if (valid) {
                    int next_r = pivot_r, next_c = pivot_c;
                    if (last >= 0) {
                        next_r = r;
                        if (pivot_r < 0)
                            next_c = last;
                    }
                    int last_row = last_zero(columns[c], rs, r + 1);
                    valid =
                        last_row < 0 || next_r < 0 ||
                        columns[c].compare(rs, r - rs + 1, columns[next_c], rs, r - rs + 1) == 0;
                    if (valid) {
                        if (last_row >= 0) {
                            next_r = last_row;
                            next_c = c;
                        }
                        const int length = at - start + 1;
                        int nr, nc;
                        if (pivot_r >= 0) {
                            nr = black_r + (grid[r][next_c] == '1');
                            nc = black_c + (columns[c][next_r] == '1');
                        } else if (next_r < 0) {
                            nr = nc = length;
                        } else if (last >= 0) {
                            nr = length - 1;
                            nc = static_cast<int>(
                                std::count(grid[r].begin() + cs, grid[r].begin() + c + 1, '1'));
                        } else {
                            nr = static_cast<int>(std::count(columns[c].begin() + rs,
                                                             columns[c].begin() + r + 1, '1'));
                            nc = length - 1;
                        }
                        if (nr <= k && nc <= k) {
                            pivot_r = next_r;
                            pivot_c = next_c;
                            black_r = nr;
                            black_c = nc;
                            break;
                        }
                    }
                }
                const int old_size = at - start;
                if (pivot_r < 0 || pivot_r == rs || pivot_c == cs) {
                    pivot_r = pivot_c = -1;
                    black_r = black_c = old_size - 1;
                } else {
                    black_r -= grid[rs][pivot_c] == '1';
                    black_c -= grid[pivot_r][cs] == '1';
                }
                ++start;
            }
            const int bound = at - start + 1;
            if (bound >= k && (pivot_r < r - k + 1 || pivot_c < c - k + 1))
                ++answer;
            if (bound > k && black_r == k && black_c == k && pivot_r >= 0) {
                const int first_r = static_cast<int>(columns[pivot_c].find('1', r0 + start));
                const int first_c = static_cast<int>(grid[pivot_r].find('1', c0 + start));
                const int high =
                    std::min({at - k, first_r - r0, first_c - c0, pivot_r - r0, pivot_c - c0});
                if (high >= start)
                    answer += high - start + 1;
            }
        }
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m, k;
    if (!(std::cin >> n >> m >> k))
        return 0;
    std::vector<std::string> grid(n);
    for (auto &row : grid)
        std::cin >> row;
    std::cout << solve(grid, k) << '\n';
}
