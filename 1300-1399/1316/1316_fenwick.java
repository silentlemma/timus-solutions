import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int TOP = 1000000; // 10000.00 in cents
    static final int CENTS = 100;
    static final int DIGITS = 2;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static String next() throws IOException {
        while (!words.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null)
                return "QUIT";
            words = new StringTokenizer(line);
        }
        return words.nextToken();
    }

    // a price with at most two decimals, in cents
    static int cents(String s) {
        int dot = s.indexOf('.');
        String whole = dot < 0 ? s : s.substring(0, dot);
        String frac = (dot < 0 ? "" : s.substring(dot + 1)) + "00";
        return (whole.isEmpty() ? 0 : Integer.parseInt(whole)) * CENTS +
            Integer.parseInt(frac.substring(0, DIGITS));
    }

    public static void main(String[] args) throws IOException {
        // bids counted by price, indexed from the highest price down, so that
        // "at least X" is a Fenwick prefix sum
        int[] tree = new int[TOP + 1];
        long sold = 0;
        for (String kind = next(); !kind.equals("QUIT"); kind = next()) {
            int r = TOP + 1 - cents(next());
            if (kind.equals("SALE")) {
                long k = Long.parseLong(next());
                long count = 0;
                for (; r > 0; r &= r - 1)
                    count += tree[r];
                sold += Math.min(count, k);
            } else {
                int step = kind.equals("BID") ? 1 : -1;
                for (; r <= TOP; r += r & -r)
                    tree[r] += step;
            }
        }
        // the exchange earns one cent per piece sold
        System.out.printf("%d.%02d%n", sold / CENTS, sold % CENTS);
    }
}
