public class Main {
    static final int MAX_LENGTH = 1000;
    static short[] first = new short[MAX_LENGTH + 1], second = new short[MAX_LENGTH + 1];
    static boolean[] forward = new boolean[MAX_LENGTH + 1], backward = new boolean[MAX_LENGTH + 1];
    static char[] moves = new char[2 * MAX_LENGTH];
    static int used;

    static String token() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        StringBuilder value = new StringBuilder();
        while (c > ' ') {
            value.append((char)c);
            c = System.in.read();
        }
        return value.toString();
    }
    static boolean frontier(boolean[] row, int a0, int a1, int b0, int b1, int step) {
        int width = (b1 - b0) * step;
        for (int t = 0; t <= width; t++)
            row[t] = false;
        row[0] = true;
        for (int i = a0;; i += step) {
            boolean any = false;
            for (int t = 0; t <= width; t++) {
                int sum = first[i] + second[b0 + step * t];
                row[t] = sum >= -1 && sum <= 1 && (row[t] || (t > 0 && row[t - 1]));
                any |= row[t];
            }
            if (!any)
                return false;
            if (i == a1)
                break;
        }
        return true;
    }
    static void append(char move, int count) {
        while (count-- > 0)
            moves[used++] = move;
    }
    static boolean recover(int a0, int a1, int b0, int b1) {
        if (a0 == a1 || b0 == b1) {
            for (int i = a0; i <= a1; i++)
                for (int j = b0; j <= b1; j++) {
                    int sum = first[i] + second[j];
                    if (sum < -1 || sum > 1)
                        return false;
                }
            append(a0 == a1 ? '2' : '1', a1 - a0 + b1 - b0);
            return true;
        }
        int middle = (a0 + a1) / 2;
        boolean single = a1 - a0 == 1;
        if (!frontier(forward, a0, single ? a0 : middle, b0, b1, 1) ||
            !frontier(backward, a1, single ? a1 : middle, b1, b0, -1))
            return false;
        int width = b1 - b0, split = -1;
        for (int t = 0; t <= width; t++)
            if (forward[t] && backward[width - t]) {
                split = t;
                break;
            }
        if (split < 0)
            return false;
        // Height1 selects an edge between two rows, not a recursively equal half.
        if (single) {
            append('2', split);
            append('1', 1);
            append('2', width - split);
            return true;
        }
        // All recursive frames keep only indices; the buffers are shared.
        return recover(a0, middle, b0, b0 + split) && recover(middle, a1, b0 + split, b1);
    }
    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(token());
        String a = token(), b = token();
        for (int i = 0; i < n; i++) {
            first[i + 1] = (short)(first[i] + (a.charAt(i) == '1' ? 1 : -1));
            second[i + 1] = (short)(second[i] + (b.charAt(i) == '1' ? 1 : -1));
        }
        System.out.println(recover(0, n, 0, n) ? new String(moves, 0, used) : "Impossible");
    }
}
