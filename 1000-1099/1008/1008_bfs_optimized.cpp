#include <array>
#include <cstdint>
#include <cstdio>

constexpr int HEADER_BUFFER_SIZE = 32;

constexpr int SIDE = 12;
constexpr int FIRST = 1;
constexpr int LAST = SIDE - 2;
constexpr int MAX_PIXELS = LAST * LAST;
constexpr int DIRECTIONS = 4;
constexpr int DELTA[DIRECTIONS] = {SIDE, 1, -SIDE, -1};
constexpr char LETTERS[] = "RTLB";

using Image = std::array<bool, SIDE * SIDE>;
using Queue = std::array<std::uint8_t, MAX_PIXELS>;

void print_coordinates(int pixel) { std::printf("%d %d\n", pixel / SIDE, pixel % SIDE); }

void describe(int count) {
    Image black{};
    int start = SIDE * SIDE;
    for (int i = 0; i < count; ++i) {
        int x, y;
        std::scanf("%d%d", &x, &y);
        const int pixel = x * SIDE + y;
        black[pixel] = true;
        if (pixel < start) {
            start = pixel;
        }
    }
    Queue queue;
    queue[0] = start;
    black[start] = false;
    print_coordinates(start);
    int end = 1;
    for (int head = 0; head < count; ++head) {
        const int pixel = queue[head];
        for (int direction = 0; direction < DIRECTIONS; ++direction) {
            const int next = pixel + DELTA[direction];
            if (black[next]) {
                black[next] = false;
                queue[end++] = next;
                std::putchar(LETTERS[direction]);
            }
        }
        std::puts(head + 1 < count ? "," : ".");
    }
}

void list_pixels(int x, int y) {
    Image black{};
    Queue queue;
    const int start = x * SIDE + y;
    queue[0] = start;
    black[start] = true;
    int end = 1;
    for (int head = 0; head < end; ++head) {
        char line[DIRECTIONS + 2];
        if (std::scanf("%5s", line) != 1) {
            return;
        }
        for (const char *token = line; *token != ',' && *token != '.'; ++token) {
            for (int direction = 0; direction < DIRECTIONS; ++direction) {
                if (*token == LETTERS[direction]) {
                    const int next = queue[head] + DELTA[direction];
                    black[next] = true;
                    queue[end++] = next;
                    break;
                }
            }
        }
    }
    std::printf("%d\n", end);
    for (int row = FIRST; row <= LAST; ++row) {
        for (int col = FIRST; col <= LAST; ++col) {
            const int pixel = row * SIDE + col;
            if (black[pixel]) {
                print_coordinates(pixel);
            }
        }
    }
}

int main() {
    char first_line[HEADER_BUFFER_SIZE];
    if (!std::fgets(first_line, sizeof first_line, stdin)) {
        return 0;
    }
    int first, second;
    const int read = std::sscanf(first_line, "%d%d", &first, &second);
    if (read == 1) {
        describe(first);
    } else if (read == 2) {
        list_pixels(first, second);
    }
}
