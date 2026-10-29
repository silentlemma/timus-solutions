#include <cstdio>

int main() {
    constexpr int kindCount = 3;
    int counts[kindCount] = {};
    const char *names[kindCount] = {"Emperor Penguin", "Little Penguin", "Macaroni Penguin"};
    // every record is two words, the kind and "Penguin"
    // the kinds start with different capitals E, L and M, which neither
    // "Penguin" nor the number contains, so counting them is enough
    for (int c; (c = getchar()) != EOF;) {
        if (c == 'E')
            ++counts[0];
        else if (c == 'L')
            ++counts[1];
        else if (c == 'M')
            ++counts[2];
    }
    int best = 0;
    for (int i = 1; i < kindCount; ++i)
        if (counts[i] > counts[best])
            best = i;
    puts(names[best]);
}
