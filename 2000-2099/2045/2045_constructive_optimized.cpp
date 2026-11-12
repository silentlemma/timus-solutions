#include <algorithm>
#include <cstdio>

constexpr int MAX_LENGTH = 2000, TAIL_SIZE = 3;
constexpr char TAIL[] = "bcd";

int main() {
    int n;
    if (std::scanf("%d", &n) != 1)
        return 0;
    char prefix[MAX_LENGTH], tail[MAX_LENGTH];
    for (int i = 0; i < n; ++i) {
        prefix[i] = 'a';
        tail[i] = TAIL[i % TAIL_SIZE];
    }
    for (int count = 1; count <= n; ++count) {
        std::printf("%d : ", count);
        if (count < std::min(n, TAIL_SIZE))
            std::fputs("NO", stdout);
        else if (n < TAIL_SIZE)
            std::fwrite(prefix, 1, n, stdout);
        else {
            int run = count - TAIL_SIZE;
            std::fwrite(prefix, 1, run, stdout);
            std::fwrite(tail, 1, n - run, stdout);
        }
        std::putchar('\n');
    }
}
