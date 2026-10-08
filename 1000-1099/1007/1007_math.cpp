#include <iostream>
#include <string>

// Weight of a word: the sum of the positions (from 1) of its ones.
long long weight(const std::string &s) {
    long long w = 0;
    for (size_t i = 0; i < s.size(); i++)
        if (s[i] == '1')
            w += i + 1;
    return w;
}

std::string restore(std::string s, int n) {
    int mod = n + 1, len = s.size();
    long long w = weight(s);
    if (len == n) {
        // a raised zero at position p adds exactly p to the weight
        if (w % mod != 0)
            s[w % mod - 1] = '0';
        return s;
    }
    // onesAfter: ones to the right of the changed place; they shift by one
    long long onesAfter = 0;
    if (len == n - 1) {
        for (int i = len; i >= 0; i--) {
            for (char d = '0'; d <= '1'; d++)
                if ((w + onesAfter + (d - '0') * (i + 1)) % mod == 0)
                    return s.insert(i, 1, d);
            if (i > 0)
                onesAfter += s[i - 1] == '1';
        }
    } else {
        for (int i = len - 1; i >= 0; i--) {
            if ((w - onesAfter - (s[i] - '0') * (i + 1)) % mod == 0)
                return s.erase(i, 1);
            onesAfter += s[i] == '1';
        }
    }
    return s;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::string s, out;
    while (std::cin >> s)
        out += restore(s, n) + '\n';
    std::cout << out;
}
