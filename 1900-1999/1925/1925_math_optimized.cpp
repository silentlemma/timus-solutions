#include <cstdio>

// the pairs are added up as scanf reads them; the history is not stored
int main() {
    int count, current;
    scanf("%d%d", &count, &current);
    int answer = current - 2;
    for (int i = 0; i < count; ++i) {
        int displayed, entered;
        scanf("%d%d", &displayed, &entered);
        answer += displayed - entered - 2;
    }
    if (answer >= 0) {
        printf("%d\n", answer);
    } else {
        puts("Big Bang!");
    }
}
