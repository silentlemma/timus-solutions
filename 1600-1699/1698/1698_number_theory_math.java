import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    private static final BigInteger FIVE = BigInteger.valueOf(5);
    private static final int ONE_DIGIT_SOLUTIONS = 3;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine().trim());
        BigInteger oddPower = FIVE.pow(n);
        BigInteger modulus = BigInteger.ONE.shiftLeft(n);
        // This residue is zero modulo 5^n and one modulo 2^n.
        String suffix = oddPower.multiply(oddPower.modInverse(modulus)).toString();
        // An omitted leading zero still contributes one number via its complement.
        int count = ONE_DIGIT_SOLUTIONS + n - suffix.length();
        for (int i = 0; i < suffix.length() - 1; i++) {
            char digit = suffix.charAt(i);
            count += (digit == '0' || digit == '9') ? 1 : 2;
        }
        System.out.println(count);
    }
}
