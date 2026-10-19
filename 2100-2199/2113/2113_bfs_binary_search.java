import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_HEIGHT = 100_000;
    private static final int INF = Integer.MAX_VALUE;

    private static int[] heights;
    private static int[] flood;
    private static int[] distance;
    private static int[] queue;
    private static int[] offsets;
    private static int start;

    private static final class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int ch;
            do {
                ch = input.read();
            } while (ch <= ' ' && ch != -1);
            int value = 0;
            while (ch >= '0' && ch <= '9') {
                value = value * 10 + ch - '0';
                ch = input.read();
            }
            return value;
        }
    }

    private static boolean canEscape(int jump) {
        Arrays.fill(distance, -1);
        distance[start] = 0;
        queue[0] = start;
        int head = 0;
        int tail = 1;
        while (head < tail) {
            int cell = queue[head++];
            if (flood[cell] == INF) {
                return true;
            }
            int arrival = distance[cell] + 1;
            for (int offset : offsets) {
                int next = cell + offset;
                if (distance[next] == -1 && arrival < flood[next]
                        && heights[next] - heights[cell] <= jump) {
                    distance[next] = arrival;
                    queue[tail++] = next;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int rows = input.nextInt();
        int columns = input.nextInt();
        int stride = columns + 2;
        int size = (rows + 2) * stride;
        heights = new int[size];
        flood = new int[size];
        distance = new int[size];
        queue = new int[rows * columns];
        offsets = new int[] {-stride, -1, 1, stride};
        for (int row = 1; row <= rows; row++) {
            for (int column = 1; column <= columns; column++) {
                int cell = row * stride + column;
                heights[cell] = input.nextInt();
                flood[cell] = INF;
            }
        }
        int rabbitRow = input.nextInt();
        int rabbitColumn = input.nextInt();
        start = rabbitRow * stride + rabbitColumn;
        int waterRow = input.nextInt();
        int waterColumn = input.nextInt();
        int water = waterRow * stride + waterColumn;
        flood[water] = 0;
        queue[0] = water;
        int head = 0;
        int tail = 1;
        while (head < tail) {
            int cell = queue[head++];
            for (int offset : offsets) {
                int next = cell + offset;
                if (flood[next] == INF && heights[next] <= heights[cell]) {
                    flood[next] = flood[cell] + 1;
                    queue[tail++] = next;
                }
            }
        }
        if (!canEscape(MAX_HEIGHT)) {
            System.out.println(-1);
            return;
        }
        int low = 0;
        int high = MAX_HEIGHT;
        while (low < high) {
            int middle = low + (high - low) / 2;
            if (canEscape(middle)) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        System.out.println(low);
    }
}
