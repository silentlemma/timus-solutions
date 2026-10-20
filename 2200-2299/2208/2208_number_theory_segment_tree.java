import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_FACTORS = 7;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final BufferedInputStream input =
                new BufferedInputStream(System.in, BUFFER_SIZE);

        int nextInt() throws IOException {
            int current;
            do {
                current = input.read();
            } while (current <= ' ');
            int value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = input.read();
            }
            return value;
        }
    }

    private static final class PrimeSets {
        final int[] offset;
        final int[] length;
        final int[] count;
        final int[] coordinate;
        final int[] bit;
        final int[] previous;

        PrimeSets(int maximum, int[] positions, int[] starts, int[] lengths) {
            offset = starts;
            length = lengths;
            coordinate = positions;
            count = new int[maximum + 1];
            bit = new int[positions.length];
            previous = new int[positions.length];
        }

        int locate(int prime, int position) {
            int left = 1;
            int right = length[prime] + 1;
            while (left < right) {
                int middle = (left + right) / 2;
                if (coordinate[offset[prime] + middle] < position) {
                    left = middle + 1;
                } else {
                    right = middle;
                }
            }
            return left;
        }

        void add(int prime, int index, int delta) {
            for (; index <= length[prime]; index += index & -index) {
                bit[offset[prime] + index] += delta;
            }
            count[prime] += delta;
        }

        int prefix(int prime, int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) {
                result += bit[offset[prime] + index];
            }
            return result;
        }

        int selectNode(int prime, int rank) {
            int step = Integer.highestOneBit(length[prime]);
            int index = 0;
            for (; step > 0; step /= 2) {
                int next = index + step;
                if (next <= length[prime] && bit[offset[prime] + next] < rank) {
                    rank -= bit[offset[prime] + next];
                    index = next;
                }
            }
            return offset[prime] + index + 1;
        }
    }

    private static final class SegmentTree {
        final int base;
        final int[] maximum;

        SegmentTree(int length) {
            int size = 1;
            while (size < length) {
                size *= 2;
            }
            base = size;
            maximum = new int[base * 2];
        }

        void set(int position, int value) {
            int node = base + position - 1;
            maximum[node] = value;
            for (node /= 2; node > 0; node /= 2) {
                maximum[node] = Math.max(maximum[node * 2], maximum[node * 2 + 1]);
            }
        }

        int first(int node, int left, int right, int queryLeft, int queryRight) {
            if (right < queryLeft || left > queryRight || maximum[node] < queryLeft) {
                return 0;
            }
            if (left == right) {
                return left;
            }
            int middle = (left + right) / 2;
            int result = first(node * 2, left, middle, queryLeft, queryRight);
            if (result == 0) {
                result = first(node * 2 + 1, middle + 1, right, queryLeft, queryRight);
            }
            return result;
        }
    }

    private static PrimeSets sets;
    private static SegmentTree tree;
    private static int[] members;

    private static void refresh(int position) {
        int best = 0;
        int end = (position + 1) * MAX_FACTORS;
        for (int slot = position * MAX_FACTORS; slot < end; slot++) {
            best = Math.max(best, sets.previous[members[slot]]);
        }
        tree.set(position, best);
    }

    private static void collect(int position, int value, int[] spf, int[][] raw,
                                int[] sizes) {
        while (value > 1) {
            int prime = spf[value];
            if (raw[prime] == null) {
                raw[prime] = new int[2];
            } else if (sizes[prime] == raw[prime].length) {
                raw[prime] = Arrays.copyOf(raw[prime], sizes[prime] * 2);
            }
            raw[prime][sizes[prime]++] = position;
            while (value % prime == 0) {
                value /= prime;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int q = input.nextInt();
        int[] values = new int[n + 1];
        int maximum = 2;
        for (int position = 1; position <= n; position++) {
            values[position] = input.nextInt();
            maximum = Math.max(maximum, values[position]);
        }
        int[] kinds = new int[q];
        int[] first = new int[q];
        int[] second = new int[q];
        for (int index = 0; index < q; index++) {
            kinds[index] = input.nextInt();
            first[index] = input.nextInt();
            second[index] = input.nextInt();
            if (kinds[index] == 2) {
                maximum = Math.max(maximum, second[index]);
            }
        }
        int[] spf = new int[maximum + 1];
        for (int prime = 2; prime <= maximum; prime++) {
            if (spf[prime] != 0) {
                continue;
            }
            spf[prime] = prime;
            if (prime <= maximum / prime) {
                for (int multiple = prime * prime; multiple <= maximum; multiple += prime) {
                    if (spf[multiple] == 0) {
                        spf[multiple] = prime;
                    }
                }
            }
        }
        int[][] raw = new int[maximum + 1][];
        int[] sizes = new int[maximum + 1];
        for (int position = 1; position <= n; position++) {
            collect(position, values[position], spf, raw, sizes);
        }
        for (int index = 0; index < q; index++) {
            if (kinds[index] == 2) {
                collect(first[index], second[index], spf, raw, sizes);
            }
        }
        int capacity = 1;
        for (int size : sizes) {
            capacity += size;
        }
        int[] coordinate = new int[capacity];
        int[] offset = new int[maximum + 1];
        int[] length = new int[maximum + 1];
        int used = 0;
        for (int prime = 2; prime <= maximum; prime++) {
            if (sizes[prime] == 0) {
                continue;
            }
            Arrays.sort(raw[prime], 0, sizes[prime]);
            offset[prime] = used;
            int last = 0;
            for (int index = 0; index < sizes[prime]; index++) {
                int position = raw[prime][index];
                if (position != last) {
                    coordinate[++used] = position;
                    length[prime]++;
                    last = position;
                }
            }
            raw[prime] = null;
        }
        sets = new PrimeSets(maximum, Arrays.copyOf(coordinate, used + 1), offset, length);
        members = new int[(n + 1) * MAX_FACTORS];
        int[] last = new int[maximum + 1];
        tree = new SegmentTree(n);
        for (int position = 1; position <= n; position++) {
            int slot = position * MAX_FACTORS;
            int best = 0;
            for (int value = values[position]; value > 1;) {
                int prime = spf[value];
                int node = sets.offset[prime] + sets.locate(prime, position);
                members[slot++] = node;
                sets.previous[node] = last[prime];
                sets.bit[node] = 1;
                best = Math.max(best, last[prime]);
                last[prime] = position;
                sets.count[prime]++;
                while (value % prime == 0) {
                    value /= prime;
                }
            }
            tree.maximum[tree.base + position - 1] = best;
        }
        for (int prime = 2; prime <= maximum; prime++) {
            for (int index = 1; index <= length[prime]; index++) {
                int parent = index + (index & -index);
                if (parent <= length[prime]) {
                    sets.bit[offset[prime] + parent] += sets.bit[offset[prime] + index];
                }
            }
        }
        for (int node = tree.base - 1; node > 0; node--) {
            tree.maximum[node] = Math.max(tree.maximum[node * 2], tree.maximum[node * 2 + 1]);
        }
        StringBuilder output = new StringBuilder();
        for (int query = 0; query < q; query++) {
            int left = first[query];
            int right = second[query];
            if (kinds[query] == 1) {
                int position = tree.first(1, 1, tree.base, left, right);
                if (position == 0) {
                    output.append(-1).append('\n');
                } else {
                    output.append(tree.maximum[tree.base + position - 1]);
                    output.append(' ').append(position).append('\n');
                }
                continue;
            }
            int oldValue = values[left];
            if (oldValue == right) {
                continue;
            }
            for (int value = oldValue; value > 1;) {
                int prime = spf[value];
                if (right % prime != 0) {
                    int index = sets.locate(prime, left);
                    int node = sets.offset[prime] + index;
                    int rank = sets.prefix(prime, index);
                    if (rank < sets.count[prime]) {
                        int next = sets.selectNode(prime, rank + 1);
                        sets.previous[next] = sets.previous[node];
                        refresh(sets.coordinate[next]);
                    }
                    sets.add(prime, index, -1);
                }
                while (value % prime == 0) {
                    value /= prime;
                }
            }
            for (int value = right; value > 1;) {
                int prime = spf[value];
                if (oldValue % prime != 0) {
                    int index = sets.locate(prime, left);
                    int node = sets.offset[prime] + index;
                    int rank = sets.prefix(prime, index - 1);
                    sets.previous[node] = 0;
                    if (rank > 0) {
                        sets.previous[node] = sets.coordinate[sets.selectNode(prime, rank)];
                    }
                    if (rank < sets.count[prime]) {
                        int next = sets.selectNode(prime, rank + 1);
                        sets.previous[next] = left;
                        refresh(sets.coordinate[next]);
                    }
                    sets.add(prime, index, 1);
                }
                while (value % prime == 0) {
                    value /= prime;
                }
            }
            values[left] = right;
            int slot = left * MAX_FACTORS;
            Arrays.fill(members, slot, slot + MAX_FACTORS, 0);
            for (int value = right; value > 1;) {
                int prime = spf[value];
                members[slot++] = sets.offset[prime] + sets.locate(prime, left);
                while (value % prime == 0) {
                    value /= prime;
                }
            }
            refresh(left);
        }
        System.out.print(output);
    }
}
