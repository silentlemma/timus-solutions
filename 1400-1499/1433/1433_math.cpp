#include <algorithm>
#include <cstdio>
#include <cstring>

const int FACES = 4;

bool equivalent(const char *a, const char *b) {
    char first[FACES + 1], second[FACES + 1];
    std::strcpy(first, a);
    std::strcpy(second, b);
    std::sort(first, first + FACES);
    std::sort(second, second + FACES);
    if (std::strcmp(first, second))
        return false;
    for (int i = 1; i < FACES; i++)
        if (first[i] == first[i - 1])
            return true;
    int permutation[FACES];
    for (int i = 0; i < FACES; i++) {
        permutation[i] = 0;
        while (a[permutation[i]] != b[i])
            permutation[i]++;
    }
    int inversions = 0;
    for (int i = 0; i < FACES; i++)
        for (int j = i + 1; j < FACES; j++)
            inversions += permutation[i] > permutation[j];
    return inversions % 2 == 0;
}

int main() {
    char a[FACES + 1], b[FACES + 1];
    if (scanf("%4s%4s", a, b) != 2)
        return 0;
    puts(equivalent(a, b) ? "equal" : "different");
    return 0;
}
