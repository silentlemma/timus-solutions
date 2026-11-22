#include <algorithm>
#include <cstdio>
#include <cstring>
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

struct Request {
    int start, next;
};

int main() {
    Input input;
    Output output;
    int stops = input.number(), capacity = input.number();
    int requests = input.number(), price = input.number();
    std::vector<int> firstAtEnd(stops + 1);
    std::vector<Request> trips(requests + 1);
    for (int id = 1; id <= requests; ++id) {
        int start = input.number(), end = input.number();
        trips[id] = {start, firstAtEnd[end]};
        firstAtEnd[end] = id;
    }

    std::vector<int> seatEnds(capacity);
    std::vector<int> chosen;
    chosen.reserve(requests);
    // Finish earlier trips first and use the latest seat that is already free.
    for (int end = 1; end <= stops; ++end) {
        for (int id = firstAtEnd[end]; id != 0; id = trips[id].next) {
            auto after = std::upper_bound(seatEnds.begin(), seatEnds.end(), trips[id].start);
            if (after == seatEnds.begin())
                continue;
            const int seat = static_cast<int>(after - seatEnds.begin()) - 1;
            // Destinations are nondecreasing; the replacement belongs at the end.
            std::memmove(seatEnds.data() + seat, seatEnds.data() + seat + 1,
                         (capacity - seat - 1) * sizeof(int));
            seatEnds.back() = end;
            chosen.push_back(id);
        }
    }
    output.number(static_cast<unsigned long long>(chosen.size()) * price);
    output.byte('\n');
    for (std::size_t i = 0; i < chosen.size(); ++i) {
        if (i)
            output.byte(' ');
        output.number(chosen[i]);
    }
    output.byte('\n');
    output.flush();
}
