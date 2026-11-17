import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static BigInteger ways(int length, int limit) {
        if (limit == 0) {
            return BigInteger.ONE;
        }
        if (limit >= length) {
            return BigInteger.ONE.shiftLeft(length);
        }
        int needed = length - limit;
        BigInteger[] history = new BigInteger[Math.min(needed, limit + 2)];
        // Slot j remembers the count for length j - 1, until its last use.
        history[0] = BigInteger.ONE;
        if (history.length > 1) {
            history[1] = BigInteger.ONE;
        }
        BigInteger current = BigInteger.ONE;
        for (int i = 1; i <= length; i++) {
            current = current.shiftLeft(1);
            if (i > limit) {
                current = current.subtract(history[(i - limit - 1) % history.length]);
            }
            if (i + 1 < needed) {
                history[(i + 1) % history.length] = current;
            }
        }
        return current;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer(input.readLine());
        System.out.println(
            ways(Integer.parseInt(tokens.nextToken()), Integer.parseInt(tokens.nextToken())));
    }
}
