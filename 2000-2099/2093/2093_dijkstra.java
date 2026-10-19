import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final long SNOW_SCALE = 100;
    private static final long SNOW_FACTOR = 100500;
    private static final long SNOW_LIMIT = SNOW_SCALE * (SNOW_FACTOR - 1);
    private static final int TIME_BITS = 30;
    private static final long TIME_MASK = (1L << TIME_BITS) - 1;
    private static final long INFINITY = Long.MAX_VALUE / 2;

    private static class FastInput {
        private static final int BUFFER_SIZE = 1 << 16;
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position >= length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character;
            do {
                character = read();
            } while (character <= ' ');
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    private static class Heap {
        private final long[] times;
        private final int[] vertices;
        private int size;
        long currentTime;
        int currentVertex;

        Heap(int capacity) {
            times = new long[capacity];
            vertices = new int[capacity];
        }

        void push(long time, int vertex) {
            int index = size++;
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (times[parent] <= time) {
                    break;
                }
                times[index] = times[parent];
                vertices[index] = vertices[parent];
                index = parent;
            }
            times[index] = time;
            vertices[index] = vertex;
        }

        void pop() {
            currentTime = times[0];
            currentVertex = vertices[0];
            --size;
            if (size == 0) {
                return;
            }
            long time = times[size];
            int vertex = vertices[size];
            int index = 0;
            while (index * 2 + 1 < size) {
                int child = index * 2 + 1;
                if (child + 1 < size && times[child + 1] < times[child]) {
                    ++child;
                }
                if (times[child] >= time) {
                    break;
                }
                times[index] = times[child];
                vertices[index] = vertices[child];
                index = child;
            }
            times[index] = time;
            vertices[index] = vertex;
        }
    }

    private static long[] base;
    private static int[] offset;
    private static long[] intervals;

    private static long duration(int edge, long elapsed) {
        elapsed = Math.min(elapsed, SNOW_LIMIT);
        return base[edge] + (elapsed * base[edge] + SNOW_SCALE - 1) / SNOW_SCALE;
    }

    private static long earliest(int edge, long current) {
        long lastFinish = 0;
        for (int index = offset[edge]; index < offset[edge + 1]; ++index) {
            long start = intervals[index] >>> TIME_BITS;
            long finish = intervals[index] & TIME_MASK;
            long departure = Math.max(current, lastFinish);
            if (departure < start) {
                long arrival = departure + duration(edge, departure - lastFinish);
                // A feasible arrival precedes every later cleaning and open gap.
                if (arrival <= start) {
                    return arrival;
                }
            }
            lastFinish = finish;
        }
        long departure = Math.max(current, lastFinish);
        return departure + duration(edge, departure - lastFinish);
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int vertexCount = input.nextInt();
        int edgeCount = input.nextInt();
        int[] head = new int[vertexCount];
        Arrays.fill(head, -1);
        int[] target = new int[2 * edgeCount];
        int[] next = new int[2 * edgeCount];
        int[] road = new int[2 * edgeCount];
        base = new long[edgeCount];
        offset = new int[edgeCount + 1];
        for (int edge = 0; edge < edgeCount; ++edge) {
            int from = input.nextInt() - 1;
            int to = input.nextInt() - 1;
            base[edge] = input.nextInt();
            int arc = 2 * edge;
            target[arc] = to;
            next[arc] = head[from];
            road[arc] = edge;
            head[from] = arc;
            ++arc;
            target[arc] = from;
            next[arc] = head[to];
            road[arc] = edge;
            head[to] = arc;
        }

        int cleaningCount = input.nextInt();
        int[] cleaningRoad = new int[cleaningCount];
        long[] unsorted = new long[cleaningCount];
        for (int index = 0; index < cleaningCount; ++index) {
            int edge = input.nextInt() - 1;
            long start = input.nextInt();
            long finish = input.nextInt();
            cleaningRoad[index] = edge;
            unsorted[index] = (start << TIME_BITS) | finish;
            ++offset[edge + 1];
        }
        for (int edge = 0; edge < edgeCount; ++edge) {
            offset[edge + 1] += offset[edge];
        }
        intervals = new long[cleaningCount];
        int[] cursor = offset.clone();
        for (int index = 0; index < cleaningCount; ++index) {
            intervals[cursor[cleaningRoad[index]]++] = unsorted[index];
        }
        for (int edge = 0; edge < edgeCount; ++edge) {
            Arrays.sort(intervals, offset[edge], offset[edge + 1]);
        }

        long[] distance = new long[vertexCount];
        Arrays.fill(distance, INFINITY);
        Heap heap = new Heap(edgeCount + 1);
        distance[0] = 0;
        heap.push(0, 0);
        while (heap.size > 0) {
            heap.pop();
            long current = heap.currentTime;
            int vertex = heap.currentVertex;
            if (current != distance[vertex]) {
                continue;
            }
            if (vertex == vertexCount - 1) {
                System.out.println(current);
                break;
            }
            for (int arc = head[vertex]; arc != -1; arc = next[arc]) {
                int to = target[arc];
                int edge = road[arc];
                if (current + base[edge] >= distance[to]) {
                    continue;
                }
                long arrival = earliest(edge, current);
                if (arrival < distance[to]) {
                    distance[to] = arrival;
                    heap.push(arrival, to);
                }
            }
        }
    }
}
