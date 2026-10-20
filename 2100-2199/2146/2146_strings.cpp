#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

constexpr int LETTERS = 26;

int main() {
    std::ios::sync_with_stdio(false);
    int n, k;
    std::string s;
    std::cin >> n >> k >> s;
    // On a circle every period can be replaced by its gcd with n, so only the
    // divisors of n are tried, from the smallest.
    for (int d = 1; d <= n; d++) {
        if (n % d != 0) continue;
        std::vector<int> count(d * LETTERS, 0);
        for (int i = 0; i < n; i++) count[(i % d) * LETTERS + (s[i] - 'a')]++;
        std::vector<char> best(d);
        int changes = n;
        for (int r = 0; r < d; r++) {
            int top = 0;
            for (int c = 1; c < LETTERS; c++)
                if (count[r * LETTERS + c] > count[r * LETTERS + top]) top = c;
            best[r] = (char)('a' + top);
            changes -= count[r * LETTERS + top];
        }
        if (changes <= k) {
            for (int i = 0; i < n; i++) s[i] = best[i % d];
            std::cout << d << '\n' << s << '\n';
            return 0;
        }
    }
    return 0;
}
