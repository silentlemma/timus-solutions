import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int DAY = 24 * 60;
    private static final int TRUCK = 3_000_000;
    private static final int CUP = 100;
    private static final int ORDER = 10_000_000;
    private static final int VERTEX_BITS = 9;
    private static final int TIME_BITS = 11;
    private static final int LOAD_SHIFT = VERTEX_BITS + TIME_BITS;
    private static final int VERTEX_MASK = (1 << VERTEX_BITS) - 1;
    private static final int TIME_MASK = (1 << TIME_BITS) - 1;
    private static final int NONE = -1;
    private static final int BUFFER_SIZE = 16 * 1024;
    private static final int INITIAL_DEGREE = 4;

    private static class Input {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, size;

        private int nextByte() throws IOException {
            if (position >= size) {
                size = stream.read(buffer);
                position = 0;
                if (size < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int number() throws IOException {
            int c = nextByte();
            while (c >= 0 && c <= ' ') {
                c = nextByte();
            }
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = nextByte();
            }
            return value;
        }
    }

    private static class Routes {
        private final long[][] graph;
        private final int[] degree, distance, previous, next;
        private final int[] heads = new int[DAY + 1];

        Routes(int vertices) {
            graph = new long[vertices][];
            degree = new int[vertices];
            distance = new int[vertices];
            previous = new int[vertices];
            next = new int[vertices];
        }

        void add(int from, long edge) {
            int count = degree[from];
            if (count == 0) {
                graph[from] = new long[INITIAL_DEGREE];
            } else if (count == graph[from].length) {
                graph[from] = Arrays.copyOf(graph[from], count * 2);
            }
            graph[from][count] = edge;
            degree[from] = count + 1;
        }

        int sortAndBound() {
            int destination = graph.length - 1;
            if (degree[0] == 0 || degree[destination] == 0) {
                return 0;
            }
            for (int v = 0; v < graph.length; ++v) {
                if (degree[v] > 1) {
                    Arrays.sort(graph[v], 0, degree[v]);
                }
            }
            return (int)(Math.min(graph[0][degree[0] - 1],
                                  graph[destination][degree[destination] - 1]) >>>
                         LOAD_SHIFT);
        }

        boolean canDeliver(int load) {
            long threshold = (long)load << LOAD_SHIFT;
            Arrays.fill(distance, DAY + 1);
            Arrays.fill(heads, NONE);
            distance[0] = 0;
            previous[0] = next[0] = NONE;
            heads[0] = 0;
            for (int minute = 0; minute <= DAY; ++minute) {
                while (heads[minute] != NONE) {
                    int v = heads[minute];
                    heads[minute] = next[v];
                    if (next[v] != NONE) {
                        previous[next[v]] = NONE;
                    }
                    if (v == graph.length - 1) {
                        return true;
                    }
                    for (int i = degree[v] - 1; i >= 0; --i) {
                        long edge = graph[v][i];
                        if (edge < threshold) {
                            break;
                        }
                        int to = (int)(edge & VERTEX_MASK);
                        int arrival = minute + (int)(edge >>> VERTEX_BITS & TIME_MASK);
                        int old = distance[to];
                        if (arrival >= old) {
                            continue;
                        }
                        if (old <= DAY) {
                            int before = previous[to], after = next[to];
                            if (before == NONE) {
                                heads[old] = after;
                            } else {
                                next[before] = after;
                            }
                            if (after != NONE) {
                                previous[after] = before;
                            }
                        }
                        distance[to] = arrival;
                        previous[to] = NONE;
                        next[to] = heads[arrival];
                        if (next[to] != NONE) {
                            previous[next[to]] = to;
                        }
                        heads[arrival] = to;
                    }
                }
            }
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int vertices = input.number(), roads = input.number();
        if (vertices == 1) {
            System.out.println(ORDER);
            return;
        }
        Routes graph = new Routes(vertices);
        int[] loads = new int[roads];
        int count = 0;
        for (int i = 0; i < roads; ++i) {
            int a = input.number() - 1, b = input.number() - 1;
            int minutes = input.number(), weight = input.number();
            if (weight >= TRUCK + CUP) {
                int load = (weight - TRUCK) / CUP;
                long edge = (long)load << LOAD_SHIFT | (long)minutes << VERTEX_BITS;
                graph.add(a, edge | b);
                graph.add(b, edge | a);
                loads[count++] = load;
            }
        }
        int upper = graph.sortAndBound();
        Arrays.sort(loads, 0, count);
        int distinct = 0;
        for (int i = 0; i < count && loads[i] <= upper; ++i) {
            int load = loads[i];
            if (distinct == 0 || load != loads[distinct - 1]) {
                loads[distinct++] = load;
            }
        }
        int left = 0, right = distinct;
        while (left < right) {
            int middle = (left + right) / 2;
            if (graph.canDeliver(loads[middle])) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        System.out.println(left == 0 ? 0 : loads[left - 1]);
    }
}
