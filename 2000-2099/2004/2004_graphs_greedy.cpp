#include <iostream>
#include <string>
#include <vector>

std::string solve(int order) {
    int size = 1 << order;
    int mask = size - 1;
    std::vector<unsigned char> seen(size, 0);
    seen[0] = 1;
    std::string result(order, '0');
    result.reserve(size + order - 1);
    int window = 0;
    for (int step = 0; step < size - 1; ++step) {
        window = (window << 1) & mask;
        if (!seen[window | 1]) {
            window |= 1;
            result.push_back('1');
        } else {
            result.push_back('0');
        }
        seen[window] = 1;
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int order;
    std::cin >> order;
    std::cout << solve(order) << '\n';
}
