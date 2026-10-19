#include <cstdio>
#include <cstring>

const int MOST = 50;

// page i open is bit i - 1 of a Gray code word: F1 flips bit 0, the other
// move flips the bit above the lowest set one; these are the reflected Gray
// code steps, so the states form one path ordered by the decoded word
long long rank(const char *pages) {
    long long gray = 0, place = 0;
    for (int i = strlen(pages) - 1; i >= 0; i--) gray = gray * 2 + (pages[i] - '0');
    for (; gray; gray >>= 1) place ^= gray;
    return place;
}

int main() {
    int n;
    char start[MOST + 1], goal[MOST + 1];
    if (scanf("%d %50s %50s", &n, start, goal) < 1) return 0;
    long long diff = rank(start) - rank(goal);
    printf("%lld\n", diff < 0 ? -diff : diff);
    return 0;
}
