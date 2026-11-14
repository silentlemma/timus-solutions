import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = input.read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = number(input), value = number(input);
        int untouched = value, ending = -value, used = ending;
        // Ending flips the last value. Used allows the flip to end anywhere.
        for (int i = 1; i < n; ++i) {
            value = number(input);
            ending = Math.min(-value, Math.max(ending, untouched));
            used = Math.max(ending, Math.min(value, used));
            untouched = Math.min(value, untouched);
        }
        System.out.println(used);
    }
}
