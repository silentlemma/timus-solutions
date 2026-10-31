#include <cstdio>
const int MAX_QUEUE = 1000;
// each queue has at most 1000 cars, plus its terminating zero.
char south[MAX_QUEUE + 1], north[MAX_QUEUE + 1];
// the width of each %s is MAX_QUEUE, so a token always fits its buffer
const char QUEUE_FORMAT[] = "%1000s %1000s";
int main() {
    std::scanf(QUEUE_FORMAT, south, north);
    int i = 0, j = 0, elapsed = 0;
    while (south[i] && north[j]) {
        char a = south[i], b = north[j];
        i += a != 'L' || b == 'L';
        j += b != 'L' || a == 'L';
        ++elapsed;
    }
    while (south[i++])
        ++elapsed;
    while (north[j++])
        ++elapsed;
    std::printf("%d\n", elapsed);
}
