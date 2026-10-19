#include <array>
#include <cctype>
#include <climits>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

const int DIMENSIONS = 3;
using Vec = std::array<int, DIMENSIONS>;

const std::string NAMES = "UDLRFB";
// the outward normal of every face, in the order of NAMES
const Vec FACES[] = {{0, 1, 0}, {0, -1, 0}, {-1, 0, 0}, {1, 0, 0}, {0, 0, 1}, {0, 0, -1}};

static int dot(const Vec &a, const Vec &b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

// a quarter turn of v about the axis a: counter-clockwise seen from the tip
// of a for sign 1, clockwise for sign -1
static Vec turn(const Vec &v, const Vec &a, int sign) {
    Vec cross = {a[1] * v[2] - a[2] * v[1], a[2] * v[0] - a[0] * v[2], a[0] * v[1] - a[1] * v[0]};
    int along = dot(a, v);
    Vec r;
    for (size_t k = 0; k < r.size(); k++) r[k] = sign * cross[k] + a[k] * along;
    return r;
}

int main() {
    std::string moves;
    std::cin >> moves;
    // a sticker is a cubie position with every coordinate in -1..1 and the
    // outward normal of a face that cubie touches
    std::vector<std::pair<Vec, Vec>> stickers;
    for (int x = -1; x <= 1; x++) {
        for (int y = -1; y <= 1; y++) {
            for (int z = -1; z <= 1; z++) {
                for (const Vec &n : FACES) {
                    if (dot({x, y, z}, n) == 1) stickers.push_back({{x, y, z}, n});
                }
            }
        }
    }
    int count = stickers.size();
    std::map<std::pair<Vec, Vec>, int> index;
    for (int i = 0; i < count; i++) index[stickers[i]] = i;
    // the place every sticker moves to under each letter
    std::map<char, std::vector<int>> table;
    for (size_t f = 0; f < NAMES.size(); f++) {
        const Vec &a = FACES[f];
        for (int sign : {1, -1}) {
            char letter = sign == 1 ? NAMES[f] : (char)std::tolower(NAMES[f]);
            std::vector<int> to(count);
            for (int i = 0; i < count; i++) {
                const auto &[p, n] = stickers[i];
                to[i] = dot(p, a) == 1 ? index[{turn(p, a, sign), turn(n, a, sign)}] : i;
            }
            table[letter] = to;
        }
    }
    std::vector<const std::vector<int> *> byLetter(1 << CHAR_BIT, nullptr);
    for (auto &[letter, to] : table) byLetter[(unsigned char)letter] = &to;
    // where each sticker ends up after the whole sequence
    std::vector<int> place(count);
    std::iota(place.begin(), place.end(), 0);
    for (char c : moves) {
        const std::vector<int> &to = *byLetter[(unsigned char)c];
        for (int &p : place) p = to[p];
    }
    // the sequence returns the cube after the lcm of the cycle lengths
    long long order = 1;
    std::vector<bool> seen(count, false);
    for (int start = 0; start < count; start++) {
        long long length = 0;
        for (int i = start; !seen[i]; i = place[i]) {
            seen[i] = true;
            length++;
        }
        if (length) order = std::lcm(order, length);
    }
    std::cout << order - 1 << "\n";
    return 0;
}
