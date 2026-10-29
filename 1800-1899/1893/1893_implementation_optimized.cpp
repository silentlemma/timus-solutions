#include <cstdio>
#include <cstring>

constexpr int PREMIUM_LAST = 2;
constexpr int BUSINESS_LAST = 20;

// scanf and puts instead of iostream and std::string
int main() {
    int row;
    char letter;
    std::scanf("%d%c", &row, &letter);
    char right_window;
    const char *aisles;
    if (row <= PREMIUM_LAST) {
        right_window = 'D';
        aisles = "BC";
    } else if (row <= BUSINESS_LAST) {
        right_window = 'F';
        aisles = "BCDE";
    } else {
        right_window = 'K';
        aisles = "CDGH";
    }
    if (letter == 'A' || letter == right_window)
        std::puts("window");
    else if (std::strchr(aisles, letter) != nullptr)
        std::puts("aisle");
    else
        std::puts("neither");
}
