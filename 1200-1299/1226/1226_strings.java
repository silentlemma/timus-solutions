import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class Main {
    static boolean letter(int c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

    public static void main(String[] args) throws IOException {
        // latin-1 preserves every input byte; only ascii letters are transformed.
        BufferedReader in =
            new BufferedReader(new InputStreamReader(System.in, StandardCharsets.ISO_8859_1));
        BufferedWriter out =
            new BufferedWriter(new OutputStreamWriter(System.out, StandardCharsets.ISO_8859_1));
        StringBuilder word = new StringBuilder();
        for (int c = in.read(); c != -1; c = in.read()) {
            if (letter(c)) {
                word.append((char)c);
            } else {
                out.write(word.reverse().toString());
                word.setLength(0);
                out.write(c);
            }
        }
        out.write(word.reverse().toString());
        out.flush();
    }
}
