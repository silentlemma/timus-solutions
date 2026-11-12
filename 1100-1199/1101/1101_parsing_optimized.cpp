#include <cctype>
#include <cstdint>
#include <cstdio>
#include <vector>

const int REGISTER_COUNT = 26;
const int EXPRESSION_LIMIT = 250;
const int LINE_END_RESERVE = 3;
const int INPUT_FIELDS = 3;
const int FORK = 1;
const int SWITCH_OFFSET = 2;
const int OUTPUT_SIZE = 8192;
const int POINT_RESERVE = 12;
const int DECIMAL_BASE = 10;

enum Op : uint8_t {
    OP_TRUE = REGISTER_COUNT,
    OP_FALSE,
    OP_NOT,
    OP_AND,
    OP_OR,
    OPEN_PAREN,
    CLOSE_PAREN,
    END_TOKEN
};

struct Parser {
    const char *cursor;
    uint8_t token = END_TOKEN, code[EXPRESSION_LIMIT]{};
    int size = 0;
    uint32_t relevant = 0;

    void next() {
        while (std::isspace(static_cast<unsigned char>(*cursor)))
            ++cursor;
        if (!*cursor) {
            token = END_TOKEN;
            return;
        }
        if (*cursor == '(' || *cursor == ')') {
            token = *cursor++ == '(' ? OPEN_PAREN : CLOSE_PAREN;
            return;
        }
        const char *start = cursor;
        while (std::isupper(static_cast<unsigned char>(*cursor)))
            ++cursor;
        if (cursor - start == 1)
            token = uint8_t(*start - 'A');
        else if (*start == 'T')
            token = OP_TRUE;
        else if (*start == 'F')
            token = OP_FALSE;
        else if (*start == 'N')
            token = OP_NOT;
        else if (*start == 'A')
            token = OP_AND;
        else
            token = OP_OR;
    }

    void disjunction() {
        conjunction();
        while (token == OP_OR) {
            next();
            conjunction();
            code[size++] = OP_OR;
        }
    }

    void conjunction() {
        unary();
        while (token == OP_AND) {
            next();
            unary();
            code[size++] = OP_AND;
        }
    }

    void unary() {
        if (token == OP_NOT) {
            next();
            unary();
            code[size++] = OP_NOT;
        } else if (token == OPEN_PAREN) {
            next();
            disjunction();
            next();
        } else {
            code[size++] = token;
            if (token < REGISTER_COUNT)
                relevant |= uint32_t(1) << token;
            next();
        }
    }

    bool value(uint32_t registers) const {
        bool stack[EXPRESSION_LIMIT];
        int top = 0;
        for (int i = 0; i < size; ++i) {
            uint8_t op = code[i];
            if (op < REGISTER_COUNT)
                stack[top++] = (registers >> op) & 1;
            else if (op == OP_TRUE || op == OP_FALSE)
                stack[top++] = op == OP_TRUE;
            else if (op == OP_NOT)
                stack[top - 1] = !stack[top - 1];
            else {
                --top;
                stack[top - 1] =
                    op == OP_AND ? stack[top - 1] && stack[top] : stack[top - 1] || stack[top];
            }
        }
        return stack[0];
    }
};

struct Output {
    char bytes[OUTPUT_SIZE];
    int used = 0;
    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }
    void number(int value) {
        if (value < 0) {
            bytes[used++] = '-';
            value = -value;
        }
        char digits[POINT_RESERVE];
        int count = 0;
        do {
            digits[count++] = char('0' + value % DECIMAL_BASE);
            value /= DECIMAL_BASE;
        } while (value);
        while (count)
            bytes[used++] = digits[--count];
    }
    void point(int x, int y) {
        if (used + POINT_RESERVE > OUTPUT_SIZE)
            flush();
        number(x);
        bytes[used++] = ' ';
        number(y);
        bytes[used++] = '\n';
    }
};

int main() {
    char expression[EXPRESSION_LIMIT + LINE_END_RESERVE];
    if (!fgets(expression, sizeof(expression), stdin))
        return 0;
    Parser parser{expression};
    parser.next();
    parser.disjunction();
    int n = 0, m = 0, k = 0;
    if (scanf("%d %d %d", &n, &m, &k) != INPUT_FIELDS)
        return 0;
    int width = 2 * n + 1;
    std::vector<uint8_t> field(width * width);
    for (int i = 0; i < m; ++i) {
        int x = 0, y = 0;
        scanf("%d %d", &x, &y);
        field[(x + n) * width + y + n] = FORK;
    }
    for (int i = 0; i < k; ++i) {
        int x = 0, y = 0;
        char name = 0;
        scanf("%d %d %c", &x, &y, &name);
        field[(x + n) * width + y + n] = uint8_t(name - 'A' + SWITCH_OFFSET);
    }
    Output output;
    int x = 0, y = 0, dx = 1, dy = 0;
    uint32_t registers = 0, cachedMask = 0;
    bool cached = false, known = false;
    while (-n <= x && x <= n && -n <= y && y <= n) {
        output.point(x, y);
        uint8_t object = field[(x + n) * width + y + n];
        if (object >= SWITCH_OFFSET)
            registers ^= uint32_t(1) << (object - SWITCH_OFFSET);
        else if (object == FORK) {
            uint32_t mask = registers & parser.relevant;
            if (!known || mask != cachedMask) {
                cached = parser.value(mask);
                cachedMask = mask;
                known = true;
            }
            int nextX = cached ? dy : -dy;
            dy = cached ? -dx : dx;
            dx = nextX;
        }
        x += dx;
        y += dy;
    }
    output.flush();
}
