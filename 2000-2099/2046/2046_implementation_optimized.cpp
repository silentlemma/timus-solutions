#include <cstdio>
#include <cstring>

constexpr int WIDTH = 10;
constexpr int ROWS = 4;
constexpr int COLUMNS = 3;
constexpr int MAX_WORDS = 5;
constexpr int NAME_BUFFER_SIZE = 64;
constexpr int DAY_BUFFER_SIZE = 16;
constexpr int LINE_SIZE = COLUMNS * (WIDTH + 1) + 2;

void endLine() {
    int c;
    do {
        c = getchar();
    } while (c != '\n' && c != EOF);
}

int main() {
    int count;
    scanf("%d", &count);
    endLine();
    char grid[ROWS][COLUMNS][MAX_WORDS][WIDTH];
    memset(grid, ' ', sizeof(grid));
    int heights[ROWS] = {};
    for (int &height : heights)
        height = 1;
    while (count--) {
        char name[NAME_BUFFER_SIZE], day[DAY_BUFFER_SIZE];
        fgets(name, sizeof(name), stdin);
        int lesson;
        scanf("%15s%d", day, &lesson);
        endLine();
        --lesson;
        int column = day[0] == 'S' ? 2 : day[1] == 'u' ? 0 : 1;
        int level = 0, used = 0, start = 0;
        while (name[start] && name[start] != '\r' && name[start] != '\n') {
            if (name[start] == ' ') {
                ++start;
                continue;
            }
            int end = start;
            while (name[end] && name[end] > ' ')
                ++end;
            int length = end - start;
            if (used && used + 1 + length > WIDTH) {
                ++level;
                used = 0;
            }
            if (used)
                ++used;
            // Five words need at most five padded lines, with no string allocations.
            memcpy(grid[lesson][column][level] + used, name + start, length);
            used += length;
            start = end;
        }
        if (level + 1 > heights[lesson])
            heights[lesson] = level + 1;
    }
    char border[LINE_SIZE], line[LINE_SIZE];
    for (int i = 0; i < LINE_SIZE - 1; ++i)
        border[i] = i % (WIDTH + 1) == 0 ? '+' : '-';
    border[LINE_SIZE - 1] = '\n';
    fwrite(border, 1, sizeof(border), stdout);
    for (int row = 0; row < ROWS; ++row) {
        for (int level = 0; level < heights[row]; ++level) {
            line[0] = '|';
            for (int col = 0; col < COLUMNS; ++col) {
                memcpy(line + 1 + col * (WIDTH + 1), grid[row][col][level], WIDTH);
                line[(col + 1) * (WIDTH + 1)] = '|';
            }
            line[LINE_SIZE - 1] = '\n';
            fwrite(line, 1, sizeof(line), stdout);
        }
        fwrite(border, 1, sizeof(border), stdout);
    }
}
