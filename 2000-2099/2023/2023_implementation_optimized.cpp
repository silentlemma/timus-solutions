#include <cstdio>
#include <cstdlib>

int main() {
    int position = 0;
    int steps = 0;
    // a label's only capital letter is its first one, and the first letters
    // tell the positions apart: A P O R, B M S and the rest
    for (int c; (c = getchar()) != EOF;) {
        if (c < 'A' || c > 'Z')
            continue;
        int target = 2;
        switch (c) {
        case 'A':
        case 'P':
        case 'O':
        case 'R':
            target = 0;
            break;
        case 'B':
        case 'M':
        case 'S':
            target = 1;
            break;
        }
        steps += std::abs(target - position);
        position = target;
    }
    printf("%d\n", steps);
}
