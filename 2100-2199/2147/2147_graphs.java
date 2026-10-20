import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final class FastScanner {
        private static final int BUFFER_SIZE = 65536;
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length == -1) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int symbol = read();
            while (symbol <= ' ' && symbol != -1) {
                symbol = read();
            }
            int value = 0;
            while (symbol >= '0' && symbol <= '9') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        int n = input.nextInt();
        int m = input.nextInt();
        long x = input.nextInt();
        long y = input.nextInt();
        int[] from = new int[m];
        int[] to = new int[m];
        int[] outDegree = new int[n];
        int[] inDegree = new int[n];
        for (int edge = 0; edge < m; edge++) {
            from[edge] = input.nextInt() - 1;
            to[edge] = input.nextInt() - 1;
            outDegree[from[edge]]++;
            inDegree[to[edge]]++;
        }
        int[][] graph = new int[n][];
        int[][] reverse = new int[n][];
        for (int vertex = 0; vertex < n; vertex++) {
            graph[vertex] = new int[outDegree[vertex]];
            reverse[vertex] = new int[inDegree[vertex]];
        }
        for (int edge = 0; edge < m; edge++) {
            graph[from[edge]][--outDegree[from[edge]]] = to[edge];
            reverse[to[edge]][--inDegree[to[edge]]] = from[edge];
        }

        boolean[] seen = new boolean[n];
        int[] next = new int[n];
        int[] order = new int[n];
        int orderSize = 0;
        int[] stack = new int[n];
        int top = 0;
        for (int start = 0; start < n; start++) {
            if (seen[start]) {
                continue;
            }
            seen[start] = true;
            stack[top++] = start;
            while (top > 0) {
                int vertex = stack[top - 1];
                if (next[vertex] < graph[vertex].length) {
                    int target = graph[vertex][next[vertex]++];
                    if (!seen[target]) {
                        seen[target] = true;
                        stack[top++] = target;
                    }
                } else {
                    order[orderSize++] = vertex;
                    top--;
                }
            }
        }

        int[] component = new int[n];
        Arrays.fill(component, -1);
        int componentCount = 0;
        for (int index = orderSize - 1; index >= 0; index--) {
            int start = order[index];
            if (component[start] != -1) {
                continue;
            }
            component[start] = componentCount;
            stack[top++] = start;
            while (top > 0) {
                int vertex = stack[--top];
                for (int target : reverse[vertex]) {
                    if (component[target] == -1) {
                        component[target] = componentCount;
                        stack[top++] = target;
                    }
                }
            }
            componentCount++;
        }

        boolean[] weakSeen = new boolean[n];
        boolean[] counted = new boolean[componentCount];
        long answer = 0;
        for (int start = 0; start < n; start++) {
            if (weakSeen[start]) {
                continue;
            }
            long vertices = 0;
            long components = 0;
            weakSeen[start] = true;
            stack[top++] = start;
            while (top > 0) {
                int vertex = stack[--top];
                vertices++;
                int id = component[vertex];
                if (!counted[id]) {
                    counted[id] = true;
                    components++;
                }
                for (int target : graph[vertex]) {
                    if (!weakSeen[target]) {
                        weakSeen[target] = true;
                        stack[top++] = target;
                    }
                }
                for (int target : reverse[vertex]) {
                    if (!weakSeen[target]) {
                        weakSeen[target] = true;
                        stack[top++] = target;
                    }
                }
            }
            long cost = (vertices - 1) * y;
            if (x < y) {
                cost = Math.min((vertices - components) * y + (components - 1) * x,
                        vertices * x);
            }
            answer += cost;
        }
        System.out.println(answer);
    }
}
