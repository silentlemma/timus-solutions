#include <iostream>
#include <string>
#include <vector>

std::string s;
std::vector<std::vector<int>> best, cut; // cut > 0: split before s[cut]; < 0: -cut is the period

// the shortest folding of s[i..j]
std::string fold(int i, int j) {
    int c = cut[i][j];
    if (c > 0)
        return fold(i, c - 1) + fold(c, j);
    if (c < 0)
        return std::to_string((j - i + 1) / -c) + "(" + fold(i, i - c - 1) + ")";
    return s.substr(i, j - i + 1);
}

int main() {
    std::cin >> s;
    int n = s.size();
    best.assign(n, std::vector<int>(n));
    cut.assign(n, std::vector<int>(n, 0));
    for (int size = 1; size <= n; size++)
        for (int i = 0; i + size <= n; i++) {
            int j = i + size - 1;
            best[i][j] = size;
            for (int k = i + 1; k <= j; k++)
                if (best[i][k - 1] + best[k][j] < best[i][j]) {
                    best[i][j] = best[i][k - 1] + best[k][j];
                    cut[i][j] = k;
                }
            // a period p repeats when the segment equals itself shifted by p
            for (int p = 1; p < size; p++) {
                if (size % p != 0 || s.compare(i, size - p, s, i + p, size - p) != 0)
                    continue;
                int l = std::to_string(size / p).size() + 2 + best[i][i + p - 1];
                if (l < best[i][j])
                    best[i][j] = l, cut[i][j] = -p;
            }
        }
    std::cout << fold(0, n - 1) << "\n";
}
