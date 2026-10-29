#include <cstdio>

// the numbers are parsed with getchar instead of scanf
int nextInt() {
    int c = getchar();
    while (c <= ' ' && c != EOF)
        c = getchar();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    int n = nextInt();
    // the pocket is a stack: roll the balls in order, and whenever the top
    // one is the next ball the inspector took out, take it out
    // each ball is checked as it is read, so their order is never stored
    int *pocket = new int[n];
    int top = 0, next = 1;
    for (int i = 0; i < n; ++i) {
        int ball = nextInt();
        while (next <= ball)
            pocket[top++] = next++;
        if (top == 0 || pocket[top - 1] != ball) {
            puts("Cheater");
            delete[] pocket;
            return 0;
        }
        --top;
    }
    puts("Not a proof");
    delete[] pocket;
}
