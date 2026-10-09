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
        // Josephus: with m characters left, the one that stays last sits at
        // (survivor of m - 1) + STEP, counted from where the first deletion was
        int survivor = 0;
        for (int m = 2; m <= chars.length; m++) {
            survivor = (survivor + STEP) % m;
        }
        char last = (char)chars[survivor];
        System.out.println(last == '?' ? "Yes" : last == ' ' ? "No" : "No comments");
    }
}
