public class Main {
    static final int LETTERS = 26;
    public static void main(String[] args) throws java.io.IOException {
        // The entire legal word has at most50letters, so signed byte counts fit.
        byte[] counts = new byte[LETTERS];
        int best = 0, c;
        while ((c = System.in.read()) >= 0)
            if (c >= 'a' && c <= 'z') {
                int letter = c - 'a';
                if (++counts[letter] > counts[best])
                    best = letter;
            }
        System.out.write(new byte[] {(byte)('a' + best), '\n'});
    }
}
