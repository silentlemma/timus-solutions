import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int length;
        private int offset;

        private int read() throws IOException {
            if (offset == length) {
                length = stream.read(buffer);
                offset = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[offset++];
        }

        int nextInt() throws IOException {
            int character = read();
            while (character <= ' ') {
                character = read();
            }
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    private static final class Entry implements Comparable<Entry> {
        final long score;
        final int role;

        Entry(long score, int role) {
            this.score = score;
            this.role = role;
        }

        @Override
        public int compareTo(Entry other) {
            int order = Long.compare(score, other.score);
            return order != 0 ? order : Integer.compare(role, other.role);
        }
    }

    private static final class Occurrences {
        final int[] positions;
        final int[] owners;
        final int[] starts;
        final int[] sizes;
        final int[] counts;
        final int[] steps;
        final int[] tree;
        final int boundary;

        Occurrences(long[] keys, long stride, int roleCount) {
            int size = keys.length;
            positions = new int[size];
            owners = new int[size];
            starts = new int[roleCount];
            sizes = new int[roleCount];
            counts = new int[roleCount];
            steps = new int[roleCount];
            tree = new int[size];
            boundary = (int) stride;
            long previous = -1;
            int role = -1;
            for (int rank = 0; rank < size; rank++) {
                long value = keys[rank] / stride;
                if (value != previous) {
                    role++;
                    starts[role] = rank;
                    previous = value;
                }
                owners[rank] = role;
                sizes[role]++;
                positions[rank] = (int) (keys[rank] % stride);
            }
            for (role = 0; role < roleCount; role++) {
                steps[role] = Integer.highestOneBit(sizes[role]);
            }
        }

        void build() {
            for (int role = 0; role < starts.length; role++) {
                int base = starts[role];
                int size = sizes[role];
                for (int index = 1; index <= size; index++) {
                    int parent = index + (index & -index);
                    if (parent <= size) {
                        tree[base + parent - 1] += tree[base + index - 1];
                    }
                }
            }
        }

        void add(int rank, int delta) {
            int role = owners[rank];
            int base = starts[role];
            int size = sizes[role];
            for (int index = rank - base + 1; index <= size; index += index & -index) {
                tree[base + index - 1] += delta;
            }
            counts[role] += delta;
        }

        int select(int role, int order) {
            int base = starts[role];
            int size = sizes[role];
            int index = 0;
            for (int step = steps[role]; step > 0; step >>= 1) {
                int next = index + step;
                if (next <= size && tree[base + next - 1] < order) {
                    index = next;
                    order -= tree[base + next - 1];
                }
            }
            return positions[base + index];
        }

        long contribution(int rank) {
            int role = owners[rank];
            int base = starts[role];
            int before = 0;
            for (int index = rank - base; index > 0; index -= index & -index) {
                before += tree[base + index - 1];
            }
            int left = before == 0 ? 0 : select(role, before);
            int right = before == counts[role] ? boundary : select(role, before + 1);
            int position = positions[rank];
            return (long) (position - left) * (right - position);
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int q = input.nextInt();
        long stride = n + 1L;
        long[] initialKeys = new long[n];
        long[] queryKeys = new long[q];
        int[] queryPositions = new int[q];
        long[] keys = new long[n + q];
        for (int position = 0; position < n; position++) {
            long key = input.nextInt() * stride + position + 1;
            initialKeys[position] = key;
            keys[position] = key;
        }
        for (int query = 0; query < q; query++) {
            int position = input.nextInt() - 1;
            long key = input.nextInt() * stride + position + 1;
            queryPositions[query] = position;
            queryKeys[query] = key;
            keys[n + query] = key;
        }
        Arrays.sort(keys);
        int unique = 0;
        for (long key : keys) {
            if (unique == 0 || keys[unique - 1] != key) {
                keys[unique++] = key;
            }
        }
        keys = Arrays.copyOf(keys, unique);
        int roleCount = 0;
        long previous = -1;
        for (long key : keys) {
            long role = key / stride;
            if (role != previous) {
                roleCount++;
                previous = role;
            }
        }
        Occurrences occurrences = new Occurrences(keys, stride, roleCount);
        int[] current = new int[n];
        long total = (long) n * (n + 1) / 2;
        long[] scores = new long[roleCount];
        Arrays.fill(scores, total);
        int[] last = new int[roleCount];
        for (int index = 0; index < n; index++) {
            int rank = Arrays.binarySearch(keys, initialKeys[index]);
            int role = occurrences.owners[rank];
            int position = index + 1;
            current[index] = rank;
            occurrences.tree[rank] = 1;
            occurrences.counts[role]++;
            scores[role] -= (long) (position - last[role]) * (n + 1 - position);
            last[role] = position;
        }
        occurrences.build();
        PriorityQueue<Entry> heap = new PriorityQueue<>();
        for (int role = 0; role < roleCount; role++) {
            heap.add(new Entry(scores[role], role));
        }
        StringBuilder output = new StringBuilder();
        for (int query = 0; query < q; query++) {
            int position = queryPositions[query];
            int oldRank = current[position];
            int newRank = Arrays.binarySearch(keys, queryKeys[query]);
            if (oldRank != newRank) {
                int oldRole = occurrences.owners[oldRank];
                int newRole = occurrences.owners[newRank];
                occurrences.add(oldRank, -1);
                scores[oldRole] += occurrences.contribution(oldRank);
                scores[newRole] -= occurrences.contribution(newRank);
                occurrences.add(newRank, 1);
                current[position] = newRank;
                heap.add(new Entry(scores[oldRole], oldRole));
                heap.add(new Entry(scores[newRole], newRole));
            }
            while (heap.peek().score != scores[heap.peek().role]) {
                heap.remove();
            }
            output.append(heap.peek().score).append('\n');
        }
        System.out.print(output);
    }
}
