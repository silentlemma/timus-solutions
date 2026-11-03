#include <cstdio>
#include <iostream>
#include <iterator>
#include <string>
using namespace std;

const int WALL = 36, SMALLEST = 2;
int digit(unsigned char c) {
    if (c >= '0' && c <= '9')
        return c - '0';
    if (c >= 'A' && c <= 'Z')
        return c - 'A' + 10;
    return WALL;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string text((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    int best = -1, bestBase = SMALLEST;
    for (int base = SMALLEST; base <= WALL; base++) {
        bool inside = false;
        int count = 0;
        for (unsigned char c : text) {
            bool current = digit(c) < base;
            if (current && !inside)
                count++;
            inside = current;
        }
        if (count > best) {
            best = count;
            bestBase = base;
        }
    }
    printf("%d %d\n", bestBase, best);
}
