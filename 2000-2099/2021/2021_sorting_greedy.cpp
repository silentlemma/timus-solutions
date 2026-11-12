#include <algorithm>
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

constexpr int MAX_PLAYERS = 1000, SCORES = 7, TEAMS = 2;
uint16_t head[TEAMS][SCORES], next_id[TEAMS][MAX_PLAYERS + 1];

int take(int team, int &score, int step) {
    while (head[team][score] == 0)
        score += step;
    int id = head[team][score];
    head[team][score] = next_id[team][id];
    return id;
}

int main() {
    int n = number(), totals[TEAMS] = {};
    for (int team = 0; team < TEAMS; ++team) {
        for (int id = 1; id <= n; ++id) {
            int score = number();
            totals[team] += score;
            next_id[team][id] = head[team][score];
            head[team][score] = id;
        }
    }
    int step[TEAMS] = {1, 1}, score[TEAMS] = {};
    if (totals[0] > totals[1]) {
        step[1] = -1;
        score[1] = SCORES - 1;
    } else if (totals[0] < totals[1]) {
        step[0] = -1;
        score[0] = SCORES - 1;
    }
    for (int round = 0; round < n; ++round) {
        int first = take(0, score[0], step[0]), second = take(1, score[1], step[1]);
        std::printf("%d %d\n", first, second);
    }
}
