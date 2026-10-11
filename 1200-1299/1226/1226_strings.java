import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int BUFFER = 1 << 16;

    static boolean letter(byte c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream all = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int len = in.read(buf); len > 0; len = in.read(buf)) {
            all.write(buf, 0, len);
        }
        byte[] text = all.toByteArray();
        // every run of Latin letters is reversed in place; everything else stays
        for (int i = 0; i < text.length; i++) {
            int j = i;
            while (j < text.length && letter(text[j])) {
                j++;
            }
            for (int a = i, b = j - 1; a < b; a++, b--) {
                byte t = text[a];
                text[a] = text[b];
                text[b] = t;
            }
            i = Math.max(i, j);
        }
        System.out.write(text);
        System.out.flush();
    }
}
