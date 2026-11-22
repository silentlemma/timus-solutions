#include <algorithm>
#include <cstdio>
#include <vector>

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

    void word(char *text) {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        while (c > ' ') {
            *text++ = c;
            c = byte();
        }
        *text = 0;
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

constexpr int MAX_OPERATIONS = 100000, COMMAND_SIZE = 8, PRICE_SIZE = 16;
constexpr int CENTS = 100, DECIMAL_PLACES = 2, BID = -1, DEL = -2;

struct Operation {
    int price, amount;
};

int price(const char *text) {
    int whole = 0, fraction = 0, digits = 0;
    while (*text >= '0' && *text <= '9')
        whole = whole * 10 + *text++ - '0';
    if (*text == '.') {
        ++text;
        while (*text >= '0' && *text <= '9') {
            fraction = fraction * 10 + *text++ - '0';
            ++digits;
        }
    }
    while (digits++ < DECIMAL_PLACES)
        fraction *= 10;
    return whole * CENTS + fraction;
}

int main() {
    std::vector<Operation> operations;
    std::vector<int> prices;
    operations.reserve(MAX_OPERATIONS);
    prices.reserve(MAX_OPERATIONS);
    Input input;
    char command[COMMAND_SIZE], token[PRICE_SIZE];
    for (;;) {
        input.word(command);
        if (command[0] == 'Q' || command[0] == 0)
            break;
        input.word(token);
        int value = price(token), amount;
        if (command[0] == 'B') {
            amount = BID;
            prices.push_back(value);
        } else if (command[0] == 'D')
            amount = DEL;
        else
            amount = input.number();
        operations.push_back({value, amount});
    }
    std::sort(prices.begin(), prices.end());
    prices.erase(std::unique(prices.begin(), prices.end()), prices.end());
    std::vector<int> tree(prices.size() + 1);
    int active = 0;
    long long revenue = 0;
    for (const auto &operation : operations) {
        int index =
            std::lower_bound(prices.begin(), prices.end(), operation.price) - prices.begin();
        if (operation.amount < 0) {
            int delta = operation.amount == BID ? 1 : -1;
            active += delta;
            for (++index; index < static_cast<int>(tree.size()); index += index & -index) {
                tree[index] += delta;
            }
        } else {
            // lower_bound counts strictly cheaper prices, retaining equal bids for the sale.
            int cheaper = 0;
            for (; index > 0; index -= index & -index)
                cheaper += tree[index];
            revenue += std::min(operation.amount, active - cheaper);
        }
    }
    printf("%lld.%02lld\n", revenue / CENTS, revenue % CENTS);
}
