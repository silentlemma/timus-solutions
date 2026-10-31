import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next(in);
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = next(in);
            pairs[i][1] = i + 1;
        }
        Arrays.sort(pairs, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                int byCount = Integer.compare(a[0], b[0]);
                return byCount != 0 ? byCount : Integer.compare(a[1], b[1]);
            }
        });
        int q = next(in);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int lo = next(in), hi = next(in), x = next(in);
            int left = 0, right = n;
            // find the first pair at least (x, lo) in lexicographic order.
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (pairs[mid][0] < x || (pairs[mid][0] == x && pairs[mid][1] < lo))
                    left = mid + 1;
                else
                    right = mid;
            }
            boolean found = left < n && pairs[left][0] == x && pairs[left][1] <= hi;
            out.append(found ? '1' : '0');
        }
        System.out.println(out);
    }
}
