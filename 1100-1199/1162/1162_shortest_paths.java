import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BigInteger scaled(String text, int places) {
        int dot = text.indexOf('.');
        int digits = dot < 0 ? 0 : text.length() - dot - 1;
        StringBuilder value = new StringBuilder(text.replace(".", ""));
        for (int i = digits; i < places; i++) {
            value.append('0');
        }
        return new BigInteger(value.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tok.nextToken()), m = Integer.parseInt(tok.nextToken());
        int s = Integer.parseInt(tok.nextToken());
        String text = tok.nextToken();
        int dot = text.indexOf('.');
        int places = Math.max(2, dot < 0 ? 0 : text.length() - dot - 1);
        BigInteger v = scaled(text, places), unit = BigInteger.TEN.pow(places - 2);
        BigInteger hundred = BigInteger.valueOf(100);
        List<int[]> ends = new ArrayList<>();
        List<int[]> terms = new ArrayList<>();
        for (int k = 0; k < m; k++) {
            int a = Integer.parseInt(tok.nextToken()), b = Integer.parseInt(tok.nextToken());
            int rab = scaled(tok.nextToken(), 2).intValue(),
                cab = scaled(tok.nextToken(), 2).intValue();
            int rba = scaled(tok.nextToken(), 2).intValue(),
                cba = scaled(tok.nextToken(), 2).intValue();
            ends.add(new int[] {a, b});
            terms.add(new int[] {rab, cab});
            ends.add(new int[] {b, a});
            terms.add(new int[] {rba, cba});
        }
        // All amounts share an exact denominator, multiplied by 100 each pass.
        // A change on pass n means a reachable gaining cycle.
        BigInteger[] best = new BigInteger[n + 1];
        best[s] = v;
        boolean changed = false;
        for (int pass = 0; pass < n; pass++) {
            BigInteger[] after = new BigInteger[n + 1];
            for (int c = 1; c <= n; c++) {
                if (best[c] != null) {
                    after[c] = best[c].multiply(hundred);
                }
            }
            changed = false;
            for (int e = 0; e < ends.size(); e++) {
                int from = ends.get(e)[0], to = ends.get(e)[1];
                int rate = terms.get(e)[0], fee = terms.get(e)[1];
                BigInteger cost = unit.multiply(BigInteger.valueOf(fee));
                if (best[from] != null && best[from].compareTo(cost) >= 0) {
                    BigInteger got = best[from].subtract(cost).multiply(BigInteger.valueOf(rate));
                    if (after[to] == null || got.compareTo(after[to]) > 0) {
                        after[to] = got;
                        changed = true;
                    }
                }
            }
            best = after;
            unit = unit.multiply(hundred);
            v = v.multiply(hundred);
            if (best[s].compareTo(v) > 0 || !changed) {
                break;
            }
        }
        System.out.println(best[s].compareTo(v) > 0 || changed ? "YES" : "NO");
    }
}
