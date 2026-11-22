#include <algorithm>
#include <cstdio>
#include <vector>

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
    void number(unsigned long long value) {
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

struct City {
    int joy = 0;
    int degree = 0, neighbors = 0, weights = 0;
    int first = 0, second = 0;
    int first_child = 0, second_child = 0;
};

int main() {
    Input input;
    Output output;
    int cities = input.number(), flights = input.number();
    std::vector<City> tree(cities + 1);
    for (int i = 1; i <= cities; ++i) {
        tree[i].joy = input.number();
    }
    const auto add = [&](int city, int neighbor, int joy) {
        ++tree[city].degree;
        tree[city].neighbors ^= neighbor;
        tree[city].weights ^= joy;
    };
    for (int i = 0; i < flights; ++i) {
        int a = input.number(), b = input.number(), joy = input.number();
        add(a, b, joy);
        add(b, a, joy);
    }

    std::vector<int> order;
    order.reserve(cities);
    for (int i = 1; i <= cities; ++i) {
        if (tree[i].degree <= 1)
            order.push_back(i);
    }
    int best = -1, center = 0;
    for (std::size_t i = 0; i < order.size(); ++i) {
        const int v = order[i];
        const City &city = tree[v];
        const int through = city.joy + city.first + city.second;
        if (through > best) {
            best = through;
            center = v;
        }
        if (city.degree == 0)
            continue;

        // At a leaf the two XOR accumulators identify its only remaining edge.
        const int parent = city.neighbors;
        const int weight = city.weights;
        City &above = tree[parent];
        above.neighbors ^= v;
        above.weights ^= weight;
        if (--above.degree == 1)
            order.push_back(parent);

        const int branch = weight + city.joy + city.first;
        if (branch > above.first) {
            above.second = above.first;
            above.second_child = above.first_child;
            above.first = branch;
            above.first_child = v;
        } else if (branch > above.second) {
            above.second = branch;
            above.second_child = v;
        }
    }

    order.clear();
    for (int v = tree[center].first_child; v; v = tree[v].first_child)
        order.push_back(v);
    std::reverse(order.begin(), order.end());
    order.push_back(center);
    for (int v = tree[center].second_child; v; v = tree[v].first_child)
        order.push_back(v);
    output.number(best);
    output.byte('\n');
    output.number(order.size());
    output.byte('\n');
    for (std::size_t i = 0; i < order.size(); ++i) {
        output.number(order[i]);
        output.byte(i + 1 == order.size() ? '\n' : ' ');
    }
    output.flush();
}
