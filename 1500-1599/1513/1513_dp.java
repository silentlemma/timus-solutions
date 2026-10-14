import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        // count[i + 1]: lines of i words with no more than k lemons in a row,
        // with count[0] = 1 standing for length -1
        BigInteger[] count = new BigInteger[n + 2];
        count[0] = count[1] = BigInteger.ONE;
        for (int i = 1; i <= n; i++) {
            // a valid line of i words is a valid line of i - 1 words plus a word,
            // except those ending in exactly k + 1 lemons after a banana
            BigInteger next = count[i].shiftLeft(1);
            if (i > k)
                next = next.subtract(count[i - k - 1]);
            count[i + 1] = next;
        }
        System.out.println(count[n + 1]);
    }
}
