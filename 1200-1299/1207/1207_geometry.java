import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer tok = new StringTokenizer(in.readLine());
            x[i] = Long.parseLong(tok.nextToken());
            y[i] = Long.parseLong(tok.nextToken());
        }
        // the lowest point (the leftmost of the lowest) sees all others within
        // half a turn, so they can be sorted by angle with cross products
        int pivot = 0;
        for (int i = 1; i < n; i++) {
            if (y[i] < y[pivot] || (y[i] == y[pivot] && x[i] < x[pivot])) {
                pivot = i;
            }
        }
        Integer[] others = new Integer[n - 1];
        for (int i = 0, k = 0; i < n; i++) {
            if (i != pivot) {
                others[k++] = i;
            }
        }
        final long px = x[pivot], py = y[pivot];
        Arrays.sort(others, (i, j) -> {
            long cross = (x[i] - px) * (y[j] - py) - (y[i] - py) * (x[j] - px);
            return Long.compare(0, cross);
        });
        // the middle one leaves (n - 2) / 2 points on each side of the line
        System.out.println((pivot + 1) + " " + (others[(n - 2) / 2] + 1));
    }
}
