#include <iostream>
#include <vector>

using Integer = long long;
constexpr Integer MODULUS = 1000000007;

Integer power(Integer value, int exponent) {
    Integer result = 1;
    while (exponent > 0) {
        if (exponent & 1) {
            result = result * value % MODULUS;
        }
        value = value * value % MODULUS;
        exponent >>= 1;
    }
    return result;
}

std::vector<Integer> settingsCounts(int size) {
    std::vector<Integer> ways(size + 1);
    for (int count = 1; count <= size; ++count) {
        Integer closed = 0;
        for (int prefix = 1; prefix < count; ++prefix) {
            closed = (closed * count + ways[prefix]) % MODULUS;
        }
        const Integer difference = (power(count, count - 1) - closed + MODULUS) % MODULUS;
        ways[count] = count * difference % MODULUS;
    }
    return ways;
}

int main() {
    int size;
    std::cin >> size;
    std::cout << settingsCounts(size)[size] << '\n';
    return 0;
}
