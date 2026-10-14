import java.io.*;

public class Main {
    static final String ENDS = ".!?"; // marks that end a sentence
    static final int CHUNK = 1 << 14; // bytes read at a time

    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        byte[] chunk = new byte[CHUNK];
        for (int n; (n = System.in.read(chunk)) > 0;)
            buffer.write(chunk, 0, n);
        byte[] text = buffer.toByteArray();
        boolean start = true; // the next letter opens a sentence
        for (int i = 0; i < text.length; i++) {
            byte c = text[i];
            if (c >= 'A' && c <= 'Z') {
                if (!start)
                    text[i] = (byte)(c + 'a' - 'A');
                start = false;
            } else if (ENDS.indexOf(c) >= 0) {
                start = true;
            }
        }
        System.out.write(text);
        System.out.flush();
    }
}
