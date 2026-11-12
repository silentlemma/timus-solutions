#include <cstdio>

const int MAX_LENGTH = 10000;
const int BUFFER_SIZE = 4096;
const int HEX_RADIX = 16;
const char DIGITS[] = "0123456789ABCDEF";

struct Input {
    unsigned char bytes[BUFFER_SIZE];
    int position = 0, length = 0;

    int next() {
        if (position == length) {
            length = int(fread(bytes, 1, sizeof(bytes), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return bytes[position++];
    }

    int hexValue(int c) {
        if (c <= '9')
            return c - '0';
        return c <= 'F' ? c - 'A' + 10 : c - 'a' + 10;
    }

    int encoded() {
        int c = next();
        while (c && c <= ' ')
            c = next();
        return hexValue(c) * HEX_RADIX + hexValue(next());
    }
};

struct Output {
    char bytes[BUFFER_SIZE];
    int used = 0;

    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }

    void key(int value) {
        if (used + 2 >= BUFFER_SIZE)
            flush();
        bytes[used++] = DIGITS[value / HEX_RADIX];
        bytes[used++] = DIGITS[value % HEX_RADIX];
    }
};

int main() {
    Input input;
    unsigned char shorter[MAX_LENGTH];
    int length = 0, c = input.next();
    while (c && c <= ' ')
        c = input.next();
    while (c > ' ') {
        int high = input.hexValue(c), low = input.hexValue(input.next());
        shorter[length++] = static_cast<unsigned char>(high * HEX_RADIX + low);
        c = input.next();
    }
    Output output;
    int previous = input.encoded() ^ ' ';
    output.key(previous);
    for (int i = 0; i < length; ++i) {
        // Eliminate the shared plaintext byte; retain only the preceding key byte.
        previous ^= shorter[i] ^ input.encoded();
        output.key(previous);
    }
    output.bytes[output.used++] = '\n';
    output.flush();
}
