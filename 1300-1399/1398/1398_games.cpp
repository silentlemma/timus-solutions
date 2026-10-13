#include <algorithm>
#include <cstdio>
#include <cstring>

const int BLACK = 0, DRAW = 1, WHITE = 2; // results, better for white upwards
const int SIZE = 8;
const int SECOND = 6; // the black pawn may move two squares from rank 7
const int DIAGONALS[][2] = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

int memo[2][SIZE][SIZE][SIZE][SIZE]; // memo[turn][bf][br][pf][pr], -1 when unknown

bool inside(int f, int r) { return f >= 0 && f < SIZE && r >= 0 && r < SIZE; }

// can the bishop reach square (qf, qr) on an otherwise empty board?
bool sees(int bf, int br, int qf, int qr) {
    for (auto &d : DIAGONALS)
        for (int f = bf + d[0], r = br + d[1]; inside(f, r); f += d[0], r += d[1])
            if (f == qf && r == qr)
                return true;
    return false;
}

int black(int bf, int br, int pf, int pr);

int white(int bf, int br, int pf, int pr) {
    int &m = memo[0][bf][br][pf][pr];
    if (m >= 0)
        return m;
    int best = BLACK;
    for (auto &d : DIAGONALS)
        for (int f = bf + d[0], r = br + d[1]; inside(f, r); f += d[0], r += d[1]) {
            if (f == pf && r == pr)
                return m = WHITE; // the bishop takes the pawn
            best = std::max(best, black(f, r, pf, pr));
        }
    return m = best;
}

int black(int bf, int br, int pf, int pr) {
    int &m = memo[1][bf][br][pf][pr];
    if (m >= 0)
        return m;
    int best = WHITE + 1; // no move yet
    if (br == pr - 1 && (bf == pf - 1 || bf == pf + 1))
        best = BLACK; // the pawn takes the bishop and cannot be stopped
    if (!(bf == pf && br == pr - 1)) {
        if (pr - 1 == 0)
            // a queen: white wins only by taking it at once
            best = std::min(best, sees(bf, br, pf, 0) ? WHITE : BLACK);
        else {
            best = std::min(best, white(bf, br, pf, pr - 1));
            if (pr == SECOND && !(bf == pf && br == pr - 2))
                best = std::min(best, white(bf, br, pf, pr - 2));
        }
    }
    return m = best > WHITE ? DRAW : best; // a blocked pawn is a draw
}

int main() {
    char bf, br, pf, pr; // the squares as a letter and a digit each
    scanf(" %c%c %c%c", &bf, &br, &pf, &pr);
    memset(memo, -1, sizeof memo);
    int result = white(bf - 'a', br - '1', pf - 'a', pr - '1');
    const char *names[] = {"BLACK", "DRAW", "WHITE"};
    printf("%s\n", names[result]);
}
