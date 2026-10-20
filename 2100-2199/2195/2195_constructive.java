import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final class FastScanner {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int value = 0;
            int c;
            do {
                c = input.read();
            } while (c <= ' ' && c != -1);
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = input.read();
            }
            return value;
        }
    }

    private static final class Tree {
        final int[] parent;
        final int[] order;

        Tree(FastScanner input, int n) throws IOException {
            parent = new int[n];
            order = new int[n];
            int[][] children = new int[n][2];
            int[] childCount = new int[n];
            for (int vertex = 1; vertex < n; vertex++) {
                int p = input.nextInt();
                parent[vertex] = p;
                children[p][childCount[p]++] = vertex;
            }

            int[] stack = new int[n];
            int size = 1;
            int length = 0;
            while (size > 0) {
                int vertex = stack[--size];
                order[length++] = vertex;
                for (int i = childCount[vertex] - 1; i >= 0; i--) {
                    stack[size++] = children[vertex][i];
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        int n = input.nextInt();
        Tree a = new Tree(input, n);
        Tree b = new Tree(input, n);
        int[] label = new int[n];
        for (int i = 0; i < n; i++) {
            label[b.order[i]] = a.order[i];
        }

        int[] moved = new int[n];
        int[] destination = new int[n];
        int count = 0;
        for (int i = 1; i < n; i++) {
            int vertex = a.order[i];
            int previous = a.order[i - 1];
            if (a.parent[vertex] != previous) {
                moved[count] = vertex;
                destination[count++] = previous;
            }
        }
        // Undo the target's flattening after matching the two preorder paths.
        for (int i = n - 1; i > 0; i--) {
            int vertex = b.order[i];
            if (b.parent[vertex] != b.order[i - 1]) {
                moved[count] = label[vertex];
                destination[count++] = label[b.parent[vertex]];
            }
        }

        StringBuilder output = new StringBuilder();
        output.append(count).append('\n');
        for (int i = 0; i < count; i++) {
            output.append(moved[i]).append(' ').append(destination[i]).append('\n');
        }
        System.out.print(output);
    }
}
