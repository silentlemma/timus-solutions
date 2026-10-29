#include <cstdio>

const int INPUT_BUFFER_SIZE = 16384;

// up to 500 000 numbers are parsed by hand from 16 KB blocks, much faster
// than scanf; the values are at most 10^9 and fit in an int
class Input {
    char buffer[INPUT_BUFFER_SIZE];
    int position = 0;
    int length = 0;

    int nextByte() {
        if (position == length) {
            length = static_cast<int>(std::fread(buffer, 1, sizeof(buffer), stdin));
            position = 0;
            if (length == 0)
                return EOF;
        }
        return buffer[position++];
    }

  public:
    int nextInt() {
        int ch;
        do {
            ch = nextByte();
        } while (ch != EOF && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = nextByte();
        }
        return value;
    }
};

int main() {
    Input input;
    int count = input.nextInt();
    // the Boyer-Moore vote: a value met more often than all the others together
    // survives pairing every note with a different one
    int leader = 0, lead = 0;
    for (int i = 0; i < count; i++) {
        int value = input.nextInt();
        if (lead == 0) {
            leader = value;
            lead = 1;
        } else if (value == leader) {
            lead++;
        } else {
            lead--;
        }
    }
    std::printf("%d\n", leader);
}
