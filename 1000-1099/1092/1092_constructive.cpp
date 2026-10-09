#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int n;
std::vector<std::vector<bool>> a;
std::vector<std::vector<int>> ops;

void flip(const std::vector<int> &perm) {
    ops.push_back(perm);
    for (int r = 0; r < n; r++)
        a[r][perm[r]] = !a[r][perm[r]];
}

void parities(std::vector<int> &rows, std::vector<int> &cols) {
    rows.clear(), cols.clear();
    for (int i = 0; i < n; i++) {
        int row = 0, col = 0;
        for (int j = 0; j < n; j++)
            row += a[i][j], col += a[j][i];
        if (row % 2)
            rows.push_back(i);
        if (col % 2)
            cols.push_back(i);
    }
}

int main() {
    int half;
    if (!(std::cin >> half))
        return 0;
    n = 2 * half + 1;
    a.assign(n, std::vector<bool>(n));
    for (int i = 0; i < n; i++) {
        std::string row;
        std::cin >> row;
        for (int j = 0; j < n; j++)
            a[i][j] = row[j] == '+';
    }
    // two transversals that differ in two rows flip the corners of a
    // rectangle, which keeps every row and column parity; one transversal
    // flips all the parities at once
    std::vector<int> rows, cols;
    parities(rows, cols);
    if ((int)std::max(rows.size(), cols.size()) == n) {
        std::vector<int> diagonal(n);
        for (int i = 0; i < n; i++)
            diagonal[i] = i;
        flip(diagonal);
        parities(rows, cols);
    }
    // the target keeps the parities with max(|rows|, |cols|) plus signs,
    // and the unmatched lines come in pairs and share line 0
    std::vector<std::vector<bool>> t(n, std::vector<bool>(n, false));
    size_t paired = std::min(rows.size(), cols.size());
    for (size_t k = 0; k < paired; k++)
        t[rows[k]][cols[k]] = true;
    for (size_t k = paired; k < rows.size(); k++)
        t[rows[k]][0] = !t[rows[k]][0];
    for (size_t k = paired; k < cols.size(); k++)
        t[0][cols[k]] = !t[0][cols[k]];
    int last = n - 1;
    for (int i = 0; i < last; i++)
        for (int j = 0; j < last; j++) {
            if (a[i][j] == t[i][j])
                continue;
            std::vector<int> perm(n), rest;
            for (int c = 0; c < n; c++)
                if (c != j && c != last)
                    rest.push_back(c);
            for (int r = 0, k = 0; r < n; r++)
                perm[r] = r == i ? j : r == last ? last : rest[k++];
            flip(perm);
            std::swap(perm[i], perm[last]);
            flip(perm);
        }
    std::string out = "There is solution:\n";
    for (const auto &perm : ops) {
        for (int r = 0; r < n; r++)
            out += std::to_string(perm[r] + 1) + (r + 1 < n ? " " : "\n");
    }
    std::cout << out;
}
