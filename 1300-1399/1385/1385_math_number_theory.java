import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    static final int DECIMAL_BASE = 10;

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(
            new BufferedReader(new InputStreamReader(System.in)).readLine().trim());
        BigInteger unit = BigInteger.TEN.pow(n), first = unit.divide(BigInteger.TEN),
                   answer = BigInteger.ZERO;
        // A divides B=k*A, and k must divide10^N; count every possible A.
        for (int k = 1; k < DECIMAL_BASE; k++) {
            BigInteger[] division = unit.divideAndRemainder(BigInteger.valueOf(k));
            if (division[1].signum() == 0)
                answer = answer.add(division[0].subtract(first));
        }
        System.out.println(answer);
    }
}
