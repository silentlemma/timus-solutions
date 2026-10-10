#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    int m, n;
    if (!(std::cin >> m >> n))
        return 0;
    if (m == 0 || n == 0) {
        std::cout << std::string(m, '\n');
        return 0;
    }
    std::vector<std::string> final(m);
    for (auto &row : final)
        std::cin >> row;
    // row r as a bit mask of its cells visited an odd number of times
    std::vector<uint64_t> odd(m, 0);
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++) {
            long long visits;
            std::cin >> visits;
            odd[r] |= (uint64_t)(visits & 1) << c;
        }
    // the offsets of integer length, the cell itself included
    std::vector<std::pair<int, int>> offsets;
    for (int dr = 1 - m; dr < m; dr++)
        for (int dc = 1 - n; dc < n; dc++) {
            int q = dr * dr + dc * dc, root = (int)std::lround(std::sqrt((double)q));
            if (root * root == q)
                offsets.push_back({dr, dc});
        }
    uint64_t full = (1ULL << n) - 1;
    std::string out;
    for (int r = 0; r < m; r++) {
        // bit c is set when cell (r, c) was flipped an odd number of times
        uint64_t flips = 0;
        for (auto [dr, dc] : offsets)
            if (r + dr >= 0 && r + dr < m) {
                uint64_t row = odd[r + dr];
                flips ^= (dc >= 0 ? row >> dc : row << -dc) & full;
            }
        for (int c = 0; c < n; c++)
            out += ((final[r][c] == 'B') ^ (flips >> c & 1)) ? 'B' : 'W';
        out += '\n';
    }
    std::cout << out;
}
