#include <cstdio>

const int DISKS = 4, PETALS = 3, BITS = DISKS + PETALS;

// petal j lies in every disk except disk j
bool valid(const int *bits) {
    int total = 0;
    for (int d = 0; d < DISKS; d++)
        total += bits[d];
    for (int j = 0; j < PETALS; j++) {
        if ((total - bits[j]) % 2 != bits[DISKS + j])
            return false;
    }
    return true;
}

int main() {
    int bits[BITS];
    // every bit is a single character, read with getchar and written with putchar
    for (int &b : bits) {
        int ch;
        do {
            ch = std::getchar();
        } while (ch != EOF && ch <= ' ');
        if (ch == EOF)
            return 0;
        b = ch - '0';
    }
    // try the word as it is, then each single change
    for (int k = -1; k < BITS; k++) {
        if (k >= 0)
            bits[k] ^= 1;
        if (valid(bits))
            break;
        if (k >= 0)
            bits[k] ^= 1;
    }
    for (int i = 0; i < BITS; i++) {
        std::putchar('0' + bits[i]);
        std::putchar(i + 1 == BITS ? '\n' : ' ');
    }
    return 0;
}
