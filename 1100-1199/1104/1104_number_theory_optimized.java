import java.io.IOException;

public class Main {
    static final int MAX_BASE = 36;
    static final int BUFFER_SIZE = 4096;

    public static void main(String[] args) throws IOException {
        byte[] buffer = new byte[BUFFER_SIZE];
        int total = 0, top = 1;
        // the digits are summed chunk by chunk: the line of up to 10^6 digits is
        // never stored
        for (int length; (length = System.in.read(buffer)) > 0;) {
            for (int i = 0; i < length; i++) {
                int c = buffer[i];
                if (c <= ' ')
                    continue;
                int digit = c >= 'A' ? c - 'A' + 10 : c - '0';
                total += digit;
                if (digit > top)
                    top = digit;
            }
        }
        // base is 1 modulo base - 1, so the number is congruent to its digit sum
        for (int base = top + 1; base <= MAX_BASE; base++) {
            if (total % (base - 1) == 0) {
                System.out.println(base);
                return;
            }
        }
        System.out.println("No solution.");
    }
}
