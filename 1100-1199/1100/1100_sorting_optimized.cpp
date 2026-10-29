#include <cstdio>
#include <vector>

constexpr int MOST = 100;
constexpr int BUFFER_SIZE = 8192;
constexpr int DECIMAL_DIGITS = 10;

// numbers are read and written by hand through 8 KB buffers: with 150 000
// lines this is much faster than scanf and printf
class Input {
    char buffer[BUFFER_SIZE];
    int position = 0;
    int length = 0;

    int readByte() {
        if (position == length) {
            length = static_cast<int>(fread(buffer, 1, BUFFER_SIZE, stdin));
            position = 0;
            if (length == 0)
                return EOF;
        }
        return buffer[position++];
    }

  public:
    int readInt() {
        int c;
        do {
            c = readByte();
        } while (c != EOF && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }
};

class Output {
    char buffer[BUFFER_SIZE];
    int length = 0;

  public:
    void flush() {
        fwrite(buffer, 1, length, stdout);
        length = 0;
    }

    void put(char c) {
        if (length == BUFFER_SIZE)
            flush();
        buffer[length++] = c;
    }

    void number(int value) {
        char digits[DECIMAL_DIGITS];
        int count = 0;
        do {
            digits[count++] = static_cast<char>('0' + value % 10);
            value /= 10;
        } while (value != 0);
        while (count > 0)
            put(digits[--count]);
    }
};

int main() {
    Input input;
    int n = input.readInt();
    // bubble sort never swaps equal scores, so teams with the same score keep
    // their input order: a counting sort by score does the same
    std::vector<int> buckets[MOST + 1];
    for (int i = 0; i < n; ++i) {
        int team = input.readInt();
        int solved = input.readInt();
        buckets[solved].push_back(team);
    }
    Output output;
    for (int solved = MOST; solved >= 0; --solved) {
        for (int team : buckets[solved]) {
            output.number(team);
            output.put(' ');
            output.number(solved);
            output.put('\n');
        }
    }
    output.flush();
}
