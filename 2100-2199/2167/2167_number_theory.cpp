#include <cstdio>

constexpr int BITS = 20;
constexpr int LIMIT = 1 << BITS;
bool composite[LIMIT] = {true, true};

int main() {
    for (int prime = 2; prime * prime < LIMIT; ++prime) {
        if (!composite[prime]) {
            for (int multiple = prime * prime; multiple < LIMIT; multiple += prime) {
                composite[multiple] = true;
            }
        }
    }

    int queries;
    scanf("%d", &queries);
    while (queries--) {
        int value;
        scanf("%d", &value);
        int key = 0;
        while (composite[value ^ key]) {
            ++key;
        }
        printf("%d\n", key);
    }
}
