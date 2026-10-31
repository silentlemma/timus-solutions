import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static final BufferedReader INPUT = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");

    // tokenize text without scanner; keep every decimal digit for exact rounding.
    static String next() throws java.io.IOException {
        while (!tokens.hasMoreTokens())
            tokens = new StringTokenizer(INPUT.readLine());
        return tokens.nextToken();
    }

    static final int TOTAL = 1000, MAX_ODD = 100, OUTCOMES = 3;

    public static void main(String[] args) throws java.io.IOException {
        BigInteger numerator = BigInteger.ONE;
        BigInteger denominator = BigInteger.ZERO;
        for (int i = 0; i < OUTCOMES; i++) {
            BigDecimal odd = new BigDecimal(next());
            int scale = Math.max(odd.scale(), 0);
            BigInteger value = odd.setScale(scale).unscaledValue();
            denominator =
                denominator.multiply(value).add(numerator.multiply(BigInteger.TEN.pow(scale)));
            numerator = numerator.multiply(value);
        }
        numerator = numerator.multiply(BigInteger.valueOf(TOTAL));
        // betting in proportion to 1 / k on every outcome pays the same whatever
        // happens, and any other split pays less on some outcome
        int low = 0, high = TOTAL * MAX_ODD / OUTCOMES + 1;
        while (low + 1 < high) {
            int middle = (low + high) / 2;
            if (numerator.multiply(BigInteger.valueOf(2))
                    .compareTo(denominator.multiply(BigInteger.valueOf(2 * middle - 1))) >= 0)
                low = middle;
            else
                high = middle;
        }
        System.out.println(low);
    }
}
