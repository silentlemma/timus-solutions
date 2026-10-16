import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int) in.nval;
        int[] thrown = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            thrown[i] = (int) in.nval;
        }
        BigInteger bn = BigInteger.valueOf(n);
        BigInteger bm = BigInteger.valueOf(n - 1);
        // build the catch X digit by digit in base n. Adding s n^j to X keeps
        // the first j fishermen happy and adds s (n - 1)^j to what fisherman
        // j + 1 finds, which is s (-1)^j modulo n: that fixes s
        BigInteger caught = BigInteger.ZERO, found = BigInteger.ZERO;
        BigInteger powerN = BigInteger.ONE, powerM = BigInteger.ONE;
        for (int j = 0; j < n; j++) {
            int a = thrown[j];
            int s = ((a - found.mod(bn).intValue()) % n + n) % n;
            if (j % 2 == 1) {
                s = (n - s) % n;
            }
            BigInteger bs = BigInteger.valueOf(s);
            caught = caught.add(powerN.multiply(bs));
            found = found.add(powerM.multiply(bs));
            // the fisherman throws a fishes away and leaves (n - 1)/n of the rest
            found = found.subtract(BigInteger.valueOf(a)).divide(bn).multiply(bm);
            powerN = powerN.multiply(bn);
            powerM = powerM.multiply(bm);
        }
        // every catch of this residue modulo n^n works; at least one fish
        System.out.println(caught.signum() == 0 ? powerN : caught);
    }
}
