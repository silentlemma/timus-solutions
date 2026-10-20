import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final long INFINITY = Long.MAX_VALUE;
    private static final int BUFFER_SIZE = 1 << 16;

    private static final class FastInput {
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

        int integer() throws IOException {
            int symbol;
            do {
                symbol = read();
            } while (symbol <= ' ');
            int value = 0;
            while (symbol >= '0' && symbol <= '9') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }

        void windRow(byte[] wind, int offset, int width) throws IOException {
            int symbol;
            do {
                symbol = read();
            } while (symbol <= ' ');
            wind[offset] = (byte) symbol;
            for (int column = 1; column < width; column++) {
                wind[offset + column] = (byte) read();
            }
        }
    }

    private static final class MinHeap {
        private int[] vertices;
        private long[] times;
        private int size;
        int vertex;
        long time;

        MinHeap(int capacity) {
            vertices = new int[capacity];
            times = new long[capacity];
        }

        void push(int nextVertex, long nextTime) {
            if (size == vertices.length) {
                vertices = Arrays.copyOf(vertices, size * 2);
                times = Arrays.copyOf(times, size * 2);
            }
            int index = size++;
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (times[parent] <= nextTime) {
                    break;
                }
                vertices[index] = vertices[parent];
                times[index] = times[parent];
                index = parent;
            }
            vertices[index] = nextVertex;
            times[index] = nextTime;
        }

        void pop() {
            vertex = vertices[0];
            time = times[0];
            size--;
            if (size == 0) {
                return;
            }
            int lastVertex = vertices[size];
            long lastTime = times[size];
            int index = 0;
            while (index * 2 + 1 < size) {
                int child = index * 2 + 1;
                if (child + 1 < size && times[child + 1] < times[child]) {
                    child++;
                }
                if (lastTime <= times[child]) {
                    break;
                }
                vertices[index] = vertices[child];
                times[index] = times[child];
                index = child;
            }
            vertices[index] = lastVertex;
            times[index] = lastTime;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int height = input.integer();
        int width = input.integer();
        int stride = width + 2;
        int size = (height + 2) * stride;
        int person = input.integer() * stride + input.integer();
        int drone = input.integer() * stride + input.integer();
        int[] cost = new int[size];
        for (int row = 1; row <= height; row++) {
            for (int column = 1; column <= width; column++) {
                cost[row * stride + column] = input.integer();
            }
        }
        byte[] wind = new byte[size];
        for (int row = 1; row <= height; row++) {
            input.windRow(wind, row * stride + 1, width);
        }
        long[] distance = new long[size];
        Arrays.fill(distance, INFINITY);
        distance[person] = 0;
        MinHeap queue = new MinHeap(height * width);
        queue.push(person, 0);
        int[] steps = {-stride, stride, -1, 1};
        while (queue.size > 0) {
            queue.pop();
            int current = queue.vertex;
            long currentTime = queue.time;
            if (currentTime != distance[current]) {
                continue;
            }
            for (int step : steps) {
                int next = current + step;
                if (cost[next] == 0) {
                    continue;
                }
                long arrival = currentTime + cost[next];
                if (arrival < distance[next]) {
                    distance[next] = arrival;
                    queue.push(next, arrival);
                }
            }
        }
        int[] firstVisit = new int[size];
        Arrays.fill(firstVisit, -1);
        int[] path = new int[height * width];
        int pathLength = 0;
        while (cost[drone] != 0 && firstVisit[drone] == -1) {
            firstVisit[drone] = pathLength;
            path[pathLength++] = drone;
            switch (wind[drone]) {
                case 'U':
                    drone -= stride;
                    break;
                case 'D':
                    drone += stride;
                    break;
                case 'L':
                    drone--;
                    break;
                case 'R':
                    drone++;
                    break;
                default:
                    throw new IllegalStateException();
            }
        }
        int cycleStart = firstVisit[drone];
        long cycleLength = pathLength - cycleStart;
        long answer = INFINITY;
        for (int time = 0; time < pathLength; time++) {
            long candidate = time;
            long arrival = distance[path[time]];
            if (arrival > candidate) {
                if (cycleStart == -1 || time < cycleStart) {
                    continue;
                }
                long difference = arrival - candidate;
                candidate += (difference + cycleLength - 1) / cycleLength * cycleLength;
            }
            answer = Math.min(answer, candidate);
        }
        System.out.println(answer == INFINITY ? -1 : answer);
    }
}
