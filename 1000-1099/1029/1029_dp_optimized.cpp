#include <algorithm>
#include <cstdint>
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

enum class Parent : std::uint8_t { below, left, right };

int main() {
    Input input;
    Output output;
    int floors = input.number(), width = input.number();
    std::vector<Parent> parents(floors * width, Parent::below);
    std::vector<long long> cost(width), fee(width);
    for (int floor = 0; floor < floors; ++floor) {
        Parent *directions = parents.data() + floor * width;
        for (int room = 0; room < width; ++room) {
            fee[room] = input.number();
            cost[room] += fee[room];
        }
        for (int room = 1; room < width; ++room) {
            const long long candidate = cost[room - 1] + fee[room];
            if (candidate < cost[room]) {
                cost[room] = candidate;
                directions[room] = Parent::left;
            }
        }
        for (int room = width - 2; room >= 0; --room) {
            const long long candidate = cost[room + 1] + fee[room];
            if (candidate < cost[room]) {
                cost[room] = candidate;
                directions[room] = Parent::right;
            }
        }
    }
    int room = static_cast<int>(std::min_element(cost.begin(), cost.end()) - cost.begin());
    int floor = floors - 1;
    std::vector<std::uint16_t> path;
    while (floor >= 0) {
        path.push_back(room + 1);
        switch (parents[floor * width + room]) {
        case Parent::below:
            --floor;
            break;
        case Parent::left:
            --room;
            break;
        case Parent::right:
            ++room;
            break;
        }
    }
    for (auto i = path.rbegin(); i != path.rend(); ++i) {
        output.number(*i);
        output.byte(i + 1 == path.rend() ? '\n' : ' ');
    }
    output.flush();
}
