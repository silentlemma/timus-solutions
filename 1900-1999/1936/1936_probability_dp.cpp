#include <iomanip>
#include <iostream>
#include <vector>

constexpr int GESTURE_COUNT = 3;
constexpr int OUTPUT_DIGITS = 12;

double expectedRounds(int count) {
    std::vector<double> expected(count + 1, 0.0);
    double powerThree = 1.0, powerTwo = 2.0;
    for (int players = 2; players <= count; ++players) {
        powerThree *= GESTURE_COUNT;
        powerTwo *= 2;
        double weightedSuccessors = 0.0, combination = 1.0;
        for (int survivors = 1; survivors < players; ++survivors) {
            combination = combination * (players - survivors + 1) / survivors;
            weightedSuccessors += combination * expected[survivors];
        }
        expected[players] = (powerThree + weightedSuccessors) / (powerTwo - 2);
    }
    return expected[count];
}

int main() {
    int count;
    std::cin >> count;
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS) << expectedRounds(count) << '\n';
    return 0;
}
