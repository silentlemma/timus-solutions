import java.io.BufferedInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Main {
    private static final long MODULUS = 614889782588491410L;
    private static final int QUERY_FIELDS = 3;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static String nextToken() throws IOException {
        int value;
        do { value = INPUT.read(); } while (value <= ' ' && value >= 0);
        StringBuilder token = new StringBuilder();
        while (value > ' ') { token.append((char) value); value = INPUT.read(); }
        return token.toString();
    }

    private static long nextLong() throws IOException {
        int value;
        do { value = INPUT.read(); } while (value <= ' ' && value >= 0);
        long result = 0;
        while (value > ' ') { result = result * 10 + value - '0'; value = INPUT.read(); }
        return result;
    }

    static long[] processQueries(String number, long[][] queries) {
        byte[] digits = number.getBytes(StandardCharsets.US_ASCII);
        long[] weights = new long[digits.length];
        weights[0] = 1;
        for (int index = 1; index < weights.length; ++index) {
            weights[index] = weights[index - 1] * 10 % MODULUS;
        }
        long remainder = 0;
        for (byte digit : digits) {
            remainder = (remainder * 10 + (digit - '0')) % MODULUS;
        }
        long[] answers = new long[queries.length];
        int used = 0;
        for (long[] query : queries) {
            if (query[0] == 0) {
                answers[used++] = remainder % query[1];
            } else {
                int place = (int) query[1];
                int index = digits.length - place;
                long difference = query[2] - (digits[index] - '0');
                digits[index] = (byte) ('0' + query[2]);
                remainder = (remainder + difference * weights[place - 1]) % MODULUS;
                if (remainder < 0) remainder += MODULUS;
            }
        }
        return Arrays.copyOf(answers, used);
    }

    public static void main(String[] args) throws IOException {
        String number = nextToken();
        int count = (int) nextLong();
        long[][] queries = new long[count][QUERY_FIELDS];
        for (long[] query : queries) {
            query[0] = nextLong();
            query[1] = nextLong();
            if (query[0] == 1) query[2] = nextLong();
        }
        StringBuilder output = new StringBuilder();
        for (long answer : processQueries(number, queries)) output.append(answer).append('\n');
        System.out.print(output);
    }
}
