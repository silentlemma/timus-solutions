#include <cstdio>

constexpr int WIDTH = 80;

int main() {
    char screen[WIDTH];
    for (char &cell : screen)
        cell = ' ';
    int cursor = 0;
    for (int key = std::getchar(); key != EOF && key != '\n' && key != '\r'; key = std::getchar()) {
        if (key == '<') {
            if (cursor != 0)
                --cursor;
        } else {
            if (key != '>')
                screen[cursor] = char(key);
            if (++cursor == WIDTH)
                cursor = 0;
        }
    }
    std::fwrite(screen, 1, WIDTH, stdout);
    std::putchar('\n');
}
