import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);

        int nextInt() throws IOException {
            int value = 0;
            int ch;
            do {
                ch = input.read();
            } while (ch <= ' ' && ch != -1);
            while (ch > ' ') {
                value = value * 10 + ch - '0';
                ch = input.read();
            }
            return value;
        }
    }

    private static int arrange(int[] values, int capacity, int[] queue) {
        Arrays.sort(values);
        int left = 0;
        int right = values.length;
        int at = 0;
        int trips = 0;
        while (right - left >= 2) {
            if (values[left] + values[right - 1] > capacity) {
                // The largest value cannot share a trip with any remaining value.
                queue[at++] = values[left++];
                queue[at++] = values[--right];
                trips += 2;
            } else {
                queue[at++] = values[left++];
                queue[at++] = values[left++];
                ++trips;
            }
        }
        if (left < right) {
            queue[at] = values[left];
            ++trips;
        }
        return trips;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int capacity = input.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; ++i) {
            values[i] = input.nextInt();
        }
        int[] queue = new int[count];
        int trips = arrange(values, capacity, queue);
        StringBuilder output = new StringBuilder();
        output.append(trips).append('\n');
        for (int i = 0; i < count; ++i) {
            if (i > 0) {
                output.append(' ');
            }
            output.append(queue[i]);
        }
        output.append('\n');
        System.out.print(output);
    }
}
