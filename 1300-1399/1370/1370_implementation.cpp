#include <cstdio>
#include <string>
#include <vector>

const int WINDOW = 10; // digits seen in the window

int main() {
    int n = 0, m = 0;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> digits(n);
    for (int &d : digits)
        if (scanf("%d", &d) != 1)
            return 0;
    // each click moves the window one digit on, around the wheel
    std::string out;
    for (int i = 0; i < WINDOW; i++)
        out += (char)('0' + digits[(m + i) % n]);
    printf("%s\n", out.c_str());
    return 0;
}
