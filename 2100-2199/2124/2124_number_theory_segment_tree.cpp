#include <algorithm>
#include <cstdio>
#include <numeric>
#include <string>
#include <vector>

class FastInput {
    static constexpr int BUFFER_SIZE = 65536;
    char buffer[BUFFER_SIZE];
    int position = 0;
    int length = 0;

    int read() {
        if (position == length) {
            length = static_cast<int>(std::fread(buffer, 1, BUFFER_SIZE, stdin));
            position = 0;
            if (length == 0) {
                return EOF;
            }
        }
        return buffer[position++];
    }

  public:
    int next() {
        int symbol;
        do {
            symbol = read();
        } while (symbol <= ' ' && symbol != EOF);
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = read();
        }
        return value;
    }
};

class Group {
    int modulus;
    int size;
    std::vector<int> factors;

  public:
    explicit Group(int prime) : modulus(prime), size(prime - 1) {
        int remaining = size;
        for (int factor = 2; factor <= remaining / factor; ++factor) {
            if (remaining % factor != 0) {
                continue;
            }
            factors.push_back(factor);
            do {
                remaining /= factor;
            } while (remaining % factor == 0);
        }
        if (remaining > 1) {
            factors.push_back(remaining);
        }
    }

    int multiply(int left, int right) const {
        return static_cast<int>(static_cast<long long>(left) * right % modulus);
    }

    int power(int value, int exponent) const {
        int result = 1;
        while (exponent > 0) {
            if (exponent % 2 != 0) {
                result = multiply(result, value);
            }
            value = multiply(value, value);
            exponent /= 2;
        }
        return result;
    }

    int inverse(int value) const { return power(value, modulus - 2); }

    int index(int value) const {
        if (value == 1) {
            return size;
        }
        if (value == modulus - 1) {
            return size / 2;
        }
        int order = size;
        for (int factor : factors) {
            while (order % factor == 0 && power(value, order / factor) == 1) {
                order /= factor;
            }
        }
        return size / order;
    }

    int combinedOrder(int value, int divisor) const {
        if (value == 1) {
            return size / divisor;
        }
        if (value == modulus - 1) {
            return size / std::gcd(divisor, size / 2);
        }
        int order = size;
        // Only factors shared with the difference subgroup can reduce the answer.
        for (int factor : factors) {
            while (divisor % factor == 0 && power(value, order / factor) == 1) {
                divisor /= factor;
                order /= factor;
            }
        }
        return order;
    }
};

class GcdTree {
    int base = 1;
    int identity;
    std::vector<int> tree;

  public:
    GcdTree(const std::vector<int> &values, int neutral) : identity(neutral) {
        while (base < static_cast<int>(values.size())) {
            base *= 2;
        }
        tree.assign(2 * base, identity);
        std::copy(values.begin(), values.end(), tree.begin() + base);
        for (int node = base - 1; node > 0; --node) {
            tree[node] = std::gcd(tree[2 * node], tree[2 * node + 1]);
        }
    }

    void set(int position, int value) {
        int node = base + position;
        if (tree[node] == value) {
            return;
        }
        tree[node] = value;
        while (node > 1) {
            node /= 2;
            int updated = std::gcd(tree[2 * node], tree[2 * node + 1]);
            if (tree[node] == updated) {
                break;
            }
            tree[node] = updated;
        }
    }

    int query(int left, int right) const {
        int result = identity;
        left += base;
        right += base;
        while (left < right && result != 1) {
            if (left % 2 != 0) {
                result = std::gcd(result, tree[left++]);
            }
            if (right % 2 != 0) {
                result = std::gcd(result, tree[--right]);
            }
            left /= 2;
            right /= 2;
        }
        return result;
    }
};

class Fenwick {
    std::vector<int> tree;
    const Group &group;

  public:
    Fenwick(int length, const Group &arithmetic) : tree(length + 1, 1), group(arithmetic) {}

    void multiply(int position, int value) {
        for (int node = position + 1; node < static_cast<int>(tree.size()); node += node & -node) {
            tree[node] = group.multiply(tree[node], value);
        }
    }

    int prefix(int position) const {
        int result = 1;
        for (int node = position + 1; node > 0; node -= node & -node) {
            result = group.multiply(result, tree[node]);
        }
        return result;
    }
};

int main() {
    FastInput input;
    int prime = input.next();
    int length = input.next();
    int queries = input.next();
    Group group(prime);
    std::vector<int> original(length);
    std::vector<int> prefix(length + 1, 1);
    for (int i = 0; i < length; ++i) {
        original[i] = input.next();
        prefix[i + 1] = group.multiply(prefix[i], original[i]);
    }
    std::vector<int> difference(length, 1);
    // One inverse suffices for all initial adjacent ratios.
    int inverse = group.inverse(prefix[length]);
    for (int i = length - 1; i > 0; --i) {
        inverse = group.multiply(inverse, original[i]);
        difference[i] = group.multiply(original[i], group.multiply(inverse, prefix[i - 1]));
    }
    std::vector<int> indices(length, prime - 1);
    for (int i = 1; i < length; ++i) {
        indices[i] = group.index(difference[i]);
    }
    GcdTree tree(indices, prime - 1);
    Fenwick changes(length, group);
    std::string output;
    for (int query = 0; query < queries; ++query) {
        int type = input.next();
        int left = input.next() - 1;
        int right = input.next();
        if (type == 1) {
            int multiplier = input.next();
            if (multiplier == 1) {
                continue;
            }
            changes.multiply(left, multiplier);
            if (left > 0) {
                difference[left] = group.multiply(difference[left], multiplier);
                tree.set(left, group.index(difference[left]));
            }
            if (right < length) {
                int reciprocal = group.inverse(multiplier);
                changes.multiply(right, reciprocal);
                difference[right] = group.multiply(difference[right], reciprocal);
                tree.set(right, group.index(difference[right]));
            }
        } else {
            int divisor = tree.query(left + 1, right);
            int answer = prime - 1;
            if (divisor != 1) {
                int value = group.multiply(original[left], changes.prefix(left));
                answer = group.combinedOrder(value, divisor);
            }
            output += std::to_string(answer);
            output += '\n';
        }
    }
    std::fwrite(output.data(), 1, output.size(), stdout);
}
