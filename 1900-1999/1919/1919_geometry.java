import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long nextLong() throws IOException {
        int value;
        do {
            value = INPUT.read();
        } while (value <= ' ' && value >= 0);
        long result = 0;
        while (value > ' ') {
            result = result * 10 + value - '0';
            value = INPUT.read();
        }
        return result;
    }

    private static boolean fits(long first, long second, long height, long circumference) {
        if (first > circumference) {
            return false;
        }
        if (second <= height) {
            return true;
        }
        long residual = height * circumference - first * second;
        if (residual < 0) {
            return false;
        }
        BigInteger remainder = BigInteger.valueOf(residual);
        BigInteger square = BigInteger.valueOf(first * first);
        BigInteger difference = BigInteger.valueOf(circumference * circumference - first * first);
        return remainder.multiply(remainder).compareTo(square.multiply(difference)) >= 0;
    }

    public static void main(String[] args) throws IOException {
        long width = nextLong();
        long height = nextLong();
        long count = nextLong();
        StringBuilder output = new StringBuilder();
        for (long index = 0; index < count; ++index) {
            long cylinderHeight = nextLong();
            long circumference = nextLong();
            boolean possible = fits(width, height, cylinderHeight, circumference)
                    || fits(height, width, cylinderHeight, circumference);
            output.append(possible ? "Block the hole\n" : "Too small\n");
        }
        System.out.print(output);
    }
}
