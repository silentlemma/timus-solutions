import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int TENTHS = 10;

    private static int next(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int whole = 0;
        while (ch >= '0' && ch <= '9') {
            whole = whole * TENTHS + ch - '0';
            ch = input.read();
        }
        if (ch == '.') {
            int fraction = input.read();
            if (fraction >= '0' && fraction <= '9') {
                return whole * TENTHS + fraction - '0';
            }
        }
        return whole * TENTHS;
    }

    private static long square(long x) { return x * x; }

    private static boolean fits(int narrow, int wide, int shortSide, int longSide) {
        if (narrow > shortSide) {
            return false;
        }
        if (wide <= longSide) {
            return true;
        }
        long sum = square(wide + narrow);
        long difference = square(wide - narrow);
        return square(longSide + shortSide) * difference + square(longSide - shortSide) * sum >=
            2 * sum * difference;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int first = next(input);
        int second = next(input);
        int third = next(input);
        int narrow = Math.min(first, second);
        int wide = Math.max(first, second);
        if (third < narrow) {
            wide = narrow;
            narrow = third;
        } else {
            wide = Math.min(wide, third);
        }
        int a = next(input);
        int b = next(input);
        System.out.println(fits(narrow, wide, Math.min(a, b), Math.max(a, b)) ? "YES" : "NO");
    }
}
