import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;

public class Main {
    private static final long LABEL_BASE = 1000000001L;
    private static final int BUFFER_SIZE = 65536;
    private static final int SPACE = ' ';

    private static final InputStream STREAM = System.in;
    private static final byte[] BUFFER = new byte[BUFFER_SIZE];
    private static int position;
    private static int size;

    private static int read() throws IOException {
        if (position == size) {
            size = STREAM.read(BUFFER);
            position = 0;
            if (size < 0) {
                return -1;
            }
        }
        return BUFFER[position++];
    }

    private static int nextInt() throws IOException {
        int current = read();
        while (current <= SPACE && current >= 0) {
            current = read();
        }
        int value = 0;
        while (current > SPACE) {
            value = value * 10 + current - '0';
            current = read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int length = nextInt();
        int[] values = new int[length];
        int[] tree = new int[2 * length];
        for (int index = 0; index < length; index++) {
            values[index] = nextInt();
            tree[length + index] = values[index];
        }
        for (int index = length - 1; index > 0; index--) {
            tree[index] = Math.max(tree[2 * index], tree[2 * index + 1]);
        }

        int[] goodUntil = new int[length];
        for (int offset = 0; offset < 2; offset++) {
            HashMap<Long, Integer> nextEdge = new HashMap<>(length);
            int limit = length;
            for (int start = length - 2 - offset; start >= 0; start -= 2) {
                int first = values[start];
                int second = values[start + 1];
                if (first == 0 || second == 0 || first == second) {
                    limit = start;
                } else {
                    if (first > second) {
                        int temporary = first;
                        first = second;
                        second = temporary;
                    }
                    long key = first * LABEL_BASE + second;
                    Integer next = nextEdge.put(key, start);
                    if (next != null) {
                        limit = Math.min(limit, next);
                    }
                }
                goodUntil[start] = limit;
            }
        }

        int answer = 0;
        for (int start = 0; start + 1 < length; start++) {
            int vertices = values[start];
            int edges = values[start + 1];
            if (vertices == 0 || edges > (length - start - 2) / 2) {
                continue;
            }
            if (edges == 0) {
                answer++;
                continue;
            }
            int end = start + 2 + 2 * edges;
            if (end > goodUntil[start + 2]) {
                continue;
            }
            int left = length + start + 2;
            int right = length + end;
            int largest = 0;
            while (left < right) {
                if (left % 2 == 1) {
                    largest = Math.max(largest, tree[left++]);
                }
                if (right % 2 == 1) {
                    largest = Math.max(largest, tree[--right]);
                }
                left /= 2;
                right /= 2;
            }
            if (largest <= vertices) {
                answer++;
            }
        }
        System.out.print(answer + "\n");
    }
}
