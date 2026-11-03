#include <cstdint>
#include <cstdio>
#include <utility>
#include <vector>

const int MAX_SIDE = 50, MAX_SQUARED = 2 * MAX_SIDE * MAX_SIDE;
const int COLOUR_XOR = 'W' ^ 'B';
char final[MAX_SIDE][MAX_SIDE + 1];
uint64_t odd[MAX_SIDE];
bool square[MAX_SQUARED];
const int BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int m = next_int(), n = next_int();
    if (m == 0 || n == 0) {
        for (int r = 0; r < m; r++)
            putchar('\n');
        return 0;
    }
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++) {
            int ch = read();
            while (ch <= ' ')
                ch = read();
            final[r][c] = char(ch);
        }
    uint64_t columns = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++)
            odd[r] |= uint64_t(next_int() & 1) << c;
        columns ^= odd[r];
    }
    for (int k = 0; k * k < MAX_SQUARED; k++)
        square[k * k] = true;
    std::vector<std::pair<int, int>> offsets;
    for (int dr = 1; dr < m; dr++)
        for (int dc = 1; dc < n; dc++)
            if (square[dr * dr + dc * dc])
                offsets.push_back({dr, dc});
    uint64_t full = (uint64_t(1) << n) - 1;
    for (int r = 0; r < m; r++) {
        // Row and column include the origin twice, so XOR its row once more.
        uint64_t flips = columns ^ odd[r];
        if (__builtin_popcountll(odd[r]) & 1)
            flips ^= full;
        for (auto [dr, dc] : offsets) {
            uint64_t combined = 0;
            if (r >= dr)
                combined ^= odd[r - dr];
            if (r + dr < m)
                combined ^= odd[r + dr];
            flips ^= (combined << dc) ^ (combined >> dc);
        }
        flips &= full;
        for (int c = 0; c < n; c++)
            if ((flips >> c) & 1)
                final[r][c] ^= COLOUR_XOR;
        puts(final[r]);
    }
}
