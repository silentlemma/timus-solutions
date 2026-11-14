import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int SMALLEST_CYCLE = 3;

    private static int pairs(int size) { return size * (size - 1) / 2; }

    private static byte[] chooseCycles(int vertices, int target) {
        byte[] minimum = new byte[target + 1];
        byte[] last = new byte[target + 1];
        Arrays.fill(minimum, (byte)(vertices + 1));
        minimum[0] = 0;
        // Use the fewest vertices in cycles. The remaining vertices are singletons.
        for (int size = SMALLEST_CYCLE; size <= vertices; size++) {
            int weight = pairs(size);
            for (int sum = weight; sum <= target; sum++) {
                int count = minimum[sum - weight] + size;
                if (count < minimum[sum]) {
                    minimum[sum] = (byte)count;
                    last[sum] = (byte)size;
                }
            }
        }
        return minimum[target] <= vertices ? last : null;
    }

    private static void edge(StringBuilder output, int a, int b) {
        output.append(a).append(' ').append(b).append('\n');
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer(input.readLine());
        int vertices = Integer.parseInt(tokens.nextToken());
        int target = pairs(vertices) - Integer.parseInt(tokens.nextToken());
        if (target < 0 || target > pairs(vertices)) {
            System.out.println(-1);
            return;
        }
        byte[] last = chooseCycles(vertices, target);
        if (last == null) {
            System.out.println(-1);
            return;
        }

        StringBuilder output = new StringBuilder();
        int first = 1;
        int previous = 0;
        while (target > 0) {
            int size = last[target];
            if (previous != 0) {
                edge(output, previous, first);
            }
            int end = first + size - 1;
            for (int vertex = first; vertex < end; vertex++) {
                edge(output, vertex, vertex + 1);
            }
            edge(output, end, first);
            previous = first;
            first = end + 1;
            target -= pairs(size);
        }
        for (int vertex = first; vertex <= vertices; vertex++) {
            if (previous != 0) {
                edge(output, previous, vertex);
            }
            previous = vertex;
        }
        System.out.print(output);
    }
}
