#include <iostream>

// the smallest number for each word, from the largest down
const int FROM[] = {1000, 500, 250, 100, 50, 20, 10, 5, 1};
const char *WORDS[] = {"legion", "zounds", "swarm",   "throng", "horde",
                       "lots",   "pack",   "several", "few"};

int main() {
    int n;
    if (!(std::cin >> n)) return 0;
    int i = 0;
    while (n < FROM[i]) i++;
    std::cout << WORDS[i] << "\n";
    return 0;
}
