import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static int readNumber(BufferedInputStream input) throws IOException {
        int ch;
        do {
            ch = input.read();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = readNumber(input), gcd = 0;
        for (int i = 0; i < n && gcd != 1; i++) {
            int length = readNumber(input);
            while (length != 0) {
                int remainder = gcd % length;
                gcd = length;
                length = remainder;
            }
        }
        System.out.println(gcd);
    }
}
