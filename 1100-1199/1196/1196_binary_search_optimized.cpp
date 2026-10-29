#include <algorithm>
#include <cstdio>
#include <vector>

const int INPUT_BUFFER_SIZE = 65536;

// up to a million numbers are parsed by hand from 64 KB blocks, much faster
// than scanf
class Input {
    char buffer[INPUT_BUFFER_SIZE];
    int position = 0, length = 0;

    int readByte() {
        if (position == length) {
            length = static_cast<int>(fread(buffer, 1, sizeof(buffer), stdin));
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
            ch = readByte();
        } while (ch != EOF && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = readByte();
        }
        return value;
    }
};

int main() {
    Input input;
    int size = input.nextInt();
    // the teacher's dates come sorted, so each of the student's dates is
    // looked up by binary search, counting repeats every time
    std::vector<int> known(size);
    for (int &year : known)
        year = input.nextInt();
    int queries = input.nextInt(), count = 0;
    for (int i = 0; i < queries; ++i)
        count += std::binary_search(known.begin(), known.end(), input.nextInt());
    printf("%d\n", count);
}
