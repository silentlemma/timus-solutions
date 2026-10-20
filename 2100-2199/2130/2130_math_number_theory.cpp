#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    constexpr std::uint64_t MAX_VALUE = 1'000'000'000'000;
    int count;
    if (!(std::cin >> count)) {
        return 0;
    }

    std::uint64_t multiple = 1;
    std::vector<std::uint64_t> forbidden;
    forbidden.reserve(count);
    bool possible = true;

    for (int index = 0; index < count; ++index) {
        std::uint64_t divisor;
        int answer;
        std::cin >> divisor >> answer;

        if (possible) {
            if (answer == 0) {
                if (multiple % divisor == 0) {
                    possible = false;
                } else {
                    forbidden.push_back(divisor);
                }
            } else {
                const std::uint64_t factor = divisor / std::gcd(multiple, divisor);
                if (multiple > MAX_VALUE / factor) {
                    possible = false;
                } else if (factor != 1) {
                    multiple *= factor;
                    // Each scan follows a growth by at least a factor of two.
                    for (const std::uint64_t denied : forbidden) {
                        if (multiple % denied == 0) {
                            possible = false;
                            break;
                        }
                    }
                }
            }
        }

        if (possible) {
            std::cout << multiple << '\n';
        } else {
            std::cout << -1 << '\n';
        }
    }
}
