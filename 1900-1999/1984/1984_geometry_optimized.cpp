#include <cmath>
#include <cstdio>

const int OUTPUT_DIGITS = 10;

int main() {
    int count;
    scanf("%d", &count);
    double radius = count == 1 ? 1.0 : 1.0 + 1.0 / std::sin(std::acos(-1.0) / count);
    printf("%.*f\n", OUTPUT_DIGITS, radius);
}
