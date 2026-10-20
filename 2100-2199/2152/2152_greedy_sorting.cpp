#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using Integer = std::uint64_t;
using Money = __uint128_t;

constexpr Integer MAX_DIGIT = 9;
constexpr Integer CENTS = 100;
constexpr std::size_t OUTPUT_ROW_SIZE = 24;

struct Package {
    Integer weight;
    Integer price;
};

struct Change {
    Money gain;
    std::size_t index;
    Integer value;
    bool weight;
};

Integer increase(Integer value) {
    Integer place = 1;
    while (place <= value / 10) {
        place *= 10;
    }
    while (place > 0) {
        Integer digit = value / place % 10;
        if (digit != MAX_DIGIT) {
            return value + (MAX_DIGIT - digit) * place;
        }
        place /= 10;
    }
    return value;
}

Integer excess(Integer value, Integer limit) {
    return value > limit ? value - limit : 0;
}

std::string decimal(Money value) {
    std::string result;
    do {
        result.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    } while (value > 0);
    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::size_t count, budget;
    Integer max_weight, max_price, weight_rate, price_rate;
    std::cin >> count >> budget >> max_weight >> max_price >> weight_rate >> price_rate;
    std::vector<Package> packages(count);
    std::vector<Change> changes;
    changes.reserve(count);
    Money total = 0;

    for (std::size_t index = 0; index < count; ++index) {
        Package &package = packages[index];
        std::cin >> package.weight >> package.price;
        Integer weight_excess = excess(package.weight, max_weight);
        Integer price_excess = excess(package.price, max_price);
        Integer new_weight = increase(package.weight);
        Integer new_price = increase(package.price);
        Money weight_gain = Money(excess(new_weight, max_weight) - weight_excess) * weight_rate;
        weight_gain *= CENTS;
        Money price_gain = Money(excess(new_price, max_price) - price_excess) * price_rate;
        total += Money(weight_excess) * weight_rate * CENTS + Money(price_excess) * price_rate;
        if (weight_gain >= price_gain && weight_gain > 0) {
            changes.push_back({weight_gain, index, new_weight, true});
        } else if (price_gain > 0) {
            changes.push_back({price_gain, index, new_price, false});
        }
    }

    std::sort(changes.begin(), changes.end(), [](const Change &left, const Change &right) {
        if (left.gain != right.gain) {
            return left.gain > right.gain;
        }
        return left.index < right.index;
    });
    std::size_t chosen = std::min(budget, changes.size());
    for (std::size_t index = 0; index < chosen; ++index) {
        const Change &change = changes[index];
        total += change.gain;
        if (change.weight) {
            packages[change.index].weight = change.value;
        } else {
            packages[change.index].price = change.value;
        }
    }

    std::string output = decimal(total / CENTS) + ".";
    Integer fraction = static_cast<Integer>(total % CENTS);
    if (fraction < 10) {
        output += '0';
    }
    output += std::to_string(fraction) + "\n";
    output.reserve(output.size() + count * OUTPUT_ROW_SIZE);
    for (const Package &package : packages) {
        output += std::to_string(package.weight) + " " + std::to_string(package.price) + "\n";
    }
    std::cout << output;
}
