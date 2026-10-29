#include <cstdio>

constexpr int PLAYERS = 3;
constexpr int MAX_COUNT = 4000;

// the numbers are parsed by hand with getchar instead of scanf
int readInt() {
    int c = getchar();
    while (c <= ' ' && c != EOF) {
        c = getchar();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    int common[MAX_COUNT];
    int size = readInt();
    for (int i = 0; i < size; ++i) {
        common[i] = readInt();
    }
    // walk the sorted intersection and each next list together, always moving past the
    // smallest current number
    for (int player = 1; player < PLAYERS; ++player) {
        int n = readInt(), at = 0, kept = 0;
        for (int i = 0; i < n; ++i) {
            int value = readInt();
            while (at < size && common[at] < value) {
                ++at;
            }
            if (at < size && common[at] == value) {
                // kept never overtakes at, so the stored numbers not yet compared stay intact
                common[kept++] = value;
                ++at;
            }
        }
        size = kept;
    }
    printf("%d\n", size);
}
