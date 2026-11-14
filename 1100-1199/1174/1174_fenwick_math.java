import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int BASE = 1_000_000_000;
    private static final int LIMB_DIGITS = 9;
    private static final int MAX_LIMBS = 18;

    private static int read(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int size = read(input);
        int[] position = new int[size + 1];
        for (int i = 1; i <= size; i++) {
            position[read(input)] = i;
        }
        int[] tree = new int[size + 1];
        int[] rank = new int[MAX_LIMBS];
        int limbs = 1;
        for (int value = 1; value <= size; value++) {
            int pos = position[value];
            int left = 0;
            for (int i = pos - 1; i > 0; i -= i & -i) {
                left += tree[i];
            }
            for (int i = pos; i <= size; i += i & -i) {
                tree[i]++;
            }
            long carry = (rank[0] & 1) == 0 ? value - 1 - left : left;
            for (int i = 0; i < limbs; i++) {
                long number = (long)rank[i] * value + carry;
                rank[i] = (int)(number % BASE);
                carry = number / BASE;
            }
            if (carry != 0) {
                rank[limbs++] = (int)carry;
            }
        }
        int i = 0;
        while (i < limbs && rank[i] == BASE - 1) {
            rank[i++] = 0;
        }
        rank[i]++;
        if (i == limbs) {
            limbs++;
        }
        StringBuilder output = new StringBuilder().append(rank[--limbs]);
        while (limbs > 0) {
            String digits = Integer.toString(rank[--limbs]);
            for (int padding = digits.length(); padding < LIMB_DIGITS; padding++) {
                output.append('0');
            }
            output.append(digits);
        }
        System.out.println(output);
    }
}
