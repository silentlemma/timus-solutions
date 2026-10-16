import java.io.IOException;
import java.io.InputStream;

public class Main {
    // below this many bits the string is short enough to search directly
    static final int SMALL_BITS = 6;
    // the palindrome is made of the numbers 2^(k-1) + 5, 2^(k-1) + 6 and the
    // start of 2^(k-1) + 7, three numbers of k bits less two
    static final int NUMBERS = 3, TAIL = 3, BUFFER = 1 << 16;

    static int longest(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) sb.append(Integer.toBinaryString(i));
        String s = sb.toString();
        int best = 0;
        for (int centre = 0; centre < 2 * s.length() - 1; centre++) {
            int lo = centre / 2, hi = (centre + 1) / 2;
            while (lo >= 0 && hi < s.length() && s.charAt(lo) == s.charAt(hi)) {
                lo--;
                hi++;
            }
            best = Math.max(best, hi - lo - 1);
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        // the number can have a million digits, so it is read as a stream:
        // its length, its value while short, the first one after the leading
        // one and the last three digits are all that matter
        InputStream in = System.in;
        byte[] buffer = new byte[BUFFER];
        int k = 0, value = 0, firstOne = -1, last = 0;
        for (int got = in.read(buffer); got > 0; got = in.read(buffer)) {
            for (int i = 0; i < got; i++) {
                int bit = buffer[i] - '0';
                if (bit != 0 && bit != 1) continue;
                if (bit == 1 && k > 0 && firstOne < 0) firstOne = k;
                if (k < SMALL_BITS) value = value * 2 + bit;
                last = (last * 2 + bit) & ((1 << TAIL) - 1);
                k++;
            }
        }
        if (k < SMALL_BITS) {
            System.out.println(longest(value));
            return;
        }
        // n reaches 2^(k-1) + 7 when a one follows the leading one before the
        // last three bits, or when those bits are all ones
        boolean reached = (firstOne >= 0 && firstOne < k - TAIL) || last == (1 << TAIL) - 1;
        int bits = reached ? k : k - 1;
        System.out.println(NUMBERS * bits - 2);
    }
}
