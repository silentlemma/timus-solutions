import java.util.HashMap;
import java.util.Map;

public class Main {

    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available <= 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static String next() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        StringBuilder value = new StringBuilder();
        while (c > ' ') {
            value.append((char)c);
            c = read();
        }
        return value.toString();
    }

    static final String[] MEDALS = {"gold", "silver", "bronze"};
    static final int PER_MEDAL = 4;
    static final int PRIZE = 5;

    public static void main(String[] args) throws java.io.IOException {
        Map<String, String> medal = new HashMap<>();
        // each name and forecast occupies its own line; retain only medallists.
        for (String kind : MEDALS)
            for (int i = 0; i < PER_MEDAL; i++)
                medal.put(next(), kind);
        int n = (int)nextLong(), best = -1, winners = 0;
        for (int p = 0; p < n; p++) {
            int k = (int)nextLong(), right = 0;
            for (int i = 0; i < k; i++) {
                String team = next();
                next();
                if (next().equals(medal.get(team)))
                    right++;
            }
            if (right > best) {
                best = right;
                winners = 1;
            } else if (right == best)
                winners++;
        }
        System.out.println(PRIZE * winners);
    }
}
