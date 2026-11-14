import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    // Floor(log10(2) * SCALE). The product fits in a signed long.
    private static final long LOG_NUMERATOR = 301_029_995_663L;
    private static final long SCALE = 1_000_000_000_000L;

    public static void main(String[] args) throws IOException {
        int ch = System.in.read();
        while (ch >= 0 && ch <= ' ') {
            ch = System.in.read();
        }
        long n = 0;
        while (ch >= '0' && ch <= '9') {
            n = n * DECIMAL + ch - '0';
            ch = System.in.read();
        }
        long even = n & ~1L;
        System.out.println(even * LOG_NUMERATOR / SCALE);
    }
}
