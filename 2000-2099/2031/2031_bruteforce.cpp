#include <iostream>
#include <string>

constexpr int BASE = 10;
constexpr int LIMIT = BASE * BASE - 1;
// the d-th character is digit d turned upside down, as in the statement, and
// ? marks a digit that reads as nothing
const std::string TURN = "01????9?86";

std::string solve(int count) {
    int run = 0;
    for (int value = 1; value <= LIMIT; ++value) {
        if (TURN[value / BASE] != '?' && TURN[value % BASE] != '?')
            ++run;
        else
            run = 0;
        if (run >= count) {
            std::string answer;
            for (int target = value; target > value - count; --target) {
                if (!answer.empty())
                    answer += ' ';
                answer += TURN[target % BASE];
                answer += TURN[target / BASE];
            }
            return answer;
        }
    }
    return "Glupenky Pierre";
}

int main() {
    int count;
    if (std::cin >> count)
        std::cout << solve(count) << '\n';
}
