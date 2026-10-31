#include <cstdio>

int main() {
    long long population;
    int count;
    std::scanf("%lld%d", &population, &count);
    long long answer = population;
    // twenty deficits of at most one billion require a signed 64-bit sum.
    while (count--) {
        long long lower;
        std::scanf("%lld", &lower);
        answer -= population - lower;
    }
    std::printf("%lld\n", answer > 0 ? answer : 0);
}
