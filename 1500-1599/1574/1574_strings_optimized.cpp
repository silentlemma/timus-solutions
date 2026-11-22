#include <cstdio>

constexpr int IO_SIZE = 16384;
char input[IO_SIZE];

int main() {
    int balance = 0, lowest = 0, count = 0;

    for (std::size_t size; (size = std::fread(input, 1, sizeof input, stdin)) != 0;) {
        for (std::size_t i = 0; i < size; ++i) {
            const char ch = input[i];
            if (ch != '(' && ch != ')')
                continue;
            balance += ch == '(' ? 1 : -1;
            if (balance < lowest) {
                lowest = balance;
                count = 1;
            } else if (balance == lowest) {
                ++count;
            }
        }
    }
    std::printf("%d\n", balance == 0 ? count : 0);
}
