import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 65536;
    private static final int MAX_FACTOR_COUNT = 10;

    private static final class FastInput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int next() throws IOException {
            int symbol;
            do {
                symbol = read();
            } while (symbol <= ' ' && symbol != -1);
            int value = 0;
            while (symbol > ' ') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }
    }

    private static int gcd(int left, int right) {
        while (right != 0) {
            int remainder = left % right;
            left = right;
            right = remainder;
        }
        return left;
    }

    private static final class Group {
        private final int modulus;
        private final int size;
        private final int[] factors = new int[MAX_FACTOR_COUNT];
        private int factorCount;

        Group(int prime) {
            modulus = prime;
            size = prime - 1;
            int remaining = size;
            for (int factor = 2; factor <= remaining / factor; factor++) {
                if (remaining % factor != 0) {
                    continue;
                }
                factors[factorCount++] = factor;
                do {
                    remaining /= factor;
                } while (remaining % factor == 0);
            }
            if (remaining > 1) {
                factors[factorCount++] = remaining;
            }
        }

        int multiply(int left, int right) {
            return (int) ((long) left * right % modulus);
        }

        int power(int value, int exponent) {
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

        int inverse(int value) {
            return power(value, modulus - 2);
        }

        int index(int value) {
            if (value == 1) {
                return size;
            }
            if (value == modulus - 1) {
                return size / 2;
            }
            int order = size;
            for (int i = 0; i < factorCount; i++) {
                int factor = factors[i];
                while (order % factor == 0 && power(value, order / factor) == 1) {
                    order /= factor;
                }
            }
            return size / order;
        }

        int combinedOrder(int value, int divisor) {
            if (value == 1) {
                return size / divisor;
            }
            if (value == modulus - 1) {
                return size / gcd(divisor, size / 2);
            }
            int order = size;
            // Only shared factors can reduce the order of the generated subgroup.
            for (int i = 0; i < factorCount; i++) {
                int factor = factors[i];
                while (divisor % factor == 0 && power(value, order / factor) == 1) {
                    divisor /= factor;
                    order /= factor;
                }
            }
            return order;
        }
    }

    private static final class GcdTree {
        private int base = 1;
        private final int identity;
        private final int[] tree;

        GcdTree(int[] values, int neutral) {
            identity = neutral;
            while (base < values.length) {
                base *= 2;
            }
            tree = new int[2 * base];
            Arrays.fill(tree, identity);
            System.arraycopy(values, 0, tree, base, values.length);
            for (int node = base - 1; node > 0; node--) {
                tree[node] = gcd(tree[2 * node], tree[2 * node + 1]);
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
                int updated = gcd(tree[2 * node], tree[2 * node + 1]);
                if (tree[node] == updated) {
                    break;
                }
                tree[node] = updated;
            }
        }

        int query(int left, int right) {
            int result = identity;
            left += base;
            right += base;
            while (left < right && result != 1) {
                if (left % 2 != 0) {
                    result = gcd(result, tree[left++]);
                }
                if (right % 2 != 0) {
                    result = gcd(result, tree[--right]);
                }
                left /= 2;
                right /= 2;
            }
            return result;
        }
    }

    private static final class Fenwick {
        private final int[] tree;
        private final Group group;

        Fenwick(int length, Group arithmetic) {
            tree = new int[length + 1];
            Arrays.fill(tree, 1);
            group = arithmetic;
        }

        void multiply(int position, int value) {
            for (int node = position + 1; node < tree.length; node += node & -node) {
                tree[node] = group.multiply(tree[node], value);
            }
        }

        int prefix(int position) {
            int result = 1;
            for (int node = position + 1; node > 0; node -= node & -node) {
                result = group.multiply(result, tree[node]);
            }
            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int prime = input.next();
        int length = input.next();
        int queries = input.next();
        Group group = new Group(prime);
        int[] original = new int[length];
        int[] prefix = new int[length + 1];
        prefix[0] = 1;
        for (int i = 0; i < length; i++) {
            original[i] = input.next();
            prefix[i + 1] = group.multiply(prefix[i], original[i]);
        }
        int[] difference = new int[length];
        Arrays.fill(difference, 1);
        // Recover adjacent ratios using a single modular inverse.
        int inverse = group.inverse(prefix[length]);
        for (int i = length - 1; i > 0; i--) {
            inverse = group.multiply(inverse, original[i]);
            difference[i] = group.multiply(original[i], group.multiply(inverse, prefix[i - 1]));
        }
        int[] indices = new int[length];
        indices[0] = prime - 1;
        for (int i = 1; i < length; i++) {
            indices[i] = group.index(difference[i]);
        }
        GcdTree tree = new GcdTree(indices, prime - 1);
        Fenwick changes = new Fenwick(length, group);
        StringBuilder output = new StringBuilder();
        for (int query = 0; query < queries; query++) {
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
                output.append(answer).append('\n');
            }
        }
        System.out.print(output);
    }
}
