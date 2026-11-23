import java.io.IOException;

public class Main {
    static final int SIZE = 8;
    static final int[][] DIAGONALS = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    static int[][] board = new int[SIZE][SIZE]; // 0 empty, 1 white, 2 black

    static boolean inside(int c, int r) { return c >= 0 && c < SIZE && r >= 0 && r < SIZE; }

    // some checker has a checker of the other color next to it on a diagonal
    // and a free square right behind that one
    static boolean canCapture() {
        for (int c = 0; c < SIZE; c++) {
            for (int r = 0; r < SIZE; r++) {
                if (board[c][r] == 0)
                    continue;
                for (int[] d : DIAGONALS) {
                    int oc = c + d[0], or = r + d[1], lc = c + 2 * d[0], lr = r + 2 * d[1];
                    if (inside(lc, lr) && board[oc][or] != 0 && board[oc][or] != board[c][r] &&
                        board[lc][lr] == 0)
                        return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        for (int number = 1; in.hasNext(); number++) {
            String move = in.next().toLowerCase();
            int c = move.charAt(0) - 'a', r = Integer.parseInt(move.substring(1)) - 1;
            board[c][r] = number % 2 == 1 ? 1 : 2; // white moves on the odd lines
            if (canCapture()) {
                System.out.println(number);
                return;
            }
        }
        System.out.println("Draw");
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
