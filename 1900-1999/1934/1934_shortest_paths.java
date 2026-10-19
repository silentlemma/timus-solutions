import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    private static final int PERCENT_SCALE = 100;
    private static final int PROBABILITY_DIGITS = 12;
    private static final int INPUT_BUFFER_SIZE = 1 << 16;

    private static final class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);
        private final byte[] buffer = new byte[INPUT_BUFFER_SIZE];
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

        int nextInt() throws IOException {
            int symbol;
            do {
                symbol = read();
            } while (symbol <= ' ' && symbol >= 0);
            int value = 0;
            while (symbol > ' ') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }
    }

    private static final class Graph {
        final int[] head;
        final int[] next;
        final int[] edge;
        private int size;

        Graph(int count, int roads) {
            head = new int[count];
            Arrays.fill(head, -1);
            next = new int[2 * roads];
            edge = new int[2 * roads];
        }

        void add(int first, int second, int probability) {
            next[size] = head[first];
            edge[size] = PERCENT_SCALE * second + probability;
            head[first] = size++;
        }
    }

    private static final class Route {
        final int[] path;
        final double risk;

        Route(int[] path, double risk) {
            this.path = path;
            this.risk = risk;
        }
    }

    private static Route safestShortestPath(Graph graph, int start, int target) {
        int count = graph.head.length;
        double[] costs = new double[PERCENT_SCALE];
        for (int probability = 0; probability < PERCENT_SCALE; probability++) {
            costs[probability] = -Math.log1p(-(double) probability / PERCENT_SCALE);
        }
        int[] distance = new int[count];
        int[] parent = new int[count];
        int[] queue = new int[count];
        double[] best = new double[count];
        Arrays.fill(distance, -1);
        Arrays.fill(parent, -1);
        Arrays.fill(best, Double.POSITIVE_INFINITY);
        distance[start] = 0;
        best[start] = 0;
        queue[0] = start;
        int tail = 1;
        for (int head = 0; head < tail; head++) {
            int city = queue[head];
            if (city == target) {
                break;
            }
            for (int index = graph.head[city]; index >= 0; index = graph.next[index]) {
                int neighbor = graph.edge[index] / PERCENT_SCALE;
                int probability = graph.edge[index] % PERCENT_SCALE;
                if (distance[neighbor] < 0) {
                    distance[neighbor] = distance[city] + 1;
                    queue[tail++] = neighbor;
                }
                if (distance[neighbor] == distance[city] + 1) {
                    double candidate = best[city] + costs[probability];
                    if (candidate < best[neighbor]) {
                        best[neighbor] = candidate;
                        parent[neighbor] = city;
                    }
                }
            }
        }
        int[] path = new int[distance[target] + 1];
        int city = target;
        for (int index = path.length - 1; index >= 0; index--) {
            path[index] = city;
            city = parent[city];
        }
        return new Route(path, -Math.expm1(-best[target]));
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int roads = input.nextInt();
        int start = input.nextInt() - 1;
        int target = input.nextInt() - 1;
        Graph graph = new Graph(count, roads);
        for (int index = 0; index < roads; index++) {
            int first = input.nextInt() - 1;
            int second = input.nextInt() - 1;
            int probability = input.nextInt();
            graph.add(first, second, probability);
            graph.add(second, first, probability);
        }
        Route route = safestShortestPath(graph, start, target);
        StringBuilder output = new StringBuilder();
        output.append(route.path.length).append(' ');
        output.append(String.format(Locale.US, "%." + PROBABILITY_DIGITS + "f%n", route.risk));
        for (int index = 0; index < route.path.length; index++) {
            if (index != 0) {
                output.append(' ');
            }
            output.append(route.path[index] + 1);
        }
        System.out.println(output);
    }
}
