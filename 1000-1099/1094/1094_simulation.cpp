#include <iostream>
#include <string>

const int WIDTH = 80;

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::string screen(WIDTH, ' ');
    int cursor = 0;
    for (char key : line) {
        if (key == '\r' || key == '\n')
            continue;
        if (key == '<')
            cursor--;
        else if (key == '>')
            cursor++;
        else
            screen[cursor++] = key;
        // past either edge the cursor jumps to the leftmost position
        if (cursor < 0 || cursor >= WIDTH)
            cursor = 0;
    }
    std::cout << screen << "\n";
}
