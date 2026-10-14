#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int CELLS = 4;                         // the program needs at most four cells
const int VALUES = 27;                       // a cell holds 0 or a letter, kept as 0 or 1 to 26
const int OTHERS = VALUES * VALUES * VALUES; // states of the cells away from the pointer
const int STATES = CELLS * OTHERS;
const int LETTER_BASE = 'a' - 1;
const int UNREACHABLE = 1 << 30;

int main() {
    string s;
    cin >> s;
    // a state, after a letter is printed, is the pointer's cell (holding that
    // letter) and the values of the other three cells, left to right; the
    // used cells form a block of four that holds the start cell somewhere
    vector<int> cost(STATES, UNREACHABLE);
    for (int start = 0; start < CELLS; start++)
        cost[start * OTHERS] = 0;
    vector<vector<int>> cameFrom;
    int previous = 0; // the value under the pointer: 0 before the first letter
    for (char c : s) {
        int letter = c - LETTER_BASE;
        vector<int> next(STATES, UNREACHABLE), back(STATES, -1);
        for (int state = 0; state < STATES; state++) {
            int here = cost[state];
            if (here == UNREACHABLE)
                continue;
            int p = state / OTHERS, rest = state % OTHERS;
            int digits[CELLS - 1] = {rest / (VALUES * VALUES), rest / VALUES % VALUES,
                                     rest % VALUES};
            int w[CELLS];
            for (int cell = 0, k = 0; cell < CELLS; cell++)
                w[cell] = cell == p ? previous : digits[k++];
            for (int q = 0; q < CELLS; q++) {
                int change = w[q] ? letter - w[q] : letter + LETTER_BASE;
                int total = here + abs(p - q) + abs(change) + 1;
                int code = 0;
                for (int cell = 0; cell < CELLS; cell++)
                    if (cell != q)
                        code = code * VALUES + w[cell];
                code += q * OTHERS;
                if (total < next[code]) {
                    next[code] = total;
                    back[code] = state;
                }
            }
        }
        cameFrom.push_back(back);
        cost = next;
        previous = letter;
    }
    // walk back to recover the cells used, then write the program
    int state = 0;
    for (int st = 0; st < STATES; st++)
        if (cost[st] < cost[state])
            state = st;
    vector<int> cells(s.size() + 1);
    for (int i = s.size(); i > 0; i--) {
        cells[i] = state / OTHERS;
        state = cameFrom[i - 1][state];
    }
    cells[0] = state / OTHERS;
    int values[CELLS] = {};
    string out;
    for (size_t i = 0; i < s.size(); i++) {
        int p = cells[i], q = cells[i + 1], letter = s[i] - LETTER_BASE;
        out += string(abs(q - p), q > p ? '>' : '<');
        int change = values[q] ? letter - values[q] : letter + LETTER_BASE;
        out += string(abs(change), change > 0 ? '+' : '-');
        out += '.';
        values[q] = letter;
    }
    printf("%s\n", out.c_str());
}
