#include <iostream>
#include <string>

int main() {
    const int SIDE = 8;
    const int JUMPS[8][2] = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                             {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
    int n;
    std::cin >> n;
    for (int t = 0; t < n; t++) {
        std::string square;
        std::cin >> square;
        int col = square[0] - 'a', row = square[1] - '1', count = 0;
        // the knight attacks every square one jump away that is on the board
        for (auto &jump : JUMPS) {
            int c = col + jump[0], r = row + jump[1];
            count += c >= 0 && c < SIDE && r >= 0 && r < SIDE;
        }
        std::cout << count << "\n";
    }
}
