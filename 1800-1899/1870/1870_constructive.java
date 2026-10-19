import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // 2 * 3: both must be invertible modulo n
    static final int BAD = 6;

    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        if (gcd(n, BAD) != 1) {
            System.out.println("No");
            return;
        }
        // queen i on row 2i: rows 2i, diagonals 3i and anti-diagonals i are all
        // different modulo n
        StringBuilder out = new StringBuilder("Yes\n");
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                out.append(' ');
            }
            out.append(2L * i % n + 1);
        }
        System.out.println(out);
    }
}
