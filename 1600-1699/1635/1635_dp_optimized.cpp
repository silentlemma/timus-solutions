#include <cstdint>
#include <cstdio>
#include <cstring>

const int MAX_LENGTH = 4000;
char text[MAX_LENGTH + 1];
uint16_t best[MAX_LENGTH + 1], previous[MAX_LENGTH + 1], ends[MAX_LENGTH];

int main() {
    if (scanf("%4000s", text) != 1)
        return 0;
    int n = std::strlen(text), left = 0, right = n - 1;
    while (left < right && text[left] == text[right]) {
        left++;
        right--;
    }
    // One whole palindrome is already an optimal partition.
    if (left >= right) {
        printf("1\n%s\n", text);
        return 0;
    }
    for (int i = 1; i <= n; i++)
        best[i] = n + 1;
    // Earlier centers finalize every prefix used by the current palindrome.
    // Counts and prefix indices are at most4001, so16-bit cells suffice.
    for (int twice = 0; twice < 2 * n - 1; twice++) {
        int l = twice / 2, r = l + twice % 2;
        while (l >= 0 && r < n && text[l] == text[r]) {
            if (best[l] + 1 < best[r + 1]) {
                best[r + 1] = best[l] + 1;
                previous[r + 1] = l;
            }
            l--;
            r++;
        }
    }
    int count = 0;
    for (int end = n; end; end = previous[end])
        ends[count++] = end;
    printf("%u\n", unsigned(best[n]));
    for (int i = count - 1; i >= 0; i--) {
        int end = ends[i], start = previous[end];
        fwrite(text + start, 1, end - start, stdout);
        putchar(i ? ' ' : '\n');
    }
}
