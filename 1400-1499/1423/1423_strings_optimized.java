import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int BUFFER = 1 << 16;
    static final int SPACE = ' ';
    static final int BYTE = 0xFF; // bytes read as unsigned

    static byte[] data;
    static int pos;

    // the next run of bytes above the space, as characters from 33 to 255 may come
    static byte[] next() {
        while (pos < data.length && (data[pos] & BYTE) <= SPACE)
            pos++;
        int start = pos;
        while (pos < data.length && (data[pos] & BYTE) > SPACE)
            pos++;
        return java.util.Arrays.copyOfRange(data, start, pos);
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream raw = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int got; (got = in.read(buf)) > 0;)
            raw.write(buf, 0, got);
        data = raw.toByteArray();
        int n = Integer.parseInt(new String(next()));
        byte[] s = next(), t = next();
        // t is s turned left by k, that is right by n - k: find it in s + s with KMP
        int[] fail = new int[n];
        for (int i = 1, k = 0; i < n; i++) {
            while (k > 0 && t[i] != t[k])
                k = fail[k - 1];
            if (t[i] == t[k])
                k++;
            fail[i] = k;
        }
        for (int i = 0, k = 0; i + 1 < 2 * n; i++) {
            byte c = s[i % n];
            while (k > 0 && c != t[k])
                k = fail[k - 1];
            if (c == t[k])
                k++;
            if (k == n) {
                int start = i - n + 1;
                System.out.println((n - start) % n);
                return;
            }
        }
        System.out.println(-1);
    }
}
