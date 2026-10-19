#include <iostream>
#include <string>

long long solve(const std::string &state) {
    constexpr int PEG_SUM = 3;
    int source = 0;
    long long answer = 0;
    for (int disk = static_cast<int>(state.size()) - 1; disk >= 0; --disk) {
        int target = state[disk] - 'A';
        if (target != source) {
            answer += 1LL << disk;
            source = PEG_SUM - source - target;
        }
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::string state;
    if (!(std::cin >> count >> state))
        return 0;
    std::cout << solve(state) << '\n';
    return 0;
}
