import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (int)in.nval;
        }
        // n + 1 prefix sums modulo n take at most n values: two of them are
        // equal, and the numbers between them sum to a multiple of n
        int[] first = new int[n];
        Arrays.fill(first, -1);
        first[0] = 0;
        for (int i = 1, sum = 0; i <= n; i++) {
            sum = (sum + a[i - 1]) % n;
            if (first[sum] >= 0) {
                StringBuilder out = new StringBuilder().append(i - first[sum]).append('\n');
                for (int j = first[sum]; j < i; j++) {
                    out.append(a[j]).append('\n');
                }
                System.out.print(out);
                return;
            }
            first[sum] = i;
        }
    }
}
