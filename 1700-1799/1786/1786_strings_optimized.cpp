#include <cstdio>
#include <cstring>

constexpr char NAME[] = "Sandro";
// the statement allows 200 letters; reserve one extra byte for the terminator.
constexpr int TEXT_CAPACITY = 201;
const int COINS = 5;

char lower(char c) {
    // the input contains only Latin letters.
    return c <= 'Z' ? c + ('a' - 'A') : c;
}

int main() {
    char text[TEXT_CAPACITY];
    if (std::scanf("%200s", text) != 1)
        return 0;
    const size_t length = std::strlen(text);
    int best = -1;
    for (size_t start = 0; start + (sizeof(NAME) - 1) <= length; start++) {
        int cost = 0;
        for (size_t k = 0; k < (sizeof(NAME) - 1); k++) {
            char a = text[start + k], b = NAME[k];
            // one fee for the wrong case, one for the wrong letter
            if ((a <= 'Z') != (b <= 'Z'))
                cost += COINS;
            if (lower(a) != lower(b))
                cost += COINS;
        }
        if (best < 0 || cost < best)
            best = cost;
    }
    std::printf("%d\n", best);
    return 0;
}
