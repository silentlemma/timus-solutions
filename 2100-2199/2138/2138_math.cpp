#include <cstdio>

constexpr int DIGITS = 4;
constexpr unsigned BASE = 256;

int main() {
    unsigned v;
    scanf("%*s %u", &v);  // the type of the sender is skipped
    // Both directions reverse the four base-256 digits, so the type does not matter.
    unsigned sent = 0;
    for (int i = 0; i < DIGITS; i++) {
        sent = sent * BASE + v % BASE;
        v /= BASE;
    }
    printf("%u\n", sent);
    return 0;
}
