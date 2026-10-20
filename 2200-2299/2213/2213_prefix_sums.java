import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int SPACE = ' ';
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static String next() throws IOException {
        StringBuilder token = new StringBuilder();
        int c;
        do {
            c = INPUT.read();
        } while (c <= SPACE && c != -1);
        while (c > SPACE) {
            token.append((char)c);
            c = INPUT.read();
        }
        return token.toString();
    }

    private static long cell(long[] board, int n, int m, int row, int col) {
        if (row < 0 || row >= n || col < 0 || col >= m) {
            return 0;
        }
        return board[row * m + col];
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(next());
        int m = Integer.parseInt(next());
        long[] board = new long[n * m];
        for (int i = 0; i < board.length; ++i) {
            board[i] = Long.parseLong(next());
        }
        String s = next();
        int length = s.length();
        String directions = "RDLU";
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int[] x = new int[length + 1];
        int[] y = new int[length + 1];
        long[] cost = new long[length + 1];
        cost[0] = board[0];
        for (int i = 0; i < length; ++i) {
            int d = directions.indexOf(s.charAt(i));
            x[i + 1] = x[i] + dx[d];
            y[i + 1] = y[i] + dy[d];
            cost[i + 1] = cell(board, n, m, x[i + 1], y[i + 1]);
        }
        long best = 0;
        int source = 0;
        int target = 0;
        for (int d = 0; d < directions.length(); ++d) {
            long left = 0, right = 0, leftMax = 0, rightMax = 0;
            int leftAt = 0, rightAt = -1;
            for (int i = 0; i < length; ++i) {
                // Prefix maxima select endpoints of the translated path interval.
                if (left > leftMax) {
                    leftMax = left;
                    leftAt = i;
                }
                left += cell(board, n, m, x[i] + dx[d], y[i] + dy[d]) - cost[i + 1];
                if (s.charAt(i) == directions.charAt(d) && left - leftMax < best) {
                    best = left - leftMax;
                    source = i;
                    target = leftAt;
                }
                if (s.charAt(i) == directions.charAt(d) && (rightAt == -1 || right > rightMax)) {
                    rightMax = right;
                    rightAt = i;
                }
                right += cell(board, n, m, x[i + 1] - dx[d], y[i + 1] - dy[d]) - cost[i];
                if (rightAt != -1 && right - rightMax < best) {
                    best = right - rightMax;
                    source = rightAt;
                    target = i;
                }
            }
        }
        char moved = s.charAt(source);
        StringBuilder answer = new StringBuilder(s);
        answer.deleteCharAt(source);
        answer.insert(target, moved);
        System.out.println(answer);
    }
}
