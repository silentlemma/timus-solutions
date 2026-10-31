import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
    static class Input {
        final StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int nextInt() throws IOException {
            input.nextToken();
            return (int)input.nval;
        }
    }
    static int[][] readGraph(Input input, int count, int roads) throws IOException {
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
        int first = 2 * start;
        distance[first] = distance[first + 1] = 0;
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(first);
        queue.add(first + 1);
        while (!queue.isEmpty()) {
            int state = queue.removeFirst();
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
                    if (cost == 0)
                        queue.addFirst(nextState);
                    else
                        queue.addLast(nextState);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.nextInt();
        int roads = input.nextInt();
        int[][] adjacency = readGraph(input, count, roads);
        int start = input.nextInt() - 1;
        int target = input.nextInt() - 1;
        System.out.println(minimumChanges(adjacency, start, target));
    }
}
