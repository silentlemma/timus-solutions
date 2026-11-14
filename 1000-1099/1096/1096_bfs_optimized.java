import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_ROUTE = 2000;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = 10 * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = number(input);
        short[] first = new short[MAX_ROUTE + 1];
        short[] front = new short[count + 1], back = new short[count + 1];
        short[] next = new short[count + 1];
        for (short id = 1; id <= count; ++id) {
            int route = number(input);
            front[id] = (short)route;
            back[id] = (short)number(input);
            next[id] = first[route];
            first[route] = id;
        }
        int target = number(input);
        short left = (short)number(input), right = (short)number(input);
        short[] previous = new short[MAX_ROUTE + 1];
        Arrays.fill(previous, (short)-1);
        previous[left] = previous[right] = 0;
        short[] queue = new short[MAX_ROUTE];
        int tail = 0;
        queue[tail++] = left;
        if (right != left) {
            queue[tail++] = right;
        }
        // A swap makes the back route available using one more exchange.
        for (int head = 0; head < tail && previous[target] < 0; ++head) {
            for (short id = first[queue[head]]; id != 0; id = next[id]) {
                short route = back[id];
                if (previous[route] < 0) {
                    previous[route] = id;
                    queue[tail++] = route;
                }
            }
        }
        if (previous[target] < 0) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        short[] path = new short[count];
        int length = 0;
        for (short id = previous[target]; id != 0; id = previous[front[id]]) {
            path[length++] = id;
        }
        StringBuilder output = new StringBuilder().append(length).append('\n');
        while (length > 0) {
            output.append(path[--length]).append('\n');
        }
        System.out.print(output);
    }
}
