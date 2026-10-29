#include <cstdio>

constexpr int KNOWN_HUNGRY = 2, KNOWN_FULL = 10; // given in the statement
constexpr int WORD_CAPACITY = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int hungry = KNOWN_HUNGRY, full = KNOWN_FULL;
    for (int i = 0; i < n; ++i) {
        int count;
        // scanf into a small char array instead of iostream and std::string; the
        // first letter tells hungry from satisfied
        char verdict[WORD_CAPACITY];
        if (scanf("%d %9s", &count, verdict) != 2)
            return 0;
        if (verdict[0] == 'h') {
            if (count > hungry)
                hungry = count;
        } else if (count < full) {
            full = count;
        }
    }
    // the smallest satisfying amount must exceed the largest hungry one
    if (full > hungry)
        printf("%d\n", full);
    else
        puts("Inconsistent");
}
