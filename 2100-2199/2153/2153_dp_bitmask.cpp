#include <array>
#include <iostream>
#include <string>

constexpr int ROLE_COUNT = 4;
constexpr int MASK_COUNT = 1 << ROLE_COUNT;
const std::string ROLE_CODES = "WMCR";
const std::array<std::string, ROLE_COUNT> ROLE_NAMES = {"warrior", "mage", "cleric", "rogue"};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int member_count;
    std::cin >> member_count;
    std::array<bool, MASK_COUNT> reachable{};
    reachable[0] = true;

    for (int member = 0; member < member_count; ++member) {
        std::string qualifications;
        std::cin >> qualifications;
        int skills = 0;
        for (int role = 0; role < ROLE_COUNT; ++role) {
            if (qualifications.find(ROLE_CODES[role]) != std::string::npos) {
                skills |= 1 << role;
            }
        }

        // Every extension has a larger mask, so this member is used at most once.
        for (int mask = MASK_COUNT - 1; mask >= 0; --mask) {
            if (!reachable[mask]) {
                continue;
            }
            for (int role = 0; role < ROLE_COUNT; ++role) {
                int bit = 1 << role;
                if ((skills & bit) != 0 && (mask & bit) == 0) {
                    reachable[mask | bit] = true;
                }
            }
        }
    }

    std::array<int, MASK_COUNT> sizes{};
    int best = 0;
    int common = MASK_COUNT - 1;
    for (int mask = 0; mask < MASK_COUNT; ++mask) {
        sizes[mask] = sizes[mask >> 1] + (mask & 1);
        if (!reachable[mask]) {
            continue;
        }
        if (sizes[mask] > best) {
            best = sizes[mask];
            common = mask;
        } else if (sizes[mask] == best) {
            common &= mask;
        }
    }

    std::cout << best << '\n';
    if (best < ROLE_COUNT) {
        std::cout << "Looking for";
        for (int role = 0; role < ROLE_COUNT; ++role) {
            if ((common & (1 << role)) == 0) {
                std::cout << ' ' << ROLE_NAMES[role];
            }
        }
        std::cout << '\n';
    }
}
