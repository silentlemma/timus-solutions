#include <cstdio>

int main() {
    int balance = 0, lowest = 0, count = 0;
    for (int ch = std::getchar(); ch != EOF; ch = std::getchar()) {
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
    std::printf("%d\n", balance == 0 ? count : 0);
}
