#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

// counts are capped here: two ways already make the answer ambiguous
const int MANY = 2;

// whether digit c of the paper may be bit b
bool fits(char c, int b) { return c == '?' || c - '0' == b; }

int main() {
    std::ios::sync_with_stdio(false);
    std::string k, x;
    if (!(std::cin >> k >> x)) return 0;
    int n = k.size();
    // the Gray code of k has digit x(i) = k(i) xor k(i - 1), with a 0 before
    // the first digit; ways[b][i] counts the readings of the first i + 1
    // digits that end with k(i) = b
    std::vector<int> ways[2] = {std::vector<int>(n), std::vector<int>(n)};
    int w[2] = {1, 0};
    for (int i = 0; i < n; i++) {
        int next[2] = {0, 0};
        for (int cur = 0; cur < 2; cur++) {
            if (!fits(k[i], cur)) continue;
            for (int prev = 0; prev < 2; prev++) {
                if (fits(x[i], prev ^ cur)) next[cur] = std::min(MANY, next[cur] + w[prev]);
            }
        }
        for (int b = 0; b < 2; b++) ways[b][i] = w[b] = next[b];
    }
    if (w[0] + w[1] == 0) {
        std::cout << "Impossible\n";
        return 0;
    }
    if (w[0] + w[1] > 1) {
        std::cout << "Ambiguity\n";
        return 0;
    }
    // walk back along the single reading: exactly one earlier digit of k
    // with a reading of its own leads on to the next one
    std::string bits(n, '0'), code(n, '0');
    int cur = w[1] ? 1 : 0;
    bits[n - 1] = '0' + cur;
    for (int i = n - 1; i > 0; i--) {
        for (int prev = 0; prev < 2; prev++) {
            if (ways[prev][i - 1] && fits(x[i], prev ^ cur)) {
                bits[i - 1] = '0' + prev;
                code[i] = '0' + (prev ^ cur);
            }
        }
        cur = bits[i - 1] - '0';
    }
    code[0] = bits[0];
    std::cout << bits << "\n" << code << "\n";
    return 0;
}
