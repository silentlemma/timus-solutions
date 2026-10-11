#include <cstdio>
#include <string>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    int half = n / 2;
    // 1 + 9 k^2 with k = 11...1 (half ones), and 9 k^2 = k 10^half - k
    std::string answer;
    if (half == 0) {
        answer = "1";
    } else if (half == 1) {
        answer = "10";
    } else {
        answer = std::string(half - 1, '1') + "0" + std::string(half - 2, '8') + "90";
    }
    puts(answer.c_str());
    return 0;
}
