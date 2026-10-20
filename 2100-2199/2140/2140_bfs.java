import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int PADDING = 2;
    private static final int DIRECTION_COUNT = 4;
    private static final int WALK = 0;
    private static final int JUMP = 1;
    private static final int DROP = 2;
    private static final int CLIMB = 3;

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        String next() throws IOException {
            int character;
            do {
                character = input.read();
            } while (character <= ' ' && character != -1);
            StringBuilder token = new StringBuilder();
            while (character > ' ') {
                token.append((char) character);
                character = input.read();
            }
            return token.toString();
        }

        int number() throws IOException {
            return Integer.parseInt(next());
        }

        int position(int width, int plane) throws IOException {
            int x = number();
            int y = number();
            int z = number();
            return z * plane + (x + 1) * width + y + 1;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int a = input.number();
        int b = input.number();
        int h = input.number();
        int width = b + 2 * PADDING;
        int rows = a + 2 * PADDING;
        int plane = width * rows;
        int total = plane * (h + 2);
        boolean[] air = new boolean[total];
        for (int z = 1; z <= h; z++) {
            for (int x = 1; x <= a; x++) {
                String row = input.next();
                int base = z * plane + (x + 1) * width + PADDING;
                for (int y = 0; y < b; y++) {
                    air[base + y] = row.charAt(y) == '.';
                }
            }
        }
        int start = input.position(width, plane);
        int goal = input.position(width, plane);
        boolean[] stand = new boolean[total];
        for (int id = plane; id < total; id++) {
            stand[id] = air[id] && !air[id - plane];
        }
        int[] parent = new int[total];
        Arrays.fill(parent, -1);
        byte[] action = new byte[total];
        int[] queue = new int[total];
        queue[0] = start;
        int tail = 1;
        parent[start] = start;
        int[] deltas = {-width, 1, width, -1};
        for (int head = 0; head < tail && parent[goal] < 0; head++) {
            int current = queue[head];
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                int delta = deltas[direction];
                int near = current + delta;
                if (stand[near] && parent[near] < 0) {
                    parent[near] = current;
                    action[near] = (byte) (WALK * DIRECTION_COUNT + direction);
                    queue[tail++] = near;
                }
                int target = near + delta;
                if (air[near] && air[near - plane] && stand[target] && parent[target] < 0) {
                    parent[target] = current;
                    action[target] = (byte) (JUMP * DIRECTION_COUNT + direction);
                    queue[tail++] = target;
                }
                target = near - plane;
                if (air[near] && stand[target] && parent[target] < 0) {
                    parent[target] = current;
                    action[target] = (byte) (DROP * DIRECTION_COUNT + direction);
                    queue[tail++] = target;
                }
                target = near + plane;
                if (air[current + plane] && stand[target] && parent[target] < 0) {
                    parent[target] = current;
                    action[target] = (byte) (CLIMB * DIRECTION_COUNT + direction);
                    queue[tail++] = target;
                }
            }
        }
        if (parent[goal] < 0) {
            System.out.println("NO");
            return;
        }
        byte[] path = new byte[total];
        int length = 0;
        for (int id = goal; id != start; id = parent[id]) {
            path[length++] = action[id];
        }
        String[] moves = {"walk", "jump", "drop", "climb"};
        String[] directions = {"north", "east", "south", "west"};
        StringBuilder output = new StringBuilder("YES\n");
        output.append(length).append('\n');
        for (int index = length - 1; index >= 0; index--) {
            int code = path[index];
            output.append(moves[code / DIRECTION_COUNT]).append(' ');
            output.append(directions[code % DIRECTION_COUNT]).append('\n');
        }
        System.out.print(output);
    }
}
