#include <cmath>
#include <cstdio>
#include <vector>

int main() {
    std::vector<unsigned long long> nums;
    unsigned long long x;
    while (scanf("%llu", &x) == 1)
        nums.push_back(x);
    for (auto it = nums.rbegin(); it != nums.rend(); ++it)
        printf("%.4f\n", std::sqrt(static_cast<double>(*it)));
    return 0;
}
