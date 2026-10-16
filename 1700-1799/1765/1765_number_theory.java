import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        boolean[] broken = new boolean[n];
        for (int i = 0; i < k; i++) broken[Integer.parseInt(st.nextToken()) - 1] = true;
        List<Integer> primes = new ArrayList<>();
        int m = n;
        for (int d = 2; d * d <= m; d++) {
            if (m % d == 0) {
                primes.add(d);
                while (m % d == 0) m /= d;
            }
        }
        if (m > 1) primes.add(m);
        // a balanced set of tips is a union of disjoint regular p-gons and q-gons,
        // and blades n / (p q) apart form a p by q grid whose rows are the q-gons
        // and whose columns are the p-gons
        int p = primes.get(0), q = primes.size() > 1 ? primes.get(1) : 1;
        int classes = n / (p * q);
        List<Integer> remove = new ArrayList<>();
        for (int base = 0; base < classes; base++) {
            boolean[] badRow = new boolean[p], badCol = new boolean[q];
            int rows = 0, cols = 0;
            for (int t = 0; t < p * q; t++) {
                if (!broken[base + t * classes]) continue;
                if (!badRow[t % p]) rows++;
                if (!badCol[t % q]) cols++;
                badRow[t % p] = true;
                badCol[t % q] = true;
            }
            if (rows == 0) continue;
            // a row and a column always share a cell, so the kept blades are
            // either all clean rows or all clean columns, whichever hold more, and
            // with one prime the rows are single blades that never balance
            boolean byRows = q > 1 && (p - rows) * q >= (q - cols) * p;
            for (int t = 0; t < p * q; t++) {
                int c = base + t * classes;
                boolean dropped = byRows ? badRow[t % p] : badCol[t % q];
                if (dropped && !broken[c]) remove.add(c + 1);
            }
        }
        if (remove.size() + k == n) {
            System.out.println(-1);
            return;
        }
        StringBuilder out = new StringBuilder();
        out.append(remove.size()).append('\n');
        for (int i = 0; i < remove.size(); i++) {
            if (i > 0) out.append(' ');
            out.append(remove.get(i));
        }
        System.out.println(out);
    }
}
