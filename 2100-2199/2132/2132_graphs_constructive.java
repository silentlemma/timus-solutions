import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;

public class Main {
    private static final int MAX_VERTEX = 100000;
    private static final int MAX_EDGES = 100000;
    private static final int BUFFER_SIZE = 65536;
    private static final int END_OF_INPUT = -1;
    private static final int ROOT_PARENT = -1;

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position >= length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return END_OF_INPUT;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character;
            do {
                character = read();
            } while (character >= 0 && character <= ' ');
            if (character < 0) {
                return END_OF_INPUT;
            }
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    private static void emit(StringBuilder output, int first, int middle, int last) {
        output.append(first).append(' ').append(middle).append(' ').append(last).append('\n');
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int[] first = new int[MAX_EDGES];
        int[] second = new int[MAX_EDGES];
        int[] degree = new int[MAX_VERTEX + 1];
        int edgeCount = 0;
        int largest = 0;
        int from;
        while ((from = input.nextInt()) >= 0) {
            int to = input.nextInt();
            first[edgeCount] = from;
            second[edgeCount++] = to;
            degree[from]++;
            degree[to]++;
            largest = Math.max(largest, Math.max(from, to));
        }

        int[] offset = new int[largest + 2];
        for (int vertex = 1; vertex <= largest; vertex++) {
            offset[vertex + 1] = offset[vertex] + degree[vertex];
        }
        int[] next = offset.clone();
        int[] adjacent = new int[edgeCount * 2];
        for (int edge = 0; edge < edgeCount; edge++) {
            adjacent[next[first[edge]]++] = second[edge];
            adjacent[next[second[edge]]++] = first[edge];
        }

        int[] parent = new int[largest + 1];
        int[] rank = new int[largest + 1];
        int[] stack = new int[largest + 1];
        int[] order = new int[largest + 1];
        int orderSize = 0;
        for (int root = 1; root <= largest; root++) {
            if (degree[root] == 0 || parent[root] != 0) {
                continue;
            }
            parent[root] = ROOT_PARENT;
            int stackSize = 0;
            stack[stackSize++] = root;
            while (stackSize > 0) {
                int vertex = stack[--stackSize];
                rank[vertex] = orderSize;
                order[orderSize++] = vertex;
                for (int index = offset[vertex]; index < offset[vertex + 1]; index++) {
                    int neighbor = adjacent[index];
                    if (parent[neighbor] == 0) {
                        parent[neighbor] = vertex;
                        stack[stackSize++] = neighbor;
                    }
                }
            }
        }

        StringBuilder output = new StringBuilder();
        output.append(edgeCount / 2).append('\n');
        boolean[] usedParent = new boolean[largest + 1];
        for (int index = orderSize - 1; index >= 0; index--) {
            int vertex = order[index];
            int pending = 0;
            for (int edge = offset[vertex]; edge < offset[vertex + 1]; edge++) {
                int neighbor = adjacent[edge];
                if (neighbor == parent[vertex]) {
                    continue;
                }
                if (parent[neighbor] == vertex) {
                    if (usedParent[neighbor]) {
                        continue;
                    }
                } else if (rank[neighbor] > rank[vertex]) {
                    continue;
                }
                if (pending == 0) {
                    pending = neighbor;
                } else {
                    emit(output, pending, vertex, neighbor);
                    pending = 0;
                }
            }
            if (pending != 0) {
                if (parent[vertex] == ROOT_PARENT) {
                    System.out.println(ROOT_PARENT);
                    return;
                }
                emit(output, pending, vertex, parent[vertex]);
                usedParent[vertex] = true;
            }
        }

        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        writer.write(output.toString());
        writer.flush();
    }
}
