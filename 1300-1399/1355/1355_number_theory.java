import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // how many primes multiply to n, counted with repetition
    static int primeFactors(long n) {
        int count = 0;
        for (long d = 2; d * d <= n; d++)
            while (n % d == 0) {
                n /= d;
                count++;
            }
        return count + (n > 1 ? 1 : 0);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int t = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            long a = (long)in.nval;
            in.nextToken();
            long b = (long)in.nval;
            // every step multiplies the number by at least one prime
            out.append(b % a == 0 ? 1 + primeFactors(b / a) : 0).append('\n');
        }
        System.out.print(out);
    }
}
