#include <algorithm>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    // best sums with the last word kept and dropped; neighbours may not both stay
    long long kept = 0, dropped = 0;
    int length = 0, c;
    while (true) {
        c = getchar();
        if (c != EOF && isalpha(c)) {
            length++;
            continue;
        }
        if (length > 0) {
            long long next = dropped + length;
            dropped = max(dropped, kept);
            kept = next;
            length = 0;
        }
        if (c == EOF)
            break;
    }
    printf("%lld\n", max(kept, dropped));
}
