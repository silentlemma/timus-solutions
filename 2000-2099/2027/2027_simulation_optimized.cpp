#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 8192;
const int NUMBER_RESERVE = 16;
const int DECIMAL_BASE = 10;
const int ALPHABET = 26;
const int VALUE_LIMIT = 100000;
const int TICK_LIMIT = 1000000;
const int DIRECTIONS = 4;
const int DIRECTION_MASK = DIRECTIONS - 1;

enum Op : uint8_t {
    OUTSIDE,
    RIGHT,
    DOWN,
    LEFT,
    UP,
    NOP,
    HALT,
    INPUT,
    OUTPUT,
    INCREMENT,
    DECREMENT,
    TURN,
    REGISTER_BASE
};

struct Reader {
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
    int character() {
        int c = next();
        while (c && c <= ' ')
            c = next();
        return c;
    }
    int number() {
        int c = character(), value = 0;
        bool negative = c == '-';
        if (c == '-' || c == '+')
            c = next();
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL_BASE + c - '0';
            c = next();
        }
        return negative ? -value : value;
    }
};

struct Writer {
    char bytes[BUFFER_SIZE];
    int used = 0;
    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }
    void number(int value) {
        if (used + NUMBER_RESERVE > BUFFER_SIZE)
            flush();
        if (value < 0) {
            bytes[used++] = '-';
            value = -value;
        }
        char digits[NUMBER_RESERVE];
        int length = 0;
        do {
            digits[length++] = char('0' + value % DECIMAL_BASE);
            value /= DECIMAL_BASE;
        } while (value);
        while (length)
            bytes[used++] = digits[--length];
        bytes[used++] = '\n';
    }
    void finish(const char *message) {
        flush();
        fputs(message, stdout);
    }
};

uint8_t instruction(int c) {
    switch (c) {
    case '>':
        return RIGHT;
    case 'v':
        return DOWN;
    case '<':
        return LEFT;
    case '^':
        return UP;
    case '#':
        return HALT;
    case '?':
        return INPUT;
    case '!':
        return OUTPUT;
    case '+':
        return INCREMENT;
    case '-':
        return DECREMENT;
    case '@':
        return TURN;
    default:
        return c >= 'A' && c <= 'Z' ? uint8_t(REGISTER_BASE + c - 'A') : uint8_t(NOP);
    }
}

int main() {
    Reader in;
    Writer out;
    int height = in.number(), width = in.number(), stride = width + 2;
    std::vector<uint8_t> program((height + 2) * stride);
    for (int row = 1; row <= height; ++row)
        for (int col = 1; col <= width; ++col)
            program[row * stride + col] = instruction(in.character());
    int remaining = in.number(), last = 0, current = 0, memory[ALPHABET] = {};
    int position = stride + 1, direction = 0;
    const int move[DIRECTIONS] = {1, stride, -1, -stride};
    for (int tick = 0; tick < TICK_LIMIT; ++tick) {
        uint8_t op = program[position];
        if (op == HALT) {
            out.flush();
            return 0;
        }
        if (op <= UP)
            direction = op - RIGHT;
        else if (op >= REGISTER_BASE) {
            int prior = memory[op - REGISTER_BASE];
            memory[op - REGISTER_BASE] = current;
            current = prior;
        } else
            switch (op) {
            case INPUT:
                if (remaining > 0) {
                    last = in.number();
                    --remaining;
                }
                current = last;
                break;
            case OUTPUT:
                out.number(current);
                current = 0;
                break;
            case INCREMENT:
                ++current;
                break;
            case DECREMENT:
                --current;
                break;
            case TURN:
                direction = (direction + (current == 0 ? DIRECTION_MASK : 1)) & DIRECTION_MASK;
                break;
            default:
                break;
            }
        if (current < -VALUE_LIMIT || current > VALUE_LIMIT) {
            out.finish("OVERFLOW ERROR\n");
            return 0;
        }
        position += move[direction];
        if (program[position] == OUTSIDE) {
            out.finish("RUNTIME ERROR\n");
            return 0;
        }
    }
    out.finish("TIME LIMIT EXCEEDED\n");
}
