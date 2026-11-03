#include <cstdio>
#include <map>
#include <string>

const int MAX_NAME = 30;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::map<std::string, int> counts;
    int largest = 0;
    char prefecture[MAX_NAME + 1];
    for (int i = 0; i < (1 << n); i++) {
        // Names do not affect the answer; do not allocate a String for them.
        scanf("%*30s %30s", prefecture);
        int count = ++counts[prefecture];
        if (count > largest)
            largest = count;
    }
    int unsafe = 0;
    while ((1 << unsafe) < largest)
        unsafe++;
    printf("%d\n", n - unsafe);
}
