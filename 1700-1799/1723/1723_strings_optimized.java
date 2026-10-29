import java.io.IOException;

public class Main {
    static final int LETTERS = 26;

    // every occurrence of a spell starts with an occurrence of its first
    // letter, so a most frequent single letter is a strongest spell
    public static void main(String[] args) throws IOException {
        int[] count = new int[LETTERS];
        int best = 0;
        // the letters are read byte by byte from System.in, with no string of the
        // whole word, and the answer is written as one byte
        int c;
        while ((c = System.in.read()) != -1) {
            if (c < 'a' || c > 'z')
                continue;
            count[c - 'a']++;
            if (count[c - 'a'] > count[best]) {
                best = c - 'a';
            }
        }
        System.out.write('a' + best);
        System.out.write('\n');
        System.out.flush();
    }
}
