#include <cstdio>

// scanf and puts instead of iostream, which needs less memory
int main() {
    int size;
    if (scanf("%d", &size) != 1)
        return 0;
    int total = size * (size + 1) / 2;
    puts(total % 2 == 0 ? "black" : "grimy");
}
