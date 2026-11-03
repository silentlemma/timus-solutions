#include <cstdio>
#include <utility>
#include <vector>

const int BUFFER_SIZE = 4096;
char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (available == 0)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int first_bad(const std::vector<int> &a, int direction) {
    int i = 0, n = static_cast<int>(a.size());
    while (i + 1 < n && a[i] * direction <= a[i + 1] * direction)
        i++;
    return i;
}

int main() {
    // Buffer the large input; the boundary scans themselves remain linear.
    int n = next_int();
    std::vector<int> a(n);
    for (int &v : a)
        v = next_int();
    int up = first_bad(a, 1), down = first_bad(a, -1);
    if (up == n - 1 || down == n - 1) {
        puts("Nothing to do here");
        return 0;
    }
    for (int direction : {1, -1}) {
        int left = direction == 1 ? up : down, right = n - 1;
        // Equal runs can hide the actual swapped endpoint behind a violation.
        while (left > 0 && a[left - 1] == a[left])
            left--;
        while (a[right - 1] * direction <= a[right] * direction)
            right--;
        while (right + 1 < n && a[right + 1] == a[right])
            right++;
        std::swap(a[left], a[right]);
        if (first_bad(a, direction) == n - 1) {
            printf("Yes\n%d %d\n", left + 1, right + 1);
            return 0;
        }
        std::swap(a[left], a[right]);
    }
    puts("No hope");
}
