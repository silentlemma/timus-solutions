import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final long MODULUS = 1000000007;

    private static long power(long value, int exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * value % MODULUS;
            }
            value = value * value % MODULUS;
            exponent >>= 1;
        }
        return result;
    }

    static long[] settingsCounts(int size) {
        long[] ways = new long[size + 1];
        for (int count = 1; count <= size; count++) {
            long closed = 0;
            for (int prefix = 1; prefix < count; prefix++) {
                closed = (closed * count + ways[prefix]) % MODULUS;
            }
            long difference = (power(count, count - 1) - closed + MODULUS) % MODULUS;
            ways[count] = count * difference % MODULUS;
        }
        return ways;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(input.readLine().trim());
        System.out.println(settingsCounts(size)[size]);
    }
}
