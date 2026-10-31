public class Main {
    private static final int DIGITS = 4;
    private static final long BASE = 256;

    public static void main(String[] args) throws java.io.IOException {
        // the only digits in the input belong to the one unsigned 32-bit value.
        long v = 0;
        int c;
        while ((c = System.in.read()) != -1) {
            if (c >= '0' && c <= '9') {
                v = v * 10 + c - '0';
            }
        }
        // both directions reverse the four base-256 digits, so the type does not matter.
        long sent = 0;
        for (int i = 0; i < DIGITS; i++) {
            sent = sent * BASE + v % BASE;
            v /= BASE;
        }
        System.out.println(sent);
    }
}
