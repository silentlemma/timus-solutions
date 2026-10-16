import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long FOUR = 4;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            StringTokenizer tokens = new StringTokenizer(line);
            while (tokens.hasMoreTokens()) {
                long m = Long.parseLong(tokens.nextToken());
                // by the Hull-Dobell theorem the full cycles come from a - 1
                // divisible by every prime of m, and by 4 when 4 divides m,
                // with any b coprime to m; so a runs over 1, 1 + c, ...
                long c = 1, rest = m;
                for (long p = 2; p * p <= rest; p++) {
                    if (rest % p == 0) {
                        c *= p;
                        while (rest % p == 0) rest /= p;
                    }
                }
                if (rest > 1) c *= rest;
                if (m % FOUR == 0) c *= 2;
                out.append((m - c + 2) / 2).append('\n');
            }
        }
        System.out.print(out);
    }
}
