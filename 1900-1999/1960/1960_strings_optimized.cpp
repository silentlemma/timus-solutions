#include <cstdint>
#include <cstdio>

constexpr int IO_SIZE = 16384;
constexpr int DECIMAL_DIGITS = 16;
class Input {
    char data[IO_SIZE];
    int position = 0, size = 0;

  public:
    int byte() {
        if (position == size) {
            size = std::fread(data, 1, sizeof data, stdin);
            position = 0;
            if (size == 0)
                return EOF;
        }
        return static_cast<unsigned char>(data[position++]);
    }
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = byte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value * sign;
    }
};
class Output {
    char data[IO_SIZE];
    int size = 0;

  public:
    void flush() {
        std::fwrite(data, 1, size, stdout);
        size = 0;
    }
    void byte(char c) {
        if (size == IO_SIZE)
            flush();
        data[size++] = c;
    }
    void number(unsigned value) {
        char digits[DECIMAL_DIGITS];
        int count = 0;
        do {
            digits[count++] = '0' + value % 10;
            value /= 10;
        } while (value);
        while (count)
            byte(digits[--count]);
    }
};

constexpr int MAX_LENGTH = 100000, ROOT_COUNT = 2, EMPTY_ROOT = 1;

struct Node {
    int32_t length;
    uint32_t link, child, sibling;
    char letter;
};

Node nodes[MAX_LENGTH + ROOT_COUNT];
char text[MAX_LENGTH + 1];

uint32_t transition(uint32_t parent, char letter) {
    // A palindrome has one inner palindrome: its incoming edge can live in its own node.
    for (uint32_t edge = nodes[parent].child; edge != 0; edge = nodes[edge].sibling)
        if (nodes[edge].letter == letter)
            return edge;
    return 0;
}

int main() {
    if (scanf("%100000s", text) != 1)
        return 0;
    Output output;
    nodes[0].length = -1;
    uint32_t count = ROOT_COUNT, last = EMPTY_ROOT;
    for (int position = 0; text[position] != '\0'; ++position) {
        char letter = text[position];
        uint32_t parent = last;
        while (true) {
            int left = position - nodes[parent].length - 1;
            if (left >= 0 && text[left] == letter)
                break;
            parent = nodes[parent].link;
        }
        uint32_t node = transition(parent, letter);
        if (node == 0) {
            node = count++;
            nodes[node].length = nodes[parent].length + 2;
            nodes[node].letter = letter;
            nodes[node].sibling = nodes[parent].child;
            nodes[parent].child = node;
            if (nodes[node].length == 1)
                nodes[node].link = EMPTY_ROOT;
            else {
                uint32_t candidate = nodes[parent].link;
                while (true) {
                    int left = position - nodes[candidate].length - 1;
                    if (left >= 0 && text[left] == letter)
                        break;
                    candidate = nodes[candidate].link;
                }
                nodes[node].link = transition(candidate, letter);
            }
        }
        last = node;
        if (position)
            output.byte(' ');
        output.number(count - ROOT_COUNT);
    }
    output.byte('\n');
    output.flush();
}
