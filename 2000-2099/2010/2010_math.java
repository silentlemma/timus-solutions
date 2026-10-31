import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    private static final long[][] MOVES = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
                                           {1, -2},  {1, 2},  {2, -1},  {2, 1}};
    private static final String[] LABELS = {"King", "Knight", "Bishop", "Rook", "Queen"};

    private static long[] solve(long n, long x, long y) {
        long king =
            (1 + (x > 1 ? 1 : 0) + (x < n ? 1 : 0)) * (1 + (y > 1 ? 1 : 0) + (y < n ? 1 : 0)) - 1;
        long knight = 0;
        for (long[] move : MOVES) {
            long nx = x + move[0], ny = y + move[1];
            if (1 <= nx && nx <= n && 1 <= ny && ny <= n)
                knight++;
        }
        long bishop = Math.min(x - 1, y - 1) + Math.min(x - 1, n - y) + Math.min(n - x, y - 1) +
                      Math.min(n - x, n - y);
        long rook = 2 * (n - 1);
        return new long[] {king, knight, bishop, rook, rook + bishop};
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        long n = (long)input.nval;
        input.nextToken();
        long x = (long)input.nval;
        input.nextToken();
        long y = (long)input.nval;
        long[] answer = solve(n, x, y);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < answer.length; i++)
            out.append(LABELS[i]).append(": ").append(answer[i]).append('\n');
        System.out.print(out);
    }
}
