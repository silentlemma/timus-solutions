#include <cstdio>
#include <utility>
#include <vector>

const int MAX_SIDE = 50, MAX_SQUARED = 2 * MAX_SIDE * MAX_SIDE;
const int COLOUR_XOR = 'W' ^ 'B';
char board[MAX_SIDE][MAX_SIDE + 1];
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
            board[r][c] = char(ch);
        }
    for (int k = 0; k * k < MAX_SQUARED; k++)
        square[k * k] = true;
    std::vector<std::pair<int, int>> offsets;
    for (int dr = 1 - m; dr < m; dr++)
        for (int dc = 1 - n; dc < n; dc++)
            if (square[dr * dr + dc * dc])
                offsets.push_back({dr, dc});
    // An even count cancels; one odd visit toggles its integer-distance cells.
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            if (next_int() & 1)
                for (auto [dr, dc] : offsets) {
                    int a = r + dr, b = c + dc;
                    if (a >= 0 && a < m && b >= 0 && b < n)
                        board[a][b] ^= COLOUR_XOR;
                }
    for (int r = 0; r < m; r++)
        puts(board[r]);
}
