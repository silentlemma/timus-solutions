#include <algorithm>
#include <iostream>
#include <string>

const std::string TAIL = "bcd";

std::string word_for(int n, int count, const std::string &tail) {
    int alphabet = static_cast<int>(TAIL.size());
    if (count < std::min(n, alphabet))
        return "NO";
    if (n < alphabet)
        return std::string(n, 'a');
    int prefix = count - alphabet;
    return std::string(prefix, 'a') + tail.substr(0, n - prefix);
}

void solve(int n) {
    std::string tail;
    while (static_cast<int>(tail.size()) < n)
        tail += TAIL;
    for (int count = 1; count <= n; ++count)
        std::cout << count << " : " << word_for(n, count, tail) << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    solve(n);
}
