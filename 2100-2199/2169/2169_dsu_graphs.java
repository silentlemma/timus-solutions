import java.io.IOException;

public class Main {
    private static final long MODULUS = 1_000_000_007L;
    private static final int MAX_INCOMING = 3;
    private static final int MAX_DEGREE = MAX_INCOMING + 1;
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int BYTE_MASK = 255;

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
            return buffer[position++] & BYTE_MASK;
        }

        int nextInt() throws IOException {
            int current = read();
            while (current <= ' ' && current != -1) {
                current = read();
            }
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static final class DisjointSet {
        private final int[] parent;
        private final int[] size;
        private final int[] edges;

        DisjointSet(int count) {
            parent = new int[count];
            size = new int[count];
            edges = new int[count];
            for (int vertex = 0; vertex < count; vertex++) {
                parent[vertex] = vertex;
                size[vertex] = 1;
            }
        }

        int find(int vertex) {
            while (parent[vertex] != vertex) {
                parent[vertex] = parent[parent[vertex]];
                vertex = parent[vertex];
            }
            return vertex;
        }

        void addEdge(int first, int second) {
            int firstRoot = find(first);
            int secondRoot = find(second);
            if (firstRoot == secondRoot) {
                edges[firstRoot]++;
                return;
            }
            if (size[firstRoot] < size[secondRoot]) {
                int temporary = firstRoot;
                firstRoot = secondRoot;
                secondRoot = temporary;
            }
            parent[secondRoot] = firstRoot;
            size[firstRoot] += size[secondRoot];
            edges[firstRoot] += edges[secondRoot] + 1;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int vertexCount = input.nextInt();
        int edgeCount = input.nextInt();
        DisjointSet components = new DisjointSet(vertexCount);
        int[] degree = new int[vertexCount];
        for (int edge = 0; edge < edgeCount; edge++) {
            int first = input.nextInt() - 1;
            int second = input.nextInt() - 1;
            degree[first]++;
            degree[second]++;
            components.addEdge(first, second);
        }

        int[] sinks = new int[vertexCount];
        for (int vertex = 0; vertex < vertexCount; vertex++) {
            if (degree[vertex] > MAX_DEGREE) {
                System.out.println(0);
                return;
            }
            if (degree[vertex] <= MAX_INCOMING) {
                sinks[components.find(vertex)]++;
            }
        }

        long answer = 1;
        for (int root = 0; root < vertexCount; root++) {
            if (components.parent[root] != root) {
                continue;
            }
            if (components.edges[root] > components.size[root]) {
                answer = 0;
                break;
            }
            // Trees choose a sink; a single cycle chooses its direction.
            long choices = components.edges[root] == components.size[root] ? 2 : sinks[root];
            answer = answer * choices % MODULUS;
        }
        System.out.println(answer);
    }
}
