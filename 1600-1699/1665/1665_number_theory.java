import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final long FIRST_ODD = 3; // the smallest divisor worth trying

    // whether n is a product of an odd number of factors, each 2 or an odd
    // number above 1: n = 2^twos * rest with rest odd
    static boolean paid(long n) {
        int twos = 0;
        while (n % 2 == 0) {
            n /= 2;
            twos++;
        }
        if (n == 1) {
            return twos % 2 == 1;
        }
        if (twos % 2 == 0) {
            return true; // rest as a single factor
        }
        // an odd count needs rest split into two factors, so not a prime
        for (long d = FIRST_ODD; d * d <= n; d += 2) {
            if (n % d == 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int t = (int) in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            out.append(paid((long) in.nval) ? "YES" : "NO").append('\n');
        }
        System.out.print(out);
    }
}
