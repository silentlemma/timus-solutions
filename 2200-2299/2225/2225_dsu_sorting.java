import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int c = INPUT.read();
        while (c <= ' ') {
            c = INPUT.read();
        }
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = INPUT.read();
        }
        return value;
    }

    private static int findRoot(int[] parent, int vertex) {
        while (parent[vertex] != vertex) {
            parent[vertex] = parent[parent[vertex]];
            vertex = parent[vertex];
        }
        return vertex;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        long[] order = new long[n];
        int[] parent = new int[n];
        int[] size = new int[n];
        for (int i = 0; i < n; ++i) {
            // The index breaks ties without changing the height order.
            order[i] = (long) nextInt() * n + i;
            parent[i] = i;
        }
        Arrays.sort(order);
        long answer = 0;
        for (int position = n - 1; position >= 0; --position) {
            int vertex = (int) (order[position] % n);
            long height = order[position] / n;
            size[vertex] = 1;
            answer += height;
            for (int direction = -1; direction <= 1; direction += 2) {
                int neighbor = vertex + direction;
                if (neighbor < 0 || neighbor >= n || size[neighbor] == 0) {
                    continue;
                }
                int a = findRoot(parent, vertex);
                int b = findRoot(parent, neighbor);
                // Joining two odd runs saves one strike at every remaining level.
                if (size[a] % 2 == 1 && size[b] % 2 == 1) {
                    answer -= height;
                }
                if (size[a] < size[b]) {
                    int temporary = a;
                    a = b;
                    b = temporary;
                }
                parent[b] = a;
                size[a] += size[b];
            }
        }
        System.out.println(answer);
    }
}
