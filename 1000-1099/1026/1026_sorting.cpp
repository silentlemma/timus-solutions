#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    std::cin >> n;
    std::vector<int> base(n);
    for (int &x : base)
        std::cin >> x;
    std::string separator;
    std::cin >> separator >> k;
    // the i-th smallest element is the i-th element of the sorted database
    std::sort(base.begin(), base.end());
    std::string out;
    for (int q = 0, i; q < k && std::cin >> i; q++)
        out += std::to_string(base[i - 1]) + "\n";
    std::cout << out;
}
