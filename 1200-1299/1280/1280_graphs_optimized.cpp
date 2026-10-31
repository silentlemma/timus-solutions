#include <bitset>
#include <cstdio>

// refills allow arbitrarily long input with only four kibibytes of storage.
const int INPUT_BUFFER = 4096;
char input_buffer[INPUT_BUFFER];
int input_pos = 0, input_len = 0;

int read_byte() {
    if (input_pos == input_len) {
        input_len = static_cast<int>(fread(input_buffer, 1, INPUT_BUFFER, stdin));
        input_pos = 0;
        if (input_len == 0)
            return EOF;
    }
    return input_buffer[input_pos++];
}

int next_int() {
    int c = read_byte();
    while (c != EOF && c <= ' ')
        c = read_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read_byte();
    }
    return value;
}

const int MAX_SUBJECTS = 1000;
// n <= 1000: one bit per possible rule uses about 125 kibibytes.
std::bitset<MAX_SUBJECTS + 1> rules[MAX_SUBJECTS + 1];
int place[MAX_SUBJECTS + 1];
int main() {
    int n = next_int(), m = next_int();
    for (int i = 0; i < m; i++) {
        int from = next_int(), to = next_int();
        rules[from].set(to);
    }
    for (int i = 0; i < n; i++)
        place[next_int()] = i;
    // the plan is right exactly when every rule points forward in it; a
    // rule from a subject to itself can never hold
    bool ok = true;
    for (int from = 1; from <= n; from++)
        for (int to = 1; to <= n; to++)
            if (rules[from][to] && place[from] >= place[to])
                ok = false;
    puts(ok ? "YES" : "NO");
}
