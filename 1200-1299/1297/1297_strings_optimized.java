import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int MAX_LENGTH = 1000;
    private static final int INPUT_BUFFER_SIZE = 1024;

    public static void main(String[] args) throws IOException {
        // the at most 1000 letters go into a byte array with one more byte for the
        // line end, and the answer is written straight from it without a String
        BufferedInputStream input = new BufferedInputStream(System.in, INPUT_BUFFER_SIZE);
        byte[] s = new byte[MAX_LENGTH + 1];
        int inputLength = 0;
        int ch;
        while ((ch = input.read()) != -1 && ch <= ' ') {
        }
        while (ch > ' ' && inputLength < MAX_LENGTH) {
            s[inputLength++] = (byte)ch;
            ch = input.read();
        }
        int n = inputLength, bestStart = 0, bestLen = 0;
        // every letter and every gap between two letters is a centre, 2n - 1 in all, and
        // each is expanded as far as it goes; ties keep the leftmost start
        for (int centre = 0; centre < 2 * n - 1; centre++) {
            int lo = centre / 2, hi = (centre + 1) / 2;
            while (lo >= 0 && hi < n && s[lo] == s[hi]) {
                lo--;
                hi++;
            }
            int length = hi - lo - 1, start = lo + 1;
            if (length > bestLen || (length == bestLen && start < bestStart)) {
                bestStart = start;
                bestLen = length;
            }
        }
        s[bestStart + bestLen] = '\n';
        System.out.write(s, bestStart, bestLen + 1);
    }
}
