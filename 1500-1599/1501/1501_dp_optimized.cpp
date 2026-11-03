#include <cstdint>
#include <cstdio>

const int MAX_LENGTH = 1000;
const int INPUT_FIELDS = 3;
std::int16_t first[MAX_LENGTH + 1], second[MAX_LENGTH + 1];
bool forward[MAX_LENGTH + 1], backward[MAX_LENGTH + 1];
char moves[2 * MAX_LENGTH + 1];
int used;

bool frontier(bool *row, int a0, int a1, int b0, int b1, int step) {
    int width = (b1 - b0) * step;
    for (int t = 0; t <= width; t++)
        row[t] = false;
    row[0] = true;
    for (int i = a0;; i += step) {
        bool any = false;
        for (int t = 0; t <= width; t++) {
            int sum = first[i] + second[b0 + step * t];
            row[t] = sum >= -1 && sum <= 1 && (row[t] || (t > 0 && row[t - 1]));
            any |= row[t];
        }
        if (!any)
            return false;
        if (i == a1)
            break;
    }
    return true;
}

void append(char move, int count) {
    while (count--)
        moves[used++] = move;
}

bool recover(int a0, int a1, int b0, int b1) {
    if (a0 == a1 || b0 == b1) {
        for (int i = a0; i <= a1; i++)
            for (int j = b0; j <= b1; j++) {
                int sum = first[i] + second[j];
                if (sum < -1 || sum > 1)
                    return false;
            }
        append(a0 == a1 ? '2' : '1', a1 - a0 + b1 - b0);
        return true;
    }
    int middle = (a0 + a1) / 2;
    // One first-pile card joins the upper and lower rows across a vertical edge.
    bool single = a1 - a0 == 1;
    if (!frontier(forward, a0, single ? a0 : middle, b0, b1, 1) ||
        !frontier(backward, a1, single ? a1 : middle, b1, b0, -1))
        return false;
    int width = b1 - b0, split = -1;
    for (int t = 0; t <= width; t++)
        if (forward[t] && backward[width - t]) {
            split = t;
            break;
        }
    if (split < 0)
        return false;
    if (single) {
        append('2', split);
        append('1', 1);
        append('2', width - split);
        return true;
    }
    // Only the split column survives; child calls may overwrite both buffers.
    return recover(a0, middle, b0, b0 + split) && recover(middle, a1, b0 + split, b1);
}

int main() {
    int n;
    char a[MAX_LENGTH + 1], b[MAX_LENGTH + 1];
    if (scanf("%d%1000s%1000s", &n, a, b) != INPUT_FIELDS)
        return 0;
    for (int i = 0; i < n; i++) {
        first[i + 1] = first[i] + (a[i] == '1' ? 1 : -1);
        second[i + 1] = second[i] + (b[i] == '1' ? 1 : -1);
    }
    if (!recover(0, n, 0, n))
        puts("Impossible");
    else {
        moves[used] = 0;
        puts(moves);
    }
}
