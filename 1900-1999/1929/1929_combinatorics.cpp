#include <iostream>

constexpr int TEAM_SIZE = 3;

int waysToChoose(int available, int count) {
    if (count < 0 || count > available) {
        return 0;
    }
    if (count == 0) {
        return 1;
    }
    if (count == 1) {
        return available;
    }
    return available * (available - 1) / 2;
}

int countTeams(int total, int specialCount, int firstSpecial) {
    const int special = specialCount - firstSpecial;
    const int ordinary = total - specialCount - (1 - firstSpecial);
    const int remainingTeams = total / TEAM_SIZE - 1;
    int answer = 0;
    for (int chosenSpecial = 0; chosenSpecial < TEAM_SIZE; ++chosenSpecial) {
        const int removedSpecial = firstSpecial + chosenSpecial;
        if (removedSpecial == 0 || specialCount - removedSpecial < remainingTeams) {
            continue;
        }
        answer += waysToChoose(special, chosenSpecial) *
                  waysToChoose(ordinary, TEAM_SIZE - 1 - chosenSpecial);
    }
    return answer;
}

int main() {
    int total, specialCount;
    std::cin >> total >> specialCount;
    int firstSpecial = 0;
    for (int i = 0; i < specialCount; ++i) {
        int identifier;
        std::cin >> identifier;
        if (identifier == 1) {
            firstSpecial = 1;
        }
    }
    std::cout << countTeams(total, specialCount, firstSpecial) << '\n';
    return 0;
}
