#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

const int LONGEST = 100, TOP = 9, MAX_SUM = LONGEST * TOP, NONE = LONGEST + 1;
int low[MAX_SUM + 1], high[MAX_SUM + 1], offset[MAX_SUM + 2];
std::vector<unsigned char> fewest;

int lookup(int total, int squares) {
    if (total < 0 || total > MAX_SUM || squares < total || (squares - total) % 2)
        return NONE;
    int b = (squares - total) / 2;
    if (b < low[total] || b > high[total])
        return NONE;
    return fewest[offset[total] + b - low[total]];
}

int main() {
    for (int total = 0; total <= MAX_SUM; total++) {
        // Parity leaves b=(square_sum-total)/2. Balance 100 slots for its
        // minimum and pack nines for its maximum; other cells cannot occur.
        int q = total / LONGEST, r = total % LONGEST;
        int least = (LONGEST - r) * q * q + r * (q + 1) * (q + 1);
        q = total / TOP;
        r = total % TOP;
        int greatest = q * TOP * TOP + r * r;
        low[total] = (least - total) / 2;
        high[total] = (greatest - total) / 2;
        offset[total + 1] = offset[total] + high[total] - low[total] + 1;
    }
    fewest.assign(offset[MAX_SUM + 1], NONE);
    fewest[0] = 0;
    for (int total = 1; total <= MAX_SUM; total++) {
        int destination = offset[total] - low[total];
        for (int digit = 1; digit <= std::min(TOP, total); digit++) {
            int previous = total - digit, delta = digit * (digit - 1) / 2;
            int first = std::max(low[total], low[previous] + delta);
            int last = std::min(high[total], high[previous] + delta);
            int shift = offset[previous] - low[previous] - delta - destination;
            for (int position = destination + first; position <= destination + last; position++) {
                int value = fewest[position + shift] + 1;
                if (value < fewest[position])
                    fewest[position] = value;
            }
        }
    }
    int tests;
    scanf("%d", &tests);
    std::string output;
    while (tests--) {
        int total, squares;
        scanf("%d %d", &total, &squares);
        int size = lookup(total, squares);
        if (size == NONE) {
            output += "No solution\n";
            continue;
        }
        int digit = 1;
        for (int left = size - 1; left >= 0; left--) {
            while (lookup(total - digit, squares - digit * digit) != left)
                digit++;
            output += char('0' + digit);
            total -= digit;
            squares -= digit * digit;
        }
        output += '\n';
    }
    printf("%s", output.c_str());
}
