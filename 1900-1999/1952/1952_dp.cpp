#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Natural {
    static constexpr uint32_t BASE = 1000000000;
    static constexpr int DECIMAL_DIGITS = 9;
    static constexpr int BINARY_CHUNK_BITS = 29;
    std::vector<uint32_t> words;

    Natural(uint64_t value = 0) {
        while (value != 0) {
            words.push_back(static_cast<uint32_t>(value % BASE));
            value /= BASE;
        }
    }
    explicit Natural(const std::string &text) {
        for (size_t end = text.size(); end > 0;) {
            const size_t begin = end > DECIMAL_DIGITS ? end - DECIMAL_DIGITS : 0;
            words.push_back(static_cast<uint32_t>(std::stoul(text.substr(begin, end - begin))));
            end = begin;
        }
        trim();
    }
    void trim() {
        while (!words.empty() && words.back() == 0)
            words.pop_back();
    }
    bool zero() const { return words.empty(); }
    bool one() const { return words.size() == 1 && words[0] == 1; }
    int compare(const Natural &other) const {
        if (words.size() != other.words.size())
            return words.size() < other.words.size() ? -1 : 1;
        for (size_t i = words.size(); i > 0; --i) {
            if (words[i - 1] != other.words[i - 1])
                return words[i - 1] < other.words[i - 1] ? -1 : 1;
        }
        return 0;
    }
    bool operator==(const Natural &other) const { return words == other.words; }
    bool operator!=(const Natural &other) const { return !(*this == other); }
    bool operator<(const Natural &other) const { return compare(other) < 0; }
    Natural operator+(const Natural &other) const {
        Natural result;
        const size_t count = std::max(words.size(), other.words.size());
        result.words.resize(count);
        uint64_t carry = 0;
        for (size_t i = 0; i < count; ++i) {
            uint64_t value = carry;
            if (i < words.size())
                value += words[i];
            if (i < other.words.size())
                value += other.words[i];
            result.words[i] = static_cast<uint32_t>(value % BASE);
            carry = value / BASE;
        }
        if (carry != 0)
            result.words.push_back(static_cast<uint32_t>(carry));
        return result;
    }
    Natural operator-(const Natural &other) const {
        if (compare(other) < 0)
            throw std::logic_error("negative natural subtraction");
        Natural result;
        result.words.resize(words.size());
        int64_t borrow = 0;
        for (size_t i = 0; i < words.size(); ++i) {
            int64_t value = static_cast<int64_t>(words[i]) - borrow;
            if (i < other.words.size())
                value -= other.words[i];
            borrow = value < 0 ? 1 : 0;
            if (value < 0)
                value += BASE;
            result.words[i] = static_cast<uint32_t>(value);
        }
        result.trim();
        return result;
    }
    Natural multiplySmall(uint32_t other) const {
        if (other == 0 || zero())
            return Natural();
        Natural result;
        result.words.resize(words.size());
        uint64_t carry = 0;
        for (size_t i = 0; i < words.size(); ++i) {
            const uint64_t value = static_cast<uint64_t>(words[i]) * other + carry;
            result.words[i] = static_cast<uint32_t>(value % BASE);
            carry = value / BASE;
        }
        while (carry != 0) {
            result.words.push_back(static_cast<uint32_t>(carry % BASE));
            carry /= BASE;
        }
        return result;
    }
    Natural operator*(const Natural &other) const {
        if (zero() || other.zero())
            return Natural();
        Natural result;
        result.words.assign(words.size() + other.words.size() + 1, 0);
        for (size_t i = 0; i < words.size(); ++i) {
            uint64_t carry = 0;
            for (size_t j = 0; j < other.words.size() || carry != 0; ++j) {
                uint64_t value = result.words[i + j] + carry;
                if (j < other.words.size())
                    value += static_cast<uint64_t>(words[i]) * other.words[j];
                result.words[i + j] = static_cast<uint32_t>(value % BASE);
                carry = value / BASE;
            }
        }
        result.trim();
        return result;
    }
    std::pair<Natural, uint32_t> divideSmall(uint32_t other) const {
        if (other == 0)
            throw std::logic_error("zero divisor");
        Natural quotient;
        quotient.words.resize(words.size());
        uint64_t remainder = 0;
        for (size_t i = words.size(); i > 0; --i) {
            const uint64_t value = remainder * BASE + words[i - 1];
            quotient.words[i - 1] = static_cast<uint32_t>(value / other);
            remainder = value % other;
        }
        quotient.trim();
        return {std::move(quotient), static_cast<uint32_t>(remainder)};
    }
    void shiftBaseAdd(uint32_t word) {
        if (zero() && word == 0)
            return;
        words.insert(words.begin(), word);
    }
    std::pair<Natural, Natural> divide(const Natural &other) const {
        if (other.zero())
            throw std::logic_error("zero divisor");
        if (compare(other) < 0)
            return {Natural(), *this};
        if (other.words.size() == 1) {
            auto result = divideSmall(other.words[0]);
            return {std::move(result.first), Natural(result.second)};
        }
        const uint32_t normalizer = BASE / (other.words.back() + 1);
        const Natural dividend = multiplySmall(normalizer);
        const Natural divisor = other.multiplySmall(normalizer);
        Natural quotient, remainder;
        quotient.words.assign(dividend.words.size(), 0);
        const size_t width = divisor.words.size();
        for (size_t i = dividend.words.size(); i > 0; --i) {
            remainder.shiftBaseAdd(dividend.words[i - 1]);
            const uint64_t first = remainder.words.size() > width ? remainder.words[width] : 0;
            const uint64_t second =
                remainder.words.size() >= width ? remainder.words[width - 1] : 0;
            uint64_t estimate = (first * BASE + second) / divisor.words.back();
            estimate = std::min(estimate, static_cast<uint64_t>(BASE - 1));
            Natural product = divisor.multiplySmall(static_cast<uint32_t>(estimate));
            while (product.compare(remainder) > 0) {
                --estimate;
                product = product - divisor;
            }
            remainder = remainder - product;
            quotient.words[i - 1] = static_cast<uint32_t>(estimate);
        }
        quotient.trim();
        remainder = remainder.divideSmall(normalizer).first;
        return {std::move(quotient), std::move(remainder)};
    }
    Natural operator/(const Natural &other) const { return divide(other).first; }
    Natural operator%(const Natural &other) const { return divide(other).second; }
    static Natural gcd(Natural first, Natural second) {
        while (!second.zero()) {
            Natural remainder = first % second;
            first = std::move(second);
            second = std::move(remainder);
        }
        return first;
    }
    static Natural powerTen(int digits) {
        Natural result;
        result.words.assign(static_cast<size_t>(digits / DECIMAL_DIGITS) + 1, 0);
        uint32_t top = 1;
        for (int i = 0; i < digits % DECIMAL_DIGITS; ++i)
            top *= 10;
        result.words.back() = top;
        return result;
    }
    Natural shiftBinary(int count) const {
        Natural result = *this;
        while (count > 0) {
            const int chunk = std::min(count, BINARY_CHUNK_BITS);
            result = result.multiplySmall(uint32_t{1} << chunk);
            count -= chunk;
        }
        return result;
    }
    int decimalDigits() const {
        if (zero())
            return 1;
        int result = static_cast<int>(words.size() - 1) * DECIMAL_DIGITS;
        for (uint32_t top = words.back(); top != 0; top /= 10)
            ++result;
        return result;
    }
    Natural squareRoot() const {
        if (zero())
            return Natural();
        Natural current = powerTen((decimalDigits() + 1) / 2);
        while (true) {
            Natural next = (current + *this / current).divideSmall(2).first;
            if (next.compare(current) >= 0)
                return current;
            current = std::move(next);
        }
    }
    std::string str() const {
        if (zero())
            return "0";
        std::string result = std::to_string(words.back());
        for (size_t i = words.size() - 1; i > 0; --i) {
            const std::string part = std::to_string(words[i - 1]);
            result.append(DECIMAL_DIGITS - part.size(), '0');
            result += part;
        }
        return result;
    }
    long double approximate() const {
        long double result = 0;
        for (size_t i = words.size(); i > 0; --i)
            result = result * BASE + words[i - 1];
        return result;
    }
};

struct Rational {
    static constexpr int FRACTION_BITS = 52;
    static constexpr int EXPONENT_BIAS = 1023;
    static constexpr uint64_t FRACTION_MASK = (uint64_t{1} << FRACTION_BITS) - 1;
    int sign = 0;
    Natural numerator, denominator = Natural(1);

    Rational(int64_t value = 0) {
        sign = (value > 0) - (value < 0);
        const uint64_t absolute =
            value < 0 ? static_cast<uint64_t>(-(value + 1)) + 1 : static_cast<uint64_t>(value);
        numerator = Natural(absolute);
    }
    Rational(int sign, Natural numerator, Natural denominator, bool normalized = false)
        : sign(sign), numerator(std::move(numerator)), denominator(std::move(denominator)) {
        if (this->denominator.zero())
            throw std::logic_error("zero divisor");
        if (this->numerator.zero()) {
            this->sign = 0;
            this->denominator = Natural(1);
            return;
        }
        if (!normalized) {
            const Natural common = Natural::gcd(this->numerator, this->denominator);
            if (!common.one()) {
                this->numerator = this->numerator / common;
                this->denominator = this->denominator / common;
            }
        }
    }
    static Rational fraction(int64_t numerator, uint64_t denominator) {
        Rational result(numerator);
        return Rational(result.sign, std::move(result.numerator), Natural(denominator));
    }
    Rational operator-() const { return Rational(-sign, numerator, denominator, true); }
    Rational operator+(const Rational &other) const {
        if (sign == 0)
            return other;
        if (other.sign == 0)
            return *this;
        Natural first = numerator, second = other.numerator, den = denominator;
        if (denominator != other.denominator) {
            first = first * other.denominator;
            second = second * denominator;
            den = denominator * other.denominator;
        }
        if (sign == other.sign)
            return Rational(sign, first + second, std::move(den));
        const int order = first.compare(second);
        if (order == 0)
            return Rational();
        return order > 0 ? Rational(sign, first - second, std::move(den))
                         : Rational(other.sign, second - first, std::move(den));
    }
    Rational operator-(const Rational &other) const { return *this + -other; }
    Rational operator*(const Rational &other) const {
        if (sign == 0 || other.sign == 0)
            return Rational();
        return Rational(sign * other.sign, numerator * other.numerator,
                        denominator * other.denominator);
    }
    Rational divide(int64_t other) const {
        if (other <= 0)
            throw std::logic_error("nonpositive divisor");
        return Rational(sign, numerator, denominator * Natural(static_cast<uint64_t>(other)));
    }
    int compare(const Rational &other) const {
        if (sign != other.sign)
            return sign < other.sign ? -1 : 1;
        if (sign == 0)
            return 0;
        if (denominator == other.denominator)
            return sign * numerator.compare(other.numerator);
        return sign * (numerator * other.denominator).compare(other.numerator * denominator);
    }
    bool operator==(const Rational &other) const {
        return sign == other.sign && numerator == other.numerator &&
               denominator == other.denominator;
    }
    static Rational fromDouble(double value) {
        if (value == 0)
            return Rational();
        uint64_t raw;
        std::memcpy(&raw, &value, sizeof(raw));
        int exponent = static_cast<int>((raw >> FRACTION_BITS) & (2 * EXPONENT_BIAS + 1));
        uint64_t mantissa = raw & FRACTION_MASK;
        if (exponent == 0)
            exponent = 1 - EXPONENT_BIAS - FRACTION_BITS;
        else {
            mantissa |= uint64_t{1} << FRACTION_BITS;
            exponent -= EXPONENT_BIAS + FRACTION_BITS;
        }
        Natural numerator(mantissa), denominator(1);
        if (exponent >= 0)
            numerator = numerator.shiftBinary(exponent);
        else
            denominator = denominator.shiftBinary(-exponent);
        const int sign = (raw >> (FRACTION_BITS + 11)) != 0 ? -1 : 1;
        return Rational(sign, std::move(numerator), std::move(denominator));
    }
    double approximate() const {
        return static_cast<double>(sign * numerator.approximate() / denominator.approximate());
    }
    std::string str() const {
        return (sign < 0 ? "-" : "") + numerator.str() + "/" + denominator.str();
    }
};

#include <limits>
#include <map>
#include <numeric>

struct Point {
    int64_t x = 0, y = 0;
};
struct Aura {
    int64_t cap, rise, fall;
};
struct Spell {
    std::string kind;
    int64_t power = 0, duration = 0;
    std::vector<Point> places;
};
struct Interval {
    double low = 0, high = 0;
};
constexpr int INITIAL_ROOT_DIGITS = 16;
constexpr int BOUND_ROOT_DIGITS = 32;

double down(double value) {
    return std::nextafter(value, -std::numeric_limits<double>::infinity());
}
double up(double value) { return std::nextafter(value, std::numeric_limits<double>::infinity()); }
Interval exactInterval(int64_t value) {
    return {static_cast<double>(value), static_cast<double>(value)};
}
Interval addInterval(Interval a, Interval b) { return {down(a.low + b.low), up(a.high + b.high)}; }
Interval subInterval(Interval a, Interval b) { return {down(a.low - b.high), up(a.high - b.low)}; }
Interval mulInterval(Interval a, Interval b) {
    const double x = a.low * b.low, y = a.low * b.high, z = a.high * b.low, w = a.high * b.high;
    return {down(std::min(std::min(x, y), std::min(z, w))),
            up(std::max(std::max(x, y), std::max(z, w)))};
}
Interval divInterval(Interval a, int64_t denominator) {
    return {down(a.low / denominator), up(a.high / denominator)};
}
Interval minInterval(Interval a, Interval b) {
    return {std::min(a.low, b.low), std::min(a.high, b.high)};
}
Interval maxInterval(Interval a, Interval b) {
    return {std::max(a.low, b.low), std::max(a.high, b.high)};
}
Interval nonnegative(Interval value) { return maxInterval({}, value); }
int64_t squaredDistance(Point a, Point b) {
    const int64_t x = a.x - b.x, y = a.y - b.y;
    return x * x + y * y;
}
double travel(Point a, Point b, int64_t speed) {
    return std::sqrt(static_cast<double>(squaredDistance(a, b))) / speed;
}
Interval travelBounds(Point a, Point b, int64_t speed) {
    const int64_t squared = squaredDistance(a, b);
    if (squared == 0)
        return {};
    const double value = travel(a, b, speed);
    double low = down(value), high = up(value);
    const Rational target(squared), scale(speed * speed);
    const auto compare = [&](double endpoint) {
        const Rational number = Rational::fromDouble(endpoint);
        return (number * number * scale).compare(target);
    };
    while (compare(low) > 0)
        low = down(low);
    while (compare(high) < 0)
        high = up(high);
    return {low, high};
}

struct Surd {
    std::map<uint64_t, Rational> terms;
    Surd(int64_t value = 0) {
        if (value != 0)
            terms.emplace(1, Rational(value));
    }
    explicit Surd(const Rational &value) {
        if (value.sign != 0)
            terms.emplace(1, value);
    }
    bool operator==(const Surd &other) const { return terms == other.terms; }
    Surd operator+(const Surd &other) const {
        Surd result = *this;
        for (const auto &[key, value] : other.terms) {
            auto found = result.terms.find(key);
            if (found == result.terms.end())
                result.terms.emplace(key, value);
            else {
                Rational sum = found->second + value;
                if (sum.sign == 0)
                    result.terms.erase(found);
                else
                    found->second = std::move(sum);
            }
        }
        return result;
    }
    Surd operator-() const {
        Surd result;
        for (const auto &[key, value] : terms)
            result.terms.emplace(key, -value);
        return result;
    }
    Surd operator-(const Surd &other) const {
        if (*this == other)
            return Surd();
        return *this + -other;
    }
    Surd operator*(const Surd &other) const {
        Surd result;
        for (const auto &[first, a] : terms) {
            for (const auto &[second, b] : other.terms) {
                const uint64_t common = std::gcd(first, second);
                const uint64_t key = (first / common) * (second / common);
                Rational value = a * b * Rational(static_cast<int64_t>(common));
                auto found = result.terms.find(key);
                if (found != result.terms.end())
                    value = value + found->second;
                if (value.sign == 0)
                    result.terms.erase(key);
                else
                    result.terms[key] = std::move(value);
            }
        }
        return result;
    }
    Surd scale(int64_t scalar) const {
        if (scalar == 0)
            return Surd();
        if (scalar == 1)
            return *this;
        Surd result;
        for (const auto &[key, value] : terms)
            result.terms.emplace(key, value * Rational(scalar));
        return result;
    }
    Surd divide(int64_t denominator) const {
        if (denominator == 1)
            return *this;
        Surd result;
        for (const auto &[key, value] : terms)
            result.terms.emplace(key, value.divide(denominator));
        return result;
    }
    Surd square() const { return *this * *this; }
    std::pair<Rational, Rational> bounds(int digits) const;
    int sign() const {
        if (terms.empty())
            return 0;
        if (terms.size() == 1)
            return terms.begin()->second.sign;
        for (int digits = INITIAL_ROOT_DIGITS;; digits *= 2) {
            const auto enclosure = bounds(digits);
            if (enclosure.first.sign > 0)
                return 1;
            if (enclosure.second.sign < 0)
                return -1;
        }
    }
    int compare(const Surd &other) const {
        if (*this == other)
            return 0;
        return (*this - other).sign();
    }
    Interval floatBounds() const {
        const auto exact = bounds(BOUND_ROOT_DIGITS);
        double low = exact.first.approximate(), high = exact.second.approximate();
        while (Rational::fromDouble(low).compare(exact.first) > 0)
            low = down(low);
        while (Rational::fromDouble(high).compare(exact.second) < 0)
            high = up(high);
        return {low, high};
    }
};

const std::pair<Rational, Rational> &rootBounds(uint64_t radicand, int digits) {
    static std::map<std::pair<uint64_t, int>, std::pair<Rational, Rational>> cache;
    const std::pair<uint64_t, int> key{radicand, digits};
    const auto found = cache.find(key);
    if (found != cache.end())
        return found->second;
    const Natural denominator = Natural::powerTen(digits);
    const Natural lower = (denominator * denominator * Natural(radicand)).squareRoot();
    return cache
        .emplace(key, std::make_pair(Rational(1, lower, denominator),
                                     Rational(1, lower + Natural(1), denominator)))
        .first->second;
}
std::pair<Rational, Rational> Surd::bounds(int digits) const {
    Rational low, high;
    for (const auto &[key, value] : terms) {
        if (key == 1) {
            low = low + value;
            high = high + value;
            continue;
        }
        const auto &roots = rootBounds(key, digits);
        const Rational &left = value.sign < 0 ? roots.second : roots.first;
        const Rational &right = value.sign < 0 ? roots.first : roots.second;
        low = low + value * left;
        high = high + value * right;
    }
    return {std::move(low), std::move(high)};
}
Surd minimum(const Surd &a, const Surd &b) { return a.compare(b) <= 0 ? a : b; }
Surd maximum(const Surd &a, const Surd &b) { return a.compare(b) >= 0 ? a : b; }
Surd squareRoot(int64_t value) {
    if (value == 0)
        return Surd();
    static std::map<int64_t, Surd> cache;
    const auto found = cache.find(value);
    if (found != cache.end())
        return found->second;
    int64_t remaining = value, outside = 1, inside = 1;
    for (int64_t divisor = 2; divisor * divisor <= remaining; ++divisor) {
        int count = 0;
        while (remaining % divisor == 0) {
            remaining /= divisor;
            ++count;
        }
        for (int pair = 0; pair < count / 2; ++pair)
            outside *= divisor;
        if ((count & 1) != 0)
            inside *= divisor;
    }
    Surd result;
    result.terms.emplace(static_cast<uint64_t>(inside * remaining), Rational(outside));
    cache.emplace(value, result);
    return result;
}
Surd exactTravel(Point a, Point b, int64_t speed) {
    return squareRoot(squaredDistance(a, b)).divide(speed);
}
struct AuraValue {
    double power, damage, deficit;
};
AuraValue auraFloat(double start, Aura a, double running, double duration) {
    const double falling = std::min(running, start / a.fall);
    const double after = std::max(0.0, start - a.fall * running);
    const double runArea = (start + after) * falling / 2;
    const double runLoss =
        ((a.cap - start) + (a.cap - after)) * falling / 2 + a.cap * (running - falling);
    const double casting = std::max(0.0, duration - running);
    const double rising = std::min(casting, (a.cap - after) / a.rise);
    const double final = std::min(static_cast<double>(a.cap), after + a.rise * casting);
    const double castArea = (after + final) * rising / 2 + a.cap * (casting - rising);
    const double castLoss = ((a.cap - after) + (a.cap - final)) * rising / 2;
    return {final, runArea + castArea, runLoss + castLoss};
}
std::pair<Interval, Interval> auraInterval(Interval start, Aura a, Interval running,
                                           Interval duration) {
    const Interval cap = exactInterval(a.cap);
    const Interval falling = nonnegative(minInterval(running, divInterval(start, a.fall)));
    const Interval after =
        nonnegative(subInterval(start, mulInterval(exactInterval(a.fall), running)));
    const Interval casting = nonnegative(subInterval(duration, running));
    const Interval rising = nonnegative(
        minInterval(casting, divInterval(nonnegative(subInterval(cap, after)), a.rise)));
    const Interval final =
        minInterval(cap, addInterval(after, mulInterval(exactInterval(a.rise), casting)));
    Interval run = divInterval(mulInterval(addInterval(nonnegative(subInterval(cap, start)),
                                                       nonnegative(subInterval(cap, after))),
                                           falling),
                               2);
    run = addInterval(run, mulInterval(cap, nonnegative(subInterval(running, falling))));
    const Interval cast = divInterval(mulInterval(addInterval(nonnegative(subInterval(cap, after)),
                                                              nonnegative(subInterval(cap, final))),
                                                  rising),
                                      2);
    return {final, nonnegative(addInterval(run, cast))};
}
std::pair<Surd, Surd> exactAura(const Surd &start, Aura a, const Surd &running,
                                const Surd &duration, bool healing) {
    const Surd cap(a.cap);
    if (start == cap && running.scale(a.fall).compare(cap) <= 0 &&
        running.scale(a.rise + a.fall).compare(duration.scale(a.rise)) <= 0) {
        const Surd loss = running.square().scale(a.fall * (a.rise + a.fall)).divide(2 * a.rise);
        return {cap, healing ? loss : duration.scale(a.cap) - loss};
    }
    const Surd after = maximum(Surd(), start - running.scale(a.fall));
    const Surd final = minimum(cap, after + (duration - running).scale(a.rise));
    const Surd run = (start.square() - after.square()).divide(2 * a.fall);
    const Surd deficit = ((cap - after).square() - (cap - final).square()).divide(2 * a.rise);
    const Surd metric = healing ? running.scale(a.cap) - run + deficit
                                : run + (duration - running).scale(a.cap) - deficit;
    return {final, metric};
}

#include <functional>
#include <iostream>
#include <optional>

constexpr int MASK_KEY_BITS = 16;
constexpr uint8_t MISSING_PARENT = 255;
constexpr const char *BREATH = "Breath";
constexpr const char *TAIL = "Tail";
using ExactWeights = std::vector<std::vector<std::vector<Surd>>>;
using FloatWeights = std::vector<std::vector<std::vector<double>>>;

int bitCount(int mask) { return __builtin_popcount(static_cast<unsigned>(mask)); }
int bitIndex(int mask) { return __builtin_ctz(static_cast<unsigned>(mask)); }
struct Layout {
    std::vector<std::vector<int>> groups;
    std::vector<int> ranks, offsets;
    explicit Layout(int size) : groups(size + 1), ranks(1 << size), offsets(size + 2) {
        for (int mask = 0; mask < (1 << size); ++mask) {
            const int count = bitCount(mask);
            ranks[mask] = static_cast<int>(groups[count].size());
            groups[count].push_back(mask);
        }
        for (int count = 0; count <= size; ++count) {
            const int width = static_cast<int>(groups[count].size());
            offsets[count + 1] = offsets[count] + width * width;
        }
    }
    int pairIndex(int first, int second) const {
        const int count = bitCount(first);
        return offsets[count] + ranks[first] * static_cast<int>(groups[count].size()) +
               ranks[second];
    }
};
const Layout &layoutFor(int size) {
    static std::map<int, Layout> cache;
    const auto found = cache.find(size);
    if (found != cache.end())
        return found->second;
    return cache.emplace(size, Layout(size)).first->second;
}
struct CostTable {
    std::vector<double> values;
    const Layout *layout = nullptr;
    bool pairs = false;
    double get(int first, int second) const {
        return values[pairs ? layout->pairIndex(first, second) : first];
    }
};
CostTable assignment(const FloatWeights &weights, int size, bool pairs, bool maximize,
                     double cutoff) {
    const int limit = 1 << size;
    const Layout &layout = layoutFor(size);
    const int count = pairs ? layout.offsets[weights.size() + 1] : limit;
    std::vector<double> result(count, maximize ? -1 : cutoff);
    result[0] = 0;
    for (int actor = 0; actor < static_cast<int>(weights.size()); ++actor) {
        const int width = static_cast<int>(layout.groups[actor].size());
        const int nextWidth = static_cast<int>(layout.groups[actor + 1].size());
        for (const int left : layout.groups[actor]) {
            const auto &seconds = pairs ? layout.groups[actor] : layout.groups[0];
            for (const int right : seconds) {
                const int index =
                    pairs ? layout.offsets[actor] + layout.ranks[left] * width + layout.ranks[right]
                          : left;
                const double current = result[index];
                if (maximize ? current < 0 : current >= cutoff)
                    continue;
                for (int freeA = (limit - 1) ^ left; freeA != 0;) {
                    const int bitA = freeA & -freeA;
                    freeA ^= bitA;
                    const int a = bitIndex(bitA), nextLeft = left | bitA;
                    const int base =
                        pairs ? layout.offsets[actor + 1] + layout.ranks[nextLeft] * nextWidth
                              : nextLeft;
                    for (int freeB = pairs ? ((limit - 1) ^ right) : 1; freeB != 0;) {
                        const int bitB = freeB & -freeB;
                        freeB ^= bitB;
                        const int b = pairs ? bitIndex(bitB) : 0;
                        const int target = base + (pairs ? layout.ranks[right | bitB] : 0);
                        const double candidate = current + weights[actor][a][b];
                        if (maximize ? candidate > result[target] : candidate < result[target])
                            result[target] = candidate;
                    }
                }
            }
        }
    }
    return {std::move(result), &layout, pairs};
}
std::vector<int> maskPlaces(int mask) {
    std::vector<int> result;
    while (mask != 0) {
        const int bit = mask & -mask;
        mask ^= bit;
        result.push_back(bitIndex(bit));
    }
    return result;
}
ExactWeights restrictWeights(const ExactWeights &weights, int firstMask, int secondMask,
                             bool pairs) {
    const auto first = maskPlaces(firstMask),
               second = pairs ? maskPlaces(secondMask) : std::vector<int>{0};
    ExactWeights result(weights.size());
    for (size_t actor = 0; actor < weights.size(); ++actor) {
        for (const int a : first) {
            std::vector<Surd> row;
            for (const int b : second)
                row.push_back(weights[actor][a][b]);
            result[actor].push_back(std::move(row));
        }
    }
    return result;
}
std::vector<int> reconstruct(int index, int people, int size, bool pairs, const Layout &layout,
                             const std::vector<uint8_t> &parent) {
    std::vector<int> result(people);
    while (people > 0) {
        const int code = parent[index];
        const int a = pairs ? code / size : code, b = pairs ? code % size : 0;
        if (pairs) {
            const int rank = index - layout.offsets[people];
            const int width = static_cast<int>(layout.groups[people].size());
            const int first = layout.groups[people][rank / width] ^ (1 << a);
            const int second = layout.groups[people][rank % width] ^ (1 << b);
            index = layout.pairIndex(first, second);
        } else
            index ^= 1 << a;
        result[--people] = code;
    }
    return result;
}
Surd restrictedOptimum(const ExactWeights &weights, bool pairs) {
    const int size = static_cast<int>(weights.size());
    bool identical = true;
    for (int actor = 1; actor < size; ++actor)
        identical = identical && weights[actor] == weights[0];
    if (identical) {
        if (!pairs) {
            Surd result;
            for (const auto &row : weights[0])
                result = result + row[0];
            return result;
        }
        ExactWeights matching(size, std::vector<std::vector<Surd>>(size, std::vector<Surd>(1)));
        for (int actor = 0; actor < size; ++actor) {
            for (int place = 0; place < size; ++place)
                matching[actor][place][0] = weights[0][actor][place];
        }
        return restrictedOptimum(matching, false);
    }
    const Layout &layout = layoutFor(size);
    const int limit = 1 << size, count = pairs ? layout.offsets[size + 1] : limit;
    const double infinity = std::numeric_limits<double>::infinity();
    std::vector<double> lower(count, infinity), upper(count, infinity);
    std::vector<uint8_t> parent(count, MISSING_PARENT);
    lower[0] = upper[0] = 0;
    std::vector<std::vector<std::vector<Interval>>> bounds(size);
    for (int actor = 0; actor < size; ++actor) {
        for (const auto &row : weights[actor]) {
            std::vector<Interval> converted;
            for (const auto &value : row)
                converted.push_back(value.floatBounds());
            bounds[actor].push_back(std::move(converted));
        }
    }
    for (int actor = 0; actor < size; ++actor) {
        std::map<int, std::vector<int>> previousPaths;
        for (const int left : layout.groups[actor]) {
            const auto &seconds = pairs ? layout.groups[actor] : layout.groups[0];
            for (const int right : seconds) {
                const int index = pairs ? layout.pairIndex(left, right) : left;
                if (std::isinf(lower[index]))
                    continue;
                for (int freeA = (limit - 1) ^ left; freeA != 0;) {
                    const int bitA = freeA & -freeA;
                    freeA ^= bitA;
                    const int a = bitIndex(bitA);
                    for (int freeB = pairs ? ((limit - 1) ^ right) : 1; freeB != 0;) {
                        const int bitB = freeB & -freeB;
                        freeB ^= bitB;
                        const int b = pairs ? bitIndex(bitB) : 0;
                        const int target =
                            pairs ? layout.pairIndex(left | bitA, right | bitB) : left | bitA;
                        const Interval bound = bounds[actor][a][b];
                        const double low = down(lower[index] + bound.low),
                                     high = up(upper[index] + bound.high);
                        bool choose = std::isinf(lower[target]) || high < lower[target];
                        if (!choose && low < upper[target]) {
                            auto found = previousPaths.find(index);
                            if (found == previousPaths.end()) {
                                found = previousPaths
                                            .emplace(index, reconstruct(index, actor, size, pairs,
                                                                        layout, parent))
                                            .first;
                            }
                            const auto &previous = found->second;
                            const auto incumbent =
                                reconstruct(target, actor + 1, size, pairs, layout, parent);
                            Surd difference;
                            for (int person = 0; person <= actor; ++person) {
                                const int next =
                                    person == actor ? (pairs ? a * size + b : a) : previous[person];
                                const int old = incumbent[person];
                                if (next == old)
                                    continue;
                                const int na = pairs ? next / size : next,
                                          nb = pairs ? next % size : 0;
                                const int oa = pairs ? old / size : old,
                                          ob = pairs ? old % size : 0;
                                difference =
                                    difference + weights[person][na][nb] - weights[person][oa][ob];
                            }
                            choose = difference.sign() < 0;
                        }
                        if (choose) {
                            lower[target] = low;
                            upper[target] = high;
                            parent[target] = static_cast<uint8_t>(pairs ? a * size + b : a);
                        }
                    }
                }
            }
        }
    }
    const int finalIndex = pairs ? layout.pairIndex(limit - 1, limit - 1) : limit - 1;
    const auto choices = reconstruct(finalIndex, size, size, pairs, layout, parent);
    Surd result;
    for (int actor = 0; actor < size; ++actor) {
        const int code = choices[actor];
        result = result + weights[actor][pairs ? code / size : code][pairs ? code % size : 0];
    }
    return result;
}

struct Candidate {
    int first, second;
    double value;
};
struct Damage {
    Interval bounds;
    std::optional<Surd> exact;
    std::function<Surd()> refine;
    const Surd &exactValue() {
        if (!exact) {
            exact = refine();
            refine = nullptr;
        }
        return *exact;
    }
};
struct Group {
    FloatWeights weights;
    double error;
};
struct Block {
    std::vector<Aura> attackers, healers;
    int64_t health, speed;
    Point start;
    std::vector<Spell> breaths;
    Spell storm;
    bool initial;
    double latest;
    Interval latestBounds;
    Block(const std::vector<Aura> &attackers, const std::vector<Aura> &healers, int64_t health,
          int64_t speed, Point start, const std::vector<Spell> &breaths, const Spell &storm,
          bool initial)
        : attackers(attackers), healers(healers), health(health), speed(speed), start(start),
          breaths(breaths), storm(storm), initial(initial) {
        latest = travel(start, storm.places[0], speed);
        latestBounds = travelBounds(start, storm.places[0], speed);
        if (!breaths.empty()) {
            latest = 0;
            latestBounds = {};
            for (const Point place : breaths.back().places) {
                latest = std::max(latest, travel(place, storm.places[0], speed));
                latestBounds =
                    maxInterval(latestBounds, travelBounds(place, storm.places[0], speed));
            }
        }
    }
    int64_t healerCaps() const {
        int64_t sum = 0;
        for (const Aura aura : healers)
            sum += aura.cap;
        return sum;
    }
    int64_t fixedLoss() const {
        const int64_t caps = healerCaps();
        int64_t sum = 0;
        for (const Spell &s : breaths)
            sum += (s.power - caps) * s.duration;
        return sum;
    }
    Surd exactLatest() const {
        if (breaths.empty())
            return exactTravel(start, storm.places[0], speed);
        Surd result;
        for (const Point place : breaths.back().places)
            result = maximum(result, exactTravel(place, storm.places[0], speed));
        return result;
    }
    Surd exactBudget() const {
        return Surd(health - fixedLoss()) - exactLatest().scale(storm.power - healerCaps());
    }
    ExactWeights exactGroup(const std::vector<Aura> &auras, bool healing) const {
        const Spell &first = breaths.empty() ? storm : breaths[0];
        const int size = static_cast<int>(first.places.size());
        const bool pairs = breaths.size() == 2;
        std::vector<Surd> outgoing(size), returning(size);
        for (int a = 0; a < size; ++a) {
            outgoing[a] = exactTravel(start, first.places[a], speed);
            if (!breaths.empty())
                returning[a] = exactTravel(breaths.back().places[a], storm.places[0], speed);
        }
        const Surd longest = exactLatest();
        std::vector<std::vector<Surd>> between(size, std::vector<Surd>(pairs ? size : 0));
        if (pairs)
            for (int a = 0; a < size; ++a)
                for (int b = 0; b < size; ++b) {
                    between[a][b] = exactTravel(first.places[a], breaths[1].places[b], speed);
                }
        ExactWeights result(auras.size());
        for (size_t actor = 0; actor < auras.size(); ++actor) {
            const Aura aura = auras[actor];
            bool reused = false;
            for (size_t previous = 0; previous < actor; ++previous) {
                const Aura other = auras[previous];
                if (aura.cap == other.cap && aura.rise == other.rise && aura.fall == other.fall) {
                    result[actor] = result[previous];
                    reused = true;
                    break;
                }
            }
            if (reused)
                continue;
            result[actor].assign(size, std::vector<Surd>(pairs ? size : 1));
            const Surd power(initial && !healing ? 0 : aura.cap);
            for (int a = 0; a < size; ++a) {
                const Surd duration = healing && breaths.empty() ? longest : Surd(first.duration);
                const auto state = exactAura(power, aura, outgoing[a], duration, healing);
                for (int b = 0; b < (pairs ? size : 1); ++b) {
                    Surd value = state.second;
                    if (!breaths.empty()) {
                        Surd at = state.first;
                        int slot = a;
                        if (pairs) {
                            const auto middle = exactAura(at, aura, between[a][b],
                                                          Surd(breaths[1].duration), healing);
                            at = middle.first;
                            value = value + middle.second;
                            slot = b;
                        }
                        const Surd end = healing ? longest : Surd(storm.duration);
                        value = value + exactAura(at, aura, returning[slot], end, healing).second;
                    }
                    result[actor][a][b] = std::move(value);
                }
            }
        }
        return result;
    }
    Group group(const std::vector<Aura> &auras, bool healing) const {
        const Spell &first = breaths.empty() ? storm : breaths[0];
        const int size = static_cast<int>(first.places.size());
        const bool pairs = breaths.size() == 2;
        std::vector<double> outgoing(size), returning(size);
        std::vector<Interval> outBounds(size), retBounds(size);
        std::vector<std::vector<double>> between(size, std::vector<double>(pairs ? size : 0));
        std::vector<std::vector<Interval>> betweenBounds(size,
                                                         std::vector<Interval>(pairs ? size : 0));
        for (int a = 0; a < size; ++a) {
            outgoing[a] = travel(start, first.places[a], speed);
            outBounds[a] = travelBounds(start, first.places[a], speed);
            if (!breaths.empty()) {
                returning[a] = travel(breaths.back().places[a], storm.places[0], speed);
                retBounds[a] = travelBounds(breaths.back().places[a], storm.places[0], speed);
            }
            if (pairs)
                for (int b = 0; b < size; ++b) {
                    between[a][b] = travel(first.places[a], breaths[1].places[b], speed);
                    betweenBounds[a][b] =
                        travelBounds(first.places[a], breaths[1].places[b], speed);
                }
        }
        FloatWeights result(auras.size(), std::vector<std::vector<double>>(
                                              size, std::vector<double>(pairs ? size : 1)));
        double error = 0, largestSum = 0;
        for (size_t actor = 0; actor < auras.size(); ++actor) {
            const Aura aura = auras[actor];
            const int64_t initialPower = initial && !healing ? 0 : aura.cap;
            double largestError = 0, largestWeight = 0;
            for (int a = 0; a < size; ++a) {
                const double duration =
                    healing && breaths.empty() ? latest : static_cast<double>(first.duration);
                const Interval durationBounds =
                    healing && breaths.empty() ? latestBounds : exactInterval(first.duration);
                const AuraValue state =
                    auraFloat(static_cast<double>(initialPower), aura, outgoing[a], duration);
                const auto stateBounds =
                    auraInterval(exactInterval(initialPower), aura, outBounds[a], durationBounds);
                for (int b = 0; b < (pairs ? size : 1); ++b) {
                    double value = healing ? state.deficit : state.damage;
                    Interval loss = stateBounds.second,
                             area = mulInterval(exactInterval(aura.cap), durationBounds);
                    if (!breaths.empty()) {
                        AuraValue middle = state;
                        Interval powerBound = stateBounds.first;
                        int slot = a;
                        if (pairs) {
                            middle = auraFloat(state.power, aura, between[a][b],
                                               static_cast<double>(breaths[1].duration));
                            const auto middleBounds =
                                auraInterval(powerBound, aura, betweenBounds[a][b],
                                             exactInterval(breaths[1].duration));
                            powerBound = middleBounds.first;
                            loss = addInterval(loss, middleBounds.second);
                            area = addInterval(area, exactInterval(aura.cap * breaths[1].duration));
                            value += healing ? middle.deficit : middle.damage;
                            slot = b;
                        }
                        const double end = healing ? latest : static_cast<double>(storm.duration);
                        const Interval endBounds =
                            healing ? latestBounds : exactInterval(storm.duration);
                        const AuraValue final = auraFloat(middle.power, aura, returning[slot], end);
                        const auto finalBounds =
                            auraInterval(powerBound, aura, retBounds[slot], endBounds);
                        loss = addInterval(loss, finalBounds.second);
                        area = addInterval(area, mulInterval(exactInterval(aura.cap), endBounds));
                        value += healing ? final.deficit : final.damage;
                    }
                    const Interval enclosure = healing ? loss : subInterval(area, loss);
                    largestError =
                        up(std::max(largestError, std::max(std::abs(value - enclosure.low),
                                                           std::abs(enclosure.high - value))));
                    largestWeight =
                        std::max(largestWeight,
                                 std::max(std::abs(value), std::max(std::abs(enclosure.low),
                                                                    std::abs(enclosure.high))));
                    result[actor][a][b] = value;
                }
            }
            error = up(error + largestError);
            largestSum = up(largestSum + largestWeight);
        }
        const double ulp =
            std::nextafter(largestSum, std::numeric_limits<double>::infinity()) - largestSum;
        return {std::move(result), up(error + 2 * auras.size() * ulp)};
    }
    Surd exactDamage(const std::vector<Candidate> &candidates, double error) const {
        const ExactWeights weights = exactGroup(attackers, false);
        if (breaths.empty()) {
            Surd result;
            for (const auto &person : weights)
                result = result + person[0][0];
            return result;
        }
        const bool pairs = breaths.size() == 2;
        Surd globalUpper;
        for (const auto &person : weights) {
            Surd largest = person[0][0];
            for (const auto &row : person)
                for (const auto &value : row)
                    largest = maximum(largest, value);
            globalUpper = globalUpper + largest;
        }
        for (const Candidate choice : candidates) {
            if (pairs && choice.first != choice.second)
                continue;
            const auto places = maskPlaces(choice.first);
            Surd diagonal;
            for (size_t actor = 0; actor < places.size(); ++actor) {
                const int place = places[actor];
                diagonal = diagonal + weights[actor][place][pairs ? place : 0];
            }
            if (diagonal == globalUpper)
                return globalUpper;
            break;
        }
        std::vector<int> order(candidates.size());
        std::iota(order.begin(), order.end(), 0);
        std::sort(order.begin(), order.end(), [&](int a, int b) {
            if (candidates[a].value != candidates[b].value)
                return candidates[a].value > candidates[b].value;
            return a < b;
        });
        std::optional<Surd> best;
        double bestLower = -std::numeric_limits<double>::infinity();
        for (const int index : order) {
            const Candidate choice = candidates[index];
            if (up(choice.value + error) < bestLower)
                break;
            const ExactWeights part = restrictWeights(weights, choice.first, choice.second, pairs);
            Surd upper, diagonal;
            for (size_t actor = 0; actor < part.size(); ++actor) {
                Surd largest = part[actor][0][0];
                for (const auto &row : part[actor])
                    for (const auto &value : row)
                        largest = maximum(largest, value);
                upper = upper + largest;
                diagonal = diagonal + part[actor][actor][pairs ? actor : 0];
            }
            if (best && upper.compare(*best) <= 0)
                continue;
            Surd value = upper;
            if (!(diagonal == upper)) {
                ExactWeights negative = part;
                for (auto &person : negative)
                    for (auto &row : person)
                        for (auto &cost : row)
                            cost = -cost;
                value = -restrictedOptimum(negative, pairs);
            }
            if (!best || value.compare(*best) > 0) {
                best = std::move(value);
                if (*best == globalUpper)
                    return *best;
                bestLower = best->floatBounds().low;
            }
        }
        return *best;
    }
    std::optional<Damage> damage() const;
};

struct SurvivalRefiner {
    ExactWeights weights;
    Surd budget;
    bool pairs;
    std::map<int, bool> cache;
    explicit SurvivalRefiner(const Block &block)
        : weights(block.exactGroup(block.healers, true)), budget(block.exactBudget()),
          pairs(block.breaths.size() == 2) {}
    bool feasible(int first, int second) {
        const int key = (first << MASK_KEY_BITS) | second;
        const auto found = cache.find(key);
        if (found != cache.end())
            return found->second;
        const ExactWeights part = restrictWeights(weights, first, second, pairs);
        Surd lower, diagonal;
        for (size_t actor = 0; actor < part.size(); ++actor) {
            Surd smallest = part[actor][0][0];
            for (const auto &row : part[actor])
                for (const auto &value : row)
                    smallest = minimum(smallest, value);
            lower = lower + smallest;
            diagonal = diagonal + part[actor][actor][pairs ? actor : 0];
        }
        bool result = false;
        if (lower.compare(budget) < 0) {
            result =
                diagonal.compare(budget) < 0 || restrictedOptimum(part, pairs).compare(budget) < 0;
        }
        cache.emplace(key, result);
        return result;
    }
};
std::optional<Damage> Block::damage() const {
    const double budget =
        static_cast<double>(health - fixedLoss()) - (storm.power - healerCaps()) * latest;
    const Interval budgetBounds =
        subInterval(exactInterval(health - fixedLoss()),
                    mulInterval(exactInterval(storm.power - healerCaps()), latestBounds));
    if (budgetBounds.high <= 0)
        return std::nullopt;
    const Group healerGroup = group(healers, true);
    const double error = up(healerGroup.error + up(std::max(std::abs(budget - budgetBounds.low),
                                                            std::abs(budgetBounds.high - budget))));
    std::optional<SurvivalRefiner> refiner;
    const auto survives = [&](double value, int first, int second) {
        if (std::isinf(value))
            return false;
        if (up(value + error) < budget)
            return true;
        if (down(value - error) >= budget)
            return false;
        if (breaths.empty()) {
            Surd loss;
            for (const auto &person : exactGroup(healers, true))
                loss = loss + person[0][0];
            return loss.compare(exactBudget()) < 0;
        }
        if (!refiner)
            refiner.emplace(*this);
        return refiner->feasible(first, second);
    };
    if (breaths.empty()) {
        double loss = 0;
        for (const auto &person : healerGroup.weights)
            loss += person[0][0];
        if (!survives(loss, 0, 0))
            return std::nullopt;
        const Group attackersGroup = group(attackers, false);
        double value = 0;
        for (const auto &person : attackersGroup.weights)
            value += person[0][0];
        const double damageError = attackersGroup.error;
        return Damage{{down(value - damageError), up(value + damageError)},
                      std::nullopt,
                      [block = *this, damageError] { return block.exactDamage({}, damageError); }};
    }
    const int size = static_cast<int>(attackers.size() + healers.size()), full = (1 << size) - 1;
    const bool pairs = breaths.size() == 2;
    const auto &masks = layoutFor(size).groups[healers.size()];
    double upperLoss = 0;
    for (const auto &person : healerGroup.weights) {
        double largest = 0;
        for (const auto &row : person)
            for (const double value : row)
                largest = std::max(largest, value);
        upperLoss = up(upperLoss + largest);
    }
    const bool allSurvive = up(upperLoss + error) < budget;
    CostTable survival;
    if (!allSurvive)
        survival = assignment(healerGroup.weights, size, pairs, false, up(budget + error));
    const auto feasible = [&](int first, int second) {
        return allSurvive || survives(survival.get(first, second), first, second);
    };
    bool any = allSurvive;
    for (const int first : masks) {
        if (any)
            break;
        for (const int second : pairs ? masks : layoutFor(size).groups[0]) {
            if (feasible(first, second)) {
                any = true;
                break;
            }
        }
    }
    if (!any)
        return std::nullopt;
    const Group attackersGroup = group(attackers, false);
    const CostTable damage = assignment(attackersGroup.weights, size, pairs, true,
                                        std::numeric_limits<double>::infinity());
    double best = -std::numeric_limits<double>::infinity();
    std::vector<Candidate> candidates;
    for (const int first : masks)
        for (const int second : pairs ? masks : layoutFor(size).groups[0]) {
            if (!feasible(first, second))
                continue;
            const int left = full ^ first, right = pairs ? (full ^ second) : 0;
            const double value = damage.get(left, right);
            best = std::max(best, value);
            candidates.push_back({left, right, value});
        }
    const double damageError = attackersGroup.error, threshold = down(best - damageError);
    std::vector<Candidate> kept;
    for (const Candidate choice : candidates)
        if (up(choice.value + damageError) >= threshold)
            kept.push_back(choice);
    return Damage{{down(best - damageError), up(best + damageError)},
                  std::nullopt,
                  [block = *this, kept = std::move(kept), damageError] {
                      return block.exactDamage(kept, damageError);
                  }};
}
bool killed(std::vector<Damage> &amounts, int64_t health) {
    Interval total;
    for (const auto &amount : amounts)
        total = addInterval(total, amount.bounds);
    if (total.low >= health)
        return true;
    if (total.high < health)
        return false;
    Surd exact;
    for (auto &amount : amounts)
        exact = exact + amount.exactValue();
    return exact.compare(Surd(health)) >= 0;
}
int solve(const std::vector<Aura> &attackers, const std::vector<Aura> &healers, int64_t health,
          int64_t speed, int64_t dragon, const std::vector<Spell> &spells) {
    Point start;
    bool initial = true;
    std::vector<Spell> breaths;
    std::vector<Damage> amounts;
    for (size_t index = 0; index < spells.size(); ++index) {
        const Spell &spell = spells[index];
        if (spell.kind == TAIL)
            break;
        if (spell.kind == BREATH) {
            breaths.push_back(spell);
            continue;
        }
        const Block block(attackers, healers, health, speed, start, breaths, spell, initial);
        auto amount = block.damage();
        if (!amount)
            return 0;
        amounts.push_back(std::move(*amount));
        if (killed(amounts, dragon))
            return static_cast<int>(index) + 1;
        start = spell.places[0];
        initial = false;
        breaths.clear();
    }
    return 0;
}
int readAndSolve(std::istream &input) {
    int n, m, k;
    int64_t health, speed, dragon;
    if (!(input >> n >> m >> k >> health >> speed >> dragon))
        return 0;
    std::vector<Aura> attackers(n), healers(m);
    for (auto &aura : attackers)
        input >> aura.cap >> aura.rise >> aura.fall;
    for (auto &aura : healers)
        input >> aura.cap >> aura.rise >> aura.fall;
    std::vector<Spell> spells(k);
    for (auto &spell : spells) {
        input >> spell.kind;
        if (spell.kind == TAIL)
            continue;
        input >> spell.power >> spell.duration;
        spell.places.resize(spell.kind == BREATH ? n + m : 1);
        for (auto &place : spell.places)
            input >> place.x >> place.y;
    }
    return solve(attackers, healers, health, speed, dragon, spells);
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    const int answer = readAndSolve(std::cin);
    if (answer == 0)
        std::cout << "You are not prepared\n";
    else
        std::cout << "No useful loot again\n" << answer << '\n';
}
