import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static class FastInput {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ');
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = stream.read();
            }
            return value;
        }
    }

    static int[][] readGraph(FastInput input, int count, int roads) throws IOException {
        int[] lower = new int[roads];
        int[] upper = new int[roads];
        int[] degrees = new int[count];
        for (int i = 0; i < roads; i++) {
            lower[i] = input.nextInt() - 1;
            upper[i] = input.nextInt() - 1;
            degrees[lower[i]]++;
            degrees[upper[i]]++;
        }
        int[][] adjacency = new int[count][];
        for (int city = 0; city < count; city++) {
            adjacency[city] = new int[degrees[city]];
        }
        Arrays.fill(degrees, 0);
        for (int i = 0; i < roads; i++) {
            adjacency[lower[i]][degrees[lower[i]]++] = 2 * upper[i];
            adjacency[upper[i]][degrees[upper[i]]++] = 2 * lower[i] + 1;
        }
        return adjacency;
    }

    static int minimumChanges(int[][] adjacency, int start, int target) {
        int stateCount = 2 * adjacency.length;
        int[] distance = new int[stateCount];
        Arrays.fill(distance, stateCount);
        boolean[] settled = new boolean[stateCount];
        int arcEntries = 0;
        for (int[] neighbors : adjacency) {
            arcEntries += neighbors.length;
        }
        // Two initial entries plus at most one insertion per expanded arc.
        int capacity = 2 * arcEntries + 2 + 1;
        int[] queue = new int[capacity];
        int first = 2 * start;
        distance[first] = distance[first + 1] = 0;
        queue[0] = first;
        queue[1] = first + 1;
        int head = 0;
        int tail = 2;
        while (head != tail) {
            int state = queue[head++];
            if (head == capacity) {
                head = 0;
            }
            if (settled[state]) {
                continue;
            }
            settled[state] = true;
            int city = state / 2;
            int gear = state & 1;
            if (city == target) {
                return distance[state];
            }
            for (int nextState : adjacency[city]) {
                int cost = (nextState & 1) == gear ? 0 : 1;
                int candidate = distance[state] + cost;
                if (candidate < distance[nextState]) {
                    distance[nextState] = candidate;
                    if (cost == 0) {
                        if (head == 0) {
                            head = capacity;
                        }
                        queue[--head] = nextState;
                    } else {
                        queue[tail++] = nextState;
                        if (tail == capacity) {
                            tail = 0;
                        }
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int roads = input.nextInt();
        int[][] adjacency = readGraph(input, count, roads);
        int start = input.nextInt() - 1;
        int target = input.nextInt() - 1;
        System.out.println(minimumChanges(adjacency, start, target));
    }
}
