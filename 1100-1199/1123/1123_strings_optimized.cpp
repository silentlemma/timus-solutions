#include <cstdio>
#include <cstring>

const int MAX_DIGITS = 2001;

int main() {
    // the statement allows 2001 digits; each array also holds the terminator.
    char input[MAX_DIGITS + 1], best[MAX_DIGITS + 1];
    int size = 0, c;
    do {
        c = getchar();
    } while (c != EOF && c <= ' ');
    while (c >= '0' && c <= '9') {
        input[size++] = static_cast<char>(c);
        c = getchar();
    }
    input[size] = '\0';
    int start = 0;
    while (start + 1 < size && input[start] == '0')
        ++start;
    char *digits = input + start;
    int n = size - start;
    std::memcpy(best, digits, n + 1);
    for (int i = 0; i < n / 2; ++i)
        best[n - 1 - i] = best[i];
    if (std::strcmp(best, digits) < 0) {
        // an all-nine prefix already mirrors above the input, so carry stops.
        int middle = (n - 1) / 2;
        while (best[middle] == '9')
            best[middle--] = '0';
        ++best[middle];
        for (int i = 0; i < n / 2; ++i)
            best[n - 1 - i] = best[i];
    }
    puts(best);
}
