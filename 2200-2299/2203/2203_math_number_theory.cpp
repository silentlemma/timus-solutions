#include <cstdint>
#include <iostream>

using Integer = std::int64_t;

Integer gcd(Integer a, Integer b) {
    while (b != 0) {
        Integer remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

Integer inverse(Integer value, Integer modulus) {
    Integer remainder = modulus;
    Integer coefficient = 1;
    Integer next_coefficient = 0;
    while (remainder != 0) {
        Integer quotient = value / remainder;
        Integer next_remainder = value - quotient * remainder;
        value = remainder;
        remainder = next_remainder;
        Integer next = coefficient - quotient * next_coefficient;
        coefficient = next_coefficient;
        next_coefficient = next;
    }
    return (coefficient % modulus + modulus) % modulus;
}

Integer visits(Integer a, Integer b, Integer x, Integer y, Integer n) {
    if (x <= a || y <= b) {
        return n;
    }
    Integer divisor_a = gcd(a, x);
    Integer divisor_b = gcd(b, y);
    Integer period_a = x / divisor_a;
    Integer period_b = y / divisor_b;
    Integer events_a = a / divisor_a;
    Integer events_b = b / divisor_b;
    Integer common = gcd(period_a, period_b);
    Integer modulus = period_b / common;
    Integer multiplier = inverse(period_a / common, modulus);
    Integer period = period_a * modulus;
    Integer answer = (n * a + x - 1) / x + (n * b + y - 1) / y;

    // Purchase indices are floor(j * period / events), starting with index zero.
    for (Integer i = 0; i < events_a; ++i) {
        Integer first = i * period_a / events_a;
        for (Integer j = 0; j < events_b; ++j) {
            Integer second = j * period_b / events_b;
            Integer difference = second - first;
            if (difference % common != 0) {
                continue;
            }
            // CRT gives one shared purchase index per common period.
            Integer shift = (difference / common * multiplier) % modulus;
            if (shift < 0) {
                shift += modulus;
            }
            Integer start = first + period_a * shift;
            if (start < n) {
                answer -= 1 + (n - 1 - start) / period;
            }
        }
    }
    return answer;
}

int main() {
    Integer a, b, x, y, n;
    std::cin >> a >> b >> x >> y >> n;
    std::cout << visits(a, b, x, y, n) << '\n';
}
