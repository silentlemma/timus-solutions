#include <cstdio>
#include <map>
#include <vector>

using namespace std;

const long long MOD = 1000000000;
const int OPEN = 1, CLOSE = 2; // plugs are brackets: the two ends of one path
const int BITS = 2;            // a plug state keeps two bits per plug
const int MASK = (1 << BITS) - 1;

int width;

int get(int code, int k) { return code >> (BITS * k) & MASK; }

int with(int code, int k, int v) { return (code & ~(MASK << (BITS * k))) | v << (BITS * k); }

// the bracket matching plug k: rightwards for an opening one, leftwards otherwise
int partner(int code, int k) {
    int step = get(code, k) == OPEN ? 1 : -1, depth = 0;
    for (int j = k;; j += step) {
        if (get(code, j) == get(code, k))
            depth++;
        else if (get(code, j))
            depth--;
        if (depth == 0)
            return j;
    }
}

// run one row of cells over a plug state and return the states it can leave
// below; plug c is the left plug of cell c, plug c + 1 its upper plug
map<int, long long> rowMoves(int start, bool last) {
    map<int, long long> states = {{start << BITS, 1}};
    for (int c = 0; c < width; c++) {
        map<int, long long> next;
        for (auto [p, ways] : states) {
            int left = get(p, c), up = get(p, c + 1);
            auto put = [&](int q, int down, int right) {
                next[with(with(q, c, down), c + 1, right)] += ways;
            };
            if (!left && !up) {
                if (c + 1 < width && !last)
                    put(p, OPEN, CLOSE); // a new path turning right and down
            } else if (left && up) {
                int q = p;
                if (left == OPEN && up == CLOSE) {
                    // closing the cycle: only at the very last cell, with nothing else open
                    if (last && c == width - 1 && with(with(p, c, 0), c + 1, 0) == 0)
                        put(p, 0, 0);
                    continue;
                }
                if (left == OPEN && up == OPEN)
                    q = with(q, partner(q, c + 1), OPEN);
                else if (left == CLOSE && up == CLOSE)
                    q = with(q, partner(q, c), CLOSE);
                put(q, 0, 0);
            } else {
                int plug = left ? left : up;
                if (!last)
                    put(p, plug, 0);
                if (c + 1 < width)
                    put(p, 0, plug);
            }
        }
        states = next;
    }
    map<int, long long> result;
    for (auto [p, ways] : states)
        if (get(p, width) == 0)
            result[p] = ways % MOD;
    return result;
}

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &a, const Matrix &b) {
    int n = a.size();
    Matrix c(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++)
        for (int k = 0; k < n; k++)
            if (a[i][k])
                for (int j = 0; j < n; j++)
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
    return c;
}

int main() {
    long long height;
    scanf("%d %lld", &width, &height);
    // every plug state that a row can leave behind, reached from the empty one
    map<int, int> index = {{0, 0}};
    vector<int> order = {0};
    for (size_t i = 0; i < order.size(); i++)
        for (auto [t, ways] : rowMoves(order[i], false))
            if (!index.count(t)) {
                index[t] = order.size();
                order.push_back(t);
            }
    int size = order.size();
    Matrix step(size, vector<long long>(size, 0)), power(size, vector<long long>(size, 0));
    for (int i = 0; i < size; i++) {
        power[i][i] = 1;
        for (auto [t, ways] : rowMoves(order[i], false))
            step[i][index[t]] = ways;
    }
    // the first height - 1 rows by fast powering, then the last row that closes the cycle
    for (long long e = height - 1; e > 0; e >>= 1) {
        if (e & 1)
            power = multiply(power, step);
        step = multiply(step, step);
    }
    long long total = 0;
    for (int i = 0; i < size; i++) {
        auto closed = rowMoves(order[i], true);
        if (closed.count(0))
            total = (total + power[0][i] * closed[0]) % MOD;
    }
    printf("%lld\n", 2 * total % MOD); // every cycle can be walked in two directions
}
