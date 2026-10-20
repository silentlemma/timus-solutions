import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int DIRECT = 0;
    private static final int SUBTREE = 1;
    private static final int LIMITED = 2;
    private static final int QUERY = 3;
    private static final int BUFFER_SIZE = 65536;
    private static final int INITIAL_CAPACITY = 4;

    private static class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextTokenStart() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ' && c != -1);
            return c;
        }

        int nextInt() throws IOException {
            int c = nextTokenStart();
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return value;
        }
    }

    private static class IntList {
        private int[] values = new int[INITIAL_CAPACITY];
        private int size;

        void add(int value) {
            if (size == values.length) {
                values = Arrays.copyOf(values, size * 2);
            }
            values[size++] = value;
        }

        int[] sortedUnique() {
            Arrays.sort(values, 0, size);
            int count = 0;
            for (int i = 0; i < size; ++i) {
                if (count == 0 || values[i] != values[count - 1]) {
                    values[count++] = values[i];
                }
            }
            return Arrays.copyOf(values, count);
        }
    }

    private static int lowerBound(int[] values, int target) {
        int left = 0;
        int right = values.length;
        while (left < right) {
            int middle = (left + right) / 2;
            if (values[middle] < target) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int[] parent = new int[n + 1];
        int[] head = new int[n + 1];
        int[] next = new int[n + 1];
        int[] depth = new int[n + 1];
        for (int vertex = 2; vertex <= n; ++vertex) {
            parent[vertex] = input.nextInt();
            next[vertex] = head[parent[vertex]];
            head[parent[vertex]] = vertex;
            depth[vertex] = depth[parent[vertex]] + 1;
        }
        int[] deepest = depth.clone();
        int[] size = new int[n + 1];
        Arrays.fill(size, 1);
        for (int vertex = n; vertex > 1; --vertex) {
            size[parent[vertex]] += size[vertex];
            deepest[parent[vertex]] = Math.max(deepest[parent[vertex]], deepest[vertex]);
        }
        int[] entry = new int[n + 1];
        int[] stack = new int[n];
        int count = 1;
        int timer = 0;
        stack[0] = 1;
        while (count > 0) {
            int vertex = stack[--count];
            entry[vertex] = ++timer;
            for (int child = head[vertex]; child != 0; child = next[child]) {
                stack[count++] = child;
            }
        }

        int q = input.nextInt();
        int[] kind = new int[q];
        int[] vertices = new int[q];
        int[] limits = new int[q];
        long[] values = new long[q];
        IntList[] pending = new IntList[n + 1];
        for (int day = 0; day < q; ++day) {
            int command = input.nextTokenStart();
            int vertex = input.nextInt();
            vertices[day] = vertex;
            if (command == '?') {
                kind[day] = QUERY;
                continue;
            }
            int access = input.nextInt();
            limits[day] = depth[vertex] + access;
            values[day] = input.nextInt();
            if (access == 0) {
                kind[day] = DIRECT;
            } else if (limits[day] >= deepest[vertex]) {
                kind[day] = SUBTREE;
            } else {
                kind[day] = LIMITED;
                for (int side = 0; side < 2; ++side) {
                    int endpoint = entry[vertex] + side * size[vertex];
                    while (endpoint <= n) {
                        if (pending[endpoint] == null) {
                            pending[endpoint] = new IntList();
                        }
                        pending[endpoint].add(limits[day]);
                        endpoint += endpoint & -endpoint;
                    }
                }
            }
        }
        int[][] coordinates = new int[n + 1][];
        long[][] trees = new long[n + 1][];
        for (int i = 1; i <= n; ++i) {
            coordinates[i] = pending[i] == null ? new int[0] : pending[i].sortedUnique();
            trees[i] = new long[coordinates[i].length + 1];
        }

        long[] direct = new long[n + 1];
        long[] ordinary = new long[n + 1];
        StringBuilder output = new StringBuilder();
        for (int day = 0; day < q; ++day) {
            int vertex = vertices[day];
            int position = entry[vertex];
            if (kind[day] == DIRECT) {
                direct[vertex] += values[day];
            } else if (kind[day] == QUERY) {
                long answer = direct[vertex];
                while (position > 0) {
                    answer += ordinary[position];
                    int[] coords = coordinates[position];
                    int index = coords.length - lowerBound(coords, depth[vertex]);
                    while (index > 0) {
                        answer += trees[position][index];
                        index &= index - 1;
                    }
                    position &= position - 1;
                }
                output.append(answer).append('\n');
            } else {
                // Euler differences confine every addition to its subtree.
                for (int side = 0; side < 2; ++side) {
                    int endpoint = position + side * size[vertex];
                    long delta = side == 0 ? values[day] : -values[day];
                    while (endpoint <= n) {
                        if (kind[day] == SUBTREE) {
                            ordinary[endpoint] += delta;
                        } else {
                            int[] coords = coordinates[endpoint];
                            int index = coords.length - lowerBound(coords, limits[day]);
                            while (index < trees[endpoint].length) {
                                trees[endpoint][index] += delta;
                                index += index & -index;
                            }
                        }
                        endpoint += endpoint & -endpoint;
                    }
                }
            }
        }
        System.out.print(output);
    }
}
