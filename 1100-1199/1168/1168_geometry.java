import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // R is a real number; all other lengths are integers, so a squared
    // distance is an integer and only the integer part of R*R matters
    static final double EPS = 1e-6;
    // above every altitude a station allows: 32000 plus 100000
    static final long SKY = 1000000;

    static long isqrt(long v) {
        long s = (long)Math.sqrt((double)v);
        while (s * s > v) {
            s--;
        }
        while ((s + 1) * (s + 1) <= v) {
            s++;
        }
        return s;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int m = Integer.parseInt(in.nextToken()), n = Integer.parseInt(in.nextToken());
        int k = Integer.parseInt(in.nextToken());
        long[] h = new long[m * n];
        for (int c = 0; c < m * n; c++) {
            h[c] = Long.parseLong(in.nextToken());
        }
        int[] si = new int[k], sj = new int[k];
        long[] z = new long[k], reach = new long[k];
        boolean[] taken = new boolean[m * n];
        for (int t = 0; t < k; t++) {
            si[t] = Integer.parseInt(in.nextToken()) - 1;
            sj[t] = Integer.parseInt(in.nextToken()) - 1;
            double r = Double.parseDouble(in.nextToken());
            z[t] = h[si[t] * n + sj[t]];
            reach[t] = (long)(r * r + EPS);
            taken[si[t] * n + sj[t]] = true;
        }
        long total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (taken[i * n + j]) {
                    continue;
                }
                // the receiver at altitude a hears a station at height z
                // when (a - z)^2 <= R^2 - (horizontal distance)^2
                long low = h[i * n + j], high = SKY;
                for (int t = 0; t < k && low <= high; t++) {
                    long di = i - si[t], dj = j - sj[t];
                    long rest = reach[t] - di * di - dj * dj;
                    if (rest < 0) {
                        high = -1;
                        break;
                    }
                    long s = isqrt(rest);
                    low = Math.max(low, z[t] - s);
                    high = Math.min(high, z[t] + s);
                }
                if (low <= high) {
                    total += high - low + 1;
                }
            }
        }
        System.out.println(total);
    }
}
