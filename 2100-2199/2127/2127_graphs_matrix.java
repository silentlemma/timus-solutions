import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int MODULUS = 998244353;
    private static final int CYCLE_PERIOD = 4;
    private static final int BRANCH_DEGREE = 3;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int limit;

        private int read() throws IOException {
            if (position == limit) {
                limit = input.read(buffer);
                position = 0;
                if (limit <= 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int integer() throws IOException {
            int current = read();
            while (current <= ' ' && current != -1) {
                current = read();
            }
            int result = 0;
            while (current > ' ') {
                result = result * 10 + current - '0';
                current = read();
            }
            return result;
        }
    }

    private static long power(long base, int exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * base % MODULUS;
            }
            base = base * base % MODULUS;
            exponent >>= 1;
        }
        return result;
    }

    private static long determinant(int[][] matrix, int size) {
        long result = 1;
        for (int column = 0; column < size; column++) {
            int pivot = column;
            while (pivot < size && matrix[pivot][column] == 0) {
                pivot++;
            }
            if (pivot == size) {
                return 0;
            }
            if (pivot != column) {
                int[] temporary = matrix[pivot];
                matrix[pivot] = matrix[column];
                matrix[column] = temporary;
                result = MODULUS - result;
            }
            int value = matrix[column][column];
            result = result * value % MODULUS;
            long inverse = power(value, MODULUS - 2);
            for (int row = column + 1; row < size; row++) {
                if (matrix[row][column] == 0) {
                    continue;
                }
                long factor = matrix[row][column] * inverse % MODULUS;
                for (int next = column + 1; next < size; next++) {
                    long reduced = matrix[row][next] - factor * matrix[column][next] % MODULUS;
                    if (reduced < 0) {
                        reduced += MODULUS;
                    }
                    matrix[row][next] = (int) reduced;
                }
            }
        }
        return result;
    }

    private static void addEdge(int[][] matrix, int from, int to, int weight) {
        matrix[from][to] = (matrix[from][to] + weight) % MODULUS;
        matrix[to][from] = (matrix[to][from] + weight) % MODULUS;
    }

    private static long solve(FastInput input) throws IOException {
        int n = input.integer();
        int m = input.integer();
        int[] head = new int[n];
        int[] degree = new int[n];
        boolean[] alive = new boolean[n];
        Arrays.fill(head, -1);
        Arrays.fill(alive, true);
        int[] to = new int[2 * m];
        int[] next = new int[2 * m];
        for (int edge = 0; edge < m; edge++) {
            int u = input.integer() - 1;
            int v = input.integer() - 1;
            int first = 2 * edge;
            to[first] = v;
            next[first] = head[u];
            head[u] = first;
            to[first + 1] = u;
            next[first + 1] = head[v];
            head[v] = first + 1;
            degree[u]++;
            degree[v]++;
        }
        int[] queue = new int[n];
        int end = 0;
        for (int vertex = 0; vertex < n; vertex++) {
            if (degree[vertex] == 0) {
                return 0;
            }
            if (degree[vertex] == 1) {
                queue[end++] = vertex;
            }
        }
        long answer = 1;
        // A leaf and its neighbor form an invertible block of determinant -1.
        for (int front = 0; front < end; front++) {
            int u = queue[front];
            if (!alive[u]) {
                continue;
            }
            int v = -1;
            for (int edge = head[u]; edge != -1; edge = next[edge]) {
                if (alive[to[edge]]) {
                    v = to[edge];
                    break;
                }
            }
            if (v == -1) {
                return 0;
            }
            alive[u] = false;
            alive[v] = false;
            answer = MODULUS - answer;
            for (int edge = head[v]; edge != -1; edge = next[edge]) {
                int w = to[edge];
                if (!alive[w]) {
                    continue;
                }
                degree[w]--;
                if (degree[w] == 0) {
                    return 0;
                }
                if (degree[w] == 1) {
                    queue[end++] = w;
                }
            }
        }
        int[] ids = new int[n];
        Arrays.fill(ids, -1);
        int branches = 0;
        for (int vertex = 0; vertex < n; vertex++) {
            if (alive[vertex] && degree[vertex] >= BRANCH_DEGREE) {
                ids[vertex] = branches++;
            }
        }
        int capacity = 2 * branches;
        int[][] matrix = new int[capacity][capacity];
        boolean[] seen = new boolean[n];
        int size = branches;
        for (int u = 0; u < n; u++) {
            if (ids[u] == -1) {
                continue;
            }
            for (int edge = head[u]; edge != -1; edge = next[edge]) {
                int v = to[edge];
                if (!alive[v]) {
                    continue;
                }
                if (ids[v] != -1) {
                    if (u < v) {
                        addEdge(matrix, ids[u], ids[v], 1);
                    }
                    continue;
                }
                if (seen[v]) {
                    continue;
                }
                int previous = u;
                int length = 0;
                while (ids[v] == -1) {
                    seen[v] = true;
                    length++;
                    int w = -1;
                    for (int current = head[v]; current != -1; current = next[current]) {
                        if (alive[to[current]] && to[current] != previous) {
                            w = to[current];
                            break;
                        }
                    }
                    previous = v;
                    v = w;
                }
                int weight = 1;
                if (((length / 2) & 1) != 0) {
                    weight = MODULUS - 1;
                    answer = MODULUS - answer;
                }
                // Eliminate pairs on the path; an odd path retains one vertex.
                if ((length & 1) == 0) {
                    addEdge(matrix, ids[u], ids[v], weight);
                } else {
                    if (size == capacity) {
                        return 0;
                    }
                    addEdge(matrix, ids[u], size, weight);
                    addEdge(matrix, ids[v], size, 1);
                    size++;
                }
            }
        }
        for (int start = 0; start < n; start++) {
            if (!alive[start] || ids[start] != -1 || seen[start]) {
                continue;
            }
            int previous = -1;
            int vertex = start;
            int length = 0;
            while (!seen[vertex]) {
                seen[vertex] = true;
                length++;
                int w = -1;
                for (int edge = head[vertex]; edge != -1; edge = next[edge]) {
                    if (alive[to[edge]] && to[edge] != previous) {
                        w = to[edge];
                        break;
                    }
                }
                previous = vertex;
                vertex = w;
            }
            if ((length & 1) != 0) {
                answer = answer * 2 % MODULUS;
            } else if (length % CYCLE_PERIOD == 0) {
                return 0;
            } else {
                answer = answer * (MODULUS - CYCLE_PERIOD) % MODULUS;
            }
        }
        return answer * determinant(matrix, size) % MODULUS;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(solve(new FastInput()));
    }
}
