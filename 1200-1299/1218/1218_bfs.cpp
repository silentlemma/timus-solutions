#include <array>
#include <cstdio>

constexpr int MAX_JEDI = 200;
constexpr int NAME_CAPACITY = 31;
constexpr int PARAMETERS = 3;
constexpr int MAJORITY = 2;

struct Jedi {
    char name[NAME_CAPACITY];
    std::array<int, PARAMETERS> strength;
};

bool beats(const Jedi &a, const Jedi &b) {
    int stronger = 0;
    for (int i = 0; i < PARAMETERS; ++i) {
        stronger += a.strength[i] > b.strength[i];
    }
    return stronger >= MAJORITY;
}

int main() {
    int count;
    if (std::scanf("%d", &count) != 1 || count == 0) {
        return 0;
    }
    std::array<Jedi, MAX_JEDI> jedi;
    int leader = 0;
    for (int i = 0; i < count; ++i) {
        auto &j = jedi[i];
        std::scanf("%30s%d%d%d", j.name, &j.strength[0], &j.strength[1], &j.strength[2]);
        // A new leader reaches all earlier Jedi through the previous leader.
        if (i > 0 && beats(j, jedi[leader])) {
            leader = i;
        }
    }

    // Every Jedi who reaches the leader can also reach everyone the leader reaches.
    std::array<bool, MAX_JEDI> reaches_leader{};
    std::array<int, MAX_JEDI> queue;
    reaches_leader[leader] = true;
    queue[0] = leader;
    int end = 1;
    for (int head = 0; head < end; ++head) {
        const Jedi &next = jedi[queue[head]];
        for (int i = 0; i < count; ++i) {
            if (!reaches_leader[i] && beats(jedi[i], next)) {
                reaches_leader[i] = true;
                queue[end++] = i;
            }
        }
    }
    for (int i = 0; i < count; ++i) {
        if (reaches_leader[i]) {
            std::puts(jedi[i].name);
        }
    }
}
