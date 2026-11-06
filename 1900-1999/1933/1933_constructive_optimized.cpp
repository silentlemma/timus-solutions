#include <charconv>
#include <cstdio>

constexpr int MAX_PAIRS = 100;
constexpr int MAX_SIZE = 2 * MAX_PAIRS + 1;
constexpr int FIELD_WIDTH = 4;

int main() {
    int pairs;
    if (std::scanf("%d", &pairs) != 1)
        return 0;
    const int size = 2 * pairs + 1;
    char buffer[MAX_SIZE * FIELD_WIDTH];
    for (int row = 0; row < size; ++row) {
        char *end = buffer;
        int round = row == 0 ? size : row;
        for (int column = 0; column < size; ++column) {
            if (column > 0)
                *end++ = ' ';
            end = std::to_chars(end, buffer + sizeof buffer, row == column ? 0 : round).ptr;
            round = round == size ? 1 : round + 1;
        }
        *end++ = '\n';
        std::fwrite(buffer, 1, end - buffer, stdout);
    }
}
