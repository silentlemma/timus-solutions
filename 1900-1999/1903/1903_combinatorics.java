import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long MODULUS = 1000000007L;

    private static long power(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * base % MODULUS;
            }
            base = base * base % MODULUS;
            exponent /= 2;
        }
        return result;
    }

    private static final class Binomial {
        private final long[] factorial;
        private final long[] inverse;

        Binomial(int maximum) {
            factorial = new long[maximum + 1];
            inverse = new long[maximum + 1];
            factorial[0] = 1;
            for (int i = 1; i <= maximum; i++) {
                factorial[i] = factorial[i - 1] * i % MODULUS;
            }
            inverse[maximum] = power(factorial[maximum], MODULUS - 2);
            for (int i = maximum; i > 0; i--) {
                inverse[i - 1] = inverse[i] * i % MODULUS;
            }
        }

        long choose(int total, int take) {
            if (take < 0 || take > total) {
                return 0;
            }
            return factorial[total] * inverse[take] % MODULUS * inverse[total - take] % MODULUS;
        }
    }

    private static long bad(Binomial combinations, int others, int selected,
                            int pool, int threshold) {
        long result = 0;
        for (int count = threshold; count <= Math.min(pool, selected - 1); count++) {
            result += combinations.choose(pool, count)
                * combinations.choose(others - pool, selected - 1 - count) % MODULUS;
            result %= MODULUS;
        }
        return result;
    }

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.next();
        int selected = input.next();
        int[] classes = new int[n];
        for (int i = 0; i < n; i++) {
            classes[i] = input.next();
        }
        int identified = input.next() - 1;
        int position = input.next();
        int lower = 0;
        int greater = 0;
        for (int value : classes) {
            if (value < classes[identified]) {
                lower++;
            } else if (value > classes[identified]) {
                greater++;
            }
        }
        int others = n - 1;
        Binomial combinations = new Binomial(others);
        long answer = combinations.choose(others, selected - 1);
        answer = (answer - bad(combinations, others, selected, lower, position) + MODULUS)
            % MODULUS;
        answer = (answer - bad(combinations, others, selected, greater, selected - position + 1)
            + MODULUS) % MODULUS;
        System.out.println(answer);
    }
}
