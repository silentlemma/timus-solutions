import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static String readToken(BufferedInputStream input) throws IOException {
        StringBuilder token = new StringBuilder();
        int ch = input.read();
        while (ch <= ' ' && ch != -1) {
            ch = input.read();
        }
        while (ch > ' ') {
            token.append((char) ch);
            ch = input.read();
        }
        return token.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        String x = readToken(input);
        String y = readToken(input);
        int size = Math.max(x.length(), y.length());
        int xPadding = size - x.length();
        int yPadding = size - y.length();

        int propagating = 0;
        int longest = 0;
        for (int i = 0; i < size; ++i) {
            char a = i < xPadding ? '0' : x.charAt(i - xPadding);
            char b = i < yPadding ? '0' : y.charAt(i - yPadding);
            if (a != b) {
                ++propagating;
            } else {
                // A common one starts a carry through the differing bits above it.
                if (a == '1') {
                    longest = Math.max(longest, propagating + 1);
                }
                propagating = 0;
            }
        }
        // Include the initial call and the final call with a zero second argument.
        System.out.println(longest + 2);
    }
}
