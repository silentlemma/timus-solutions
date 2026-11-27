import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class Main {
    static final int STEP = 1999;

    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream text = new ByteArrayOutputStream();
        for (int c; (c = System.in.read()) != -1;) {
            if (c != '\r' && c != '\n') {
                text.write(c);
            }
        }
        byte[] chars = text.toByteArray();
        // Josephus: J(m) is zero-based from the original counting start.
        // After the first deletion, counting restarts STEP positions from that start.
        // Thus J(m) = (J(m - 1) + STEP) % m, with J(1) = 0.
        int survivor = 0;
        for (int m = 2; m <= chars.length; m++) {
            survivor = (survivor + STEP) % m;
        }
        char last = (char)chars[survivor];
        System.out.println(last == '?' ? "Yes" : last == ' ' ? "No" : "No comments");
    }
}
