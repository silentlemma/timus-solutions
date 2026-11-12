#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr int FACES = 6, ROTATIONS = 24, PERMUTATIONS = 720;
constexpr int MAX_DICE = 100000, CLASSES = PERMUTATIONS / ROTATIONS;
constexpr uint8_t UNKNOWN = UINT8_MAX;
using Die = std::array<uint8_t, FACES>;
constexpr int TURNS[2][FACES] = {{3, 5, 2, 1, 4, 0}, {0, 1, 5, 2, 3, 4}};
Die rotations[ROTATIONS];
uint8_t kind[PERMUTATIONS], groups[CLASSES], members[MAX_DICE];

int rank(const Die &die) {
    int result = 0;
    for (int i = 0; i < FACES; ++i) {
        int smaller = 0;
        for (int j = i + 1; j < FACES; ++j)
            smaller += die[j] < die[i];
        result = result * (FACES - i) + smaller;
    }
    return result;
}

bool prepare() {
    for (int i = 0; i < FACES; ++i)
        rotations[0][i] = i;
    int used = 1;
    for (int i = 0; i < used; ++i) {
        for (const auto &turn : TURNS) {
            Die next;
            for (int face = 0; face < FACES; ++face)
                next[face] = rotations[i][turn[face]];
            if (std::find(rotations, rotations + used, next) == rotations + used) {
                if (used == ROTATIONS)
                    return false;
                rotations[used++] = next;
            }
        }
    }
    if (used != ROTATIONS)
        return false;
    std::fill(kind, kind + PERMUTATIONS, UNKNOWN);
    std::fill(groups, groups + CLASSES, UNKNOWN);
    Die die;
    for (int i = 0; i < FACES; ++i)
        die[i] = i + 1;
    int classes = 0;
    do {
        if (kind[rank(die)] != UNKNOWN)
            continue;
        for (const auto &rotation : rotations) {
            Die next;
            for (int face = 0; face < FACES; ++face)
                next[face] = die[rotation[face]];
            kind[rank(next)] = classes;
        }
        ++classes;
    } while (std::next_permutation(die.begin(), die.end()));
    return classes == CLASSES;
}

int main() {
    int n = number();
    if (!prepare())
        return 1;
    int used = 0;
    for (int i = 0; i < n; ++i) {
        Die die;
        for (auto &face : die)
            face = number();
        uint8_t key = kind[rank(die)];
        if (groups[key] == UNKNOWN)
            groups[key] = used++;
        members[i] = groups[key];
    }
    std::printf("%d\n", used);
    // At most thirty scans avoid storing indices and the complete output text.
    for (int group = 0; group < used; ++group) {
        bool first = true;
        for (int die = 0; die < n; ++die) {
            if (members[die] != group)
                continue;
            if (!first)
                std::putchar(' ');
            std::printf("%d", die + 1);
            first = false;
        }
        std::putchar('\n');
    }
}
