#include <cstdio>
#include <vector>

int main() {
    long long k;
    scanf("%lld", &k);
    // from the BELL&RET cell upwards: "CALL i + 1" at cell i doubles the
    // bells made from the next cell, a call of the last cell adds one more,
    // so the binary digits of K give the cells
    std::vector<bool> doubles;
    int top = 0;
    while (k >> (top + 1))
        top++;
    for (int b = top - 1; b >= 0; b--) {
        doubles.push_back(true);
        if (k >> b & 1)
            doubles.push_back(false);
    }
    int last = doubles.size();
    for (int cell = 0; cell < last; cell++)
        printf("CALL %d\n", doubles[last - 1 - cell] ? cell + 1 : last);
    printf("BELL&RET\n");
}
