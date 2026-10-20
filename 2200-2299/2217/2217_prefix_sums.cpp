#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::string s;
    std::cin >> n >> s;
    if (n % 2 == 0 && std::count(s.begin(), s.end(), '0') % 2 != 0) {
        std::cout << "NO\n";
        return 0;
    }

    int balance = 0;
    for (int i = 0; i < n / 2; ++i) {
        // A zero can move left, so the suffix must supply at least as many zeros.
        balance += (s[n - 1 - i] == '0') - (s[i] == '0');
        if (balance < 0) {
            std::cout << "NO\n";
            return 0;
        }
    }
    std::cout << "YES\n";
}
