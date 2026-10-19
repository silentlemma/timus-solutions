#include <algorithm>
#include <iostream>

constexpr int PRIME_THREE = 3;
constexpr int PRIME_FIVE = 5;
constexpr int MAX_THREE_WEIGHT = 3;
constexpr int FIVE_WEIGHT = 4;

int hall(int value, int groups) {
    const int primes[] = {2, PRIME_THREE, PRIME_FIVE};
    const int weights[] = {1, std::min(groups - 1, MAX_THREE_WEIGHT), FIVE_WEIGHT};
    int color = 0, index = 0;
    for (int prime : primes) {
        while (value % prime == 0) {
            value /= prime;
            color += weights[index];
        }
        ++index;
    }
    return color % groups + 1;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, groups;
    std::cin >> size >> groups;
    std::cout << "Yes\n";
    for (int index = 0; index < size; ++index) {
        int value;
        std::cin >> value;
        std::cout << hall(value, groups) << '\n';
    }
    return 0;
}
