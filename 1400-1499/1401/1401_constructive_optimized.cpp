#include <cstdio>

const int MAX_EXPONENT = 9;
const int MAX_SIDE = 1 << MAX_EXPONENT;
// n <= 9 gives a board of at most 512 by 512 and labels at most 87381.
int board[MAX_SIDE][MAX_SIDE];
int count = 0;

// recursion needs only n stack frames; reverse quarters keep the simple numbering.
void tile(int top, int left, int side, int hr, int hc) {
    int label = ++count, half = side / 2;
    for (int dr = 1; dr >= 0; --dr)
        for (int dc = 1; dc >= 0; --dc) {
            int r0 = top + dr * half, c0 = left + dc * half, r, c;
            if (r0 <= hr && hr < r0 + half && c0 <= hc && hc < c0 + half) {
                r = hr;
                c = hc;
            } else {
                r = top + half - 1 + dr;
                c = left + half - 1 + dc;
                board[r][c] = label;
            }
            if (half > 1)
                tile(r0, c0, half, r, c);
        }
}

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    int size = 1 << n;
    tile(0, 0, size, x - 1, y - 1);
    // stream the board instead of retaining another full copy as text.
    for (int r = 0; r < size; ++r)
        for (int c = 0; c < size; ++c)
            printf("%d%c", board[r][c], c + 1 < size ? ' ' : '\n');
}
