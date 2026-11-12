#include <algorithm>
#include <cstdint>
#include <cstdio>

using namespace std;

const int CANS = 3;
const int BYTE_BITS = 8;
const int VALUES = 1 << BYTE_BITS;
const int FACE_SIZE = VALUES * VALUES;
const int FACE_COUNT = 2 * CANS;
const int WORD_BITS = 64;

int capacity[CANS];
uint64_t seen[FACE_COUNT * FACE_SIZE / WORD_BITS];
uint32_t states[FACE_COUNT * FACE_SIZE];
bool volumes[CANS * (VALUES - 1) + 1];

bool mark(const int *v) {
    for (int i = 0; i < CANS; ++i) {
        if (v[i] != 0 && v[i] != capacity[i])
            continue;
        int face = 2 * i + (v[i] != 0);
        int key = face * FACE_SIZE + v[(i + 1) % CANS] * VALUES + v[(i + 2) % CANS];
        uint64_t bit = uint64_t(1) << (key % WORD_BITS);
        if (seen[key / WORD_BITS] & bit)
            return false;
        seen[key / WORD_BITS] |= bit;
        return true;
    }
    return false;
}

int main() {
    for (int &c : capacity)
        scanf("%d", &c);
    int zero[CANS] = {};
    mark(zero);
    int tail = 1, answer = 0;
    for (int head = 0; head < tail; ++head) {
        uint32_t code = states[head];
        int v[CANS] = {int(code >> (2 * BYTE_BITS)), int(code >> BYTE_BITS & (VALUES - 1)),
                       int(code & (VALUES - 1))};
        for (int mask = 1; mask < (1 << CANS); ++mask) {
            int sum = 0;
            for (int i = 0; i < CANS; ++i)
                if (mask & (1 << i))
                    sum += v[i];
            if (sum && !volumes[sum]) {
                volumes[sum] = true;
                ++answer;
            }
        }
        for (int i = 0; i < CANS; ++i) {
            for (int j = -1; j < CANS; ++j) {
                if (i == j)
                    continue;
                int w[CANS] = {v[0], v[1], v[2]};
                if (j < 0) {
                    w[i] = capacity[i];
                } else {
                    int poured = min(v[i], capacity[j] - v[j]);
                    w[i] -= poured;
                    w[j] += poured;
                }
                if (mark(w))
                    states[tail++] = uint32_t(w[0]) << (2 * BYTE_BITS) |
                                     uint32_t(w[1]) << BYTE_BITS | uint32_t(w[2]);
            }
        }
    }
    printf("%d\n", answer);
}
