import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;

    static boolean isLetter(int c) { return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'; }

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(System.in);
        byte[] buffer = new byte[BUFFER];
        // best sums with the last word kept and dropped; neighbours may not both stay
        long kept = 0, dropped = 0;
        int length = 0;
        while (true) {
            int read = in.read(buffer);
            for (int i = 0; i < Math.max(read, 1); i++) {
                if (read > 0 && isLetter(buffer[i])) {
                    length++;
                    continue;
                }
                if (length > 0) {
                    long next = dropped + length;
                    dropped = Math.max(dropped, kept);
                    kept = next;
                    length = 0;
                }
            }
            if (read < 0)
                break;
        }
        System.out.println(Math.max(kept, dropped));
    }
}
