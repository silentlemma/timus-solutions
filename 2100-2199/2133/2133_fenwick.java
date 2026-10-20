import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int UPDATE = 1;
    private static final int BUFFER_SIZE = 65536;
    private static final InputStream INPUT = System.in;
    private static final byte[] BUFFER = new byte[BUFFER_SIZE];
    private static int inputPosition;
    private static int inputLength;

    private static int read() throws IOException {
        if (inputPosition == inputLength) {
            inputLength = INPUT.read(BUFFER);
            inputPosition = 0;
            if (inputLength < 0) {
                return -1;
            }
        }
        return BUFFER[inputPosition++];
    }

    private static int nextInt() throws IOException {
        int current = read();
        while (current <= ' ') {
            current = read();
        }
        int value = 0;
        while (current >= '0') {
            value = value * 10 + current - '0';
            current = read();
        }
        return value;
    }

    private static void add(int[] tree, int index, int delta) {
        while (index < tree.length) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    private static int prefix(int[] tree, int index) {
        int total = 0;
        while (index > 0) {
            total += tree[index];
            index -= index & -index;
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) {
            heights[i] = nextInt();
        }
        int q = nextInt();
        int[] positions = new int[q];
        int[] values = new int[q];
        int[] coordinates = Arrays.copyOf(heights, n + q);
        for (int i = 0; i < q; i++) {
            positions[i] = -1;
            if (nextInt() == UPDATE) {
                positions[i] = nextInt() - 1;
            }
            values[i] = nextInt();
            coordinates[n + i] = values[i];
        }
        Arrays.sort(coordinates);
        int size = 0;
        for (int value : coordinates) {
            if (size == 0 || coordinates[size - 1] != value) {
                coordinates[size++] = value;
            }
        }
        for (int i = 0; i < n; i++) {
            heights[i] = Arrays.binarySearch(coordinates, 0, size, heights[i]) + 1;
        }
        for (int i = 0; i < q; i++) {
            values[i] = Arrays.binarySearch(coordinates, 0, size, values[i]) + 1;
        }
        int[] tree = new int[size + 1];
        // Each active building contributes one, and each active adjacency removes one.
        for (int i = 0; i < n; i++) {
            tree[heights[i]]++;
            if (i > 0) {
                tree[Math.min(heights[i - 1], heights[i])]--;
            }
        }
        for (int i = 1; i <= size; i++) {
            int parent = i + (i & -i);
            if (parent <= size) {
                tree[parent] += tree[i];
            }
        }
        StringBuilder output = new StringBuilder();
        for (int operation = 0; operation < q; operation++) {
            int position = positions[operation];
            int value = values[operation];
            if (position < 0) {
                output.append(1 - prefix(tree, value - 1)).append('\n');
                continue;
            }
            int old = heights[position];
            if (old == value) {
                continue;
            }
            add(tree, old, -1);
            add(tree, value, 1);
            for (int neighbor = position - 1; neighbor <= position + 1; neighbor += 2) {
                if (neighbor < 0 || neighbor >= n) {
                    continue;
                }
                int before = Math.min(old, heights[neighbor]);
                int after = Math.min(value, heights[neighbor]);
                if (before != after) {
                    add(tree, before, 1);
                    add(tree, after, -1);
                }
            }
            heights[position] = value;
        }
        System.out.print(output.toString());
    }
}
