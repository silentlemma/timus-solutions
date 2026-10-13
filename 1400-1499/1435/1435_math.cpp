#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const long long NINE = 9;
const long long BASE = 10;
const int CHUNK = 1 << 16;

// the whole input at once: 200 000 numbers are too slow for scanf here
string input;
size_t pos = 0;

string word() {
    while (pos < input.size() && (input[pos] < '0' || input[pos] > '9'))
        pos++;
    size_t start = pos;
    while (pos < input.size() && input[pos] >= '0' && input[pos] <= '9')
        pos++;
    return input.substr(start, pos - start);
}

int main() {
    char buffer[CHUNK];
    for (size_t got; (got = fread(buffer, 1, CHUNK, stdin)) > 0;)
        input.append(buffer, got);
    int n = stoi(word());
    vector<string> records(n);
    long long total = 0;
    for (string &r : records) {
        r = word();
        total += stoll(r);
    }
    long long diff = stoll(word()) - total;
    if (diff == 0) {
        printf("Input has no error.\n");
        return 0;
    }
    // swapping digits a (at 10^(i+1)) and b (at 10^i) adds 9 * (b - a) * 10^i
    if (diff % NINE == 0) {
        long long step = diff / NINE;
        int place = 0;
        while (step % BASE == 0) {
            step /= BASE;
            place++;
        }
        if (llabs(step) < BASE)
            for (int number = 0; number < n; number++) {
                string &digits = records[number];
                int hi = (int)digits.size() - 2 - place; // index of the digit at 10^(i+1)
                if (hi < 0 || digits[hi + 1] - digits[hi] != step)
                    continue;
                if (hi == 0 && digits[1] == '0')
                    continue; // the swap would make a leading zero
                swap(digits[hi], digits[hi + 1]);
                printf("Error in record #%d. Correct number is: %s.\n", number + 1, digits.c_str());
                return 0;
            }
    }
    printf("Unrecoverable error.\n");
}
