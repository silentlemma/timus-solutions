import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int PRIME_THREE = 3;
    private static final int PRIME_FIVE = 5;
    private static final int MAX_THREE_WEIGHT = 3;
    private static final int FIVE_WEIGHT = 4;

    static int hall(int value, int groups) {
        int[] primes = {2, PRIME_THREE, PRIME_FIVE};
        int[] weights = {1, Math.min(groups - 1, MAX_THREE_WEIGHT), FIVE_WEIGHT};
        int color = 0;
        for (int index = 0; index < primes.length; ++index) {
            while (value % primes[index] == 0) {
                value /= primes[index];
                color += weights[index];
            }
        }
        return color % groups + 1;
    }

    static int nextInt(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int size = nextInt(in), groups = nextInt(in);
        StringBuilder output = new StringBuilder("Yes\n");
        for (int index = 0; index < size; ++index)
            output.append(hall(nextInt(in), groups)).append('\n');
        System.out.print(output);
    }
}
