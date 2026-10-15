#include <cstdio>
#include <string>
#include <vector>

typedef unsigned __int128 Big;  // 30! < 2^128, so every count fits

const int EDGES = 30;
const int COLOURS = 30;
const int ROTATIONS = 60;
// the rotations other than the identity: how many there are and the cycle
// length on the edges; a half-turn also keeps two edges in place
const int FACE_TURNS = 24, FACE_CYCLE = 5;
const int VERTEX_TURNS = 20, VERTEX_CYCLE = 3;
const int HALF_TURNS = 15, HALF_CYCLE = 2;
const int BASE = 10;

// colourings of cycles of this length that use each colour counts[c]
// times, or 0 if some count does not split into whole cycles
Big cycles(const std::vector<int>& counts, int length) {
    Big ways = 1;
    int used = 0;
    for (int c : counts) {
        if (c % length != 0) {
            return 0;
        }
        for (int i = 1; i <= c / length; i++) {  // a binomial, one exact factor at a time
            used++;
            ways = ways * used / i;
        }
    }
    return ways;
}

int main() {
    std::vector<int> counts(COLOURS + 1, 0);
    for (int i = 0; i < EDGES; i++) {
        int c;
        scanf("%d", &c);
        counts[c]++;
    }
    Big total = cycles(counts, 1);
    total += FACE_TURNS * cycles(counts, FACE_CYCLE);
    total += VERTEX_TURNS * cycles(counts, VERTEX_CYCLE);
    // a half-turn: colour the two kept edges first, in order
    Big kept = 0;
    for (int a = 0; a <= COLOURS; a++) {
        for (int b = 0; b <= COLOURS; b++) {
            std::vector<int> rest = counts;
            rest[a]--;
            rest[b]--;
            if (rest[a] >= 0 && rest[b] >= 0) {
                kept += cycles(rest, HALF_CYCLE);
            }
        }
    }
    total += HALF_TURNS * kept;
    total /= ROTATIONS;
    std::string digits;
    do {
        digits.insert(digits.begin(), char('0' + (int)(total % BASE)));
        total /= BASE;
    } while (total > 0);
    printf("%s\n", digits.c_str());
}
