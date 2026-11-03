#include <cstdio>
#include <cstring>

const int DECIMAL_BASE = 10, PREFIX_PLACES = 3, BUFFER_SIZE = 4096;
char zeros[BUFFER_SIZE];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int places = n < PREFIX_PLACES ? n : PREFIX_PLACES, unit = 1;
    for (int i = 0; i < places; i++)
        unit *= DECIMAL_BASE;
    int count = 0;
    // Every k<10 that divides a power of10 already divides10^3.
    // Compute the prefix from the counting formula, never a stored answer table.
    for (int k = 1; k < DECIMAL_BASE; k++)
        if (unit % k == 0)
            count += unit / k - unit / DECIMAL_BASE;
    printf("%d", count);
    std::memset(zeros, '0', sizeof(zeros));
    int remaining = n - places;
    while (remaining > 0) {
        int chunk = remaining < BUFFER_SIZE ? remaining : BUFFER_SIZE;
        fwrite(zeros, 1, chunk, stdout);
        remaining -= chunk;
    }
    putchar('\n');
}
