#include <iostream>
#include <vector>

constexpr long long MOD = 1000000007;

long long solve(int n, int a, int b) {
    std::vector<long long> ends_one(b + 1), ends_two(a + 1);
    ends_one[0] = ends_two[0] = 1;
    long long window_one = 1, window_two = 1, last_one = 0, last_two = 0;
    for (int length = 1; length <= n; ++length) {
        last_one = window_one;
        last_two = window_two;
        long long expired_two = length >= a ? ends_two[(length - a) % (a + 1)] : 0;
        long long expired_one = length >= b ? ends_one[(length - b) % (b + 1)] : 0;
        window_one = (window_one + last_two + MOD - expired_two) % MOD;
        window_two = (window_two + last_one + MOD - expired_one) % MOD;
        ends_one[length % (b + 1)] = last_one;
        ends_two[length % (a + 1)] = last_two;
    }
    return (last_one + last_two) % MOD;
}

int main() {
    int n, a, b;
    std::cin >> n >> a >> b;
    std::cout << solve(n, a, b) << '\n';
    return 0;
}
