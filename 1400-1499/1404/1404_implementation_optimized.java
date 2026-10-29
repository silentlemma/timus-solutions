public class Main {
    // added to the first letter
    private static final int SHIFT = 5;
    private static final int LETTERS = 26;
    private static final int MAX_LENGTH = 100;

    public static void main(String[] args) throws java.io.IOException {
        // the decoded letters and the line end go into one byte array
        byte[] plain = new byte[MAX_LENGTH + 1];
        int length = 0;
        // each code is the previous code plus the letter, modulo 26: take differences
        int previous = SHIFT;
        int ch;
        while ((ch = System.in.read()) != -1) {
            if (ch <= ' ') {
                if (length > 0) {
                    break;
                }
                continue;
            }
            int code = ch - 'a';
            plain[length++] = (byte)('a' + (code - previous + LETTERS) % LETTERS);
            previous = code;
        }
        plain[length++] = '\n';
        System.out.write(plain, 0, length);
    }
}
