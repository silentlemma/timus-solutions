import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int TOP = 0, BOTTOM = 1, NORTH = 2, SOUTH = 3, EAST = 4, WEST = 5, SIDES = 6;
    static final int GO_EAST = 0, GO_WEST = 1, GO_NORTH = 2, GO_SOUTH = 3, MOVES = 4;
    static final int SIZE = 12;
    static final int[] DX = {1, -1, 0, 0};
    static final int[] DY = {0, 0, 1, -1};

    // a roll moves every face to a new side; only the side that holds the
    // starting top face matters, so each roll (east, west, north, south)
    // maps every side to the side it lands on
    static final int[][] ROLL = {
        {EAST, WEST, NORTH, SOUTH, BOTTOM, TOP},
        {WEST, EAST, NORTH, SOUTH, TOP, BOTTOM},
        {NORTH, SOUTH, BOTTOM, TOP, EAST, WEST},
        {SOUTH, NORTH, TOP, BOTTOM, EAST, WEST},
    };

    static GoalInput input = new GoalInput();
    static String next() throws IOException { return input.next(); }
    static int number() throws IOException { return input.nextInt(); }

    public static void main(String[] args) throws IOException {
        int width = number(), height = number();
        int a = number(), b = number();
        int c = number(), d = number();
        boolean[][][] blocked = new boolean[SIZE][SIZE][MOVES];
        String kind = "";
        for (String w = next(); w != null; w = next()) {
            if (w.equals("v") || w.equals("h")) {
                kind = w;
                continue;
            }
            int n = Integer.parseInt(w), m = number();
            // a v wall stands between (n, m) and (n + 1, m), an h wall between
            // (n, m) and (n, m + 1), and each blocks the move both ways
            if (kind.equals("v")) {
                blocked[n][m][GO_EAST] = blocked[n + 1][m][GO_WEST] = true;
            } else {
                blocked[n][m][GO_NORTH] = blocked[n][m + 1][GO_SOUTH] = true;
            }
        }
        int[][][] dist = new int[SIZE][SIZE][SIDES];
        for (int[][] plane : dist) {
            for (int[] row : plane)
                Arrays.fill(row, -1);
        }
        int[] queue = new int[SIZE * SIZE * SIDES];
        int head = 0, tail = 0;
        dist[a][b][TOP] = 0;
        queue[tail++] = (a * SIZE + b) * SIDES + TOP;
        while (head < tail) {
            int state = queue[head++];
            int side = state % SIDES, cell = state / SIDES;
            int x = cell / SIZE, y = cell % SIZE;
            if (x == c && y == d && side == TOP) {
                System.out.println(dist[x][y][side]);
                return;
            }
            for (int k = 0; k < MOVES; k++) {
                int nx = x + DX[k], ny = y + DY[k];
                if (nx < 1 || nx > width || ny < 1 || ny > height || blocked[x][y][k])
                    continue;
                int ns = ROLL[k][side];
                if (dist[nx][ny][ns] < 0) {
                    dist[nx][ny][ns] = dist[x][y][side] + 1;
                    queue[tail++] = (nx * SIZE + ny) * SIDES + ns;
                }
            }
        }
        System.out.println("No solution");
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[4096];
        private int position, length;
        private String pending;
        double nval;
        String sval;

        int read() throws IOException {
            if (position >= length) {
                length = System.in.read(data);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return data[position++] & 255;
        }

        private int first() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        long nextLong() throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        int nextInt() throws IOException { return (int)nextLong(); }

        String next() throws IOException {
            if (pending != null) {
                String word = pending;
                pending = null;
                return word;
            }
            int c = first();
            if (c < 0)
                return null;
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }

        boolean hasNext() throws IOException {
            if (pending == null)
                pending = next();
            return pending != null;
        }

        void nextToken() throws IOException {
            int c = first();
            if ((c >= '0' && c <= '9') || c == '-' || c == '+') {
                boolean negative = c == '-';
                if (negative || c == '+')
                    c = read();
                long value = 0;
                while (c >= '0' && c <= '9') {
                    value = value * 10 + c - '0';
                    c = read();
                }
                nval = negative ? -value : value;
                sval = null;
            } else {
                StringBuilder word = new StringBuilder();
                while (c > ' ') {
                    word.append((char)c);
                    c = read();
                }
                sval = word.toString();
            }
        }

        long scaled(int scale) throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            boolean fraction = false;
            while (c > ' ') {
                if (c == '.')
                    fraction = true;
                else {
                    value = value * 10 + c - '0';
                    if (fraction)
                        scale /= 10;
                }
                c = read();
            }
            value *= scale;
            return negative ? -value : value;
        }
    }
}
