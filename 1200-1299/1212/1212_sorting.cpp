#include <algorithm>
#include <cstdint>
#include <cstdio>

using namespace std;

const int MAX_SHIPS = 30;
const int MAX_LENGTH = 4;
// Vertical ships exclude at most 6*6 anchors; horizontal ones at most 3*9.
const int MAX_ANCHORS = MAX_SHIPS * (MAX_LENGTH + 2) * (MAX_LENGTH + 2);

struct Zone {
    int top, bottom, left, right;
};

Zone zones[MAX_SHIPS];
uint32_t blocked[MAX_ANCHORS];
int ships, length;

long long countLines(int rows, int cols, bool flipped) {
    if (cols < length)
        return 0;
    int used = 0;
    for (int i = 0; i < ships; ++i) {
        const Zone &source = zones[i];
        Zone z = flipped ? Zone{source.left, source.right, source.top, source.bottom} : source;
        int top = max(1, z.top), bottom = min(rows, z.bottom);
        int left = max(1, z.left - length + 1), right = min(cols - length + 1, z.right);
        for (int row = top; row <= bottom; ++row)
            for (int col = left; col <= right; ++col)
                blocked[used++] = uint32_t((row - 1) * cols + col - 1);
    }
    sort(blocked, blocked + used);
    auto end = unique(blocked, blocked + used);
    return 1LL * rows * (cols - length + 1) - (end - blocked);
}

int main() {
    int rows, cols;
    scanf("%d %d %d", &rows, &cols, &ships);
    for (int i = 0; i < ships; ++i) {
        int col, row, size;
        char way;
        scanf("%d %d %d %c", &col, &row, &size, &way);
        int bottom = row + (way == 'V' ? size - 1 : 0);
        int right = col + (way == 'H' ? size - 1 : 0);
        zones[i] = {row - 1, bottom + 1, col - 1, right + 1};
    }
    scanf("%d", &length);
    long long answer = countLines(rows, cols, false);
    if (length > 1)
        answer += countLines(cols, rows, true);
    printf("%lld\n", answer);
}
