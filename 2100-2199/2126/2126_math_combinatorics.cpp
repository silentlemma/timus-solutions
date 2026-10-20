#include <algorithm>
#include <iostream>
#include <vector>

using Integer = long long;
constexpr Integer CHOICES = 3;

Integer power(Integer base, Integer exponent, Integer modulus) {
    Integer result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent /= 2;
    }
    return result;
}

int main() {
    Integer n, modulus;
    std::cin >> n >> modulus;
    const Integer half = (modulus - 1) / 2;
    Integer exponent = 0;
    std::vector<Integer> digits;
    for (Integer remaining = n; remaining > 0; remaining /= modulus) {
        Integer digit = remaining % modulus;
        // Reflect central trinomial coefficients into the lower half.
        if (digit > half) {
            digit = modulus - 1 - digit;
            exponent += half - digit;
        }
        digits.push_back(digit);
    }
    std::sort(digits.begin(), digits.end());

    Integer index = 0, previous = 1, current = 1, factorial = 1;
    Integer numerator = 1, denominator = 1;
    for (Integer digit : digits) {
        while (index < digit) {
            ++index;
            const Integer before = index - 1;
            // F_i = i! * T_i avoids division inside the recurrence.
            const Integer next =
                ((2 * index - 1) * current + CHOICES * before * before * previous) % modulus;
            previous = current;
            current = next;
            factorial = factorial * index % modulus;
        }
        numerator = numerator * current % modulus;
        denominator = denominator * factorial % modulus;
    }

    Integer draws = numerator * power(denominator, modulus - 2, modulus) % modulus;
    draws = draws * power(modulus - CHOICES, exponent, modulus) % modulus;
    const Integer total = power(CHOICES, n, modulus);
    const Integer answer = (total - draws + modulus) % modulus * ((modulus + 1) / 2) % modulus;
    std::cout << answer << '\n';
}
