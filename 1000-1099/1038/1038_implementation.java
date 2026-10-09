import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStream in = new BufferedInputStream(System.in);
        int errors = 0;
        // a new sentence waits for its first letter; inWord: the previous character
        // was a letter
        boolean newSentence = true, inWord = false;
        int c;
        while ((c = in.read()) != -1) {
            boolean lower = c >= 'a' && c <= 'z';
            boolean upper = c >= 'A' && c <= 'Z';
            if (lower || upper) {
                if (lower && newSentence) {
                    errors++;
                }
                if (upper && inWord) {
                    errors++;
                }
                newSentence = false;
                inWord = true;
            } else {
                inWord = false;
                if (c == '.' || c == '?' || c == '!') {
                    newSentence = true;
                }
            }
        }
        System.out.println(errors);
    }
}
