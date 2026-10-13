#include <cstdio>
#include <string>

const int FULL = 100; // brightness is given in percent

int main() {
    int n, b;
    scanf("%d %d", &n, &b);
    // lamp i is on when floor((i + 1) b / 100) grows: every stretch then holds
    // less than one lamp more or less than L b / 100, and the pattern repeats
    std::string row(n, '0');
    for (int i = 0; i < n; i++)
        if ((i % FULL + 1) * b / FULL > i % FULL * b / FULL)
            row[i] = '1';
    puts(row.c_str());
}
