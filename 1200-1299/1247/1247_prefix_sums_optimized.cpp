#include <unistd.h>

const int BUFFER_SIZE = 4096;
const int BASE = 10;
const char YES[] = "YES\n", NO[] = "NO\n";
char input[BUFFER_SIZE];
int position, available;

int readByte() {
    if (position >= available) {
        available = static_cast<int>(read(STDIN_FILENO, input, sizeof input));
        position = 0;
        if (available <= 0)
            return -1;
    }
    return input[position++];
}

int nextInt() {
    int c = readByte();
    while (c >= 0 && c <= ' ')
        c = readByte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * BASE + c - '0';
        c = readByte();
    }
    return value;
}

int main() {
    int size = nextInt(), limit = nextInt(), prefix = 0;
    for (int i = 0; i < size; i++) {
        prefix += nextInt() - 1;
        // Total excess is limit: every prefix must stay in [0,limit].
        if (prefix < 0 || prefix > limit) {
            (void)write(STDOUT_FILENO, NO, sizeof NO - 1);
            return 0;
        }
    }
    (void)write(STDOUT_FILENO, YES, sizeof YES - 1);
}
