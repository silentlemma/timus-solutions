import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long CENTS = 100;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        long k = Long.parseLong(in.nextToken());
        // lengths have exactly two decimals, so in centimetres they are exact
        long[] cables = new long[n];
        long high = 0;
        for (int i = 0; i < n; i++) {
            cables[i] = Long.parseLong(in.nextToken().replace(".", ""));
            high = Math.max(high, cables[i]);
        }
        // more pieces come out of shorter ones, so the longest length that
        // still gives k pieces is found by binary search; 0 means even 1 cm
        // is too long
        long low = 0;
        while (low < high) {
            long mid = (low + high + 1) / 2, pieces = 0;
            for (long c : cables) {
                pieces += c / mid;
            }
            if (pieces >= k) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        System.out.println(String.format("%d.%02d", low / CENTS, low % CENTS));
    }
}
