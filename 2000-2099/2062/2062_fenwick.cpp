#include <cstdint>
#include <iostream>
#include <vector>

class Charges {
    int size;
    std::vector<std::int64_t> initial, tree;
    std::vector<int> offsets;
    std::vector<std::uint16_t> divisors;

    std::int64_t point(int index) const {
        std::int64_t result = 0;
        while (index > 0) {
            result += tree[index];
            index &= index - 1;
        }
        return result;
    }

  public:
    explicit Charges(std::vector<std::int64_t> values)
        : size(static_cast<int>(values.size()) - 1), initial(std::move(values)), tree(size + 1),
          offsets(size + 2) {
        for (int divisor = 1; divisor * divisor <= size; ++divisor)
            for (int multiple = divisor * divisor; multiple <= size; multiple += divisor)
                ++offsets[multiple + 1];
        for (int index = 1; index <= size + 1; ++index)
            offsets[index] += offsets[index - 1];
        divisors.resize(offsets.back());
        auto cursor = offsets;
        for (int divisor = 1; divisor * divisor <= size; ++divisor)
            for (int multiple = divisor * divisor; multiple <= size; multiple += divisor)
                divisors[cursor[multiple]++] = static_cast<std::uint16_t>(divisor);
    }

    void irradiate(int left, int right, std::int64_t power) {
        for (int index = left; index <= size; index += index & -index)
            tree[index] += power;
        for (int index = right + 1; index <= size; index += index & -index)
            tree[index] -= power;
    }

    std::int64_t measure(int index) const {
        std::int64_t result = initial[index];
        for (int at = offsets[index]; at < offsets[index + 1]; ++at) {
            int divisor = divisors[at];
            int partner = index / divisor;
            result += point(divisor);
            if (partner != divisor)
                result += point(partner);
        }
        return result;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<std::int64_t> initial(size + 1);
    for (int index = 1; index <= size; ++index)
        std::cin >> initial[index];
    Charges charges(std::move(initial));
    int count;
    std::cin >> count;
    while (count--) {
        int type;
        std::cin >> type;
        if (type == 1) {
            int index;
            std::cin >> index;
            std::cout << charges.measure(index) << '\n';
        } else {
            int left, right;
            std::int64_t power;
            std::cin >> left >> right >> power;
            charges.irradiate(left, right, power);
        }
    }
}
