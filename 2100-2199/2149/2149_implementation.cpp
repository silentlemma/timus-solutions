#include <algorithm>
#include <iostream>
#include <string>

constexpr int STEP = 5;  // four characters of a pigeon and a separating column

int main() {
    int n;
    std::string top;
    std::cin >> n >> top;
    // halves counts the pigeons that break the pattern with the left half looking
    // left, parity those that break the pattern with even positions looking left,
    // and the two opposite patterns break exactly at the other pigeons
    int halves = 0, parity = 0;
    for (int i = 0; i < n; i++) {
        bool left = top[i * STEP] == '<';
        if (left != (i < n / 2)) halves++;
        if (left != (i % 2 == 0)) parity++;
    }
    std::cout << std::min(std::min(halves, n - halves), std::min(parity, n - parity)) << '\n';
    return 0;
}
