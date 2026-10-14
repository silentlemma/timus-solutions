#include <iostream>
#include <string>
#include <vector>
using namespace std;

// the places a stick can take in one cell of the picture
enum {
    TOP = 1,
    MIDDLE = TOP << 1,
    BOTTOM = MIDDLE << 1,
    UPPER_LEFT = BOTTOM << 1,
    UPPER_RIGHT = UPPER_LEFT << 1,
    LOWER_LEFT = UPPER_RIGHT << 1,
    LOWER_RIGHT = LOWER_LEFT << 1,
    UPPER_SLASH = LOWER_RIGHT << 1,
    LOWER_SLASH = UPPER_SLASH << 1,
    PLUS_UPRIGHT = LOWER_SLASH << 1,
    EQUAL_UPPER = PLUS_UPRIGHT << 1,
    EQUAL_LOWER = EQUAL_UPPER << 1,
    SIDES = UPPER_LEFT | UPPER_RIGHT | LOWER_LEFT | LOWER_RIGHT,
};
const int DIGIT_SHAPE[] = {
    TOP | SIDES | BOTTOM,
    UPPER_SLASH | UPPER_RIGHT | LOWER_RIGHT,
    TOP | UPPER_RIGHT | LOWER_SLASH | BOTTOM,
    TOP | UPPER_SLASH | MIDDLE | LOWER_SLASH,
    UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_RIGHT,
    TOP | UPPER_LEFT | MIDDLE | LOWER_RIGHT | BOTTOM,
    UPPER_SLASH | MIDDLE | LOWER_LEFT | LOWER_RIGHT | BOTTOM,
    TOP | UPPER_SLASH | LOWER_LEFT,
    TOP | SIDES | MIDDLE | BOTTOM,
    TOP | UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_SLASH,
};
const int PLUS_SHAPE = MIDDLE | PLUS_UPRIGHT; // the bar lies where a middle stick does
const int EQUAL_SHAPE = EQUAL_UPPER | EQUAL_LOWER;
const int LONGEST = 8; // digits in a number
const int BASE = 10;
const int NONE = -1;

int shapeOf(char c) {
    return c == '+' ? PLUS_SHAPE : c == '=' ? EQUAL_SHAPE : DIGIT_SHAPE[c - '0'];
}
int sticks(int shape) { return __builtin_popcount(shape); }

struct Step {
    int kept = NONE; // sticks kept in place so far, NONE if unreachable
    int dx, dy, dz, carry, used;
};

string solve(const string &text, int k) {
    int n = text.size(), total = 0;
    vector<int> cells(n);
    for (int i = 0; i < n; i++)
        total += sticks(cells[i] = shapeOf(text[i]));
    auto kept = [&](int pos, int shape) { return sticks(cells[pos] & shape); };
    for (int lenX = 1; lenX <= LONGEST; lenX++)
        for (int lenY = 1; lenY <= LONGEST; lenY++) {
            int lenZ = n - 2 - lenX - lenY;
            // no leading zeros, so z has at least as many digits as x and y
            if (lenZ < max(lenX, lenY) || lenZ > LONGEST)
                continue;
            int plus = lenX, equal = lenX + lenY + 1;
            // table[col][carry][used]: the best way to fill col columns from the right
            vector<vector<vector<Step>>> table(lenZ + 1,
                                               vector<vector<Step>>(2, vector<Step>(total + 1)));
            table[0][0][sticks(PLUS_SHAPE) + sticks(EQUAL_SHAPE)].kept =
                kept(plus, PLUS_SHAPE) + kept(equal, EQUAL_SHAPE);
            for (int col = 0; col < lenZ; col++) {
                int posX = col < lenX ? lenX - 1 - col : NONE;
                int posY = col < lenY ? lenX + lenY - col : NONE;
                int posZ = n - 1 - col;
                for (int carry = 0; carry < 2; carry++)
                    for (int used = 0; used <= total; used++) {
                        int have = table[col][carry][used].kept;
                        if (have == NONE)
                            continue;
                        for (int dx = 0; dx < (posX == NONE ? 1 : BASE); dx++) {
                            if (posX != NONE && dx == 0 && col == lenX - 1 && lenX > 1)
                                continue;
                            for (int dy = 0; dy < (posY == NONE ? 1 : BASE); dy++) {
                                if (posY != NONE && dy == 0 && col == lenY - 1 && lenY > 1)
                                    continue;
                                int dz = (dx + dy + carry) % BASE, out = (dx + dy + carry) / BASE;
                                if (dz == 0 && col == lenZ - 1 && lenZ > 1)
                                    continue;
                                int more = sticks(DIGIT_SHAPE[dz]);
                                int gain = kept(posZ, DIGIT_SHAPE[dz]);
                                if (posX != NONE) {
                                    more += sticks(DIGIT_SHAPE[dx]);
                                    gain += kept(posX, DIGIT_SHAPE[dx]);
                                }
                                if (posY != NONE) {
                                    more += sticks(DIGIT_SHAPE[dy]);
                                    gain += kept(posY, DIGIT_SHAPE[dy]);
                                }
                                if (used + more > total)
                                    continue;
                                Step &next = table[col + 1][out][used + more];
                                if (next.kept < have + gain)
                                    next = {have + gain, dx, dy, dz, carry, used};
                            }
                        }
                    }
            }
            // every stick must be used, and the moved ones are those not kept
            const Step &last = table[lenZ][0][total];
            if (last.kept == NONE || total - last.kept > k)
                continue;
            string x(lenX, '0'), y(lenY, '0'), z(lenZ, '0');
            int carry = 0, used = total;
            for (int col = lenZ; col > 0; col--) {
                const Step &s = table[col][carry][used];
                int c = col - 1;
                if (c < lenX)
                    x[lenX - 1 - c] = '0' + s.dx;
                if (c < lenY)
                    y[lenY - 1 - c] = '0' + s.dy;
                z[lenZ - 1 - c] = '0' + s.dz;
                carry = s.carry;
                used = s.used;
            }
            return x + "+" + y + "=" + z;
        }
    return "Impossible";
}

int main() {
    // the expression may be written with spaces, K comes last
    vector<string> tokens;
    string token;
    while (cin >> token)
        tokens.push_back(token);
    string text;
    for (size_t i = 0; i + 1 < tokens.size(); i++)
        text += tokens[i];
    cout << solve(text, stoi(tokens.back())) << "\n";
}
