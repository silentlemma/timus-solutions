#include <cstdint>
#include <iostream>
#include <vector>

using Mask = std::uint32_t;

void visit(Mask first, Mask last, Mask dimensions, std::vector<Mask> &answer) {
    if ((dimensions & (dimensions - 1)) == 0) {
        answer.push_back(first);
        if (last != first)
            answer.push_back(last);
        return;
    }
    Mask difference = first ^ last;
    Mask split = difference & -difference;
    Mask remaining = dimensions ^ split;
    Mask bridge = remaining & -remaining;
    if ((first ^ bridge ^ split) == last && remaining != bridge) {
        Mask choices = remaining ^ bridge;
        bridge = choices & -choices;
    }
    Mask middle = first ^ bridge;
    visit(first, middle, remaining, answer);
    visit(middle ^ split, last, remaining, answer);
}

std::vector<Mask> buildPath(Mask start, Mask finish, Mask free) {
    std::vector<Mask> answer;
    answer.reserve(Mask{1} << __builtin_popcount(free));
    visit(start, finish, free, answer);
    return answer;
}

Mask readMask() {
    int count;
    std::cin >> count;
    Mask mask = 0;
    for (int i = 0; i < count; ++i) {
        int bit;
        std::cin >> bit;
        mask |= Mask{1} << (bit - 1);
    }
    return mask;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int dimensions;
    std::cin >> dimensions;
    Mask start = readMask(), finish = readMask();
    auto path = buildPath(start, finish, (Mask{1} << dimensions) - 1);
    std::cout << path.size() << '\n';
    for (Mask mask : path) {
        std::cout << __builtin_popcount(mask);
        while (mask != 0) {
            Mask bit = mask & -mask;
            std::cout << ' ' << __builtin_ctz(bit) + 1;
            mask ^= bit;
        }
        std::cout << '\n';
    }
}
