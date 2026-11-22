#include <cstdio>
#include <string>
#include <unordered_map>
#include <utility>

constexpr int IO_SIZE = 4096;
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

const int MAX_PRODUCTS = 1000, MAX_CUSTOMERS = 1000, NAME_SIZE = 21;
struct Customer {
    int product, wanted, seen;
};
int stock[MAX_PRODUCTS + 1];
Customer line[MAX_CUSTOMERS];

int main() {
    Input input;
    int m = input.number();
    std::unordered_map<std::string, int> ids;
    ids.reserve(2 * m);
    const auto word = [&]() {
        std::string value;
        int c = input.byte();
        while (c >= 0 && c <= ' ')
            c = input.byte();
        while (c > ' ') {
            value += static_cast<char>(c);
            c = input.byte();
        }
        return value;
    };
    for (int id = 1; id <= m; id++) {
        stock[id] = input.number();
        word();
        ids[word()] = id;
    }
    int n = input.number();
    for (int i = 0; i < n; i++) {
        int amount = input.number();
        word();
        auto found = ids.find(word());
        line[i] = {found == ids.end() ? 0 : found->second, amount, -1};
    }
    int front = 0, minutes = 0;
    while (front < n) {
        Customer &customer = line[front];
        int &left = stock[customer.product];
        minutes++;
        if (left >= customer.wanted)
            left -= customer.wanted;
        else if (left == customer.seen)
            left = 0;
        else if (left > 0) {
            customer.seen = left;
            if (front + 1 == n)
                break;
            std::swap(line[front], line[front + 1]);
            continue;
        }
        front++;
    }
    printf("%d\n", minutes);
}
