import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final long TIME_BASE = 1000001L;

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        input.next();
        int count = input.next();
        long[] origins = new long[count];
        long[] destinations = new long[count];
        long[] keys = new long[2 * count + 2];
        for (int i = 0; i < count; i++) {
            int from = input.next();
            int to = input.next();
            int leave = input.next();
            int enter = input.next();
            origins[i] = from * TIME_BASE + leave;
            destinations[i] = to * TIME_BASE + enter;
            keys[2 * i] = origins[i];
            keys[2 * i + 1] = destinations[i];
        }
        int from = input.next();
        int to = input.next();
        int start = input.next();
        int deadline = input.next();
        long sourceKey = from * TIME_BASE + start;
        long goalKey = to * TIME_BASE + deadline;
        keys[2 * count] = sourceKey;
        keys[2 * count + 1] = goalKey;
        Arrays.sort(keys);
        int nodes = 0;
        for (long key : keys) {
            if (nodes == 0 || key != keys[nodes - 1]) {
                keys[nodes++] = key;
            }
        }
        int[] head = new int[nodes];
        Arrays.fill(head, -1);
        int[] arrival = new int[count];
        int[] following = new int[count];
        for (int i = 0; i < count; i++) {
            int departure = Arrays.binarySearch(keys, 0, nodes, origins[i]);
            arrival[i] = Arrays.binarySearch(keys, 0, nodes, destinations[i]);
            following[i] = head[departure];
            head[departure] = i;
        }
        int source = Arrays.binarySearch(keys, 0, nodes, sourceKey);
        int goal = Arrays.binarySearch(keys, 0, nodes, goalKey);
        int[] previous = new int[nodes];
        int[] usedFlight = new int[nodes];
        Arrays.fill(previous, -1);
        previous[source] = source;
        int[] queue = new int[nodes];
        queue[0] = source;
        int size = 1;
        int cursor = 0;
        while (cursor < size && previous[goal] == -1) {
            int node = queue[cursor++];
            int next = node + 1;
            if (next < nodes && keys[node] / TIME_BASE == keys[next] / TIME_BASE
                && previous[next] == -1) {
                previous[next] = node;
                queue[size++] = next;
            }
            for (int flight = head[node]; flight != -1; flight = following[flight]) {
                int target = arrival[flight];
                if (previous[target] == -1) {
                    previous[target] = node;
                    usedFlight[target] = flight + 1;
                    queue[size++] = target;
                }
            }
        }
        if (previous[goal] == -1) {
            System.out.println("Impossible");
            return;
        }
        int[] route = new int[count];
        int length = 0;
        for (int node = goal; node != source; node = previous[node]) {
            if (usedFlight[node] != 0) {
                route[length++] = usedFlight[node];
            }
        }
        StringBuilder output = new StringBuilder();
        output.append(length).append('\n');
        for (int i = length - 1; i >= 0; i--) {
            if (i != length - 1) {
                output.append(' ');
            }
            output.append(route[i]);
        }
        output.append('\n');
        System.out.print(output);
    }
}
