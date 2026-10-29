#include <algorithm>
#include <cstdio>
#include <string>

using namespace std;

constexpr int COUNT = 3;

int apply(int x, char op, int y) {
    if (op == '*')
        return x * y;
    return op == '+' ? x + y : x - y;
}

// x op1 y op2 z, multiplication first
int evaluate(int x, char op1, int y, char op2, int z) {
    if (op2 == '*' && op1 != '*')
        return apply(x, op1, y * z);
    return apply(apply(x, op1, y), op2, z);
}

int main() {
    int v[COUNT];
    for (int &x : v)
        scanf("%d", &x);
    const string ops = "+-*";
    sort(v, v + COUNT);
    int best = v[0] + v[1] + v[2];
    do {
        for (char a : ops)
            for (char b : ops)
                best = min(best, evaluate(v[0], a, v[1], b, v[2]));
    } while (next_permutation(v, v + COUNT));
    printf("%d\n", best);
}
