import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static InputStream in = new BufferedInputStream(System.in, BUFFER);

    static int read() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int v = 0;
        while (c >= '0') {
            v = v * 10 + c - '0';
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = read();
        // the teacher's dates come sorted, so each of the student's dates is
        // looked up by binary search, counting repeats every time
        int[] known = new int[n];
        for (int i = 0; i < n; i++) {
            known[i] = read();
        }
        int m = read(), count = 0;
        for (int i = 0; i < m; i++) {
            if (Arrays.binarySearch(known, read()) >= 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
