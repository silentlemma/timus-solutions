import java.io.*;
import java.util.*;

public class Main {
    static long mod(long v, long m) { return (v % m + m) % m; }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line = in.readLine();
        if (line == null)
            return;
        long n = Long.parseLong(line.trim());
        HashSet<Long> used = new HashSet<>((int)(2 * n));
        StringBuilder out = new StringBuilder();
        long total = 0, length = 0; // the sum and the number of terms so far
        for (long m = 1; m <= n; m++) {
            // put a large x at position k and then m at k + 1: x must make the
            // sum divisible by k, and x + m divisible by k + 1
            long k = length + 1;
            long a = mod(-total, k);
            long b = mod(-total - m, k + 1);
            // x = a + k t, and k = -1 modulo k + 1, so t = a - b modulo k + 1
            long step = k * (k + 1);
            long x = a + k * mod(a - b, k + 1);
            if (x <= n)
                x += (n - x) / step * step + step;
            while (used.contains(x))
                x += step;
            used.add(x);
            out.append(x).append(' ').append(m).append(m < n ? ' ' : '\n');
            total += x + m;
            length += 2;
        }
        PrintWriter w = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        w.print(out);
        w.flush();
    }
}
