import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // the 15000th prime is 163841
    static final int LIMIT = 163842;

    public static void main(String[] args) throws IOException {
        boolean[] composite = new boolean[LIMIT];
        int[] primes = new int[LIMIT];
        int count = 0;
        for (int p = 2; p < LIMIT; p++) {
            if (composite[p]) {
                continue;
            }
            primes[count++] = p;
            for (long q = (long)p * p; q < LIMIT; q += p) {
                composite[(int)q] = true;
            }
        }
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int k = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < k; i++) {
            in.nextToken();
            out.append(primes[(int)in.nval - 1]).append("\n");
        }
        System.out.print(out);
    }
}
