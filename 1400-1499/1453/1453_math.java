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
        int n = (int)in.nval;
        in.nextToken();
        int s = (int)in.nval;
        long rook = (long)n * (s - 1);
        if (n == 1) { // in one dimension a bishop moves exactly like a rook
            System.out.println(rook);
            return;
        }
        // t bishop steps need room t on the chosen side of every coordinate
        int[] both = new int[s]; // both[m]: coordinates with room m on each side
        int reach = s;           // beyond this some coordinate has no room
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int x = (int)in.nval;
            both[Math.min(s - x, x - 1)]++;
            reach = Math.min(reach, Math.max(s - x, x - 1));
        }
        long[] count = new long[n + 1]; // count[k]: lengths t with 2^k directions
        int k = n - both[0];
        for (int t = 1; t <= reach; t++) {
            count[k]++;
            k -= both[t];
        }
        BigInteger ways = BigInteger.ZERO; // the sum of count[k] 2^k, doubling from the top
        for (int j = n; j >= 0; j--)
            ways = ways.shiftLeft(1).add(BigInteger.valueOf(count[j]));
        System.out.println(ways.add(BigInteger.valueOf(rook)));
    }
}
